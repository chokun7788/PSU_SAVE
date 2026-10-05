from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


ROOT = Path(__file__).resolve().parents[1]
GT_PATH = ROOT / "data" / "ground_truth" / "competition_by_game_v2" / "ground_truth_competition_all_games_v2_diverse.jsonl"
RESULT_PATH = ROOT / "reports" / "pipeline_ground_truth_results_competition_by_game_v2_all_20260703.jsonl"
CAUSE_PATH = ROOT / "reports" / "competition_ground_truth_by_game_v2_item_audit_20260703.jsonl"
OUT_MD = ROOT / "docs" / "24_competition_ground_truth_v2_answer_style_audit.md"
OUT_JSONL = ROOT / "reports" / "competition_ground_truth_v2_answer_style_audit_20260703.jsonl"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def norm(text: str) -> str:
    return str(text).lower().replace(",", "").replace("–", "-").replace("—", "-")


def first_non_empty_line(answer: str) -> str:
    for line in str(answer).splitlines():
        if line.strip():
            return line.strip()
    return ""


def strip_answer_prefix(line: str) -> str:
    return re.sub(r"^(คำตอบ|answer)\s*[:：]\s*", "", line.strip(), flags=re.IGNORECASE).strip()


def keyword_hits(text: str, keywords: list[str]) -> tuple[list[str], list[str]]:
    hay = norm(text)
    hit: list[str] = []
    miss: list[str] = []
    for keyword in keywords:
        key = norm(keyword)
        if key in hay:
            hit.append(str(keyword))
        else:
            miss.append(str(keyword))
    return hit, miss


def reference_order(answer: str) -> str:
    text = str(answer)
    first_ref_positions = [
        pos
        for pos in [
            text.find("แหล่งข้อมูล"),
            text.find("อ้างอิง"),
            text.find("source"),
            text.find("Source"),
        ]
        if pos >= 0
    ]
    if not first_ref_positions:
        return "no_reference_marker"
    first_answer_content = first_non_empty_line(text)
    if not first_answer_content:
        return "empty_answer"
    first_ref = min(first_ref_positions)
    first_line_end = text.find("\n")
    if first_line_end == -1:
        first_line_end = len(text)
    return "reference_after_answer" if first_ref > first_line_end else "reference_too_early"


def desired_first_line_hint(gt: dict[str, Any]) -> str:
    intent = str(gt.get("intent", ""))
    game = str(gt.get("game", ""))
    keywords = [str(item) for item in gt.get("expected_keywords", [])]
    key_text = ", ".join(keywords)
    if intent == "team_size":
        return f"ควรขึ้นต้นด้วยจำนวนผู้เล่น/ทีมของ {game} ให้ชัด เช่นมีคำว่า {key_text}"
    if intent in {"format", "game_setting"}:
        return f"ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น {key_text}"
    if intent in {"pause", "rematch", "late_start", "penalty"}:
        return f"ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น {key_text}"
    if intent in {"equipment", "area_rules", "character", "skin", "hero_rule", "bug_rule", "policy"}:
        return f"ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น {key_text}"
    if intent in {"schedule", "schedule_location", "checkin"}:
        return f"ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น {key_text}"
    return f"ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: {key_text}"


def style_class(row: dict[str, Any], gt: dict[str, Any], cause: dict[str, Any]) -> tuple[str, str]:
    answer = str(row.get("answer", ""))
    first = strip_answer_prefix(first_non_empty_line(answer))
    expected_keywords = [str(item) for item in row.get("expected_keywords", [])]
    first_hit, first_miss = keyword_hits(first, expected_keywords)
    full_hit, full_miss = keyword_hits(answer, expected_keywords)
    cause_code = str(cause.get("cause_code", ""))
    route = str(row.get("route_category", ""))
    mode = str(row.get("mode", ""))

    if not answer.strip():
        return "empty_answer", "ไม่มีคำตอบให้ประเมิน"
    if mode == "pipeline:no_answer":
        return "no_answer", "รูปแบบสุภาพ แต่ไม่ควรตอบไม่พบข้อมูลถ้าข้อมูลมีอยู่ใน competition chunks"
    if route != "competition_rules":
        return "wrong_domain_first_line", "บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ"
    if cause_code == "wrong_fact_card_intent":
        return "direct_but_wrong_fact", "มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม"
    if first_miss and not full_miss:
        return "details_have_answer_but_first_line_missing", "ข้อมูลที่ต้องการอาจอยู่ในรายละเอียด/หลักฐาน แต่บรรทัดแรกยังไม่ตอบสิ่งที่ถามโดยตรง"
    if first_miss and full_miss:
        return "missing_expected_content", "ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ"
    if len(first) > 220:
        return "first_line_too_long", "บรรทัดแรกยาวเกินไป ควรตอบสั้นๆ ก่อนแล้วค่อยขยายรายละเอียดด้านล่าง"
    if row.get("verdict") == "PASS":
        return "good_direct_first", "ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง"
    if first_hit and not full_miss:
        return "mostly_good_but_failed_other_check", "รูปแบบคำตอบนำหน้าพอใช้ได้ แต่ยัง fail จาก source/validation/keyword บางส่วน"
    return "needs_manual_style_check", "ต้องอ่านเทียบกับคำถามและเฉลยเพิ่มเติม"


