from __future__ import annotations

"""Run the Thai and English 1,600-case corpora with one recoverable worker.

The watchdog belongs to this evaluator.  It records a right-censored
``harness_timeout`` and replaces only its own worker; it does not claim that
the production API killed the underlying request at that instant.
"""

import argparse
import dataclasses
import json
import math
import multiprocessing as mp
import os
import queue
import shutil
import sys
import threading
import time
from collections import Counter
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

THAI_CORPUS = ROOT / "data" / "eval" / "model_benchmark_1500.jsonl"
ENGLISH_CORPUS = ROOT / "data" / "eval" / "english_shadow_1600_machine_20260908.jsonl"
MODEL = "scb10x/typhoon2.5-qwen3-4b"


def _plain(value: Any) -> Any:
    if dataclasses.is_dataclass(value):
        return _plain(dataclasses.asdict(value))
    if isinstance(value, SimpleNamespace):
        return {key: _plain(item) for key, item in vars(value).items()}
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(_plain(value), ensure_ascii=False, indent=2), encoding="utf-8")


def _percentile(values: list[float], percentage: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil(len(ordered) * percentage / 100) - 1))
    return round(ordered[index], 4)


def _runtime_environment() -> dict[str, str]:
    """Mirror the current local web preview profile, not the old 10s benchmark."""
    return {
        "PYTHONIOENCODING": "utf-8",
        "PYTHONUTF8": "1",
        "PSU_BILINGUAL_EN_ENABLED": "1",
        "PSU_LOCAL_LLM_ASSIST_ENABLED": "1",
        "PSU_CHATBOT_OLLAMA_MODEL": MODEL,
        "PSU_INTENT_LLM_MODEL": MODEL,
        "PSU_TOOL_ROUTER_MODEL": MODEL,
        "PSU_FACTS_LLM_MODEL": MODEL,
        "PSU_KNOWLEDGE_LLM_MODEL": MODEL,
        "PSU_PRODUCT_BACKEND_TIMEOUT_SEC": "20",
        "PSU_PIPELINE_GLOBAL_TIMEOUT_SEC": "19",
        "PSU_INTENT_LLM_TIMEOUT_SEC": "14",
        "PSU_INTENT_LLM_NUM_PREDICT": "18",
        "PSU_INTENT_LLM_NUM_CTX": "1536",
        "PSU_QUERY_PLANNER_TIMEOUT_SEC": "4",
        "PSU_GENERAL_LLM_TIMEOUT_SEC": "8",
        "PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC": "6",
        "PSU_OLLAMA_KEEP_ALIVE": "30m",
        # Match the local web worker: a cold BGE process can consume several
        # seconds before the first query embedding.  The evaluator measures
        # request behaviour, not model boot time, so warm it before `ready`.
        "PSU_EMBEDDING_KEEP_ALIVE": "30m",
        "PSU_PIPELINE_WARMUP_EMBEDDING": "1",
        "PSU_PIPELINE_WORKER_WARMUP_LLM": "1",
        "PSU_MODEL_FIRST_PREFLIGHT_CONFIDENCE": "0.99",
        "PSU_INTENT_LLM_FIRST_ONLY_WEAK": "0",
        "PSU_INTENT_STRONG_ROUTE_SKIP_LLM_CONFIDENCE": "0.99",
        "PSU_INTENT_STRONG_HEURISTIC_SKIP_LLM_CONFIDENCE": "0.99",
        "PSU_LLM_PREFLIGHT": "1",
        "PSU_PIPELINE_WARMUP": "1",
        "PSU_PIPELINE_WORKER_SUPERVISOR": "0",
        "PSU_INPUT_QUALITY_GUARD_MODE": "enforce",
        "PSU_INPUT_QUALITY_REPEAT_POLICY": "warn_and_continue",
        "PSU_SEMANTIC_RETRIEVAL": "1",
        "PSU_MODEL_FIRST_FLOW": "1",
        "PSU_RAG_LLM_COMPOSER": "1",
        "PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW": "1",
        "PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH": str(
            ROOT / "data" / "locales" / "en" / "localization_review_drafts_machine_20260915_audited.jsonl"
        ),
    }


