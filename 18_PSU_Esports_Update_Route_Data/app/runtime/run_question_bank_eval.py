from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.pipeline.engine import answer_question_pipeline_debug

DEFAULT_QUESTION_BANK = PROJECT_ROOT / "data" / "eval" / "user_question_bank_400.jsonl"
DEFAULT_OUTPUT_ROOT = PROJECT_ROOT / "data" / "eval" / "question_bank_runs"


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _plain(value: Any) -> Any:
    if hasattr(value, "__dataclass_fields__"):
        return {key: _plain(getattr(value, key)) for key in value.__dataclass_fields__}
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _source_list(hits: list[dict[str, Any]]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for hit in hits:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        source = {
            "id": str(hit.get("id") or metadata.get("title") or ""),
            "title": str(metadata.get("title") or hit.get("id") or ""),
            "category": str(metadata.get("category") or ""),
            "source_url": str(metadata.get("source_url") or ""),
        }
        key = (source["id"], source["source_url"])
        if key in seen:
            continue
        seen.add(key)
        output.append(source)
    return output


def _trace_compact(trace: list[Any], limit: int = 10) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in trace[-limit:]:
        rows.append({
            "stage": getattr(item, "stage", ""),
            "decision": getattr(item, "decision", ""),
            "confidence": getattr(item, "confidence", 0.0),
            "detail": getattr(item, "detail", ""),
            "metadata": getattr(item, "metadata", {}),
        })
    return rows


def _strategy_from_mode(mode: str) -> str:
    clean = mode.removeprefix("pipeline:")
    if clean.startswith("structured_"):
        return "structured"
    if "calculator" in clean or "fast_path" in clean or clean.endswith("_fast"):
        return "fastpath/rulebase"
    if "rule" in clean:
        return "fastpath/rulebase"
    if "vector" in clean or "rag" in clean or "hybrid" in clean or "curated" in clean or "fact_card" in clean:
        return "rag/vector"
    if "llm" in clean:
        return "llm"
    if "clarification" in clean:
        return "clarification"
    if "no_answer" in clean:
        return "no_answer"
    return "pipeline"


def _csv_answer(answer: str, max_chars: int = 900) -> str:
    clean = " ".join((answer or "").split())
    return clean if len(clean) <= max_chars else clean[: max_chars - 3] + "..."


def _selected_candidate(artifact: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(artifact, dict):
        return {}
    selected = artifact.get("selected_candidate")
    return selected if isinstance(selected, dict) else {}


def _final_artifact(artifact: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(artifact, dict):
        return {}
    final = artifact.get("final")
    return final if isinstance(final, dict) else {}


def _run_one(item: dict[str, Any], *, rag_fallback: bool, allow_llm: bool) -> dict[str, Any]:
    started = time.perf_counter()
    result = answer_question_pipeline_debug(
        str(item.get("question") or ""),
        experimental_rag_fallback=rag_fallback,
        experimental_allow_llm=allow_llm,
    )
    wall_sec = round(time.perf_counter() - started, 4)
    artifact = _plain(result.decision_artifact)
    selected = _selected_candidate(artifact)
    final = _final_artifact(artifact)
    return {
        "id": item.get("id"),
        "category": item.get("category"),
        "question_no": item.get("question_no"),
        "question": item.get("question"),
        "expected_support": item.get("expected_support"),
        "note": item.get("note"),
        "answer": result.answer,
        "mode": result.mode,
        "strategy": _strategy_from_mode(result.mode),
        "route_category": result.route.category,
        "route_intent": result.route.intent,
        "route_confidence": result.route.confidence,
        "confidence": result.confidence,
        "elapsed_sec": result.elapsed,
        "wall_sec": wall_sec,
        "validation_ok": result.validation.ok,
        "validation_errors": list(result.validation.errors),
        "validation_warnings": list(result.validation.warnings),
        "universal_intent": _plain(result.universal_intent),
        "selected_candidate_id": selected.get("capability_id", ""),
        "selected_candidate_action": selected.get("action", ""),
        "selected_candidate_score": selected.get("score", ""),
        "final_execution_step": final.get("execution_step", ""),
        "evidence_count": final.get("evidence_count", len(result.hits)),
        "source_ids": final.get("source_ids", []),
        "sources": _source_list(result.hits),
        "decision_artifact": artifact,
        "trace": _trace_compact(result.trace),
    }


def _write_outputs(results: list[dict[str, Any]], output_dir: Path, summary: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "results.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    with (output_dir / "results.jsonl").open("w", encoding="utf-8") as file:
        for row in results:
            file.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")

    csv_fields = [
        "id",
        "category",
        "question_no",
        "question",
        "answer_preview",
        "mode",
        "strategy",
        "route",
        "confidence",
        "wall_sec",
        "selected_candidate_id",
        "selected_candidate_action",
        "selected_candidate_score",
        "final_execution_step",
        "evidence_count",
        "source_ids",
        "validation_ok",
        "expected_support",
    ]
    with (output_dir / "results.csv").open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=csv_fields)
        writer.writeheader()
        for row in results:
            writer.writerow({
                "id": row.get("id"),
                "category": row.get("category"),
                "question_no": row.get("question_no"),
                "question": row.get("question"),
                "answer_preview": _csv_answer(str(row.get("answer") or "")),
                "mode": row.get("mode"),
                "strategy": row.get("strategy"),
                "route": f"{row.get('route_category')}/{row.get('route_intent')}",
                "confidence": row.get("confidence"),
                "wall_sec": row.get("wall_sec"),
                "selected_candidate_id": row.get("selected_candidate_id"),
                "selected_candidate_action": row.get("selected_candidate_action"),
                "selected_candidate_score": row.get("selected_candidate_score"),
                "final_execution_step": row.get("final_execution_step"),
                "evidence_count": row.get("evidence_count"),
                "source_ids": " | ".join(str(value) for value in (row.get("source_ids") or [])),
                "validation_ok": row.get("validation_ok"),
                "expected_support": row.get("expected_support"),
            })

    easy_rows: list[dict[str, Any]] = []
    for row in results:
        easy_rows.append({
            "id": row.get("id"),
            "category": row.get("category"),
            "question_no": row.get("question_no"),
            "question": row.get("question"),
            "answer": row.get("answer"),
            "mode": row.get("mode"),
            "strategy": row.get("strategy"),
            "route": f"{row.get('route_category')}/{row.get('route_intent')}",
            "confidence": row.get("confidence"),
            "wall_sec": row.get("wall_sec"),
            "selected_candidate_id": row.get("selected_candidate_id"),
            "selected_candidate_action": row.get("selected_candidate_action"),
            "final_execution_step": row.get("final_execution_step"),
            "evidence_count": row.get("evidence_count"),
            "source_ids": row.get("source_ids"),
            "expected_support": row.get("expected_support"),
        })
    (output_dir / "results_easy.json").write_text(
        json.dumps(easy_rows, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    easy_csv_fields = [
        "id",
        "category",
        "question_no",
        "question",
        "answer",
        "mode",
        "strategy",
        "route",
        "confidence",
        "wall_sec",
        "selected_candidate_id",
        "selected_candidate_action",
        "final_execution_step",
        "evidence_count",
        "source_ids",
        "expected_support",
    ]
    with (output_dir / "results_easy.csv").open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=easy_csv_fields)
        writer.writeheader()
        for row in easy_rows:
            writer.writerow({
                **row,
                "source_ids": " | ".join(str(value) for value in (row.get("source_ids") or [])),
            })

    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )


def run_eval(args: argparse.Namespace) -> Path:
    question_bank = Path(args.question_bank)
    rows = _read_jsonl(question_bank)
    if args.category:
        rows = [row for row in rows if str(row.get("category")) == args.category]
    if args.limit:
        rows = rows[: args.limit]

    if args.tool_router:
        os.environ["PSU_LLM_TOOL_ROUTER"] = "1"
    elif args.disable_tool_router:
        os.environ["PSU_LLM_TOOL_ROUTER"] = "0"
    os.environ["PSU_ENTITY_RERANKER"] = "1" if args.entity_reranker else "0"
    os.environ["PSU_PIPELINE_GLOBAL_TIMEOUT_SEC"] = str(max(0.0, float(args.global_timeout)))
    if args.entity_reranker_model:
        os.environ["PSU_ENTITY_RERANKER_MODEL"] = args.entity_reranker_model
    if args.entity_reranker_cache_dir:
        os.environ["PSU_ENTITY_RERANKER_CACHE_DIR"] = args.entity_reranker_cache_dir

    generated_at = datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix = args.name or "question_bank_400_decision_artifact"
    output_dir = Path(args.output_dir) if args.output_dir else DEFAULT_OUTPUT_ROOT / f"{generated_at}_{suffix}"

    results: list[dict[str, Any]] = []
    started = time.perf_counter()
    total = len(rows)
    for index, item in enumerate(rows, start=1):
        result = _run_one(item, rag_fallback=args.rag_fallback, allow_llm=args.allow_llm)
        results.append(result)
        if args.progress and (index == 1 or index % args.progress == 0 or index == total):
            print(
                f"[{index}/{total}] {result['id']} "
                f"{result['mode']} {result['route_category']}/{result['route_intent']} "
                f"{result['wall_sec']}s",
                flush=True,
            )

    total_wall_sec = round(time.perf_counter() - started, 3)
    by_category: dict[str, int] = dict(Counter(str(row.get("category")) for row in results))
    mode_counts = dict(Counter(str(row.get("mode")) for row in results))
    route_counts = dict(Counter(f"{row.get('route_category')}/{row.get('route_intent')}" for row in results))
    strategy_counts = dict(Counter(str(row.get("strategy")) for row in results))
    selected_candidate_counts = dict(Counter(str(row.get("selected_candidate_id")) for row in results))
    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(results),
        "total_wall_sec": total_wall_sec,
        "avg_wall_sec": round(total_wall_sec / max(len(results), 1), 4),
        "question_bank": str(question_bank),
        "output_dir": str(output_dir),
        "allow_llm": args.allow_llm,
        "rag_fallback": args.rag_fallback,
        "tool_router_env": os.getenv("PSU_LLM_TOOL_ROUTER", "0"),
        "entity_reranker_env": os.getenv("PSU_ENTITY_RERANKER", "0"),
        "global_timeout_sec": float(os.getenv("PSU_PIPELINE_GLOBAL_TIMEOUT_SEC", "0")),
        "entity_reranker_model": os.getenv("PSU_ENTITY_RERANKER_MODEL", ""),
        "entity_reranker_cache_dir": os.getenv("PSU_ENTITY_RERANKER_CACHE_DIR", ""),
        "category_filter": args.category,
        "limit": args.limit,
        "category_counts": by_category,
        "strategy_counts": strategy_counts,
        "mode_counts": mode_counts,
        "route_counts": route_counts,
        "selected_candidate_counts": selected_candidate_counts,
    }
    _write_outputs(results, output_dir, summary)
    return output_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PSU Esports question bank through the pipeline and export JSON/CSV outputs.")
    parser.add_argument("--question-bank", default=str(DEFAULT_QUESTION_BANK))
    parser.add_argument("--output-dir", default="")
    parser.add_argument("--name", default="")
    parser.add_argument("--category", default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--progress", type=int, default=25)
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--no-rag-fallback", dest="rag_fallback", action="store_false")
    parser.set_defaults(rag_fallback=True)
    parser.add_argument("--tool-router", action="store_true", help="Set PSU_LLM_TOOL_ROUTER=1 for this run.")
    parser.add_argument("--disable-tool-router", action="store_true", help="Set PSU_LLM_TOOL_ROUTER=0 for this run.")
    parser.add_argument("--entity-reranker", action="store_true", help="Set PSU_ENTITY_RERANKER=1 for this run.")
    parser.add_argument("--entity-reranker-model", default=os.getenv("PSU_ENTITY_RERANKER_MODEL", "BAAI/bge-reranker-v2-m3"))
    parser.add_argument("--entity-reranker-cache-dir", default=os.getenv("PSU_ENTITY_RERANKER_CACHE_DIR", "D:/AIModels/huggingface"))
    parser.add_argument("--global-timeout", type=float, default=float(os.getenv("PSU_PIPELINE_GLOBAL_TIMEOUT_SEC", "0")))
    args = parser.parse_args()
    output_dir = run_eval(args)
    print(f"Saved eval outputs to: {output_dir}")


if __name__ == "__main__":
    main()
