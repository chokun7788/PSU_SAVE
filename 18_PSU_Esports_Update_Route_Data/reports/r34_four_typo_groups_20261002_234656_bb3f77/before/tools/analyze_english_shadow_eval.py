from __future__ import annotations

"""Create an auditable analysis for a machine-translated English Shadow run.

This tool measures routing, language-safety, validation, and latency.  It does
not claim that machine translations or untranslated knowledge are ready for the
public chatbot; those still require the human-approval workflow.
"""

import argparse
import json
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


THAI_START = "\u0e00"
THAI_END = "\u0e7f"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def percentile(values: list[float], percentage: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil(len(ordered) * percentage / 100) - 1))
    return ordered[index]


def has_thai(text: str) -> bool:
    return any(THAI_START <= character <= THAI_END for character in str(text or ""))


def _rate(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 6) if denominator else None


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze an English Shadow translation and evaluation run.")
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    corpus = read_jsonl(args.corpus)
    results = read_jsonl(args.results)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    expected_by_id = {
        str(row.get("id") or ""): (
            row.get("expected_categories")
            if isinstance(row.get("expected_categories"), list)
            else [row.get("expected_category")] if row.get("expected_category") else []
        )
        for row in corpus
    }

    corpus_ids = [str(row.get("id") or "") for row in corpus]
    english_questions = [str(row.get("question_en") or "").strip() for row in corpus]
    duplicate_question_count = len(english_questions) - len(set(question.casefold() for question in english_questions if question))
    translation_statuses = Counter(str(row.get("translation_status") or "missing") for row in corpus)
    translation_methods = Counter(str(row.get("translation_method") or "missing") for row in corpus)
    category_expected = Counter(str(row.get("expected_category") or "unspecified") for row in corpus)
    language_leaks = [str(row.get("id")) for row in corpus if has_thai(str(row.get("question_en") or ""))]
    missing_questions = [str(row.get("id")) for row in corpus if not str(row.get("question_en") or "").strip()]

    failure_types: Counter[str] = Counter()
    route_confusion: Counter[str] = Counter()
    by_group: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "passed": 0, "blocked": 0})
    mode_counts: Counter[str] = Counter()
    response_language_counts: Counter[str] = Counter()
    latency = [float(row.get("latency_sec") or 0.0) for row in results]
    timeout_count = 0
    thai_answer_leaks = 0
    exceptions = 0
    strict_pass = 0
    localization_blocked = 0
    slowest: list[dict[str, Any]] = []

    for row in results:
        group = str(row.get("group") or "unspecified")
        by_group[group]["total"] += 1
        passed = bool(row.get("strict_pass"))
        strict_pass += int(passed)
        by_group[group]["passed"] += int(passed)
        blocked = bool(row.get("blockers"))
        localization_blocked += int(blocked)
        by_group[group]["blocked"] += int(blocked)
        mode_counts[str(row.get("mode") or "missing")] += 1
        language = row.get("language") or {}
        response_language_counts[str(language.get("effective") or "missing")] += 1
        thai_answer_leaks += int(has_thai(str(row.get("answer") or "")))
        timeout_count += int(float(row.get("latency_sec") or 0.0) >= 10.0)
        exceptions += int(str(row.get("mode") or "") == "exception")
        for failure in row.get("failures") or []:
            failure_types[str(failure).split(":", 1)[0]] += 1
        expected_values = expected_by_id.get(str(row.get("id") or ""), [])
        expected = "|".join(str(value) for value in expected_values)
        actual = str(row.get("route_category") or "")
        if expected_values and actual and actual not in expected_values:
            route_confusion[f"{expected} -> {actual}"] += 1
        slowest.append({
            "id": row.get("id"),
            "question": row.get("question"),
            "latency_sec": row.get("latency_sec"),
            "mode": row.get("mode"),
            "route_category": row.get("route_category"),
            "failures": row.get("failures") or [],
        })

    for value in by_group.values():
        value["pass_rate"] = _rate(value["passed"], value["total"])

    total = len(results)
    analysis = {
        "purpose": "Machine-translated English Shadow regression analysis. It measures pipeline behavior, not human-approved English quality.",
        "translation_audit": {
            "total_corpus_rows": len(corpus),
            "unique_ids": len(set(corpus_ids)),
            "duplicate_ids": len(corpus_ids) - len(set(corpus_ids)),
            "translation_statuses": dict(translation_statuses),
            "translation_methods": dict(translation_methods),
            "missing_question_en": len(missing_questions),
            "thai_script_in_question_en": len(language_leaks),
            "duplicate_english_questions": duplicate_question_count,
            "expected_categories": dict(category_expected),
        },
        "evaluation": {
            "total_cases": total,
            "strict_pass": strict_pass,
            "strict_pass_rate": _rate(strict_pass, total),
            "localization_blocked_cases": localization_blocked,
            "timeout_cases": timeout_count,
            "exception_cases": exceptions,
            "thai_prose_in_answers": thai_answer_leaks,
            "response_languages": dict(response_language_counts),
            "mode_counts": dict(mode_counts),
            "failure_types": dict(failure_types),
            "route_confusion_top_20": dict(route_confusion.most_common(20)),
            "by_group": dict(by_group),
            "latency_sec": {
                "mean": round(statistics.fmean(latency), 4) if latency else 0.0,
                "p50": round(percentile(latency, 50), 4),
                "p95": round(percentile(latency, 95), 4),
                "p99": round(percentile(latency, 99), 4),
                "max": round(max(latency), 4) if latency else 0.0,
            },
            "slowest_20": sorted(slowest, key=lambda item: float(item["latency_sec"] or 0.0), reverse=True)[:20],
        },
        "interpretation_limits": [
            "Every machine-translated question remains unreviewed test data and is not public chatbot knowledge.",
            "Shadow rows generally verify expected route, effective language, validation, and latency; they do not replace an English Gold answer-quality review.",
            "A localization_pending blocker is an intentional safety outcome when approved English content does not exist.",
        ],
    }
    (args.output_dir / "analysis.json").write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")

    latency_summary = analysis["evaluation"]["latency_sec"]
    lines = [
        "# English Shadow Evaluation Analysis",
        "",
        "> Scope: machine-translated, unreviewed test questions. This is a routing and safety regression result, not approved English knowledge quality.",
        "",
        "## Translation Audit",
        f"- Corpus: {len(corpus)} rows; duplicate IDs: {analysis['translation_audit']['duplicate_ids']}",
        f"- Translation status: `{json.dumps(dict(translation_statuses), ensure_ascii=False)}`",
        f"- Missing English questions: {len(missing_questions)}; Thai script leakage: {len(language_leaks)}; duplicate English prompts: {duplicate_question_count}",
        "",
        "## Pipeline Result",
        f"- Strict pass: {strict_pass}/{total} ({(_rate(strict_pass, total) or 0) * 100:.2f}%)",
        f"- Localization-pending blockers: {localization_blocked}; timeouts: {timeout_count}; exceptions: {exceptions}; Thai-answer leakage: {thai_answer_leaks}",
        f"- Latency: mean {latency_summary['mean']:.3f}s, P50 {latency_summary['p50']:.3f}s, P95 {latency_summary['p95']:.3f}s, P99 {latency_summary['p99']:.3f}s, max {latency_summary['max']:.3f}s",
        "",
        "## Leading Failure Types",
    ]
    lines.extend([f"- `{name}`: {count}" for name, count in failure_types.most_common(12)] or ["- None"])
    lines.extend(["", "## Interpretation", "- Do not promote these translations into the public localization registry without human review."])
    (args.output_dir / "analysis.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(analysis, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
