import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ["PSU_BILINGUAL_EN_ENABLED"] = "1"
os.environ["PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW"] = "1"
os.environ["PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH"] = str(
    ROOT / "data" / "locales" / "en" / "localization_review_drafts_competition_20260921_repaired.jsonl"
)

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
    game = _answer("Tell me about God of War Ragnarök")
    assert game.mode == "pipeline:structured_game_detail_en", game
    assert "action-adventure" in game.answer.casefold(), game.answer

    competition = _answer("What are the ROV competition rules?")
    assert competition.mode == "pipeline:structured_competition_rules_en", competition
    assert "competition" in competition.answer.casefold(), competition.answer
    assert "กฎ" not in competition.answer, competition.answer

    overtime = _answer("What is the Counter-Strike 2 overtime format and starting money?")
    assert overtime.mode == "pipeline:structured_competition_rules_en", overtime
    assert "starting money is $10,000" in overtime.answer, overtime.answer

    venue = _answer("Where is the RoV competition venue?")
    assert venue.mode == "pipeline:structured_competition_rules_en", venue
    assert "Building 5, Floor 1" in venue.answer, venue.answer

    bug = _answer("What is the VALORANT rule for a Game Breaking Bug?")
    assert bug.mode == "pipeline:structured_competition_rules_en", bug
    assert "Game Breaking Bug" in bug.answer, bug.answer

    print("ENGLISH DRAFT PREVIEW SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
