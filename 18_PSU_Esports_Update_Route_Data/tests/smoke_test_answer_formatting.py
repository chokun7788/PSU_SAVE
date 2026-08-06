from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item not in text]
    if missing:
        raise AssertionError(f"{label}: missing {missing}\n{text}")


def assert_not_contains(text: str, forbidden: list[str], label: str) -> None:
    found = [item for item in forbidden if item in text]
    if found:
        raise AssertionError(f"{label}: forbidden {found}\n{text}")


def main() -> int:
    equipment = answer_question_pipeline_debug("อุปกรณ์บนหน้า Home มีอะไรบ้าง").answer
    assert_contains(
        equipment,
        [
            "อุปกรณ์บนหน้า Home:",
            "PC Zone",
            "•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)",
            "•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset",
            "Cockpit Zone",
            "•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)",
            "PlayStation 5 Zone",
            "•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)",
            "VR Zone",
            "•    Sony PlayStation VR2 (จำนวน 1 ชุด)",
        ],
        "home equipment formatting",
    )
    assert_not_contains(equipment, ["- PC Zone:", "- Cockpit Zone:"], "home equipment old inline format")
    print("OK answer formatting: equipment")

    ps5_games = answer_question_pipeline_debug("PS5 มีเกมอะไรบ้าง").answer
    assert_contains(
        ps5_games,
        [
            "PlayStation 5 Zone",
            "•    EA Sports FC 24",
            "•    FINAL FANTASY XVI",
            "•    TEKKEN 8",
        ],
        "ps5 game formatting",
    )
    assert_not_contains(ps5_games, ["- PlayStation 5 Zone:"], "ps5 game old inline format")
    print("OK answer formatting: PS5 games")

    all_games = answer_question_pipeline_debug("มีเกมทั้งหมดอะไรบ้าง").answer
    assert_contains(
        all_games,
        [
            "PC Zone",
            "Nintendo Switch Zone",
            "•    Mario Kart 8 Deluxe",
            "•    Pokémon Champions",
            "VR Zone",
            "•    Beat Saber",
        ],
        "all game formatting",
    )
    assert_not_contains(all_games, ["- Nintendo Switch Zone:"], "all game old inline format")
    print("ANSWER FORMATTING SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
