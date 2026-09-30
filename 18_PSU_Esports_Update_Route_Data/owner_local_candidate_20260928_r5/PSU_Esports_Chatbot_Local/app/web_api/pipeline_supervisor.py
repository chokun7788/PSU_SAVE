from __future__ import annotations

"""Crash-contained process workers for the answer pipeline.

This is intentionally a small standard-library implementation.  The web
process owns HTTP, session locks, and logs; child workers own only pipeline
execution.  A timed-out or crashed child can therefore be replaced without
restarting the web API or leaking a semaphore in the request handler.
"""

import multiprocessing as mp
import os
import queue
import threading
import time
import uuid
from dataclasses import dataclass
from typing import Any

from app.pipeline.performance_trace import (
    ParentPerformanceLogger,
    emit_performance_event,
    performance_event_context,
)


def _truthy(value: str | None, *, default: bool = False) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def worker_supervisor_enabled() -> bool:
    return _truthy(os.getenv("PSU_PIPELINE_WORKER_SUPERVISOR"), default=False)


def worker_count() -> int:
    try:
        return max(1, min(8, int(os.getenv("PSU_PIPELINE_WORKERS", "4"))))
    except ValueError:
        return 4


def worker_recycle_requests() -> int:
    try:
        return max(1, int(os.getenv("PSU_PIPELINE_WORKER_RECYCLE_REQUESTS", "500")))
    except ValueError:
        return 500


def worker_queue_wait_sec() -> float:
    """Bound admission wait for the single local-GPU worker.

    A short queue absorbs a burst of quick structured requests.  It is part
    of the caller's deadline, never an unbounded hidden queue for LLM work.
    """
    try:
        return max(0.0, min(5.0, float(os.getenv("PSU_PIPELINE_WORKER_QUEUE_WAIT_SEC", "3.0"))))
    except ValueError:
        return 3.0


def worker_startup_timeout_sec() -> float:
    try:
        return max(1.0, min(60.0, float(os.getenv("PSU_PIPELINE_WORKER_STARTUP_TIMEOUT_SEC", "15"))))
    except ValueError:
        return 15.0


def worker_semantic_warmup_enabled() -> bool:
    """Warm the child embedding client before accepting the first RAG request.

    A single local worker is the normal GPU profile.  In that profile, warming
    its process-local client during startup prevents the first semantic request
    from paying model/client initialization time.  Multiple workers remain
    opt-in because warming many embedding clients concurrently can contend for
    the same local runtime.
    """
    explicit = os.getenv("PSU_PIPELINE_WORKER_WARMUP_EMBEDDING")
    if explicit is not None:
        return _truthy(explicit)
    return worker_count() == 1 and _truthy(os.getenv("PSU_SEMANTIC_RETRIEVAL"), default=False)


def worker_llm_warmup_enabled() -> bool:
    """Load the one local LLM before admitting requests in the local profile.

    This moves a model-load pause to controlled server startup instead of
    letting an otherwise simple first question wait behind it.  It remains
    opt-in for multi-worker deployments to avoid duplicated GPU residency.
    """
    explicit = os.getenv("PSU_PIPELINE_WORKER_WARMUP_LLM")
    if explicit is not None:
        return _truthy(explicit)
    return (
        worker_count() == 1
        and _truthy(os.getenv("PSU_LOCAL_LLM_ASSIST_ENABLED"), default=False)
    )


def _worker_exit_diagnostics(
    exit_code: int | None,
    *,
    timed_out: bool,
    worker_error_type: str = "",
) -> dict[str, Any]:
    """Classify the observable outcome without claiming an unproven root cause."""
    if timed_out:
        exit_type = "hard_timeout_termination"
    elif worker_error_type:
        exit_type = "application_exception"
    elif exit_code in {-1073741819, 0xC0000005}:
        exit_type = "native_access_violation"
    elif exit_code is None:
        exit_type = "unknown_worker_exit"
    elif exit_code == 0:
        exit_type = "unexpected_clean_exit"
    else:
        exit_type = "unknown_worker_exit"
    return {
        "exit_type": exit_type,
        "exit_code": exit_code,
        "worker_error_type": worker_error_type,
        "timed_out": timed_out,
    }


