from __future__ import annotations

import json
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
OUT_MD = ROOT / "docs" / "23_competition_ground_truth_by_game_v2_item_audit.md"
OUT_JSONL = ROOT / "reports" / "competition_ground_truth_by_game_v2_item_audit_20260703.jsonl"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def first_trace_value(row: dict[str, Any], stage: str, key: str = "decision") -> str:
    for trace in row.get("trace", []):
        if trace.get("stage") == stage:
            return str(trace.get(key, ""))
    return ""


def top_retrieved(row: dict[str, Any]) -> str:
    retrieved = row.get("retrieved_ids") or []
    return str(retrieved[0]) if retrieved else ""


def keyword_group_note(answer: str, missing: list[str]) -> str:
    lower = answer.lower()
    notes: list[str] = []
    if "ชนะครบ 2 เกม" in missing and ("first to 2" in lower or "ft2" in lower):
        notes.append("AI ใช้คำเทียบเท่า `FT2/First to 2` แต่ตัวตรวจคาดคำว่า `ชนะครบ 2 เกม`")
    if "3 รอบ" in missing and ("r3" in lower or "round 3" in lower):
        notes.append("AI ใช้คำเทียบเท่า `R3/Round 3` แต่ตัวตรวจคาดคำว่า `3 รอบ`")
    if "best of 3" in " ".join(missing).lower() and ("bo3" in lower or "best of 3" in lower):
        notes.append("AI ตอบแนว BO3 แล้ว แต่ keyword อาจสะกด/รูปแบบไม่ตรง")
    if "ปรับแพ้ทันที" in missing and "ปรับแพ้" in lower:
        notes.append("AI มีคำว่า `ปรับแพ้` แต่ยังไม่ชัดว่า `ทันที` ตามเกณฑ์")
    if "ห้าม" in missing and any(term in lower for term in ("ไม่อนุญาต", "prohibited", "strictly prohibited", "ไม่ได้")):
        notes.append("AI อาจสื่อความหมายว่า `ห้าม` ด้วยคำอื่น แต่ตัวตรวจคาดคำว่า `ห้าม`")
    return "; ".join(notes)


def answer_style(row: dict[str, Any]) -> str:
    mode = str(row.get("mode", ""))
    route = str(row.get("route_category", ""))
    retrieved = ", ".join(str(item) for item in row.get("retrieved_ids", [])[:3]) or "-"
    answer = str(row.get("answer_short", ""))

    if mode == "pipeline:games_fast_path":
        return "ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้"
    if mode == "pipeline:schedule_fast_path":
        return "ตอบเป็นเวลาเปิด-ปิด/ตารางบริการของศูนย์ ทำให้หลุดจากตารางหรือกติกาการแข่งขัน"
    if route == "service_fee":
        return "ตอบจากหมวดราคา/ค่าบริการ ซึ่งเป็นคนละ domain กับกติกาการแข่งขัน"
    if route == "events_news":
        return "ตอบจากข่าวหรือกิจกรรม ทำให้คำตอบกลายเป็นข่าว ไม่ใช่กติกาของรายการแข่งขัน"
    if mode == "pipeline:rules_fast_path":
        return "ตอบจาก rulebase กฎทั่วไปของศูนย์ ไม่ใช่กฎการแข่งขันของเกมนั้น"
    if mode == "pipeline:no_answer":
        return "ตอบว่าไม่พบข้อมูล ทั้งที่หลายข้อมีข้อมูลอยู่ใน competition chunks แต่ pipeline ดึงไม่ถึง"
    if mode == "pipeline:competition_fact_card":
        return f"ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `{retrieved}`"
    if mode == "pipeline:rag_direct_curated":
        return f"ตอบจาก curated/chunk retrieval โดยตรงจาก `{retrieved}` อาจตรงบางส่วนหรือดึง source ผิด"
    if row.get("verdict") == "PASS":
        return "ตอบตรงตาม keyword/source ที่ตั้งไว้ และรูปแบบคำตอบอยู่ในเกณฑ์"
    return f"ตอบด้วย route `{route}` mode `{mode}` ลักษณะคำตอบต้องอ่านเทียบกับ expected"


