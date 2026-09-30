from __future__ import annotations

import argparse
import csv
import json
import os
import statistics
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.keyboard_input_anomaly import KeyboardInputAnomalyDetector
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.llm_health import preflight_ollama
from app.pipeline.warmup import warm_pipeline_caches


DEFAULT_DATASET = ROOT / "data" / "eval" / "keyboard_input_anomaly_ground_truth_500_20260830.jsonl"
DEFAULT_CORPUS = ROOT / "data" / "eval" / "model_benchmark_1500.jsonl"
DEFAULT_OUTPUT_ROOT = ROOT / "reports" / "keyboard_input_pipeline_eval"


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(item) for item in value if str(item)]
    return [str(value)]


def _plain(value: Any) -> Any:
    if hasattr(value, "__dataclass_fields__"):
        return {key: _plain(getattr(value, key)) for key in value.__dataclass_fields__}
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _llm_calls(result: Any) -> list[dict[str, Any]]:
    artifact = _plain(getattr(result, "decision_artifact", None))
    if isinstance(artifact, dict):
        calls = artifact.get("llm_calls")
        if isinstance(calls, list):
            return [dict(call) for call in calls if isinstance(call, dict) and call]
    return []


def _stage_timings(result: Any) -> list[dict[str, Any]]:
    timings: list[dict[str, Any]] = []
    for item in getattr(result, "trace", []):
        if getattr(item, "stage", "") != "timing":
            continue
        metadata = _plain(getattr(item, "metadata", {}))
        timings.append({
            "process": getattr(item, "decision", ""),
            "elapsed_ms": float(metadata.get("elapsed_ms") or 0.0),
            "elapsed_sec": float(metadata.get("elapsed_sec") or 0.0),
        })
    return timings


def _judge_against_source(source: dict[str, Any] | None, result: Any, wall_sec: float, timeout_sec: float) -> dict[str, Any]:
    if not source:
        return {"applicable": False, "passed": None, "score": None, "errors": ["source_case_unavailable"]}

    answer = str(result.answer or "")
    mode = str(result.mode or "")
    category = str(result.route.category or "")
    errors: list[str] = []
    expected_categories = _as_list(source.get("expected_category"))
    if expected_categories and category not in expected_categories:
        errors.append(f"category_mismatch:{category}")
    expected_modes = _as_list(source.get("expected_mode_prefix"))
    if expected_modes and not any(mode.startswith(prefix) for prefix in expected_modes):
        errors.append(f"mode_mismatch:{mode}")
    for term in _as_list(source.get("must_contain")):
        if term.lower() not in answer.lower():
            errors.append(f"missing:{term}")
    must_contain_any = _as_list(source.get("must_contain_any"))
    if must_contain_any and not any(term.lower() in answer.lower() for term in must_contain_any):
        errors.append("missing_any")
    for term in _as_list(source.get("must_not_contain")):
        if term.lower() in answer.lower():
            errors.append(f"forbidden:{term}")
    if bool(source.get("llm_required")) and not _llm_calls(result):
        errors.append("llm_required")
    if not bool(result.validation.ok):
        errors.append("validation_failed")
    if wall_sec > timeout_sec:
        errors.append("timeout_budget_exceeded")

    score = 100.0
    score -= 18.0 * sum(item.startswith("category_mismatch") for item in errors)
    score -= 12.0 * sum(item.startswith("mode_mismatch") for item in errors)
    score -= 12.0 * sum(item.startswith("missing:") for item in errors)
    score -= 16.0 * sum(item == "missing_any" for item in errors)
    score -= 20.0 * sum(item.startswith("forbidden:") for item in errors)
    score -= 25.0 * sum(item == "llm_required" for item in errors)
    score -= 10.0 * sum(item == "timeout_budget_exceeded" for item in errors)
    return {"applicable": True, "passed": not errors, "score": max(0.0, round(score, 2)), "errors": errors}


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round((pct / 100.0) * (len(ordered) - 1))))
    return round(ordered[index], 4)


