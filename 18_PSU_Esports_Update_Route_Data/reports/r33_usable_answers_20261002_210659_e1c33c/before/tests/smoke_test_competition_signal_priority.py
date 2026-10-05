from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def main() -> int:
    for question in (
        "VALORANT ใช้ผู้เล่นกี่คน",
        "แข่ง VALORANT มาสายจะโดนอะไร",
        "เกมหลุดระหว่างแข่งต้องทำอย่างไร",
        "การแข่งขันมีตัวสำรองได้ไหม",
    ):
        result = answer_question_pipeline_debug(
            question,
            experimental_rag_fallback=True,
            experimental_allow_llm=False,
            global_timeout_sec=20.0,
        )
        assert result.route.category == "competition_rules", (question, result.route, result.answer)
        assert result.mode != "pipeline:structured_game_detail", (question, result.mode, result.answer)
    print("OK competition signals outrank a named game-detail route")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
