from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parents[0]
DEFAULT_GROUND_TRUTH = BASE / "15_PSU_Esports_Local_RAG_Qwen3_4B" / "ground_truth" / "ground_truth_v2_360.jsonl"
REPORT_DIR = ROOT / "reports"
RUN_DATE = date.today().isoformat()

sys.path.insert(0, str(ROOT))
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from tools.run_ground_truth_fast_eval import keyword_status, short_answer, source_status  # noqa: E402


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def quality_expectations(item: dict[str, Any]) -> dict[str, list[str]]:
    question = str(item.get("question", "")).lower()
    expects: dict[str, list[str]] = {"must_contain": [], "must_not_contain": [], "must_start_with_any": []}

    if "morning" in question and "afternoon" in question and ("วันจันทร์" in question or "จันทร์" in question or "monday" in question):
        expects["must_contain"].extend(["13:00", "16:00", "Maintenance"])
        expects["must_not_contain"].extend(["24 ชั่วโมง", "24 hours"])
        expects["must_start_with_any"].extend(["วันจันทร์ Morning เล่นไม่ได้", "Morning เล่นไม่ได้", "วันจันทร์ช่วงเช้า"])

    if "ต่างกัน" in question or "ต่างกันเท่า" in question:
        expects["must_start_with_any"].append("ต่างกัน")

    if ("ราคา" in question or "เท่าไหร่" in question or "กี่บาท" in question) and item.get("category") == "service_fee":
        expects["must_not_contain"].append("ยังไม่ทราบกลุ่มผู้ใช้")

    return expects


def quality_status(answer: str, item: dict[str, Any]) -> tuple[bool, list[str]]:
    expects = quality_expectations(item)
    problems: list[str] = []
    answer_lower = answer.lower()
    first = ""
    for line in answer.splitlines():
        if line.strip():
            first = line.strip()
            break
    first_core = first
    for prefix in ("คำตอบ:", "Answer:"):
        if first_core.lower().startswith(prefix.lower()):
            first_core = first_core[len(prefix):].strip()
            break

    for text in expects["must_contain"]:
        if text.lower() not in answer_lower:
            problems.append(f"quality missing: {text}")
    for text in expects["must_not_contain"]:
        if text.lower() in answer_lower:
            problems.append(f"quality forbidden: {text}")
    starts = expects["must_start_with_any"]
    if starts and not any(first_core.startswith(text) for text in starts):
        problems.append("quality first sentence mismatch: " + " OR ".join(starts))

    if item.get("category") == "service_fee":
        direct_answer = re.split(r"\n\s*\nรายละเอียดจากตาราง:", answer, maxsplit=1)[0]
        direct_lower = direct_answer.lower().replace(",", "")
        direct_missing = [
            str(keyword)
            for keyword in item.get("expected_keywords", [])
            if str(keyword).lower().replace(",", "") not in direct_lower
        ]
        if direct_missing:
            problems.append("service_fee direct answer missing: " + ", ".join(direct_missing))
    return not problems, problems


def build_report(results: list[dict[str, Any]], result_path: Path) -> str:
    total = len(results)
    passed = sum(1 for row in results if row["verdict"] == "PASS")
    failed = sum(1 for row in results if row["verdict"] == "FAIL")
    errors = sum(1 for row in results if row["verdict"] == "ERROR")
    latencies = [float(row["latency_sec"]) for row in results if isinstance(row.get("latency_sec"), (int, float))]
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
    p95_latency = sorted(latencies)[int(len(latencies) * 0.95) - 1] if latencies else 0.0
    mode_counts = Counter(str(row.get("mode", "unknown")) for row in results)
    category_counts = Counter(str(row.get("route_category", "unknown")) for row in results)

    lines = [
        "# Pipeline Ground Truth Evaluation",
        "",
        f"วันที่: {RUN_DATE}",
        "",
        "## Summary",
        "",
        f"- Total: {total}",
        f"- PASS: {passed}",
        f"- FAIL: {failed}",
        f"- ERROR: {errors}",
        f"- Pass rate: {(passed / total * 100 if total else 0):.2f}%",
        f"- Average latency: {avg_latency:.4f}s",
        f"- P95 latency: {p95_latency:.4f}s",
        f"- Keyword fail: {sum(1 for row in results if not row.get('keyword_ok'))}",
        f"- Source fail: {sum(1 for row in results if not row.get('source_ok'))}",
        f"- Quality fail: {sum(1 for row in results if not row.get('quality_ok'))}",
        f"- Validation fail: {sum(1 for row in results if row.get('validation_errors'))}",
        "",
        "## Mode Distribution",
        "",
    ]
    for mode, count in mode_counts.most_common():
        lines.append(f"- `{mode}`: {count}")

    lines.extend(["", "## Route Category Distribution", ""])
    for category, count in category_counts.most_common():
        lines.append(f"- `{category}`: {count}")

    failed_rows = [row for row in results if row["verdict"] != "PASS"]
    lines.extend(["", "## Failed Cases", ""])
    if not failed_rows:
        lines.append("No failed cases.")
    else:
        lines.extend(["| ID | Category | Route | Problem | Answer Short |", "|---|---|---|---|---|"])
        for row in failed_rows:
            problems = []
            problems.extend(row.get("missing_keywords", []))
            problems.extend(row.get("missing_source_keywords", []))
            problems.extend(row.get("quality_problems", []))
            problems.extend(row.get("validation_errors", []))
            answer = str(row.get("answer_short", "")).replace("|", "\\|")
            lines.append(f"| {row['id']} | {row.get('category')} | `{row.get('route_category')}` | {'; '.join(problems)} | {answer} |")

    lines.extend(["", "## Files", "", f"- Results JSONL: `{result_path}`"])
    return "\n".join(lines) + "\n"


