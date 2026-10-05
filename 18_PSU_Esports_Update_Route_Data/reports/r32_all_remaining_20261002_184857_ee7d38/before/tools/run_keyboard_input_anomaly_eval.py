from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.keyboard_input_anomaly import KeyboardInputAnomalyDetector  # noqa: E402


DEFAULT_DATASET = ROOT / "data" / "eval" / "keyboard_input_anomaly_ground_truth_500_20260830.jsonl"
DEFAULT_CORPUS = ROOT / "data" / "eval" / "model_benchmark_1500.jsonl"
DEFAULT_OUTPUT_DIR = ROOT / "reports" / "keyboard_input_anomaly_eval" / "20260830_ngram_baseline_v1"
DETECTOR_VERSION = "char_ngram_hidden_layout_hypothesis_v1"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSONL at {path}:{line_number}: {exc}") from exc
    return rows


def safe_divide(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def binary_metrics(expected: Iterable[bool], predicted: Iterable[bool]) -> dict[str, Any]:
    pairs = list(zip(expected, predicted))
    tp = sum(want and got for want, got in pairs)
    fp = sum(not want and got for want, got in pairs)
    tn = sum(not want and not got for want, got in pairs)
    fn = sum(want and not got for want, got in pairs)
    precision = safe_divide(tp, tp + fp)
    recall = safe_divide(tp, tp + fn)
    specificity = safe_divide(tn, tn + fp)
    f1 = safe_divide(2 * precision * recall, precision + recall)
    beta = 0.5
    f_beta = safe_divide((1 + beta * beta) * precision * recall, (beta * beta * precision) + recall)
    return {
        "total": len(pairs),
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "precision": round(precision, 6),
        "recall": round(recall, 6),
        "f1": round(f1, 6),
        "f0_5": round(f_beta, 6),
        "accuracy": round(safe_divide(tp + tn, len(pairs)), 6),
        "specificity": round(specificity, 6),
        "false_positive_rate": round(1 - specificity, 6),
    }


def tune_threshold(
    rows: list[dict[str, Any]],
    *,
    score_field: str,
    label_field: str,
    minimum_precision: float,
) -> dict[str, Any]:
    scores = sorted({float(row[score_field]) for row in rows})
    if not scores:
        raise ValueError(f"no scores for {score_field}")
    candidates = [scores[-1] + 0.000001, max(0.0, scores[0] - 0.000001)]
    candidates.extend(scores)
    candidates.extend((left + right) / 2 for left, right in zip(scores, scores[1:]))

    trials: list[dict[str, Any]] = []
    expected = [bool(row[label_field]) for row in rows]
    for threshold in sorted(set(candidates)):
        predicted = [float(row[score_field]) >= threshold for row in rows]
        metrics = binary_metrics(expected, predicted)
        trials.append({"threshold": round(threshold, 6), **metrics})

    eligible = [trial for trial in trials if trial["tp"] > 0 and trial["precision"] >= minimum_precision]
    if eligible:
        selected = max(
            eligible,
            key=lambda trial: (
                trial["recall"],
                trial["f0_5"],
                trial["precision"],
                -trial["false_positive_rate"],
                -trial["threshold"],
            ),
        )
        selection_reason = f"maximum calibration recall with precision >= {minimum_precision:.2f}"
    else:
        selected = max(
            trials,
            key=lambda trial: (trial["f0_5"], trial["precision"], trial["recall"], -trial["threshold"]),
        )
        selection_reason = "fallback to maximum calibration F0.5 because the precision floor was unreachable"
    return {
        "score_field": score_field,
        "label_field": label_field,
        "minimum_precision": minimum_precision,
        "selected_threshold": selected["threshold"],
        "selection_reason": selection_reason,
        "selected_calibration_metrics": selected,
        "candidate_count": len(trials),
    }


def evaluate_label(rows: list[dict[str, Any]], expected_field: str, predicted_field: str) -> dict[str, Any]:
    return binary_metrics(
        [bool(row[expected_field]) for row in rows],
        [bool(row[predicted_field]) for row in rows],
    )


def action_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    actions = ("request_retype", "soft_flag_typo", "continue")
    confusion: dict[str, dict[str, int]] = {
        expected: {predicted: 0 for predicted in actions}
        for expected in actions
    }
    for row in rows:
        expected = str(row["expected_action"])
        predicted = str(row["predicted_action"])
        confusion.setdefault(expected, {}).setdefault(predicted, 0)
        confusion[expected][predicted] += 1
    correct = sum(row["expected_action"] == row["predicted_action"] for row in rows)
    return {
        "total": len(rows),
        "correct": correct,
        "accuracy": round(safe_divide(correct, len(rows)), 6),
        "confusion": confusion,
    }


def exact_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    exact_flags = sum(bool(row["exact_flags_correct"]) for row in rows)
    block_correct = sum(bool(row["block_correct"]) for row in rows)
    return {
        "total": len(rows),
        "exact_flags_correct": exact_flags,
        "exact_flags_accuracy": round(safe_divide(exact_flags, len(rows)), 6),
        "block_correct": block_correct,
        "block_accuracy": round(safe_divide(block_correct, len(rows)), 6),
    }


def score_diagnostics(rows: list[dict[str, Any]], score_field: str, label_field: str) -> dict[str, Any]:
    positives = sorted(float(row[score_field]) for row in rows if bool(row[label_field]))
    negatives = sorted(float(row[score_field]) for row in rows if not bool(row[label_field]))

    def percentile(values: list[float], fraction: float) -> float:
        if not values:
            return 0.0
        index = max(0, min(len(values) - 1, round((len(values) - 1) * fraction)))
        return round(values[index], 6)

    positive_min = min(positives, default=0.0)
    negative_max = max(negatives, default=0.0)
    return {
        "positive_count": len(positives),
        "negative_count": len(negatives),
        "positive_min": round(positive_min, 6),
        "positive_p05": percentile(positives, 0.05),
        "positive_median": percentile(positives, 0.50),
        "negative_median": percentile(negatives, 0.50),
        "negative_p95": percentile(negatives, 0.95),
        "negative_max": round(negative_max, 6),
        "observed_separation_margin": round(positive_min - negative_max, 6),
    }


def hypothesis_diagnostics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    layout_rows = [row for row in rows if row["should_detect_keyboard_layout"]]
    repeat_rows = [row for row in rows if row["should_detect_repeated_character"]]

    def preview_metrics(items: list[dict[str, Any]], field: str) -> dict[str, Any]:
        exact = sum(row.get(field) == row.get("canonical_question") for row in items)
        present = sum(bool(row.get(field)) for row in items)
        return {
            "count": len(items),
            "preview_present": present,
            "preview_present_rate": round(safe_divide(present, len(items)), 6),
            "preview_exact_canonical": exact,
            "preview_exact_canonical_rate": round(safe_divide(exact, len(items)), 6),
        }

    direction_correct = sum(
        row.get("expected_layout_direction") == row.get("predicted_layout_direction")
        for row in layout_rows
    )
    return {
        "layout_direction": {
            "count": len(layout_rows),
            "correct": direction_correct,
            "accuracy": round(safe_divide(direction_correct, len(layout_rows)), 6),
            "confusion": {
                expected: dict(sorted(counter.items()))
                for expected, counter in sorted(
                    (
                        expected,
                        Counter(str(row.get("predicted_layout_direction")) for row in layout_rows if row.get("expected_layout_direction") == expected),
                    )
                    for expected in sorted({str(row.get("expected_layout_direction")) for row in layout_rows})
                )
            },
        },
        "layout_preview_all": preview_metrics(layout_rows, "layout_candidate_preview"),
        "layout_preview_layout_only": preview_metrics(
            [row for row in layout_rows if not row["should_detect_repeated_character"]],
            "layout_candidate_preview",
        ),
        "layout_preview_combined": preview_metrics(
            [row for row in layout_rows if row["should_detect_repeated_character"]],
            "layout_candidate_preview",
        ),
        "repeat_preview_all": preview_metrics(repeat_rows, "repeat_candidate_preview"),
        "repeat_preview_repeat_only": preview_metrics(
            [row for row in repeat_rows if not row["should_detect_keyboard_layout"]],
            "repeat_candidate_preview",
        ),
        "repeat_preview_combined": preview_metrics(
            [row for row in repeat_rows if row["should_detect_keyboard_layout"]],
            "repeat_candidate_preview",
        ),
    }


def grouped_metrics(rows: list[dict[str, Any]], key: str) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[str(row.get(key) or "unknown")].append(row)
    output: dict[str, Any] = {}
    for value, items in sorted(groups.items()):
        output[value] = {
            "count": len(items),
            "layout": evaluate_label(items, "should_detect_keyboard_layout", "predicted_keyboard_layout"),
            "repeat": evaluate_label(items, "should_detect_repeated_character", "predicted_repeated_character"),
            "action": action_metrics(items),
            "exact": exact_metrics(items),
        }
    return output


def split_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    no_flag_rows = [row for row in rows if not row["expected_flags"]]
    any_false_positive = sum(bool(row["predicted_flags"]) for row in no_flag_rows)
    return {
        "count": len(rows),
        "layout": evaluate_label(rows, "should_detect_keyboard_layout", "predicted_keyboard_layout"),
        "repeat": evaluate_label(rows, "should_detect_repeated_character", "predicted_repeated_character"),
        "action": action_metrics(rows),
        "exact": exact_metrics(rows),
        "no_flag_controls": {
            "count": len(no_flag_rows),
            "any_false_positive": any_false_positive,
            "any_false_positive_rate": round(safe_divide(any_false_positive, len(no_flag_rows)), 6),
        },
    }


def error_tags(row: dict[str, Any]) -> list[str]:
    tags: list[str] = []
    if row["predicted_keyboard_layout"] and not row["should_detect_keyboard_layout"]:
        tags.append("layout_false_positive")
    if not row["predicted_keyboard_layout"] and row["should_detect_keyboard_layout"]:
        tags.append("layout_false_negative")
    if row["predicted_repeated_character"] and not row["should_detect_repeated_character"]:
        tags.append("repeat_false_positive")
    if not row["predicted_repeated_character"] and row["should_detect_repeated_character"]:
        tags.append("repeat_false_negative")
    if row["predicted_action"] != row["expected_action"]:
        tags.append("action_mismatch")
    return tags


def run_detector(
    detector: KeyboardInputAnomalyDetector,
    cases: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, float]]:
    feature_rows: list[dict[str, Any]] = []
    elapsed_values: list[float] = []
    for case in cases:
        started = time.perf_counter()
        features = detector.analyze(str(case["observed_input"]))
        elapsed_ms = (time.perf_counter() - started) * 1000
        elapsed_values.append(elapsed_ms)
        feature_rows.append(
            {
                **case,
                "expected_layout_direction": case.get("layout_direction"),
                **{
                    **features.to_dict(),
                    "predicted_layout_direction": features.layout_direction,
                },
                "detector_elapsed_ms": round(elapsed_ms, 6),
            }
        )
        feature_rows[-1].pop("layout_direction", None)
    sorted_elapsed = sorted(elapsed_values)
    p95_index = max(0, min(len(sorted_elapsed) - 1, int(len(sorted_elapsed) * 0.95) - 1))
    latency = {
        "mean_ms": round(statistics.fmean(elapsed_values), 6) if elapsed_values else 0.0,
        "median_ms": round(statistics.median(elapsed_values), 6) if elapsed_values else 0.0,
        "p95_ms": round(sorted_elapsed[p95_index], 6) if sorted_elapsed else 0.0,
        "max_ms": round(max(elapsed_values), 6) if elapsed_values else 0.0,
        "total_ms": round(sum(elapsed_values), 6),
    }
    return feature_rows, latency


