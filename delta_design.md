# Delta Model Design

## Goal

The model should predict how a knowledge graph changes over time. The main architecture combines an attention-based graph neural network with a recurrent model, most likely an LSTM.

The model uses a global node pool. Some nodes may be unconnected in a given timestep, which is expected.

## Text and Relation Representation

### Relation Embeddings

Relations are represented by learned embeddings over a limited relation subset. Examples include `born`, `died`, `friends`, `enemies`, and `killed_by`.

### Node Text Embeddings

Each node can be represented with pretrained embeddings from multiple textual fields:

- name
- description
- class or type

The preferred approach is to concatenate those embeddings and pass them through an embedding head that synthesizes the text features and projects them down to the GNN hidden dimension.

Text embeddings could also be merged with structural embeddings, but the graph structure should largely be learned through message passing.

## Embedding Head

Use a simple MLP that takes the text embedding vector for a node and projects it into the model hidden dimension.

## Graph Update Rule

For node `i`, the update is:

```text
h(t + 1)_i = nonlinearity(sum_j a_ij * m_ij)
```

where `a_ij` is an attention score and `m_ij` is a message from neighbor `j`.

The attention score is:

```text
a_score_ij = nonlinearity(a(z_i, z_j, edge_ij))
z = W_n * h
```

Attention is computed only over neighbors and normalized with softmax.

Messages combine neighbor hidden state and relation features:

```text
m_ij = W_h * h(t)_j + W_r * edge_ij
```

## Multi-Head Attention

Multi-head attention should be considered after the single-head version is working.

- The hidden dimension must be divisible by the number of heads.
- Each head can use its own `W_h`, `W_r`, and attention parameters, projected down to `dim / num_heads`.
- The head outputs are concatenated.
- A cheaper variant can share weights across heads. It is less expressive than full multi-head attention, but still captures multiple relationship patterns.

## Stabilization

Because the update uses sums over neighbors, layer normalization and residual connections are useful:

```text
h(t + 1) = GNNLayer(h(t))
h(t + 1) = LayerNorm(h(t + 1) + h(t))
```

If multi-head attention changes dimensions, the residual path needs a projection. A feed-forward block can also be added:

```text
h(t + 1) = LayerNorm(h(t + 1) + MLP(h(t + 1)))
```

Dropout may also improve generalization.

## Recurrent State

After several graph updates, the model should have rich contextual node embeddings for link prediction and generation.

The current preferred recurrent strategy stores an LSTM hidden state for each node. This preserves fine-grained node information, at the cost of a weaker global graph-level representation. The per-node LSTM state is then used for scoring.

## Link Prediction as Delta Prediction

The model predicts graph changes rather than predicting the entire next graph from scratch.

- Existing triples are carried forward to the next timestep.
- The model predicts additions and deletions with two separate scoring heads.
- Training candidates include true additions/deletions plus an equal number of sampled negatives.

Negative addition candidates can be generated with:

- random node sampling
- nearby nodes at graph distance 1 to 3
- embedding-similar nodes

Relation candidates can be sampled by:

- random relation sampling
- relation counts among neighbors, with noise
- an expensive learned score such as `MLP(i, j, relation)`

## Candidate Scoring

Use separate scoring heads for additions and deletions. Batch candidate triples into tensors and score them with an MLP using:

```text
MLP(i, j, edge, i_hidden, j_hidden)
```

The output is passed through a sigmoid to produce a probability. Loss is computed against positive addition/deletion examples and sampled negatives.

## Loss

Use binary cross entropy over addition and deletion samples from the next graph.

- Positive edges are labeled `1`.
- Negative sampled edges are labeled `0`.
- Addition and deletion losses are summed.

This should capture both positive and negative samples for additions and deletions.

## Generation

Generation is autoregressive:

1. Start from one graph snapshot.
2. Run the model to predict additions and deletions.
3. Apply the predicted changes.
4. Feed the updated graph back into the model.
