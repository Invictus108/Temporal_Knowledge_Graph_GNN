# Temporal Knowledge Graph GNN

This repository explores neural models for temporal knowledge graphs. The goal is to predict how a knowledge graph changes over time, especially which edges should be added or deleted at the next timestep.

The main modeling direction is a delta-prediction architecture: encode each graph snapshot with a relation-aware GNN, maintain recurrent node memory over time, generate candidate edge additions/deletions, and score those candidates with separate addition and deletion heads.

## Paper

The write-up for this project is included in the repository as [paper.pdf](paper.pdf). It covers the motivation, model design, datasets, and experimental results in more detail than this README.

## Project Overview

Temporal knowledge graphs contain facts that are only valid during certain time ranges. Instead of predicting an entire graph from scratch at every timestep, this project treats graph evolution as a sequence of changes:

1. Start from the current graph snapshot.
2. Encode node, relation, and temporal edge features.
3. Update per-node recurrent memory.
4. Propose candidate additions and deletions.
5. Score those candidates.
6. Apply the predicted delta to produce the next graph.

This framing avoids some of the class imbalance from full-graph prediction, where most existing edges simply persist.

## Model Design

The current model family combines:

- global node features from text embeddings
- learned relation embeddings
- relation-aware graph attention/message passing
- edge relative-time features that track how long a triple has been active
- per-node LSTM hidden states
- explicit node, pair, and triple history features
- separate addition and deletion scoring heads

The design notes are documented in:

- [model_ideas.md](model_ideas.md)
- [delta_design.md](delta_design.md)
- [notes.md](notes.md)

## Data

The project uses both real and synthetic temporal knowledge graph data.

### Wikidata

The custom Wikidata pipeline extracts valid triples from a Wikidata dump, resolves entity and relation labels/descriptions, builds yearly or monthly temporal JSON files, and converts them into PyTorch Geometric datasets.

Pipeline notes:

- [pipeline.md](pipeline.md)
- [datasets.md](datasets.md)
- [data_exploration/data.md](data_exploration/data.md)

Important files:

- `data_exploration/custom_wikidata/data_pipeline.ipynb`: extracts valid triples from a Wikidata dump.
- `data_exploration/custom_wikidata/data_processing.ipynb`: resolves entity and relation metadata.
- `data_exploration/custom_wikidata/json_gen.ipynb`: creates yearly/monthly JSON snapshots.
- `data_exploration/wikidata_torch_dataset_gen.ipynb`: creates PyTorch Geometric datasets.
- `data_exploration/wikidata_dataset_class.py`: defines `GlobalTemporalTextKGDataset`.
- `data_exploration/custom_wikidata/tag_entities.py`: adds heuristic tags such as `person`, `place`, `organization`, `event`, and `work`.

Packaged dataset artifacts include:

- `datasets/wikidata12k_with_rel_time.pt`
- `datasets/descriptions_dataset_1800_2.pt`
- `datasets/wikidata_with_description_clean.json`
- `datasets/wikidata_with_description_clean_tagged.json`

### Synthetic Data

Synthetic datasets are used for controlled validation. They define typed nodes and deterministic relation paths, with variants such as:

- `2ent_2rel`
- `2ent_5rel`
- `2ent_9rel`
- `5ent_5rel`
- `10ent_10rel`

The small GitHub-friendly versions live in `datasets/sample_sythetic/`. The directory name is intentionally left as it exists in the repo.

Synthetic data documentation:

- [datasets/sample_sythetic/datasets.md](datasets/sample_sythetic/datasets.md)
- [data_exploration/synthetic_data/datasets.md](data_exploration/synthetic_data/datasets.md)

Important files:

- `data_exploration/synthetic_data_gen.ipynb`: generates synthetic temporal graph JSON files.
- `data_exploration/synthetic_dataset_class.py`: defines `SyntheticTemporalGraphDataset`.

### ICEWS and YAGO Exploration

