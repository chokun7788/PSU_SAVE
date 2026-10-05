from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def check(
    question: str,
    must_contain: list[str],
    *,
    must_not_contain: list[str] | None = None,
    mode: str | tuple[str, ...] = ("pipeline:structured_game_controls", "pipeline:game_control_vector_first"),
    route_category: str = "games",
) -> None:
    result = answer_question_pipeline_debug(question)
    answer_lower = result.answer.lower()

    missing = [item for item in must_contain if item.lower() not in answer_lower]
    if missing:
        raise AssertionError(f"{question}: missing {missing}\n{result.answer}")

    forbidden = [item for item in (must_not_contain or []) if item.lower() in answer_lower]
    if forbidden:
        raise AssertionError(f"{question}: forbidden {forbidden}\n{result.answer}")

    allowed_modes = (mode,) if isinstance(mode, str) else mode
    if result.mode not in allowed_modes:
        raise AssertionError(f"{question}: expected mode {mode}, got {result.mode}")

    if result.route.category != route_category:
        raise AssertionError(f"{question}: expected route {route_category}, got {result.route.category}")

    if not result.validation.ok:
        raise AssertionError(f"{question}: validation errors {result.validation.errors}\n{result.answer}")

    print(f"OK {result.mode} {result.route.category} {result.elapsed:.4f}s | {question}")


def main() -> int:
    check(
        "เกมนี้มีปุ่มอะไรบ้าง",
        ["ยังไม่แน่ใจว่าหมายถึงเกมไหน", "TEKKEN 8", "Mario Kart 8 Deluxe"],
        must_not_contain=["NARUTO X BORUTO", "local://control_game"],
        mode="pipeline:game_control_missing_game_context",
    )
    check(
        "เล่นยังไง",
        ["ยังไม่แน่ใจว่าหมายถึงเกมไหน", "TEKKEN 8", "Mario Kart 8 Deluxe"],
        must_not_contain=["NARUTO X BORUTO", "local://control_game"],
        mode="pipeline:game_control_missing_game_context",
    )
    check(
        "ถามหลายๆอย่างเกี่ยวกับเกม",
        ["ถามเรื่องเกมได้", "มีเกมอะไรบ้าง", "TEKKEN 8 มีปุ่มอะไรบ้าง"],
        must_not_contain=["NARUTO X BORUTO", "The Legend of Zelda"],
        mode="pipeline:game_meta_clarification",
    )
    check(
        "มาริโอคาร์ทไลฟ์ปุ่มเร่งเครื่องกดอะไร",
        ["Mario Kart Live: Home Circuit", "ไม่พบ", "รายการเกมปัจจุบัน", "ไม่ดึงปุ่มของเกมอื่น"],
        must_not_contain=["ZR", "เร่งเครื่อง"],
        mode="pipeline:structured_game_controls_no_current_game",
    )
    check(
        "มาริโอคาร์ทไลฟ์ปุ่มทั้งหมดมีอะไรบ้าง",
        [
            "Mario Kart Live: Home Circuit",
            "ไม่พบ",
            "รายการเกมปัจจุบัน",
            "ไม่ดึงปุ่มของเกมอื่น",
        ],
        must_not_contain=["Left Stick", "D-Pad", "ZR"],
        mode="pipeline:structured_game_controls_no_current_game",
    )
    check(
        "Mario Kart 8 Deluxe ปุ่มทั้งหมดมีอะไรบ้าง",
        ["Mario Kart 8 Deluxe", "L (Left Stick)", "A", "B", "ZL", "ZR", "+ (Plus)"],
        must_not_contain=["Mario Kart Live: Home Circuit"],
    )
    check(
        "ปุ่มกระโดดใน Call of Duty กดอะไร",
        ["ยังไม่ชัด", "Call of Duty: Modern Warfare III", "Call of Duty: Warzone"],
        must_not_contain=["The Last of Us", "L1: กระโดด"],
        mode="pipeline:ambiguity_clarification",
        route_category="clarification",
    )
    check(
        "Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง",
        ["ยังไม่ชัด", "Call of Duty: Modern Warfare III", "Call of Duty: Warzone"],
        must_not_contain=["The Last of Us", "The Finals", "L1: กระโดด"],
        mode="pipeline:ambiguity_clarification",
        route_category="clarification",
    )
    check(
        "เทคเคน 8 ปุ่มเตะขวากดอะไร",
        ["TEKKEN 8", "Circle", "ลูกเตะขวา"],
        must_not_contain=["D-Pad Up", "Triangle", "Cross"],
    )
    check(
        "ปุ่มทั้งหมดของเทคเคน 8 มีอะไรบ้าง",
        ["TEKKEN 8", "Square", "Triangle", "Cross", "Circle", "D-Pad Up", "D-Pad Left", "D-Pad Down", "L1", "R1", "Options"],
    )
    check(
        "ลิตเติลไนท์แม ปุ่มวิ่งกดอะไร",
        ["Little Nightmares", "Square", "วิ่ง"],
    )
    check(
        "เกมเทคอิดเอ้าปุ่มกระโดดกดอะไร",
        ["It Takes Two", "Cross", "กระโดด"],
    )

    print("GAME CONTROL SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
