from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def check(question: str, *, domain: str, operation: str, must_contain: list[str]) -> None:
    result = answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=True,
        experimental_allow_llm=False,
    )
    intent = result.universal_intent
    if intent is None:
        raise AssertionError(f"{question}: missing universal intent")
    if intent.domain != domain or intent.operation != operation:
        raise AssertionError(
            f"{question}: expected {domain}/{operation}, got {intent.domain}/{intent.operation}\n{result.answer}"
        )
    missing = [text for text in must_contain if text.lower() not in result.answer.lower()]
    if missing:
        raise AssertionError(f"{question}: missing {missing}\n{result.answer}")
    print(f"OK {intent.domain}/{intent.operation} {result.mode} | {question}")


def check_mode(question: str, *, domain: str, operation: str, mode: str, must_contain: list[str]) -> None:
    result = answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=True,
        experimental_allow_llm=True,
    )
    intent = result.universal_intent
    if intent is None:
        raise AssertionError(f"{question}: missing universal intent")
    if intent.domain != domain or intent.operation != operation:
        raise AssertionError(
            f"{question}: expected {domain}/{operation}, got {intent.domain}/{intent.operation}\n{result.answer}"
        )
    if result.mode != mode:
        raise AssertionError(f"{question}: expected mode {mode}, got {result.mode}\n{result.answer}")
    missing = [text for text in must_contain if text.lower() not in result.answer.lower()]
    if missing:
        raise AssertionError(f"{question}: missing {missing}\n{result.answer}")
    print(f"OK {intent.domain}/{intent.operation} {result.mode} | {question}")


def main() -> int:
    check_mode(
        "สวัสดี",
        domain="knowledge",
        operation="detail",
        mode="pipeline:chatbot_greeting_fast_path",
        must_contain=["PSU Esports Assistant", "เกม", "วิธีจอง"],
    )
    check_mode(
        "ทำไรได้บ้าง",
        domain="knowledge",
        operation="detail",
        mode="pipeline:chatbot_identity_fast_path",
        must_contain=["PSU Esports Assistant", "เกม", "ค่าบริการ", "จอง"],
    )
    check(
        "สมาชิกใน PSU Esport มีกี่หมวด",
        domain="members",
        operation="group_count",
        must_contain=["3 หมวด", "Members", "cooperative education", "PSU Phuket Esports Club"],
    )
    check(
        "ตอนนี้สตาฟมีใครบ้าง",
        domain="members",
        operation="list",
        must_contain=["Members", "cooperative education", "PSU Phuket Esports Club"],
    )
    check(
        "เกมตอนนี้มีเกมอะไรบ้าง",
        domain="games",
        operation="list",
        must_contain=["42 เกม", "PC Zone", "Nintendo Switch Zone"],
    )
    check(
        "Nintendo มีเกมอะไรบ้าง",
        domain="games",
        operation="list",
        must_contain=["Nintendo Switch Zone"],
    )
    check(
        "PS5 มีเกมกี่เกม",
        domain="games",
        operation="count",
        must_contain=["PlayStation 5 Zone", "เกม"],
    )
    check(
        "เกมใน PS5 มีอะไรมั่ง",
        domain="games",
        operation="list",
        must_contain=["PlayStation 5 Zone", "TEKKEN 8"],
    )
    check(
        "Tekken 8",
        domain="games",
        operation="detail",
        must_contain=["TEKKEN 8", "PlayStation 5 Zone"],
    )
    check(
        "Over cook",
        domain="games",
        operation="detail",
        must_contain=["Overcooked", "Overcooked! 2"],
    )
    check(
        "TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง",
        domain="game_controls",
        operation="control",
        must_contain=["TEKKEN 8", "Square", "Triangle"],
    )
    check(
        "ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท",
        domain="service_fee",
        operation="price_calculate",
        must_contain=["2 ชั่วโมง", "2 session"],
    )
    check(
        "ใครเป็นผู้จัดการ",
        domain="members",
        operation="role_lookup",
        must_contain=["นายชนะชัย สิริพันธ์วราภรณ์", "ผู้จัดการ"],
    )
    check(
        "นายเป็นใคร",
        domain="knowledge",
        operation="detail",
        must_contain=["PSU Esports Assistant", "PSU Esports Studio - Phuket", "เกม", "วิธีจอง"],
    )
    print("UNIVERSAL INTENT SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
