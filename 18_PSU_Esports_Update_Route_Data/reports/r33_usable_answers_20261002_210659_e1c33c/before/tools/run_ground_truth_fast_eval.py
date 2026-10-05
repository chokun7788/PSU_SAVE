from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
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
from app.runtime.fast_answer import answer_question_fast  # noqa: E402


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def keyword_status(answer: str, expected_keywords: list[str]) -> tuple[bool, list[str]]:
    if not expected_keywords:
        return True, []

    def norm(text: str) -> str:
        return str(text).lower().replace(",", "")

    answer_lower = norm(answer)
    missing = [kw for kw in expected_keywords if norm(kw) not in answer_lower]
    return not missing, missing


def source_status(hits: list[dict[str, Any]], expected_source_keywords: list[str]) -> tuple[bool, list[str]]:
    if not expected_source_keywords:
        return True, []
    source_aliases: list[str] = []
    for hit in hits:
        metadata = hit.get("metadata", {})
        source_url = str(metadata.get("source_url", "")).lower()
        category = str(metadata.get("category", "")).lower()
        source_id = str(hit.get("id", "")).lower()
        if "esports.computing.psu.ac.th" in source_url:
            source_aliases.append("Reservation")
        if "service-fee" in source_url or "service_fee" in category or "service_fee" in source_id:
            source_aliases.extend(["service_fee", "Service Fee"])
        if "/home" in source_url:
            source_aliases.append("home")
        if "/knowledge" in source_url:
            source_aliases.append("Knowledge")
        if "/events-news/news" in source_url:
            source_aliases.append("News")
        if "/members" in source_url:
            source_aliases.append("Members")
        if "contact" in category or "/contact" in source_url:
            source_aliases.append("Contact")

    haystack = " ".join(
        [
            str(hit.get("id", "")) + " "
            + str(hit.get("metadata", {}).get("title", "")) + " "
            + str(hit.get("metadata", {}).get("category", "")) + " "
            + str(hit.get("metadata", {}).get("source_url", "")) + " "
            + str(hit.get("metadata", {}).get("source_ids", ""))
            for hit in hits
        ]
        + source_aliases
    ).lower()
    missing = [kw for kw in expected_source_keywords if kw.lower() not in haystack]
    return not missing, missing


def short_answer(answer: str, limit: int = 220) -> str:
    text = " ".join((answer or "").split())
    return text if len(text) <= limit else text[:limit].rstrip() + "..."


