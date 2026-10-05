from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def _safe_name(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    return safe.strip("._") or "case"


def _text_block(value: Any) -> str:
    return f"````text\n{'' if value is None else value}\n````"


def _table_text(value: Any, limit: int = 160) -> str:
    if value is None:
        text = ""
    elif isinstance(value, (list, dict)):
        text = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    else:
        text = str(value)
    text = text.replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 3] + "..."


def _passed(row: dict[str, Any]) -> bool:
    return bool((row.get("judge") or {}).get("passed"))


def _answer_for_display(row: dict[str, Any]) -> str:
    answer = str(row.get("answer") or "")
    if answer.strip():
        return answer
    return "[ไม่มีคำตอบ: Chatbot ส่ง answer เป็นค่าว่าง]"


def _error_text(row: dict[str, Any]) -> str:
    errors = (row.get("judge") or {}).get("errors") or []
    return ", ".join(str(error) for error in errors) or "-"


def _visible_llm_calls(row: dict[str, Any]) -> list[dict[str, Any]]:
    calls: list[dict[str, Any]] = []
    for trace_item in row.get("trace") or []:
        metadata = trace_item.get("metadata") or {}
        call = metadata.get("llm_call")
        if isinstance(call, dict):
            calls.append(call)
    return calls


def _budget_used_calls(row: dict[str, Any]) -> int:
    values = [int(call.get("llm_budget_used_calls") or 0) for call in _visible_llm_calls(row)]
    return max(values or [0])


def _explicit_timeout(row: dict[str, Any]) -> bool:
    patterns = (
        "timeouterror",
        "timed_out",
        "timed out",
        "deadline_exceeded",
        "request_timeout",
        "global_timeout_exceeded",
    )
    top_level = [
        row.get("mode"),
        row.get("validation_errors"),
        (row.get("judge") or {}).get("errors"),
    ]
    if any(pattern in json.dumps(top_level, ensure_ascii=False).lower() for pattern in patterns):
        return True
    for item in row.get("trace") or []:
        trace_decision = " ".join(
            str(item.get(key) or "") for key in ("stage", "decision", "detail")
        ).lower()
        if any(pattern in trace_decision for pattern in patterns):
            return True
    return False


