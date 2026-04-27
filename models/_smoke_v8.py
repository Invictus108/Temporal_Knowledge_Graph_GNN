"""
Smoke test for the patched v8 model code.

Loads cells 2..8 from deltas_v8.ipynb, execs them in a fresh namespace,
loads the small 2ent_5rel synthetic dataset, builds the model on CPU with
a tiny config, and runs ONE training epoch + ONE validation pass. This
exists purely to catch import-time / shape / signature errors introduced
by the patch — it is not a quality measurement.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "data_exploration"))

NB = ROOT / "models" / "deltas_v8.ipynb"
SYN = ROOT / "data_exploration" / "synthetic_data" / "2ent_5rel.json"


def collect_code_cells(nb_path: Path, indices) -> str:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    chunks = []
    for i in indices:
        cell = nb["cells"][i]
        src = cell["source"]
        if isinstance(src, list):
            src = "".join(src)
        chunks.append(f"# === cell {i} ===\n" + src)
    return "\n\n".join(chunks)


def main() -> int:
    print("loading notebook code (cells 2..8) ...")
    body = collect_code_cells(NB, [2, 4, 5, 6, 7, 8])

    ns: dict = {"__name__": "smoke_v8"}
    exec(compile(body, str(NB) + ":<cells 2..8>", "exec"), ns)

    print("importing synthetic dataset ...")
    from synthetic_dataset_class import SyntheticTemporalGraphDataset
    dataset = SyntheticTemporalGraphDataset.from_json(SYN)
    print(f"  timesteps: {len(dataset)}")
    print(f"  num_nodes: {dataset.num_nodes}")
    print(f"  num_rels:  {len(dataset.id_to_rel)}")

    import torch
    device = torch.device("cpu")

    TemporalDeltaModel = ns["TemporalDeltaModel"]
    train_epoch = ns["train_epoch"]
    validate = ns["validate"]
    HISTORY_RECENT_WINDOW = 8

    # constants are read out of the notebook namespace where possible
    ns["HISTORY_RECENT_WINDOW"] = HISTORY_RECENT_WINDOW
    ns["NEGATIVES_PER_POSITIVE"] = 2

    model = TemporalDeltaModel(
        in_dim=dataset.x_global.shape[1],
        hidden_dim=16,
        relation_dim=8,
        num_relations=len(dataset.id_to_rel),
        num_gnn_layers=1,
        heads=2,
        dropout=0.0,
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)

    # If the dataset is short, validate on the very last 1-2 transitions only.
    val_steps = max(1, min(2, len(dataset) // 4))
    train_end = len(dataset) - val_steps

    print(f"smoke-running 1 epoch | train_end={train_end} val_steps={val_steps}")
    train_metrics = train_epoch(
        model=model,
        dataset=dataset,
        optimizer=optimizer,
        device=device,
        train_end=train_end,
        sample_size=8,
        proposal_target_count=32,
        bptt_steps=4,
        history_len=4,
    )
    print(f"train_metrics: {train_metrics}")

    val_metrics = validate(
        model=model,
        dataset=dataset,
        device=device,
        val_start=train_end,
        proposal_target_count=32,
        history_len=4,
    )
    print("val_metrics:")
    for k, v in val_metrics.items():
        print(f"  {k:24s} {v}")

    needed = ["add_mrr", "del_mrr", "add_hits@10", "del_hits@10"]
    missing = [k for k in needed if k not in val_metrics]
    if missing:
        print(f"FAIL: missing keys: {missing}")
        return 1
    print("OK: all new ranking keys present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
