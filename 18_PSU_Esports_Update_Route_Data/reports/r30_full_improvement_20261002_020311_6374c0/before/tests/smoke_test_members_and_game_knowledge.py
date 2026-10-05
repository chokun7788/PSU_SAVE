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
        ["Members", "cooperative education and Internship student", "PSU Phuket Esports Club - PSU Phuket", "นายชนะชัย", "นายษุภากรณ์"],
        mode="pipeline:structured_members_group_list",
    )
    check(
        "ตอนนี้สตาฟมีใครบ้าง",
        ["Members", "cooperative education and Internship student", "PSU Phuket Esports Club - PSU Phuket", "นายชนะชัย"],
        mode="pipeline:structured_members_group_list",
    )
    check(
        "staff มีใครบ้าง",
        ["Members", "cooperative education and Internship student", "PSU Phuket Esports Club - PSU Phuket", "นายชนะชัย"],
        mode="pipeline:structured_members_group_list",
    )
    check(
        "สตาฟเล่นเกมอะไรบ้าง",
        ["ยังไม่พบข้อมูลที่ยืนยันได้", "เล่นเกม/ดูแลเกมหรือโซนไหน", "หน้า Members"],
        mode="pipeline:structured_members_game_relation_no_data",
        must_not_contain=["สมาชิกจากหน้า Members แยกตามหมวด", "PlayStation 5 Zone", "Nintendo Switch Zone"],
    )
    check(
        "ใครดูแลเกม PS5",
        ["ยังไม่พบข้อมูลที่ยืนยันได้", "เล่นเกม/ดูแลเกมหรือโซนไหน", "หน้า Members"],
        mode="pipeline:structured_members_game_relation_no_data",
        must_not_contain=["สมาชิกจากหน้า Members แยกตามหมวด", "PlayStation 5 Zone", "Nintendo Switch Zone"],
    )
    check(
        "cooperative education and Internship student มีใครบ้าง",
        ["นายณภัทร", "Mr. Amine Abidellaoui", "นายสุพศิน", "Mr. Yanis Igoudjil", "นายภาสวุฒิ"],
        mode="pipeline:structured_members_group_list",
    )
    check(
        "กรรมการมีใครบ้าง",
        ["ตำแหน่ง กรรมการ", "8 คน", "นางสาวกมลวรรณ", "นางสาวชญาภา", "นายอรรถนนท์"],
        mode="pipeline:structured_members_role_lookup",
    )
    check(
        "นายชนะชัยทำตำแหน่งอะไร",
        ["นายชนะชัย สิริพันธ์วราภรณ์", "ผู้จัดการ"],
        mode="pipeline:structured_members_person_lookup",
    )
    check(
        "ใครเป็นผู้จัดการ",
        ["ตำแหน่ง ผู้จัดการ", "นายชนะชัย สิริพันธ์วราภรณ์", "Members"],
        mode="pipeline:structured_members_role_lookup",
    )
    check(
        "ใครเป็นนักวิชาการคอมพิวเตอร์",
        ["ตำแหน่ง นักวิชาการคอมพิวเตอร์", "นายพฤทธิ์ เกษตรสมบูรณ์", "นายณัฐวัฒน์ นิธิคุณานนต์"],
        mode="pipeline:structured_members_role_lookup",
    )
    check(
        "ตำแหน่งประธานคือใคร",
        ["ตำแหน่ง ประธาน", "นายษุภากรณ์ จิราจินดากุล"],
        mode="pipeline:structured_members_role_lookup",
        must_not_contain=["รองประธาน"],
    )
    check(
        "ใครทำตำแหน่ง AI Chat Bot Developer",
        ["นายภาสวุฒิ ชูติประชากิจ", "AI Chat Bot Developer"],
        mode="pipeline:structured_members_role_lookup",
    )
    check(
        "ใครทำแชทบอท",
        ["นายภาสวุฒิ ชูติประชากิจ", "AI Chat Bot Developer"],
        mode="pipeline:structured_members_role_lookup",
        must_not_contain=["สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน"],
    )
    check(
        "ใครทำ chatbot",
        ["นายภาสวุฒิ ชูติประชากิจ", "AI Chat Bot Developer"],
        mode="pipeline:structured_members_role_lookup",
        must_not_contain=["สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน"],
    )
    check(
        "คนทำแชทบอทคือใคร",
        ["นายภาสวุฒิ ชูติประชากิจ", "AI Chat Bot Developer"],
        mode="pipeline:structured_members_role_lookup",
        must_not_contain=["สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน"],
    )
    print("MEMBERS AND GAME KNOWLEDGE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
