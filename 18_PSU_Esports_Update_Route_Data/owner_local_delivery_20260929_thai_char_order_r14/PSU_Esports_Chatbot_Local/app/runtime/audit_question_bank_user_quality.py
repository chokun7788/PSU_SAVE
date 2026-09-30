from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


DEFAULT_RUN_DIR = PROJECT_ROOT / "data" / "eval" / "question_bank_runs" / "20260721_000537_decision_artifact_baseline_400"
DEFAULT_OUTPUT_ROOT = PROJECT_ROOT / "data" / "eval" / "audits"


RUBRIC = {
    "correctness": {
        "max": 4.0,
        "description": "ตอบถูกตามข้อมูลที่ควรใช้ ไม่สลับ domain ไม่มั่วข้อมูล และไม่ตอบขัดกับ expected_support",
    },
    "relevance": {
        "max": 2.0,
        "description": "ตอบตรงคำถามก่อน ไม่ตอบกว้างเกิน ไม่ลาก catalog หรือ policy อื่นมาแทนสิ่งที่ถาม",
    },
    "evidence": {
        "max": 1.5,
        "description": "มีแหล่งข้อมูล/section/source id ชัดเจน และ source สอดคล้องกับคำตอบ",
    },
    "completeness": {
        "max": 1.5,
        "description": "รายละเอียดพอใช้จริง ครอบคลุมสิ่งที่ user ต้องการ เช่น จำนวน เวลา ปุ่ม ขั้นตอน หรือข้อจำกัด",
    },
    "clarity": {
        "max": 1.0,
        "description": "อ่านง่าย กระชับ จัด format ดี ไม่ยาวเกินสำหรับคำถามเฉพาะ และไม่ทำให้ user งง",
    },
}


