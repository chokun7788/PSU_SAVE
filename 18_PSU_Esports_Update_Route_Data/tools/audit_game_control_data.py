from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "control_game" / "nintendo"
SPLIT_DIR = ROOT / "data" / "control_game_split"
CURATED_PATH = ROOT / "data" / "curated" / "game_control_facts.jsonl"
VECTOR_INDEX_PATH = ROOT / "data" / "vector" / "psu_hybrid_vector_index.json"

sys.path.insert(0, str(ROOT))
from tools.build_game_control_facts import GAME_NAME_OVERRIDES, SUPPORTED_PLATFORM_KEYS, control_mappings, platform_key, slug  # noqa: E402


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON: {path}: {exc}") from exc


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise AssertionError(f"Invalid JSONL: {path}:{line_no}: {exc}") from exc
    return rows


def source_summary() -> tuple[list[str], dict[tuple[str, str], int], bool]:
    problems: list[str] = []
    expected_counts: dict[tuple[str, str], int] = {}
    if not SOURCE_DIR.exists() or not list(SOURCE_DIR.glob("*.json")):
        return problems, expected_counts, False

    for path in sorted(SOURCE_DIR.glob("*.json")):
        data = read_json(path)
        controls = data.get("game_controls", {}) if isinstance(data, dict) else {}
        game = GAME_NAME_OVERRIDES.get(path.name, str(controls.get("game_name") or path.stem).strip())
        platform = str(controls.get("platform") or "").strip()
        key = platform_key(platform)
        mappings = control_mappings(controls)
        expected_counts[(game, key)] = len(mappings)

        if key not in SUPPORTED_PLATFORM_KEYS:
            problems.append(f"{path.name}: unsupported platform {platform!r}")
        if not mappings:
            problems.append(f"{path.name}: no control mappings found")

        known_list_keys = {"button_mappings", "driving_controls", "pause_menu_shortcuts"}
        for field, value in controls.items():
            if field in known_list_keys or not isinstance(value, list) or not value:
                continue
            if all(isinstance(item, dict) and "button" in item for item in value):
                problems.append(f"{path.name}: unhandled control-like list key {field!r}")

        for index, item in enumerate(mappings, 1):
            if not isinstance(item, dict):
                problems.append(f"{path.name}: mapping {index} is not object")
                continue
            button = (
                item.get("button")
                or item.get("button_ps5")
                or item.get("button_switch")
                or item.get("button_pc")
                or item.get("button_vr")
            )
            action = item.get("action_th") or item.get("action_en")
            if not button:
                problems.append(f"{path.name}: mapping {index} missing button")
            if not action:
                problems.append(f"{path.name}: mapping {index} missing action")

    return problems, expected_counts, True


def curated_summary(expected_counts: dict[tuple[str, str], int], check_source_counts: bool) -> tuple[list[str], Counter[tuple[str, str]], Counter[tuple[str, str]]]:
    problems: list[str] = []
    rows = read_jsonl(CURATED_PATH)
    detail_counts: Counter[tuple[str, str]] = Counter()
    summary_counts: Counter[tuple[str, str]] = Counter()
    ids: Counter[str] = Counter(str(row.get("id") or "") for row in rows)

    for duplicate_id, count in ids.items():
        if duplicate_id and count > 1:
            problems.append(f"curated duplicate id {duplicate_id}: {count}")

    for row in rows:
        if row.get("category") != "game_controls":
            continue
        game = str(row.get("game") or "").strip()
        platform = str(row.get("platform_key") or "").strip()
        key = (game, platform)
        if row.get("button"):
            detail_counts[key] += 1
            if not (row.get("action_th") or row.get("action_en")):
                problems.append(f"{row.get('id')}: button row missing action")
        else:
            summary_counts[key] += 1
            expected = expected_counts.get(key)
            actual = row.get("control_count")
            if check_source_counts and expected is not None and actual != expected:
                problems.append(f"{row.get('id')}: control_count {actual} != expected {expected}")

    if check_source_counts:
        for key, expected in expected_counts.items():
            if detail_counts[key] != expected:
                problems.append(f"{key}: curated detail rows {detail_counts[key]} != source mappings {expected}")
            if summary_counts[key] != 1:
                problems.append(f"{key}: expected 1 summary row, got {summary_counts[key]}")

    for key, count in detail_counts.items():
        if count > 0 and summary_counts[key] != 1:
            problems.append(f"{key}: curated detail rows exist but summary rows={summary_counts[key]}")

    return problems, detail_counts, summary_counts


def split_summary(detail_counts: Counter[tuple[str, str]], summary_counts: Counter[tuple[str, str]]) -> list[str]:
    problems: list[str] = []
    for (game, platform), detail_count in detail_counts.items():
        game_slug = slug(game)
        path = SPLIT_DIR / platform / f"{game_slug}.jsonl"
        if not path.exists():
            problems.append(f"missing split file: {path}")
            continue
        rows = read_jsonl(path)
        expected = detail_count + summary_counts[(game, platform)]
        if len(rows) != expected:
            problems.append(f"{path}: rows {len(rows)} != expected {expected}")
    return problems


def vector_summary() -> list[str]:
    problems: list[str] = []
    curated_game_controls = [
        row for row in read_jsonl(CURATED_PATH)
        if row.get("category") == "game_controls"
    ]
    index = read_json(VECTOR_INDEX_PATH)
    vector_game_controls = [
        doc for doc in index.get("docs", [])
        if doc.get("category") == "game_controls"
    ]
    if len(vector_game_controls) != len(curated_game_controls):
        problems.append(
            f"vector game_controls docs {len(vector_game_controls)} != curated game_controls rows {len(curated_game_controls)}"
        )
    return problems


def main() -> int:
    problems: list[str] = []

    source_problems, expected_counts, source_checked = source_summary()
    problems.extend(source_problems)

    curated_problems, detail_counts, summary_counts = curated_summary(expected_counts, source_checked)
    problems.extend(curated_problems)

    problems.extend(split_summary(detail_counts, summary_counts))
    problems.extend(vector_summary())

    platform_games: dict[str, set[str]] = defaultdict(set)
    source_for_report = expected_counts if source_checked else detail_counts
    for game, platform in source_for_report:
        platform_games[platform].add(game)

    if problems:
        print("GAME CONTROL AUDIT FAILED")
        for problem in problems:
            print("-", problem)
        return 1

    print("GAME CONTROL AUDIT OK")
    if source_checked:
        print(f"- source files: {len(list(SOURCE_DIR.glob('*.json')))}")
        print(f"- source mappings: {sum(expected_counts.values())}")
    else:
        print(f"- source files: skipped ({SOURCE_DIR} not available)")
    for platform in sorted(platform_games):
        rows = sum(count for (game, key), count in source_for_report.items() if key == platform)
        print(f"- {platform}: {len(platform_games[platform])} games, {rows} detail rows")
    print(f"- curated game_controls rows: {sum(detail_counts.values()) + sum(summary_counts.values())}")
    print(f"- vector path: {VECTOR_INDEX_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
