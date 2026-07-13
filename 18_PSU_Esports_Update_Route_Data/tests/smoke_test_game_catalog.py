from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item.lower() not in text.lower()]
    if missing:
        raise AssertionError(f"{label}: missing {missing}\n{text}")


def assert_not_contains(text: str, forbidden: list[str], label: str) -> None:
    found = [item for item in forbidden if item.lower() in text.lower()]
    if found:
        raise AssertionError(f"{label}: forbidden {found}\n{text}")


def main() -> int:
    result = answer_question_pipeline_debug("มีเกมทั้งหมดอะไรบ้าง")
    assert_contains(
        result.answer,
        [
            "36 เกม",
            "Mario Kart Live: Home Circuit",
            "EA Sports FC 24",
            "FINAL FANTASY XVI",
            "Hogwarts Legacy",
            "Uncharted: Legacy of Thieves Collection",
        ],
        "full game catalog",
    )
    print("OK game catalog: all games")

    result = answer_question_pipeline_debug("PS5 มีเกมอะไรบ้าง")
    assert_contains(
        result.answer,
        [
            "PlayStation 5 Zone",
            "EA Sports FC 24",
            "Resident Evil Village",
            "The Last of Us Part I / Part II",
            "Uncharted: Legacy of Thieves Collection",
        ],
        "ps5 game catalog",
    )
    print("OK game catalog: PS5")

    result = answer_question_pipeline_debug("Nintendo Switch มีเกมอะไรบ้าง")
    assert_contains(
        result.answer,
        [
            "Nintendo Switch Zone",
            "Mario Kart Live: Home Circuit",
            "Mario Party Superstars",
            "Ring Fit Adventure",
            "The Legend of Zelda: Breath of the Wild",
        ],
        "nintendo game catalog",
    )
    print("OK game catalog: Nintendo")

    result = answer_question_pipeline_debug("เกมแนวแข่งรถมีอะไรบ้าง")
    assert_contains(result.answer, ["Mario Kart 8 Deluxe", "Gran Turismo 7"], "racing genre")
    assert_not_contains(result.answer, ["PSU Phuket CS2 2026 Tournament"], "racing should not route to tournament")
    print("OK game catalog: racing genre")

    result = answer_question_pipeline_debug("TEKKEN 8 มีปุ่มอะไรบ้าง")
    assert_contains(
        result.answer,
        ["Square", "Triangle", "Cross", "Circle", "D-Pad Up", "L1", "R1", "R1 (While in Heat)", "Options"],
        "tekken full controls",
    )
    if result.answer.count("\n- ") < 12:
        raise AssertionError(f"tekken full controls: expected all control rows\n{result.answer}")
    print("OK game controls: TEKKEN full list")

    print("GAME CATALOG SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
