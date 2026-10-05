from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.warmup import warm_pipeline_caches  # noqa: E402


def test_pipeline_warmup() -> None:
    result = warm_pipeline_caches()
    assert result.ok, result.errors
    assert "game_title_aliases" in result.warmed
    assert "structured_tools" in result.warmed
    assert "routing_data" in result.warmed
    assert "retrieval_data" in result.warmed
    assert "probe_queries" in result.warmed

    answer = answer_question_pipeline_debug(
        "อุปกรณ์ไหนเกมเยอะสุด",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert answer.mode == "pipeline:structured_game_zone_ranking", answer.mode
    assert answer.elapsed < 1.0, answer.elapsed


if __name__ == "__main__":
    test_pipeline_warmup()
    print("OK pipeline warmup")