def classify(row: dict[str, Any], gt: dict[str, Any]) -> tuple[str, str, str]:
    verdict = str(row.get("verdict", ""))
    route = str(row.get("route_category", ""))
    mode = str(row.get("mode", ""))
    expected_intent = str(gt.get("intent", ""))
    expected_key = str(gt.get("source_fact_key", ""))
    retrieved = top_retrieved(row)
    missing_keywords = list(row.get("missing_keywords", []))
    missing_sources = list(row.get("missing_source_keywords", []))
    source_ok = bool(row.get("source_ok"))
    keyword_ok = bool(row.get("keyword_ok"))
    quality_ok = bool(row.get("quality_ok"))
    validation_errors = list(row.get("validation_errors", []))

    if verdict == "PASS":
        return (
            "pass",
            "ผ่านตามเกณฑ์: keyword/source/validation ตรง",
            "ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้",
        )

    if route != "competition_rules":
        route_problem = {
            "games": "Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา",
            "schedule": "Router จัดเป็น schedule ของศูนย์ เพราะเจอคำถามเวลา/รอบ ทำให้ตอบเวลาเปิด-ปิดศูนย์แทนตารางแข่งขัน",
            "service_fee": "Router จัดเป็น service_fee เพราะเจอคำคล้ายราคา/เวลา/ชั่วโมง ทำให้ไปดึงข้อมูลราคาแทนกติกา",
            "events_news": "Router จัดเป็น events_news เพราะเจอคำว่า PSU/รายการ/2026 แล้วไปค้นข่าวแทนเอกสารกติกา",
            "rules": "Router จัดเป็น rules ทั่วไปของศูนย์ ไม่ใช่ competition_rules",
            "general": "Router ไม่มั่นใจพอและปล่อยเป็น general ทำให้ retrieval ไม่เจาะเอกสารการแข่งขัน",
        }.get(route, f"Router จัดผิดหมวดเป็น `{route}`")
        return (
            "wrong_route",
            route_problem,
            "เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่",
        )

    if mode == "pipeline:no_answer":
        return (
            "no_answer_despite_data",
            "Route เข้า competition_rules แล้ว แต่ retrieval/fact card ไม่เจอ context ที่มั่นใจพอ จึงตอบไม่พบข้อมูล",
            "ให้ fallback ไปค้น `competition_rule_chunks.jsonl` และใช้ RAG/LLM สรุปเมื่อ fact card ไม่ครอบคลุม",
        )

    if mode == "pipeline:competition_fact_card":
        generic_tokens = {
            "cs2", "rov", "aov", "valorant", "tekken8", "tekken",
            "competition", "rules", "rule", "psu", "phuket", "blueket",
        }
        expected_tokens = [
            token
            for token in expected_key.lower().replace("-", "_").split("_")
            if len(token) >= 3 and token not in generic_tokens
        ]
        retrieved_lower = retrieved.lower()
        intent_in_retrieved = expected_intent and expected_intent.lower() in retrieved_lower
        key_hint_in_retrieved = any(token in retrieved_lower for token in expected_tokens)
        if not keyword_ok and not intent_in_retrieved and not key_hint_in_retrieved:
            return (
                "wrong_fact_card_intent",
                f"Fact card ที่ถูกเลือก `{retrieved or '-'}` คนละ intent กับที่ถาม (`{expected_intent}`) ทำให้ตอบผิดประเด็น",
                "เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน",
            )
        if not keyword_ok and source_ok:
            note = keyword_group_note(str(row.get("answer", "")), missing_keywords)
            problem = "Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ"
            if note:
                problem += f"; {note}"
            return (
                "partial_or_strict_keyword",
                problem,
                "ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator",
            )
        if not source_ok:
            return (
                "wrong_source_fact_card",
                f"เลือก fact card/source ไม่ตรงเอกสารที่คาดไว้: missing source {missing_sources}",
                "ตรวจ source_ids ของ fact card และการ scoring ของชื่อเกม",
            )

    if mode == "pipeline:rag_direct_curated":
        if not source_ok:
            return (
                "rag_wrong_source",
                f"RAG ดึง source ผิดหรือกว้างเกินไป จึงไม่พบ source expected: {missing_sources}",
                "เพิ่ม filter ให้ competition_rules จำกัด document ตามชื่อเกมก่อนจัดอันดับ chunks",
            )
        if not keyword_ok:
            note = keyword_group_note(str(row.get("answer", "")), missing_keywords)
            problem = "RAG ดึง source ถูกแต่คำตอบไม่ครบ keyword สำคัญ"
            if note:
                problem += f"; {note}"
            return (
                "rag_partial_answer",
                problem,
                "ปรับ chunk selection/answer synthesis ให้ตอบ direct answer ก่อน แล้วค่อยรายละเอียด",
            )

    if validation_errors:
        return (
            "validation_failed",
            "คำตอบติด validation errors: " + "; ".join(str(item) for item in validation_errors),
            "ปรับ formatter หรือข้อมูลอ้างอิงให้ผ่าน validation",
        )
    if not quality_ok:
        return (
            "quality_failed",
            "คำตอบผิด quality expectation: " + "; ".join(str(item) for item in row.get("quality_problems", [])),
            "ปรับลำดับคำตอบให้ตอบสิ่งที่ถามก่อน และลดข้อความที่ทำให้เข้าใจผิด",
        )
    return (
        "keyword_or_source_mismatch",
        f"Keyword/source ไม่ตรง: missing_keywords={missing_keywords}, missing_sources={missing_sources}",
        "อ่าน case นี้แบบ manual และเพิ่ม rule/fact card/synonym ตามจุดที่ขาด",
    )


