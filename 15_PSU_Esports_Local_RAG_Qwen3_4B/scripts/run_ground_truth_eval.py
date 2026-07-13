from __future__ import annotations

import argparse
import json
import os
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


PROJECT_DIR = Path(__file__).resolve().parents[1]
REPORT_DIR = PROJECT_DIR.parent / "16_PSU_Esports_RAG_Experiment_Timeline"
RUN_DATE = date.today().isoformat()
GROUND_TRUTH_PATH = PROJECT_DIR / "ground_truth" / "ground_truth_full.jsonl"
NOTEBOOK_PATH = PROJECT_DIR / "notebooks" / "01_local_rag_qwen3_4b.ipynb"
RESULT_JSONL_PATH = REPORT_DIR / f"ground_truth_eval_results_{RUN_DATE}.jsonl"
REPORT_PATH = REPORT_DIR / f"ground_truth_eval_{RUN_DATE}.md"
CHAT_LOG_PATH = REPORT_DIR / f"ground_truth_chat_log_{RUN_DATE}.jsonl"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def load_notebook_namespace() -> dict[str, Any]:
    os.chdir(PROJECT_DIR)
    nb = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    ns: dict[str, Any] = {}
    # Config, load records, Chroma, retriever, and answer functions.
    for idx in [4, 7, 11, 12, 14, 16]:
        exec("".join(nb["cells"][idx]["source"]), ns)
    ns["LOG_PATH"] = CHAT_LOG_PATH
    return ns


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
    for h in hits:
        source_url = str(h.get("metadata", {}).get("source_url", "")).lower()
        if "esports.computing.psu.ac.th" in source_url:
            source_aliases.append("Reservation")
        category = str(h.get("metadata", {}).get("category", "")).lower()
        source_id = str(h.get("id", "")).lower()
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
        if "/gallery" in source_url:
            source_aliases.append("Gallery")
    haystack = " ".join(
        [
            str(h.get("id", "")) + " "
            + str(h.get("metadata", {}).get("title", "")) + " "
            + str(h.get("metadata", {}).get("category", "")) + " "
            + str(h.get("metadata", {}).get("source_url", "")) + " "
            + str(h.get("metadata", {}).get("source_ids", ""))
            for h in hits
        ]
        + source_aliases
    ).lower()
    missing = [kw for kw in expected_source_keywords if kw.lower() not in haystack]
    return not missing, missing


def short_answer(answer: str, limit: int = 220) -> str:
    text = " ".join((answer or "").split())
    return text if len(text) <= limit else text[:limit].rstrip() + "..."