def _compact_trace(trace: list[Any]) -> list[dict[str, Any]]:
    allowed_metadata = {
        "elapsed_ms", "elapsed_sec", "reason", "model", "status", "error_type",
        "used_llm", "remaining_sec", "global_remaining_sec", "timing_status",
        "candidate_count", "comparison_count", "queue_wait_sec", "stage",
    }
    rows: list[dict[str, Any]] = []
    for item in trace:
        row = _plain(item)
        if isinstance(row, dict):
            metadata = row.get("metadata", {})
            compact_metadata = {
                str(key): value
                for key, value in metadata.items()
                if str(key) in allowed_metadata and isinstance(value, (str, int, float, bool, type(None)))
            } if isinstance(metadata, dict) else {}
            rows.append({
                "stage": row.get("stage", ""),
                "decision": row.get("decision", ""),
                "confidence": row.get("confidence", 0.0),
                "detail": row.get("detail", ""),
                "metadata": compact_metadata,
            })
    return rows[-30:]


def _worker_main(conn, environment: dict[str, str]) -> None:
    os.environ.update(environment)
    try:
        from app.pipeline.engine import AnswerQualityPipeline

        pipeline = AnswerQualityPipeline()
        # Keep model/client boot outside every individual case.  The web
        # profile already does this in its supervised worker; mirroring it
        # here prevents a cold embedding request from being mislabeled as a
        # retrieval regression or a harness timeout.
        if environment.get("PSU_SEMANTIC_RETRIEVAL") == "1":
            try:
                from app.pipeline.semantic_embeddings import warm_semantic_embedding_model

                warm_semantic_embedding_model()
            except Exception:
                # A failed warmup must be observable through normal cases and
                # must not make the evaluator claim a successful RAG run.
                pass
        if environment.get("PSU_LOCAL_LLM_ASSIST_ENABLED") == "1":
            try:
                from app.pipeline.llm_health import preflight_ollama

                preflight_ollama(
                    model=environment.get("PSU_INTENT_LLM_MODEL", MODEL),
                    kind="evaluator_worker_warmup",
                    timeout_sec=45.0,
                )
            except Exception:
                pass
        conn.send({"event": "ready"})
        while True:
            task = conn.recv()
            if task is None:
                return
            started = time.perf_counter()
            try:
                result = pipeline.answer(
                    str(task["question"]),
                    locale=str(task["locale"]),
                    experimental_allow_llm=True,
                    experimental_rag_fallback=True,
                    global_timeout_sec=20.0,
                )
                trace = _compact_trace(list(getattr(result, "trace", []) or []))
                stages = [row for row in trace if row.get("stage") == "timing"]
                conn.send({
                    "event": "result",
                    "status": "completed",
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "elapsed_sec": float(getattr(result, "elapsed", 0.0)),
                    "answer": str(getattr(result, "answer", "")),
                    "mode": str(getattr(result, "mode", "")),
                    "route_category": str(getattr(getattr(result, "route", None), "category", "")),
                    "route_intent": str(getattr(getattr(result, "route", None), "intent", "")),
                    "confidence": float(getattr(result, "confidence", 0.0)),
                    "validation_ok": bool(getattr(getattr(result, "validation", None), "ok", False)),
                    "validation_errors": list(getattr(getattr(result, "validation", None), "errors", []) or []),
                    "validation_warnings": list(getattr(getattr(result, "validation", None), "warnings", []) or []),
                    "language": _plain(getattr(result, "language", None)),
                    "universal_intent": _plain(getattr(result, "universal_intent", None)),
                    "trace": trace,
                    "stage_timings": stages,
                })
            except Exception as exc:  # The parent preserves a per-case error and continues.
                conn.send({
                    "event": "result",
                    "status": "exception",
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "answer": "",
                    "mode": "exception",
                    "route_category": "",
                    "route_intent": "",
                    "confidence": 0.0,
                    "validation_ok": False,
                    "validation_errors": [type(exc).__name__],
                    "error": repr(exc),
                })
    except Exception as exc:
        try:
            conn.send({"event": "startup_error", "error": repr(exc)})
        except (BrokenPipeError, EOFError, OSError):
            pass