def _load_rows(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def _compact(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _has(text: str, *terms: str) -> bool:
    low = (text or "").lower()
    return any(term.lower() in low for term in terms)


def _starts_with_wrong_catalog(answer: str, question: str) -> bool:
    return _has(
        answer,
        "ทั้งหมด 44 เกม",
        "ทั้งหมด 42 เกม",
        "PC Zone (6 เกม)",
        "PlayStation 5 Zone (23 เกม)",
        "PlayStation 5 Zone (17 เกม)",
    ) and _has(
        question,
        "rov",
        "valorant",
        "cs2",
        "tekken",
        "มายคราฟ",
        "minecraft",
    )


def _looks_like_no_answer(answer: str, mode: str) -> bool:
    return "no_answer" in mode or _has(
        answer,
        "ยังไม่พบข้อมูล",
        "ไม่พบข้อมูล",
        "ยังไม่ได้เปิด",
        "general_llm_disabled",
        "ตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิด",
    )


def _expected_domain_ok(row: dict[str, Any]) -> bool:
    expected = str(row.get("expected_support") or "")
    route = str(row.get("route") or "")
    mode = str(row.get("mode") or "")
    candidate = str(row.get("selected_candidate_id") or "")
    source_ids = " ".join(str(x) for x in row.get("source_ids") or [])
    answer = str(row.get("answer") or "")

    if expected == "competition_rules":
        return "competition_rules" in route or "competition" in source_ids or "competition" in candidate or "competition" in mode
    if expected == "game_controls_or_clarification":
        return "game_control" in route or "game_control" in mode or "clarification" in mode or "control" in source_ids
    if expected == "general_llm_or_decline":
        return "general" in route or "llm" in mode or _looks_like_no_answer(answer, mode)
    if expected in {"in_kb", "in_kb_or_catalog"}:
        return bool(row.get("source_ids")) or "structured" in mode or "fast_path" in mode
    return True


def _question_requires_direct_number(question: str) -> bool:
    return _has(question, "กี่", "เท่าไหร่", "กี่คน", "กี่เครื่อง", "กี่ชุด", "กี่บาท", "กี่โมง", "กี่นาที", "กี่ชั่วโมง")


def _answer_has_number(answer: str) -> bool:
    return bool(re.search(r"\d|หนึ่ง|สอง|สาม|สี่|ห้า|หก|เจ็ด|แปด|เก้า|สิบ", answer or ""))


def _reservation_question_answered_as_equipment(question: str, answer: str, mode: str) -> bool:
    if not _has(question, "จอง"):
        return False
    if "structured_equipment" in mode:
        return True
    return _has(answer, "Nintendo Switch OLED:", "Gaming PC รุ่น", "Logitech G923", "PlayStation 5 Slim:") and not _has(
        answer,
        "จอง",
        "ระบบจอง",
        "ล่วงหน้า",
        "ชำระ",
    )


def _wrong_equipment_focus(question: str, answer: str) -> bool:
    first = _compact(answer)[:160].lower()
    q = question.lower()
    a = answer.lower()

    display_question = (
        "monitor" in q
        or "หน้าจอ" in q
        or "จอภาพ" in q
        or ("จอ" in q and "จอย" not in q)
    )
    checks = []
    if display_question:
        checks.append((("monitor", "จอ"), ("gaming pc", "logitech")))
    if "ทีวี" in q or re.search(r"\btv\b", q):
        checks.append((("tv", "ทีวี", "นิ้ว"), ("logitech", "gaming pc", "playstation 5 slim")))
    if "พวงมาลัย" in q or "wheel" in q:
        checks.append((("logitech", "g923", "พวงมาลัย", "wheel"), ("tv 65",)))
    if ("คอม" in q or re.search(r"\bpc\b", q)) and "เปิดไม่ติด" not in q and "ไม่ให้ช้า" not in q:
        checks.append((("gaming pc", "คอม"), ("monitor", "logitech")))

    for required, wrong_first in checks:
        if not any(term in a for term in required):
            return True
        if any(term in first for term in wrong_first) and not any(term in first for term in required):
            return True
    return False


def _route_mismatch_penalty(row: dict[str, Any]) -> bool:
    expected = str(row.get("expected_support") or "")
    if expected == "competition_rules" and not _expected_domain_ok(row):
        return True
    question = str(row.get("question") or "")
    route = str(row.get("route") or "")
    if _has(question, "จอง", "เช็คอิน", "สลิป", "ชำระ", "ยกเลิก") and not any(
        part in route for part in ("reservation", "service_fee", "contact")
    ):
        return True
    return False


def audit_row(row: dict[str, Any]) -> dict[str, Any]:
    question = str(row.get("question") or "")
    answer = str(row.get("answer") or "")
    mode = str(row.get("mode") or "")
    expected = str(row.get("expected_support") or "")
    route = str(row.get("route") or "")

    scores = {
        "correctness": 4.0,
        "relevance": 2.0,
        "evidence": 1.5,
        "completeness": 1.5,
        "clarity": 1.0,
    }
    issue_tags: list[str] = []
    user_problem: list[str] = []

    if not _expected_domain_ok(row):
        scores["correctness"] -= 2.2
        scores["relevance"] -= 0.8
        scores["evidence"] -= 0.7
        issue_tags.append("wrong_domain_or_source")
        user_problem.append("คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ")

    if _starts_with_wrong_catalog(answer, question):
        scores["correctness"] -= 1.8
        scores["relevance"] -= 1.2
        scores["completeness"] -= 0.8
        scores["clarity"] -= 0.3
        issue_tags.append("specific_question_answered_with_full_catalog")
        user_problem.append("ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม")

    if _reservation_question_answered_as_equipment(question, answer, mode):
        scores["correctness"] -= 2.0
        scores["relevance"] -= 1.0
        scores["completeness"] -= 0.6
        issue_tags.append("reservation_question_answered_as_equipment")
        user_problem.append("ผู้ใช้ถามวิธีจอง/เงื่อนไขจอง แต่ระบบตอบรายละเอียดอุปกรณ์แทน")

    if expected != "general_llm_or_decline" and _wrong_equipment_focus(question, answer):
        scores["correctness"] -= 1.8
        scores["relevance"] -= 0.9
        scores["completeness"] -= 0.5
        issue_tags.append("wrong_equipment_focus")
        user_problem.append("คำถามเจาะอุปกรณ์ชิ้นหนึ่ง แต่ระบบโฟกัสอุปกรณ์อีกชิ้น")

    if _question_requires_direct_number(question) and not _answer_has_number(answer):
        scores["correctness"] -= 1.2
        scores["relevance"] -= 0.6
        scores["completeness"] -= 0.5
        issue_tags.append("missing_direct_number")
        user_problem.append("คำถามต้องการตัวเลข/จำนวน แต่คำตอบไม่มีตัวเลขตรง ๆ")

    if _question_requires_direct_number(question) and _answer_has_number(answer) and len(_compact(answer)) > 900:
        scores["relevance"] -= 0.4
        scores["clarity"] -= 0.2
        issue_tags.append("number_answer_too_verbose")
        user_problem.append("มีตัวเลขอยู่ แต่คำตอบยาวเกินและไม่ได้ตอบตัวเลขก่อน")

    if _looks_like_no_answer(answer, mode):
        if expected == "general_llm_or_decline":
            scores["correctness"] -= 1.0
            scores["relevance"] -= 0.4
            scores["completeness"] -= 0.8
            issue_tags.append("safe_decline_but_not_useful")
            user_problem.append("เป็นคำถามนอกเรื่องที่ควรให้ Local LLM ช่วยได้ แต่รอบนี้ปิด LLM จึงตอบไม่ได้")
        else:
            scores["correctness"] -= 2.0
            scores["relevance"] -= 0.8
            scores["completeness"] -= 0.8
            issue_tags.append("no_answer_for_supported_question")
            user_problem.append("คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล")

    if len(_compact(answer)) > 1800 and not _has(question, "ทั้งหมด", "มีอะไรบ้าง", "ครบ", "list", "รายการ"):
        scores["relevance"] -= 0.5
        scores["clarity"] -= 0.4
        issue_tags.append("too_long_for_specific_question")
        user_problem.append("คำตอบยาวเกินสำหรับคำถามเฉพาะ ทำให้หาคำตอบหลักยาก")

    if not row.get("source_ids"):
        scores["evidence"] -= 0.8
        issue_tags.append("missing_source_id")
        user_problem.append("ไม่มี source id ให้ตรวจสอบย้อนกลับ")

    if expected == "competition_rules" and row.get("source_ids") and not any("competition" in str(x) for x in row.get("source_ids") or []):
        scores["evidence"] -= 0.5
        issue_tags.append("source_not_specific_enough")
        user_problem.append("แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง")

    if "structured" in str(row.get("selected_candidate_id") or "") and "fast_path" in mode:
        issue_tags.append("candidate_execution_mismatch")
        user_problem.append("ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน")

    if route == "general/unknown_domain_query" and expected != "general_llm_or_decline":
        scores["correctness"] -= 1.0
        scores["relevance"] -= 0.5
        issue_tags.append("weak_general_route_for_supported_question")
        user_problem.append("คำถามที่ควรอยู่ในฐานข้อมูลถูก route เป็น general/unknown")

    scores = {key: max(0.0, round(value, 2)) for key, value in scores.items()}
    total = round(sum(scores.values()), 2)
    if total >= 8.5:
        level = "good"
    elif total >= 7.0:
        level = "usable"
    elif total >= 5.0:
        level = "needs_review"
    else:
        level = "bad"

    if not issue_tags:
        issue_tags.append("no_major_issue_detected")
        user_problem.append("ไม่พบปัญหาใหญ่จากกฎ audit รอบนี้")

    return {
        **row,
        "score_total": total,
        "score_level": level,
        "score_correctness": scores["correctness"],
        "score_relevance": scores["relevance"],
        "score_evidence": scores["evidence"],
        "score_completeness": scores["completeness"],
        "score_clarity": scores["clarity"],
        "issue_tags": issue_tags,
        "user_problem": user_problem,
    }


def _write_rubric(path: Path) -> None:
    lines = [
        "# User Quality Audit Rubric",
        "",
        "คะแนนเต็ม 10 ใช้ประเมินว่า ถ้าเป็นผู้ใช้จริงถามคำถามนั้นแล้วได้คำตอบนี้ จะใช้งานได้ดีแค่ไหน",
        "",
        "| เกณฑ์ | คะแนน | ความหมาย |",
        "|---|---:|---|",
    ]
    for key, item in RUBRIC.items():
        lines.append(f"| {key} | {item['max']} | {item['description']} |")
    lines.extend([
        "",
        "ระดับคะแนน:",
        "",
        "•    8.5-10 = good: ใช้ได้ดี",
        "•    7.0-8.49 = usable: ใช้ได้แต่ควรปรับ",
        "•    5.0-6.99 = needs_review: ผู้ใช้มีโอกาสสับสนหรือไม่ได้คำตอบครบ",
        "•    0-4.99 = bad: ตอบผิดทาง/ไม่ตอบคำถาม/ใช้งานจริงมีปัญหาชัดเจน",
        "",
        "หมายเหตุ: audit รอบนี้เป็น heuristic user-review pass สำหรับไล่ปัญหา 400 ข้อให้เร็ว ไม่ใช่ human ground truth ขั้นสุดท้าย",
    ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "id",
        "category",
        "question_no",
        "question",
        "score_total",
        "score_level",
        "score_correctness",
        "score_relevance",
        "score_evidence",
        "score_completeness",
        "score_clarity",
        "issue_tags",
        "user_problem",
        "answer",
        "mode",
        "strategy",
        "route",
        "selected_candidate_id",
        "final_execution_step",
        "evidence_count",
        "source_ids",
        "expected_support",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                **{field: row.get(field) for field in fields},
                "issue_tags": " | ".join(row.get("issue_tags") or []),
                "user_problem": " | ".join(row.get("user_problem") or []),
                "source_ids": " | ".join(str(x) for x in row.get("source_ids") or []),
            })


def _summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_category: dict[str, list[float]] = defaultdict(list)
    by_level = Counter()
    issues = Counter()
    for row in rows:
        by_category[str(row.get("category"))].append(float(row.get("score_total") or 0))
        by_level[str(row.get("score_level"))] += 1
        for tag in row.get("issue_tags") or []:
            issues[str(tag)] += 1
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(rows),
        "average_score": round(mean(float(row["score_total"]) for row in rows), 3) if rows else 0,
        "level_counts": dict(by_level),
        "category_average_scores": {cat: round(mean(vals), 3) for cat, vals in sorted(by_category.items())},
        "top_issue_tags": dict(issues.most_common(20)),
        "low_score_count_lt_5": sum(1 for row in rows if float(row["score_total"]) < 5),
        "needs_review_count_lt_7": sum(1 for row in rows if float(row["score_total"]) < 7),
    }


def _write_report(path: Path, rows: list[dict[str, Any]], summary: dict[str, Any], source_results: Path) -> None:
    issue_counter = Counter(tag for row in rows for tag in row.get("issue_tags") or [])
    low_rows = sorted(rows, key=lambda row: (float(row["score_total"]), str(row.get("id"))))[:30]
    category_lows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in sorted(rows, key=lambda row: float(row["score_total"])):
        cat = str(row.get("category"))
        if len(category_lows[cat]) < 8:
            category_lows[cat].append(row)

    lines = [
        "# User Quality Audit Report",
        "",
        f"Source results: `{source_results}`",
        "",
        "## Summary",
        "",
        f"•    Total: {summary['total']}",
        f"•    Average score: {summary['average_score']} / 10",
        f"•    Score levels: {summary['level_counts']}",
        f"•    Cases below 7: {summary['needs_review_count_lt_7']}",
        f"•    Cases below 5: {summary['low_score_count_lt_5']}",
        "",
        "## Category Average",
        "",
    ]
    for category, score in summary["category_average_scores"].items():
        lines.append(f"•    {category}: {score} / 10")

    lines.extend(["", "## Top Issue Tags", ""])
    for tag, count in issue_counter.most_common(15):
        lines.append(f"•    {tag}: {count}")

    lines.extend([
        "",
        "## Main Problems As A Real User",
        "",
        "1. บางคำถามเฉพาะเกมถูกตอบเป็น catalog/list ทั้งหมด ทำให้ไม่ได้คำตอบที่ถาม เช่น `ROV คือเกมอะไร` แต่ตอบรายชื่อเกมทั้ง catalog (เช่น 42 เกมตามข้อมูลล่าสุด)",
        "2. คำถามเรื่องจองบางข้อถูกตอบเป็นข้อมูลอุปกรณ์ เช่น ถาม Nintendo Switch ต้องเลือกอะไรตอนจอง แต่ตอบรายละเอียดเครื่อง Nintendo Switch OLED",
        "3. คำถามเจาะอุปกรณ์บางข้อจับ item ผิด เช่น ถามจอ/ทีวี/จำนวนชุด แต่คำตอบเริ่มจากอุปกรณ์คนละชิ้น",
        "4. Out-of-scope 94 ข้อจบที่ `general_llm_disabled` เพราะรอบ baseline ปิด LLM จึงปลอดภัยแต่ไม่ค่อยมีประโยชน์กับผู้ใช้ทั่วไป",
        "5. Decision Artifact ช่วยเห็นปัญหาใหม่ว่า selected candidate บางข้อไม่ตรงกับ execution จริง ทำให้ควรปรับ registry/ranking ให้สะท้อนทางที่ใช้จริงขึ้น",
        "",
        "## Lowest Scoring Examples",
        "",
    ])
    for row in low_rows:
        answer = _compact(str(row.get("answer") or ""))[:320]
        lines.append(f"### {row['id']} - {row['score_total']}/10")
        lines.append(f"Question: {row.get('question')}")
        lines.append(f"Mode/route: `{row.get('mode')}` / `{row.get('route')}`")
        lines.append(f"Issues: {', '.join(row.get('issue_tags') or [])}")
        lines.append(f"User problem: {'; '.join(row.get('user_problem') or [])}")
        lines.append(f"Answer preview: {answer}")
        lines.append("")

    lines.extend(["## Low Examples By Category", ""])
    for category, cat_rows in sorted(category_lows.items()):
        lines.append(f"### {category}")
        for row in cat_rows:
            lines.append(f"•    {row['id']} ({row['score_total']}/10): {row.get('question')} -> {', '.join(row.get('issue_tags') or [])}")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def run_audit(args: argparse.Namespace) -> Path:
    source = Path(args.results)
    rows = _load_rows(source)
    audited = [audit_row(row) for row in rows]
    run_name = args.name or f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_user_quality_audit"
    output_dir = Path(args.output_dir) if args.output_dir else DEFAULT_OUTPUT_ROOT / run_name
    output_dir.mkdir(parents=True, exist_ok=True)

    summary = _summary(audited)
    summary["source_results"] = str(source)
    summary["output_dir"] = str(output_dir)

    (output_dir / "audit_results.json").write_text(json.dumps(audited, ensure_ascii=False, indent=2), encoding="utf-8")
    with (output_dir / "audit_results.jsonl").open("w", encoding="utf-8") as file:
        for row in audited:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")
    _write_csv(output_dir / "audit_results.csv", audited)
    low = [row for row in audited if float(row["score_total"]) < 7]
    (output_dir / "low_score_cases.json").write_text(json.dumps(low, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_csv(output_dir / "low_score_cases.csv", low)
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_rubric(output_dir / "audit_rubric.md")
    _write_report(output_dir / "audit_report.md", audited, summary, source)
    return output_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Score question-bank outputs as a real-user quality audit.")
    parser.add_argument("--results", default=str(DEFAULT_RUN_DIR / "results_easy.json"))
    parser.add_argument("--output-dir", default="")
    parser.add_argument("--name", default="")
    args = parser.parse_args()
    output_dir = run_audit(args)
    print(f"Saved user quality audit to: {output_dir}")


if __name__ == "__main__":
    main()
