from __future__ import annotations

import sys
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
        before = supervisor.health()
        assert before["started"] and before["worker_count"] == 1
        call = supervisor.answer(
            "สมาชิกทีมมีใครบ้าง",
            timeout_sec=5.0,
            experimental_rag_fallback=False,
            experimental_allow_llm=False,
        )
        assert call.status == "ok", call.error
        assert call.result is not None
        assert call.result.route.category == "overview"
        assert call.result.elapsed < 5.0
        import time

        time.sleep(0.2)
        performance = supervisor.health()["performance"]
        assert performance["events_written"] > 0
        assert Path(performance["path"]).exists()
        print("OK supervised worker returns a pipeline result with parent-owned performance events")
    finally:
        supervisor.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
