import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


# =========================
# CONFIG
# =========================
EVENTS_FILE = "C:/Users/jaden/OneDrive/Yale Classes/CPSC 4520/Temporal_Knowledge_Graph_GNN/data/events.2022.20230106.tab/events.2022.20230106.tab"
SEP = "/t"                    # use "\t" if your file is .tab
MAX_ROWS = None              # set to an int like 50000 if file is huge
TOP_NODES = 30               # how many nodes to show in the final graph
DATE_START = None            # e.g. "2014-01-01"
DATE_END = None              # e.g. "2014-01-31"


# =========================
# LOAD
# =========================
df = pd.read_csv(EVENTS_FILE, sep="\t", engine="python")

print("Columns found:")
print(list(df.columns))


# =========================
# FIND RELEVANT COLUMNS
# =========================
def first_existing_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    raise ValueError(f"Could not find any of these columns: {candidates}")


source_col = first_existing_column(df, [
    "Source Name", "source_name", "Source", "source"
])

target_col = first_existing_column(df, [
    "Target Name", "target_name", "Target", "target"
])

relation_col = first_existing_column(df, [
    "Event Text", "event_text",
    "Event Description", "event_description",
    "CAMEO Code Description", "cameo_code_description",
    "Event Code", "event_code",
    "CAMEO Code", "cameo_code"
])

time_col = first_existing_column(df, [
    "Event Date", "event_date", "Date", "date"
])

print("\nUsing columns:")
print("source   =", source_col)
print("target   =", target_col)
print("relation =", relation_col)
print("time     =", time_col)


# =========================
# CLEAN
# =========================
df = df.dropna(subset=[source_col, target_col, relation_col, time_col]).copy()
df[time_col] = pd.to_datetime(df[time_col], errors="coerce")
df = df.dropna(subset=[time_col])

if DATE_START is not None:
    df = df[df[time_col] >= pd.Timestamp(DATE_START)]
if DATE_END is not None:
    df = df[df[time_col] <= pd.Timestamp(DATE_END)]

print("\nRows after cleaning/filtering:", len(df))

if len(df) == 0:
    raise ValueError("No rows left after cleaning/filtering.")


# =========================
# OPTIONAL: KEEP A SMALLER,
# MORE READABLE SUBSET
# =========================
# Pick the most active nodes, then only keep edges among them.
all_nodes = pd.concat([df[source_col], df[target_col]])
top_nodes = all_nodes.value_counts().head(TOP_NODES).index.tolist()

sub = df[
    df[source_col].isin(top_nodes) &
    df[target_col].isin(top_nodes)
].copy()

# If still too big, keep only the earliest 40 edges
sub = sub.sort_values(time_col).head(40)

print("Edges in displayed subgraph:", len(sub))
print("Nodes in displayed subgraph:", len(set(sub[source_col]).union(set(sub[target_col]))))

if len(sub) == 0:
    raise ValueError("No edges remain in the chosen subgraph. Increase TOP_NODES or loosen date filters.")


# =========================
# BUILD TEMPORAL MULTIGRAPH
# =========================
# MultiDiGraph lets the same source-target pair have multiple labeled/time-stamped edges.
G = nx.MultiDiGraph()

for _, row in sub.iterrows():
    src = str(row[source_col]).strip()
    tgt = str(row[target_col]).strip()
    rel = str(row[relation_col]).strip()
    t = row[time_col]

    G.add_edge(
        src,
        tgt,
        relation=rel,
        time=t,
        label=f"{rel} @ {t.date()}"
    )


# =========================
# DRAW
# =========================
plt.figure(figsize=(16, 12))
pos = nx.spring_layout(G, seed=42, k=1.4)

# nodes
nx.draw_networkx_nodes(G, pos, node_size=2200)

# node labels
nx.draw_networkx_labels(G, pos, font_size=9)

# edges
nx.draw_networkx_edges(
    G,
    pos,
    arrows=True,
    arrowstyle="->",
    min_source_margin=15,
    min_target_margin=15,
    connectionstyle="arc3,rad=0.12",
    alpha=0.7
)

# edge labels
edge_labels = {}
for u, v, k, data in G.edges(keys=True, data=True):
    edge_labels[(u, v, k)] = data["label"]

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=7,
    rotate=False,
    label_pos=0.5
)

plt.title("ICEWS Temporal Event Graph (labeled edges with time)")
plt.axis("off")
plt.tight_layout()
plt.show()


# =========================
# PRINT EDGE TABLE TOO
# =========================
print("\nDisplayed edges:")
print(
    sub[[source_col, relation_col, target_col, time_col]]
    .sort_values(time_col)
    .to_string(index=False)
)