def _configure_environment(args: argparse.Namespace) -> None:
    os.environ["PYTHONIOENCODING"] = "utf-8"
    os.environ["PSU_LLM_PREFLIGHT"] = "0"
    os.environ["PSU_OLLAMA_THINK"] = "false"
    os.environ["PSU_CHATBOT_OLLAMA_MODEL"] = args.model
    os.environ["PSU_INTENT_LLM_MODEL"] = args.model
    os.environ["PSU_TOOL_ROUTER_MODEL"] = args.model
    os.environ["PSU_FACTS_LLM_MODEL"] = args.model
    os.environ["PSU_GENERAL_LLM_TIMEOUT_SEC"] = str(args.timeout_sec)
    os.environ["PSU_PIPELINE_GLOBAL_TIMEOUT_SEC"] = str(args.timeout_sec)
    os.environ["PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC"] = str(args.timeout_sec)
    os.environ["PSU_FACTS_LLM_TIMEOUT_SEC"] = str(min(args.timeout_sec, args.facts_timeout_sec))
    os.environ["PSU_INTENT_LLM_TIMEOUT_SEC"] = str(min(args.timeout_sec, 8.0))
    os.environ["PSU_TOOL_ROUTER_TIMEOUT_SEC"] = str(min(args.timeout_sec, 1.2))
    os.environ["PSU_GENERAL_LLM_NUM_PREDICT"] = str(args.num_predict)
    os.environ["PSU_RAG_LLM_NUM_PREDICT"] = str(args.num_predict)
    os.environ["PSU_FACTS_LLM_NUM_PREDICT"] = str(max(args.num_predict, args.facts_num_predict))
    os.environ["PSU_GENERAL_LLM_NUM_CTX"] = str(args.num_ctx)
    os.environ["PSU_FACTS_LLM_NUM_CTX"] = str(args.facts_num_ctx)
    os.environ["PSU_INTENT_LLM_NUM_CTX"] = str(min(args.num_ctx, 2048))
    os.environ["PSU_TOOL_ROUTER_NUM_CTX"] = str(min(args.num_ctx, 2048))
    os.environ["PSU_QUERY_PLANNER_NUM_CTX"] = str(min(args.num_ctx, 2048))
    os.environ["PSU_LLM_TOOL_ROUTER"] = "1" if args.tool_router else "0"
    os.environ["PSU_FACTS_LLM_COMPOSER"] = "1" if args.facts_composer else "0"
    os.environ["PSU_RAG_LLM_COMPOSER"] = "1" if args.facts_composer else "0"
    os.environ["PSU_MODEL_FIRST_FLOW"] = "1"
    os.environ["PSU_MODEL_FIRST_MIN_REMAINING_SEC"] = str(args.model_first_min_remaining_sec)
    os.environ["PSU_SEMANTIC_RETRIEVAL"] = "1"
    os.environ["PSU_EMBEDDING_MODEL"] = args.embedding_model
    os.environ["PSU_EMBEDDING_NUM_CTX"] = str(args.embedding_num_ctx)
    os.environ["OLLAMA_URL"] = args.ollama_url.rstrip("/")


def _summarize(rows: list[dict[str, Any]], meta: dict[str, Any]) -> dict[str, Any]:
    wall_values = [float(row.get("wall_sec") or 0.0) for row in rows]
    pipeline_rows = [row for row in rows if row.get("pipeline_executed")]
    pipeline_wall_values = [float(row.get("wall_sec") or 0.0) for row in pipeline_rows]
    source_rows = [row for row in pipeline_rows if row.get("source_judge", {}).get("applicable")]
    action_correct = sum(row.get("predicted_action") == row.get("expected_action") for row in rows)
    block_correct = sum(bool(row.get("predicted_should_block")) == bool(row.get("expected_should_block")) for row in rows)
    source_passed = sum(bool(row.get("source_judge", {}).get("passed")) for row in source_rows)
    timeout_rows = [
        row for row in pipeline_rows
        if float(row.get("wall_sec") or 0.0) > float(meta["timeout_sec"])
        or "timeout" in str(row.get("mode") or "").lower()
    ]
    return {
        **meta,
        "total": len(rows),
        "guard_action_accuracy_pct": round(action_correct / max(1, len(rows)) * 100, 2),
        "guard_block_accuracy_pct": round(block_correct / max(1, len(rows)) * 100, 2),
        "pipeline_executed": len(pipeline_rows),
        "guard_blocked": len(rows) - len(pipeline_rows),
        "source_contract_evaluated": len(source_rows),
        "source_contract_passed": source_passed,
        "source_contract_pass_rate_pct": round(source_passed / max(1, len(source_rows)) * 100, 2),
        "timeout_or_over_budget_count": len(timeout_rows),
        "llm_call_total": sum(int(row.get("llm_call_count") or 0) for row in rows),
        "llm_pipeline_case_count": sum(int(row.get("llm_call_count") or 0) > 0 for row in rows),
        "avg_wall_sec_all": round(statistics.mean(wall_values), 4) if wall_values else 0.0,
        "p95_wall_sec_all": _percentile(wall_values, 95),
        "max_wall_sec_all": max(wall_values, default=0.0),
        "avg_wall_sec_pipeline": round(statistics.mean(pipeline_wall_values), 4) if pipeline_wall_values else 0.0,
        "p95_wall_sec_pipeline": _percentile(pipeline_wall_values, 95),
        "max_wall_sec_pipeline": max(pipeline_wall_values, default=0.0),
        "mode_counts": dict(Counter(str(row.get("mode") or "") for row in pipeline_rows)),
        "family_counts": dict(Counter(str(row.get("anomaly_family") or "") for row in rows)),
        "guard_error_counts": dict(Counter(
            "action_mismatch" for row in rows if row.get("predicted_action") != row.get("expected_action")
        )),
        "source_error_counts": dict(Counter(
            error for row in source_rows for error in row.get("source_judge", {}).get("errors", [])
        )),
    }


