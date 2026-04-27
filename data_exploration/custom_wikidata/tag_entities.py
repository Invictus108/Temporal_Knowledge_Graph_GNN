"""
Adds a `tags` list to every head/tail entity in a temporal-KG JSON.

Reads:  datasets/wikidata_with_description_clean.json
Writes: datasets/wikidata_with_description_clean_tagged.json   (NEW FILE — original untouched)

Each entity dict gains a `tags` field, e.g.
    {"label": "Joseph E. Stiglitz",
     "description": "American economist...",
     "tags": ["person"]}

Tags are inferred from the entity description with regex heuristics. An entity
can carry multiple tags (e.g. ["person", "athlete"]). If nothing matches, the
list contains "other".

The category vocabulary is intentionally small and stable so that downstream
filtering (`category_filter=["person", "place"]`) stays simple.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "datasets" / "wikidata_with_description_clean.json"
DST = ROOT / "datasets" / "wikidata_with_description_clean_tagged.json"


# --- pattern banks (lowercased description) --------------------------------

PERSON_PROFESSIONS = (
    r"politician|footballer|player|athlete|coach|cyclist|swimmer|skater|"
    r"runner|boxer|wrestler|tennis player|golfer|cricketer|rugby player|"
    r"actor|actress|singer|musician|composer|conductor|guitarist|pianist|"
    r"violinist|drummer|rapper|songwriter|"
    r"writer|author|poet|novelist|journalist|editor|playwright|screenwriter|"
    r"film director|filmmaker|film producer|cinematographer|"
    r"scientist|physicist|chemist|biologist|biochemist|mathematician|"
    r"economist|psychologist|sociologist|anthropologist|historian|"
    r"philosopher|theologian|"
    r"engineer|architect|inventor|"
    r"painter|sculptor|illustrator|photographer|"
    r"chef|"
    r"diplomat|statesman|stateswoman|monarch|emperor|empress|king|queen|"
    r"prince|princess|duke|duchess|earl|baron|baroness|viscount|"
    r"president|prime minister|senator|congressman|congresswoman|"
    r"governor|mayor|judge|attorney|lawyer|"
    r"general|admiral|colonel|soldier|"
    r"physician|surgeon|nurse|"
    r"professor|academic|researcher|scholar|theorist|"
    r"businessman|businesswoman|entrepreneur|industrialist|investor|banker|"
    r"priest|bishop|cardinal|pope|rabbi|imam|monk|nun|"
    r"comedian|dancer|choreographer|"
    r"explorer|astronaut|cosmonaut|"
    r"computer scientist|programmer|software developer"
)
PERSON_RE = re.compile(
    r"\b(?:" + PERSON_PROFESSIONS + r")\b", re.IGNORECASE
)
# Strong person signal: "(1920–2014)", "(1861-1940)", "(born 1948)", "(b. 1948)".
# Requires either a year-range OR an explicit "born"/"b." prefix — a single
# bare year in parens (e.g. "(2002–)") is NOT enough.
PERSON_DATE_RE = re.compile(
    r"\(\s*(?:"
    r"born\s+\d{3,4}"
    r"|b\.\s*\d{3,4}"
    r"|\d{3,4}\s*[-–—]\s*\d{3,4}"
    r")\s*\)",
    re.IGNORECASE,
)

PLACE_RE = re.compile(
    r"\b(commune|village|town|city|capital|borough|county|province|prefecture|"
    r"district|region|department|state|territory|country|nation|island|archipelago|"
    r"municipality|hamlet|settlement|metropolis|"
    r"river|lake|mountain|peak|valley|desert|forest|sea|ocean|gulf|bay|strait|"
    r"continent|peninsula|plateau|"
    r"neighborhood|neighbourhood|suburb)\b",
    re.IGNORECASE,
)

ORGANIZATION_RE = re.compile(
    r"\b(company|corporation|firm|enterprise|business|"
    r"organization|organisation|institution|agency|bureau|"
    r"university|college|school|academy|institute|"
    r"club|team|squad|"
    r"party|coalition|alliance|union|federation|confederation|league|association|"
    r"government|ministry|department|"
    r"bank|fund|"
    r"church|denomination|order|"
    r"foundation|charity|ngo|"
    r"laboratory|consortium|"
    r"newspaper|magazine|publisher|broadcaster|network|studio|label)\b",
    re.IGNORECASE,
)

SPORTS_TEAM_RE = re.compile(
    r"\b(football club|soccer club|basketball team|hockey team|baseball team|"
    r"national team|sports team|esports|fc\b|f\.c\.|cf\b|c\.f\.)\b",
    re.IGNORECASE,
)

AWARD_RE = re.compile(
    r"\b(award|prize|medal|honour|honor|decoration|trophy|cup\b)\b",
    re.IGNORECASE,
)

POSITION_RE = re.compile(
    r"\b(position|office|title|role|"
    r"prime minister of|president of|secretary of|minister of|"
    r"member of|chair of|chairman of|chairwoman of|chairperson of|"
    r"governor of|mayor of|head of|director of|"
    r"shadow (secretary|minister|cabinet))\b",
    re.IGNORECASE,
)

EVENT_RE = re.compile(
    r"\b(election|war|battle|revolution|uprising|coup|treaty|"
    r"olympics|championship|tournament|competition|cup final|"
    r"festival|ceremony|conference|summit|"
    r"earthquake|flood|hurricane|tsunami|pandemic|epidemic|"
    r"disaster|accident|incident|crisis|protest|riot)\b",
    re.IGNORECASE,
)

WORK_RE = re.compile(
    r"\b(film|movie|novel|book|short story|poem|play|opera|"
    r"song|single|album|ep\b|"
    r"video game|television series|tv series|tv show|sitcom|drama|"
    r"painting|sculpture|symphony|concerto|sonata)\b",
    re.IGNORECASE,
)

GROUP_RE = re.compile(
    r"\b(band|orchestra|ensemble|choir|duo|trio|quartet|quintet|"
    r"music group|musical group|girl group|boy band)\b",
    re.IGNORECASE,
)

# common short-description patterns — good fallbacks
SHORT_AWARD = re.compile(r"^(award|annual award|category of)\b", re.IGNORECASE)
SHORT_PLACE = re.compile(
    r"^(commune in|village in|city in|town in|country in|island in|river in|"
    r"capital of|county in|province in|state in|region in|district in|"
    r"municipality of|municipality in)\b",
    re.IGNORECASE,
)
SHORT_PERSON = re.compile(
    r"^(american|british|english|french|german|italian|spanish|russian|"
    r"chinese|japanese|indian|brazilian|argentine|argentinian|canadian|"
    r"australian|dutch|belgian|swedish|norwegian|danish|finnish|polish|"
    r"swiss|austrian|portuguese|mexican|turkish|ukrainian|czech|hungarian|"
    r"greek|romanian|irish|scottish|welsh|israeli|moroccan|egyptian|"
    r"south african|nigerian|kenyan)\b",
    re.IGNORECASE,
)


def tag_entity(label: str, description: str) -> list[str]:
    """
    Return a list of tags for a single entity, ordered by specificity.

    Strategy: first try strong/structural signals (date pattern, place, org,
    award, position, event, work, group). Only fall back to person via
    profession word or nationality prefix when no other strong tag matched —
    that prevents "American film studio" from being tagged person just because
    "American" hits the nationality fallback.
    """
    desc = (description or "").strip()
    label = (label or "").strip()
    tags: list[str] = []

    has_profession = bool(PERSON_RE.search(desc))
    has_person_date = bool(PERSON_DATE_RE.search(desc))
    has_group = bool(GROUP_RE.search(desc))

    # Person date-range alone is ambiguous (could be a band's active years),
    # so require it not to coincide with a group/work/org cue.
    if has_profession or (has_person_date and not has_group):
        tags.append("person")

    if PLACE_RE.search(desc) or SHORT_PLACE.search(desc):
        tags.append("place")

    if SPORTS_TEAM_RE.search(desc) or SPORTS_TEAM_RE.search(label):
        tags.append("organization")
        tags.append("sports_team")
    elif ORGANIZATION_RE.search(desc) or ORGANIZATION_RE.search(label):
        tags.append("organization")

    if AWARD_RE.search(desc) or AWARD_RE.search(label) or SHORT_AWARD.search(desc):
        tags.append("award")

    if POSITION_RE.search(desc) or POSITION_RE.search(label):
        tags.append("position")

    if EVENT_RE.search(desc):
        tags.append("event")

    if WORK_RE.search(desc):
        tags.append("work")

    if has_group:
        tags.append("group")

    # If we still have no tag, fall back to a nationality-prefix person guess.
    if not tags and SHORT_PERSON.search(desc):
        tags.append("person")

    # de-dup while preserving order
    seen = set()
    uniq: list[str] = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            uniq.append(t)

    if not uniq:
        uniq.append("other")
    return uniq


def main() -> int:
    if not SRC.exists():
        print(f"source not found: {SRC}", file=sys.stderr)
        return 1

    print(f"loading {SRC} ...")
    with SRC.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # cache by label → tags so we tag each unique entity once
    label_to_tags: dict[str, list[str]] = {}
    head_count = 0
    tail_count = 0

    for year, entries in data.items():
        for entry in entries:
            for side in ("head", "tail"):
                ent = entry[side]
                label = ent.get("label", "")
                desc = ent.get("description", "")
                key = label or desc
                if key not in label_to_tags:
                    label_to_tags[key] = tag_entity(label, desc)
                ent["tags"] = list(label_to_tags[key])
                if side == "head":
                    head_count += 1
                else:
                    tail_count += 1

    # tag distribution report
    counter: Counter[str] = Counter()
    for tags in label_to_tags.values():
        for t in tags:
            counter[t] += 1

    print(f"unique entities tagged: {len(label_to_tags)}")
    print(f"head fields written: {head_count}")
    print(f"tail fields written: {tail_count}")
    print("tag distribution (over unique entities):")
    for t, c in counter.most_common():
        pct = 100.0 * c / len(label_to_tags)
        print(f"  {t:18s} {c:6d}  ({pct:5.1f}%)")

    print(f"writing {DST} ...")
    with DST.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
