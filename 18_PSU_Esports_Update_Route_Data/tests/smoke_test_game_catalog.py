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
            "42 เกม",
            "Call of Duty: Warzone",
            "Delta Force",
            "EA Sports FC 24",
            "eFootball",
            "FINAL FANTASY XVI",
            "Hogwarts Legacy",
            "THE FINALS",
            "Pokémon Champions",
            "Resident Evil Village",
            "Uncharted: Legacy of Thieves Collection",
        ],
        "full game catalog",
    )
    assert_not_contains(result.answer, ["Mario Kart Live: Home Circuit"], "full game catalog should use current reservation catalog")
    print("OK game catalog: all games")

    for question in ("เกมตอนนี้มีเกมอะไรบ้าง", "เกมทั้งหมดมีกี่เกม"):
        result = answer_question_pipeline_debug(question)
        assert_contains(
            result.answer,
            ["42 เกม", "PC Zone", "PlayStation 5 Zone", "Nintendo Switch Zone", "VR Zone", "Cockpit Zone"],
            question,
        )
        assert_not_contains(result.answer, ["Mario Kart Live: Home Circuit"], question)
        if "PlayStation 5 Zone มีเกมที่ยืนยันได้" in result.answer:
            raise AssertionError(f"{question}: should answer all games, not only PS5\n{result.answer}")
    print("OK game catalog: explicit all/current games")

    result = answer_question_pipeline_debug("PS5 มีเกมอะไรบ้าง")
    assert_contains(
        result.answer,
        [
            "PlayStation 5 Zone",
            "Delta Force",
            "EA Sports FC 24",
            "eFootball",
            "Resident Evil Village",
            "The Last of Us Part II (Remastered)",
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
            "Pokémon Champions",
            "Mario Kart 8 Deluxe",
            "Mario Party Superstars",
            "Ring Fit Adventure",
            "The Legend of Zelda: Breath of The Wild",
        ],
        "nintendo game catalog",
    )
    assert_not_contains(result.answer, ["Mario Kart Live: Home Circuit"], "nintendo current game catalog")
    print("OK game catalog: Nintendo")

    result = answer_question_pipeline_debug("เกมแนวแข่งรถมีอะไรบ้าง")
    assert_contains(result.answer, ["Mario Kart 8 Deluxe", "Gran Turismo 7"], "racing genre")
    assert_not_contains(result.answer, ["PSU Phuket CS2 2026 Tournament"], "racing should not route to tournament")
    print("OK game catalog: racing genre")

    result = answer_question_pipeline_debug("เกม Minecraft มีข้อมูลไหม", experimental_rag_fallback=True, experimental_allow_llm=True)
    assert_contains(result.answer, ["ยังไม่พบ Minecraft", "รายการเกมที่ยืนยันได้"], "minecraft data availability")
    if result.mode != "pipeline:games_known_unsupported_fast_path":
        raise AssertionError(f"minecraft data availability: expected fast path, got {result.mode}")
    print("OK game catalog: Minecraft unsupported fast path")

    result = answer_question_pipeline_debug("เกม TEKKEN 8 มีข้อมูลไหม", experimental_rag_fallback=True, experimental_allow_llm=True)
    assert_contains(result.answer, ["TEKKEN 8", "ได้ครับ"], "tekken data availability")
    if result.mode not in {"pipeline:games_availability_fast_path", "pipeline:structured_service_game_availability"}:
        raise AssertionError(f"tekken data availability: expected availability path, got {result.mode}")
    print("OK game catalog: TEKKEN availability path")

    result = answer_question_pipeline_debug("TEKKEN 8 มีปุ่มอะไรบ้าง")
    assert_contains(
        result.answer,
        ["Square", "Triangle", "Cross", "Circle", "D-Pad Up", "L1", "R1", "R1 (While in Heat)", "Options"],
        "tekken full controls",
    )
    if result.answer.count("\n•    ") < 12:
        raise AssertionError(f"tekken full controls: expected all control rows\n{result.answer}")
    print("OK game controls: TEKKEN full list")

    print("GAME CATALOG SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
