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


def ask(question: str):
    return answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )


def main() -> int:
    result = ask("เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค")
    if result.route.category != "general":
        raise AssertionError(f"text generation should route general, got {result.route.category}/{result.route.intent}")
    assert_not_contains(result.answer, ["ตำแหน่ง ประชาสัมพันธ์", "นายธนชาติ"], "text generation must not become member lookup")
    print("OK text generation does not hijack members")

    result = ask("Sony PlayStation VR2 คืออะไร")
    if result.mode != "pipeline:structured_equipment_item":
        raise AssertionError(f"PS VR2 should be equipment item, got {result.mode}")
    assert_contains(result.answer, ["Sony PlayStation VR2", "VR Zone"], "PS VR2 equipment item")
    assert_not_contains(result.answer, ["PlayStation 5 Slim With Ultra HD"], "PS VR2 must not answer PS5 Slim")
    print("OK PS VR2 item priority")

    result = ask("ถ้าจะเล่น Beat Saber ต้องจองอะไร")
    if result.mode != "pipeline:structured_booking_game_service_selection":
        raise AssertionError(f"Beat Saber booking should map by game, got {result.mode}")
    assert_contains(result.answer, ["Beat Saber", "VR Station 30 นาที", "VR Station 1 ชั่วโมง"], "Beat Saber booking")
    print("OK Beat Saber booking maps to VR Station")

    result = ask("ถ้าจะเล่น Horizon Call of the Mountain ต้องจองอะไร")
    if result.mode != "pipeline:structured_booking_game_service_selection":
        raise AssertionError(f"Horizon booking should map by game, got {result.mode}")
    assert_contains(result.answer, ["Horizon Call of the Mountain", "VR Station"], "Horizon booking")
    print("OK Horizon booking maps to VR Station")

    result = ask("TEKKEN 8 เล่นที่ไหน แล้ว Resident Evil Village ปุ่มอะไร")
    if result.mode != "pipeline:multi_question_splitter":
        raise AssertionError(f"compound game question should split, got {result.mode}")
    assert_contains(result.answer, ["TEKKEN 8 เล่นที่ไหน", "PC Zone", "Resident Evil Village ปุ่มอะไร"], "compound game split")
    print("OK mixed game compound split")

    result = ask("Beat Saber ถ้าจะหลบและจัดตำแหน่งร่างกายต้องกดอะไร")
    if result.mode != "pipeline:structured_game_controls":
        raise AssertionError(f"single action control should not split, got {result.mode}")
    assert_contains(result.answer, ["Head/body movement", "หลบและจัดตำแหน่งร่างกาย"], "Beat Saber body movement control")
    print("OK single Beat Saber body movement control")

    result = ask("ช่วงเช้าวันจันทร์เปิดไหม")
    assert_contains(result.answer, ["ปิด/ไม่เปิดให้จองเล่น", "Maintenance"], "Monday morning closed wording")
    print("OK closed schedule wording")

    print("FULL EVAL REGRESSION FIXES SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
