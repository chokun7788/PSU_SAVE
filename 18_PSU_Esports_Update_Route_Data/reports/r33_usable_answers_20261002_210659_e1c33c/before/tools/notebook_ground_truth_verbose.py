from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from datetime import datetime
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

sys.path.insert(0, str(ROOT))
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from tools.run_ground_truth_fast_eval import keyword_status, source_status  # noqa: E402
from tools.run_ground_truth_pipeline_eval import quality_status  # noqa: E402


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _safe_label(label: str | None) -> str:
    if label:
        keep = []
        for char in label:
            keep.append(char if char.isalnum() or char in {"_", "-"} else "_")
        return "".join(keep).strip("_") or "notebook_verbose"
    return "notebook_verbose_" + datetime.now().strftime("%Y%m%d_%H%M%S")


def _source_rows(hits: list[dict[str, Any]]) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for hit in hits or []:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        source_id = str(hit.get("id") or metadata.get("title") or "")
        source_url = str(metadata.get("source_url") or metadata.get("url") or "")
        category = str(metadata.get("category") or "")
        source_ids = metadata.get("source_ids", [])
        source_ids_text = ", ".join(str(item) for item in source_ids) if isinstance(source_ids, list) else str(source_ids)
        key = (source_id, source_url)
        if key in seen:
            continue
        seen.add(key)
        sources.append({
            "id": source_id,
            "url": source_url,
            "category": category,
            "source_ids": source_ids_text,
        })
    return sources


def _source_markdown(sources: list[dict[str, str]]) -> str:
    if not sources:
        return "- ไม่มี source ที่ส่งกลับมา"
    lines: list[str] = []
    for source in sources:
        label_parts = [part for part in [source.get("id"), source.get("category"), source.get("source_ids")] if part]
        label = " / ".join(label_parts)
        url = source.get("url", "")
        if url.startswith("http"):
            lines.append(f"- [{url}]({url}) (`{label}`)")
        elif url:
            lines.append(f"- `{url}` (`{label}`)")
        else:
            lines.append(f"- `{label}`")
    return "\n".join(lines)


def _expected_markdown(item: dict[str, Any]) -> str:
    expected_keywords = item.get("expected_keywords", [])
    expected_sources = item.get("expected_source_keywords", [])
    category = item.get("category", "-")
    answer_type = item.get("answer_type", "-")
    difficulty = item.get("difficulty", "-")
    variant = item.get("variant_type", "-")
    parts = [
        "ต้องมีคำสำคัญ: " + (", ".join(str(item) for item in expected_keywords) if expected_keywords else "-"),
        "Expected source keywords: " + (", ".join(str(item) for item in expected_sources) if expected_sources else "-"),
        f"หมวด: {category}",
        f"ชนิดคำตอบ: {answer_type}",
        f"ระดับ: {difficulty}",
        f"variant: {variant}",
    ]
    return " | ".join(parts)


def _result_markdown(row: dict[str, Any]) -> str:
    no = row["no"]
    verdict = row["verdict"]
    verdict_th = "ถูก" if verdict == "PASS" else "ผิด"
    badge = "PASS" if verdict == "PASS" else "FAIL"
    keyword_ok = row.get("keyword_ok")
    source_ok = row.get("source_ok")
    quality_ok = row.get("quality_ok")
    validation_ok = not row.get("validation_errors")
    matched_sources = row.get("matched_source_keywords", [])
    missing_keywords = row.get("missing_keywords", [])
    missing_sources = row.get("missing_source_keywords", [])
    quality_problems = row.get("quality_problems", [])
    validation_errors = row.get("validation_errors", [])
    validation_warnings = row.get("validation_warnings", [])

    lines = [
        f"## {no}. [{badge}] {verdict_th}",
        "",
        f"**คำถาม:** {row.get('question', '')}",
        "",
        "**คำตอบ(จาก AI):**",
        "",
        str(row.get("answer", "")).strip() or "-",
        "",
        "**แหล่งข้อมูล:**",
        "",
        _source_markdown(row.get("sources", [])),
        "",
        "**เฉลย/เกณฑ์ที่ถูก:**",
        "",
        _expected_markdown(row.get("ground_truth", {})),
        "",
        "**ผลตรวจ:**",
        "",
        f"- สถานะ: {verdict_th}",
        f"- keyword_ok: `{keyword_ok}`",
        f"- source_ok: `{source_ok}` | matched: `{matched_sources}`",
        f"- quality_ok: `{quality_ok}`",
        f"- validation_ok: `{validation_ok}`",
        f"- route: `{row.get('route_category')}` | intent: `{row.get('route_intent')}`",
        f"- mode: `{row.get('mode')}` | elapsed: `{row.get('latency_sec')}` sec",
    ]
    if missing_keywords:
        lines.append(f"- missing_keywords: `{missing_keywords}`")
    if missing_sources:
        lines.append(f"- missing_source_keywords: `{missing_sources}`")
    if quality_problems:
        lines.append(f"- quality_problems: `{quality_problems}`")
    if validation_errors:
        lines.append(f"- validation_errors: `{validation_errors}`")
    if validation_warnings:
        lines.append(f"- validation_warnings: `{validation_warnings}`")
    return "\n".join(lines).rstrip() + "\n"


