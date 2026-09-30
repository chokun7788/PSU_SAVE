"""Build 1,000 Thai and 1,000 English typo probes from master GT v2.

This creates new synthetic questions. It never edits the original ground truth.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.normalization import KEYBOARD_EN_TO_THAI  # noqa: E402


SOURCE = ROOT / "data" / "eval" / "master_ground_truth_bilingual_10000_v2.jsonl"
OUTPUT = ROOT / "data" / "eval" / "master_gt_bilingual_multi_error_2000_20260929_r15.jsonl"
SEED = 20260929
RECIPES = ("repeat", "neighbor", "delete", "transpose", "mixed")
KEY_ROWS = ("qwertyuiop", "asdfghjkl", "zxcvbnm")
THAI_KEY_ROWS = ("1234567890-=", "qwertyuiop[]\\", "asdfghjkl;'", "zxcvbnm,./")
PROTECTED_RE = re.compile(
    r"https?://\S+|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|"
    r"\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}:\d{2}\b|"
    r"\b\d+(?:[.,]\d+)?\b|\b(?:PC\s*#?\d+|PS5|VR\s*#?\d+)\b",
    re.IGNORECASE,
)
ENGLISH_TOKEN_RE = re.compile(r"[A-Za-z]{3,}")


def _neighbors(rows: tuple[str, ...], mapping: dict[str, str] | None = None) -> dict[str, tuple[str, ...]]:
    result: dict[str, tuple[str, ...]] = {}
    for row in rows:
        for index, key in enumerate(row):
            char = mapping.get(key, "") if mapping else key
            if not char or len(char) != 1:
                continue
            values = []
            for other in (index - 1, index + 1):
                if 0 <= other < len(row):
                    neighbor = mapping.get(row[other], "") if mapping else row[other]
                    if len(neighbor) == 1 and neighbor != char:
                        values.append(neighbor)
            if values:
                result[char] = tuple(values)
    return result


THAI_NEIGHBORS = _neighbors(THAI_KEY_ROWS, KEYBOARD_EN_TO_THAI)
ENGLISH_NEIGHBORS = _neighbors(KEY_ROWS)


def _protected_literals(row: dict) -> list[str]:
    question = str(row["question"])
    values = [match.group() for match in PROTECTED_RE.finditer(question)]
    target = str(row.get("expected_target") or "").strip()
    if target and target.casefold() in question.casefold():
        values.append(question[question.casefold().index(target.casefold()):][: len(target)])
    return list(dict.fromkeys(values))


def _protected_mask(question: str, row: dict) -> list[bool]:
    protected = [False] * len(question)
    for literal in _protected_literals({**row, "question": question}):
        start = question.casefold().find(literal.casefold())
        if start >= 0:
            for index in range(start, start + len(literal)):
                protected[index] = True
    if row["locale"] == "th":
        for match in re.finditer(r"[A-Za-z][A-Za-z0-9'-]*", question):
            for index in range(match.start(), match.end()):
                protected[index] = True
    else:
        for match in ENGLISH_TOKEN_RE.finditer(question):
            if match.start() > 0 and match.group()[0].isupper():
                for index in range(match.start(), match.end()):
                    protected[index] = True
    return protected


def _positions(question: str, row: dict, action: str, avoid: int = -100) -> list[int]:
    protected = _protected_mask(question, row)
    locale = row["locale"]
    allowed = [False] * len(question)
    if locale == "th":
        for index, char in enumerate(question):
            allowed[index] = not protected[index] and "\u0e00" <= char <= "\u0e7f"
    else:
        for match in ENGLISH_TOKEN_RE.finditer(question):
            for index in range(match.start(), match.end()):
                allowed[index] = not protected[index]
    positions = []
    for index, char in enumerate(question):
        if not allowed[index] or abs(index - avoid) < 4:
            continue
        if action == "neighbor":
            neighbors = THAI_NEIGHBORS if locale == "th" else ENGLISH_NEIGHBORS
            if char.lower() not in neighbors:
                continue
        if action == "transpose" and (
            index + 1 >= len(question) or not allowed[index + 1]
            or question[index + 1] == char
        ):
            continue
        positions.append(index)
    return positions


def _mutate_once(question: str, row: dict, action: str, rng: random.Random, avoid: int = -100) -> tuple[str, int]:
    positions = _positions(question, row, action, avoid)
    if not positions:
        raise ValueError(f"No {action} position in {row['id']}: {question!r}")
    index = rng.choice(positions)
    char = question[index]
    if action == "repeat":
        return question[:index] + char + question[index:], index
    if action == "delete":
        return question[:index] + question[index + 1 :], index
    if action == "transpose":
        return question[:index] + question[index + 1] + char + question[index + 2 :], index
    neighbors = THAI_NEIGHBORS if row["locale"] == "th" else ENGLISH_NEIGHBORS
    replacement = rng.choice(neighbors[char.lower()])
    if char.isupper():
        replacement = replacement.upper()
    return question[:index] + replacement + question[index + 1 :], index


def _mutate(row: dict, recipe: str, rng: random.Random) -> tuple[str, list[str]]:
    question = str(row["question"])
    actions = ("neighbor", "delete") if recipe == "mixed" else (recipe,)
    changed_at = -100
    for action in actions:
        if not _positions(question, row, action, changed_at):
            changed_at = -100
        question, changed_at = _mutate_once(question, row, action, rng, changed_at)
    return question, list(actions)


def _sample(rows: list[dict], locale: str, count: int, rng: random.Random) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        if row.get("locale") == locale:
            grouped[str(row["domain"])].append(row)
    domains = sorted(grouped)
    quotas = {domain: count // len(domains) + (index < count % len(domains)) for index, domain in enumerate(domains)}
    selected = []
    for domain in domains:
        candidates = sorted(grouped[domain], key=lambda row: row["id"])
        rng.shuffle(candidates)
        usable = []
        for row in candidates:
            if all(_positions(str(row["question"]), row, action) for action in RECIPES if action != "mixed"):
                usable.append(row)
            if len(usable) >= quotas[domain]:
                break
        if len(usable) < quotas[domain]:
            raise ValueError(f"Too few mutable {locale}/{domain} rows: {len(usable)} < {quotas[domain]}")
        selected.extend(usable)
    rng.shuffle(selected)
    return selected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--count-per-locale", type=int, default=1000)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"Output already exists: {args.output}")
    if args.count_per_locale <= 0:
        parser.error("Count must be positive")
    rows = [json.loads(line) for line in args.source.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    rng = random.Random(SEED)
    output = []
    for locale in ("th", "en"):
        for ordinal, row in enumerate(_sample(rows, locale, args.count_per_locale, rng)):
            recipe = RECIPES[ordinal % len(RECIPES)]
            noisy, edits = _mutate(row, recipe, rng)
            literals = _protected_literals(row)
            if noisy == row["question"] or any(literal not in noisy for literal in literals):
                raise AssertionError(f"Mutation changed a protected literal or had no effect: {row['id']}")
            output.append({
                "id": row["id"], "locale": locale, "domain": row["domain"],
                "clean_question": row["question"], "noisy_question": noisy,
                "edit_recipe": recipe, "edit_actions": edits,
                "protected_literals": literals,
                "expected_route_categories": row.get("expected_route_categories", []),
                "expected_answer_status": row.get("expected_answer_status", ""),
                "answer_contract": row.get("answer_contract", {}),
                "expected_target": row.get("expected_target", ""),
                "review_status": row.get("review_status", ""),
                "source_contract": row.get("source_contract", {}),
                "metadata": row.get("metadata", {}),
                "latency_ceiling_sec": row.get("latency_ceiling_sec", 20.0),
                "source_fixture": args.source.name,
                "synthetic_seed": SEED,
            })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in output),
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(args.output), "count": len(output),
        "locales": dict(Counter(row["locale"] for row in output)),
        "recipes": dict(Counter(row["edit_recipe"] for row in output)),
        "domains_per_locale": {
            locale: dict(Counter(row["domain"] for row in output if row["locale"] == locale))
            for locale in ("th", "en")
        },
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
