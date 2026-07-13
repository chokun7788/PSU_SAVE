from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "reports" / "pipeline_ground_truth_results_quality_pipeline_round4_group_fix_20260701.jsonl"
REPORT_DIR = ROOT / "reports"

sys.path.insert(0, str(ROOT))
from app.core.normalization import normalize_text  # noqa: E402
from app.runtime.fast_answer import PRICE_VALUES, _detect_group, _service_keys_for_query  # noqa: E402


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def direct_answer(answer: str) -> str:
    value = re.split(r"\n\s*\nรายละเอียดจากตาราง:", answer, maxsplit=1)[0]
    value = re.split(r"\nแหล่งข้อมูล:", value, maxsplit=1)[0]
    return value.strip()


def first_line(answer: str) -> str:
    for line in answer.splitlines():
        if line.strip():
            return line.strip()
    return ""


def has_any(text: str, *terms: str) -> bool:
    return any(term in text for term in terms)


def promote_decision(current: str, new: str) -> str:
    order = {"pass": 0, "minor_fix": 1, "major_fix": 2, "needs_data": 2, "needs_policy": 2}
    return new if order.get(new, 0) > order.get(current, 0) else current


def add_issue(issues: list[str], text: str, decision: str, current: str) -> str:
    issues.append(text)
    return promote_decision(current, decision)


def audit_service_fee(row: dict[str, Any], direct: str, q: str) -> tuple[str, int, list[str], list[str]]:
    decision = "pass"
    score = 4
    issues: list[str] = []
    suggestions: list[str] = []

    group = _detect_group(q)
    keys = _service_keys_for_query(q)
    direct_norm = direct.lower().replace(",", "")

    if "pc" in q or "คอม" in q:
        if "ไม่พบ" in direct and ("pc" in direct.lower() or "PC" in direct):
            return decision, score, issues, suggestions
        decision = add_issue(issues, "คำถาม PC ควรตอบว่าไม่พบราคาที่ยืนยันได้ ไม่ควรคำนวณราคาเอง", "major_fix", decision)
        suggestions.append("ตอบว่า Service Fee 2026 ยังไม่มีราคา PC ที่ยืนยันได้")
        return decision, 1, issues, suggestions

    if group and len(keys) == 1:
        expected_price = PRICE_VALUES[keys[0]][group]
        if f"{expected_price} บาท" not in direct_norm and f"ราคา {expected_price}" not in direct_norm:
            decision = add_issue(
                issues,
                f"คำตอบหลักควรมีราคา {expected_price} บาท สำหรับกลุ่มที่ถาม แต่ไม่พบในคำตอบหลัก",
                "major_fix",
                decision,
            )
            suggestions.append(f"ให้ขึ้นต้นด้วยราคา {expected_price} บาท แล้วค่อยตามรายละเอียดจากตาราง")
            score = min(score, 1)
        if group == "psu" and "general adult" in direct.lower():
            decision = add_issue(issues, "จับกลุ่มผิด: คำถามเป็นเด็ก/นักศึกษา PSU แต่ตอบเป็น General Adult", "major_fix", decision)
            score = min(score, 0)
        if group == "general_student" and "general adult" in direct.lower():
            decision = add_issue(issues, "จับกลุ่มผิด: คำถามเป็นต่างมหาลัย/General Student แต่ตอบเป็น General Adult", "major_fix", decision)
            score = min(score, 0)

    if group and "ยังไม่ทราบกลุ่มผู้ใช้" in direct:
        decision = add_issue(issues, "คำถามระบุกลุ่มแล้ว แต่ระบบยังตอบว่าไม่ทราบกลุ่มผู้ใช้", "major_fix", decision)
        score = min(score, 1)

    if "ต่างกัน" in q:
        if not first_line(direct).startswith("ต่างกัน"):
            decision = add_issue(issues, "คำถามถามว่าส่วนต่างเท่าไหร่ แต่ไม่ได้ตอบส่วนต่างเป็นประโยคแรก", "minor_fix", decision)
            suggestions.append("ขึ้นต้นว่า ต่างกัน X บาท ก่อนแจกแจงราคาแต่ละตัว")
            score = min(score, 3)

    for keyword in row.get("expected_keywords", []):
        key = str(keyword).lower().replace(",", "")
        if key not in direct_norm:
            decision = add_issue(issues, f"keyword เฉลย `{keyword}` ไม่อยู่ในคำตอบหลัก", "major_fix", decision)
            score = min(score, 1)

    return decision, score, issues, suggestions


