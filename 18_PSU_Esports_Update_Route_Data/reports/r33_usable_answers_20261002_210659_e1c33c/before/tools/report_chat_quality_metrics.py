from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOG_DIR = ROOT / "data" / "logs"


def _read_records(log_dir: Path, pattern: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(log_dir.glob(pattern)):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                records.append(value)
    return records


def _percentile(values: list[float], percentile: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, round((len(ordered) - 1) * percentile)))
    return ordered[index]


def summarize(
    records: list[dict[str, Any]],
    *,
    max_reject_rate: float,
    max_timeout_rate: float,
    max_p95_sec: float,
) -> dict[str, Any]:
    metrics_rows: list[dict[str, Any]] = []
    latencies: list[float] = []
    missing_metrics = 0
    for record in records:
        artifact = record.get("decision_artifact")
        metrics = artifact.get("production_metrics") if isinstance(artifact, dict) else None
        if not isinstance(metrics, dict):
            missing_metrics += 1
            continue
        metrics_rows.append(metrics)
        latency = record.get("wall_sec", record.get("latency_sec"))
        if isinstance(latency, (int, float)):
            latencies.append(float(latency))

    total = len(metrics_rows)
    outcomes = Counter(str(row.get("outcome") or "unknown") for row in metrics_rows)
    gate_statuses = Counter(str(row.get("quality_gate_status") or "unknown") for row in metrics_rows)
    review_reasons: Counter[str] = Counter()
    for row in metrics_rows:
        review_reasons.update(str(value) for value in row.get("shadow_review_reasons") or [] if value)

    reject_rate = gate_statuses.get("reject", 0) / total if total else 0.0
    timeout_rate = outcomes.get("timeout", 0) / total if total else 0.0
    p95_sec = _percentile(latencies, 0.95)
    gates = {
        "reject_rate": reject_rate <= max_reject_rate,
        "timeout_rate": timeout_rate <= max_timeout_rate,
        "p95_latency": p95_sec <= max_p95_sec,
        "metrics_present": total > 0,
    }
    return {
        "records_total": len(records),
        "records_with_metrics": total,
        "records_missing_metrics": missing_metrics,
        "outcomes": dict(outcomes),
        "quality_gate_statuses": dict(gate_statuses),
        "repair_attempted": sum(bool(row.get("repair_attempted")) for row in metrics_rows),
        "repair_recovered": sum(bool(row.get("repair_recovered")) for row in metrics_rows),
        "llm_call_total": sum(int(row.get("llm_call_count") or 0) for row in metrics_rows),
        "shadow_review_required": sum(bool(row.get("requires_shadow_review")) for row in metrics_rows),
        "shadow_review_reasons": dict(review_reasons),
        "latency": {
            "count": len(latencies),
            "avg_sec": round(statistics.fmean(latencies), 4) if latencies else 0.0,
            "p95_sec": round(p95_sec, 4),
            "max_sec": round(max(latencies), 4) if latencies else 0.0,
        },
        "thresholds": {
            "max_reject_rate": max_reject_rate,
            "max_timeout_rate": max_timeout_rate,
            "max_p95_sec": max_p95_sec,
        },
        "release_gates": gates,
        "release_gate_passed": all(gates.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize correctness-control metrics from PSU chatbot JSONL logs.")
    parser.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR))
    parser.add_argument("--pattern", default="web_chat_*.jsonl")
    parser.add_argument("--output", default="")
    parser.add_argument("--max-reject-rate", type=float, default=0.0)
    parser.add_argument("--max-timeout-rate", type=float, default=0.01)
    parser.add_argument("--max-p95-sec", type=float, default=8.0)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    summary = summarize(
        _read_records(Path(args.log_dir), args.pattern),
        max_reject_rate=max(0.0, args.max_reject_rate),
        max_timeout_rate=max(0.0, args.max_timeout_rate),
        max_p95_sec=max(0.0, args.max_p95_sec),
    )
    text = json.dumps(summary, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text + "\n", encoding="utf-8")
    return 2 if args.strict and not summary["release_gate_passed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
