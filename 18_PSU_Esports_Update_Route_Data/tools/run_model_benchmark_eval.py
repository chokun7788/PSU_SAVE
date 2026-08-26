from __future__ import annotations

import argparse
import csv
import json
import os
import re
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "data" / "eval" / "model_benchmark_1500.jsonl"
DEFAULT_CONFIG = ROOT / "data" / "eval" / "model_benchmark_models_under_10b.json"
REPORT_ROOT = ROOT / "reports" / "model_benchmark"


def _configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _stratified_select(rows: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    """Select a deterministic, proportional sample across question groups."""
    if limit <= 0 or len(rows) <= limit:
        return rows

    grouped: dict[str, list[tuple[int, dict[str, Any]]]] = defaultdict(list)
    for index, row in enumerate(rows):
        grouped[str(row.get("group") or "unknown")].append((index, row))

    group_keys = sorted(grouped)
    total = len(rows)
    quotas: dict[str, int] = {}
    remainders: dict[str, float] = {}
    for key in group_keys:
        raw = len(grouped[key]) * limit / total
        quotas[key] = min(len(grouped[key]), int(raw))
        remainders[key] = raw - int(raw)

    if limit >= len(group_keys):
        for key in group_keys:
            quotas[key] = max(1, quotas[key])

    allocated = sum(quotas.values())
    while allocated < limit:
        candidates = [key for key in group_keys if quotas[key] < len(grouped[key])]
        if not candidates:
            break
        key = max(candidates, key=lambda item: (remainders[item], len(grouped[item]), item))
        quotas[key] += 1
        allocated += 1

    while allocated > limit:
        candidates = [key for key in group_keys if quotas[key] > (1 if limit >= len(group_keys) else 0)]
        if not candidates:
            break
        key = min(candidates, key=lambda item: (remainders[item], quotas[item], item))
        quotas[key] -= 1
        allocated -= 1

    selected: list[tuple[int, dict[str, Any]]] = []
    for key in group_keys:
        bucket = grouped[key]
        quota = quotas[key]
        if quota <= 0:
            continue
        if quota == len(bucket):
            positions = list(range(len(bucket)))
        else:
            positions = sorted({round(index * (len(bucket) - 1) / (quota - 1)) for index in range(quota)}) if quota > 1 else [0]
            while len(positions) < quota:
                for position in range(len(bucket)):
                    if position not in positions:
                        positions.append(position)
                        if len(positions) == quota:
                            break
        selected.extend(bucket[position] for position in positions[:quota])

    selected.sort(key=lambda item: item[0])
    return [row for _, row in selected[:limit]]


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False, default=str, separators=(",", ":")) for row in rows) + "\n", encoding="utf-8")


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, default=str), encoding="utf-8")


def _plain(value: Any) -> Any:
    if hasattr(value, "__dataclass_fields__"):
        return {key: _plain(getattr(value, key)) for key in value.__dataclass_fields__}
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    if isinstance(value, tuple):
        return [str(item) for item in value if str(item)]
    return [str(value)]


def _contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def _mode_matches(mode: str, expected: Any) -> bool:
    prefixes = _as_list(expected)
    if not prefixes:
        return True
    return any(mode.startswith(prefix) for prefix in prefixes)


def _category_matches(category: str, expected: Any) -> bool:
    expected_values = _as_list(expected)
    if not expected_values:
        return True
    return category in expected_values


def _llm_call_rows(trace: list[dict[str, Any]]) -> list[dict[str, Any]]:
    calls: list[dict[str, Any]] = []
    for item in trace:
        metadata = item.get("metadata") if isinstance(item, dict) else None
        if isinstance(metadata, dict):
            call = metadata.get("llm_call")
            if isinstance(call, dict) and call:
                calls.append(call)
    return calls


def _full_llm_call_rows(result: Any) -> list[dict[str, Any]]:
    artifact = _plain(getattr(result, "decision_artifact", None))
    if isinstance(artifact, dict):
        calls = artifact.get("llm_calls")
        if isinstance(calls, list):
            return [dict(call) for call in calls if isinstance(call, dict) and call]
    full_trace = [_plain(item) for item in getattr(result, "trace", [])]
    return _llm_call_rows(full_trace)


def _stage_timing_rows(trace: list[Any]) -> list[dict[str, Any]]:
    timings: list[dict[str, Any]] = []
    for item in trace:
        if getattr(item, "stage", "") != "timing":
            continue
        metadata = _plain(getattr(item, "metadata", {}))
        timings.append({
            "process": getattr(item, "decision", ""),
            "elapsed_ms": float(metadata.get("elapsed_ms") or 0.0),
            "elapsed_sec": float(metadata.get("elapsed_sec") or 0.0),
            "detail": getattr(item, "detail", ""),
        })
    return timings