def _worker_main(requests: Any, results: Any, events: Any, ready: Any, run_id: str, worker_id: int) -> None:
    # Imports live here so Windows spawn starts cleanly and native model state
    # stays contained in the worker process.
    from app.runtime.pipeline_answer import answer_question_pipeline_debug

    # Warm only local/deterministic indexes here.  Loading the Local LLM or
    # embedding model in every worker would contend for GPU memory; those are
    # still health-gated at call time.  These indexes otherwise create an
    # avoidable first-request tail spike on Windows.
    try:
        from app.pipeline.entity_resolver import _game_resolver_index
        from app.pipeline.vector_retrieval import load_vector_index

        _game_resolver_index()
        load_vector_index()
    except Exception:
        # The worker can still run deterministic paths built from source data.
        # Do not expose warmup internals or user data in the performance trace.
        pass

    if worker_semantic_warmup_enabled():
        try:
            from app.pipeline.semantic_embeddings import warm_semantic_embedding_model

            warm_semantic_embedding_model()
        except Exception:
            # The request pipeline still has its normal bounded retrieval
            # fallback if the local embedding runtime is unavailable at boot.
            pass

    if worker_llm_warmup_enabled():
        try:
            from app.pipeline.llm_health import preflight_ollama

            model = (
                os.getenv("PSU_INTENT_LLM_MODEL")
                or os.getenv("PSU_CHATBOT_OLLAMA_MODEL")
                or "scb10x/typhoon2.5-qwen3-4b"
            )
            preflight_ollama(model=model, kind="worker_startup_warmup", timeout_sec=45.0)
        except Exception:
            # Health gates still protect actual calls if the local runtime is
            # unavailable.  Startup must remain recoverable.
            pass

    # The parent only accepts user work after this point during normal server
    # startup.  That keeps process-spawn/import time out of the first request.
    ready.set()

    while True:
        task = requests.get()
        if task is None:
            return
        task_id = str(task.get("task_id") or "")
        request_id = str(task.get("request_id") or task_id)
        with performance_event_context(events, run_id=run_id, request_id=request_id, worker_id=worker_id):
            try:
                result = answer_question_pipeline_debug(
                    str(task["question"]),
                    experimental_rag_fallback=bool(task.get("experimental_rag_fallback", False)),
                    experimental_allow_llm=bool(task.get("experimental_allow_llm", False)),
                    global_timeout_sec=float(task.get("pipeline_timeout_sec", 9.0)),
                    locale=str(task.get("locale") or "auto"),
                    locale_decision=task.get("locale_decision"),
                )
                emit_performance_event("request_finished", "pipeline", status="completed", attributes={"mode": result.mode})
                results.put({"task_id": task_id, "status": "ok", "result": result})
            except BaseException as exc:  # Worker boundary: report then let parent decide replacement.
                emit_performance_event("stage_failed", "pipeline", status=type(exc).__name__)
                results.put({"task_id": task_id, "status": "error", "error": repr(exc), "error_type": type(exc).__name__})


@dataclass
class SupervisedCall:
    status: str
    result: Any | None = None
    worker_id: int = -1
    error: str = ""
    elapsed_sec: float = 0.0
    diagnostics: dict[str, Any] | None = None


@dataclass
class _WorkerSlot:
    worker_id: int
    requests: Any
    results: Any
    ready: Any
    process: mp.Process
    lock: threading.Lock
    completed_requests: int = 0