def _start_worker(environment: dict[str, str]) -> tuple[mp.Process, Any]:
    ctx = mp.get_context("spawn")
    parent, child = ctx.Pipe()
    process = ctx.Process(target=_worker_main, args=(child, environment))
    process.start()
    child.close()
    if not parent.poll(180):
        _stop_worker(process, parent)
        raise RuntimeError("worker startup exceeded 180 seconds")
    event = parent.recv()
    if event.get("event") != "ready":
        _stop_worker(process, parent)
        raise RuntimeError(f"worker startup failed: {event}")
    return process, parent


def _stop_worker(process: mp.Process | None, conn: Any | None) -> None:
    if process is not None and process.is_alive():
        try:
            _send_with_timeout(conn, None, timeout_sec=1.0)
        except (BrokenPipeError, EOFError, OSError, AttributeError):
            pass
        process.join(2)
    if process is not None and process.is_alive():
        process.terminate()
        process.join(8)
    if process is not None and process.is_alive():
        process.kill()
        process.join(8)
    if conn is not None:
        conn.close()


def _send_with_timeout(conn: Any, payload: Any, timeout_sec: float = 5.0) -> tuple[bool, Exception | None]:
    """Bound the parent-side Pipe send, which can block on a stuck reader."""
    mailbox: queue.Queue[tuple[str, Exception | None]] = queue.Queue(maxsize=1)

    def send_message() -> None:
        try:
            conn.send(payload)
            mailbox.put(("sent", None))
        except (BrokenPipeError, EOFError, OSError) as exc:
            mailbox.put(("error", exc))

    sender = threading.Thread(target=send_message, daemon=True)
    sender.start()
    sender.join(timeout_sec)
    if sender.is_alive():
        return False, TimeoutError(f"worker channel did not accept a task within {timeout_sec:.1f}s")
    outcome, error = mailbox.get_nowait()
    return outcome == "sent", error


def _receive(conn: Any, watchdog_sec: float) -> dict[str, Any]:
    started = time.perf_counter()
    mailbox: queue.Queue[tuple[str, Any]] = queue.Queue(maxsize=1)

    def receive_message() -> None:
        try:
            mailbox.put(("result", conn.recv()))
        except (EOFError, OSError) as exc:
            mailbox.put(("worker_crash", exc))

    # ``Connection.poll()`` may become true after only a message header is
    # available.  Receiving in this small reader thread lets the parent keep a
    # hard timeout around the complete payload, including deserialization.
    reader = threading.Thread(target=receive_message, daemon=True)
    reader.start()
    reader.join(watchdog_sec)
    if reader.is_alive():
        return {
            "status": "harness_timeout",
            "wall_sec": round(time.perf_counter() - started, 4),
            "right_censored": True,
            "answer": "",
            "mode": "harness_timeout",
            "route_category": "",
            "route_intent": "",
            "validation_ok": False,
            "validation_errors": ["watchdog_expired"],
            "error": "No result returned before evaluator watchdog; this is not a product answer.",
        }
    kind, payload = mailbox.get_nowait()
    if kind == "worker_crash":
        return {
            "status": "worker_crash",
            "wall_sec": round(time.perf_counter() - started, 4),
            "answer": "",
            "mode": "worker_crash",
            "route_category": "",
            "route_intent": "",
            "validation_ok": False,
            "validation_errors": ["worker_pipe_closed"],
        }
    event = payload
    if event.get("event") != "result":
        return {"status": "worker_error", "wall_sec": round(time.perf_counter() - started, 4), **event}
    return {key: value for key, value in event.items() if key != "event"}


def _warm_worker(conn: Any) -> dict[str, Any]:
    """Load lazy model/index state before scoring a user's benchmark case."""
    sent, error = _send_with_timeout(conn, {"question": "นายเป็นใคร", "locale": "th"})
    if not sent:
        return {
            "status": "worker_crash",
            "wall_sec": 0.0,
            "answer": "",
            "mode": "worker_crash",
            "route_category": "",
            "route_intent": "",
            "validation_ok": False,
            "validation_errors": [type(error).__name__ if error else "worker_send_failed"],
            "error": "Worker channel did not accept warmup task.",
        }
    return _receive(conn, 60.0)


