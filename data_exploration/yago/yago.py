import os
import random
import networkx as nx
import matplotlib.pyplot as plt

# =========================
# GLOBAL CONFIG
# =========================
BASE_PATH = "../../data/tkg_data/extracted/data"

DATASET = "yago"   # "wiki_data" or "yago"
SPLIT = "train.txt"     # train.txt / test.txt / valid.txt

MAX_EDGES = 1000
MAX_NODES = 200


# =========================
# LOAD MAPPINGS
# =========================
def load_mapping(path):
    mapping = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                name = parts[0]
                idx = int(parts[1])
                mapping[idx] = name
    return mapping


# =========================
# LOAD TRIPLES
# =========================
def load_triples(path):
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
# BUILD GRAPH
# =========================
def build_graph(triples, entity_map, relation_map):
    G = nx.Graph()

    # sample to keep it readable
    if len(triples) > MAX_EDGES:
        triples = random.sample(triples, MAX_EDGES)

    for h, r, t, st, et in triples:
        h_name = entity_map.get(h, str(h))
        t_name = entity_map.get(t, str(t))
        r_name = relation_map.get(r, str(r))

        G.add_edge(h_name, t_name, relation=r_name)

    return G


# =========================
# GET LARGEST COMPONENT
# =========================
def largest_component(G):
    if len(G.nodes) == 0:
        return G

    comp = max(nx.connected_components(G), key=len)
    G_sub = G.subgraph(comp).copy()

    if len(G_sub.nodes) > MAX_NODES:
        nodes = list(G_sub.nodes)[:MAX_NODES]
        G_sub = G_sub.subgraph(nodes).copy()

    return G_sub


# =========================
# VISUALIZE
# =========================
def visualize(G, title):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=500, font_size=8)

    edge_labels = nx.get_edge_attributes(G, "relation")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    plt.title(title)
    plt.show()


# =========================
# MAIN
# =========================
def main():
    dataset_path = BASE_PATH + "/" + DATASET

    entity_path = dataset_path + "/large/entity2id.txt"
    relation_path = dataset_path + "/large/relation2id.txt"

    entity_map = load_mapping(entity_path)
    relation_map = load_mapping(relation_path)

    triples = load_triples(dataset_path + "/large/" + SPLIT)

    print(f"Loaded {len(triples)} triples")

    G = build_graph(triples, entity_map, relation_map)
    G = largest_component(G)

    print(f"Graph: {len(G.nodes)} nodes, {len(G.edges)} edges")

    visualize(G, f"{DATASET} - {SPLIT}")


if __name__ == "__main__":
    main()