class PipelineWorkerSupervisor:
    def __init__(self, *, workers: int | None = None) -> None:
        self._ctx = mp.get_context("spawn")
        self._count = workers if workers is not None else worker_count()
        self._slots: list[_WorkerSlot] = []
        self._guard = threading.Lock()
        self._cursor = 0
        self._started = False
        self._events = self._ctx.Queue(maxsize=4096)
        self._performance = ParentPerformanceLogger(self._events)

    def start(self) -> None:
        with self._guard:
            if self._started:
                return
            self._performance.start()
            self._slots = [self._new_slot(index) for index in range(self._count)]
            self._started = True
            # Startup happens before ThreadingHTTPServer begins accepting
            # requests.  A failed worker is left observable and will be
            # replaced on demand, rather than stalling the first user request.
            for slot in self._slots:
                slot.ready.wait(timeout=worker_startup_timeout_sec())

    def shutdown(self) -> None:
        with self._guard:
            for slot in self._slots:
                self._stop_slot(slot)
            self._slots.clear()
            self._started = False
            self._performance.stop()

    def health(self) -> dict[str, Any]:
        with self._guard:
            return {
                "enabled": True,
                "started": self._started,
                "worker_count": len(self._slots),
                "workers": [
                    {
                        "worker_id": slot.worker_id,
                        "pid": slot.process.pid,
                        "alive": slot.process.is_alive(),
                        "ready": slot.ready.is_set(),
                        "completed_requests": slot.completed_requests,
                        "busy": slot.lock.locked(),
                    }
                    for slot in self._slots
                ],
                "performance": self._performance.snapshot(),
            }

    def answer(
        self,
        question: str,
        *,
        timeout_sec: float,
        experimental_rag_fallback: bool,
        experimental_allow_llm: bool,
        request_id: str = "",
        locale: str = "auto",
        locale_decision: dict[str, Any] | None = None,
    ) -> SupervisedCall:
        started = time.perf_counter()
        self.start()
        slot = self._acquire_slot(wait_sec=min(worker_queue_wait_sec(), timeout_sec))
        if slot is None:
            return SupervisedCall("busy", error="no_pipeline_worker_available", elapsed_sec=time.perf_counter() - started)
        try:
            queue_wait_sec = time.perf_counter() - started
            remaining_timeout_sec = max(0.05, timeout_sec - queue_wait_sec)
            if not slot.process.is_alive():
                diagnostics = _worker_exit_diagnostics(slot.process.exitcode, timed_out=False)
                self._replace_slot(slot)
                self._performance.emit_parent("worker_exit", "pipeline", request_id=request_id, worker_id=slot.worker_id, status=diagnostics["exit_type"], attributes=diagnostics)
                return SupervisedCall("restarting", worker_id=slot.worker_id, error="worker_not_alive", elapsed_sec=time.perf_counter() - started, diagnostics=diagnostics)
            if not slot.ready.is_set():
                diagnostics = _worker_exit_diagnostics(slot.process.exitcode, timed_out=False)
                diagnostics["exit_type"] = "worker_starting"
                self._performance.emit_parent("worker_replaced", "pipeline", request_id=request_id, worker_id=slot.worker_id, status="starting", attributes=diagnostics)
                return SupervisedCall("restarting", worker_id=slot.worker_id, error="worker_not_ready", elapsed_sec=time.perf_counter() - started, diagnostics=diagnostics)
            task_id = uuid.uuid4().hex
            self._performance.emit_parent(
                "worker_assigned",
                "pipeline",
                request_id=request_id or task_id,
                worker_id=slot.worker_id,
                status="started",
                attributes={"queue_wait_sec": round(queue_wait_sec, 4)},
            )
            try:
                # A frozen child must not make the parent block while trying
                # to enqueue a second task. The per-slot lock normally makes
                # this impossible, but the bounded operation is the final
                # containment boundary for a broken queue/worker pair.
                slot.requests.put({
                    "task_id": task_id,
                    "request_id": request_id or task_id,
                    "question": question,
                    "experimental_rag_fallback": experimental_rag_fallback,
                    "experimental_allow_llm": experimental_allow_llm,
                    "locale": locale,
                    "locale_decision": locale_decision or {},
                    # The child must respect queue time already consumed in
                    # the parent; otherwise a burst could exceed the HTTP SLA.
                    "pipeline_timeout_sec": max(0.1, remaining_timeout_sec - 0.15),
                }, timeout=min(0.25, max(0.05, remaining_timeout_sec * 0.1)))
            except queue.Full:
                diagnostics = _worker_exit_diagnostics(slot.process.exitcode, timed_out=True)
                diagnostics["exit_type"] = "worker_queue_stalled"
                self._replace_slot(slot)
                self._performance.emit_parent(
                    "worker_timeout",
                    "pipeline",
                    request_id=request_id or task_id,
                    worker_id=slot.worker_id,
                    status="worker_queue_stalled",
                    attributes=diagnostics,
                )
                return SupervisedCall(
                    "timeout",
                    worker_id=slot.worker_id,
                    error="pipeline_worker_queue_stalled",
                    elapsed_sec=time.perf_counter() - started,
                    diagnostics=diagnostics,
                )
            try:
                event = slot.results.get(timeout=max(0.05, remaining_timeout_sec))
            except queue.Empty:
                diagnostics = _worker_exit_diagnostics(slot.process.exitcode, timed_out=True)
                self._replace_slot(slot)
                self._performance.emit_parent("worker_timeout", "pipeline", request_id=request_id or task_id, worker_id=slot.worker_id, status=diagnostics["exit_type"], attributes=diagnostics)
                self._performance.emit_parent("worker_replaced", "pipeline", request_id=request_id or task_id, worker_id=slot.worker_id, status="restarting")
                return SupervisedCall("timeout", worker_id=slot.worker_id, error="pipeline_worker_timeout", elapsed_sec=time.perf_counter() - started, diagnostics=diagnostics)
            if event.get("task_id") != task_id:
                self._replace_slot(slot)
                return SupervisedCall("restarting", worker_id=slot.worker_id, error="worker_result_protocol_mismatch", elapsed_sec=time.perf_counter() - started)
            if event.get("status") != "ok":
                diagnostics = _worker_exit_diagnostics(slot.process.exitcode, timed_out=False, worker_error_type=str(event.get("error_type") or ""))
                self._replace_slot(slot)
                self._performance.emit_parent("worker_exit", "pipeline", request_id=request_id or task_id, worker_id=slot.worker_id, status=diagnostics["exit_type"], attributes=diagnostics)
                return SupervisedCall("restarting", worker_id=slot.worker_id, error=str(event.get("error") or "worker_error"), elapsed_sec=time.perf_counter() - started, diagnostics=diagnostics)
            slot.completed_requests += 1
            result = event.get("result")
            if slot.completed_requests >= worker_recycle_requests():
                self._replace_slot(slot)
            self._performance.emit_parent("worker_result", "pipeline", request_id=request_id or task_id, worker_id=slot.worker_id, status="completed", attributes={"elapsed_ms": round((time.perf_counter() - started) * 1000, 3)})
            return SupervisedCall("ok", result=result, worker_id=slot.worker_id, elapsed_sec=time.perf_counter() - started)
        finally:
            slot.lock.release()

    def _new_slot(self, worker_id: int) -> _WorkerSlot:
        requests = self._ctx.Queue(maxsize=1)
        results = self._ctx.Queue(maxsize=1)
        ready = self._ctx.Event()
        process = self._ctx.Process(
            target=_worker_main,
            args=(requests, results, self._events, ready, self._performance.run_id, worker_id),
            name=f"psu-pipeline-worker-{worker_id}",
            daemon=True,
        )
        process.start()
        return _WorkerSlot(worker_id, requests, results, ready, process, threading.Lock())

    def _stop_slot(self, slot: _WorkerSlot) -> None:
        if slot.process.is_alive():
            try:
                slot.requests.put_nowait(None)
                slot.process.join(timeout=0.2)
            except Exception:
                pass
        if slot.process.is_alive():
            slot.process.terminate()
            slot.process.join(timeout=1.0)
        if slot.process.is_alive():
            # ``terminate`` should be sufficient on Windows, but preserve a
            # final hard stop so a non-returning child cannot keep the API
            # permanently degraded.
            slot.process.kill()
            slot.process.join(timeout=1.0)

    def _replace_slot(self, slot: _WorkerSlot) -> None:
        with self._guard:
            self._stop_slot(slot)
            replacement = self._new_slot(slot.worker_id)
            for index, current in enumerate(self._slots):
                if current is slot:
                    self._slots[index] = replacement
                    break

    def _acquire_slot(self, *, wait_sec: float = 0.0) -> _WorkerSlot | None:
        deadline = time.perf_counter() + max(0.0, wait_sec)
        while True:
            with self._guard:
                slots = list(self._slots)
                start = self._cursor
                self._cursor = (self._cursor + 1) % max(1, len(slots))
            for offset in range(len(slots)):
                slot = slots[(start + offset) % len(slots)]
                if not slot.ready.is_set():
                    continue
                if slot.lock.acquire(blocking=False):
                    return slot
            remaining = deadline - time.perf_counter()
            if remaining <= 0:
                return None
            # Do not spin while another request is using the only local model.
            time.sleep(min(0.01, remaining))