def read_last_chat_log() -> dict[str, Any]:
    if not CHAT_LOG_PATH.exists():
        return {}
    lines = [line for line in CHAT_LOG_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        return {}
    return json.loads(lines[-1])


def evaluate(limit: int | None = None) -> list[dict[str, Any]]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    if RESULT_JSONL_PATH.exists():
        RESULT_JSONL_PATH.unlink()
    if CHAT_LOG_PATH.exists():
        CHAT_LOG_PATH.unlink()

    ns = load_notebook_namespace()
    answer_question = ns["answer_question"]
    rows = load_jsonl(GROUND_TRUTH_PATH)
    if limit:
        rows = rows[:limit]

    results: list[dict[str, Any]] = []
    with RESULT_JSONL_PATH.open("w", encoding="utf-8") as f:
        for index, item in enumerate(rows, 1):
            print(f"[{index}/{len(rows)}] {item['id']} | {item['question']}", flush=True)
            start = time.time()
            try:
                answer, hits, elapsed = answer_question(item["question"])
                wall_sec = round(time.time() - start, 3)
                log_row = read_last_chat_log()
                mode = log_row.get("mode", "unknown")
                keyword_ok, missing_keywords = keyword_status(answer, item.get("expected_keywords", []))
                source_ok, missing_sources = source_status(hits, item.get("expected_source_keywords", []))
                verdict = "PASS" if keyword_ok and source_ok else "FAIL"
                result = {
                    "id": item["id"],
                    "category": item.get("category"),
                    "answer_type": item.get("answer_type"),
                    "difficulty": item.get("difficulty"),
                    "question": item["question"],
                    "mode": mode,
                    "verdict": verdict,
                    "keyword_ok": keyword_ok,
                    "source_ok": source_ok,
                    "missing_keywords": missing_keywords,
                    "missing_source_keywords": missing_sources,
                    "latency_sec": elapsed,
                    "wall_sec": wall_sec,
                    "retrieved_ids": [h.get("id") for h in hits],
                    "answer": answer,
                    "answer_short": short_answer(answer),
                }
            except Exception as exc:
                result = {
                    "id": item["id"],
                    "category": item.get("category"),
                    "answer_type": item.get("answer_type"),
                    "difficulty": item.get("difficulty"),
                    "question": item["question"],
                    "mode": "error",
                    "verdict": "ERROR",
                    "keyword_ok": False,
                    "source_ok": False,
                    "missing_keywords": item.get("expected_keywords", []),
                    "missing_source_keywords": item.get("expected_source_keywords", []),
                    "latency_sec": None,
                    "wall_sec": round(time.time() - start, 3),
                    "retrieved_ids": [],
                    "answer": repr(exc),
                    "answer_short": repr(exc),
                }
            print(f"  -> {result['verdict']} mode={result['mode']} latency={result['latency_sec']}", flush=True)
            results.append(result)
            f.write(json.dumps(result, ensure_ascii=False) + "\n")

    REPORT_PATH.write_text(build_report(results), encoding="utf-8")
    print(REPORT_PATH)
    print(RESULT_JSONL_PATH)
    return results


def group_summary(results: list[dict[str, Any]], key: str) -> list[tuple[str, int, int, float]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in results:
        grouped[str(row.get(key, "-"))].append(row)
    summary = []
    for name, rows in grouped.items():
        total = len(rows)
        passed = sum(1 for r in rows if r["verdict"] == "PASS")
        summary.append((name, passed, total, passed / total * 100 if total else 0.0))
    return sorted(summary, key=lambda x: (-x[3], x[0]))


def build_report(results: list[dict[str, Any]]) -> str:
    total = len(results)
    passed = sum(1 for r in results if r["verdict"] == "PASS")
    failed = sum(1 for r in results if r["verdict"] == "FAIL")
    errors = sum(1 for r in results if r["verdict"] == "ERROR")
    pass_rate = passed / total * 100 if total else 0.0
    latencies = [float(r["latency_sec"]) for r in results if isinstance(r.get("latency_sec"), (int, float))]
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
    mode_counts = Counter(str(r.get("mode", "unknown")) for r in results)
    answer_type_counts = Counter(str(r.get("answer_type", "-")) for r in results)

    keyword_fail = sum(1 for r in results if not r.get("keyword_ok"))
    source_fail = sum(1 for r in results if not r.get("source_ok"))
    not_found_count = sum(1 for r in results if "ไม่พบข้อมูล" in str(r.get("answer", "")))
    chinese_leak_count = sum(1 for r in results if any("\u4e00" <= ch <= "\u9fff" for ch in str(r.get("answer", ""))))

    lines = [
        "# Ground Truth Evaluation - PSU Esports Local RAG",
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
        f"- Average latency: {avg_latency:.3f}s",
        f"- Keyword fail: {keyword_fail}",
        f"- Source fail: {source_fail}",
        f"- Answers containing `ไม่พบข้อมูล`: {not_found_count}",
        f"- Chinese character leakage: {chinese_leak_count}",
        "",
        "## Mode Distribution",
        "",
    ]

    for mode, count in mode_counts.most_common():
        lines.append(f"- `{mode}`: {count}")

    lines.extend(["", "## Answer Type Distribution", ""])
    for answer_type, count in answer_type_counts.most_common():
        lines.append(f"- `{answer_type}`: {count}")

    for key, title in [
        ("category", "By Category"),
        ("answer_type", "By Answer Type"),
        ("difficulty", "By Difficulty"),
        ("mode", "By Mode"),
    ]:
        lines.extend(["", f"## {title}", "", "| Group | PASS | Total | Pass rate |", "|---|---:|---:|---:|"])
        for name, p, t, rate in group_summary(results, key):
            lines.append(f"| {name} | {p} | {t} | {rate:.2f}% |")

    failed_rows = [r for r in results if r["verdict"] != "PASS"]
    lines.extend(["", "## Failed Cases", ""])
    if not failed_rows:
        lines.append("No failed cases.")
    else:
        lines.extend(["| ID | Category | Mode | Problem | Retrieved IDs | Answer Short |", "|---|---|---|---|---|---|"])
        for row in failed_rows:
            problems = []
            if row.get("missing_keywords"):
                problems.append("missing keywords: " + ", ".join(row["missing_keywords"]))
            if row.get("missing_source_keywords"):
                problems.append("missing sources: " + ", ".join(row["missing_source_keywords"]))
            if row["verdict"] == "ERROR":
                problems.append("error")
            retrieved = ", ".join(str(x) for x in row.get("retrieved_ids", []))
            answer = str(row.get("answer_short", "")).replace("|", "\\|")
            lines.append(
                f"| {row['id']} | {row.get('category')} | `{row.get('mode')}` | "
                f"{'; '.join(problems)} | {retrieved} | {answer} |"
            )

    lines.extend(["", "## Answer Characteristics", ""])
    lines.append("- `rule_fast_path` คือคำตอบ FAQ ที่เร็วและนิ่งที่สุด")
    lines.append("- `rag_direct_curated` คือคำตอบจาก curated facts ที่ไม่ต้องเรียก LLM จึงเร็วและลด hallucination")
    lines.append("- `rag_llm` คือคำตอบที่ต้องให้โมเดลสรุปจาก context จึงช้ากว่าและเสี่ยง keyword หายมากกว่า")
    lines.append("- การวัดนี้เป็น keyword/source match แบบเข้ม ถ้าคำตอบถูกความหมายแต่ใช้คำคนละรูป อาจถูกนับเป็น FAIL ได้")
    lines.append("")
    lines.append("## Files")
    lines.append("")
    lines.append(f"- Results JSONL: `{RESULT_JSONL_PATH}`")
    lines.append(f"- Chat log JSONL: `{CHAT_LOG_PATH}`")

    return "\n".join(lines) + "\n"


def main() -> None:
    global GROUND_TRUTH_PATH, RESULT_JSONL_PATH, REPORT_PATH, CHAT_LOG_PATH

    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--ground-truth", type=Path, default=GROUND_TRUTH_PATH)
    parser.add_argument("--label", type=str, default=None)
    args = parser.parse_args()

    GROUND_TRUTH_PATH = args.ground_truth
    if args.label:
        safe_label = "".join(ch if ch.isalnum() or ch in {"_", "-"} else "_" for ch in args.label)
        RESULT_JSONL_PATH = REPORT_DIR / f"ground_truth_eval_results_{safe_label}.jsonl"
        REPORT_PATH = REPORT_DIR / f"ground_truth_eval_{safe_label}.md"
        CHAT_LOG_PATH = REPORT_DIR / f"ground_truth_chat_log_{safe_label}.jsonl"

    evaluate(limit=args.limit)


if __name__ == "__main__":
    main()
