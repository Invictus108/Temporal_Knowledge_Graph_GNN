# Sample Synthetic Datasets

The datasets in this directory are small enough to fit in the repository. Models were trained and validated on larger versions.

## `2ent_2rel`

- 2 entity types: `A`, `B`
- 400 total nodes, evenly split
- Directed edges are allowed only between different types: `A <-> B`
- All cross-type pairs are valid
- Relationships follow one deterministic path:

```text
Path 0:
contact (2 steps) -> bonded (5 steps) -> inactive
total duration: 7
```

Relation mapping:

```text
0: contact
1: bonded
```

## `2ent_5rel`

- 2 entity types: `A`, `B`
- 400 total nodes, evenly split
- Directed edges are allowed only between `A <-> B`
- All cross-type pairs are valid
- Relationships follow one of three deterministic paths:

```text
Path 0:
contact (2) -> negotiate (2) -> bonded (5) -> strained (2) -> recovery (2)
total duration: 13

Path 1:
contact (2) -> negotiate (3) -> bonded (4) -> recovery (3)
total duration: 12

Path 2:
contact (1) -> strained (3) -> negotiate (2) -> bonded (5)
total duration: 11
```

Relation mapping:

```text
0: contact
1: negotiate
2: bonded
3: strained
4: recovery
```

## `2ent_9rel`

- 2 entity types: `A`, `B`
- 400 total nodes, evenly split
- Directed edges are allowed only between `A <-> B`
- All cross-type pairs are valid
- Relationships follow one of four deterministic paths:

```text
Path 0:
contact (2) -> negotiate (3) -> collaborate (6) -> maintain (4)
total duration: 15

Path 1:
contact (2) -> negotiate (2) -> conflict (3) -> recover (2) -> collaborate (4)
total duration: 13

Path 2:
contact (1) -> trial (3) -> scale (5) -> decay (3)
total duration: 12

Path 3:
contact (2) -> conflict (2) -> recover (2) -> maintain (5) -> decay (2)
total duration: 13
```

Relation mapping:

```text
0: contact
1: negotiate
2: trial
3: collaborate
4: scale
5: conflict
6: recover
7: maintain
8: decay
```

## `5ent_5rel`

- 5 entity types: `A`, `B`, `C`, `D`, `E`
- 400 total nodes, evenly split
- Directed edges are allowed only along a cycle: `A -> B -> C -> D -> E -> A`
- No other type pairs can form relationships
- Relationships follow one of three deterministic paths:

```text
Path 0:
contact (2) -> negotiate (2) -> bonded (5) -> strained (2) -> recovery (2)
total duration: 13

Path 1:
contact (2) -> negotiate (3) -> bonded (4) -> recovery (3)
total duration: 12

Path 2:
contact (1) -> strained (3) -> negotiate (2) -> bonded (5)
total duration: 11
```

Relation mapping:

```text
0: contact
1: negotiate
2: bonded
3: strained
4: recovery
```

## `10ent_10rel`

- 10 entity types: `A` through `J`
- 400 total nodes, evenly split
- Directed edges are allowed only along a cycle: `A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> A`
- Each type can only form outgoing edges to the next type in the cycle
- Relationships follow one of five deterministic paths:

```text
Path 0:
contact (2) -> negotiate (3) -> trial (4) -> collaborate (5) -> decay (3)
total duration: 17

Path 1:
contact (1) -> scale (3) -> conflict (4) -> recover (3) -> scale (2)
total duration: 13

Path 2:
negotiate (2) -> trial (2) -> maintain (6) -> decay (3)
total duration: 13

Path 3:
contact (2) -> collaborate (3) -> conflict (3) -> recover (2) -> maintain (4) -> scale (2)
total duration: 16

Path 4:
scale (2) -> negotiate (3) -> trial (5) -> decay (2)
total duration: 12
```

Relation mapping:

```text
0: contact
1: negotiate
2: trial
3: collaborate
4: scale
5: conflict
6: recover
7: maintain
8: decay
9: scale
```
