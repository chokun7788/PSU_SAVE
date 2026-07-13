from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "control_game" / "nintendo"
SPLIT_DIR = ROOT / "data" / "control_game_split"
CURATED_PATH = ROOT / "data" / "curated" / "game_control_facts.jsonl"
GAME_TITLE_ALIASES_PATH = ROOT / "data" / "curated" / "game_title_aliases.jsonl"
SOURCE_URL_PREFIX = "local://control_game"

GAME_NAME_OVERRIDES = {
    "FINAL FANTASY XVI.json": "FINAL FANTASY XVI",
}


def slug(value: str) -> str:
    value = value.replace("™", "").replace("®", "")
    value = re.sub(r"[^0-9A-Za-zก-๙]+", "_", value).strip("_").lower()
    return value or "unknown"


def alias_key(value: str) -> str:
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", str(value or "").lower())


def unique_values(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        clean = str(value or "").strip()
        if not clean:
            continue
        key = alias_key(clean)
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(clean)
    return result


def load_game_title_aliases() -> dict[str, list[str]]:
    aliases_by_key: dict[str, list[str]] = defaultdict(list)
    if not GAME_TITLE_ALIASES_PATH.exists():
        return {}
    for line in GAME_TITLE_ALIASES_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        game = str(row.get("game") or row.get("canonical") or row.get("title") or "").strip()
        aliases = row.get("aliases") or []
        if not game or not isinstance(aliases, list):
            continue
        values = unique_values([game, *[str(alias) for alias in aliases]])
        for value in values:
            aliases_by_key[alias_key(value)].extend(values)
    return {key: unique_values(values) for key, values in aliases_by_key.items()}


def aliases_for_game(game: str, filename_stem: str, aliases_by_key: dict[str, list[str]]) -> list[str]:
    values = [game, filename_stem]
    for key in (alias_key(game), alias_key(filename_stem)):
        values.extend(aliases_by_key.get(key, []))
    return unique_values(values)


def platform_key(platform: str) -> str:
    p = (platform or "").lower()
    if "nintendo" in p or "switch" in p:
        return "nintendo"
    if "playstation" in p or "ps5" in p or p.strip() in {"ps", "ps4"}:
        return "ps5"
    return "unknown"


def platform_label(key: str, original: str) -> str:
    if key == "ps5":
        return "PlayStation / PS5"
    if key == "nintendo":
        return "Nintendo Switch"
    return original or "Unknown"


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()] if str(value).strip() else []


def buttons_for_platform(item: dict[str, Any], key: str) -> list[str]:
    if key == "ps5" and item.get("button_ps5"):
        return as_list(item.get("button_ps5"))
    if key == "nintendo" and item.get("button_switch"):
        return as_list(item.get("button_switch"))
    return as_list(item.get("button"))


def row_text(game: str, platform: str, button: str, action_th: str, action_en: str, description: str, note: str = "", section: str = "") -> str:
    parts = [
        f"{game} บน {platform}",
        f"หมวด: {section}" if section else "",
        f"ปุ่ม: {button}" if button else "",
        f"คำสั่ง: {action_th}" + (f" ({action_en})" if action_en else ""),
        f"รายละเอียด: {description}" if description else "",
        f"หมายเหตุ: {note}" if note else "",
    ]
    return "\n".join(part for part in parts if part)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in rows) + ("\n" if rows else ""),
        encoding="utf-8",
    )


def control_mappings(controls: dict[str, Any]) -> list[dict[str, Any]]:
    mappings: list[dict[str, Any]] = []
    sections = (
        ("button_mappings", ""),
        ("driving_controls", "Driving Controls"),
        ("pause_menu_shortcuts", "Pause Menu Shortcuts"),
    )
    for key, label in sections:
        values = controls.get(key) or []
        if not isinstance(values, list):
            continue
        for item in values:
            if not isinstance(item, dict):
                continue
            row = dict(item)
            if label and not row.get("section"):
                row["section"] = label
            mappings.append(row)
    return mappings


