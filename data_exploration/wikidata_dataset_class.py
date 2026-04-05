import json
import os
from typing import Any, Callable, Dict, List, Optional

import numpy as np
import torch
from torch_geometric.data import Data, InMemoryDataset

# takes the json of {year: [{head: text, tail:text, rel: text}]} as well as mappings defined above
class GlobalTemporalTextKGDataset(InMemoryDataset):
    def __init__(
        self,
        root: str,
        start_year: int,
        entity_to_id: Dict[str, int],
        relation_to_id: Dict[str, int],
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

        # Filled after loading processed file
        self.x_global: Optional[torch.Tensor] = None
        self.id_to_entity: Optional[Dict[int, str]] = None

        super().__init__(root, transform, pre_transform, pre_filter)

        obj = torch.load(self.processed_paths[0], weights_only=False)
        self.data = obj["data"]
        self.slices = obj["slices"]
        self.x_global = obj["x_global"]
        self.id_to_entity = obj["id_to_entity"]
        self.id_to_rel = obj["id_to_rel"]

    # get file names
    @property
    def raw_file_names(self) -> List[str]:
        return [self.json_filename]

    @property
    def processed_file_names(self) -> List[str]:
        return [self.dataset_filename]

    def download(self):
        pass

    # get node embeddings
    def _build_global_node_features(self) -> torch.Tensor:
        if len(self.entity_to_id) == 0:
            return torch.empty((0, 0), dtype=torch.float)

        # get num of nodes
        max_id = max(self.entity_to_id.values())
        num_nodes = max_id + 1

        # reverse mapping
        id_to_entity = {idx: text for text, idx in self.entity_to_id.items()}

        # make sure ids are contiguous
        missing = [i for i in range(num_nodes) if i not in id_to_entity]
        if missing:
            raise ValueError(
                f"entity_to_id must use contiguous ids from 0..{num_nodes-1}. "
                f"Missing ids: {missing[:10]}"
            )

        # order entities
        entity_texts_ordered = [id_to_entity[i] for i in range(num_nodes)]

        # get embeddings
        embeddings = self.embed_fn(entity_texts_ordered)
        embeddings = np.asarray(embeddings, dtype=np.float32)

        # check for emb errors
        if embeddings.shape[0] != num_nodes:
            raise ValueError(
                f"embed_fn returned {embeddings.shape[0]} embeddings for "
                f"{num_nodes} entities"
            )

        return torch.tensor(embeddings, dtype=torch.float)

    def process(self):
        # Load raw temporal triples
        with open(self.raw_paths[0], "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # Build global node feature matrix once
        # size [num_nodes, embedding_dim]
        x_global = self._build_global_node_features()
        num_nodes = x_global.size(0)

        # reverse mappings
        id_to_entity = {idx: text for text, idx in self.entity_to_id.items()}
        id_to_rel = {idx: text for text, idx in self.relation_to_id.items()}

        data_list = []

        # iterate through years
        for year in range(self.start, 2020):
            triples = raw_data[str(year)]

            src = [] # source node indices
            dst = [] # destination node indices
            rels = [] # relation ids
            active_nodes = set() # nodes used at this step

            for triple in triples:
                # get text
                head_text = triple["head"]
                tail_text = triple["tail"]
                rel_text = triple["relation"]

                # extract ids
                h_id = self.entity_to_id[head_text]
                t_id = self.entity_to_id[tail_text]
                r_id = self.relation_to_id[rel_text]

                # append ids to lists
                src.append(h_id)
                dst.append(t_id)
                rels.append(r_id)

                # add active nodes
                active_nodes.add(h_id)
                active_nodes.add(t_id)

            # tensor of edges
            # size [2, num_edges]
            edge_index = (
                torch.tensor([src, dst], dtype=torch.long)
                if len(src) > 0
                else torch.empty((2, 0), dtype=torch.long)
            )

            # tensor of edge types
            # size [num_edges]
            edge_type = (
                torch.tensor(rels, dtype=torch.long)
                if len(rels) > 0
                else torch.empty((0,), dtype=torch.long)
            )

            # tensor of active nodes
            active_nodes = (
                torch.tensor(sorted(active_nodes), dtype=torch.long)
                if len(active_nodes) > 0
                else torch.empty((0,), dtype=torch.long)
            )

            # create pygraph object
            data = Data(
                edge_index=edge_index,
                edge_type=edge_type,
                year=torch.tensor([year], dtype=torch.long),
                active_nodes=active_nodes,
                num_nodes=num_nodes,
            )

            data_list.append(data)

        data, slices = self.collate(data_list)

        torch.save(
            {
                "data": data,
                "slices": slices,
                "x_global": x_global,
                "id_to_entity": id_to_entity,
                "id_to_rel": id_to_rel
            },
            self.processed_paths[0],
        )