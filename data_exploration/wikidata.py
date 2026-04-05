import os
import json
import random
import networkx as nx
import matplotlib.pyplot as plt

# =========================
# GLOBAL CONFIG
# =========================
BASE_PATH = "../data/tkg_data/extracted/data/wiki_data/large"

SPLIT = "train.txt"

ENTITY_MAPPING_FILE = os.path.join(BASE_PATH, "entity2id.txt")
RELATION_MAPPING_FILE = os.path.join(BASE_PATH, "relation2id.txt")
TRIPLE_FILE = os.path.join(BASE_PATH, SPLIT)

ENTITY_CACHE_FILE = os.path.join(BASE_PATH, "wikidata_entity_label_cache.json")
RELATION_CACHE_FILE = os.path.join(BASE_PATH, "wikidata_relation_label_cache.json")
YEARLY_TRIPLES_JSON = os.path.join(BASE_PATH, "wiki_data_yearly_triples.json")

USE_CACHE = True

MAX_EDGES_TO_DRAW = 120
MAX_NODES_TO_DRAW = 50


# =========================
# LOAD DATA
# =========================
def load_id_mapping(path):
    """
    Reads lines like:
        Q438025    11261
        P31        15

    Returns:
        local_int_id -> raw_wikidata_id
    """
    mapping = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 2:
                continue

            raw_id = parts[0]
            local_id = int(parts[1])
            mapping[local_id] = raw_id

    return mapping

# split into triples +start_time/end_time
def load_triples(path):
    """
    Reads lines like:
        6464    5    6465    1952-##-##    1964-##-##
    Returns:
        (head, relation, tail, start, end)
    """
    triples = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 5:
                continue

            h = int(parts[0])
            r = int(parts[1])
            t = int(parts[2])
            start = parts[3]
            end = parts[4]

            triples.append((h, r, t, start, end))

    return triples


# =========================
# TIME HELPERS
# =========================
def get_year(date_str):
    try:
        return int(date_str[:4])
    except Exception:
        return None


def filter_triples_by_year(triples, year):
    active = []

    for h, r, t, start, end in triples:
        sy = get_year(start)
        ey = get_year(end)

        if sy is None or ey is None:
            continue

        if sy <= year <= ey:
            active.append((h, r, t, start, end))

    return active


def get_year_range(triples):
    min_year = None
    max_year = None

    for _, _, _, start, end in triples:
        sy = get_year(start)
        ey = get_year(end)

        if sy is None or ey is None:
            continue

        if min_year is None or sy < min_year:
            min_year = sy
        if max_year is None or ey > max_year:
            max_year = ey

    return min_year, max_year


# =========================
# CACHE HELPERS
# =========================
def load_cache(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================
# LABEL RESOLUTION
# =========================
def build_label_map(raw_map, cache_file, kind):
    """
    Returns:
        local_int_id -> display_label (either Q/P or text)
    """
    if not USE_CACHE:
        # return raw Q/P IDs (already strings like Q123, P456)
        return dict(raw_map)

    cache = load_cache(cache_file)

    return {
        local_id: cache.get(raw_id, raw_id)  # fallback to Q/P if missing
        for local_id, raw_id in raw_map.items()
    }


# =========================
# YEARLY JSON
# =========================
def build_yearly_triples_json(triples, out_path, entity_label_map, relation_label_map):
    min_year, max_year = get_year_range(triples)

    if min_year is None or max_year is None:
        raise ValueError("Could not determine year range from triples.")

    yearly = {}

    print(f"\nBuilding yearly triple JSON from {min_year} to {max_year}...")

    for year in range(min_year, max_year + 1):
        active = filter_triples_by_year(triples, year)

        yearly[str(year)] = [
            {
                "head": entity_label_map.get(h, str(h)),
                "relation": relation_label_map.get(r, str(r)),
                "tail": entity_label_map.get(t, str(t)),
                "start": start,
                "end": end,
            }
            for h, r, t, start, end in active
        ]

        if year == min_year or year == max_year or year % 25 == 0:
            print(f"  year {year}: {len(active)} active triples")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(yearly, f, indent=2)

    print(f"Saved yearly triples JSON to: {out_path}")
    return yearly


# =========================
# GRAPHING
# =========================
def build_graph(triples, entity_label_map, relation_label_map):
    G = nx.Graph()

    triples_to_draw = triples
    if len(triples_to_draw) > MAX_EDGES_TO_DRAW:
        triples_to_draw = random.sample(triples_to_draw, MAX_EDGES_TO_DRAW)

    for h, r, t, start, end in triples_to_draw:
        h_text = h
        t_text = t
        r_text = r

        edge_label = f"{r_text}\n[{start[:4]}–{end[:4]}]"
        G.add_edge(h_text, t_text, relation=edge_label)

    return G


def largest_component(G):
    if G.number_of_nodes() == 0:
        return G

    comp = max(nx.connected_components(G), key=len)
    G_sub = G.subgraph(comp).copy()

    if G_sub.number_of_nodes() > MAX_NODES_TO_DRAW:
        nodes = list(G_sub.nodes())[:MAX_NODES_TO_DRAW]
        G_sub = G_sub.subgraph(nodes).copy()

    return G_sub


def visualize(G, title):
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, alpha=0.6)
    nx.draw_networkx_labels(G, pos, font_size=7)

    edge_labels = nx.get_edge_attributes(G, "relation")
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=6,
        rotate=False,
    )

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# =========================
# MAIN
# =========================
def main():
    entity_raw_map = load_id_mapping(ENTITY_MAPPING_FILE)
    relation_raw_map = load_id_mapping(RELATION_MAPPING_FILE)
    triples = load_triples(TRIPLE_FILE)

    print(f"Loaded {len(entity_raw_map)} entities")
    print(f"Loaded {len(relation_raw_map)} relations")
    print(f"Loaded {len(triples)} triples from {SPLIT}")

    entity_label_map = build_label_map(
        entity_raw_map,
        ENTITY_CACHE_FILE,
        kind="entity"
    )
    relation_label_map = build_label_map(
        relation_raw_map,
        RELATION_CACHE_FILE,
        kind="relation"
    )

    yearly = build_yearly_triples_json(
        triples,
        YEARLY_TRIPLES_JSON,
        entity_label_map,
        relation_label_map,
    )

    for year in [2000, 2001]:
        if str(year) not in yearly:
            print(f"Year {year} not present in yearly JSON.")
            continue

        year_triples = [
            (
                item["head"],
                item["relation"],
                item["tail"],
                item["start"],
                item["end"],
            )
            for item in yearly[str(year)]
        ]

        print(f"\nYear {year}: {len(year_triples)} active triples")

        G = build_graph(year_triples, entity_label_map, relation_label_map)
        G = largest_component(G)

        print(f"Graph for {year}: {len(G.nodes())} nodes, {len(G.edges())} edges")
        visualize(G, f"wiki_data {SPLIT} snapshot at year {year}")


if __name__ == "__main__":
    main()