from __future__ import annotations

import os
import sys
import threading
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.llm_health import llm_call_allowed, release_llm_slot  # noqa: E402


def main() -> int:
    os.environ["PSU_LLM_MAX_CONCURRENCY"] = "1"
    os.environ["PSU_LLM_CONCURRENCY_WAIT_SEC"] = "0"
    first_allowed, _first = llm_call_allowed("smoke_first", "smoke-model")
    assert first_allowed is True
    result: dict[str, object] = {}

    def try_second() -> None:
        result["value"] = llm_call_allowed("smoke_second", "smoke-model")

    worker = threading.Thread(target=try_second)
    worker.start()
    worker.join(timeout=2)
    assert worker.is_alive() is False
    second_allowed, second_metadata = result["value"]  # type: ignore[misc]
    assert second_allowed is False
    assert second_metadata["llm_concurrency_allowed"] is False

    release_llm_slot()
    third_allowed, _third = llm_call_allowed("smoke_third", "smoke-model")
    assert third_allowed is True
    release_llm_slot()
    print("OK LLM concurrency guard")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

