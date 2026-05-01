# Custom Wikidata Pipeline

The custom Wikidata pipeline lives in `data_exploration/custom_wikidata`.

1. `data_pipeline.ipynb` extracts valid triples from a Wikidata dump and writes them to a CSV file.
2. `data_processing.ipynb` and `json_gen.ipynb` resolve entity and relation labels from the dump.
3. `json_gen.ipynb` takes the CSV and cache JSON files and creates yearly and monthly JSON datasets.
4. Each date key maps to an array of triples.
5. Each entity object is represented as a nested JSON object with `label` and `description` fields.
6. `wikidata_torch_dataset_gen.ipynb` converts the JSON data into a PyTorch Geometric dataset.
7. The generated dataset is passed to the model notebooks for training.