def why_wrong_plain(row: dict[str, Any], gt: dict[str, Any], cause: dict[str, Any], style_code: str) -> str:
    q = str(row.get("question", ""))
    first = strip_answer_prefix(first_non_empty_line(str(row.get("answer", ""))))
    missing = ", ".join(str(item) for item in row.get("missing_keywords", [])) or "-"
    retrieved = ", ".join(str(item) for item in row.get("retrieved_ids", [])[:3]) or "-"
    cause_code = str(cause.get("cause_code", ""))

    if row.get("verdict") == "PASS":
        return "ไม่ผิดตามเกณฑ์อัตโนมัติ"
    if cause_code == "wrong_route":
        return f"คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `{row.get('route_category')}` จึงตอบ `{first}` ซึ่งไม่ใช่คำตอบของคำถาม `{q}`"
    if cause_code == "wrong_fact_card_intent":
        return f"ระบบเลือก `{retrieved}` ทำให้คำตอบแรกเป็น `{first}` แต่คำถามต้องการ intent `{gt.get('intent')}` และยังขาด `{missing}`"
    if cause_code == "partial_or_strict_keyword":
        return f"คำตอบแรกคือ `{first}` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `{missing}` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก"
    if cause_code == "no_answer_despite_data":
        return "ระบบตอบไม่พบข้อมูล ทั้งที่ Ground Truth สร้างจากข้อมูลใน competition chunks จึงควร fallback ไปค้น chunk/LLM ต่อ"
    if cause_code == "rag_partial_answer":
        return f"RAG ดึงบริบทได้บางส่วน แต่คำตอบแรก `{first}` ยังไม่ใช่ประเด็นที่ถามและขาด `{missing}`"
    if style_code == "details_have_answer_but_first_line_missing":
        return f"คำตอบอาจมีข้อมูลอยู่ด้านล่าง แต่ first line `{first}` ยังไม่ตอบตรงคำถาม"
    return f"คำตอบแรก `{first}` ยังไม่ตรง expected keywords: {missing}"


def build_row(index: int, result: dict[str, Any], gt: dict[str, Any], cause: dict[str, Any]) -> dict[str, Any]:
    answer = str(result.get("answer", ""))
    first_raw = first_non_empty_line(answer)
    first_core = strip_answer_prefix(first_raw)
    first_hit, first_miss = keyword_hits(first_core, [str(item) for item in result.get("expected_keywords", [])])
    full_hit, full_miss = keyword_hits(answer, [str(item) for item in result.get("expected_keywords", [])])
    style_code, style_detail = style_class(result, gt, cause)

    return {
        "index": index,
        "id": result["id"],
        "game": gt.get("game", ""),
        "intent": gt.get("intent", ""),
        "question": result.get("question", ""),
        "verdict": result.get("verdict", ""),
        "route_category": result.get("route_category", ""),
        "mode": result.get("mode", ""),
        "cause_code": cause.get("cause_code", ""),
        "style_code": style_code,
        "style_detail": style_detail,
        "first_line": first_core,
        "first_line_keyword_hit": first_hit,
        "first_line_keyword_missing": first_miss,
        "full_answer_keyword_missing": full_miss,
        "reference_order": reference_order(answer),
        "retrieved_ids": result.get("retrieved_ids", []),
        "expected_keywords": result.get("expected_keywords", []),
        "answer_short": result.get("answer_short", ""),
        "why_wrong": why_wrong_plain(result, gt, cause, style_code),
        "desired_first_line_hint": desired_first_line_hint(gt),
    }