def build_item(row: dict[str, Any], gt: dict[str, Any], index: int) -> dict[str, Any]:
    cause_code, cause_detail, fix = classify(row, gt)
    return {
        "index": index,
        "id": row["id"],
        "game": gt.get("game", ""),
        "intent": gt.get("intent", ""),
        "question": row.get("question", ""),
        "verdict": row.get("verdict", ""),
        "route_category": row.get("route_category", ""),
        "route_intent": row.get("route_intent", ""),
        "mode": row.get("mode", ""),
        "confidence": row.get("confidence", ""),
        "latency_sec": row.get("latency_sec", ""),
        "expected_keywords": row.get("expected_keywords", []),
        "missing_keywords": row.get("missing_keywords", []),
        "expected_source_keywords": row.get("expected_source_keywords", []),
        "missing_source_keywords": row.get("missing_source_keywords", []),
        "retrieved_ids": row.get("retrieved_ids", []),
        "answer_short": row.get("answer_short", ""),
        "cause_code": cause_code,
        "cause_detail": cause_detail,
        "problem": problem_sentence(cause_code, row, gt),
        "answer_style": answer_style(row),
        "suggested_fix": fix,
        "router_decision": first_trace_value(row, "router"),
        "fact_card_trace": first_trace_value(row, "fact_card_retrieval", "detail"),
        "rag_trace": first_trace_value(row, "rag_retrieval", "detail"),
    }


def problem_sentence(cause_code: str, row: dict[str, Any], gt: dict[str, Any]) -> str:
    if cause_code == "pass":
        return "ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ"
    if cause_code == "wrong_route":
        return f"คำถามควรเป็น competition_rules ของ {gt.get('game')} แต่ถูกส่งไป `{row.get('route_category')}`"
    if cause_code == "wrong_fact_card_intent":
        return f"ระบบตอบจาก `{top_retrieved(row) or '-'}` แต่คำถามต้องการ intent `{gt.get('intent')}`"
    if cause_code == "partial_or_strict_keyword":
        return "คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก"
    if cause_code == "rag_wrong_source":
        return "retrieval ดึง source คนละเอกสารหรือคนละหมวด"
    if cause_code == "rag_partial_answer":
        return "retrieval ดึงเอกสารถูก แต่ synthesis ยังไม่ตอบ direct answer ให้ครบ"
    if cause_code == "no_answer_despite_data":
        return "ระบบตอบไม่พบข้อมูล ทั้งที่ข้อมูลน่าจะอยู่ใน competition chunks"
    return "ต้องตรวจ manual เพิ่มจาก missing keywords/source และคำตอบจริง"