def apply_thresholds(
    detector: KeyboardInputAnomalyDetector,
    rows: list[dict[str, Any]],
    *,
    layout_threshold: float,
    repeat_threshold: float,
) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for row in rows:
        # classify only depends on the two locked scores; mapped previews remain diagnostic.
        class_input = type("ScoreCarrier", (), {
            "layout_score": row["layout_score"],
            "repeat_score": row["repeat_score"],
        })()
        decision = detector.classify(
            class_input,
            layout_threshold=layout_threshold,
            repeat_threshold=repeat_threshold,
        )
        result = {**row, **decision}
        result["layout_correct"] = result["predicted_keyboard_layout"] == bool(result["should_detect_keyboard_layout"])
        result["repeat_correct"] = result["predicted_repeated_character"] == bool(result["should_detect_repeated_character"])
        result["block_correct"] = result["predicted_should_block"] == bool(result["should_block_answer"])
        result["exact_flags_correct"] = set(result["predicted_flags"]) == set(result["expected_flags"])
        result["action_correct"] = result["predicted_action"] == result["expected_action"]
        result["error_tags"] = error_tags(result)
        output.append(result)
    return output


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "id", "split", "anomaly_family", "difficulty", "length_band",
        "observed_input", "canonical_question", "expected_flags", "predicted_flags",
        "should_detect_keyboard_layout", "predicted_keyboard_layout", "layout_score",
        "expected_layout_direction", "predicted_layout_direction", "layout_candidate_preview", "layout_reason", "layout_correct",
        "should_detect_repeated_character", "predicted_repeated_character", "repeat_score",
        "repeat_candidate_preview", "repeat_reason", "repeat_correct",
        "expected_action", "predicted_action", "action_correct", "block_correct",
        "exact_flags_correct", "error_tags", "detector_elapsed_ms",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            payload = {field: row.get(field, "") for field in fields}
            for field in ("expected_flags", "predicted_flags", "error_tags"):
                payload[field] = json.dumps(payload[field], ensure_ascii=False)
            writer.writerow(payload)


