# Data Notes

## ICEWS

ICEWS event data is available from Harvard Dataverse:

<https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/28075>

To explore ICEWS:

1. Download an event file.
2. Unzip one of the event archives. The extracted file should usually be a `.tab` file.
3. Set `EVENTS_FILE` in the ICEWS exploration script to the extracted file path.
4. Run the exploration script or notebook.

ICEWS may not be a good fit for this project because it stores events rather than persistent relationships. The graph changes sharply between timesteps, while this project needs relationships that persist and evolve.

## Persistent Alternatives

- Wikidata12k: <https://zenodo.org/records/4286007#.X7uL8BMzYWo>
- YAGO11k
