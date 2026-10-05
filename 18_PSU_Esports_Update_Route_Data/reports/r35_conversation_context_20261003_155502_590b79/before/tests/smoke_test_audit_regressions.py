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
    result = answer_question_pipeline_debug("ROV คือเกมอะไร")
    assert result.mode != "pipeline:structured_games_catalog", result.mode
    assert_contains(result.answer, ["RoV", "MOBA"], "rov detail")
    assert_not_contains(result.answer, ["ทั้งหมด 44 เกม", "PlayStation 5 Zone (23 เกม)"], "rov detail should not be full catalog")
    print("OK ROV detail does not become catalog")

    result = answer_question_pipeline_debug("ROV รอบชิงเล่นกี่เกม")
    assert result.route.category == "competition_rules", result.route
    assert result.mode != "pipeline:structured_games_catalog", result.mode
    assert_contains(result.answer, ["RoV", "BO3"], "rov final round")
    assert_not_contains(result.answer, ["ทั้งหมด 44 เกม", "Nintendo Switch Zone"], "competition rule should not be game catalog")
    print("OK competition rule does not become catalog")

    result = answer_question_pipeline_debug("จอง Nintendo Switch ต้องเลือกอะไรบ้าง")
    assert result.mode == "pipeline:structured_booking_selection", result.mode
    assert_contains(result.answer, ["Nintendo Switch", "1-2 Persons", "3-4 Persons"], "nintendo booking choice")
    assert_not_contains(result.answer, ["Nintendo Switch OLED:", "Mario Kart 8 Deluxe"], "booking choice should not be equipment/game list")
    print("OK Nintendo booking choice")

    result = answer_question_pipeline_debug("จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม")
    assert result.mode == "pipeline:structured_booking_selection", result.mode
    assert_contains(result.answer, ["จำนวนผู้เล่น", "1-2 Persons", "3-4 Persons"], "nintendo player count")
    assert_not_contains(result.answer, ["Nintendo Switch OLED:", "Nintendo Switch Zone (16 เกม)"], "player count should not be equipment/game list")
    print("OK Nintendo player count")

    result = answer_question_pipeline_debug("อยากเล่นพวงมาลัยต้องจองโซนอะไร")
    assert result.mode == "pipeline:structured_booking_selection", result.mode
    assert_contains(result.answer, ["Cockpit Zone", "Logitech G923", "Gran Turismo 7"], "wheel booking zone")
    assert_not_contains(result.answer, ["อุปกรณ์ใน Cockpit Zone:"], "wheel booking should answer zone first")
    print("OK wheel booking zone")

    result = answer_question_pipeline_debug("PS5 มีเกมอะไรบ้าง")
    assert result.mode == "pipeline:structured_service_game_availability", result.mode
    assert_contains(result.answer, ["PlayStation 5 Zone", "TEKKEN 8"], "ps5 catalog still works")
    print("OK ordinary game catalog still works")

    print("AUDIT REGRESSION SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