def markdown_report(rows: list[dict[str, Any]]) -> str:
    total = len(rows)
    pass_count = sum(1 for row in rows if row["verdict"] == "PASS")
    style_counts = Counter(row["style_code"] for row in rows)
    cause_counts = Counter(row["cause_code"] for row in rows)
    by_game_style: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        by_game_style[row["game"]][row["style_code"]] += 1

    lines = [
        "# Competition Ground Truth V2 - Answer Style Audit",
        "",
        "วันที่: 2026-07-03",
        "",
        "รายงานนี้เน้นวิเคราะห์รูปแบบคำตอบ โดยเฉพาะหลักที่ต้องการคือ `ตอบคำตอบจริงก่อน -> รายละเอียด -> หลักฐาน/อ้างอิงท้ายสุด`",
        "",
        "## Desired Answer Format",
        "",
        "รูปแบบที่ควรใช้:",
        "",
        "```text",
        "คำตอบ: <ตอบตรงคำถามในบรรทัดแรก เช่น จำนวน/ราคา/ได้หรือไม่ได้/บทลงโทษ/เวลา>",
        "",
        "รายละเอียด:",
        "- <ขยายเงื่อนไขที่เกี่ยวข้อง>",
        "- <ข้อควรระวังหรือข้อยกเว้น>",
        "",
        "อ้างอิงจากกติกา: <ชื่อเกม / ชื่อรายการ>",
        "แหล่งข้อมูล: <source>",
        "```",
        "",
        "หลักการ:",
        "",
        "- บรรทัดแรกต้องตอบสิ่งที่ผู้ใช้ถามก่อน ห้ามเริ่มด้วยประวัติ/รายละเอียด/แหล่งข้อมูล",
        "- ถ้าคำถามถาม `ได้ไหม` ต้องตอบ `ได้/ไม่ได้/ห้าม/อนุญาต` ก่อน",
        "- ถ้าคำถามถาม `กี่` ต้องตอบตัวเลขก่อน",
        "- ถ้าคำถามถาม `โดนอะไร` ต้องตอบบทลงโทษก่อน",
        "- รายละเอียดและหลักฐานควรอยู่ข้างล่าง ไม่ควรกลบคำตอบหลัก",
        "",
        "## Summary",
        "",
        f"- Total: {total}",
        f"- PASS: {pass_count}",
        f"- FAIL: {total - pass_count}",
        "",
        "## Style Counts",
        "",
    ]
    for style, count in style_counts.most_common():
        lines.append(f"- `{style}`: {count}")

    lines.extend(["", "## Cause Counts", ""])
    for cause, count in cause_counts.most_common():
        lines.append(f"- `{cause}`: {count}")

    lines.extend(["", "## Style By Game", ""])
    for game, counter in by_game_style.items():
        lines.append(f"### {game}")
        for style, count in counter.most_common():
            lines.append(f"- `{style}`: {count}")
        lines.append("")

    lines.extend([
        "## Main Findings",
        "",
        "### 1. หลายคำตอบมี direct-first แต่เป็นคำตอบผิดเรื่อง",
        "",
        "เช่นถามคุณสมบัติผู้เข้าแข่ง แต่ first line ตอบเรื่อง pause หรือ map pool ปัญหาไม่ใช่ formatter แต่เป็น retrieval/fact card intent ผิด",
        "",
        "### 2. หลายคำถามหลุด route ก่อนจะถึง competition rules",
        "",
        "เมื่อหลุดไป `games_fast_path`, `events_news`, `schedule_fast_path` คำตอบแรกจึงกลายเป็นข้อมูลทั่วไปของศูนย์หรือข่าว ไม่ใช่กติกาการแข่งขัน",
        "",
        "### 3. บางข้อมีข้อมูลในคำตอบรวม แต่ first line ยังไม่ตอบจุดที่ถาม",
        "",
        "กรณีนี้ต้องปรับ answer synthesis ให้ดึงประเด็นที่ผู้ใช้ถามมาไว้บรรทัดแรก",
        "",
        "### 4. บางข้อเป็นปัญหาตัวตรวจ strict keyword",
        "",
        "เช่น AI ตอบ `FT2/First to 2` แต่เฉลยคาด `ชนะครบ 2 เกม` แบบนี้ความหมายถูกใกล้เคียง แต่ evaluator ยังไม่มี synonym group",
        "",
        "## Item Style Audit",
        "",
    ])

    current_game = ""
    for row in rows:
        if row["game"] != current_game:
            current_game = row["game"]
            lines.append(f"## {current_game}")
            lines.append("")
        lines.extend(
            [
                f"### {row['index']}. [{row['verdict']}] {row['id']}",
                "",
                f"- คำถาม: {row['question']}",
                f"- Intent ที่คาด: `{row['intent']}`",
                f"- Route/Mode: `{row['route_category']}` / `{row['mode']}`",
                f"- Cause: `{row['cause_code']}`",
                f"- Style: `{row['style_code']}` - {row['style_detail']}",
                f"- First line ที่ AI ตอบ: {row['first_line'] or '-'}",
                f"- Keyword ที่ขาดใน first line: `{', '.join(str(item) for item in row['first_line_keyword_missing']) or '-'}`",
                f"- Keyword ที่ขาดในคำตอบรวม: `{', '.join(str(item) for item in row['full_answer_keyword_missing']) or '-'}`",
                f"- Retrieved: `{', '.join(str(item) for item in row['retrieved_ids']) or '-'}`",
                f"- ทำไมผิด/ปัญหาคืออะไร: {row['why_wrong']}",
                f"- ควรตอบขึ้นต้นประมาณไหน: {row['desired_first_line_hint']}",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    gt_by_id = {row["id"]: row for row in load_jsonl(GT_PATH)}
    cause_by_id = {row["id"]: row for row in load_jsonl(CAUSE_PATH)}
    result_rows = load_jsonl(RESULT_PATH)
    style_rows = [
        build_row(index, result, gt_by_id[result["id"]], cause_by_id[result["id"]])
        for index, result in enumerate(result_rows, 1)
    ]

    with OUT_JSONL.open("w", encoding="utf-8", newline="\n") as f:
        for row in style_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    OUT_MD.write_text(markdown_report(style_rows), encoding="utf-8", newline="\n")

    print(f"Wrote {len(style_rows)} answer style audits")
    print(OUT_MD)
    print(OUT_JSONL)
    print(Counter(row["style_code"] for row in style_rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
