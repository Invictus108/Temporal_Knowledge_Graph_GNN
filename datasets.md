# Dataset Notes

This file records the project datasets and what each version represents.

## Custom Wikidata Datasets

- `full_monthly_v1`: monthly snapshots built from the full available range.
- `full_yearly_v1`: yearly snapshots built from the full available range.
- `monthly_1950_2000_v1`: monthly snapshots from 1950 to 2000, chosen for more consistent graph sizes.
- `limited_monthly_1950_2000_v1`: monthly snapshots from 1950 to 2000, restricted to the 23 relations in Wikidata12k for more consistent graph sizes and faster training.

## Packaged Dataset Variants

- `simple`: Wikidata12k without descriptions.
- `descriptions_dataset_1800`: Wikidata12k with descriptions, represented as yearly snapshots from 1800 to 2020.
- `descriptions_dataset_1800_2`: a later version of `descriptions_dataset_1800`; likely the same dataset with cleaner processing.
