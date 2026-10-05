from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import _split_multi_question  # noqa: E402
from app.runtime.pipeline_answer import answer_question_pipeline_debug  # noqa: E402


CASES = [
    {
        "id": "compound_controls_two_games",
        "question": "Tekken 8 กับ Mario Kart มีปุ่มอะไรบ้าง",
        "split": ["Tekken 8 มีปุ่มอะไรบ้าง", "Mario Kart มีปุ่มอะไรบ้าง"],
        "must": ["Tekken 8 มีปุ่มอะไรบ้าง", "TEKKEN 8 มีข้อมูลปุ่ม", "Mario Kart มีปุ่มอะไรบ้าง", "Mario Kart 8 Deluxe มีข้อมูลปุ่ม"],
        "must_not": ["Naruto"],
    },
    {
        "id": "compound_controls_named_live_and_resident",
        "question": "Mario Kart Live กับ Resident Evil 4 ปุ่มอะไร",
        "split": ["Mario Kart Live ปุ่มอะไร", "Resident Evil 4 ปุ่มอะไร"],
        "must": ["Mario Kart Live ปุ่มอะไร", "Mario Kart Live: Home Circuit มีข้อมูลปุ่ม", "Resident Evil 4 ปุ่มอะไร", "Resident Evil 4"],
        "must_not": ["Naruto"],
    },
    {
        "id": "compound_game_and_booking_shared_subject",
        "question": "PS5 มีเกมอะไร แล้วจองยังไง",
        "split": ["PS5 มีเกมอะไร", "จะเล่น PS5 จองยังไง"],
        "must": ["PS5 มีเกมอะไร", "PlayStation 5 Zone", "PS5 จองยังไง", "จอง PlayStation 5"],
        "must_not": ["Local LLM"],
    },
    {
        "id": "compound_price_and_games_shared_subject",
        "question": "PC ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง",
        "split": ["PC ราคาเท่าไหร่", "PC มีเกมอะไรบ้าง"],
        "must": ["PC ราคาเท่าไหร่", "PSU Student and Staff", "70 บาท", "PC มีเกมอะไรบ้าง", "PC Zone (6 เกม)"],
        "must_not": ["Local LLM"],
    },
    {
        "id": "compound_controls_then_pc_price_explicit_new_subject",
        "question": "Tekken 8 ปุ่มอะไร แล้ว PC ราคาเท่าไหร่",
        "split": ["Tekken 8 ปุ่มอะไร", "PC ราคาเท่าไหร่"],
        "must": ["Tekken 8 ปุ่มอะไร", "TEKKEN 8 มีข้อมูลปุ่ม", "PC ราคาเท่าไหร่", "PSU Student and Staff", "70 บาท"],
        "must_not": ["Tekken 8 ราคาเท่าไหร่", "Naruto"],
    },
    {
        "id": "compound_pc_games_then_ps5_price_explicit_new_subject",
        "question": "PC มีเกมอะไร แล้ว PS5 ราคาเท่าไหร่",
        "split": ["PC มีเกมอะไร", "PS5 ราคาเท่าไหร่"],
        "must": ["PC มีเกมอะไร", "PC Zone (6 เกม)", "VALORANT", "PS5 ราคาเท่าไหร่", "150 บาท"],
        "must_not": ["pc_price_answer_missing_pc_local_update_source", "Local LLM"],
    },
    {
        "id": "compound_booking_then_pc_price_explicit_new_subject",
        "question": "PS5 จองยังไง แล้ว PC ราคาเท่าไหร่",
        "split": ["PS5 จองยังไง", "PC ราคาเท่าไหร่"],
        "must": ["PS5 จองยังไง", "จอง PlayStation 5", "PC ราคาเท่าไหร่", "General Adult", "70 บาท"],
        "must_not": ["PS5 ราคาเท่าไหร่", "Local LLM"],
    },
]


def _contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def main() -> int:
    failures: list[str] = []
    for case in CASES:
        question = case["question"]
        split = _split_multi_question(question)
        if split != case["split"]:
            failures.append(f"{case['id']}: split expected {case['split']}, got {split}")
            continue

        result = answer_question_pipeline_debug(question)
        answer = result.answer or ""
        if result.mode != "pipeline:multi_question_splitter":
            failures.append(f"{case['id']}: mode expected pipeline:multi_question_splitter, got {result.mode}")
        if not result.validation.ok:
            failures.append(f"{case['id']}: validation errors {result.validation.errors}")

        missing = [item for item in case["must"] if not _contains(answer, item)]
        forbidden = [item for item in case["must_not"] if _contains(answer, item)]
        if missing:
            failures.append(f"{case['id']}: missing answer text {missing}")
        if forbidden:
            failures.append(f"{case['id']}: forbidden answer text {forbidden}")

    if failures:
        print("COMPOUND QUESTION VALIDATION FAILED")
        for failure in failures:
            print("-", failure)
        return 1

    print("COMPOUND QUESTION VALIDATION OK")
    print(f"- cases: {len(CASES)}")
    print("- split / answer completeness / validation guard: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
