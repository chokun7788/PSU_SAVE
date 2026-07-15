from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def check(question: str, must_contain: list[str], *, mode: str | None = None, must_not_contain: list[str] | None = None) -> None:
    result = answer_question_pipeline_debug(question, experimental_allow_llm=False)
    answer = result.answer
    missing = [item for item in must_contain if item.lower() not in answer.lower()]
    if missing:
        raise AssertionError(f"{question}: missing {missing}\n{answer}")
    forbidden = [item for item in (must_not_contain or []) if item.lower() in answer.lower()]
    if forbidden:
        raise AssertionError(f"{question}: forbidden {forbidden}\n{answer}")
    if mode and result.mode != mode:
        raise AssertionError(f"{question}: expected mode {mode}, got {result.mode}\n{answer}")
    if not result.validation.ok:
        raise AssertionError(f"{question}: validation errors {result.validation.errors}\n{answer}")
    print(f"OK {result.mode} {result.route.category}/{result.route.intent} {result.elapsed:.4f}s | {question}")


def main() -> int:
    check(
        "อะไรคือเกม ROV",
        ["RoV / Arena of Valor", "MOBA", "กติกาการแข่งขัน", "ยังไม่พบในรายการเกมให้เล่น"],
        mode="pipeline:game_detail_fast_path",
        must_not_contain=["เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด 36 เกม"],
    )
    check(
        "อะไรคือเกมมายคราฟ",
        ["Minecraft", "Sandbox", "ยังไม่พบในรายการเกมให้เล่น"],
        mode="pipeline:game_detail_fast_path",
    )
    check(
        "สมาชิกทีมมีใครบ้าง",
        ["Members:", "cooperative education and Internship student:", "PSU Phuket Esports Club - PSU Phuket:", "นายชนะชัย", "นายษุภากรณ์"],
        mode="pipeline:members_lookup_fast_path",
    )
    check(
        "cooperative education and Internship student มีใครบ้าง",
        ["นายณภัทร", "Mr. Amine Abidellaoui", "นายสุพศิน", "Mr. Yanis Igoudjil", "นายภาสวุฒิ"],
        mode="pipeline:members_lookup_fast_path",
    )
    check(
        "กรรมการมีใครบ้าง",
        ["นางสาวกมลวรรณ", "นางสาวชญาภา", "นายอรรถนนท์"],
        mode="pipeline:members_lookup_fast_path",
    )
    check(
        "นายชนะชัยทำตำแหน่งอะไร",
        ["นายชนะชัย สิริพันธ์วราภรณ์", "ผู้จัดการ"],
        mode="pipeline:members_person_lookup_fast_path",
    )
    print("MEMBERS AND GAME KNOWLEDGE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
