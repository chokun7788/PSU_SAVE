from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVAL = ROOT / "reports" / "pipeline_ground_truth_results_quality_pipeline_round7_new_patterns_fix_20260702.jsonl"
DEFAULT_MD = ROOT / "data" / "human_review" / "human_review_pipeline_quality_round7_new_patterns_fix_full_360.md"
DEFAULT_JSONL = ROOT / "data" / "human_review" / "human_review_pipeline_quality_round7_new_patterns_fix_full_360.jsonl"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def review_json_row(idx: int, row: dict[str, Any], eval_path: Path) -> dict[str, Any]:
    return {
        "review_no": idx,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source_eval_file": str(eval_path),
        "question_id": row.get("id") or f"row_{idx}",
        "category": row.get("category", ""),
        "answer_type": row.get("answer_type", ""),
        "difficulty": row.get("difficulty", ""),
        "route": row.get("mode") or row.get("route", ""),
        "auto_verdict": row.get("verdict", ""),
        "latency_sec": row.get("latency_sec", row.get("elapsed", "")),
        "question": row.get("question", ""),
        "ai_answer": row.get("answer", ""),
        "expected_keywords": row.get("expected_keywords", []),
        "expected_source_keywords": row.get("expected_source_keywords", []),
        "human_decision": "",
        "intent_score_0_4": None,
        "correctness_score_0_4": None,
        "completeness_score_0_4": None,
        "tone_score_0_4": None,
        "route_score_0_4": None,
        "error_tags": [],
        "reviewer_notes": "",
        "fix_suggestion": "",
    }


def write_review_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def markdown_for_row(idx: int, row: dict[str, Any]) -> str:
    question_id = row.get("id") or f"row_{idx}"
    category = row.get("category", "")
    answer_type = row.get("answer_type", "")
    difficulty = row.get("difficulty", "")
    route = row.get("mode") or row.get("route", "")
    verdict = row.get("verdict", "")
    question = row.get("question", "")
    answer = row.get("answer", "")
    expected_keywords = as_text(row.get("expected_keywords", []))
    expected_sources = as_text(row.get("expected_source_keywords", []))

    return f"""## {idx}. [{verdict}] {question_id}

หมวด: `{category}` | ชนิดคำตอบ: `{answer_type}` | ระดับ: `{difficulty}` | Route: `{route}`

**คำถาม:** {question}

**คำตอบจาก AI:**

```text
{answer}
```

**เฉลย/เกณฑ์อัตโนมัติ:** ต้องมีคำสำคัญ: `{expected_keywords}` | source keyword: `{expected_sources}`

**Human Review**

- ตรงเจตนาคำถาม 0-4:
- ความถูกต้อง 0-4:
- ความครบถ้วน 0-4:
- น้ำเสียง/อ่านง่าย 0-4:
- Route เหมาะไหม 0-4:
- Decision (`pass` / `minor_fix` / `major_fix` / `needs_data` / `needs_policy`):
- Error tags:
- หมายเหตุ:
- สิ่งที่ควรแก้:
"""


def write_review_markdown(path: Path, rows: list[dict[str, Any]], eval_path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now().isoformat(timespec="seconds")
    pass_count = sum(1 for row in rows if row.get("verdict") == "PASS")
    fail_count = sum(1 for row in rows if row.get("verdict") == "FAIL")

    header = f"""# Human Review Checker - PSU Esports Chatbot

สร้างเมื่อ: {now}

ไฟล์นี้ใช้สำหรับตรวจคุณภาพคำตอบด้วยคน หลังจากระบบ Ground Truth อัตโนมัติเช็ค keyword/source แล้ว

## วิธีให้คะแนน

- `ตรงเจตนาคำถาม`: ประโยคแรกตอบสิ่งที่ผู้ใช้ถามจริงไหม เช่น ถ้าถาม “ต่างกันเท่าไหร่” ควรขึ้นต้นด้วย “ต่างกัน ... บาท”
- `ความถูกต้อง`: ราคา เวลา กฎ และกลุ่มผู้ใช้ถูกไหม
- `ความครบถ้วน`: มีรายละเอียดที่จำเป็นครบไหม ถ้าถามเวลาโดยไม่ระบุวันควรบอกภาพรวม Monday-Friday และ Maintenance
- `น้ำเสียง/อ่านง่าย`: สุภาพ กระชับ ไม่วกวน ไม่ทำให้ลูกค้าสับสน
- `Route เหมาะไหม`: ควรใช้ rule/calculator/RAG/no-answer ถูกทางไหม

## Decision ที่แนะนำ

- `pass`: ใช้งานได้แล้ว
- `minor_fix`: ข้อเท็จจริงถูก แต่เรียงคำตอบแปลก/ขาดรายละเอียดเล็กน้อย
- `major_fix`: ตอบคนละประเด็น ราคาผิด เวลา/กฎผิด หรือทำให้เข้าใจผิด
- `needs_data`: ข้อมูลไม่มีจริง ต้องขอไฟล์/กฎ/นโยบายเพิ่ม
- `needs_policy`: ต้องให้ผู้ดูแลยืนยัน เพราะกระทบกฎหรือการดำเนินงานจริง

## Auto Summary

- Source eval: `{eval_path}`
- Total: {len(rows)}
- Auto PASS: {pass_count}
- Auto FAIL: {fail_count}

> หมายเหตุ: Auto PASS แปลว่า keyword/source ผ่านเท่านั้น ยังต้องดู Human Review เพื่อเช็คว่าตอบตรงเจตนาและอ่านเป็นธรรมชาติไหม

---
"""
    body = "\n".join(markdown_for_row(idx, row) for idx, row in enumerate(rows, 1))
    path.write_text(header + "\n" + body, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval-path", default=str(DEFAULT_EVAL))
    parser.add_argument("--limit", type=int, default=0, help="0 means all rows")
    parser.add_argument("--md-output", default=str(DEFAULT_MD))
    parser.add_argument("--jsonl-output", default=str(DEFAULT_JSONL))
    args = parser.parse_args()

    eval_path = Path(args.eval_path)
    rows = read_jsonl(eval_path)
    if args.limit and args.limit > 0:
        rows = rows[: args.limit]
    if not rows:
        print(f"No rows found: {eval_path}")
        return 1

    md_path = Path(args.md_output)
    jsonl_path = Path(args.jsonl_output)
    write_review_markdown(md_path, rows, eval_path)
    write_review_jsonl(jsonl_path, [review_json_row(idx, row, eval_path) for idx, row in enumerate(rows, 1)])
    print(f"Wrote markdown review: {md_path}")
    print(f"Wrote jsonl review: {jsonl_path}")
    print(f"Rows: {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
