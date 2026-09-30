from __future__ import annotations

import sys
import time
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.web_api.pipeline_supervisor import PipelineWorkerSupervisor  # noqa: E402


def main() -> int:
    supervisor = PipelineWorkerSupervisor(workers=1)
    try:
        supervisor.start()
        timed_out = supervisor.answer(
            "มีเกมอะไรบ้าง",
            # The parent has a 50 ms minimum receive wait. This is deliberately
            # below an ordinary pipeline response so the recovery path is real.
            timeout_sec=0.01,
            experimental_rag_fallback=False,
            experimental_allow_llm=False,
        )
        assert timed_out.status == "timeout", timed_out
        assert timed_out.diagnostics and timed_out.diagnostics["exit_type"] in {
            "hard_timeout_termination",
            "worker_queue_stalled",
        }

        for _ in range(120):
            health = supervisor.health()
            if health["workers"][0]["alive"] and health["workers"][0]["ready"]:
                break
            time.sleep(0.1)
        else:
            raise AssertionError("replacement worker did not become ready")

        recovered = supervisor.answer(
            "สมาชิกทีมมีใครบ้าง",
            timeout_sec=5.0,
            experimental_rag_fallback=False,
            experimental_allow_llm=False,
        )
        assert recovered.status == "ok", recovered
        assert recovered.result is not None
        assert recovered.result.route.category == "overview"
        print("OK timed-out worker is replaced and the next request succeeds")
        return 0
    finally:
        supervisor.shutdown()


if __name__ == "__main__":
    raise SystemExit(main())