def evaluate(ground_truth_path: Path, label: str, limit: int | None = None) -> list[dict[str, Any]]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    result_path = REPORT_DIR / f"pipeline_ground_truth_results_{label}.jsonl"
    report_path = REPORT_DIR / f"pipeline_ground_truth_report_{label}.md"
    rows = load_jsonl(ground_truth_path)
    if limit:
        rows = rows[:limit]

    results: list[dict[str, Any]] = []
    with result_path.open("w", encoding="utf-8", newline="\n") as f:
        for index, item in enumerate(rows, 1):
            started = time.perf_counter()
            try:
                result_obj = answer_question_pipeline_debug(item["question"])
                answer = result_obj.answer
                hits = result_obj.hits
                keyword_ok, missing_keywords = keyword_status(answer, item.get("expected_keywords", []))
                source_ok, missing_sources = source_status(hits, item.get("expected_source_keywords", []))
                quality_ok, quality_problems = quality_status(answer, item)
                validation_errors = list(result_obj.validation.errors)
                verdict = "PASS" if keyword_ok and source_ok and quality_ok and not validation_errors else "FAIL"
                result = {
                    "id": item["id"],
                    "category": item.get("category"),
                    "answer_type": item.get("answer_type"),
                    "difficulty": item.get("difficulty"),
                    "question": item["question"],
                    "expected_keywords": item.get("expected_keywords", []),
                    "expected_source_keywords": item.get("expected_source_keywords", []),
                    "mode": result_obj.mode,
                    "route_category": result_obj.route.category,
                    "route_intent": result_obj.route.intent,
                    "confidence": result_obj.confidence,
                    "verdict": verdict,
                    "keyword_ok": keyword_ok,
                    "source_ok": source_ok,
                    "quality_ok": quality_ok,
                    "missing_keywords": missing_keywords,
                    "missing_source_keywords": missing_sources,
                    "quality_problems": quality_problems,
                    "validation_errors": validation_errors,
                    "validation_warnings": list(result_obj.validation.warnings),
                    "latency_sec": result_obj.elapsed,
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "retrieved_ids": [hit.get("id") for hit in hits],
                    "trace": [trace.__dict__ for trace in result_obj.trace],
                    "answer": answer,
                    "answer_short": short_answer(answer),
                }
            except Exception as exc:
                result = {
                    "id": item["id"],
                    "category": item.get("category"),
                    "question": item.get("question", ""),
                    "mode": "error",
                    "route_category": "error",
                    "verdict": "ERROR",
                    "keyword_ok": False,
                    "source_ok": False,
                    "quality_ok": False,
                    "missing_keywords": item.get("expected_keywords", []),
                    "missing_source_keywords": item.get("expected_source_keywords", []),
                    "quality_problems": [],
                    "validation_errors": [repr(exc)],
                    "answer": "",
                    "answer_short": "",
                    "latency_sec": 0.0,
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "trace": [],
                }
            results.append(result)
            f.write(json.dumps(result, ensure_ascii=False) + "\n")
            print(f"[{index}/{len(rows)}] {result['id']} -> {result['verdict']} route={result.get('route_category')} mode={result.get('mode')} latency={result.get('latency_sec')}")

    report_path.write_text(build_report(results, result_path), encoding="utf-8", newline="\n")
    print(report_path)
    print(result_path)
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground-truth", default=str(DEFAULT_GROUND_TRUTH))
    parser.add_argument("--label", default=f"quality_pipeline_{RUN_DATE}")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()
    evaluate(Path(args.ground_truth), args.label, args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
