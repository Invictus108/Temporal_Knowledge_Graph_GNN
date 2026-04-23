import json
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
import torch
from torch_geometric.data import Data, InMemoryDataset


class GlobalTemporalTextKGDataset(InMemoryDataset):
    def __init__(
        self,
        root: str,
        start_year: int,
        end_year: int,
        monthly: bool,
        entity_to_id: Dict[str, int],
        relation_to_id: Dict[str, int],
        entity_to_data: Dict[str, Dict[str, Any]],
        embed_fn: Callable[[List[str]], np.ndarray],
        json_filename: str,
        dataset_filename: str,
        transform=None,
        pre_transform=None,
        pre_filter=None,
    ):
        self.json_filename = json_filename
        self.dataset_filename = dataset_filename
        self.entity_to_id = entity_to_id
        self.relation_to_id = relation_to_id
        self.embed_fn = embed_fn
        self.start = start_year
        self.end = end_year
        self.entity_to_data = entity_to_data
        self.monthly = monthly

        # Filled after loading processed file
        self.x_global: Optional[torch.Tensor] = None
        self.id_to_entity: Optional[Dict[int, str]] = None
        self.id_to_rel: Optional[Dict[int, str]] = None

        super().__init__(root, transform, pre_transform, pre_filter)

        obj = torch.load(self.processed_paths[0], weights_only=False)
        self.data = obj["data"]
        self.slices = obj["slices"]
        self.x_global = obj["x_global"]
        self.id_to_entity = obj["id_to_entity"]
        self.id_to_rel = obj["id_to_rel"]

    @property
    def raw_file_names(self) -> List[str]:
        return [self.json_filename]

    @property
    def processed_file_names(self) -> List[str]:
        return [self.dataset_filename]

    def download(self):
        pass

    def _get_timesteps(self, raw_data: Dict[str, Any]) -> List[str]:
        if self.monthly:
            timesteps = []
            for year in range(self.start, self.end):
                for month in range(1, 13):
                    key = f"{year:04d}-{month:02d}"
                    if key in raw_data:
                        timesteps.append(key)
        else:
            timesteps = [
                str(year) for year in range(self.start, self.end)
                if str(year) in raw_data
            ]
        return timesteps

    def _collect_subset_entities(
        self,
        raw_data: Dict[str, Any],
        timesteps: List[str],
    ) -> List[str]:
        used_entities = set()

        for t in timesteps:
            triples = raw_data[t]
            for triple in triples:
                head_text = triple["head"]["label"]
                tail_text = triple["tail"]["label"]
                used_entities.add(head_text)
                used_entities.add(tail_text)

        return sorted(used_entities)

    def _build_subset_global_node_features(
        self,
        subset_entities: List[str],
    ):
        if len(subset_entities) == 0:
            x_global = torch.empty((0, 0), dtype=torch.float)
            entity_to_local_id = {}
            id_to_entity = {}
            return x_global, entity_to_local_id, id_to_entity

        entity_to_local_id = {
            entity: i for i, entity in enumerate(subset_entities)
        }
        id_to_entity = {
            i: entity for entity, i in entity_to_local_id.items()
        }

        entity_payloads = [self.entity_to_data[entity] for entity in subset_entities]
        embeddings = self.embed_fn(entity_payloads)
        embeddings = np.asarray(embeddings, dtype=np.float32)

        if embeddings.shape[0] != len(subset_entities):
            raise ValueError(
                f"embed_fn returned {embeddings.shape[0]} embeddings for "
                f"{len(subset_entities)} entities"
            )

        x_global = torch.tensor(embeddings, dtype=torch.float)
        return x_global, entity_to_local_id, id_to_entity

    def process(self):
        with open(self.raw_paths[0], "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # 1. only use timesteps inside requested range
        timesteps = self._get_timesteps(raw_data)

        # 2. collect only entities appearing in those timesteps
        subset_entities = self._collect_subset_entities(raw_data, timesteps)

        # 3. build local/global mapping only for this subset
        x_global, entity_to_local_id, id_to_entity = self._build_subset_global_node_features(
            subset_entities
        )
        num_nodes = x_global.size(0)

        # relation mapping can stay global unless you also want to subset relations
        id_to_rel = {idx: text for text, idx in self.relation_to_id.items()}

        data_list = []

        # Tracks the current consecutive run length for each exact triple
        # key = (local_head_id, relation_id, local_tail_id)
        prev_run_length: Dict[Tuple[int, int, int], int] = {}
        prev_active_triples: set[Tuple[int, int, int]] = set()

        for t in timesteps:
            triples = raw_data[t]

            src = []
            dst = []
            rels = []
            rel_times = []
            active_nodes = set()
            current_active_triples = set()

            # First pass: convert triples to local ids and remember active triples this timestep
            converted_triples: List[Tuple[int, int, int]] = []
            for triple in triples:
                head_text = triple["head"]["label"]
                tail_text = triple["tail"]["label"]
                rel_text = triple["relation"]

                h_id = entity_to_local_id[head_text]
                t_id = entity_to_local_id[tail_text]
                r_id = self.relation_to_id[rel_text]

                key = (h_id, r_id, t_id)
                converted_triples.append(key)
                current_active_triples.add(key)

                active_nodes.add(h_id)
                active_nodes.add(t_id)

            # Second pass: compute rel_time for each edge
            for h_id, r_id, t_id in converted_triples:
                key = (h_id, r_id, t_id)

                if key in prev_active_triples:
                    run_len = prev_run_length[key] + 1
                else:
                    run_len = 1

                src.append(h_id)
                dst.append(t_id)
                rels.append(r_id)
                rel_times.append(float(run_len))

            # Build tensors
            edge_index = (
                torch.tensor([src, dst], dtype=torch.long)
                if len(src) > 0
                else torch.empty((2, 0), dtype=torch.long)
            )

            edge_type = (
                torch.tensor(rels, dtype=torch.long)
                if len(rels) > 0
                else torch.empty((0,), dtype=torch.long)
            )

            edge_relative_time = (
                torch.tensor(rel_times, dtype=torch.float)
                if len(rel_times) > 0
                else torch.empty((0,), dtype=torch.float)
            )

            active_nodes = (
                torch.tensor(sorted(active_nodes), dtype=torch.long)
                if len(active_nodes) > 0
                else torch.empty((0,), dtype=torch.long)
            )

            # works for both yearly and monthly
            if self.monthly:
                year_val, month_val = map(int, t.split("-"))
                time_value = year_val * 12 + (month_val - 1)
                data = Data(
                    edge_index=edge_index,
                    edge_type=edge_type,
                    edge_relative_time=edge_relative_time,   # <-- added
                    year=torch.tensor([year_val], dtype=torch.long),
                    month=torch.tensor([month_val], dtype=torch.long),
                    time=torch.tensor([time_value], dtype=torch.long),
                    active_nodes=active_nodes,
                    num_nodes=num_nodes,
                )
            else:
                year_val = int(t)
                data = Data(
                    edge_index=edge_index,
                    edge_type=edge_type,
                    edge_relative_time=edge_relative_time,   # <-- added
                    year=torch.tensor([year_val], dtype=torch.long),
                    time=torch.tensor([year_val], dtype=torch.long),
                    active_nodes=active_nodes,
                    num_nodes=num_nodes,
                )

            data_list.append(data)

            # Update run tracking for next timestep
            next_run_length: Dict[Tuple[int, int, int], int] = {}
            for h_id, r_id, t_id in converted_triples:
                key = (h_id, r_id, t_id)
                if key in prev_active_triples:
                    next_run_length[key] = prev_run_length[key] + 1
                else:
                    next_run_length[key] = 1

            prev_run_length = next_run_length
            prev_active_triples = current_active_triples

        data, slices = self.collate(data_list)

        torch.save(
            {
                "data": data,
                "slices": slices,
                "x_global": x_global,
                "id_to_entity": id_to_entity,
                "id_to_rel": id_to_rel,
            },
            self.processed_paths[0],
        )