def _failure_diagnosis(row: dict[str, Any]) -> dict[str, str]:
    case_id = str(row.get("id") or "")
    mode = str(row.get("mode") or "")
    errors = set((row.get("judge") or {}).get("errors") or [])

    if mode == "exception":
        return {
            "bucket": "system_exception",
            "assessment": "Chatbot ผิดจริง",
            "root_cause": "Request state ไม่ถูก initialize ทุกเส้นทาง จึงเกิด UnboundLocalError ก่อนสร้างคำตอบ",
            "why": "ผู้ใช้ไม่ได้รับคำตอบเลยและ answer เป็นค่าว่าง",
            "fix": "กำหนดค่า request/RAG state ตั้งแต่ต้น request และเพิ่ม regression test สำหรับ route นี้",
        }
    if case_id == "MB-0240-G-152":
        return {
            "bucket": "wrong_route_game_ranking",
            "assessment": "Chatbot ผิดจริง",
            "root_cause": "คำถามจัดอันดับจำนวนเกมถูกเปลี่ยนเป็น equipment/list แล้วเข้า hybrid retrieval ผิดหมวด",
            "why": "ถามว่าโซนหรืออุปกรณ์ใดมีเกมมากสุด แต่ตอบว่าไม่พบข้อมูลหมวด equipment",
            "fix": "ให้ game-zone ranking route มี deterministic veto, ใช้ structured game catalog และหยุด retrieval เมื่อ source domain ไม่ตรง",
        }
    if case_id == "MB-0189-G-101":
        return {
            "bucket": "substring_collision_animal_crossing",
            "assessment": "Chatbot ผิดจริง",
            "root_cause": "Raw substring `cross` ในชื่อ Animal Crossing ถูกตีความเป็นคำสั่งปุ่ม/controls และ ambiguity margin ทับ exact game entity",
            "why": "ชื่อเกม resolve แบบ exact แล้ว แต่ระบบยังถามกลับแทนการตอบข้อมูลเกม",
            "fix": "ใช้ token-boundary matcher และให้ exact entity + explicit detail question veto ambiguity ระหว่าง list/detail",
        }
    if mode == "pipeline:ambiguity_clarification":
        return {
            "bucket": "substring_collision_price_in_kho_sia",
            "assessment": "Chatbot ผิดจริง",
            "root_cause": "คำว่า `ข้อเสีย` ถูก raw substring matcher จับเป็น price term `เสีย` ทำให้ Ambiguity Gate คิดว่าถามราคาแต่ไม่มี target",
            "why": "คำถามความรู้ทั่วไปที่ชัดเจนถูกตอบด้วยคำถามกลับเรื่องบริการ/โซนและราคา",
            "fix": "เปลี่ยน lexical matcher เป็น token/context-aware matcher และเพิ่ม negative context สำหรับ `ข้อดีข้อเสีย`",
        }
    if "category_mismatch:equipment" in errors and any("คีย์บอร์ด|mechanical" in error for error in errors):
        return {
            "bucket": "general_concept_misrouted_equipment",
            "assessment": "Chatbot ผิดจริง",
            "root_cause": "คำว่า `คีย์บอร์ด` ทำให้ Question Frame เลือก equipment_lookup แม้รูปประโยค `คืออะไร` ต้องการคำจำกัดความทั่วไป",
            "why": "ระบบตอบรายการอุปกรณ์ของศูนย์แทนการอธิบายว่า mechanical keyboard คืออะไร",
            "fix": "ให้น้ำหนัก operation `definition/detail` ก่อน entity domain และบังคับ specific PSU inventory เฉพาะเมื่อมีคำถามว่า `ที่ศูนย์มีไหม/มีรุ่นอะไร`",
        }
    if case_id == "MB-0649-ANA-023":
        return {
            "bucket": "unsupported_freshness_hallucination",
            "assessment": "Chatbot ผิดจริง",
            "root_cause": "คำถาม `ตอนนี้` ถูกส่งเข้า General LLM โดยไม่มี live Web/API evidence หรือ freshness guard",
            "why": "โมเดลยกชื่อเพลงเก่ามาอ้างว่าเป็นเพลงฮิตปัจจุบัน จึงเป็น unsupported freshness claim",
            "fix": "บังคับ freshness query ใช้ live provider ที่มี timestamp หรือ no-answer/ชี้แหล่งตรวจสอบเมื่อไม่มี provider",
        }
    if case_id == "MB-0650-ANA-024":
        return {
            "bucket": "product_scope_policy_mismatch",
            "assessment": "ต้องตัดสิน Product Policy",
            "root_cause": "เป้าหมาย broad assistant ของ product ยังขัดกับ expected contract เดิมที่ให้ decline คำถามนอก PSU",
            "why": "คำถามยังไม่มีโจทย์คณิตให้คำนวณ คำตอบที่เหมาะกว่าอาจเป็นการขอให้ส่งโจทย์ ไม่ใช่ปฏิเสธแบบกว้าง",
            "fix": "กำหนด scope ให้ชัด แล้วแก้ policy/contract ให้ถามขอรายละเอียดหรือช่วยอธิบายวิธีทำโดยไม่เดาคำตอบ",
        }
    if any("latency|หน่วง" in error for error in errors):
        return {
            "bucket": "judge_false_negative_latency_synonym",
            "assessment": "Judge ตรวจพลาด",
            "root_cause": "Keyword judge รับเฉพาะ `latency` หรือ `หน่วง` แต่คำตอบใช้คำพ้อง `ความล่าช้า`/`เวลาตอบสนอง`",
            "why": "เนื้อหาคำตอบอธิบาย latency ถูกความหมาย แต่ไม่ตรง exact keyword",
            "fix": "เพิ่ม synonym-aware/semantic evaluator โดยยังตรวจสาระสำคัญเรื่อง delay และ response time",
        }
    if any("ขอบคุณ" in error for error in errors):
        return {
            "bucket": "judge_false_negative_thanks_synonym",
            "assessment": "Judge ตรวจพลาด",
            "root_cause": "Keyword judge หา `ขอบคุณ` แบบตรงตัว แต่คำตอบใช้ `ขอบพระคุณ` หรือ `ขอบใจ`",
            "why": "คำตอบทำหน้าที่กล่าวขอบคุณแล้ว แม้บางสำนวนยังควรปรับความเป็นธรรมชาติ",
            "fix": "เพิ่มกลุ่มคำพ้องและตรวจ semantic intent พร้อมแยก style lint ออกจาก correctness score",
        }
    if any("กิจกรรม" in error for error in errors):
        return {
            "bucket": "judge_false_negative_activity_synonym",
            "assessment": "Judge ตรวจพลาด",
            "root_cause": "Keyword judge ต้องเห็น `กิจกรรม` แต่คำตอบใช้ `งานแข่งขันเกม` ซึ่งสื่อความหมายเดียวกัน",
            "why": "คำตอบเป็นประโยคประชาสัมพันธ์งานตามโจทย์ แม้ถ้อยคำยาวและโฆษณาเกินจำเป็น",
            "fix": "ใช้ semantic evaluator สำหรับ activity/event และตรวจความยาว/รูปแบบด้วย style contract แยกต่างหาก",
        }
    return {
        "bucket": "unclassified_failure",
        "assessment": "ต้องตรวจเพิ่ม",
        "root_cause": "ยังจัดกลุ่ม root cause อัตโนมัติไม่ได้",
        "why": _error_text(row),
        "fix": "อ่าน route, intent, source และ trace ของเคสนี้แบบ focused reproduction",
    }


