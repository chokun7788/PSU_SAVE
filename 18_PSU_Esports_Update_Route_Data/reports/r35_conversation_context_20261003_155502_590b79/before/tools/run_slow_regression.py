"""Run the preserved slow-case corpus through the supervised production path.

This is deliberately a focused regression runner, not a replacement for the
full model-enabled evaluation.  Every run writes a new directory so historical
raw results are never overwritten.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
BASELINE = ROOT / "reports" / "current_flow_regression" / "20260901_full_model_enabled" / "results.jsonl"
OUT_ROOT = ROOT / "reports" / "slow_regression"


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _expected_routes(case_id: str) -> list[str]:
    # MB-0618 is intentionally a dependent multi-question request.  Its
    # sub-questions must resolve through overview, while the public top-level
    # route remains multi_question.
    if case_id == "MB-0618-C-007":
        return ["multi_question"]
    if case_id == "KIA-0460":
        return ["equipment"]
    if case_id.startswith("MB-"):
        return ["overview"]
    return ["games"]


def _freeze_slow_cases(baseline: Path) -> list[dict[str, Any]]:
    rows = _read_jsonl(baseline)
    selected = [
        row for row in rows
        if float(row.get("wall_sec") or 0.0) > 10.0
        or str(row.get("status") or "") in {"harness_timeout", "worker_crash", "pipeline_timeout", "hard_timeout"}
    ]
    cases: list[dict[str, Any]] = []
    for row in selected:
        cases.append({
            "id": row["id"],
            "suite": row.get("suite", "faq"),
            "question": row.get("question", ""),
            "baseline_status": row.get("status", ""),
            "baseline_wall_sec": row.get("wall_sec", 0.0),
            "expected_runtime_routes": _expected_routes(str(row["id"])),
            "latency_target_sec": 1.5 if str(row["id"]).startswith("MB-") else 9.0,
            "allowed_source_categories": ["overview"] if str(row["id"]).startswith("MB-") else ["games"],
            "answer_contract": "safe_answer_or_safe_no_answer",
        })
    return cases


def _configure_runtime() -> None:
    os.environ.update({
        "PYTHONIOENCODING": "utf-8",
        "PSU_PIPELINE_WORKER_SUPERVISOR": "1",
        "PSU_PIPELINE_WORKERS": "1",
        "PSU_PIPELINE_GLOBAL_TIMEOUT_SEC": "9",
        "PSU_LLM_MAX_CONCURRENCY": "1",
        "PSU_LLM_CONCURRENCY_WAIT_SEC": "0.20",
        "PSU_INTENT_LLM_TIMEOUT_SEC": "1.2",
        "PSU_QUERY_PLANNER_TIMEOUT_SEC": "1.2",
        "PSU_FACTS_LLM_TIMEOUT_SEC": "4",
        "PSU_GENERAL_LLM_TIMEOUT_SEC": "4",
        "PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC": "4",
    })


def _plain_route(result: Any) -> dict[str, Any]:
    route = getattr(result, "route", None)
    return {
        "category": getattr(route, "category", ""),
        "intent": getattr(route, "intent", ""),
        "reason": getattr(route, "reason", ""),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--allow-llm", action="store_true", help="Permit gated local LLM calls; default is model-enabled policy with gates.")
    args = parser.parse_args()
    baseline = args.baseline.resolve()
    if not baseline.exists():
        raise SystemExit(f"Baseline file not found: {baseline}")

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    out = args.out.resolve() if args.out else OUT_ROOT / run_id
    out.mkdir(parents=True, exist_ok=False)
    _configure_runtime()
    cases = _freeze_slow_cases(baseline)
    manifest = {
        "run_id": run_id,
        "baseline": str(baseline.relative_to(ROOT)),
        "baseline_sha256": _sha256(baseline),
        "case_count": len(cases),
        "policy": {"pipeline_budget_sec": 9.0, "api_ceiling_sec": 10.0, "allow_llm": bool(args.allow_llm)},
        "cases": cases,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    from app.web_api.pipeline_supervisor import PipelineWorkerSupervisor

    supervisor = PipelineWorkerSupervisor(workers=1)
    results: list[dict[str, Any]] = []
    started = time.perf_counter()
    try:
        supervisor.start()
        for index, case in enumerate(cases, 1):
            result_started = time.perf_counter()
            call = supervisor.answer(
                case["question"],
                timeout_sec=9.85,
                experimental_rag_fallback=True,
                experimental_allow_llm=bool(args.allow_llm),
                request_id=f"slow-{run_id}-{index:02d}",
            )
            wall_sec = time.perf_counter() - result_started
            pipeline = call.result
            route = _plain_route(pipeline) if pipeline is not None else {}
            response = {
                "id": case["id"],
                "suite": case["suite"],
                "status": call.status,
                "wall_sec": round(wall_sec, 4),
                "mode": getattr(pipeline, "mode", ""),
                "validation_ok": bool(getattr(getattr(pipeline, "validation", None), "ok", False)),
                "route": route,
                "expected_runtime_routes": case["expected_runtime_routes"],
                "route_match": route.get("category") in case["expected_runtime_routes"],
                "within_10s": wall_sec <= 10.0,
                "within_case_target": wall_sec <= float(case["latency_target_sec"]),
                "diagnostics": call.diagnostics or {},
            }
            results.append(response)
            with (out / "results.jsonl").open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(response, ensure_ascii=False) + "\n")
            print(f"[{index}/{len(cases)}] {case['id']} {call.status} {wall_sec:.3f}s route={route.get('category', '-')}", flush=True)
    finally:
        performance = supervisor.health().get("performance", {})
        supervisor.shutdown()

    summary = {
        "run_id": run_id,
        "case_count": len(results),
        "completed": sum(row["status"] == "ok" for row in results),
        "within_10s": sum(row["within_10s"] for row in results),
        "route_matches": sum(row["route_match"] for row in results),
        "max_wall_sec": max((row["wall_sec"] for row in results), default=0.0),
        "total_wall_sec": round(time.perf_counter() - started, 3),
        "performance": performance,
    }
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["within_10s"] == len(results) and summary["route_matches"] == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