def _trace_compact(trace: list[Any], limit: int = 12) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in trace[-limit:]:
        rows.append({
            "stage": getattr(item, "stage", ""),
            "decision": getattr(item, "decision", ""),
            "confidence": getattr(item, "confidence", 0.0),
            "detail": getattr(item, "detail", ""),
            "metadata": _plain(getattr(item, "metadata", {})),
        })
    return rows


def _warmup_ollama(model: str, ollama_url: str, timeout_sec: float) -> dict[str, Any]:
    """Load the selected model before timing cases; warmup is excluded from case latency."""
    payload = {
        "model": model,
        "prompt": "ตอบคำว่า พร้อมใช้งาน สั้น ๆ",
        "stream": False,
        "think": False,
        "keep_alive": os.getenv("PSU_OLLAMA_KEEP_ALIVE", "10m"),
        "options": {
            "temperature": 0.0,
            "num_predict": 8,
            "num_ctx": int(os.getenv("PSU_GENERAL_LLM_NUM_CTX", "3072")),
        },
    }
    request = urllib.request.Request(
        f"{ollama_url.rstrip('/')}/api/generate",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=max(1.0, timeout_sec)) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
        answer = str(data.get("response") or "").strip()
        return {
            "ok": bool(answer),
            "elapsed_sec": round(time.perf_counter() - started, 4),
            "response_chars": len(answer),
            "done_reason": data.get("done_reason") or "",
            "load_duration": data.get("load_duration") or 0,
            "prompt_eval_duration": data.get("prompt_eval_duration") or 0,
            "eval_duration": data.get("eval_duration") or 0,
            "error": "" if answer else "empty response",
        }
    except (OSError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return {
            "ok": False,
            "elapsed_sec": round(time.perf_counter() - started, 4),
            "response_chars": 0,
            "error": f"{type(exc).__name__}: {exc}",
        }


def _judge(case: dict[str, Any], result: Any, wall_sec: float, timeout_sec: float, run_kind: str) -> dict[str, Any]:
    answer = str(result.answer or "")
    mode = str(result.mode or "")
    route_category = str(result.route.category or "")
    errors: list[str] = []
    warnings: list[str] = []

    if not _category_matches(route_category, case.get("expected_category")):
        errors.append(f"category_mismatch:{route_category}")
    if not _mode_matches(mode, case.get("expected_mode_prefix")):
        errors.append(f"mode_mismatch:{mode}")
    for token in _as_list(case.get("must_contain")):
        if not _contains(answer, token):
            errors.append(f"missing:{token}")
    any_tokens = _as_list(case.get("must_contain_any"))
    if any_tokens and not any(_contains(answer, token) for token in any_tokens):
        errors.append("missing_any:" + "|".join(any_tokens[:8]))
    for token in _as_list(case.get("must_not_contain")):
        if token and _contains(answer, token):
            errors.append(f"forbidden:{token}")
    if not bool(result.validation.ok):
        warnings.append("pipeline_validation_not_ok")
    if wall_sec > timeout_sec + 1.0:
        warnings.append("wall_time_over_timeout_budget")

    llm_required = bool(case.get("llm_required"))
    unavailable_signals = [
        "ยังไม่ส่งคำตอบสุดท้าย",
        "ยังไม่ได้เปิด",
        "general_llm_disabled",
        "general_llm_unavailable",
        "TimeoutError",
    ]
    if llm_required and run_kind == "llm":
        if any(signal.lower() in answer.lower() or signal.lower() in mode.lower() for signal in unavailable_signals):
            errors.append("llm_required_but_unavailable")
        if len(answer.strip()) < 12:
            errors.append("llm_required_answer_too_short")
    if llm_required and run_kind == "no_llm":
        warnings.append("expected_decline_for_no_llm")

    score = 100.0
    score -= 18.0 * sum(1 for item in errors if item.startswith("category_mismatch"))
    score -= 12.0 * sum(1 for item in errors if item.startswith("mode_mismatch"))
    score -= 12.0 * sum(1 for item in errors if item.startswith("missing:"))
    score -= 16.0 * sum(1 for item in errors if item.startswith("missing_any"))
    score -= 20.0 * sum(1 for item in errors if item.startswith("forbidden:"))
    score -= 25.0 * sum(1 for item in errors if item.startswith("llm_required"))
    if wall_sec > timeout_sec:
        score -= 10.0
    score = max(0.0, round(score, 2))
    return {
        "passed": not errors,
        "score": score,
        "errors": errors,
        "warnings": warnings,
    }


def _run_worker(args: argparse.Namespace) -> int:
    os.environ["PYTHONIOENCODING"] = "utf-8"
    os.environ["PSU_LLM_PREFLIGHT"] = "0"
    os.environ["PSU_OLLAMA_THINK"] = "false"
    os.environ["PSU_GENERAL_LLM_TIMEOUT_SEC"] = str(args.timeout_sec)
    os.environ["PSU_PIPELINE_GLOBAL_TIMEOUT_SEC"] = str(args.timeout_sec)
    os.environ["PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC"] = str(args.timeout_sec)
    facts_timeout_sec = float(args.facts_timeout_sec or min(float(args.timeout_sec), 5.0))
    facts_num_predict = int(args.facts_num_predict or max(int(args.num_predict), 192))
    os.environ["PSU_FACTS_LLM_TIMEOUT_SEC"] = str(facts_timeout_sec)
    os.environ["PSU_INTENT_LLM_TIMEOUT_SEC"] = str(min(float(args.timeout_sec), 20.0))
    os.environ["PSU_TOOL_ROUTER_TIMEOUT_SEC"] = str(min(float(args.timeout_sec), 20.0))
    os.environ["PSU_GENERAL_LLM_NUM_PREDICT"] = str(args.num_predict)
    os.environ["PSU_RAG_LLM_NUM_PREDICT"] = str(args.num_predict)
    os.environ["PSU_FACTS_LLM_NUM_PREDICT"] = str(facts_num_predict)
    os.environ["PSU_INTENT_LLM_NUM_PREDICT"] = str(min(int(args.num_predict), 160))
    os.environ["PSU_TOOL_ROUTER_NUM_PREDICT"] = str(min(int(args.num_predict), 180))
    if args.num_ctx:
        os.environ["PSU_GENERAL_LLM_NUM_CTX"] = str(args.num_ctx)
        os.environ["PSU_FACTS_LLM_NUM_CTX"] = str(args.facts_num_ctx or args.num_ctx)
        os.environ["PSU_INTENT_LLM_NUM_CTX"] = str(min(int(args.num_ctx), 2048))
        os.environ["PSU_TOOL_ROUTER_NUM_CTX"] = str(min(int(args.num_ctx), 2048))
        os.environ["PSU_QUERY_PLANNER_NUM_CTX"] = str(min(int(args.num_ctx), 2048))
    os.environ["PSU_LLM_TOOL_ROUTER"] = "1" if args.tool_router else "0"
    os.environ["PSU_FACTS_LLM_COMPOSER"] = "1" if args.facts_composer else "0"
    os.environ["PSU_RAG_LLM_COMPOSER"] = "1" if args.facts_composer and args.semantic_rag else "0"
    os.environ["PSU_MODEL_FIRST_FLOW"] = "1" if args.allow_llm and args.semantic_rag else "0"
    os.environ["PSU_MODEL_FIRST_MIN_REMAINING_SEC"] = str(args.model_first_min_remaining_sec or 6.0)
    os.environ["PSU_SEMANTIC_RETRIEVAL"] = "1" if args.semantic_rag else "0"
    os.environ["PSU_EMBEDDING_MODEL"] = str(args.embedding_model or "psu-bge-m3:q8_0")
    os.environ["PSU_EMBEDDING_NUM_CTX"] = str(args.embedding_num_ctx or 1024)
    if args.disable_health_manager:
        os.environ["PSU_LLM_HEALTH_MANAGER"] = "0"
    if args.ollama_url:
        os.environ["OLLAMA_URL"] = args.ollama_url.rstrip("/")
    if args.model:
        os.environ["PSU_CHATBOT_OLLAMA_MODEL"] = args.model
        os.environ["PSU_INTENT_LLM_MODEL"] = args.model
        os.environ["PSU_TOOL_ROUTER_MODEL"] = args.model
        os.environ["PSU_FACTS_LLM_MODEL"] = args.model

    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    warmup = {"enabled": bool(args.allow_llm and args.warmup), "ok": True, "elapsed_sec": 0.0, "response_chars": 0, "error": ""}
    if args.allow_llm and args.warmup:
        warmup_url = args.ollama_url or os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
        warmup = {"enabled": True, **_warmup_ollama(args.model, warmup_url, args.warmup_timeout_sec)}
        print(f"warmup model={args.model} ok={warmup['ok']} elapsed={warmup['elapsed_sec']}s", flush=True)

    from app.pipeline.engine import answer_question_pipeline_debug

    pipeline_warmup = {
        "enabled": bool(args.warmup),
        "ok": True,
        "elapsed_sec": 0.0,
        "warmed": [],
        "errors": [],
        "timings": {},
    }
    if args.warmup:
        from app.pipeline.warmup import warm_pipeline_caches

        warmed = warm_pipeline_caches()
        pipeline_warmup = {
            "enabled": True,
            "ok": warmed.ok,
            "elapsed_sec": warmed.elapsed_sec,
            "warmed": list(warmed.warmed),
            "errors": list(warmed.errors),
            "timings": dict(warmed.timings),
        }
        print(
            f"pipeline warmup ok={warmed.ok} elapsed={warmed.elapsed_sec}s "
            f"steps={','.join(warmed.warmed)}",
            flush=True,
        )

    rows = _read_jsonl(Path(args.cases))
    if args.case_ids:
        wanted_ids = {value.strip() for value in str(args.case_ids).split(",") if value.strip()}
        rows = [row for row in rows if str(row.get("id") or "") in wanted_ids]
    if args.only_llm_required:
        rows = [row for row in rows if row.get("llm_required")]
    if args.group:
        wanted_groups = {value.strip() for value in str(args.group).split(",") if value.strip()}
        rows = [row for row in rows if str(row.get("group")) in wanted_groups]
    if args.sample_per_group:
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in rows:
            grouped[str(row.get("group") or "")].append(row)
        rows = []
        for group in sorted(grouped):
            rows.extend(grouped[group][: args.sample_per_group])
    source_case_count = len(rows)
    if args.limit:
        rows = _stratified_select(rows, args.limit) if args.stratified else rows[: args.limit]

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    run_kind = "llm" if args.allow_llm else "no_llm"
    results: list[dict[str, Any]] = []
    done_ids: set[str] = set()
    partial_path = output_dir / "partial_results.jsonl"
    if args.resume:
        resume_path = output_dir / "results.jsonl"
        if not resume_path.exists():
            resume_path = partial_path
        if resume_path.exists():
            results = _read_jsonl(resume_path)
            done_ids = {str(row.get("id") or "") for row in results if row.get("id")}
            print(f"Resuming {args.run_label}: loaded {len(done_ids)} completed cases", flush=True)
    started_all = time.perf_counter()
    pending_rows = [row for row in rows if str(row.get("id") or "") not in done_ids]
    for index, case in enumerate(pending_rows, 1):
        started = time.perf_counter()
        try:
            result = answer_question_pipeline_debug(
                str(case.get("question") or ""),
                experimental_rag_fallback=True,
                experimental_allow_llm=bool(args.allow_llm),
            )
            wall_sec = round(time.perf_counter() - started, 4)
            compact_trace = _trace_compact(result.trace)
            judge = _judge(case, result, wall_sec, float(args.timeout_sec), run_kind)
            llm_calls = _full_llm_call_rows(result)
            stage_timings = _stage_timing_rows(result.trace)
            results.append({
                "id": case.get("id"),
                "group": case.get("group"),
                "quality_bucket": case.get("quality_bucket"),
                "risk": case.get("risk"),
                "question": case.get("question"),
                "llm_required": bool(case.get("llm_required")),
                "answer": result.answer,
                "mode": result.mode,
                "route_category": result.route.category,
                "route_intent": result.route.intent,
                "confidence": result.confidence,
                "validation_ok": result.validation.ok,
                "validation_errors": list(result.validation.errors),
                "validation_warnings": list(result.validation.warnings),
                "wall_sec": wall_sec,
                "elapsed_sec": result.elapsed,
                "llm_call_count": len(llm_calls),
                "llm_elapsed_ms_total": round(sum(float(call.get("llm_elapsed_ms") or 0.0) for call in llm_calls), 2),
                "llm_kinds": sorted(set(str(call.get("llm_kind") or "") for call in llm_calls if call.get("llm_kind"))),
                "llm_calls": llm_calls,
                "stage_timings": stage_timings,
                "judge": judge,
                "trace": compact_trace,
            })
        except Exception as exc:  # noqa: BLE001 - benchmark must record crashes and continue.
            wall_sec = round(time.perf_counter() - started, 4)
            results.append({
                "id": case.get("id"),
                "group": case.get("group"),
                "quality_bucket": case.get("quality_bucket"),
                "risk": case.get("risk"),
                "question": case.get("question"),
                "llm_required": bool(case.get("llm_required")),
                "answer": "",
                "mode": "exception",
                "route_category": "",
                "route_intent": "",
                "confidence": 0.0,
                "validation_ok": False,
                "validation_errors": [type(exc).__name__, str(exc)],
                "validation_warnings": [],
                "wall_sec": wall_sec,
                "elapsed_sec": wall_sec,
                "llm_call_count": 0,
                "llm_elapsed_ms_total": 0.0,
                "llm_kinds": [],
                "judge": {"passed": False, "score": 0.0, "errors": [f"exception:{type(exc).__name__}"], "warnings": [str(exc)]},
                "trace": [],
            })
        done_count = len(results)
        if args.checkpoint_interval and (done_count % args.checkpoint_interval == 0 or index == len(pending_rows)):
            _write_jsonl(partial_path, results)
            partial_summary = _summarize_results(results, {
                "run_label": args.run_label,
                "run_kind": run_kind,
                "model": args.model,
                "partial": True,
                "total_requested": len(rows),
                "completed": len(results),
                "total_wall_sec": round(time.perf_counter() - started_all, 3),
            })
            _write_json(output_dir / "partial_summary.json", partial_summary)
        if args.progress and (index == 1 or index % args.progress == 0 or index == len(pending_rows)):
            latest = results[-1]
            print(f"[{done_count}/{len(rows)}] {latest['id']} {latest['mode']} {latest['wall_sec']}s score={latest['judge']['score']}", flush=True)

    summary = _summarize_results(results, {
        "run_label": args.run_label,
        "run_kind": run_kind,
        "model": args.model,
        "allow_llm": bool(args.allow_llm),
        "timeout_sec": float(args.timeout_sec),
        "num_predict": int(args.num_predict),
        "num_ctx": int(args.num_ctx or os.getenv("PSU_GENERAL_LLM_NUM_CTX", "3072")),
        "ollama_url": args.ollama_url,
        "tool_router": bool(args.tool_router),
        "facts_composer": bool(args.facts_composer),
        "semantic_rag": bool(args.semantic_rag),
        "embedding_model": str(args.embedding_model or "psu-bge-m3:q8_0"),
        "embedding_num_ctx": int(args.embedding_num_ctx or 1024),
        "facts_num_ctx": int(args.facts_num_ctx or args.num_ctx or 3072),
        "facts_timeout_sec": facts_timeout_sec,
        "facts_num_predict": facts_num_predict,
        "model_first_min_remaining_sec": float(args.model_first_min_remaining_sec or 6.0),
        "disable_health_manager": bool(args.disable_health_manager),
        "cases": str(args.cases),
        "limit": int(args.limit or 0),
        "source_case_count": source_case_count,
        "case_ids": str(args.case_ids or ""),
        "selection_strategy": "stratified_by_group" if args.stratified else "first_n",
        "warmup": warmup,
        "pipeline_warmup": pipeline_warmup,
        "resumed_from": len(done_ids),
        "total_wall_sec": round(time.perf_counter() - started_all, 3),
    })
    _write_run_outputs(output_dir, results, summary)
    return 0


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round((pct / 100.0) * (len(ordered) - 1))))
    return round(ordered[index], 4)


