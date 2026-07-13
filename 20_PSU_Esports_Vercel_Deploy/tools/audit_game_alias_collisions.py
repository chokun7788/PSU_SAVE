from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
ALIASES_PATH = ROOT / "data" / "curated" / "game_title_aliases.jsonl"


def alias_key(value: str) -> str:
    return "".join(ch for ch in str(value or "").lower() if ch.isalnum() or "\u0e00" <= ch <= "\u0e7f")


def load_aliases() -> dict[str, set[str]]:
    aliases_by_game: dict[str, set[str]] = defaultdict(set)
    for line_no, line in enumerate(ALIASES_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        game = str(row.get("game") or "").strip()
        if not game:
            print(f"WARN line {line_no}: missing game")
            continue
        aliases_by_game[game].add(game)
        for alias in row.get("aliases") or []:
            clean = str(alias or "").strip()
            if clean:
                aliases_by_game[game].add(clean)
    return aliases_by_game


def main() -> int:
    aliases_by_game = load_aliases()
    owners_by_alias: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for game, aliases in aliases_by_game.items():
        for alias in aliases:
            key = alias_key(alias)
            if key:
                owners_by_alias[key].append((game, alias))

    duplicates = {
        key: owners
        for key, owners in owners_by_alias.items()
        if len({game for game, _ in owners}) > 1
    }

    prefix_warnings: list[tuple[str, str, str, str]] = []
    keys = sorted(owners_by_alias, key=len)
    for index, short_key in enumerate(keys):
        if len(short_key) < 5:
            continue
        short_games = {game for game, _ in owners_by_alias[short_key]}
        for long_key in keys[index + 1:]:
            if len(long_key) > len(short_key) + 24:
                break
            if short_key == long_key or not long_key.startswith(short_key):
                continue
            long_games = {game for game, _ in owners_by_alias[long_key]}
            if short_games.isdisjoint(long_games):
                prefix_warnings.append((
                    owners_by_alias[short_key][0][1],
                    next(iter(short_games)),
                    owners_by_alias[long_key][0][1],
                    next(iter(long_games)),
                ))

    print("GAME ALIAS COLLISION AUDIT")
    print(f"- games: {len(aliases_by_game)}")
    print(f"- unique aliases: {len(owners_by_alias)}")
    print(f"- exact duplicate alias keys across games: {len(duplicates)}")
    print(f"- prefix overlaps across games: {len(prefix_warnings)}")

    if duplicates:
        print("\nExact duplicates:")
        for key, owners in sorted(duplicates.items())[:30]:
            rendered = "; ".join(f"{game} <= {alias}" for game, alias in owners)
            print(f"- {key}: {rendered}")

    if prefix_warnings:
        print("\nPrefix overlaps to review:")
        for short_alias, short_game, long_alias, long_game in prefix_warnings[:40]:
            print(f"- {short_alias!r} ({short_game}) prefixes {long_alias!r} ({long_game})")

    print("\nNote: prefix overlaps are warnings, not failures. Use them to decide where longer aliases or scoring guards are needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