def _slow_diagnosis(row: dict[str, Any]) -> dict[str, str]:
    case_id = str(row.get("id") or "")
    budget_used = _budget_used_calls(row)
    if case_id == "MB-0240-G-152":
        return {
            "bucket": "wrong_route_expensive_retrieval",
            "cause": "Wrong route ไป equipment + hybrid vector retrieval 5.489s; เวลาที่เหลืออยู่นอก trace 12 entries และต้องใช้ full timing ledger ยืนยัน",
            "fix": "แก้ route ranking, cache entity matching และเพิ่ม append-only timing ledger",
        }
    if budget_used >= 2:
        return {
            "bucket": "two_sequential_llm_calls",
            "cause": "Request ใช้ LLM budget ไปแล้ว 2 calls: intent/review ก่อน แล้วจึง general answer แบบต่อคิวลำดับเดียว",
            "fix": "ทำ clear-general one-call path, ใช้ deterministic intent และลด num_predict ตาม answer shape",
        }
    return {
        "bucket": "single_slow_generation",
        "cause": "มี LLM call เดียว แต่ token generation ใช้เวลานานเกิน 10 วินาที",
        "fix": "ลด output token budget, ใช้ concise answer contract และ hard deadline/cancel ที่ระดับ Ollama worker",
    }


def _case_markdown(index: int, row: dict[str, Any], detail_link: str) -> str:
    status = "ผ่าน" if _passed(row) else "ไม่ผ่าน"
    judge = row.get("judge") or {}
    return "\n".join(
        [
            f"# ข้อ {index:04d} - {row.get('id', '')}",
            "",
            "## โจทย์",
            "",
            _text_block(row.get("question", "")),
            "",
            "## คำตอบจาก Chatbot",
            "",
            _text_block(_answer_for_display(row)),
            "",
            "---",
            "",
            f"- ผลตรวจอัตโนมัติ: **{status}**",
            f"- Score: `{judge.get('score', '')}`",
            f"- เวลา: `{row.get('wall_sec', '')}` วินาที",
            f"- วิธีตอบ: `{row.get('mode', '')}`",
            f"- Error: `{_error_text(row)}`",
            f"- [เปิดรายละเอียด route/trace]({detail_link})",
            "",
        ]
    )


