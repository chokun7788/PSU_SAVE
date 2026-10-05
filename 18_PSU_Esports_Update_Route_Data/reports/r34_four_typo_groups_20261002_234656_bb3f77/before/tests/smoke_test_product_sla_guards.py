from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.request_deadline import (  # noqa: E402
    current_deadline,
    deadline_metadata,
    request_deadline,
    timeout_for_call,
)
from app.web_api.server import _ACTIVE_REQUESTS, _session_lock  # noqa: E402


def test_nested_pipeline_keeps_outer_product_deadline() -> None:
    with request_deadline(2.0) as outer:
        with request_deadline() as inner:
            assert inner is outer
            assert current_deadline() is outer
            metadata = deadline_metadata()
            assert metadata["global_timeout_sec"] == 2.0
            assert metadata["finalizer_reserve_sec"] >= 0.0
            assert metadata["work_remaining_sec"] <= metadata["global_remaining_sec"]


def test_llm_call_timeout_leaves_finalizer_reserve() -> None:
    previous = os.environ.get("PSU_PIPELINE_FINALIZER_RESERVE_SEC")
    os.environ["PSU_PIPELINE_FINALIZER_RESERVE_SEC"] = "0.75"
    try:
        with request_deadline(2.0):
            timeout = timeout_for_call(10.0)
    finally:
        if previous is None:
            os.environ.pop("PSU_PIPELINE_FINALIZER_RESERVE_SEC", None)
        else:
            os.environ["PSU_PIPELINE_FINALIZER_RESERVE_SEC"] = previous

    assert 0.05 < timeout <= 1.25


def test_session_lock_is_shared_and_active_request_slot_is_bounded() -> None:
    first = _session_lock("product-sla-test-session")
    second = _session_lock("product-sla-test-session")
    assert first is second

    assert _ACTIVE_REQUESTS.acquire(blocking=False) is True
    _ACTIVE_REQUESTS.release()


if __name__ == "__main__":
    test_nested_pipeline_keeps_outer_product_deadline()
    test_llm_call_timeout_leaves_finalizer_reserve()
    test_session_lock_is_shared_and_active_request_slot_is_bounded()
    print("OK product SLA guards")