def build_rows() -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    all_rows: list[dict[str, Any]] = []
    per_platform: dict[str, list[dict[str, Any]]] = defaultdict(list)
    aliases_by_key = load_game_title_aliases()

    for path in sorted(SOURCE_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        controls = data.get("game_controls", {}) if isinstance(data, dict) else {}
        game = GAME_NAME_OVERRIDES.get(path.name, str(controls.get("game_name") or path.stem).strip())
        original_platform = str(controls.get("platform") or "").strip()
        key = platform_key(original_platform)
        label = platform_label(key, original_platform)
        if key not in {"ps5", "nintendo"}:
            continue

        note = str(controls.get("note") or "").strip()
        mappings = control_mappings(controls)
        game_slug = slug(game)
        game_aliases = aliases_for_game(game, path.stem, aliases_by_key)

        summary = {
            "id": f"game_control_summary_{key}_{game_slug}",
            "category": "game_controls",
            "title": f"{game} controls on {label}",
            "game": game,
            "platform": label,
            "platform_key": key,
            "source_file": path.name,
            "source_url": f"{SOURCE_URL_PREFIX}/{path.name}",
            "control_count": len(mappings),
            "note": note,
            "text": f"{game} บน {label} มีข้อมูลปุ่มควบคุม {len(mappings)} รายการ" + (f"\nหมายเหตุ: {note}" if note else ""),
            "aliases": game_aliases,
            "tags": ["game_controls", "controls", "button_mapping", key, game],
            "priority": 18,
        }
        all_rows.append(summary)
        per_platform[key].append(summary)

        for index, item in enumerate(mappings, 1):
            buttons = buttons_for_platform(item, key)
            button = " / ".join(buttons)
            action_en = str(item.get("action_en") or "").strip()
            action_th = str(item.get("action_th") or "").strip()
            description = str(item.get("description_th") or "").strip()
            section = str(item.get("section") or "").strip()
            action_key = slug(action_en or action_th or f"action_{index}")

            row = {
                "id": f"game_control_{key}_{game_slug}_{index:02d}_{action_key}",
                "category": "game_controls",
                "title": f"{game}: {button} = {action_th or action_en}",
                "game": game,
                "platform": label,
                "platform_key": key,
                "button": button,
                "buttons": buttons,
                "action_en": action_en,
                "action_th": action_th,
                "description_th": description,
                "section": section,
                "source_file": path.name,
                "source_url": f"{SOURCE_URL_PREFIX}/{path.name}",
                "text": row_text(game, label, button, action_th, action_en, description, note, section),
                "aliases": unique_values([*game_aliases, button, *buttons, action_en, action_th]),
                "tags": ["game_controls", "controls", "button_mapping", key, game, button, action_en, action_th, section],
                "priority": 20,
            }
            all_rows.append(row)
            per_platform[key].append(row)

    return all_rows, per_platform


def main() -> int:
    if SPLIT_DIR.exists():
        shutil.rmtree(SPLIT_DIR)
    all_rows, per_platform = build_rows()

    for key in ("ps5", "nintendo"):
        rows = per_platform.get(key, [])
        write_jsonl(SPLIT_DIR / key / f"game_control_facts_{key}.jsonl", rows)

        by_game: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in rows:
            by_game[slug(str(row.get("game") or "unknown"))].append(row)
        for game_slug, game_rows in sorted(by_game.items()):
            write_jsonl(SPLIT_DIR / key / f"{game_slug}.jsonl", game_rows)

    write_jsonl(CURATED_PATH, all_rows)

    print("GAME CONTROL FACTS OK")
    print(f"- source json files: {len(list(SOURCE_DIR.glob('*.json')))}")
    print(f"- rows total: {len(all_rows)}")
    for key in ("ps5", "nintendo"):
        games = {row["game"] for row in per_platform.get(key, [])}
        print(f"- {key}: {len(games)} games, {len(per_platform.get(key, []))} rows")
    print(f"- curated: {CURATED_PATH}")
    print(f"- split: {SPLIT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