def _as_list(value: Any) -> list[str]:
    if isinstance(value, (list, tuple)):
        return [str(item) for item in value if str(item)]
    return [str(value)] if value else []


def _thai_judge(case: dict[str, Any], result: dict[str, Any]) -> list[str]:
    answer = str(result.get("answer") or "").casefold()
    errors: list[str] = []
    expected_categories = _as_list(case.get("expected_category"))
    if expected_categories and str(result.get("route_category")) not in expected_categories:
        errors.append("category")
    prefixes = _as_list(case.get("expected_mode_prefix"))
    if prefixes and not any(str(result.get("mode") or "").startswith(prefix) for prefix in prefixes):
        errors.append("mode")
    for value in _as_list(case.get("must_contain")):
        if value.casefold() not in answer:
            errors.append("missing")
    alternatives = _as_list(case.get("must_contain_any"))
    if alternatives and not any(value.casefold() in answer for value in alternatives):
        errors.append("missing_any")
    for value in _as_list(case.get("must_not_contain")):
        if value and value.casefold() in answer:
            errors.append("forbidden")
    if not bool(result.get("validation_ok")):
        errors.append("validation")
    if str(result.get("status")) != "completed":
        errors.append(str(result.get("status")))
    return errors


def _english_judge(case: dict[str, Any], result: dict[str, Any]) -> list[str]:
    from app.core.locale import contains_thai_prose

    answer = str(result.get("answer") or "")
    folded = answer.casefold()
    errors: list[str] = []
    expected_values = _as_list(case.get("expected_categories") or case.get("expected_category"))
    if expected_values and str(result.get("route_category")) not in expected_values:
        errors.append("category")
    language = result.get("language") or {}
    if str(language.get("effective") or "") != "en":
        errors.append("effective_language_not_en")
    if contains_thai_prose(answer):
        errors.append("thai_prose_leak")
    if float(result.get("elapsed_sec") or result.get("wall_sec") or 0.0) >= float(case.get("latency_ceiling_sec") or 20.0):
        errors.append("latency")
    if str(result.get("mode")) == "pipeline:request_timeout_no_answer":
        errors.append("pipeline_timeout")
    if not bool(result.get("validation_ok")):
        errors.append("validation")
    for value in _as_list(case.get("must_contain")):
        if value.casefold() not in folded:
            errors.append("missing")
    alternatives = _as_list(case.get("must_contain_any"))
    if alternatives and not any(value.casefold() in folded for value in alternatives):
        errors.append("missing_any")
    for value in _as_list(case.get("must_not_contain")):
        if value.casefold() in folded:
            errors.append("forbidden")
    if str(result.get("status")) != "completed":
        errors.append(str(result.get("status")))
    return errors


def _tasks(suite: str, corpus: Path) -> list[dict[str, Any]]:
    rows = _read_jsonl(corpus)
    tasks: list[dict[str, Any]] = []
    for row in rows:
        question = str(row.get("question") or "").strip()
        locale = "th"
        if suite == "en":
            question = str(row.get("question_en") or "").strip()
            locale = "en"
        if question:
            tasks.append({"suite": suite, "case": row, "question": question, "locale": locale})
    return tasks


def _summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    latencies = [float(row.get("wall_sec") or 0.0) for row in rows]
    errors = Counter(error for row in rows for error in row.get("failures", []))
    return {
        "total": len(rows),
        "completed": sum(row.get("status") == "completed" for row in rows),
        "strict_pass": sum(not row.get("failures") for row in rows),
        "strict_pass_rate": round(sum(not row.get("failures") for row in rows) / len(rows), 6) if rows else None,
        "status_counts": dict(Counter(str(row.get("status")) for row in rows)),
        "mode_counts": dict(Counter(str(row.get("mode")) for row in rows)),
        "failure_types": dict(errors),
        "latency_sec": {
            "mean": round(sum(latencies) / len(latencies), 4) if latencies else 0.0,
            "p50": _percentile(latencies, 50),
            "p95": _percentile(latencies, 95),
            "p99": _percentile(latencies, 99),
            "max": round(max(latencies), 4) if latencies else 0.0,
            "over_10s": sum(value >= 10.0 for value in latencies),
            "over_20s": sum(value >= 20.0 for value in latencies),
        },
    }