def audit_schedule(row: dict[str, Any], direct: str, q: str) -> tuple[str, int, list[str], list[str]]:
    decision = "pass"
    score = 4
    issues: list[str] = []
    suggestions: list[str] = []
    first = first_line(direct)

    asks_24 = "24" in q
    asks_monday = has_any(q, "จันทร์", "วันจัน", "monday")
    asks_friday = has_any(q, "ศุกร์", "friday")
    asks_morning = has_any(q, "morning", "รอบเช้า", "ช่วงเช้า", "ตอนเช้า", "09:00", "9 โมง")
    asks_afternoon = has_any(q, "afternoon", "รอบบ่าย", "ช่วงบ่าย", "ตอนบ่าย", "13:00", "บ่าย")
    q_without_open = q.replace("เปิด", "")
    asks_open = "เปิด" in q or "opening" in q
    asks_close = "ปิด" in q_without_open or "closing" in q or "ถึงกี่โมง" in q
    asks_open_close = ("เปิดปิด" in q) or (asks_open and asks_close) or "open close" in q or "service hours" in q

    if not asks_24 and ("24 ชั่วโมง" in direct or "24 hours" in direct.lower()):
        decision = add_issue(issues, "พูดเรื่องเปิด 24 ชั่วโมงทั้งที่ผู้ใช้ไม่ได้ถาม", "minor_fix", decision)
        score = min(score, 3)

    if asks_24 and not first.startswith("ไม่เปิด 24"):
        decision = add_issue(issues, "คำถามถามว่าเปิด 24 ชม. ไหม ควรตอบตรง ๆ ว่าไม่เปิด 24 ชั่วโมงก่อน", "major_fix", decision)
        score = min(score, 1)

    if asks_monday and asks_morning and "Maintenance" not in direct:
        decision = add_issue(issues, "วันจันทร์ช่วงเช้าควรระบุว่าเป็น Maintenance", "major_fix", decision)
        score = min(score, 1)

    if asks_monday and asks_afternoon and not all(term in direct for term in ["13:00", "16:00"]):
        decision = add_issue(issues, "วันจันทร์ช่วงบ่ายควรระบุ 13:00-16:00", "major_fix", decision)
        score = min(score, 1)

    if asks_friday and asks_afternoon and "Maintenance" not in direct:
        decision = add_issue(issues, "วันศุกร์ช่วงบ่ายควรระบุว่าเป็น Maintenance", "major_fix", decision)
        score = min(score, 1)

    if asks_open_close and not asks_monday and not asks_friday and not asks_morning and not asks_afternoon and "09:00" not in first:
        decision = add_issue(issues, "คำถามถามเปิด-ปิดทั่วไป คำตอบแรกควรบอกช่วงเวลาเริ่ม 09:00 และปิด/สิ้นสุด 16:00", "minor_fix", decision)
        suggestions.append("ขึ้นต้นด้วย Morning 09:00-12:00 และ Afternoon 13:00-16:00 แล้วค่อยบอก Maintenance")
        score = min(score, 3)

    if asks_open and not asks_close and not asks_monday and not asks_friday and not asks_morning and not asks_afternoon and "09:00" not in first:
        decision = add_issue(issues, "คำถามถามเวลาเปิดทั่วไป คำตอบแรกควรบอกช่วงเวลาเริ่ม 09:00", "minor_fix", decision)
        suggestions.append("ขึ้นต้นด้วย Morning 09:00-12:00 และ Afternoon 13:00-16:00")
        score = min(score, 3)

    return decision, score, issues, suggestions


def audit_no_answer(row: dict[str, Any], direct: str, q: str) -> tuple[str, int, list[str], list[str]]:
    if "ไม่พบข้อมูล" in direct:
        return "pass", 4, [], []
    return "major_fix", 1, ["หมวด no_answer ควรตอบว่าไม่พบข้อมูลที่ยืนยันได้"], ["อย่าเดาข้อมูลที่ไม่มีในฐานข้อมูล"]


