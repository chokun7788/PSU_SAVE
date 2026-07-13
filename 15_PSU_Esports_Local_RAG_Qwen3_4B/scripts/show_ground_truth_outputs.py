from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


PROJECT_DIR = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_DIR.parent / "16_PSU_Esports_RAG_Experiment_Timeline"
GROUND_TRUTH_PATH = PROJECT_DIR / "ground_truth" / "ground_truth_full.jsonl"
DEFAULT_RESULTS_PATH = REPORT_DIR / "ground_truth_eval_results_2026-06-29.jsonl"
DEFAULT_OUTPUT_PATH = REPORT_DIR / "10_ground_truth_qa_output_2026-06-29.md"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"ไม่พบไฟล์: {path}")

    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSONL ผิดรูปแบบที่ {path}:{line_no}") from exc
    return rows


def normalize_text(text: Any) -> str:
    return " ".join(str(text or "").split())


def bullet_values(values: list[Any]) -> str:
    clean_values = [normalize_text(value) for value in values if normalize_text(value)]
    return ", ".join(clean_values) if clean_values else "-"


def expected_answer_text(item: dict[str, Any]) -> str:
    """Ground truth ตอนนี้เก็บเป็น expected keywords ไม่ใช่เฉลยประโยคเต็ม."""
    expected_answer = normalize_text(item.get("expected_answer"))
    if expected_answer:
        return expected_answer

    expected_keywords = item.get("expected_keywords") or []
    expected_sources = item.get("expected_source_keywords") or []
    parts: list[str] = []
    if expected_keywords:
        parts.append(f"ต้องมีคำสำคัญ: {bullet_values(expected_keywords)}")
    if expected_sources:
        parts.append(f"แหล่งข้อมูลที่คาดว่าเกี่ยวข้อง: {bullet_values(expected_sources)}")
    if not parts:
        parts.append("ยังไม่ได้กำหนด expected_keywords/expected_answer")
    return " | ".join(parts)


def answer_text(result: dict[str, Any] | None, answer_limit: int) -> str:
    if not result:
        return "ยังไม่มีผลลัพธ์ AI สำหรับข้อนี้ ให้รัน scripts/run_ground_truth_eval.py ก่อน"

    answer = normalize_text(result.get("answer"))
    if not answer:
        answer = normalize_text(result.get("answer_short"))
    if not answer:
        answer = "AI ยังไม่ได้คืนคำตอบ"

    if answer_limit > 0 and len(answer) > answer_limit:
        return answer[:answer_limit].rstrip() + "..."
    return answer


def build_report(
    ground_truth_rows: list[dict[str, Any]],
    result_rows: list[dict[str, Any]],
    *,
    answer_limit: int,
    include_meta: bool,
    fail_only: bool,
) -> str:
    result_by_id = {row.get("id"): row for row in result_rows}

    selected_rows: list[tuple[dict[str, Any], dict[str, Any] | None]] = []
    for item in ground_truth_rows:
        result = result_by_id.get(item.get("id"))
        if fail_only and result and result.get("verdict") == "PASS":
            continue
        selected_rows.append((item, result))

    pass_count = sum(1 for row in result_rows if row.get("verdict") == "PASS")
    fail_count = sum(1 for row in result_rows if row.get("verdict") == "FAIL")

    lines: list[str] = [
        "# Ground Truth QA Output - PSU Esports Local RAG",
        "",
        f"- จำนวน Ground Truth ทั้งหมด: {len(ground_truth_rows)} ข้อ",
        f"- จำนวนที่แสดงในไฟล์นี้: {len(selected_rows)} ข้อ",
        f"- ผลประเมินล่าสุด: PASS {pass_count} / FAIL {fail_count}",
        "- หมายเหตุ: ไฟล์ ground_truth_full.jsonl ตอนนี้ยังไม่มีเฉลยเป็นประโยคเต็มทุกข้อ จึงแสดงเฉลยจาก expected_keywords และ expected_source_keywords",
        "",
    ]

    for index, (item, result) in enumerate(selected_rows, 1):
        lines.append(f"{index}.คำถาม : {normalize_text(item.get('question'))}")
        lines.append(f"คำตอบ(จากAI) : {answer_text(result, answer_limit)}")
        lines.append(f"เฉลย : {expected_answer_text(item)}")

        if include_meta:
            mode = normalize_text(result.get("mode") if result else "-")
            verdict = normalize_text(result.get("verdict") if result else "-")
            latency = result.get("latency_sec") if result else "-"
            retrieved_ids = bullet_values(result.get("retrieved_ids") or []) if result else "-"
            lines.append(f"ผลตรวจ : {verdict} | mode: {mode} | latency_sec: {latency} | retrieved_ids: {retrieved_ids}")

        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="แสดงผล Ground Truth 105 ข้อในรูปแบบ คำถาม / คำตอบจาก AI / เฉลย"
    )
    parser.add_argument(
        "--ground-truth",
        type=Path,
        default=GROUND_TRUTH_PATH,
        help="path ของ ground_truth_full.jsonl",
    )
    parser.add_argument(
        "--results",
        type=Path,
        default=DEFAULT_RESULTS_PATH,
        help="path ของไฟล์ ground_truth_eval_results_*.jsonl",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="path ของไฟล์ .md ที่ต้องการสร้าง",
    )
    parser.add_argument(
        "--answer-limit",
        type=int,
        default=0,
        help="จำกัดความยาวคำตอบ AI ต่อข้อเป็นจำนวนตัวอักษร ใส่ 0 เพื่อไม่ตัดคำตอบ",
    )
    parser.add_argument(
        "--include-meta",
        action="store_true",
        help="แสดง verdict/mode/latency/retrieved_ids เพิ่มในแต่ละข้อ",
    )
    parser.add_argument(
        "--fail-only",
        action="store_true",
        help="แสดงเฉพาะข้อที่ FAIL จากผล eval ล่าสุด",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    ground_truth_rows = load_jsonl(args.ground_truth)
    result_rows = load_jsonl(args.results)
    report = build_report(
        ground_truth_rows,
        result_rows,
        answer_limit=max(args.answer_limit, 0),
        include_meta=args.include_meta,
        fail_only=args.fail_only,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")

    pass_count = sum(1 for row in result_rows if row.get("verdict") == "PASS")
    fail_count = sum(1 for row in result_rows if row.get("verdict") == "FAIL")
    print(f"สร้างไฟล์แล้ว: {args.output}")
    print(f"Ground Truth: {len(ground_truth_rows)} ข้อ | PASS {pass_count} | FAIL {fail_count}")
    print("")
    print("ตัวอย่าง 3 ข้อแรก")
    print("-" * 60)
    preview_blocks = report.split("\n\n", 2)
    if len(preview_blocks) >= 3:
        first_items = "\n\n".join(preview_blocks[2].split("\n\n")[:3])
        print(first_items)
    else:
        print(report)


if __name__ == "__main__":
    main()