def _failure_report(failures: list[dict[str, Any]], case_links: dict[str, str]) -> str:
    diagnoses = {str(row["id"]): _failure_diagnosis(row) for row in failures}
    buckets = Counter(diagnosis["bucket"] for diagnosis in diagnoses.values())
    assessments = Counter(diagnosis["assessment"] for diagnosis in diagnoses.values())
    lines = [
        "# Failure Diagnosis - 60 ข้อ",
        "",
        "รายงานนี้อ่านโจทย์ คำตอบจริง route/mode เวลา และ judge error ของทุก failure จาก Typhoon run ใหม่",
        "",
        "## สรุป",
        "",
        f"- Failure ทั้งหมด: `{len(failures)}`",
        f"- Chatbot ผิดจริง: `{assessments.get('Chatbot ผิดจริง', 0)}`",
        f"- Judge ตรวจพลาด: `{assessments.get('Judge ตรวจพลาด', 0)}`",
        f"- ต้องตัดสิน Product Policy: `{assessments.get('ต้องตัดสิน Product Policy', 0)}`",
        "",
        "| Root-cause bucket | จำนวน |",
        "|---|---:|",
    ]
    for bucket, count in buckets.most_common():
        lines.append(f"| `{bucket}` | {count} |")
    for index, row in enumerate(failures, 1):
        diagnosis = diagnoses[str(row["id"])]
        lines.extend(
            [
                "",
                f"## {index}. {row['id']} - {diagnosis['assessment']}",
                "",
                f"- Root-cause bucket: `{diagnosis['bucket']}`",
                f"- เวลา: `{row.get('wall_sec', '')}` วินาที",
                f"- Mode: `{row.get('mode', '')}`",
                f"- Judge error: `{_error_text(row)}`",
                f"- Root cause: {diagnosis['root_cause']}",
                f"- ทำไมจึงผิด/ถูกมองว่าผิด: {diagnosis['why']}",
                f"- วิธีแก้: {diagnosis['fix']}",
                "",
                "**โจทย์**",
                "",
                _text_block(row.get("question", "")),
                "",
                "**คำตอบจาก Chatbot**",
                "",
                _text_block(_answer_for_display(row)),
                "",
                f"[เปิดไฟล์ Q&A รายข้อ]({case_links[str(row['id'])]})",
            ]
        )
    return "\n".join(lines) + "\n"


def _slow_report(slow_rows: list[dict[str, Any]], case_links: dict[str, str]) -> str:
    diagnoses = {str(row["id"]): _slow_diagnosis(row) for row in slow_rows}
    buckets = Counter(diagnosis["bucket"] for diagnosis in diagnoses.values())
    lines = [
        "# Slow Cases Over 10 Seconds - 44 ข้อ",
        "",
        "คำว่า slow ในรายงานนี้หมายถึงเกิน product target 10 วินาที ไม่ได้แปลว่าเกิด TimeoutError",
        "",
        f"- Slow ทั้งหมด: `{len(slow_rows)}`",
        f"- Slow แต่ตอบผ่าน: `{sum(_passed(row) for row in slow_rows)}`",
        f"- Slow และไม่ผ่าน: `{sum(not _passed(row) for row in slow_rows)}`",
        f"- เกิน configured 20 วินาที: `{sum(float(row.get('wall_sec') or 0) > 20 for row in slow_rows)}`",
        f"- Explicit timeout/deadline exception: `{sum(_explicit_timeout(row) for row in slow_rows)}`",
        "",
        "| Latency cause | จำนวน |",
        "|---|---:|",
    ]
    for bucket, count in buckets.most_common():
        lines.append(f"| `{bucket}` | {count} |")
    for index, row in enumerate(slow_rows, 1):
        diagnosis = diagnoses[str(row["id"])]
        visible_llm_sec = float(row.get("llm_elapsed_ms_total") or 0) / 1000
        lines.extend(
            [
                "",
                f"## {index}. {row['id']} - {row.get('wall_sec', '')}s",
                "",
                f"- ผล: **{'ผ่าน' if _passed(row) else 'ไม่ผ่าน'}**",
                f"- Latency bucket: `{diagnosis['bucket']}`",
                f"- Recorded LLM calls: `{row.get('llm_call_count', 0)}`",
                f"- LLM budget used calls ใน retained metadata: `{_budget_used_calls(row)}`",
                f"- Visible LLM elapsed: `{visible_llm_sec:.4f}` วินาที",
                f"- สาเหตุ: {diagnosis['cause']}",
                f"- วิธีแก้: {diagnosis['fix']}",
                "",
                "**โจทย์**",
                "",
                _text_block(row.get("question", "")),
                "",
                "**คำตอบจาก Chatbot**",
                "",
                _text_block(_answer_for_display(row)),
                "",
                f"[เปิดไฟล์ Q&A รายข้อ]({case_links[str(row['id'])]})",
            ]
        )
    return "\n".join(lines) + "\n"


