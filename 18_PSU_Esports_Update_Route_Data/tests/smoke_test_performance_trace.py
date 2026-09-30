from __future__ import annotations

"""Smoke checks for crash-safe performance logs without conversation content."""

import json
import queue
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.performance_trace import (  # noqa: E402
    ObservedTraceList,
    ParentPerformanceLogger,
    performance_event_context,
)
from app.pipeline.schemas import PipelineTrace  # noqa: E402
from app.web_api.pipeline_supervisor import _worker_exit_diagnostics  # noqa: E402


def test_trace_log_excludes_raw_conversation_content() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "performance.jsonl"
        events: queue.Queue[dict[str, object]] = queue.Queue()
        logger = ParentPerformanceLogger(events, run_id="trace-smoke", path=path)
        logger.start()
        with performance_event_context(events, run_id="trace-smoke", request_id="req-1", worker_id=0):
            traces = ObservedTraceList()
            traces.append(PipelineTrace(
                "retrieval",
                "completed",
                1.0,
                metadata={
                    "parts": ["PRIVATE QUESTION"],
                    "answer": "PRIVATE ANSWER",
                    "candidate_count": 4,
                    "route_category": "games",
                },
            ))
        time.sleep(0.1)
        logger.stop()
        raw = path.read_text(encoding="utf-8")
        assert "PRIVATE QUESTION" not in raw
        assert "PRIVATE ANSWER" not in raw
        records = [json.loads(line) for line in raw.splitlines()]
        retrieval = next(record for record in records if record["stage"] == "retrieval")
        attributes = retrieval["attributes"]
        assert attributes["confidence"] == 1.0
        assert attributes["candidate_count"] == 4
        assert attributes["route_category"] == "games"
        assert "parts" not in attributes
        assert "answer" not in attributes


def test_worker_exit_diagnostics_are_explicit() -> None:
    assert _worker_exit_diagnostics(-1073741819, timed_out=False)["exit_type"] == "native_access_violation"
    assert _worker_exit_diagnostics(None, timed_out=True)["exit_type"] == "hard_timeout_termination"
    assert _worker_exit_diagnostics(1, timed_out=False, worker_error_type="ValueError")["exit_type"] == "application_exception"


if __name__ == "__main__":
    test_trace_log_excludes_raw_conversation_content()
    print("OK performance trace excludes raw conversation content")
    test_worker_exit_diagnostics_are_explicit()
    print("OK worker exit diagnostics classify observable outcomes")
    print("PERFORMANCE TRACE SMOKE TEST OK")
