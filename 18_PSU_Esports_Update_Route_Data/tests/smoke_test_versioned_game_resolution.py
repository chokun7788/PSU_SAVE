from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.entity_resolver import resolve_game_entity  # noqa: E402


def main() -> int:
    versioned = resolve_game_entity("Overcooked! 2 ปุ่มอะไร", operation="controls")
    assert versioned.status == "exact", versioned.as_dict()
    assert versioned.top_candidate is not None
    assert "overcooked" in versioned.top_candidate.title.lower() and "2" in versioned.top_candidate.title, versioned.as_dict()

    family = resolve_game_entity("โอเวอคุก ปุ่มอะไร", operation="controls")
    assert family.status == "ambiguous", family.as_dict()

    original = resolve_game_entity("Overcooked! เล่นได้ที่เครื่องไหน", operation="availability")
    assert original.status == "exact", original.as_dict()
    assert original.top_candidate is not None and original.top_candidate.title == "Overcooked!", original.as_dict()

    answer = answer_question_pipeline_debug(
        "Overcooked! 2 ปุ่มอะไร",
        experimental_rag_fallback=True,
        experimental_allow_llm=False,
        global_timeout_sec=20.0,
    )
    assert answer.mode != "pipeline:ambiguity_clarification", answer.answer
    assert "Overcooked! 2" in answer.answer, answer.answer
    print("OK explicit version beats shared nickname; generic nickname remains ambiguous")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
