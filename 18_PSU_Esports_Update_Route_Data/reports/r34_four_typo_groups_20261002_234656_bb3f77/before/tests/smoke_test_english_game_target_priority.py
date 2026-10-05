from __future__ import annotations

import os
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main() -> int:
    draft_path = ROOT / "data" / "locales" / "en" / "localization_review_drafts_machine_20260909_verified.jsonl"
    os.environ.update({
        "PSU_BILINGUAL_EN_ENABLED": "1",
        "PSU_SEMANTIC_RETRIEVAL": "1",
        "PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW": "1",
        "PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH": str(draft_path),
    })
    from app.knowledge.localization import load_localization_registry  # noqa: E402
    from app.runtime.pipeline_answer import answer_question_pipeline_debug  # noqa: E402

    load_localization_registry.cache_clear()
    game_detail = answer_question_pipeline_debug(
        "Tell me about VALORANT",
        locale="en",
        experimental_allow_llm=True,
        experimental_rag_fallback=True,
        global_timeout_sec=20.0,
    )
    assert game_detail.mode == "pipeline:structured_game_detail_en", game_detail.mode
    assert game_detail.route.category == "games", game_detail.route
    assert "VALORANT is a tactical shooter" in game_detail.answer

    tournament = answer_question_pipeline_debug(
        "What are the VALORANT tournament rules?",
        locale="en",
        experimental_allow_llm=False,
        experimental_rag_fallback=True,
        global_timeout_sec=20.0,
    )
    assert tournament.route.category == "competition_rules", tournament.route
    assert tournament.mode != "pipeline:structured_game_detail_en", tournament.mode

    non_current_controls = answer_question_pipeline_debug(
        "What does the Y button do in Mario Kart Live: Home Circuit?",
        locale="en",
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
        global_timeout_sec=20.0,
    )
    assert non_current_controls.mode == "pipeline:game_controls_no_current_game_en", non_current_controls.mode
    assert "not listed in the current verified" in non_current_controls.answer
    assert "Mario Kart 8 Deluxe controls:" not in non_current_controls.answer

    non_current_availability = answer_question_pipeline_debug(
        "Can I play Mario Kart Live: Home Circuit at the studio?",
        locale="en",
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
        global_timeout_sec=20.0,
    )
    assert non_current_availability.mode == "pipeline:game_not_in_current_catalog_en", non_current_availability.mode
    assert "cannot confirm its availability" in non_current_availability.answer

    current_controls = answer_question_pipeline_debug(
        "What are the controls in Mario Kart 8 Deluxe?",
        locale="en",
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
        global_timeout_sec=20.0,
    )
    assert current_controls.mode == "pipeline:structured_game_controls_en", current_controls.mode
    assert current_controls.answer.startswith("Mario Kart 8 Deluxe controls:")

    for key in (
        "PSU_BILINGUAL_EN_ENABLED",
        "PSU_SEMANTIC_RETRIEVAL",
        "PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW",
        "PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH",
    ):
        os.environ.pop(key, None)
    load_localization_registry.cache_clear()
    print("OK English game targets retain their exact titles and do not borrow controls from a different Mario Kart game")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
