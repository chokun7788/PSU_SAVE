"""Unseen generated task-word edits; always record exceptions and answers."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tests.test_reliability_flow_20261001 import run_focused_case


def cases():
    frames = (
        ("games", "What {} are available in Cockpit", "games", (("Gran Turismo 7",),)),
        ("equipment", "What {} is available in PC Zone", "equipment", (("Gaming Monitor",),)),
        ("information", "What {} do I need to book", "reservation", (("Student ID",), ("phone number",))),
        ("booking", "What information do I need for a {}", "reservation", (("Student ID",), ("phone number",))),
        ("drinks", "Are {} allowed", "rules", (("designated areas",),)),
        ("allowed", "Are drinks {}", "rules", (("designated areas",),)),
    )
    # Real-word collisions are excluded from positive typo claims and checked
    # as negatives by the unit suite, e.g. games/gates and booking/looking.
    real_word_collisions = {"game", "gates", "names", "times", "looking", "cooking", "drink", "drains"}
    seen = set()
    for word, frame, route, groups in frames:
        variants = []
        for index, letter in enumerate(word):
            variants.append(("delete", word[:index] + word[index + 1:]))
            variants.append(("duplicate", word[:index] + letter + word[index:]))
            # Deterministic neighboring key substitutions on an English layout.
            neighbors = {"a": "s", "b": "v", "d": "s", "e": "r", "f": "g", "g": "h",
                         "i": "o", "k": "l", "l": "k", "m": "n", "n": "m", "o": "p",
                         "p": "o", "q": "w", "r": "t", "s": "a", "t": "y", "u": "i", "w": "e"}
            variants.append(("neighbor", word[:index] + neighbors.get(letter, "x") + word[index + 1:]))
        for index in range(len(word) - 1):
            if word[index] != word[index + 1]:
                variants.append(("swap", word[:index] + word[index + 1] + word[index] + word[index + 2:]))
        for recipe, typo in variants:
            question = frame.format(typo)
            if typo in real_word_collisions or question in seen:
                continue
            seen.add(question)
            yield (f"holdout-{word}-{len(seen):03d}-{recipe}", "en", question, route, groups, (), False)
    word = "แล้ว"
    variants = []
    for index, letter in enumerate(word):
        variants.append(("delete", word[:index] + word[index + 1:]))
        variants.append(("duplicate", word[:index] + letter + word[index:]))
        variants.append(("substitute", word[:index] + "ก" + word[index + 1:]))
    for index in range(len(word) - 1):
        variants.append(("swap", word[:index] + word[index + 1] + word[index] + word[index + 2:]))
    for recipe, typo in variants:
        for space in ("", " "):
            question = f"PS5 ราคาเท่าไหร่{space}{typo}มีเกมอะไรบ้าง"
            if question in seen:
                continue
            seen.add(question)
            yield (f"holdout-th-connector-{len(seen):03d}-{recipe}", "th", question, "multi_question",
                   (("บาท",), ("FINAL FANTASY XVI",)), (), False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Refusing to overwrite evidence")
    results = []
    with args.output.open("x", encoding="utf-8") as stream:
        for index, case in enumerate(cases(), 1):
            row = run_focused_case(case)
            row.pop("trace", None)
            results.append(row)
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.flush()
            if not row["passed"]:
                print(row["id"], row["question"], row["failures"], flush=True)
            elif index % 25 == 0:
                print(index, "completed", flush=True)
    print(json.dumps({"count": len(results), "passed": sum(r["passed"] for r in results)}, ensure_ascii=False))
    return 0 if all(r["passed"] for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
