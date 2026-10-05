from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ["PSU_BILINGUAL_EN_ENABLED"] = "1"

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def _answer(question: str):
    return answer_question_pipeline_debug(
        question,
        locale="en",
        experimental_allow_llm=False,
        experimental_rag_fallback=True,
        global_timeout_sec=10.0,
    )


def main() -> int:
    booking = _answer("How do I make a booking?")
    assert booking.mode == "pipeline:rule_en"
    assert "Booking steps:" in booking.answer
    assert booking.answer.count("•") == 6

    studio_rules = _answer("What are the studio rules?")
    assert studio_rules.route.category == "rules", studio_rules
    assert studio_rules.mode == "pipeline:rule_en", studio_rules
    assert "Key studio rules:" in studio_rules.answer
    assert "competition rules" not in studio_rules.answer.casefold()

    manager = _answer("Who is the manager?")
    assert manager.route.category == "overview"
    assert manager.mode == "pipeline:structured_members_source_th"
    assert "Official Thai source member record" in manager.answer
    assert "ผู้จัดการ" in manager.answer
    assert "https://esports.phuket.psu.ac.th/about-us/Members" in manager.answer

    print("ENGLISH FORMAT PARITY FIXES SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
