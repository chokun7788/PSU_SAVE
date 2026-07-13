from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.session.context_resolver import resolve_question_with_context  # noqa: E402


def answer_with_context(question: str, recent_history: list[dict[str, str]]):
    resolved = resolve_question_with_context(question, recent_history)
    result = answer_question_pipeline_debug(resolved.resolved_question)
    return resolved, result


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item.lower() not in text.lower()]
    if missing:
        raise AssertionError(f"{label}: missing {missing}\n{text}")


def assert_not_contains(text: str, forbidden: list[str], label: str) -> None:
    found = [item for item in forbidden if item.lower() in text.lower()]
    if found:
        raise AssertionError(f"{label}: forbidden {found}\n{text}")


def main() -> int:
    mario_party_history = [
        {"role": "user", "text": "เกมมาริโอ้ปาตี้"},
        {
            "role": "assistant",
            "text": "Mario Party Superstars คือเกมปาร์ตี้ที่เล่นบนกระดานและแข่งมินิเกมกับเพื่อน",
        },
    ]

    resolved, result = answer_with_context("เล่นยังไง", mario_party_history)
    assert resolved.used_context, resolved
    assert resolved.context_game == "Mario Party Superstars", resolved
    assert_contains(resolved.resolved_question, ["Mario Party Superstars", "เล่นยังไง"], "resolved play")
    assert_contains(result.answer, ["Mario Party Superstars", "ทอยลูกเต๋า", "มินิเกม"], "answer play")
    print("OK context follow-up: Mario Party เล่นยังไง")

    resolved, result = answer_with_context("มีปุ่มอะไรบ้าง", mario_party_history)
    assert resolved.used_context, resolved
    assert_contains(resolved.resolved_question, ["Mario Party Superstars", "มีปุ่มอะไรบ้าง"], "resolved controls")
    assert_contains(result.answer, ["ยังไม่พบข้อมูลปุ่มควบคุม", "Mario Party Superstars"], "answer no controls")
    assert_not_contains(result.answer, ["Super Mario Odyssey", "Mario Kart 8 Deluxe"], "answer no wrong game")
    print("OK context follow-up: Mario Party controls no-answer")

    resolved = resolve_question_with_context("จองเครื่องยังไง", mario_party_history)
    if resolved.used_context:
        raise AssertionError(f"booking topic shift should not inherit context: {resolved}")
    if "Mario Party" in resolved.resolved_question:
        raise AssertionError(f"booking topic shift leaked game context: {resolved}")
    print("OK topic shift: booking does not inherit game")

    live_history = [
        {"role": "user", "text": "มาริโอคาร์ทไลฟ์คือเกมอะไร"},
        {"role": "assistant", "text": "Mario Kart Live: Home Circuit เล่นได้ที่ Nintendo Switch Zone"},
    ]
    resolved, result = answer_with_context("ปุ่มเร่งเครื่องกดอะไร", live_history)
    assert resolved.used_context, resolved
    assert_contains(result.answer, ["Mario Kart Live: Home Circuit", "A", "เร่งเครื่อง"], "answer live accelerate")
    assert_not_contains(result.answer, ["Mario Kart 8 Deluxe"], "answer live not mk8")
    print("OK context follow-up: Mario Kart Live controls")

    print("SESSION CONTEXT SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