def group_summary(results: list[dict[str, Any]], key: str) -> list[tuple[str, int, int, float]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in results:
        grouped[str(row.get(key, "-"))].append(row)
    summary = []
    for name, rows in grouped.items():
        total = len(rows)
        passed = sum(1 for row in rows if row["verdict"] == "PASS")
        summary.append((name, passed, total, passed / total * 100 if total else 0.0))
    return sorted(summary, key=lambda item: (-item[3], item[0]))


def build_report(results: list[dict[str, Any]], result_path: Path) -> str:
    total = len(results)
    passed = sum(1 for row in results if row["verdict"] == "PASS")
    failed = sum(1 for row in results if row["verdict"] == "FAIL")
    errors = sum(1 for row in results if row["verdict"] == "ERROR")
    pass_rate = passed / total * 100 if total else 0.0
    latencies = [float(row["latency_sec"]) for row in results if isinstance(row.get("latency_sec"), (int, float))]
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
    p95_latency = sorted(latencies)[int(len(latencies) * 0.95) - 1] if latencies else 0.0
    mode_counts = Counter(str(row.get("mode", "unknown")) for row in results)

    lines = [
        "# Fast Ground Truth Evaluation - PSU Esports Update Runtime",
        "",
        f"วันที่: {RUN_DATE}",
        "",
        "## Summary",
        "",
        f"- Total: {total}",
        f"- PASS: {passed}",
        f"- FAIL: {failed}",
        f"- ERROR: {errors}",
        f"- Pass rate: {pass_rate:.2f}%",
        f"- Average latency: {avg_latency:.4f}s",
        f"- P95 latency: {p95_latency:.4f}s",
        f"- Keyword fail: {sum(1 for row in results if not row.get('keyword_ok'))}",
        f"- Source fail: {sum(1 for row in results if not row.get('source_ok'))}",
        "",
        "## Mode Distribution",
        "",
    ]
    for mode, count in mode_counts.most_common():
        lines.append(f"- `{mode}`: {count}")

    for key, title in [
        ("category", "By Category"),
        ("answer_type", "By Answer Type"),
        ("difficulty", "By Difficulty"),
        ("mode", "By Mode"),
    ]:
        lines.extend(["", f"## {title}", "", "| Group | PASS | Total | Pass rate |", "|---|---:|---:|---:|"])
        for name, ok, total_count, rate in group_summary(results, key):
            lines.append(f"| {name} | {ok} | {total_count} | {rate:.2f}% |")

    failed_rows = [row for row in results if row["verdict"] != "PASS"]
    lines.extend(["", "## Failed Cases", ""])
    if not failed_rows:
        lines.append("No failed cases.")
    else:
        lines.extend(["| ID | Category | Mode | Problem | Answer Short |", "|---|---|---|---|---|"])
        for row in failed_rows:
            problems = []
            if row.get("missing_keywords"):
                problems.append("missing keywords: " + ", ".join(row["missing_keywords"]))
            if row.get("missing_source_keywords"):
                problems.append("missing sources: " + ", ".join(row["missing_source_keywords"]))
            if row["verdict"] == "ERROR":
                problems.append("error")
            answer = str(row.get("answer_short", "")).replace("|", "\\|")
            lines.append(f"| {row['id']} | {row.get('category')} | `{row.get('mode')}` | {'; '.join(problems)} | {answer} |")

    lines.extend(["", "## Files", "", f"- Results JSONL: `{result_path}`"])
    return "\n".join(lines) + "\n"


def evaluate(ground_truth_path: Path, label: str, limit: int | None = None) -> list[dict[str, Any]]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    result_path = REPORT_DIR / f"fast_ground_truth_results_{label}.jsonl"
    report_path = REPORT_DIR / f"fast_ground_truth_report_{label}.md"
    rows = load_jsonl(ground_truth_path)
    if limit:
        rows = rows[:limit]

    results: list[dict[str, Any]] = []
    with result_path.open("w", encoding="utf-8", newline="\n") as f:
        for index, item in enumerate(rows, 1):
            started = time.perf_counter()
            try:
                answer, hits, elapsed, mode = answer_question_fast(item["question"])
                wall_sec = round(time.perf_counter() - started, 4)
                keyword_ok, missing_keywords = keyword_status(answer, item.get("expected_keywords", []))
                source_ok, missing_sources = source_status(hits, item.get("expected_source_keywords", []))
                verdict = "PASS" if keyword_ok and source_ok else "FAIL"
                result = {
                    "id": item["id"],
                    "category": item.get("category"),
                    "answer_type": item.get("answer_type"),
                    "difficulty": item.get("difficulty"),
                    "variant_type": item.get("variant_type"),
                    "question": item["question"],
                    "expected_keywords": item.get("expected_keywords", []),
                    "expected_source_keywords": item.get("expected_source_keywords", []),
                    "mode": mode,
                    "verdict": verdict,
                    "keyword_ok": keyword_ok,
                    "source_ok": source_ok,
                    "missing_keywords": missing_keywords,
                    "missing_source_keywords": missing_sources,
                    "latency_sec": elapsed,
                    "wall_sec": wall_sec,
                    "retrieved_ids": [hit.get("id") for hit in hits],
                    "answer": answer,
                    "answer_short": short_answer(answer),
                }
            except Exception as exc:
                result = {
                    "id": item["id"],
                    "category": item.get("category"),
                    "answer_type": item.get("answer_type"),
                    "difficulty": item.get("difficulty"),
                    "variant_type": item.get("variant_type"),
                    "question": item["question"],
                    "expected_keywords": item.get("expected_keywords", []),
                    "expected_source_keywords": item.get("expected_source_keywords", []),
                    "mode": "error",
                    "verdict": "ERROR",
                    "keyword_ok": False,
                    "source_ok": False,
                    "missing_keywords": item.get("expected_keywords", []),
                    "missing_source_keywords": item.get("expected_source_keywords", []),
                    "latency_sec": None,
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "retrieved_ids": [],
                    "answer": repr(exc),
                    "answer_short": repr(exc),
                }
            print(f"[{index}/{len(rows)}] {result['id']} -> {result['verdict']} mode={result['mode']} latency={result['latency_sec']}", flush=True)
            results.append(result)
            f.write(json.dumps(result, ensure_ascii=False) + "\n")

    report_path.write_text(build_report(results, result_path), encoding="utf-8", newline="\n")
    print(report_path)
    print(result_path)
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground-truth", type=Path, default=DEFAULT_GROUND_TRUTH)
    parser.add_argument("--label", default=f"{RUN_DATE}_fast")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    safe_label = "".join(ch if ch.isalnum() or ch in {"_", "-"} else "_" for ch in args.label)
    evaluate(args.ground_truth, safe_label, args.limit)


if __name__ == "__main__":
    main()
