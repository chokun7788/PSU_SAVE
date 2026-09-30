from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.normalization import KEYBOARD_EN_TO_THAI  # noqa: E402


ROWS = ("1234567890-=", "qwertyuiop[]\\", "asdfghjkl;'", "zxcvbnm,./")
DEFAULT_SOURCE = ROOT / "data" / "eval" / "thai_noisy_input_pairs_20260929.jsonl"
DEFAULT_OUTPUT = ROOT / "data" / "eval" / "thai_multi_error_from_verified49_20260929.jsonl"


def _neighbor_map() -> dict[str, tuple[str, ...]]:
    result: dict[str, tuple[str, ...]] = {}
    for row in ROWS:
        for index, key in enumerate(row):
            thai = KEYBOARD_EN_TO_THAI.get(key, "")
            if len(thai) != 1 or unicodedata.category(thai) != "Lo":
                continue
            adjacent = (
                KEYBOARD_EN_TO_THAI.get(row[other], "")
                for other in (index - 1, index + 1)
                if 0 <= other < len(row)
            )
            result[thai] = tuple(
                char for char in adjacent
                if len(char) == 1 and unicodedata.category(char) == "Lo"
            )
    return result


NEIGHBORS = _neighbor_map()


def _add_error(text: str, ordinal: int) -> tuple[str, str]:
    options = [index for index, char in enumerate(text) if char in NEIGHBORS and NEIGHBORS[char]]
    if not options:
        raise ValueError(f"No Thai base character can be perturbed: {text!r}")
    position = options[(ordinal * 7 + 3) % len(options)]
    action = ("neighbor", "delete", "repeat", "transpose")[ordinal % 4]
    if action == "neighbor":
        replacement = NEIGHBORS[text[position]][ordinal % len(NEIGHBORS[text[position]])]
        return text[:position] + replacement + text[position + 1 :], action
    if action == "delete":
        return text[:position] + text[position + 1 :], action
    if action == "repeat":
        return text[:position] + text[position] + text[position:], action
    if position + 1 < len(text) and unicodedata.category(text[position + 1]) == "Lo":
        return text[:position] + text[position + 1] + text[position] + text[position + 2 :], action
    replacement = NEIGHBORS[text[position]][0]
    return text[:position] + replacement + text[position + 1 :], "neighbor_fallback"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-manual-identity", action="store_true")
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"Output already exists: {args.output}")
    source = [json.loads(line) for line in args.source.read_text(encoding="utf-8").splitlines() if line.strip()]
    rows = []
    for ordinal, case in enumerate(source):
        perturbed, added_error = _add_error(case["noisy"], ordinal)
        rows.append({
            **case,
            "id": "MULTI-" + case["id"],
            "noisy": perturbed,
            "noise": case["noise"] + "+" + added_error,
            "source_id": case["id"],
            "review_status": "synthetic_route_probe_not_human_reviewed",
        })
    if not args.no_manual_identity:
        rows.extend({
        "id": f"MULTI-IDENTITY-{index:02d}",
        "group": "identity_compound",
        "noise": "multiple_manual_character_errors",
        "clean": "นายเป็นใครแล้วทำอะไรได้บ้าง",
        "noisy": noisy,
        "expected_intent": "chatbot_identity",
        "review_status": "manually_expected_intent_synthetic_text",
    } for index, noisy in enumerate((
        "นานเปนไคแเสทำอะไรไดเทั่ง",
        "นยเปนใคแล้วทำอาไรไดบ้าง",
        "คุนเปนไคแระช่วยอารายไดบ้าง",
        "บอทนีเปนไคแระทำอาไรไดบ้าง",
        "นายเปนคัยแล้วทำไรไดบ้าง",
        "นานเปนไคแเสทำอะไรไดเทั่งครับ",
        ), start=1))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )
    print(json.dumps({"source_cases": len(source), "generated_cases": len(rows), "output": str(args.output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
