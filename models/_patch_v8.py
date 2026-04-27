"""
One-shot patcher: edits deltas_v8.ipynb in place to fix:
  (1) addition-head ranking eval — replace tiny proposal-union pool with
      proper filtered ranking against many random tail-corruptions per positive
      (gives meaningful MRR + Hits@1/3/10).
  (2) addition-head training negatives — augment proposer-only negatives with
      random hard negatives sampled outside (current ∪ next) so the head learns
      a real ranking signal, not a proposer-relative one.
  (3) deletion-head ranking eval — same filtered protocol against random
      "would-keep" candidates so deletion Hits@k are no longer trivially 1.0.

Run once:  python models/_patch_v8.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

NB_PATH = Path(__file__).resolve().parent / "deltas_v8.ipynb"


def cell_source(cell) -> str:
    return cell["source"] if isinstance(cell["source"], str) else "".join(cell["source"])


def set_cell_source(cell, new_text: str) -> None:
    cell["source"] = new_text.splitlines(keepends=True)


def replace_once(text: str, needle: str, replacement: str, label: str) -> str:
    if needle not in text:
        raise SystemExit(f"PATCH FAILED: needle for '{label}' not found")
    if text.count(needle) != 1:
        raise SystemExit(f"PATCH FAILED: needle for '{label}' is non-unique")
    return text.replace(needle, replacement)


# ---------------------------------------------------------------------------
# Patch fragments
# ---------------------------------------------------------------------------

# Inserted at the end of cell 4: filtered ranking helpers used by validate().
RANKING_HELPERS = '''


# Sample triples that are NOT in `forbidden` — used as negatives for filtered ranking.
def _sample_filtered_negatives(
    src,
    rel,
    num_negatives,
    num_nodes,
    forbidden,
    rng,
):
    # Collect at most num_negatives unique tail-corruptions (src, rel, o') with o' != src and o' unseen.
    negatives = []
    seen = set()
    attempts = 0
    max_attempts = num_negatives * 20 + 50
    while len(negatives) < num_negatives and attempts < max_attempts:
        o_prime = rng.randrange(num_nodes)
        cand = (src, rel, o_prime)
        if o_prime != src and cand not in forbidden and cand not in seen:
            negatives.append(cand)
            seen.add(cand)
        attempts += 1
    return negatives


# Compute filtered MRR + Hits@k for the addition head.
# For each true addition (s, r, o), score (s, r, o) plus K random tail-corruptions
# sampled from outside (current_set ∪ next_set) and rank the positive.
def filtered_ranking_addition(
    model,
    graph_states,
    memory_states,
    history_cache,
    timestep,
    added_triples,
    current_set,
    next_set,
    num_nodes,
    num_negatives,
    device,
    rng,
):
    # Skip when there are no positives at this step.
    if len(added_triples) == 0:
        return None

    # Anything in current OR next that is NOT the positive itself is filtered out
    # so we don't penalize the model for ranking another genuine triple high.
    forbidden = current_set | next_set

    rec_ranks = []
    hits1 = hits3 = hits10 = 0
    pos_count = 0

    for positive in added_triples:
        src, rel, dst = positive

        # Build the candidate list: [positive, neg_1, ..., neg_K].
        negatives = _sample_filtered_negatives(
            src, rel, num_negatives, num_nodes, forbidden, rng,
        )
        if len(negatives) == 0:
            continue

        candidates = [positive] + negatives

        # Score every candidate with the addition head, including history features.
        candidate_tensor = triples_to_tensor(candidates, device, sort_output=False)
        history_features = history_cache.build_feature_tensor(
            candidates, timestep=timestep, device=device,
        )
        logits = model.addition_scorer(
            graph_states, memory_states, candidate_tensor,
            history_features=history_features,
        )

        # Rank with a tie-breaking rule that adds 0.5 for ties (standard TKG eval).
        pos_score = logits[0]
        neg_scores = logits[1:]
        higher = (neg_scores > pos_score).sum().item()
        equal = (neg_scores == pos_score).sum().item()
        rank = higher + 1 + equal * 0.5

        rec_ranks.append(1.0 / rank)
        if rank <= 1: hits1 += 1
        if rank <= 3: hits3 += 1
        if rank <= 10: hits10 += 1
        pos_count += 1

    if pos_count == 0:
        return None
    return {
        "mrr": float(sum(rec_ranks) / pos_count),
        "hits@1": hits1 / pos_count,
        "hits@3": hits3 / pos_count,
        "hits@10": hits10 / pos_count,
        "count": float(pos_count),
    }


# Compute filtered MRR + Hits@k for the deletion head.
# For each truly deleted edge (s, r, o), rank it against K random *surviving* edges
# from the current graph — i.e. ask "does the deletion head place the truly
# removed edge above edges that should remain?"
def filtered_ranking_deletion(
    model,
    graph_states,
    memory_states,
    deletion_logits_full,
    deletion_labels_full,
    num_negatives,
    rng,
):
    # deletion_logits_full and deletion_labels_full cover EVERY current edge.
    pos_indices = (deletion_labels_full > 0.5).nonzero(as_tuple=False).flatten().tolist()
    neg_indices = (deletion_labels_full < 0.5).nonzero(as_tuple=False).flatten().tolist()
    if len(pos_indices) == 0 or len(neg_indices) == 0:
        return None

    rec_ranks = []
    hits1 = hits3 = hits10 = 0

    sample_size = min(num_negatives, len(neg_indices))
    for pos_idx in pos_indices:
        sampled = rng.sample(neg_indices, sample_size) if sample_size < len(neg_indices) else neg_indices
        pos_score = deletion_logits_full[pos_idx]
        neg_scores = deletion_logits_full[sampled]
        higher = (neg_scores > pos_score).sum().item()
        equal = (neg_scores == pos_score).sum().item()
        rank = higher + 1 + equal * 0.5

        rec_ranks.append(1.0 / rank)
        if rank <= 1: hits1 += 1
        if rank <= 3: hits3 += 1
        if rank <= 10: hits10 += 1

    n = len(pos_indices)
    return {
        "mrr": float(sum(rec_ranks) / n),
        "hits@1": hits1 / n,
        "hits@3": hits3 / n,
        "hits@10": hits10 / n,
        "count": float(n),
    }
'''


# Replacement for the negative sampling section inside build_addition_training_batch.
ADDITION_NEG_OLD = '''    # Build the pool of proposal negatives that are not true additions.
    negative_pool = sorted(proposal_set - added_set)

    # Sample the requested number of negatives.
    negative_triples = sample_without_replacement(
        negative_pool,
        min(len(negative_pool), len(positive_triples) * negatives_per_positive),
    )
'''

ADDITION_NEG_NEW = '''    # Build the pool of proposal-derived negatives that are not true additions.
    proposal_neg_pool = sorted(proposal_set - added_set)

    # Decide how many negatives we want in total.
    target_neg_count = len(positive_triples) * negatives_per_positive

    # Take up to half of them from the proposer pool — those are "hard" structurally-plausible negatives.
    proposal_share = min(len(proposal_neg_pool), target_neg_count // 2)
    proposal_neg_triples = sample_without_replacement(proposal_neg_pool, proposal_share)

    # Fill the rest with truly random tail-corruptions outside (current ∪ next).
    # This breaks the proposer-relative training distribution so the addition
    # head learns absolute "is this triple plausible at t+1" scoring.
    forbidden_for_random = added_set | set(proposal_neg_triples)
    if current_triples is not None:
        forbidden_for_random = forbidden_for_random | set(current_triples)
    random_share = target_neg_count - len(proposal_neg_triples)
    random_neg_triples = []
    if random_share > 0 and num_nodes is not None and num_relations is not None:
        rng = random.Random()
        seen_random = set()
        attempts = 0
        max_attempts = random_share * 20 + 50
        while len(random_neg_triples) < random_share and attempts < max_attempts:
            s = rng.randrange(num_nodes)
            r = rng.randrange(num_relations)
            o = rng.randrange(num_nodes)
            cand = (s, r, o)
            if s != o and cand not in forbidden_for_random and cand not in seen_random:
                random_neg_triples.append(cand)
                seen_random.add(cand)
            attempts += 1

    # Concatenate the two negative streams; preserve a stable order.
    negative_triples = list(proposal_neg_triples) + list(random_neg_triples)
'''


# Signature change for build_addition_training_batch: pass current_triples + num_nodes + num_relations.
ADDITION_SIG_OLD = '''def build_addition_training_batch(
    added_triples: Sequence[Triple],
    add_proposals: torch.Tensor,
    history_cache: TemporalHistoryCache,
    timestep: int,
    sample_size: int,
    device: torch.device,
    negatives_per_positive: int = 1,
):'''

ADDITION_SIG_NEW = '''def build_addition_training_batch(
    added_triples: Sequence[Triple],
    add_proposals: torch.Tensor,
    history_cache: TemporalHistoryCache,
    timestep: int,
    sample_size: int,
    device: torch.device,
    negatives_per_positive: int = 1,
    current_triples: Optional[Sequence[Triple]] = None,
    num_nodes: Optional[int] = None,
    num_relations: Optional[int] = None,
):'''


# Train-epoch caller passes the new args through.
TRAIN_CALL_OLD = '''        # Build the addition batch and compute proposer recall for this transition.
        addition_batch, proposal_recall = build_addition_training_batch(
            added_triples=added_triples,
            add_proposals=add_proposals,
            history_cache=history_cache,
            timestep=t,
            sample_size=sample_size,
            device=device,
            negatives_per_positive=NEGATIVES_PER_POSITIVE,
        )'''

TRAIN_CALL_NEW = '''        # Build the addition batch and compute proposer recall for this transition.
        addition_batch, proposal_recall = build_addition_training_batch(
            added_triples=added_triples,
            add_proposals=add_proposals,
            history_cache=history_cache,
            timestep=t,
            sample_size=sample_size,
            device=device,
            negatives_per_positive=NEGATIVES_PER_POSITIVE,
            current_triples=current_triples,
            num_nodes=dataset.num_nodes,
            num_relations=model.num_relations,
        )'''


# Replace the validate function's addition-head + deletion-head metric blocks.
VALIDATE_ADDITION_OLD = '''        # Build the evaluation pool as proposals union gold positives so scorer quality is measurable even when recall is imperfect.
        eval_pool_triples = sorted(proposal_set | added_set)

        # Evaluate the addition head when the pool is non-empty.
        if len(eval_pool_triples) > 0:
            addition_candidates = triples_to_tensor(eval_pool_triples, device, sort_output=False)
            addition_labels = binary_labels_from_positive_set(eval_pool_triples, added_set, device)
            addition_history_features = history_cache.build_feature_tensor(
                eval_pool_triples,
                timestep=t,
                device=device,
            )
            addition_logits = model.addition_scorer(
                graph_states,
                memory_states,
                addition_candidates,
                history_features=addition_history_features,
            )
            addition_loss = F.binary_cross_entropy_with_logits(addition_logits, addition_labels)
            total_add_loss += float(addition_loss.item())
            add_eval_steps += 1
            addition_stats = oracle_topn_statistics(addition_logits, addition_labels.bool())
            total_add_hits1 += addition_stats["hits@1"]
            total_add_hits3 += addition_stats["hits@3"]
            total_add_hits10 += addition_stats["hits@10"]
            total_add_positive_count += addition_stats["count"]
            add_tp += addition_stats["tp"]
            add_fp += addition_stats["fp"]
            add_fn += addition_stats["fn"]'''

VALIDATE_ADDITION_NEW = '''        # Compute BCE loss on the proposer pool (kept for diagnostic continuity with v7).
        eval_pool_triples = sorted(proposal_set | added_set)
        if len(eval_pool_triples) > 0:
            addition_candidates = triples_to_tensor(eval_pool_triples, device, sort_output=False)
            addition_labels = binary_labels_from_positive_set(eval_pool_triples, added_set, device)
            addition_history_features = history_cache.build_feature_tensor(
                eval_pool_triples, timestep=t, device=device,
            )
            addition_logits = model.addition_scorer(
                graph_states, memory_states, addition_candidates,
                history_features=addition_history_features,
            )
            addition_loss = F.binary_cross_entropy_with_logits(addition_logits, addition_labels)
            total_add_loss += float(addition_loss.item())
            add_eval_steps += 1
            addition_stats = oracle_topn_statistics(addition_logits, addition_labels.bool())
            add_tp += addition_stats["tp"]
            add_fp += addition_stats["fp"]
            add_fn += addition_stats["fn"]

        # Filtered ranking against random tail-corruptions — this is the honest forecasting metric.
        ranking = filtered_ranking_addition(
            model=model,
            graph_states=graph_states,
            memory_states=memory_states,
            history_cache=history_cache,
            timestep=t,
            added_triples=list(added_set),
            current_set=current_set,
            next_set=set(next_triples),
            num_nodes=dataset.num_nodes,
            num_negatives=FILTERED_NEGATIVES_PER_POSITIVE,
            device=device,
            rng=_validation_rng,
        )
        if ranking is not None:
            total_add_mrr += ranking["mrr"] * ranking["count"]
            total_add_hits1 += ranking["hits@1"] * ranking["count"]
            total_add_hits3 += ranking["hits@3"] * ranking["count"]
            total_add_hits10 += ranking["hits@10"] * ranking["count"]
            total_add_positive_count += ranking["count"]'''


VALIDATE_DELETION_OLD = '''            deletion_stats = oracle_topn_statistics(deletion_logits, deletion_labels.bool())
            total_del_hits1 += deletion_stats["hits@1"]
            total_del_hits3 += deletion_stats["hits@3"]
            total_del_hits10 += deletion_stats["hits@10"]
            total_del_positive_count += deletion_stats["count"]
            del_tp += deletion_stats["tp"]
            del_fp += deletion_stats["fp"]
            del_fn += deletion_stats["fn"]'''

VALIDATE_DELETION_NEW = '''            deletion_stats = oracle_topn_statistics(deletion_logits, deletion_labels.bool())
            del_tp += deletion_stats["tp"]
            del_fp += deletion_stats["fp"]
            del_fn += deletion_stats["fn"]

            del_ranking = filtered_ranking_deletion(
                model=model,
                graph_states=graph_states,
                memory_states=memory_states,
                deletion_logits_full=deletion_logits,
                deletion_labels_full=deletion_labels,
                num_negatives=FILTERED_NEGATIVES_PER_POSITIVE,
                rng=_validation_rng,
            )
            if del_ranking is not None:
                total_del_mrr += del_ranking["mrr"] * del_ranking["count"]
                total_del_hits1 += del_ranking["hits@1"] * del_ranking["count"]
                total_del_hits3 += del_ranking["hits@3"] * del_ranking["count"]
                total_del_hits10 += del_ranking["hits@10"] * del_ranking["count"]
                total_del_positive_count += del_ranking["count"]'''


VALIDATE_TRACK_OLD = '''    # Track cumulative deletion hits@1.
    total_del_hits1 = 0.0'''

VALIDATE_TRACK_NEW = '''    # Track cumulative deletion MRR (weighted by positive count per step).
    total_del_mrr = 0.0

    # Track cumulative deletion hits@1.
    total_del_hits1 = 0.0'''


VALIDATE_ADD_TRACK_OLD = '''    # Track cumulative addition hits@1.
    total_add_hits1 = 0.0'''

VALIDATE_ADD_TRACK_NEW = '''    # Track cumulative addition MRR (weighted by positive count per step).
    total_add_mrr = 0.0

    # Track cumulative addition hits@1.
    total_add_hits1 = 0.0'''


VALIDATE_RNG_OLD = '''    # Initialize the explicit sparse history cache used by the addition head.
    history_cache = TemporalHistoryCache(recent_window=HISTORY_RECENT_WINDOW)

    # Track cumulative deletion loss.'''

VALIDATE_RNG_NEW = '''    # Initialize the explicit sparse history cache used by the addition head.
    history_cache = TemporalHistoryCache(recent_window=HISTORY_RECENT_WINDOW)

    # Use a deterministic RNG for filtered-ranking negative sampling so val numbers are reproducible.
    _validation_rng = random.Random(20260425)

    # Track cumulative deletion loss.'''


VALIDATE_RETURN_OLD = '''    # Return a small dictionary of validation metrics.
    return {
        "del_loss": total_del_loss / max(del_eval_steps, 1),
        "add_loss": total_add_loss / max(add_eval_steps, 1),
        "del_hits@1": total_del_hits1 / max(total_del_positive_count, 1.0),
        "del_hits@3": total_del_hits3 / max(total_del_positive_count, 1.0),
        "del_hits@10": total_del_hits10 / max(total_del_positive_count, 1.0),
        "add_hits@1": total_add_hits1 / max(total_add_positive_count, 1.0),
        "add_hits@3": total_add_hits3 / max(total_add_positive_count, 1.0),
        "add_hits@10": total_add_hits10 / max(total_add_positive_count, 1.0),
        "del_precision": del_precision,
        "del_recall": del_recall,
        "del_f1": del_f1,
        "add_precision": add_precision,
        "add_recall": add_recall,
        "add_f1": add_f1,
        "add_proposal_recall": total_add_proposal_recall / max(add_proposal_steps, 1),
    }'''

VALIDATE_RETURN_NEW = '''    # Return a small dictionary of validation metrics.
    return {
        "del_loss": total_del_loss / max(del_eval_steps, 1),
        "add_loss": total_add_loss / max(add_eval_steps, 1),
        "del_mrr": total_del_mrr / max(total_del_positive_count, 1.0),
        "add_mrr": total_add_mrr / max(total_add_positive_count, 1.0),
        "del_hits@1": total_del_hits1 / max(total_del_positive_count, 1.0),
        "del_hits@3": total_del_hits3 / max(total_del_positive_count, 1.0),
        "del_hits@10": total_del_hits10 / max(total_del_positive_count, 1.0),
        "add_hits@1": total_add_hits1 / max(total_add_positive_count, 1.0),
        "add_hits@3": total_add_hits3 / max(total_add_positive_count, 1.0),
        "add_hits@10": total_add_hits10 / max(total_add_positive_count, 1.0),
        "del_precision": del_precision,
        "del_recall": del_recall,
        "del_f1": del_f1,
        "add_precision": add_precision,
        "add_recall": add_recall,
        "add_f1": add_f1,
        "add_proposal_recall": total_add_proposal_recall / max(add_proposal_steps, 1),
    }'''


# A small constants block we add right before train_epoch so both build_..._batch
# and validate can use the same setting.
CONSTANTS_BLOCK = '''
# Number of random tail-corruptions per positive used by filtered ranking.
# Larger -> tighter Hits@k bounds but slower validation.
FILTERED_NEGATIVES_PER_POSITIVE = 200


'''


def main() -> int:
    if not NB_PATH.exists():
        print(f"missing notebook: {NB_PATH}", file=sys.stderr)
        return 1

    with NB_PATH.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    # ---- cell 4: append filtered ranking helpers ---------------------------
    cell4 = nb["cells"][4]
    src4 = cell_source(cell4)
    if "filtered_ranking_addition" in src4:
        print("cell 4 already patched, skipping")
    else:
        set_cell_source(cell4, src4 + RANKING_HELPERS)
        print("cell 4 patched: ranking helpers appended")

    # ---- cell 8: signature, neg pool, train call, validate ----------------
    cell8 = nb["cells"][8]
    src8 = cell_source(cell8)

    if "FILTERED_NEGATIVES_PER_POSITIVE" not in src8:
        # insert the constants block immediately before "# Train the model for one epoch."
        marker = "# Train the model for one epoch."
        src8 = replace_once(src8, marker, CONSTANTS_BLOCK + marker, "constants block")

    if "current_triples: Optional[Sequence[Triple]] = None" not in src8:
        src8 = replace_once(src8, ADDITION_SIG_OLD, ADDITION_SIG_NEW, "addition batch signature")

    if "proposal_neg_pool" not in src8:
        src8 = replace_once(src8, ADDITION_NEG_OLD, ADDITION_NEG_NEW, "addition neg pool")

    if "num_nodes=dataset.num_nodes" not in src8:
        src8 = replace_once(src8, TRAIN_CALL_OLD, TRAIN_CALL_NEW, "train_epoch call")

    if "filtered_ranking_addition(" not in src8:
        src8 = replace_once(src8, VALIDATE_ADDITION_OLD, VALIDATE_ADDITION_NEW, "validate addition")

    if "filtered_ranking_deletion(" not in src8:
        src8 = replace_once(src8, VALIDATE_DELETION_OLD, VALIDATE_DELETION_NEW, "validate deletion")

    if "total_del_mrr" not in src8:
        src8 = replace_once(src8, VALIDATE_TRACK_OLD, VALIDATE_TRACK_NEW, "validate del track")

    if "total_add_mrr" not in src8:
        src8 = replace_once(src8, VALIDATE_ADD_TRACK_OLD, VALIDATE_ADD_TRACK_NEW, "validate add track")

    if "_validation_rng = random.Random" not in src8:
        src8 = replace_once(src8, VALIDATE_RNG_OLD, VALIDATE_RNG_NEW, "validate rng init")

    if '"del_mrr"' not in src8:
        src8 = replace_once(src8, VALIDATE_RETURN_OLD, VALIDATE_RETURN_NEW, "validate return dict")

    set_cell_source(cell8, src8)
    print("cell 8 patched: training negatives + filtered ranking eval")

    # ---- save -------------------------------------------------------------
    with NB_PATH.open("w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)

    print(f"wrote {NB_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