def audit_about_us(row: dict[str, Any], direct: str, q: str) -> tuple[str, int, list[str], list[str]]:
    decision = "pass"
    score = 4
    issues: list[str] = []
    suggestions: list[str] = []

    expected_by_intent = [
        ("อธิการบดี", "ผศ.ดร.นิวัติ แก้วประดับ"),
        ("คณบดี", "รศ.ดร.อซีส นันทอมรพงศ์"),
        ("ผู้จัดการศูนย์", "นายชนะชัย สิริพันธ์วราภรณ์"),
        ("ประธาน", "นายษุภากรณ์ จิราจินดากุล"),
    ]
    for trigger, expected in expected_by_intent:
        if trigger in q and expected not in direct:
            decision = add_issue(
                issues,
                f"คำถามถามว่า `{trigger}` คือใคร แต่คำตอบหลักยังไม่มีชื่อ `{expected}`",
                "major_fix",
                decision,
            )
            suggestions.append(f"ตอบชื่อ `{expected}` เป็นประโยคแรก แล้วค่อยใส่ตำแหน่ง/แหล่งข้อมูล")
            score = min(score, 1)

    if "gallery" in q:
        if "Nintendo Switch" not in direct or "PlayStation 5" not in direct:
            decision = add_issue(
                issues,
                "คำถาม Gallery ควรระบุหมวดภาพ Nintendo Switch และ PlayStation 5 ให้ครบ",
                "major_fix",
                decision,
            )
            suggestions.append("ตอบว่า หน้า Gallery มีหมวดภาพ Nintendo Switch และ PlayStation 5")
            score = min(score, 1)

    return decision, score, issues, suggestions


def audit_events_news(row: dict[str, Any], direct: str, q: str) -> tuple[str, int, list[str], list[str]]:
    decision = "pass"
    score = 4
    issues: list[str] = []
    suggestions: list[str] = []

    expected_by_intent = [
        ("25 เมษายน", "PSU Phuket CS 2 2026"),
        ("valorant 2026", "21 กุมภาพันธ์ 2569"),
        ("surat smash", "4 คน"),
        ("นักศึกษาชาวจีน", "11 คน"),
        ("game on", "ม.3"),
    ]
    for trigger, expected in expected_by_intent:
        if trigger in q and expected not in direct:
            decision = add_issue(
                issues,
                f"คำถามข่าว `{trigger}` ควรตอบ `{expected}` ในคำตอบหลัก",
                "major_fix",
                decision,
            )
            suggestions.append("ตอบข้อมูลที่ผู้ใช้ถามก่อน แล้วค่อยใส่รายละเอียดอื่นเท่าที่จำเป็น")
            score = min(score, 1)

    if len([trigger for trigger, _ in expected_by_intent if trigger in q]) == 1:
        if first_line(direct).startswith("ข่าวของ PSU Esports Studio"):
            decision = add_issue(
                issues,
                "คำถามถามข่าวเฉพาะเรื่อง แต่คำตอบเริ่มด้วยสรุปข่าวทั้งหมด ทำให้อ่านยาก",
                "minor_fix",
                decision,
            )
            suggestions.append("ขึ้นต้นด้วยคำตอบเฉพาะเรื่อง เช่น `SURAT SMASH ส่งตัวแทน 4 คน`")
            score = min(score, 3)

    return decision, score, issues, suggestions


def audit_answer(row: dict[str, Any]) -> dict[str, Any]:
    q = normalize_text(str(row.get("question", "")))
    answer = str(row.get("answer", ""))
    direct = direct_answer(answer)
    category = str(row.get("category") or "")
    route = str(row.get("route_category") or "")
    decision = "pass"
    score = 4
    issues: list[str] = []
    suggestions: list[str] = []

    if row.get("verdict") != "PASS":
        decision = add_issue(issues, "auto evaluator ไม่ผ่าน", "major_fix", decision)
        score = min(score, 1)

    if category == "service_fee":
        decision, score, issues, suggestions = audit_service_fee(row, direct, q)
    elif route == "schedule" or (category == "reservation" and has_any(q, "เปิด", "ปิด", "เวลา", "morning", "afternoon", "24", "จันทร์", "ศุกร์")):
        decision, score, issues, suggestions = audit_schedule(row, direct, q)
    elif category == "no_answer":
        decision, score, issues, suggestions = audit_no_answer(row, direct, q)
    elif category == "about_us":
        decision, score, issues, suggestions = audit_about_us(row, direct, q)
    elif category == "events_news":
        decision, score, issues, suggestions = audit_events_news(row, direct, q)
    else:
        for keyword in row.get("expected_keywords", []):
            if str(keyword).lower() not in answer.lower():
                decision = add_issue(issues, f"ไม่พบ keyword เฉลย `{keyword}` ในคำตอบ", "major_fix", decision)
                score = min(score, 1)

    if route == "general" and category not in {"no_answer"}:
        decision = add_issue(issues, "route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน อาจควรปรับ router", "minor_fix", decision)
        score = min(score, 3)

    if not issues:
        issues.append("ตรวจด้วย audit heuristic แล้วไม่พบปัญหาหลัก")

    return {
        "id": row.get("id"),
        "category": category,
        "route_category": route,
        "mode": row.get("mode"),
        "question": row.get("question"),
        "answer": answer,
        "direct_answer": direct,
        "auto_verdict": row.get("verdict"),
        "audit_decision": decision,
        "audit_score_0_4": score,
        "audit_issues": issues,
        "fix_suggestions": suggestions,
        "latency_sec": row.get("latency_sec"),
    }


