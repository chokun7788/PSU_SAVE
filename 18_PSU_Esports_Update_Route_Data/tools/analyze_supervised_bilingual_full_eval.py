from __future__ import annotations

"""Analyze a completed run from run_supervised_bilingual_full_eval.py."""

import argparse
import json
import math
import statistics
from collections import Counter
from pathlib import Path
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def percentile(values: list[float], percentage: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    return round(ordered[max(0, min(len(ordered) - 1, math.ceil(len(ordered) * percentage / 100) - 1))], 4)


def shape(answer: str) -> dict[str, int]:
    lines = [line for line in str(answer or "").splitlines() if line.strip()]
    bullets = sum(line.lstrip().startswith(("- ", "* ", "•")) for line in lines)
    return {"lines": len(lines), "bullets": bullets}


def watchdog_escapes(rows: list[dict[str, Any]], watchdog_sec: float = 25.0) -> list[dict[str, Any]]:
    """Completed rows beyond the evaluator deadline are a harness-control defect.

    Raw results remain unchanged.  The analyzer separates these observations so
    their multi-minute durations cannot be mistaken for ordinary model latency.
    """
    return [
        row for row in rows
        if str(row.get("status")) == "completed"
        and float(row.get("wall_sec") or 0.0) > watchdog_sec
    ]


def suite_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    raw_latencies = [float(row.get("wall_sec") or 0.0) for row in rows]
    escapes = watchdog_escapes(rows)
    normal_latencies = [
        float(row.get("wall_sec") or 0.0)
        for row in rows
        if row not in escapes
    ]
    failures = Counter(error for row in rows for error in row.get("failures", []))
    confusion = Counter(
        f"{row.get('expected_category') or 'unspecified'} -> {row.get('route_category') or 'none'}"
        for row in rows
        if row.get("expected_category") and row.get("route_category")
        and str(row.get("expected_category")) != str(row.get("route_category"))
    )
    slowest = sorted(rows, key=lambda row: float(row.get("wall_sec") or 0.0), reverse=True)[:20]
    return {
        "total": len(rows),
        "strict_pass": sum(bool(row.get("strict_pass")) for row in rows),
        "strict_pass_rate": round(sum(bool(row.get("strict_pass")) for row in rows) / len(rows), 6) if rows else None,
        "status_counts": dict(Counter(str(row.get("status")) for row in rows)),
        "failure_types": dict(failures),
        "route_confusion_top_15": dict(confusion.most_common(15)),
        "mode_counts": dict(Counter(str(row.get("mode")) for row in rows)),
        "latency_sec": {
            "observed_mean_excluding_watchdog_escapes": round(statistics.fmean(normal_latencies), 4) if normal_latencies else 0.0,
            "observed_p50_excluding_watchdog_escapes": percentile(normal_latencies, 50),
            "observed_p95_excluding_watchdog_escapes": percentile(normal_latencies, 95),
            "observed_p99_excluding_watchdog_escapes": percentile(normal_latencies, 99),
            "observed_max_excluding_watchdog_escapes": round(max(normal_latencies), 4) if normal_latencies else 0.0,
            "observed_over_10s_excluding_watchdog_escapes": sum(value >= 10.0 for value in normal_latencies),
            "observed_over_20s_excluding_watchdog_escapes": sum(value >= 20.0 for value in normal_latencies),
            "raw_max_including_watchdog_escapes": round(max(raw_latencies), 4) if raw_latencies else 0.0,
        },
        "watchdog_escape_observed": len(escapes),
        "watchdog_escape_cases": [
            {
                "id": row.get("id"), "question": row.get("question"), "wall_sec": row.get("wall_sec"),
                "mode": row.get("mode"), "failures": row.get("failures"),
            }
            for row in escapes
        ],
        "slowest_20": [
            {
                "id": row.get("id"), "question": row.get("question"), "wall_sec": row.get("wall_sec"),
                "mode": row.get("mode"), "route": f"{row.get('route_category')}/{row.get('route_intent')}",
                "status": row.get("status"), "failures": row.get("failures"),
                "answer_preview": " ".join(str(row.get("answer") or "").split())[:260],
            }
            for row in slowest
        ],
    }


def parity(
    thai: list[dict[str, Any]],
    english: list[dict[str, Any]],
    english_source_ids: dict[str, str],
) -> dict[str, Any]:
    thai_by_id = {str(row.get("id")): row for row in thai}
    english_by_id = {
        english_source_ids.get(str(row.get("id")), str(row.get("id"))): row
        for row in english
    }
    shared = sorted(set(thai_by_id) & set(english_by_id))
    route_mismatch: list[dict[str, Any]] = []
    shape_gap: list[dict[str, Any]] = []
    pass_asymmetry: list[dict[str, Any]] = []
    for case_id in shared:
        th, en = thai_by_id[case_id], english_by_id[case_id]
        th_route = str(th.get("route_category") or "")
        en_route = str(en.get("route_category") or "")
        if th_route and en_route and th_route != en_route:
            route_mismatch.append({"id": case_id, "thai": th_route, "english": en_route, "question_en": en.get("question")})
        th_shape, en_shape = shape(str(th.get("answer") or "")), shape(str(en.get("answer") or ""))
        if (
            th.get("status") == en.get("status") == "completed"
            and abs(th_shape["bullets"] - en_shape["bullets"]) >= 3
        ):
            shape_gap.append({"id": case_id, "thai": th_shape, "english": en_shape, "question_en": en.get("question")})
        if bool(th.get("strict_pass")) != bool(en.get("strict_pass")):
            pass_asymmetry.append({
                "id": case_id, "thai_pass": bool(th.get("strict_pass")), "english_pass": bool(en.get("strict_pass")),
                "thai_failures": th.get("failures"), "english_failures": en.get("failures"), "question_en": en.get("question"),
            })
    return {
        "shared_ids": len(shared),
        "route_category_mismatches": len(route_mismatch),
        "large_bullet_shape_gaps": len(shape_gap),
        "pass_asymmetry": len(pass_asymmetry),
        "route_mismatch_examples": route_mismatch[:25],
        "shape_gap_examples": shape_gap[:25],
        "pass_asymmetry_examples": pass_asymmetry[:25],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    thai = read_jsonl(run_dir / "th_results.jsonl")
    english = read_jsonl(run_dir / "en_results.jsonl")
    english_corpus = next(run_dir.glob("english_shadow_1600_machine_*.jsonl"), None)
    english_source_ids: dict[str, str] = {}
    if english_corpus is not None:
        english_source_ids = {
            str(row.get("id")): str(row.get("source_case_id"))
            for row in read_jsonl(english_corpus)
            if row.get("id") and row.get("source_case_id")
        }
    result = {
        "thai": suite_summary(thai),
        "english": suite_summary(english),
        "parity": parity(thai, english, english_source_ids),
        "parity_mapping": {
            "method": "english source_case_id -> Thai benchmark id",
            "english_rows_with_source_case_id": len(english_source_ids),
        },
    }
    (run_dir / "analysis.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    th, en, pr = result["thai"], result["english"], result["parity"]
    thai_failures = [f"- `{name}`: {count}" for name, count in Counter(th["failure_types"]).most_common(12)]
    english_failures = [f"- `{name}`: {count}" for name, count in Counter(en["failure_types"]).most_common(12)]
    lines = [
        "# Supervised Thai-English 1,600 Evaluation Analysis", "",
        "> English is a machine-translated Shadow corpus. These results measure current pipeline behavior and contract compliance, not human-approved translation quality.", "",
        "## Summary", "",
        "| Suite | Strict pass | Observed P95 | Observed >=10s | Watchdog escape | Raw max | Harness timeout | Worker crash |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
        f"| Thai | {th['strict_pass']}/{th['total']} ({th['strict_pass_rate'] * 100:.2f}%) | {th['latency_sec']['observed_p95_excluding_watchdog_escapes']:.3f}s | {th['latency_sec']['observed_over_10s_excluding_watchdog_escapes']} | {th['watchdog_escape_observed']} | {th['latency_sec']['raw_max_including_watchdog_escapes']:.3f}s | {th['status_counts'].get('harness_timeout', 0)} | {th['status_counts'].get('worker_crash', 0)} |",
        f"| English | {en['strict_pass']}/{en['total']} ({en['strict_pass_rate'] * 100:.2f}%) | {en['latency_sec']['observed_p95_excluding_watchdog_escapes']:.3f}s | {en['latency_sec']['observed_over_10s_excluding_watchdog_escapes']} | {en['watchdog_escape_observed']} | {en['latency_sec']['raw_max_including_watchdog_escapes']:.3f}s | {en['status_counts'].get('harness_timeout', 0)} | {en['status_counts'].get('worker_crash', 0)} |",
        "", "## Thai-English Parity", "",
        f"- Shared case IDs: {pr['shared_ids']}",
        f"- Route category mismatches: {pr['route_category_mismatches']}",
        f"- Large bullet-format gaps: {pr['large_bullet_shape_gaps']}",
        f"- One language passed while the other failed: {pr['pass_asymmetry']}",
        "", "## Leading Failures", "",
        "### Thai", *(thai_failures or ["- None"]),
        "", "### English", *(english_failures or ["- None"]),
        "", "## Slowest Cases", "",
    ]
    for label, summary in (("Thai", th), ("English", en)):
        lines.extend([f"### {label}", ""])
        for row in summary["slowest_20"][:10]:
            lines.append(f"- `{row['id']}` {row['wall_sec']}s | `{row['mode']}` | {row['question']}")
    lines.extend([
        "", "## Watchdog-Control Observations", "",
        "- `watchdog_escape_observed` means a row returned as `completed` after exceeding the evaluator's 25-second limit. It is a runner/pipeline cancellation defect, not normal latency.",
        *[f"- Thai: `{row['id']}` {row['wall_sec']}s | `{row['mode']}`" for row in th["watchdog_escape_cases"]],
        *[f"- English: `{row['id']}` {row['wall_sec']}s | `{row['mode']}`" for row in en["watchdog_escape_cases"]],
        "", "## Limits", "", "- A watchdog timeout is a runner observation, not a response delivered to a user.", "- Direct Thai-English score comparison is limited because the English Shadow is machine-translated and has its own contract.",
    ])
    (run_dir / "analysis.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
