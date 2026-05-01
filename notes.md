# Development Notes

## Performance Notes

Too much of the model currently depends on slow CPU operations. Future work should make more of the pipeline parallel so it can better use GPUs, or add memoization to trade memory for speed.

## Progress Log

### Full-Graph Prediction

The first approach predicted the entire next graph from the full current graph plus sampled additions. This created a massive positive/negative imbalance, and the model learned to pass through existing edges.

### Balanced Current-Edge Sampling

The next version sampled current edges as positives and an equal number of additions as negatives. This balanced the positive and negative classes, but the model still learned to distinguish current edges from additions and mostly passed through current edges.

### Delta Prediction

Delta prediction introduced two scoring heads:

- an addition head
- a deletion head

Deletion candidates contained edges that were actually removed plus an equal number of sampled current triples. Addition candidates contained true additions plus proposals from candidate-proposal strategies. This version did not work well.

### Deltas with Relation Time (`deltas_v6`)

Version 6 added the amount of time an edge has been alive as a feature. After refactoring the codebase, deletion prediction began to work on synthetic data, reaching perfect F1 on a toy dataset.

### Deltas with Relation Time and History Awareness (`deltas_v7`)

Version 7 kept the relation-time feature and added node, pair, and triple history. The history features helped the model understand what makes a valid triple and were used for both candidate proposal and addition scoring.

### Deltas (`deltas_v8`)

Version 8 is similar to `deltas_v7`, but has better validation metrics.