def build_markdown(rows: list[dict[str, Any]], source: Path, out_jsonl: Path) -> str:
    counts = Counter(row["audit_decision"] for row in rows)
    by_category: dict[str, Counter] = defaultdict(Counter)
    for row in rows:
        by_category[str(row["category"])][row["audit_decision"]] += 1

    lines = [
        "# Answer Audit Report - PSU Esports Chatbot",
        "",
        f"สร้างเมื่อ: {datetime.now().isoformat(timespec='seconds')}",
        f"Source results: `{source}`",
        f"Audit JSONL: `{out_jsonl}`",
        "",
        "## Summary",
        "",
        f"- Total: {len(rows)}",
    ]
    for key in ["pass", "minor_fix", "major_fix", "needs_data", "needs_policy"]:
        lines.append(f"- {key}: {counts.get(key, 0)}")

    lines.extend(["", "## By Category", "", "| Category | pass | minor_fix | major_fix | needs_data | needs_policy |", "|---|---:|---:|---:|---:|---:|"])
    for category, counter in sorted(by_category.items()):
        lines.append(
            f"| {category} | {counter.get('pass', 0)} | {counter.get('minor_fix', 0)} | {counter.get('major_fix', 0)} | {counter.get('needs_data', 0)} | {counter.get('needs_policy', 0)} |"
        )

    attention = [row for row in rows if row["audit_decision"] != "pass"]
    lines.extend(["", "## Items To Review", ""])
    if not attention:
        lines.append("ไม่พบข้อที่ audit heuristic มองว่าต้องแก้")
    else:
        for row in attention:
            lines.extend(
                [
                    f"### {row['id']} - {row['audit_decision']} - score {row['audit_score_0_4']}/4",
                    "",
                    f"- หมวด: `{row['category']}` | route: `{row['route_category']}` | mode: `{row['mode']}`",
                    f"- คำถาม: {row['question']}",
                    "- คำตอบหลัก:",
                    "",
                    "```text",
                    row["direct_answer"],
                    "```",
                    "- ปัญหาที่พบ:",
                ]
            )
            for issue in row["audit_issues"]:
                lines.append(f"  - {issue}")
            if row["fix_suggestions"]:
                lines.append("- แนวทางแก้:")
                for suggestion in row["fix_suggestions"]:
                    lines.append(f"  - {suggestion}")
            lines.append("")

    lines.extend(["", "## All Items", ""])
    for idx, row in enumerate(rows, 1):
        lines.extend(
            [
                f"### {idx}. {row['id']} [{row['audit_decision']}]",
                "",
                f"- หมวด: `{row['category']}` | route: `{row['route_category']}` | score: `{row['audit_score_0_4']}/4`",
                f"- คำถาม: {row['question']}",
                "- คำตอบหลัก:",
                "",
                "```text",
                row["direct_answer"],
                "```",
                "- เหตุผล audit: " + "; ".join(row["audit_issues"]),
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", default=str(DEFAULT_RESULTS))
    parser.add_argument("--label", default="round5_audit_20260701")
    args = parser.parse_args()

    source = Path(args.results)
    rows = [audit_answer(row) for row in read_jsonl(source)]
    out_jsonl = REPORT_DIR / f"answer_audit_results_{args.label}.jsonl"
    out_md = REPORT_DIR / f"answer_audit_report_{args.label}.md"
    write_jsonl(out_jsonl, rows)
    out_md.write_text(build_markdown(rows, source, out_jsonl), encoding="utf-8", newline="\n")

    counts = Counter(row["audit_decision"] for row in rows)
    print(f"Audit rows: {len(rows)}")
    print(dict(counts))
    print(out_md)
    print(out_jsonl)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
