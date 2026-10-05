from __future__ import annotations

import os
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main() -> int:
    os.environ["PSU_BILINGUAL_EN_ENABLED"] = "1"
    from app.runtime.pipeline_answer import answer_question_pipeline_debug  # noqa: E402

    result = answer_question_pipeline_debug(
        "What are the controls for Pokémon Champions?",
        locale="en",
        experimental_allow_llm=False,
        experimental_rag_fallback=True,
        global_timeout_sec=20.0,
    )
    assert result.route.category == "games", (result.route, result.answer)
    assert result.mode == "pipeline:game_controls_mapping_pending_en", (result.mode, result.answer)
    assert "will not guess the controls" in result.answer
    print("OK accented English game title does not collide with Monday routing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