def markdown_report(audit_rows: list[dict[str, Any]]) -> str:
    total = len(audit_rows)
    passed = sum(1 for row in audit_rows if row["verdict"] == "PASS")
    cause_counts = Counter(row["cause_code"] for row in audit_rows)
    game_counts: dict[str, Counter[str]] = defaultdict(Counter)
    for row in audit_rows:
        game_counts[row["game"]][row["cause_code"]] += 1

    lines = [
        "# Competition Ground Truth By Game V2 - Item Cause Audit",
        "",
        "วันที่: 2026-07-03",
        "",
        "รายงานนี้ไล่ดูผลรัน Ground Truth ชุด `competition_by_game_v2` แบบเรียงข้อ เพื่อแยกว่าสาเหตุผิดเกิดจากอะไร ปัญหาคืออะไร และลักษณะคำตอบของ AI เป็นแบบไหน",
        "",
        "## Summary",
        "",
        f"- Total: {total}",
        f"- PASS: {passed}",
        f"- FAIL: {total - passed}",
        f"- Pass rate: {(passed / total * 100 if total else 0):.2f}%",
        "",
        "## Cause Counts",
        "",
    ]
    for cause, count in cause_counts.most_common():
        lines.append(f"- `{cause}`: {count}")

    lines.extend(["", "## Cause By Game", ""])
    for game, counter in game_counts.items():
        lines.append(f"### {game}")
        for cause, count in counter.most_common():
            lines.append(f"- `{cause}`: {count}")
        lines.append("")

    lines.extend(["## Item Audit", ""])
    current_game = ""
    for row in audit_rows:
        if row["game"] != current_game:
            current_game = row["game"]
            lines.append(f"## {current_game}")
            lines.append("")
        status = "ผ่าน" if row["verdict"] == "PASS" else "ผิด/ต้องแก้"
        lines.extend(
            [
                f"### {row['index']}. [{row['verdict']}] {row['id']} - {status}",
                "",
                f"- คำถาม: {row['question']}",
                f"- Intent ที่คาด: `{row['intent']}`",
                f"- Route/Mode: `{row['route_category']}` / `{row['mode']}`",
                f"- Retrieved: `{', '.join(str(item) for item in row['retrieved_ids']) or '-'}`",
                f"- Expected keywords: `{', '.join(str(item) for item in row['expected_keywords']) or '-'}`",
                f"- Missing keywords: `{', '.join(str(item) for item in row['missing_keywords']) or '-'}`",
                f"- Missing source: `{', '.join(str(item) for item in row['missing_source_keywords']) or '-'}`",
                f"- สาเหตุ: `{row['cause_code']}` - {row['cause_detail']}",
                f"- ปัญหา: {row['problem']}",
                f"- ลักษณะคำตอบ: {row['answer_style']}",
                f"- คำตอบย่อจาก AI: {row['answer_short'] or '-'}",
                f"- แนวแก้: {row['suggested_fix']}",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    gt_rows = {row["id"]: row for row in load_jsonl(GT_PATH)}
    result_rows = load_jsonl(RESULT_PATH)
    audit_rows = [build_item(row, gt_rows[row["id"]], index) for index, row in enumerate(result_rows, 1)]

    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8", newline="\n") as f:
        for row in audit_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    OUT_MD.write_text(markdown_report(audit_rows), encoding="utf-8", newline="\n")

    print(f"Wrote {len(audit_rows)} item audits")
    print(OUT_MD)
    print(OUT_JSONL)
    print(Counter(row["cause_code"] for row in audit_rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
