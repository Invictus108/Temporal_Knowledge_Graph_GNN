
# generates cache for entites and relations


import os
import json
import time
import requests

# =========================
# GLOBAL CONFIG
# =========================
BASE_PATH = "../data/tkg_data/extracted/data/wiki_data/large"

ENTITY_MAPPING_FILE = os.path.join(BASE_PATH, "entity2id.txt")
RELATION_MAPPING_FILE = os.path.join(BASE_PATH, "relation2id.txt")

ENTITY_CACHE_FILE = os.path.join(BASE_PATH, "wikidata_entity_label_cache.json")
RELATION_CACHE_FILE = os.path.join(BASE_PATH, "wikidata_relation_label_cache.json")

HEADERS = {
    "User-Agent": "TemporalKGExplorer/1.0",
    "Accept": "application/json",
}

REQUEST_SLEEP = 0.25
MAX_RETRIES = 5


# =========================
# LOAD MAPPINGS
# =========================
def load_id_mapping(path):
    """
    Reads lines like:
        Q438025    11261
        P54        17

    Returns:
        local_int_id -> raw_wikidata_id
    """
    mapping = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 2:
                continue

            raw_id = parts[0]
            local_id = int(parts[1])
            mapping[local_id] = raw_id

    return mapping


# =========================
# CACHE HELPERS
# =========================
def load_cache(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

# =========================
# DESCRIPTION RESOLUTION
# =========================
def extract_description(entity, fallback_id=None):
    descriptions = entity.get("descriptions", {})

    for key in ["en", "en-us", "en-gb", "mul"]:
        if key in descriptions and "value" in descriptions[key]:
            return descriptions[key]["value"]

    if descriptions:
        first = next(iter(descriptions.values()))
        return first.get("value", fallback_id)

    return fallback_id

def fetch_wikidata_description(wikidata_id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=20)

            if resp.status_code == 429:
                wait = max(2 ** attempt, 1)
                print(f"429 for {wikidata_id}, sleeping {wait}s...")
                time.sleep(wait)
                continue

            resp.raise_for_status()
            data = resp.json()

            entity = data.get("entities", {}).get(wikidata_id)
            if entity is None:
                return wikidata_id

            return extract_description(entity, wikidata_id)

        except Exception as e:
            wait = max(2 ** attempt, 1)
            print(f"Error resolving description for {wikidata_id}: {e}. Sleeping {wait}s...")
            time.sleep(wait)

    return wikidata_id

# =========================
# LABEL RESOLUTION
# =========================
def extract_label(entity, fallback_id=None):
    labels = entity.get("labels", {})

    for key in ["en", "en-us", "en-gb", "mul"]:
        if key in labels and "value" in labels[key]:
            return labels[key]["value"]

    if labels:
        first = next(iter(labels.values()))
        return first.get("value", fallback_id)

    return fallback_id


def fetch_wikidata_label(wikidata_id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=20)

            if resp.status_code == 429:
                wait = max(2 ** attempt, 1)
                print(f"429 for {wikidata_id}, sleeping {wait}s...")
                time.sleep(wait)
                continue

            resp.raise_for_status()
            data = resp.json()

            entity = data.get("entities", {}).get(wikidata_id)
            if entity is None:
                return wikidata_id

            return extract_label(entity, wikidata_id)

        except Exception as e:
            wait = max(2 ** attempt, 1)
            print(f"Error resolving {wikidata_id}: {e}. Sleeping {wait}s...")
            time.sleep(wait)

    return wikidata_id


def build_cache_from_mapping(mapping, cache_path, kind):
    """
    mapping: local_int_id -> raw_wikidata_id
    cache_path: where to store raw_wikidata_id -> label
    kind: 'relation' or 'entity'
    """
    cache = load_cache(cache_path)
    unique_raw_ids = sorted(set(mapping.values()))
    total = len(unique_raw_ids)

    print(f"\nBuilding {kind} cache for {total} ids...")
    print(f"Cache file: {cache_path}")

    for i, raw_id in enumerate(unique_raw_ids, start=1):
        if raw_id in cache:
            print(f"[cache   {i}/{total}] {raw_id} -> {cache[raw_id]}")
            continue

        label = fetch_wikidata_label(raw_id)
        # cache[raw_id] = label
        description = fetch_wikidata_description(raw_id)
        cache[raw_id] = {"label": label, "description": description}
        
        save_cache(cache, cache_path)

        print(f"[fetched {i}/{total}] {raw_id} -> {label}")
        time.sleep(REQUEST_SLEEP)

    print(f"Finished {kind} cache: {cache_path}")


# =========================
# MAIN
# =========================
def main():
    relation_map = load_id_mapping(RELATION_MAPPING_FILE)
    entity_map = load_id_mapping(ENTITY_MAPPING_FILE)

    print(f"Loaded {len(relation_map)} relations")
    print(f"Loaded {len(entity_map)} entities")

    # Do relations first
    build_cache_from_mapping(
        mapping=relation_map,
        cache_path=RELATION_CACHE_FILE,
        kind="relation"
    )

    # Then entities
    build_cache_from_mapping(
        mapping=entity_map,
        cache_path=ENTITY_CACHE_FILE,
        kind="entity"
    )

    print("\nDone.")


if __name__ == "__main__":
    main()