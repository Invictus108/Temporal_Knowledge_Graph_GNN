from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Union

import torch
from torch import Tensor
from torch.utils.data import Dataset


@dataclass
class TemporalGraphSnapshot:
    """
    One timestep of a temporal graph.

    Attributes
    ----------
    edge_index : LongTensor of shape [2, E]
        Directed edges for this timestep.
    edge_type : LongTensor of shape [E]
        Relation id for each edge.
    """
    edge_index: Tensor
    edge_type: Tensor


class SyntheticTemporalGraphDataset(Dataset):
    """
    Minimal temporal graph dataset compatible with code that expects:

        dataset.x_global          # Tensor [num_nodes, embed_dim]
        dataset.id_to_rel         # dict[int, str]
        dataset.id_to_entity      # dict[int, str]
        len(dataset)              # number of timesteps
        dataset[t].edge_index     # LongTensor [2, E]
        dataset[t].edge_type      # LongTensor [E]

    Expected JSON format
    --------------------
    {
      "x_global": [[...], [...], ...],              # required, shape [num_nodes, embed_dim]
      "id_to_entity": {"0": "A0", "1": "A1", ...},  # optional but recommended
      "id_to_rel": {"0": "rel1", "1": "rel2"},      # required
      "timesteps": [
        {
          "edges": [
            {"src": 0, "dst": 10, "rel": 0},
            {"src": 1, "dst": 11, "rel": 1}
          ]
        },
        {
          "edges": [...]
        }
      ]
    }

    Notes
    -----
    - Node ids and relation ids in JSON may be strings or ints.
    - Empty timesteps are allowed.
    - This class does not assume anything about the synthetic process itself.
      Your generator can create any temporal rule as long as it writes the
      JSON in the schema above.
    """

    def __init__(
        self,
        x_global: Tensor,
        timesteps: Sequence[TemporalGraphSnapshot],
        id_to_rel: Dict[int, str],
        id_to_entity: Optional[Dict[int, str]] = None,
    ) -> None:
        super().__init__()

        if not torch.is_tensor(x_global):
            raise TypeError("x_global must be a torch.Tensor")

        if x_global.ndim != 2:
            raise ValueError(
                f"x_global must have shape [num_nodes, embed_dim], got {tuple(x_global.shape)}"
            )

        self.x_global: Tensor = x_global.float()
        self.timesteps: List[TemporalGraphSnapshot] = list(timesteps)
        self.id_to_rel: Dict[int, str] = dict(id_to_rel)
        self.id_to_entity: Dict[int, str] = dict(id_to_entity) if id_to_entity is not None else {}

        self.num_nodes: int = self.x_global.shape[0]
        self.embed_dim: int = self.x_global.shape[1]

        self._validate()

    def _validate(self) -> None:
        """Validate shapes and ids."""
        for t, snapshot in enumerate(self.timesteps):
            if snapshot.edge_index.ndim != 2 or snapshot.edge_index.shape[0] != 2:
                raise ValueError(
                    f"Timestep {t}: edge_index must have shape [2, E], "
                    f"got {tuple(snapshot.edge_index.shape)}"
                )

            if snapshot.edge_type.ndim != 1:
                raise ValueError(
                    f"Timestep {t}: edge_type must have shape [E], "
                    f"got {tuple(snapshot.edge_type.shape)}"
                )

            num_edges = snapshot.edge_index.shape[1]
            if snapshot.edge_type.shape[0] != num_edges:
                raise ValueError(
                    f"Timestep {t}: edge_index has {num_edges} edges but "
                    f"edge_type has length {snapshot.edge_type.shape[0]}"
                )

            if num_edges > 0:
                min_node = int(snapshot.edge_index.min().item())
                max_node = int(snapshot.edge_index.max().item())
                if min_node < 0 or max_node >= self.num_nodes:
                    raise ValueError(
                        f"Timestep {t}: edge_index contains node ids outside "
                        f"[0, {self.num_nodes - 1}]"
                    )

                rel_ids = snapshot.edge_type.unique().tolist()
                unknown_rels = [r for r in rel_ids if int(r) not in self.id_to_rel]
                if unknown_rels:
                    raise ValueError(
                        f"Timestep {t}: unknown relation ids found: {unknown_rels}"
                    )

    def __len__(self) -> int:
        return len(self.timesteps)

    def __getitem__(self, t: int) -> TemporalGraphSnapshot:
        return self.timesteps[t]

    @classmethod
    def from_json(
        cls,
        path: Union[str, Path],
        device: Optional[Union[str, torch.device]] = None,
    ) -> "SyntheticTemporalGraphDataset":
        """
        Load dataset from a JSON file following the schema in the class docstring.
        """
        path = Path(path)
        with path.open("r", encoding="utf-8") as f:
            raw = json.load(f)

        if "x_global" not in raw:
            raise KeyError("JSON must contain 'x_global'")
        if "id_to_rel" not in raw:
            raise KeyError("JSON must contain 'id_to_rel'")
        if "timesteps" not in raw:
            raise KeyError("JSON must contain 'timesteps'")

        x_global = torch.tensor(raw["x_global"], dtype=torch.float)

        id_to_rel = {int(k): str(v) for k, v in raw["id_to_rel"].items()}
        id_to_entity = {
            int(k): str(v) for k, v in raw.get("id_to_entity", {}).items()
        }

        timesteps: List[TemporalGraphSnapshot] = []
        for step_idx, step in enumerate(raw["timesteps"]):
            edges = step.get("edges", [])

            if len(edges) == 0:
                edge_index = torch.empty((2, 0), dtype=torch.long)
                edge_type = torch.empty((0,), dtype=torch.long)
            else:
                src_list = []
                dst_list = []
                rel_list = []

                for e in edges:
                    try:
                        src = int(e["src"])
                        dst = int(e["dst"])
                        rel = int(e["rel"])
                    except KeyError as exc:
                        raise KeyError(
                            f"Timestep {step_idx}: every edge must have keys "
                            f"'src', 'dst', and 'rel'"
                        ) from exc

                    src_list.append(src)
                    dst_list.append(dst)
                    rel_list.append(rel)

                edge_index = torch.tensor([src_list, dst_list], dtype=torch.long)
                edge_type = torch.tensor(rel_list, dtype=torch.long)

            timesteps.append(
                TemporalGraphSnapshot(edge_index=edge_index, edge_type=edge_type)
            )

        dataset = cls(
            x_global=x_global,
            timesteps=timesteps,
            id_to_rel=id_to_rel,
            id_to_entity=id_to_entity,
        )

        if device is not None:
            dataset.to(device)

        return dataset

    def to(self, device: Union[str, torch.device]) -> "SyntheticTemporalGraphDataset":
        """
        Move x_global and all timestep tensors to a device.
        """
        self.x_global = self.x_global.to(device)
        self.timesteps = [
            TemporalGraphSnapshot(
                edge_index=s.edge_index.to(device),
                edge_type=s.edge_type.to(device),
            )
            for s in self.timesteps
        ]
        return self