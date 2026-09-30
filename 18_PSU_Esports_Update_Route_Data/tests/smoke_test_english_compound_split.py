from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ["PSU_BILINGUAL_EN_ENABLED"] = "1"

from app.pipeline.engine import _split_multi_question, answer_question_pipeline_debug  # noqa: E402


def _answer(question: str):
    return answer_question_pipeline_debug(
        question,
        locale="en",
        experimental_allow_llm=False,
        experimental_rag_fallback=True,
        global_timeout_sec=20.0,
    )


def main() -> int:
    split = _split_multi_question("How much does a PC cost and how do I book it?")
    assert split == ["How much does a PC cost", "how do I book PC"], split

    combined = _answer("How much does a PC cost and how do I book it?")
    assert combined.route.category == "multi_question", combined.route
    assert "Question 1:" in combined.answer
    assert "PC - 1 hour" in combined.answer
    assert "Question 2:" in combined.answer
    assert "Booking steps:" in combined.answer

    independent = _answer("What games do you have and what is the PS5 price?")
    assert independent.route.category == "multi_question", independent.route
    assert "There are currently 42 verified games available." in independent.answer
    assert "PlayStation 5 - 1 hour" in independent.answer

    single = _split_multi_question("Do you have Call of Duty and Fortnite?")
    assert single == ["Do you have Call of Duty and Fortnite?"], single
    print("OK English compound requests split before deterministic handlers without splitting game lists")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