def _summarize_results(results: list[dict[str, Any]], meta: dict[str, Any]) -> dict[str, Any]:
    times = [float(row.get("wall_sec") or 0.0) for row in results]
    passed = sum(1 for row in results if row.get("judge", {}).get("passed"))
    scores = [float(row.get("judge", {}).get("score") or 0.0) for row in results]
    errors = Counter(error for row in results for error in row.get("judge", {}).get("errors", []))
    by_group: dict[str, dict[str, Any]] = {}
    for group in sorted(set(str(row.get("group") or "") for row in results)):
        group_rows = [row for row in results if str(row.get("group") or "") == group]
        group_scores = [float(row.get("judge", {}).get("score") or 0.0) for row in group_rows]
        group_times = [float(row.get("wall_sec") or 0.0) for row in group_rows]
        by_group[group] = {
            "total": len(group_rows),
            "passed": sum(1 for row in group_rows if row.get("judge", {}).get("passed")),
            "pass_rate": round(sum(1 for row in group_rows if row.get("judge", {}).get("passed")) / max(len(group_rows), 1) * 100, 2),
            "avg_score": round(statistics.mean(group_scores), 2) if group_scores else 0.0,
            "avg_wall_sec": round(statistics.mean(group_times), 4) if group_times else 0.0,
            "p95_wall_sec": _percentile(group_times, 95),
        }
    return {
        **meta,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(results),
        "passed": passed,
        "pass_rate": round(passed / max(len(results), 1) * 100, 2),
        "avg_score": round(statistics.mean(scores), 2) if scores else 0.0,
        "avg_wall_sec": round(statistics.mean(times), 4) if times else 0.0,
        "median_wall_sec": round(statistics.median(times), 4) if times else 0.0,
        "p95_wall_sec": _percentile(times, 95),
        "max_wall_sec": round(max(times), 4) if times else 0.0,
        "llm_call_total": sum(int(row.get("llm_call_count") or 0) for row in results),
        "mode_counts": dict(Counter(str(row.get("mode") or "") for row in results)),
        "route_counts": dict(Counter(f"{row.get('route_category')}/{row.get('route_intent')}" for row in results)),
        "group_counts": dict(Counter(str(row.get("group") or "") for row in results)),
        "quality_bucket_counts": dict(Counter(str(row.get("quality_bucket") or "") for row in results)),
        "top_errors": dict(errors.most_common(30)),
        "by_group": by_group,
    }