def _run_suite(
    tasks: list[dict[str, Any]],
    out: Path,
    watchdog_sec: float,
    environment: dict[str, str],
    worker_recycle_cases: int,
    existing_rows: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    suite = tasks[0]["suite"] if tasks else "unknown"
    results: list[dict[str, Any]] = list(existing_rows or [])
    completed_ids = {str(row.get("id")) for row in results if row.get("id")}
    pending_tasks = [task for task in tasks if str(task["case"].get("id")) not in completed_ids]
    process: mp.Process | None = None
    conn: Any | None = None
    worker_number = 0
    cases_on_worker = 0
    output_path = out / f"{suite}_results.jsonl"
    warmup_path = out / f"{suite}_worker_warmups.jsonl"
    with output_path.open("a" if existing_rows else "w", encoding="utf-8") as handle:
        with warmup_path.open("a" if existing_rows else "w", encoding="utf-8") as warmups:
            try:
                for pending_index, task in enumerate(pending_tasks, 1):
                    index = len(results) + 1
                    if process is None:
                        worker_number += 1
                        process, conn = _start_worker(environment)
                        warmup = _warm_worker(conn)
                        warmups.write(json.dumps({"worker": worker_number, **warmup}, ensure_ascii=False) + "\n")
                        warmups.flush()
                        if warmup.get("status") != "completed":
                            _stop_worker(process, conn)
                            process = conn = None
                            raise RuntimeError(f"worker warmup failed: {warmup.get('status')}")
                        print(f"{suite}: worker {worker_number} ready; warmup={warmup.get('wall_sec', 0.0):.3f}s", flush=True)
                        cases_on_worker = 0
                    try:
                        sent, send_error = _send_with_timeout(
                            conn,
                            {"question": task["question"], "locale": task["locale"]},
                        )
                        if sent:
                            result = _receive(conn, watchdog_sec)
                        else:
                            result = {
                                "status": "worker_crash",
                                "wall_sec": 0.0,
                                "answer": "",
                                "mode": "worker_crash",
                                "route_category": "",
                                "route_intent": "",
                                "validation_ok": False,
                                "validation_errors": [type(send_error).__name__ if send_error else "worker_send_failed"],
                                "error": "Worker channel did not accept the task before send deadline.",
                            }
                    except (BrokenPipeError, EOFError, OSError) as exc:
                        result = {
                        "status": "worker_crash",
                        "wall_sec": 0.0,
                        "answer": "",
                        "mode": "worker_crash",
                        "route_category": "",
                        "route_intent": "",
                        "validation_ok": False,
                        "validation_errors": [type(exc).__name__],
                        "error": "Worker channel closed before the request could be sent.",
                        }
                    failures = _thai_judge(task["case"], result) if suite == "th" else _english_judge(task["case"], result)
                    record = {
                    "id": task["case"].get("id"),
                    "suite": suite,
                    "group": task["case"].get("group"),
                    "question": task["question"],
                    "expected_category": task["case"].get("expected_category") or task["case"].get("expected_categories"),
                    "failures": failures,
                    "strict_pass": not failures,
                    "worker": worker_number,
                        **result,
                    }
                    results.append(record)
                    cases_on_worker += 1
                    handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
                    handle.flush()
                    # Persist the checkpoint with every durable raw row.  A
                    # manual stop or worker crash must never leave progress
                    # reporting 25 cases behind the append-only result log.
                    _write_json(out / f"{suite}_progress.json", {
                        "completed": len(results),
                        "total": len(tasks),
                        "summary": _summarize(results),
                        "finished": len(results) == len(tasks),
                    })
                    if record["status"] in {"harness_timeout", "worker_crash", "worker_error"}:
                        print(f"{suite}: {record['id']} {record['status']}; replacing worker", flush=True)
                        _stop_worker(process, conn)
                        process = conn = None
                        cases_on_worker = 0
                    elif worker_recycle_cases and cases_on_worker >= worker_recycle_cases:
                        print(
                            f"{suite}: recycling worker {worker_number} after {cases_on_worker} cases",
                            flush=True,
                        )
                        _stop_worker(process, conn)
                        process = conn = None
                        cases_on_worker = 0
                    if index % 25 == 0 or pending_index == len(pending_tasks):
                        _write_json(out / f"{suite}_progress.json", {"completed": len(results), "total": len(tasks), "summary": _summarize(results)})
                        print(f"{suite}: progress {len(results)}/{len(tasks)} pass={sum(not row['failures'] for row in results)}", flush=True)
            finally:
                _stop_worker(process, conn)
                _write_json(out / f"{suite}_progress.json", {
                    "completed": len(results),
                    "total": len(tasks),
                    "summary": _summarize(results),
                    "finished": len(results) == len(tasks),
                })
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--suites", default="th,en", help="Comma-separated: th,en")
    parser.add_argument("--watchdog-sec", type=float, default=25.0)
    parser.add_argument(
        "--worker-recycle-cases",
        type=int,
        default=100,
        help="Proactively replace the evaluator worker after this many cases; 0 disables recycling.",
    )
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--thai-corpus", type=Path, default=THAI_CORPUS)
    parser.add_argument("--english-corpus", type=Path, default=ENGLISH_CORPUS)
    parser.add_argument("--resume", action="store_true", help="Append only missing case IDs to an interrupted run directory.")
    args = parser.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    out = args.output_dir.resolve()
    if out.exists() and any(out.iterdir()) and not args.resume:
        raise SystemExit("Use a new empty output directory; raw results are never overwritten.")
    out.mkdir(parents=True, exist_ok=True)
    environment = _runtime_environment()
    selected = [value.strip() for value in args.suites.split(",") if value.strip()]
    if any(value not in {"th", "en"} for value in selected) or not selected:
        raise SystemExit("--suites accepts only th,en")
    sources = {"th": args.thai_corpus, "en": args.english_corpus}
    for suite in selected:
        copied = out / sources[suite].name
        if not copied.exists():
            shutil.copy2(sources[suite], copied)
    manifest = {
        "started_at": datetime.now().astimezone().isoformat(),
        "profile": "current_local_web_rag_assist_draft_preview",
        "model": MODEL,
        "watchdog_sec": args.watchdog_sec,
        "suites": selected,
        "environment": environment,
        "warning": "The evaluator watchdog protects only the test worker. A harness timeout is not a chatbot response.",
    }
    if not (out / "manifest.json").exists():
        _write_json(out / "manifest.json", manifest)
    elif args.resume:
        _write_json(out / f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", manifest)
    all_rows: dict[str, list[dict[str, Any]]] = {}
    for suite in selected:
        tasks = _tasks(suite, sources[suite])
        if args.limit:
            tasks = tasks[:args.limit]
        print(f"{suite}: starting {len(tasks)} cases", flush=True)
        existing_path = out / f"{suite}_results.jsonl"
        existing_rows = _read_jsonl(existing_path) if args.resume and existing_path.exists() else []
        all_rows[suite] = _run_suite(
            tasks,
            out,
            args.watchdog_sec,
            environment,
            max(0, args.worker_recycle_cases),
            existing_rows,
        )
    summary = {
        "finished_at": datetime.now().astimezone().isoformat(),
        "suites": {suite: _summarize(rows) for suite, rows in all_rows.items()},
        "comparison_limits": [
            "Thai and English corpora use their own existing answer contracts; strict-pass rates are not a translation-quality A/B score.",
            "English Shadow is machine-translated test input and not approved public English knowledge.",
            "This is serial in-process evaluation with no browser, HTTP queue, or concurrent-user latency.",
        ],
    }
    _write_json(out / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())