def markdown_report(summary: dict[str, Any], errors: list[dict[str, Any]]) -> str:
    test = summary["metrics"]["test"]
    layout = test["layout"]
    repeat = test["repeat"]
    action = test["action"]
    exact = test["exact"]
    diagnostics = summary["test_diagnostics"]
    family_errors = Counter(error["anomaly_family"] for error in errors)
    lines = [
        "# Keyboard Input Anomaly Detector Evaluation",
        "",
        f"Generated: {summary['generated_at']}",
        f"Detector: `{summary['detector_version']}`",
        f"Evaluation status: **{summary['evaluation_status']}**",
        "",
        "## Locked Thresholds",
        "",
        "| Detector | Threshold | Calibration policy |",
        "|---|---:|---|",
        f"| Keyboard layout | {summary['thresholds']['layout']['selected_threshold']:.6f} | {summary['thresholds']['layout']['selection_reason']} |",
        f"| Repeated character | {summary['thresholds']['repeat']['selected_threshold']:.6f} | {summary['thresholds']['repeat']['selection_reason']} |",
        "",
        "## Test Split (400 cases)",
        "",
        "| Metric | Layout | Repeat |",
        "|---|---:|---:|",
        f"| Precision | {layout['precision']:.2%} | {repeat['precision']:.2%} |",
        f"| Recall | {layout['recall']:.2%} | {repeat['recall']:.2%} |",
        f"| F1 | {layout['f1']:.2%} | {repeat['f1']:.2%} |",
        f"| False-positive rate | {layout['false_positive_rate']:.2%} | {repeat['false_positive_rate']:.2%} |",
        "",
        f"- Exact flag accuracy: {exact['exact_flags_accuracy']:.2%}",
        f"- Action accuracy: {action['accuracy']:.2%}",
        f"- No-flag control false-positive rate: {test['no_flag_controls']['any_false_positive_rate']:.2%}",
        f"- Mean detector latency: {summary['latency']['mean_ms']:.3f} ms per case",
        f"- Layout score separation margin: {diagnostics['layout_scores']['observed_separation_margin']:.6f}",
        f"- Repeat score separation margin: {diagnostics['repeat_scores']['observed_separation_margin']:.6f}",
        f"- Hidden layout preview exactly matched canonical text in {diagnostics['hypotheses']['layout_preview_all']['preview_exact_canonical_rate']:.2%} of layout-positive test cases.",
        "",
        "## Error Concentration",
        "",
    ]
    if family_errors:
        lines.extend(["| Family | Error cases |", "|---|---:|"])
        lines.extend(f"| `{family}` | {count} |" for family, count in family_errors.most_common())
    else:
        lines.append("No evaluation errors were found.")
    lines.extend(
        [
            "",
            "## Interpretation Guardrail",
            "",
            "Mapped candidates in the result files are hidden diagnostic hypotheses only. They must not replace user input or be sent to Fast/Structured, RAG, or LLM answer routes automatically.",
            "",
        "The dataset is mostly synthetic. These scores are baseline engineering evidence, not a production accuracy claim. Real anonymized user typo logs still require human labeling and a separate holdout evaluation.",
        "",
        "Feature rules were revised after earlier test errors were inspected during this implementation run. The final 400-case result is therefore a regression result, not an untouched independent holdout.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate keyboard-layout and repeated-character anomaly detection.")
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--layout-min-precision", type=float, default=0.97)
    parser.add_argument("--repeat-min-precision", type=float, default=0.95)
    args = parser.parse_args()

    cases = load_jsonl(args.dataset)
    corpus_rows = load_jsonl(args.corpus)
    clean_questions = [str(row.get("question") or "") for row in corpus_rows if row.get("question")]
    if Counter(str(row.get("split")) for row in cases) != {"calibration": 100, "test": 400}:
        raise ValueError("expected exactly calibration=100 and test=400")

    detector = KeyboardInputAnomalyDetector().fit(clean_questions)
    feature_rows, latency = run_detector(detector, cases)
    calibration_features = [row for row in feature_rows if row["split"] == "calibration"]

    layout_tuning = tune_threshold(
        calibration_features,
        score_field="layout_score",
        label_field="should_detect_keyboard_layout",
        minimum_precision=args.layout_min_precision,
    )
    repeat_tuning = tune_threshold(
        calibration_features,
        score_field="repeat_score",
        label_field="should_detect_repeated_character",
        minimum_precision=args.repeat_min_precision,
    )
    layout_threshold = float(layout_tuning["selected_threshold"])
    repeat_threshold = float(repeat_tuning["selected_threshold"])
    results = apply_thresholds(
        detector,
        feature_rows,
        layout_threshold=layout_threshold,
        repeat_threshold=repeat_threshold,
    )

    calibration_rows = [row for row in results if row["split"] == "calibration"]
    test_rows = [row for row in results if row["split"] == "test"]
    errors = [row for row in results if row["error_tags"]]
    test_errors = [row for row in test_rows if row["error_tags"]]

    summary = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "detector_version": DETECTOR_VERSION,
        "evaluation_status": "regression benchmark; not an untouched independent holdout",
        "independent_holdout": False,
        "dataset": str(args.dataset.relative_to(ROOT)),
        "clean_training_corpus": str(args.corpus.relative_to(ROOT)),
        "clean_training_question_count": len(clean_questions),
        "dataset_counts": dict(Counter(str(row["split"]) for row in cases)),
        "thresholds": {"layout": layout_tuning, "repeat": repeat_tuning},
        "metrics": {
            "calibration": split_metrics(calibration_rows),
            "test": split_metrics(test_rows),
            "overall_diagnostic_only": split_metrics(results),
        },
        "test_diagnostics": {
            "layout_scores": score_diagnostics(
                test_rows,
                "layout_score",
                "should_detect_keyboard_layout",
            ),
            "repeat_scores": score_diagnostics(
                test_rows,
                "repeat_score",
                "should_detect_repeated_character",
            ),
            "hypotheses": hypothesis_diagnostics(test_rows),
        },
        "test_metrics_by_family": grouped_metrics(test_rows, "anomaly_family"),
        "test_metrics_by_length_band": grouped_metrics(test_rows, "length_band"),
        "test_metrics_by_difficulty": grouped_metrics(test_rows, "difficulty"),
        "error_counts": {
            "overall_cases_with_any_error": len(errors),
            "test_cases_with_any_error": len(test_errors),
            "test_error_tags": dict(sorted(Counter(tag for row in test_errors for tag in row["error_tags"]).items())),
            "test_error_families": dict(sorted(Counter(row["anomaly_family"] for row in test_errors).items())),
        },
        "latency": latency,
        "methodology": {
            "threshold_selection": "calibration split only; test labels are evaluated after thresholds are locked",
            "feature_iteration_disclosure": "feature rules were revised after inspecting earlier errors from the test split during this implementation turn",
            "layout_method": "Thai/English character n-gram plausibility over hidden keyboard-layout hypotheses with protected-span guards",
            "repeat_method": "adjacent-run candidates scored by corpus/lexicon evidence with expressive, punctuation, ID and lexical-double guards",
            "runtime_integration": False,
            "automatic_correction": False,
        },
        "limitations": [
            "The 500-case benchmark is mostly synthetic and does not estimate live user error prevalence.",
            "The test split was inspected during feature debugging, so the final score is regression evidence rather than an independent holdout estimate.",
            "The detector is trained on clean project benchmark questions, so evaluation reflects this domain.",
            "Thai Kedmanee is covered; Pattachote, mobile swipe typing and voice transcription are not covered.",
        ],
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    result_path = args.output_dir / "results.jsonl"
    csv_path = args.output_dir / "results.csv"
    error_path = args.output_dir / "errors.jsonl"
    calibration_error_path = args.output_dir / "calibration_errors.jsonl"
    test_error_path = args.output_dir / "test_errors.jsonl"
    summary_path = args.output_dir / "summary.json"
    report_path = args.output_dir / "report.md"
    write_jsonl(result_path, results)
    write_csv(csv_path, results)
    write_jsonl(error_path, errors)
    write_jsonl(calibration_error_path, [row for row in calibration_rows if row["error_tags"]])
    write_jsonl(test_error_path, test_errors)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report_path.write_text(markdown_report(summary, test_errors), encoding="utf-8")

    test = summary["metrics"]["test"]
    print(f"detector={DETECTOR_VERSION}")
    print(f"thresholds layout={layout_threshold:.6f} repeat={repeat_threshold:.6f}")
    print(
        "test layout "
        f"precision={test['layout']['precision']:.4f} recall={test['layout']['recall']:.4f} f1={test['layout']['f1']:.4f}"
    )
    print(
        "test repeat "
        f"precision={test['repeat']['precision']:.4f} recall={test['repeat']['recall']:.4f} f1={test['repeat']['f1']:.4f}"
    )
    print(f"test action_accuracy={test['action']['accuracy']:.4f} exact_flags={test['exact']['exact_flags_accuracy']:.4f}")
    print(f"test errors={len(test_errors)} mean_latency_ms={latency['mean_ms']:.4f}")
    print(f"output={args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