def _write_outputs(output_dir: Path, rows: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_jsonl(output_dir / "results.jsonl", rows)
    (output_dir / "results.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    fields = [
        "id", "split", "anomaly_family", "observed_input", "canonical_question", "expected_action",
        "predicted_action", "expected_should_block", "predicted_should_block", "pipeline_executed",
        "mode", "route", "wall_sec", "llm_call_count", "source_contract_passed", "source_errors",
        "answer_preview",
    ]
    with (output_dir / "results.csv").open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            source_judge = row.get("source_judge") or {}
            writer.writerow({
                "id": row.get("id"),
                "split": row.get("split"),
                "anomaly_family": row.get("anomaly_family"),
                "observed_input": row.get("observed_input"),
                "canonical_question": row.get("canonical_question"),
                "expected_action": row.get("expected_action"),
                "predicted_action": row.get("predicted_action"),
                "expected_should_block": row.get("expected_should_block"),
                "predicted_should_block": row.get("predicted_should_block"),
                "pipeline_executed": row.get("pipeline_executed"),
                "mode": row.get("mode"),
                "route": f"{row.get('route_category')}/{row.get('route_intent')}",
                "wall_sec": row.get("wall_sec"),
                "llm_call_count": row.get("llm_call_count"),
                "source_contract_passed": source_judge.get("passed"),
                "source_errors": " | ".join(str(item) for item in source_judge.get("errors", [])),
                "answer_preview": str(row.get("answer") or "").replace("\n", " ")[:500],
            })


def run_eval(args: argparse.Namespace) -> Path:
    _configure_environment(args)
    dataset = _read_jsonl(Path(args.dataset))
    if args.limit:
        dataset = dataset[: args.limit]
    corpus_rows = _read_jsonl(Path(args.corpus))
    corpus_questions = [str(row.get("question") or "") for row in corpus_rows if str(row.get("question") or "")]
    source_by_id = {str(row.get("id") or ""): row for row in corpus_rows if row.get("id")}
    output_dir = Path(args.output_dir) if args.output_dir else DEFAULT_OUTPUT_ROOT / datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir.mkdir(parents=True, exist_ok=True)

    warmup = preflight_ollama(
        model=args.model,
        kind="preflight",
        timeout_sec=args.warmup_timeout_sec,
        num_predict=1,
        num_ctx=args.num_ctx,
    )
    pipeline_warmup = warm_pipeline_caches()
    detector = KeyboardInputAnomalyDetector().fit(corpus_questions)
    rows: list[dict[str, Any]] = []
    completed_ids: set[str] = set()
    partial_path = output_dir / "partial_results.jsonl"
    if args.resume and partial_path.exists():
        rows = _read_jsonl(partial_path)
        completed_ids = {str(row.get("id")) for row in rows if row.get("id")}
        print(f"Resuming from {len(rows)} logged cases.", flush=True)
    started_all = time.perf_counter()

    for index, item in enumerate(dataset, start=1):
        if str(item.get("id")) in completed_ids:
            continue
        observed = str(item.get("observed_input") or "")
        features = detector.analyze(observed)
        decision = detector.classify(
            features,
            layout_threshold=args.layout_threshold,
            repeat_threshold=args.repeat_threshold,
        )
        source = source_by_id.get(str(item.get("source_case_id") or ""))
        started = time.perf_counter()
        pipeline_executed = not bool(decision["predicted_should_block"])
        result = None
        if pipeline_executed:
            result = answer_question_pipeline_debug(
                observed,
                experimental_rag_fallback=True,
                experimental_allow_llm=True,
            )
            wall_sec = round(time.perf_counter() - started, 4)
            calls = _llm_calls(result)
            source_judge = _judge_against_source(source, result, wall_sec, args.timeout_sec)
            answer = result.answer
            mode = result.mode
            route_category = result.route.category
            route_intent = result.route.intent
            confidence = result.confidence
            validation_ok = result.validation.ok
            validation_errors = list(result.validation.errors)
            validation_warnings = list(result.validation.warnings)
            stage_timings = _stage_timings(result)
        else:
            wall_sec = round(time.perf_counter() - started, 4)
            calls = []
            source_judge = {"applicable": False, "passed": None, "score": None, "errors": ["pipeline_skipped_by_input_guard"]}
            answer = ""
            mode = "input_guard_request_retype"
            route_category = "input_guard"
            route_intent = "keyboard_layout_mismatch"
            confidence = max(features.layout_score, features.repeat_score)
            validation_ok = True
            validation_errors = []
            validation_warnings = []
            stage_timings = []

        record = {
            "id": item.get("id"),
            "split": item.get("split"),
            "anomaly_family": item.get("anomaly_family"),
            "difficulty": item.get("difficulty"),
            "observed_input": observed,
            "canonical_question": item.get("canonical_question"),
            "source_case_id": item.get("source_case_id"),
            "expected_action": item.get("expected_action"),
            "predicted_action": decision["predicted_action"],
            "expected_should_block": bool(item.get("should_block_answer")),
            "predicted_should_block": bool(decision["predicted_should_block"]),
            "pipeline_executed": pipeline_executed,
            "keyboard_features": features.to_dict(),
            "answer": answer,
            "mode": mode,
            "route_category": route_category,
            "route_intent": route_intent,
            "confidence": confidence,
            "validation_ok": validation_ok,
            "validation_errors": validation_errors,
            "validation_warnings": validation_warnings,
            "wall_sec": wall_sec,
            "llm_call_count": len(calls),
            "llm_elapsed_ms_total": round(sum(float(call.get("llm_elapsed_ms") or 0.0) for call in calls), 2),
            "llm_kinds": sorted(set(str(call.get("llm_kind") or "") for call in calls if call.get("llm_kind"))),
            "llm_calls": calls,
            "stage_timings": stage_timings,
            "source_judge": source_judge,
        }
        rows.append(record)
        if args.checkpoint_interval and (index % args.checkpoint_interval == 0 or index == len(dataset)):
            _write_jsonl(partial_path, rows)
        if args.progress and (index == 1 or index % args.progress == 0 or index == len(dataset)):
            print(
                f"[{index}/{len(dataset)}] {record['id']} {record['predicted_action']} "
                f"{record['mode']} {record['wall_sec']}s",
                flush=True,
            )

    summary = _summarize(rows, {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "dataset": str(args.dataset),
        "corpus": str(args.corpus),
        "model": args.model,
        "allow_llm": True,
        "semantic_rag": True,
        "facts_composer": bool(args.facts_composer),
        "timeout_sec": args.timeout_sec,
        "num_predict": args.num_predict,
        "num_ctx": args.num_ctx,
        "layout_threshold": args.layout_threshold,
        "repeat_threshold": args.repeat_threshold,
        "warmup": warmup,
        "pipeline_warmup": {
            "ok": pipeline_warmup.ok,
            "elapsed_sec": pipeline_warmup.elapsed_sec,
            "warmed": list(pipeline_warmup.warmed),
            "errors": list(pipeline_warmup.errors),
            "timings": pipeline_warmup.timings,
        },
        "total_wall_sec": round(time.perf_counter() - started_all, 3),
    })
    _write_outputs(output_dir, rows, summary)
    return output_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate Keyboard Input Guard plus the LLM-enabled PSU chatbot pipeline.")
    parser.add_argument("--dataset", default=str(DEFAULT_DATASET))
    parser.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    parser.add_argument("--output-dir", default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--model", default="scb10x/typhoon2.5-qwen3-4b")
    parser.add_argument("--timeout-sec", type=float, default=9.0)
    parser.add_argument("--num-predict", type=int, default=128)
    parser.add_argument("--num-ctx", type=int, default=2048)
    parser.add_argument("--facts-num-ctx", type=int, default=3072)
    parser.add_argument("--facts-timeout-sec", type=float, default=5.0)
    parser.add_argument("--facts-num-predict", type=int, default=192)
    parser.add_argument("--facts-composer", action="store_true")
    parser.add_argument("--tool-router", action="store_true")
    parser.add_argument("--embedding-model", default="psu-bge-m3:q8_0")
    parser.add_argument("--embedding-num-ctx", type=int, default=1024)
    parser.add_argument("--model-first-min-remaining-sec", type=float, default=6.0)
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434")
    parser.add_argument("--warmup-timeout-sec", type=float, default=90.0)
    parser.add_argument("--layout-threshold", type=float, default=0.418411)
    parser.add_argument("--repeat-threshold", type=float, default=0.718849)
    parser.add_argument("--progress", type=int, default=25)
    parser.add_argument("--checkpoint-interval", type=int, default=25)
    parser.add_argument("--resume", action="store_true", help="Continue from partial_results.jsonl in the output directory.")
    args = parser.parse_args()
    output_dir = run_eval(args)
    print(f"Saved keyboard pipeline outputs to: {output_dir}")


if __name__ == "__main__":
    main()
