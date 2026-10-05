"""Summarize the current 1,600-case and keyboard-guard evaluation logs."""

from __future__ import annotations

import json
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "reports" / "model_benchmark" / "20260831_current_flow_full1600_llm" / "llm_scb10x_typhoon2.5-qwen3-4b"
KEYBOARD_DIR = ROOT / "reports" / "keyboard_input_pipeline_eval" / "20260831_current_flow_guard_llm500"
BASELINE_DIR = ROOT / "reports" / "model_benchmark" / "20260823_pipeline_fixes_full1600_final_v3" / "llm_scb10x_typhoon2.5-qwen3-4b"


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def percentile(values: list[float], percent: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    return ordered[max(0, min(len(ordered) - 1, math.ceil(len(ordered) * percent) - 1))]


def source_passed(row: dict) -> bool:
    return bool((row.get("judge") or {}).get("passed"))


def actual_calls(rows: list[dict]) -> Counter:
    return Counter(
        call.get("llm_kind")
        for row in rows
        for call in row.get("llm_calls", [])
        if not call.get("llm_skipped_by_health") and float(call.get("llm_elapsed_ms") or 0) > 0
    )


def main() -> None:
    current = read_jsonl(MODEL_DIR / "results.jsonl")
    baseline = {row["id"]: row for row in read_jsonl(BASELINE_DIR / "results.jsonl")}
    keyboard = read_jsonl(KEYBOARD_DIR / "results.jsonl")

    regressions = [
        (baseline[row["id"]], row)
        for row in current
        if source_passed(baseline[row["id"]]) and not source_passed(row)
    ]
    slow_current = sorted(current, key=lambda row: float(row.get("wall_sec") or 0), reverse=True)

    families: dict[str, dict] = defaultdict(lambda: {
        "total": 0, "blocked": 0, "pipeline": 0, "evaluated": 0, "passed": 0,
        "wall": [], "over_budget": 0, "llm_calls": 0,
    })
    keyboard_failures: list[dict] = []
    for row in keyboard:
        bucket = families[row["anomaly_family"]]
        bucket["total"] += 1
        bucket["blocked"] += int(bool(row["predicted_should_block"]))
        bucket["pipeline"] += int(bool(row["pipeline_executed"]))
        bucket["llm_calls"] += int(row["llm_call_count"])
        if row["pipeline_executed"]:
            bucket["wall"].append(float(row["wall_sec"]))
            bucket["over_budget"] += int(float(row["wall_sec"]) > 9)
        judge = row["source_judge"]
        if judge["applicable"]:
            bucket["evaluated"] += 1
            bucket["passed"] += int(bool(judge["passed"]))
            if not judge["passed"]:
                keyboard_failures.append(row)

    output = {
        "current_1600": {
            "total": len(current),
            "passed": sum(source_passed(row) for row in current),
            "regressions_from_baseline": len(regressions),
            "regression_groups": dict(Counter(row["group"] for _, row in regressions)),
            "regression_transitions": [
                {"baseline_mode": before, "current_mode": after, "count": count}
                for (before, after), count in Counter((old["mode"], new["mode"]) for old, new in regressions).most_common()
            ],
            "llm_calls_actual": dict(actual_calls(current)),
            "slowest_cases": [
                {
                    "id": row["id"], "group": row["group"], "wall_sec": row["wall_sec"],
                    "mode": row["mode"], "score": (row.get("judge") or {}).get("score"),
                }
                for row in slow_current[:15]
            ],
        },
        "keyboard_500": {
            "total": len(keyboard),
            "guard_action_accuracy_pct": round(
                sum(row["expected_action"] == row["predicted_action"] for row in keyboard) / len(keyboard) * 100, 2
            ),
            "guard_block_accuracy_pct": round(
                sum(bool(row["expected_should_block"]) == bool(row["predicted_should_block"]) for row in keyboard) / len(keyboard) * 100, 2
            ),
            "llm_calls_actual": dict(actual_calls(keyboard)),
            "families": {
                family: {
                    "total": data["total"],
                    "blocked": data["blocked"],
                    "pipeline_executed": data["pipeline"],
                    "source_contract": None if not data["evaluated"] else {
                        "evaluated": data["evaluated"],
                        "passed": data["passed"],
                        "pass_rate_pct": round(data["passed"] / data["evaluated"] * 100, 2),
                    },
                    "avg_wall_sec_pipeline": round(statistics.mean(data["wall"]), 4) if data["wall"] else 0.0,
                    "p95_wall_sec_pipeline": round(percentile(data["wall"], 0.95), 4),
                    "over_budget": data["over_budget"],
                    "llm_call_count": data["llm_calls"],
                }
                for family, data in sorted(families.items())
            },
            "failed_source_cases": [
                {
                    "id": row["id"], "family": row["anomaly_family"], "source_case_id": row["source_case_id"],
                    "input": row["observed_input"], "wall_sec": row["wall_sec"], "mode": row["mode"],
                    "score": row["source_judge"]["score"], "errors": row["source_judge"]["errors"],
                }
                for row in keyboard_failures
            ],
            "slowest_cases": [
                {
                    "id": row["id"], "family": row["anomaly_family"], "source_case_id": row["source_case_id"],
                    "wall_sec": row["wall_sec"], "mode": row["mode"],
                    "errors": row["source_judge"]["errors"],
                }
                for row in sorted(keyboard, key=lambda row: float(row["wall_sec"]), reverse=True)[:15]
            ],
        },
    }
    target = KEYBOARD_DIR / "analysis.json"
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(target)


if __name__ == "__main__":
    main()