def _analysis_report(rows: list[dict[str, Any]], failures: list[dict[str, Any]], slow: list[dict[str, Any]]) -> str:
    diagnoses = [_failure_diagnosis(row) for row in failures]
    failure_buckets = Counter(item["bucket"] for item in diagnoses)
    assessments = Counter(item["assessment"] for item in diagnoses)
    slow_buckets = Counter(_slow_diagnosis(row)["bucket"] for row in slow)
    overlap = [row for row in failures if float(row.get("wall_sec") or 0) > 10]
    double_rows = [row for row in slow if _budget_used_calls(row) >= 2]
    visible = [float(row.get("llm_elapsed_ms_total") or 0) / 1000 for row in double_rows]
    gaps = [float(row.get("wall_sec") or 0) - llm for row, llm in zip(double_rows, visible)]
    lines = [
        "# วิเคราะห์ Failure และเวลา - Fresh Typhoon 1,600 Cases",
        "",
        "## คำตอบตรงประเด็น",
        "",
        "ข้อที่ไม่ผ่านส่วนใหญ่ไม่ได้เกิดจาก timeout เพราะ failure 60 ข้อกับ slow over 10s 44 ข้อซ้อนกันเพียง 3 ข้อ",
        "",
        f"- ทั้งหมด: `{len(rows)}`",
        f"- ผ่าน: `{sum(_passed(row) for row in rows)}`",
        f"- ไม่ผ่าน: `{len(failures)}`",
        f"- เกิน 10 วินาที: `{len(slow)}`",
        f"- ไม่ผ่านและเกิน 10 วินาที: `{len(overlap)}`",
        f"- ไม่ผ่านแต่ไม่เกิน 10 วินาที: `{len(failures) - len(overlap)}`",
        f"- เกิน 10 วินาทีแต่ยังผ่าน: `{len(slow) - len(overlap)}`",
        f"- Explicit TimeoutError/deadline exception: `{sum(_explicit_timeout(row) for row in rows)}`",
        f"- เกิน configured 20 วินาที: `{sum(float(row.get('wall_sec') or 0) > 20 for row in rows)}`",
        "",
        "ดังนั้นต้องแยกคำว่า `ไม่ผ่าน`, `ช้ากว่าเป้า 10 วินาที` และ `timeout exception` ออกจากกัน",
        "",
        "## Failure 60 ข้อ",
        "",
        "| Assessment | จำนวน | ความหมาย |",
        "|---|---:|---|",
        f"| Chatbot ผิดจริง | {assessments.get('Chatbot ผิดจริง', 0)} | route, exception, unsupported claim หรือคำตอบคนละเรื่อง |",
        f"| Judge ตรวจพลาด | {assessments.get('Judge ตรวจพลาด', 0)} | คำตอบสื่อความหมายถูกแต่ไม่ตรง exact keyword |",
        f"| ต้องตัดสิน Product Policy | {assessments.get('ต้องตัดสิน Product Policy', 0)} | contract เดิมขัดกับเป้าหมาย broad assistant |",
        "",
        "| Root cause | จำนวน |",
        "|---|---:|",
    ]
    for bucket, count in failure_buckets.most_common():
        lines.append(f"| `{bucket}` | {count} |")
    lines.extend(
        [
            "",
            "### Root cause หลัก",
            "",
            "1. `general_concept_misrouted_equipment` 26 ข้อ: คำว่า keyboard ชนะ operation `คืออะไร` ทำให้ตอบรายการอุปกรณ์ PSU แทนคำจำกัดความ",
            "2. `substring_collision_price_in_kho_sia` 9 ข้อ: `ข้อเสีย` มี substring `เสีย` จึงถูกตีเป็น price query และถามกลับเรื่องบริการ/โซน",
            "3. `judge_false_negative_*` 19 ข้อ: `ความล่าช้า`, `ขอบพระคุณ`, `งานแข่งขันเกม` ถูกความหมายแต่ exact-keyword judge ไม่ยอมรับ",
            "4. `system_exception` 2 ข้อ: UnboundLocalError ทำให้ answer ว่าง",
            "5. อีก 4 ข้อ: Animal Crossing substring collision, game-zone ranking ผิด route, freshness hallucination และ product-scope policy mismatch",
            "",
            "## Slow 44 ข้อ",
            "",
            "| Latency cause | จำนวน | อธิบาย |",
            "|---|---:|---|",
            f"| Two sequential LLM calls | {slow_buckets.get('two_sequential_llm_calls', 0)} | Intent/review call แล้วตามด้วย answer call |",
            f"| Single slow generation | {slow_buckets.get('single_slow_generation', 0)} | call เดียวแต่ generation เกิน 10 วินาที |",
            f"| Wrong-route expensive retrieval | {slow_buckets.get('wrong_route_expensive_retrieval', 0)} | route ผิดและ retrieval/entity work แพง |",
            "",
        ]
    )
    if double_rows:
        lines.extend(
            [
                f"41 double-call cases มี wall เฉลี่ย `{statistics.mean(float(row.get('wall_sec') or 0) for row in double_rows):.4f}s`, "
                f"visible final LLM เฉลี่ย `{statistics.mean(visible):.4f}s` และเวลาที่ไม่อยู่ใน visible final call เฉลี่ย `{statistics.mean(gaps):.4f}s`",
                "",
                "`results.llm_call_count` บันทึก 1 call แต่ final metadata ระบุ `llm_budget_used_calls=2` จึงเป็น telemetry gap ด้วย ไม่ใช่หลักฐานว่าใช้ LLM แค่ครั้งเดียว",
                "",
            ]
        )
    lines.extend(
        [
            "## ลำดับแก้ที่แนะนำ",
            "",
            "1. P0: แก้ UnboundLocalError และเพิ่ม state initialization test",
            "2. P0: เปลี่ยน raw substring matcher เป็น boundary/context-aware matcher สำหรับ `ข้อเสีย`, `cross` และ price/control terms",
            "3. P0: ให้ deterministic game ranking และ exact entity veto route/ambiguity ที่ผิด",
            "4. P1: ทำ operation-first distinction ระหว่าง general definition กับ PSU inventory lookup",
            "5. P1: ทำ clear-general one-call path และ shape-based token budget เพื่อตัด double LLM",
            "6. P1: เพิ่ม freshness guard ที่ต้องมี live source/timestamp หรือ no-answer",
            "7. P2: แยก semantic correctness evaluator ออกจาก style/keyword lint โดยไม่แก้ expected ให้ตามคำตอบผิด",
            "8. เพิ่ม append-only timing/call ledger เพราะ trace cap 12 และ `llm_call_count` ปัจจุบันอธิบาย hidden call ไม่ครบ",
            "",
            "## ข้อจำกัด",
            "",
            "- Judge ปัจจุบันเป็น heuristic จึงมีทั้ง false negative และอาจมี false positive; ตัวเลขที่ปรับ false negative แล้วไม่ใช่ human-approved accuracy",
            "- Trace output จำกัด 12 entries ในเกือบทุกเคส จึงต้อง focused reproduction เมื่อต้องหา first wrong stage ที่เกิดก่อน retained trace",
            "- รอบนี้ใช้ global profile 20 วินาที ไม่ใช่ product profile 10 วินาที",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export simple question/answer Markdown for a chatbot benchmark run.")
    parser.add_argument("--results", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--details-relative-root", default="../../details")
    args = parser.parse_args()

    results_path = Path(args.results).resolve()
    summary_path = Path(args.summary).resolve()
    output_dir = Path(args.output_dir).resolve()
    cases_dir = output_dir / "cases"
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_dir.mkdir(parents=True, exist_ok=True)

    rows = _read_json(results_path)
    summary = _read_json(summary_path)
    if not isinstance(rows, list) or not isinstance(summary, dict):
        raise ValueError("Invalid benchmark results or summary")
    ids = [str(row.get("id") or "") for row in rows]
    if len(ids) != len(set(ids)) or any(not case_id for case_id in ids):
        raise ValueError("Result ids must be non-empty and unique")
    if int(summary.get("total") or 0) != len(rows):
        raise ValueError(f"Summary total {summary.get('total')} does not match results {len(rows)}")

    run_label = str(summary.get("run_label") or results_path.parent.name)
    case_links: dict[str, str] = {}
    index_lines = [
        "# Simple Chatbot Q&A Index",
        "",
        "แต่ละไฟล์มีโจทย์และคำตอบจริงจาก Chatbot โหมด Typhoon เป็นเนื้อหาหลัก",
        "",
        "| # | ID | ผล | เวลา | โจทย์ |",
        "|---:|---|---|---:|---|",
    ]
    for index, row in enumerate(rows, 1):
        case_id = str(row["id"])
        filename = f"{_safe_name(case_id)}.md"
        case_links[case_id] = f"cases/{filename}"
        detail_link = f"{args.details_relative_root}/{run_label}/{filename}"
        (cases_dir / filename).write_text(
            _case_markdown(index, row, detail_link),
            encoding="utf-8",
            newline="\n",
        )
        index_lines.append(
            f"| {index} | [{_table_text(case_id, 80)}](cases/{filename}) | "
            f"{'PASS' if _passed(row) else 'FAIL'} | {row.get('wall_sec', '')}s | "
            f"{_table_text(row.get('question'), 180)} |"
        )
    (output_dir / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8", newline="\n")

    failures = [row for row in rows if not _passed(row)]
    slow = sorted(
        [row for row in rows if float(row.get("wall_sec") or 0) > 10],
        key=lambda row: float(row.get("wall_sec") or 0),
        reverse=True,
    )
    (output_dir / "FAILED_60_WITH_QA_AND_CAUSE.md").write_text(
        _failure_report(failures, case_links),
        encoding="utf-8",
        newline="\n",
    )
    (output_dir / "SLOW_OVER_10S_44_WITH_QA.md").write_text(
        _slow_report(slow, case_links),
        encoding="utf-8",
        newline="\n",
    )
    (output_dir / "FAILURE_AND_LATENCY_ANALYSIS_TH.md").write_text(
        _analysis_report(rows, failures, slow),
        encoding="utf-8",
        newline="\n",
    )

    failure_counts = Counter(_failure_diagnosis(row)["bucket"] for row in failures)
    slow_counts = Counter(_slow_diagnosis(row)["bucket"] for row in slow)
    manifest = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "results": str(results_path),
        "summary": str(summary_path),
        "run_label": run_label,
        "model": summary.get("model"),
        "total": len(rows),
        "passed": sum(_passed(row) for row in rows),
        "failed": len(failures),
        "slow_over_10s": len(slow),
        "slow_and_failed": sum(not _passed(row) for row in slow),
        "explicit_timeout_exceptions": sum(_explicit_timeout(row) for row in rows),
        "case_markdown_count": len(rows),
        "failure_buckets": dict(failure_counts),
        "slow_buckets": dict(slow_counts),
    }
    (output_dir / "MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    readme = "\n".join(
        [
            "# Simple Chatbot Q&A - Typhoon",
            "",
            "ชุดนี้สร้างเพื่ออ่านคำถามและคำตอบจริงจาก Chatbot โดยไม่ต้องเปิด raw trace ก่อน",
            "",
            f"- ทั้งหมด: `{len(rows)}` ข้อ",
            f"- ผ่านอัตโนมัติ: `{sum(_passed(row) for row in rows)}`",
            f"- ไม่ผ่านอัตโนมัติ: `{len(failures)}`",
            f"- เกิน 10 วินาที: `{len(slow)}`",
            f"- ไม่ผ่านและเกิน 10 วินาที: `{sum(not _passed(row) for row in slow)}`",
            f"- Explicit timeout exception: `{sum(_explicit_timeout(row) for row in rows)}`",
            "",
            "## เปิดไฟล์",
            "",
            "- [Index Q&A ครบ 1,600 ข้อ](INDEX.md)",
            "- [Failure 60 ข้อ พร้อมโจทย์ คำตอบ และ root cause](FAILED_60_WITH_QA_AND_CAUSE.md)",
            "- [Slow 44 ข้อ พร้อมโจทย์ คำตอบ และ latency cause](SLOW_OVER_10S_44_WITH_QA.md)",
            "- [บทวิเคราะห์ Failure กับเวลา](FAILURE_AND_LATENCY_ANALYSIS_TH.md)",
            "- `cases/`: Markdown แยกหนึ่งไฟล์ต่อหนึ่งโจทย์",
            "",
            "หมายเหตุ: `FAIL` มาจาก heuristic judge จึงมีบางข้อที่คำตอบถูกความหมายแต่ keyword judge ตรวจพลาด",
            "",
        ]
    )
    (output_dir / "README.md").write_text(readme, encoding="utf-8", newline="\n")

    print(f"Output: {output_dir}")
    print(f"Case Markdown: {len(rows)}")
    print(f"Passed: {sum(_passed(row) for row in rows)}")
    print(f"Failed: {len(failures)}")
    print(f"Slow over 10s: {len(slow)}")
    print(f"Slow and failed: {sum(not _passed(row) for row in slow)}")
    print(f"Failure buckets: {dict(failure_counts)}")
    print(f"Slow buckets: {dict(slow_counts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
