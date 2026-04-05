import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
 
ACTORS_CSV = "../data/icews.actors.20181119.csv"
AGENTS_CSV = "../data/icews.agents.20140112.csv"
SECTORS_CSV = "../data/icews.sectors.20140112.csv"



# =========================
# HELPERS
# =========================
def first_existing_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    raise ValueError(f"None of these columns were found: {candidates}")


def split_multi_value(cell):
    if pd.isna(cell):
        return []
    s = str(cell).strip()
    if not s:
        return []
    return [x.strip() for x in s.split("||") if x.strip()]


# =========================
# LOAD CSVS
# =========================
actors = pd.read_csv(ACTORS_CSV)
agents = pd.read_csv(AGENTS_CSV)
sectors = pd.read_csv(SECTORS_CSV, header=None)

print("Actors columns:", list(actors.columns))
print("Agents columns:", list(agents.columns))
print("Sectors shape:", sectors.shape)


# =========================
# IDENTIFY COLUMNS
# =========================
actor_name_col = first_existing_column(
    actors, ["Actor Name", "actor_name", "Name", "Actor"]
)
actor_affil_col = first_existing_column(
    actors, ["Affiliation To", "affiliation_to", "Affiliation", "Sector"]
)

agent_name_col = first_existing_column(
    agents, ["Agent Name", "agent_name", "Name", "Agent"]
)
agent_sector_col = first_existing_column(
    agents, ["Sectors", "sectors", "Sector"]
)


# =========================
# BUILD GRAPH
# =========================
G = nx.DiGraph()

# ---- 1) Sector hierarchy ----
# The sectors file is an indented tree encoded by blank columns. :contentReference[oaicite:1]{index=1}
stack = []

for row in sectors.itertuples(index=False):
    values = list(row)

    nonempty_idx = None
    for i, v in enumerate(values):
        if pd.notna(v) and str(v).strip() != "":
            nonempty_idx = i
            break

    if nonempty_idx is None:
        continue

    level = nonempty_idx
    sector_name = str(values[level]).strip()

    G.add_node(sector_name, node_type="sector")

    if len(stack) > level:
        stack = stack[:level]

    if stack:
        parent = stack[-1]
        G.add_edge(parent, sector_name, edge_type="sector_parent_of")

    stack.append(sector_name)


# ---- 2) Actors and their affiliations ----
# Actor rows may represent affiliations either to sectors or to other actors. :contentReference[oaicite:2]{index=2}
for _, row in actors.iterrows():
    actor = str(row[actor_name_col]).strip()
    if not actor or actor.lower() == "nan":
        continue

    G.add_node(actor, node_type="actor")

    affiliations = split_multi_value(row[actor_affil_col])
    for aff in affiliations:
        if not aff:
            continue

        if aff in G.nodes and G.nodes[aff].get("node_type") == "sector":
            G.add_edge(actor, aff, edge_type="actor_affiliated_with_sector")
        else:
            G.add_node(aff, node_type="actor_or_group")
            G.add_edge(actor, aff, edge_type="actor_affiliated_with_actor")


# ---- 3) Agents and their sectors ----
# Agents can belong to one or more sectors, with values delimited by ||. :contentReference[oaicite:3]{index=3}
for _, row in agents.iterrows():
    agent = str(row[agent_name_col]).strip()
    if not agent or agent.lower() == "nan":
        continue

    G.add_node(agent, node_type="agent")

    sector_list = split_multi_value(row[agent_sector_col])
    for sec in sector_list:
        G.add_node(sec, node_type="sector")
        G.add_edge(agent, sec, edge_type="agent_in_sector")


# =========================
# SUMMARY
# =========================
print("\n=== Graph summary ===")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

node_type_counts = {}
for _, data in G.nodes(data=True):
    t = data.get("node_type", "unknown")
    node_type_counts[t] = node_type_counts.get(t, 0) + 1

print("\nNode types:")
for k, v in sorted(node_type_counts.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")


edge_type_counts = {}
for _, _, data in G.edges(data=True):
    t = data.get("edge_type", "unknown")
    edge_type_counts[t] = edge_type_counts.get(t, 0) + 1

print("\nEdge types:")
for k, v in sorted(edge_type_counts.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")


# =========================
# DISPLAY A MANAGEABLE SUBGRAPH
# =========================
# Full ICEWS graph is too large to draw directly, so keep the highest-degree nodes.
top_k = 80
top_nodes = [n for n, _ in sorted(G.degree, key=lambda x: x[1], reverse=True)[:top_k]]
H = G.subgraph(top_nodes).copy()

print(f"\nDisplaying subgraph with {H.number_of_nodes()} nodes and {H.number_of_edges()} edges")

plt.figure(figsize=(14, 10))
pos = nx.spring_layout(H, seed=42, k=0.7)

nx.draw_networkx_nodes(H, pos, node_size=500)
nx.draw_networkx_edges(H, pos, arrows=True, alpha=0.5)
nx.draw_networkx_labels(H, pos, font_size=8)

plt.title("ICEWS Dictionary Graph (top-degree subgraph)")
plt.axis("off")
plt.tight_layout()
plt.show()