def _summary_markdown(results: list[dict[str, Any]], result_path: Path, report_path: Path) -> str:
    total = len(results)
    passed = sum(1 for row in results if row.get("verdict") == "PASS")
    failed = sum(1 for row in results if row.get("verdict") == "FAIL")
    errors = sum(1 for row in results if row.get("verdict") == "ERROR")
    latencies = [float(row.get("latency_sec") or 0) for row in results]
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
    mode_counts = Counter(str(row.get("mode", "-")) for row in results)
    category_counts = Counter(str(row.get("route_category", "-")) for row in results)
    lines = [
        "# Ground Truth Verbose Result",
        "",
        f"- Total: {total}",
        f"- PASS: {passed}",
        f"- FAIL: {failed}",
        f"- ERROR: {errors}",
        f"- Pass rate: {(passed / total * 100 if total else 0):.2f}%",
        f"- Average latency: {avg_latency:.4f}s",
        f"- Results JSONL: `{result_path}`",
        f"- Report MD: `{report_path}`",
        "",
        "## Mode Summary",
    ]
    for mode, count in mode_counts.most_common():
        lines.append(f"- `{mode}`: {count}")
    lines.append("")
    lines.append("## Route Summary")
    for category, count in category_counts.most_common():
        lines.append(f"- `{category}`: {count}")
    return "\n".join(lines).rstrip() + "\n"


def _display_markdown(markdown_text: str) -> None:
    try:
        from IPython.display import Markdown, display

        display(Markdown(markdown_text))
    except Exception:
        print(markdown_text)


