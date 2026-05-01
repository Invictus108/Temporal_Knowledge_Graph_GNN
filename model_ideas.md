# Model Ideas

## Goal

The model should predict new edges and removed edges in a graph over time. The core direction is to combine an attention-based graph neural network with a recurrent model such as an LSTM.

The model uses a global node pool. Some nodes may be disconnected in a given timestep.

## Node and Relation Representation

### Relation Embeddings

Relations should be limited to a manageable subset and learned by the model. Example relations include `born`, `died`, `friends`, `enemies`, and `killed_by`.

### Node Text Options

Two options were considered.

#### One-Hot Encoding

Pros:

- Easy decoding rule: take a softmax and sample probabilities.
- Easy to implement with an `nn.Embedding` layer.

Cons:

- Less representative and likely worse for model quality.
- Can become large quickly because the data contains many proper nouns.

#### Text Embedding Layer

Generate separate embeddings for:

- name
- description
- class or type

Then merge those embeddings inside the model.

Pros:

- Much more representative.
- More manageable dimensionality.

Cons:

- Harder to implement.
- Imported embedding models may struggle with many proper nouns.
- Adding custom embedding layers makes the model more expensive.

The preferred approach is to use pretrained embeddings of names, classes, and descriptions. An embedding head then synthesizes those vectors and projects them into the GNN hidden dimension.

## Graph Encoder

The graph encoder should use an attention-style message passing rule:

```text
h(t + 1)_i = nonlinearity(sum_j a_ij * m_ij)
```

The attention score is:

```text
a_score_ij = nonlinearity(a(z_i, z_j, edge_ij))
z = W_n * h
```

The score is computed only over neighbors and normalized with softmax.

Messages combine the neighbor hidden state and the relation embedding:

```text
m_ij = W_h * h(t)_j + W_r * edge_ij
```

Multi-head attention can be added after the single-head version works.

## Stabilization

Layer normalization, residual connections, feed-forward layers, and dropout are likely useful:

```text
h(t + 1) = GNNLayer(h(t))
h(t + 1) = LayerNorm(h(t + 1) + h(t))
h(t + 1) = LayerNorm(h(t + 1) + MLP(h(t + 1)))
```

## LSTM State Strategies

### Full-Graph State

Use a graph readout:

```text
x = ReadOut(H)
```

The readout could use attention pooling, optionally conditioned on the LSTM hidden state. This captures global graph patterns but loses fine-grained node information.

### Per-Node State

Store an LSTM hidden state for each node and update it with that node's contextual embedding. This preserves fine-grained information, though it is less explicitly global.

## Link Prediction Strategies

### Predict Only Changes

Existing triples are passed forward. The model predicts additions and deletions with separate scoring heads. Candidate sets contain true positive additions/deletions plus an equal number of sampled negatives.

### Predict the Entire Graph

The model predicts all triples for the next graph. The candidate set includes current triples plus potential candidates, sampled to balance positive and negative examples.

Benefits:

- Naturally allows edge removal.
- Conceptually simpler.

Drawbacks:

- Since most edges persist, the model may learn that current edges always stay.

## Candidate Proposal

Candidate proposal must be restricted to a subset of nodes and relations to remain feasible.

Node sampling strategies:

- random nodes
- nearby nodes at graph distance 1 to 3
- embedding-similar nodes

Relation sampling strategies:

- random relations
- relations common among local neighbors, with noise
- a learned relation score such as `MLP(i, j, relation)`, though this may be expensive

Candidate proposal can also stand in for pure node generation, since it can connect previously unconnected nodes without needing a language model.

## Candidate Scoring

Batch candidate triples into tensors and score them with an MLP:

```text
MLP(i, j, edge, i_hidden, j_hidden)
```

The score is passed through a sigmoid to obtain probabilities.

Possible selection strategies:

- choose all candidates above a threshold
- choose top `k`
- sample probabilistically

## Loss

Use binary cross entropy against the next graph.

- Existing or newly true edges are labeled `1`.
- Sampled non-edges are labeled `0`.

## Generation

Generation is autoregressive. Start with one graph, predict the next graph or graph delta, apply the prediction, and feed the result back into the model.

## Data Considerations

- The data structure must be compatible with PyTorch and PyTorch Geometric.
- A strict entity typing system could provide useful structure.
- Wikidata may already contain useful type information.
- The relation set should be constrained to keep training and candidate proposal tractable.