def _write_run_outputs(output_dir: Path, results: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    _write_jsonl(output_dir / "results.jsonl", results)
    _write_json(output_dir / "results.json", results)
    _write_json(output_dir / "summary.json", summary)
    fields = [
        "id", "group", "quality_bucket", "question", "answer_preview", "mode", "route",
        "score", "passed", "wall_sec", "llm_call_count", "llm_kinds", "errors", "warnings",
    ]
    with (output_dir / "results.csv").open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in results:
            answer = " ".join(str(row.get("answer") or "").split())
            writer.writerow({
                "id": row.get("id"),
                "group": row.get("group"),
                "quality_bucket": row.get("quality_bucket"),
                "question": row.get("question"),
                "answer_preview": answer[:700],
                "mode": row.get("mode"),
                "route": f"{row.get('route_category')}/{row.get('route_intent')}",
                "score": row.get("judge", {}).get("score"),
                "passed": row.get("judge", {}).get("passed"),
                "wall_sec": row.get("wall_sec"),
                "llm_call_count": row.get("llm_call_count"),
                "llm_kinds": " | ".join(row.get("llm_kinds") or []),
                "errors": " | ".join(row.get("judge", {}).get("errors") or []),
                "warnings": " | ".join(row.get("judge", {}).get("warnings") or []),
            })


def _safe_label(value: str) -> str:
    clean = re.sub(r"[^0-9A-Za-z_.-]+", "_", value)
    return clean.strip("_") or "run"


def _run_subprocess(command: list[str], env: dict[str, str]) -> int:
    completed = subprocess.run(command, cwd=str(ROOT), env=env)
    return int(completed.returncode)


def _load_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _make_report(root: Path, run_dirs: list[Path], cases_path: Path) -> Path:
    summaries: list[dict[str, Any]] = []
    for run_dir in run_dirs:
        summary_path = run_dir / "summary.json"
        if summary_path.exists():
            summaries.append(json.loads(summary_path.read_text(encoding="utf-8")))
    summaries.sort(key=lambda row: (-float(row.get("avg_score") or 0), float(row.get("avg_wall_sec") or 9999)))

    lines = [
        "# PSU Esports Chatbot Model Benchmark Report",
        "",
        f"- Generated at: {datetime.now().isoformat(timespec='seconds')}",
        f"- Case bank: `{cases_path}`",
        f"- Runs: {len(summaries)}",
        "",
        "## Overall Ranking",
        "",
        "| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, row in enumerate(summaries, 1):
        lines.append(
            f"| {idx} | {row.get('run_label')} | {row.get('model') or 'No-LLM'} | "
            f"{row.get('pass_rate')}% | {row.get('avg_score')} | {row.get('avg_wall_sec')} | "
            f"{row.get('p95_wall_sec')} | {row.get('max_wall_sec')} | {row.get('llm_call_total')} |"
        )

    lines.extend(["", "## Group Breakdown", ""])
    for row in summaries:
        lines.append(f"### {row.get('run_label')} ({row.get('model') or 'No-LLM'})")
        lines.append("")
        lines.append("| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        for group, detail in sorted((row.get("by_group") or {}).items()):
            lines.append(
                f"| {group} | {detail.get('total')} | {detail.get('pass_rate')}% | "
                f"{detail.get('avg_score')} | {detail.get('avg_wall_sec')} | {detail.get('p95_wall_sec')} |"
            )
        top_errors = row.get("top_errors") or {}
        if top_errors:
            lines.append("")
            lines.append("Top errors:")
            for error, count in list(top_errors.items())[:8]:
                lines.append(f"- `{error}`: {count}")
        lines.append("")

    lines.extend(["## How To Read", ""])
    if any(row.get("run_kind") == "no_llm" for row in summaries):
        lines.extend([
            "- `No-LLM` คือ baseline ที่ปิด Local LLM และจะรันเฉพาะเมื่อระบุ `--include-no-llm`",
            "- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้",
        ])
    lines.extend([
        "- ค่าเริ่มต้นของ benchmark รันเฉพาะ model เพื่อไม่เสียเวลาทำ baseline ซ้ำ",
        "- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย",
        "- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run",
        "",
    ])
    report = root / "REPORT.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    return report


def _run_master(args: argparse.Namespace) -> int:
    config = _load_config(Path(args.config))
    semantic_rag_enabled = (
        bool(config.get("semantic_rag", True))
        if args.semantic_rag is None
        else bool(args.semantic_rag)
    )
    facts_composer_enabled = (
        bool(config.get("facts_composer", True))
        if args.facts_composer is None
        else bool(args.facts_composer)
    )
    embedding_model = str(args.embedding_model or config.get("embedding_model") or "psu-bge-m3:q8_0")
    embedding_num_ctx = int(args.embedding_num_ctx or config.get("embedding_num_ctx") or 1024)
    facts_num_ctx = int(args.facts_num_ctx or config.get("facts_num_ctx") or 3072)
    facts_timeout_sec = float(args.facts_timeout_sec or config.get("facts_timeout_sec") or 5.0)
    facts_num_predict = int(args.facts_num_predict or config.get("facts_num_predict") or 192)
    model_first_min_remaining_sec = float(
        args.model_first_min_remaining_sec
        or config.get("model_first_min_remaining_sec")
        or 6.0
    )
    cases_path = Path(args.cases)
    if not cases_path.exists() or args.regenerate_cases:
        command = [sys.executable, str(ROOT / "tools" / "generate_model_benchmark_cases.py"), "--target", str(args.target_cases), "--jsonl", str(cases_path)]
        result = subprocess.run(command, cwd=str(ROOT))
        if result.returncode != 0:
            return int(result.returncode)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_root = Path(args.output_dir) if args.output_dir else REPORT_ROOT / timestamp
    output_root.mkdir(parents=True, exist_ok=True)

    model_names = [str(item["name"]) for item in config.get("models", [])]
    if args.models:
        wanted = {item.strip() for item in args.models.split(",") if item.strip()}
        model_names = [name for name in model_names if name in wanted]
    elif config.get("default_models"):
        wanted = {str(item) for item in config.get("default_models", [])}
        model_names = [name for name in model_names if name in wanted]
    if args.no_models:
        model_names = []
    if args.first_models:
        model_names = model_names[: args.first_models]

    run_dirs: list[Path] = []
    env_base = os.environ.copy()
    env_base["PYTHONIOENCODING"] = "utf-8"
    env_base["OLLAMA_HOST"] = str(args.ollama_host or config.get("ollama_host") or "").replace("http://", "").replace("https://", "")
    env_base["OLLAMA_MODELS"] = str(args.ollama_models or config.get("ollama_model_dir") or "")

    if args.include_no_llm and not args.skip_no_llm:
        run_label = "no_llm"
        run_dir = output_root / run_label
        command = [
            sys.executable, str(Path(__file__).resolve()), "--worker",
            "--run-label", run_label,
            "--cases", str(cases_path),
            "--output-dir", str(run_dir),
            "--timeout-sec", str(args.timeout_sec or config.get("timeout_sec", 20)),
            "--num-predict", str(args.num_predict or config.get("num_predict", 256)),
            "--num-ctx", str(args.num_ctx or config.get("num_ctx", 3072)),
            "--progress", str(args.progress),
        ]
        if args.limit:
            command.extend(["--limit", str(args.limit)])
        if args.stratified:
            command.append("--stratified")
        if args.sample_per_group:
            command.extend(["--sample-per-group", str(args.sample_per_group)])
        if args.group:
            command.extend(["--group", str(args.group)])
        if args.case_ids:
            command.extend(["--case-ids", str(args.case_ids)])
        if args.only_llm_required:
            command.append("--only-llm-required")
        if args.warmup:
            command.extend(["--warmup", "--warmup-timeout-sec", str(args.warmup_timeout_sec)])
        if semantic_rag_enabled:
            command.append("--semantic-rag")
        command.extend([
            "--embedding-model", embedding_model,
            "--embedding-num-ctx", str(embedding_num_ctx),
            "--facts-num-ctx", str(facts_num_ctx),
            "--facts-timeout-sec", str(facts_timeout_sec),
            "--facts-num-predict", str(facts_num_predict),
            "--model-first-min-remaining-sec", str(model_first_min_remaining_sec),
        ])
        command.extend(["--checkpoint-interval", str(args.checkpoint_interval)])
        if args.resume:
            command.append("--resume")
        code = _run_subprocess(command, env_base)
        if code != 0:
            return code
        run_dirs.append(run_dir)

    for model in model_names:
        if args.pull:
            pull_env = env_base.copy()
            pull_env["OLLAMA_HOST"] = str(args.ollama_host or config.get("ollama_host") or "127.0.0.1:11435")
            print(f"Pulling {model} ...", flush=True)
            pull = subprocess.run(["ollama", "pull", model], cwd=str(ROOT), env=pull_env)
            if pull.returncode != 0:
                print(f"WARNING: pull failed for {model}; benchmark will still try to run it.", flush=True)
        run_label = "llm_" + _safe_label(model)
        run_dir = output_root / run_label
        command = [
            sys.executable, str(Path(__file__).resolve()), "--worker",
            "--run-label", run_label,
            "--model", model,
            "--allow-llm",
            "--cases", str(cases_path),
            "--output-dir", str(run_dir),
            "--timeout-sec", str(args.timeout_sec or config.get("timeout_sec", 20)),
            "--num-predict", str(args.num_predict or config.get("num_predict", 256)),
            "--num-ctx", str(args.num_ctx or config.get("num_ctx", 3072)),
            "--ollama-url", str(args.ollama_url or f"http://{str(args.ollama_host or config.get('ollama_host') or '127.0.0.1:11435').replace('http://', '').replace('https://', '')}"),
            "--progress", str(args.progress),
        ]
        if args.limit:
            command.extend(["--limit", str(args.limit)])
        if args.stratified:
            command.append("--stratified")
        if args.sample_per_group:
            command.extend(["--sample-per-group", str(args.sample_per_group)])
        if args.group:
            command.extend(["--group", str(args.group)])
        if args.case_ids:
            command.extend(["--case-ids", str(args.case_ids)])
        command.extend(["--checkpoint-interval", str(args.checkpoint_interval)])
        if args.resume:
            command.append("--resume")
        if args.only_llm_required:
            command.append("--only-llm-required")
        if args.tool_router:
            command.append("--tool-router")
        if facts_composer_enabled:
            command.append("--facts-composer")
        if semantic_rag_enabled:
            command.append("--semantic-rag")
        command.extend([
            "--embedding-model", embedding_model,
            "--embedding-num-ctx", str(embedding_num_ctx),
            "--facts-num-ctx", str(facts_num_ctx),
            "--facts-timeout-sec", str(facts_timeout_sec),
            "--facts-num-predict", str(facts_num_predict),
            "--model-first-min-remaining-sec", str(model_first_min_remaining_sec),
        ])
        if args.warmup:
            command.extend(["--warmup", "--warmup-timeout-sec", str(args.warmup_timeout_sec)])
        if args.disable_health_manager:
            command.append("--disable-health-manager")
        code = _run_subprocess(command, env_base)
        if code != 0 and args.stop_on_error:
            return code
        run_dirs.append(run_dir)

    report = _make_report(output_root, run_dirs, cases_path)
    print(f"Saved benchmark report: {report}")
    return 0


def main() -> int:
    _configure_stdout()
    parser = argparse.ArgumentParser(description="Run Ollama model benchmark for PSU Esports Chatbot.")
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--cases", default=str(DEFAULT_CASES))
    parser.add_argument("--output-dir", default="")
    parser.add_argument("--run-label", default="")
    parser.add_argument("--model", default="")
    parser.add_argument("--models", default="", help="Comma-separated model names from config.")
    parser.add_argument("--first-models", type=int, default=0)
    parser.add_argument("--no-models", action="store_true")
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--include-no-llm", action="store_true", help="Also run the legacy deterministic baseline.")
    parser.add_argument("--skip-no-llm", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--pull", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--stratified", action="store_true", help="Select a deterministic proportional sample across groups when --limit is used.")
    parser.add_argument("--warmup", action="store_true", help="Warm the Ollama model before timing benchmark cases.")
    parser.add_argument("--warmup-timeout-sec", type=float, default=90.0)
    parser.add_argument("--sample-per-group", type=int, default=0)
    parser.add_argument("--group", default="", help="One group or a comma-separated group list.")
    parser.add_argument("--case-ids", default="", help="Comma-separated case IDs to run without changing the case bank.")
    parser.add_argument("--only-llm-required", action="store_true")
    parser.add_argument("--target-cases", type=int, default=1600)
    parser.add_argument("--regenerate-cases", action="store_true")
    parser.add_argument("--timeout-sec", type=float, default=0.0)
    parser.add_argument("--num-predict", type=int, default=0)
    parser.add_argument("--num-ctx", type=int, default=0)
    parser.add_argument("--ollama-host", default="")
    parser.add_argument("--ollama-url", default="")
    parser.add_argument("--ollama-models", default="")
    parser.add_argument("--tool-router", action="store_true")
    parser.add_argument("--facts-composer", dest="facts_composer", action="store_true")
    parser.add_argument("--no-facts-composer", dest="facts_composer", action="store_false")
    parser.add_argument("--semantic-rag", dest="semantic_rag", action="store_true")
    parser.add_argument("--no-semantic-rag", dest="semantic_rag", action="store_false")
    parser.add_argument("--embedding-model", default="")
    parser.add_argument("--embedding-num-ctx", type=int, default=0)
    parser.add_argument("--facts-num-ctx", type=int, default=0)
    parser.add_argument("--facts-timeout-sec", type=float, default=0.0)
    parser.add_argument("--facts-num-predict", type=int, default=0)
    parser.add_argument("--model-first-min-remaining-sec", type=float, default=0.0)
    parser.add_argument("--disable-health-manager", action="store_true")
    parser.add_argument("--progress", type=int, default=100)
    parser.add_argument("--checkpoint-interval", type=int, default=25)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--stop-on-error", action="store_true")
    parser.set_defaults(facts_composer=None, semantic_rag=None)
    args = parser.parse_args()
    if args.worker:
        if not args.run_label:
            parser.error("--run-label is required for --worker")
        if not args.output_dir:
            parser.error("--output-dir is required for --worker")
        return _run_worker(args)
    return _run_master(args)


if __name__ == "__main__":
    raise SystemExit(main())