ICEWS was explored but is not the best fit for the main model because it stores events rather than persistent relationships. The graph can change sharply between adjacent timesteps. Wikidata12k and YAGO11k are better aligned with the persistent-relation setting.

Exploration files:

- `data_exploration/ICEWS/icews_events.py`
- `data_exploration/ICEWS/icews_exploration.py`
- `data_exploration/yago/yago.py`
- `data_exploration/wikidata.py`
- `data_exploration/wikidata_cache.py`

## Repository Structure

```text
.
|-- data_exploration/        # Data exploration, generation, and dataset classes
|-- datasets/                # Packaged processed datasets and sample synthetic data
|-- models/                  # Training notebooks, plots, diagrams, and figures
|-- personal/                # Local/archived experiments ignored by git
|-- datasets.md              # Dataset version notes
|-- delta_design.md          # Delta-model design notes
|-- model_ideas.md           # Early architecture notes
|-- notes.md                 # Experiment progress notes
|-- pipeline.md              # Custom Wikidata pipeline notes
|-- result_cache.md          # Saved experiment logs
|-- paper.pdf                # Project write-up
```

## Main Notebooks

- `models/whole_graph_v1.ipynb`: early full-graph prediction baseline.
- `models/deltas_v1.ipynb` through `models/deltas_v4.ipynb`: early delta-prediction experiments.
- `models/deltas_v6_synthetic.ipynb`: adds relation-time features and validates on synthetic data.
- `models/deltas_v7.ipynb`: adds explicit node/pair/triple history features for Wikidata.
- `models/deltas_v7_synthetic.ipynb`: synthetic version of the history-aware model.
- `models/deltas_v8.ipynb`: newer Wikidata delta model with improved validation metrics.
- `models/deltas_v8_synthetic.ipynb`: newer synthetic delta model and the most useful synthetic reference notebook.

## Environment

The code is notebook-oriented and uses Python with PyTorch and PyTorch Geometric.

Core dependencies:

- `torch`
- `torch-geometric`
- `numpy`
- `pandas`
- `networkx`
- `matplotlib`
- `sentence-transformers`
- `requests`
- `jupyter`

PyTorch and PyTorch Geometric installation depends on your CUDA or CPU setup, so install those from the official instructions for your machine.

Example setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy pandas networkx matplotlib requests sentence-transformers jupyter
```

Then install `torch` and `torch-geometric` for your platform.

On Windows PowerShell, activate the virtual environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Typical Workflow

1. Generate or load data.
   - For synthetic data, run `data_exploration/synthetic_data_gen.ipynb`.
   - For custom Wikidata data, follow `pipeline.md` and the notebooks in `data_exploration/custom_wikidata/`.

2. Convert data to a dataset object.
   - Synthetic JSON is loaded with `SyntheticTemporalGraphDataset.from_json(...)`.
   - Wikidata JSON is converted with `GlobalTemporalTextKGDataset`.

3. Train a model notebook.
   - Use `models/deltas_v8_synthetic.ipynb` for synthetic data.
   - Use `models/deltas_v8.ipynb` for Wikidata-style data.

4. Inspect results.
   - Plots are saved in `models/plots/`.
   - Paper-style figures are in `models/paper_figures/`.
   - Text logs are in `result_cache.md` and `models/plots/epochs.md`.

## Notes for Submission

Most human-authored text notes have been converted from `.txt` to Markdown. The remaining `.txt` files under `data/tkg_data/` are benchmark data files such as `train.txt`, `valid.txt`, `test.txt`, `entity2id.txt`, `relation2id.txt`, and `triple2id.txt`. They are intentionally preserved because the data loaders and standard temporal-KG formats expect those filenames.

Some notebooks contain hard-coded local paths or assume they are run from a specific directory. If moving the project to another machine, check path constants such as `BASE_PATH`, `EVENTS_FILE`, and dataset filenames before running.
