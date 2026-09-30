from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.bilingual_english import _game_title_key


def rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    catalog = {
        game
        for item in rows(ROOT / "data" / "curated" / "service_game_availability.jsonl")
        for game in item["games"]
    }
    controls = rows(ROOT / "data" / "curated" / "game_control_facts.jsonl")
    by_game: dict[str, list[dict]] = {}
    for row in controls:
        by_game.setdefault(_game_title_key(str(row.get("game") or "")), []).append(row)
    pending = []
    for game in catalog:
        records = by_game.get(_game_title_key(game), [])
        if not any(row.get("button") for row in records):
            pending.append(game)
    assert set(pending) == {"Delta Force", "Pokémon Champions"}, pending
    assert any(row.get("game") == "The Last of Us Part II (Remastered)" and row.get("button") for row in controls)
    assert any(row.get("game") == "Resident Evil 4" and row.get("button") for row in controls)
    print("OK 40/42 catalog games have sourced control mappings; two are explicitly pending staff capture")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
