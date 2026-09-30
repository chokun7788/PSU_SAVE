from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
DATASET = ROOT / "data" / "eval" / "keyboard_input_anomaly_ground_truth_500_20260830.jsonl"

from app.core.runtime_input_quality_guard import (  # noqa: E402
    DEFAULT_LAYOUT_THRESHOLD,
    DEFAULT_REPEAT_THRESHOLD,
    RuntimeInputQualityGuard,
)


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def metrics(rows: list[dict], *, field: str, expected: str) -> dict[str, float | int]:
    tp = sum(bool(row[expected]) and bool(row[field]) for row in rows)
    fp = sum(not bool(row[expected]) and bool(row[field]) for row in rows)
    fn = sum(bool(row[expected]) and not bool(row[field]) for row in rows)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": round(precision, 6),
        "recall": round(recall, 6),
        "f1": round((2 * precision * recall / (precision + recall)) if precision + recall else 0.0, 6),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate the runtime input-quality guard corpus and thresholds.")
    parser.add_argument("--dataset", type=Path, default=DATASET)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "reports" / "keyboard_input_anomaly_eval" / "20260831_runtime_corpus_probe")
    parser.add_argument("--layout-threshold", type=float, default=DEFAULT_LAYOUT_THRESHOLD)
    parser.add_argument("--repeat-threshold", type=float, default=DEFAULT_REPEAT_THRESHOLD)
    args = parser.parse_args()

    guard = RuntimeInputQualityGuard.from_environment()
    guard.mode = "enforce"
    guard.layout_threshold = args.layout_threshold
    guard.repeat_threshold = args.repeat_threshold
    cases = read_jsonl(args.dataset)
    rows: list[dict] = []
    for case in cases:
        decision = guard.inspect(str(case["observed_input"]))
        rows.append({
            "id": case["id"],
            "split": case["split"],
            "anomaly_family": case["anomaly_family"],
            "observed_input": case["observed_input"],
            "expected_layout": bool(case["should_detect_keyboard_layout"]),
            "expected_repeat": bool(case["should_detect_repeated_character"]),
            "predicted_layout": "keyboard_layout_mismatch" in decision.flags,
            "predicted_repeat": "repeated_character_typo" in decision.flags,
            "layout_score": decision.features.layout_score,
            "repeat_score": decision.features.repeat_score,
            "action": decision.action,
            "would_short_circuit": decision.should_short_circuit,
        })

    test_rows = [row for row in rows if row["split"] == "test"]
    failures = [
        row for row in test_rows
        if row["expected_layout"] != row["predicted_layout"] or row["expected_repeat"] != row["predicted_repeat"]
    ]
    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "runtime_guard": guard.startup_status(),
        "dataset": str(args.dataset),
        "thresholds": {"layout": args.layout_threshold, "repeat": args.repeat_threshold},
        "test": {
            "layout": metrics(test_rows, field="predicted_layout", expected="expected_layout"),
            "repeat": metrics(test_rows, field="predicted_repeat", expected="expected_repeat"),
            "any_error_count": len(failures),
            "error_families": dict(Counter(row["anomaly_family"] for row in failures)),
        },
        "score_ranges": {
            "repeat_positive": [
                round(min(row["repeat_score"] for row in test_rows if row["expected_repeat"]), 6),
                round(max(row["repeat_score"] for row in test_rows if row["expected_repeat"]), 6),
            ],
            "repeat_negative": [
                round(min(row["repeat_score"] for row in test_rows if not row["expected_repeat"]), 6),
                round(max(row["repeat_score"] for row in test_rows if not row["expected_repeat"]), 6),
            ],
        },
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "results.jsonl").write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8"
    )
    (args.output_dir / "errors.jsonl").write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in failures) + ("\n" if failures else ""), encoding="utf-8"
    )
    (args.output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