def evaluate_ground_truth_verbose(
    ground_truth_path: str | Path | None = None,
    *,
    label: str | None = None,
    start: int = 1,
    end: int | None = None,
    limit: int | None = None,
) -> tuple[list[dict[str, Any]], Path, Path]:
    gt_path = Path(ground_truth_path) if ground_truth_path else DEFAULT_GROUND_TRUTH
    safe_label = _safe_label(label)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    result_path = REPORT_DIR / f"pipeline_ground_truth_verbose_results_{safe_label}.jsonl"
    report_path = REPORT_DIR / f"pipeline_ground_truth_verbose_report_{safe_label}.md"

    all_rows = load_jsonl(gt_path)
    start_index = max(1, int(start)) - 1
    if limit is not None:
        selected = list(enumerate(all_rows[start_index:start_index + int(limit)], start=start_index + 1))
    elif end is not None:
        selected = list(enumerate(all_rows[start_index:int(end)], start=start_index + 1))
    else:
        selected = list(enumerate(all_rows[start_index:], start=start_index + 1))

    results: list[dict[str, Any]] = []
    report_parts: list[str] = []
    with result_path.open("w", encoding="utf-8", newline="\n") as file:
        for no, item in selected:
            started = time.perf_counter()
            try:
                result_obj = answer_question_pipeline_debug(item["question"])
                answer = result_obj.answer
                hits = result_obj.hits
                keyword_ok, missing_keywords = keyword_status(answer, item.get("expected_keywords", []))
                source_ok, missing_sources = source_status(hits, item.get("expected_source_keywords", []))
                quality_ok, quality_problems = quality_status(answer, item)
                validation_errors = list(result_obj.validation.errors)
                expected_sources = [str(value) for value in item.get("expected_source_keywords", [])]
                matched_sources = [value for value in expected_sources if value not in missing_sources]
                verdict = "PASS" if keyword_ok and source_ok and quality_ok and not validation_errors else "FAIL"
                row = {
                    "no": no,
                    "id": item.get("id", f"row_{no}"),
                    "verdict": verdict,
                    "question": item.get("question", ""),
                    "answer": answer,
                    "ground_truth": item,
                    "expected_keywords": item.get("expected_keywords", []),
                    "expected_source_keywords": item.get("expected_source_keywords", []),
                    "keyword_ok": keyword_ok,
                    "source_ok": source_ok,
                    "quality_ok": quality_ok,
                    "matched_source_keywords": matched_sources,
                    "missing_keywords": missing_keywords,
                    "missing_source_keywords": missing_sources,
                    "quality_problems": quality_problems,
                    "validation_errors": validation_errors,
                    "validation_warnings": list(result_obj.validation.warnings),
                    "mode": result_obj.mode,
                    "route_category": result_obj.route.category,
                    "route_intent": result_obj.route.intent,
                    "confidence": result_obj.confidence,
                    "latency_sec": result_obj.elapsed,
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "sources": _source_rows(hits),
                    "retrieved_ids": [hit.get("id") for hit in hits],
                }
            except Exception as exc:
                row = {
                    "no": no,
                    "id": item.get("id", f"row_{no}"),
                    "verdict": "ERROR",
                    "question": item.get("question", ""),
                    "answer": "",
                    "ground_truth": item,
                    "expected_keywords": item.get("expected_keywords", []),
                    "expected_source_keywords": item.get("expected_source_keywords", []),
                    "keyword_ok": False,
                    "source_ok": False,
                    "quality_ok": False,
                    "matched_source_keywords": [],
                    "missing_keywords": item.get("expected_keywords", []),
                    "missing_source_keywords": item.get("expected_source_keywords", []),
                    "quality_problems": [],
                    "validation_errors": [repr(exc)],
                    "validation_warnings": [],
                    "mode": "error",
                    "route_category": "error",
                    "route_intent": "error",
                    "confidence": 0.0,
                    "latency_sec": 0.0,
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "sources": [],
                    "retrieved_ids": [],
                }
            results.append(row)
            file.write(json.dumps(row, ensure_ascii=False) + "\n")
            report_parts.append(_result_markdown(row))

    summary = _summary_markdown(results, result_path, report_path)
    report_path.write_text(summary + "\n".join(report_parts), encoding="utf-8", newline="\n")
    return results, result_path, report_path


def run_ground_truth_verbose_display(
    ground_truth_path: str | Path | None = None,
    *,
    label: str | None = None,
    start: int = 1,
    end: int | None = None,
    limit: int | None = None,
    show_pass: bool = True,
    only_fail: bool = False,
) -> list[dict[str, Any]]:
    results, result_path, report_path = evaluate_ground_truth_verbose(
        ground_truth_path,
        label=label,
        start=start,
        end=end,
        limit=limit,
    )
    _display_markdown(_summary_markdown(results, result_path, report_path))
    for row in results:
        if only_fail and row.get("verdict") == "PASS":
            continue
        if not show_pass and row.get("verdict") == "PASS":
            continue
        _display_markdown(_result_markdown(row))
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground-truth", default=str(DEFAULT_GROUND_TRUTH))
    parser.add_argument("--label", default=None)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--only-fail", action="store_true")
    args = parser.parse_args()
    rows = run_ground_truth_verbose_display(
        args.ground_truth,
        label=args.label,
        start=args.start,
        end=args.end,
        limit=args.limit,
        only_fail=args.only_fail,
    )
    return 0 if all(row.get("verdict") == "PASS" for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
