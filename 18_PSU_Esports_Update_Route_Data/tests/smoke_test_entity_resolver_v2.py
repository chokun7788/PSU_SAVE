from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import AnswerQualityPipeline  # noqa: E402
from app.pipeline.entity_resolver import resolve_game_entity  # noqa: E402


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item not in text]
    if missing:
        raise AssertionError(f"{label}: missing {missing}\n{text}")


def assert_not_contains(text: str, blocked: list[str], label: str) -> None:
    found = [item for item in blocked if item in text]
    if found:
        raise AssertionError(f"{label}: found blocked {found}\n{text}")


def test_resolver_blocks_incomplete_call_of_family() -> None:
    resolution = resolve_game_entity("Call of เล่นยังไง", operation="gameplay")
    assert resolution.status == "ambiguous", resolution
    titles = [candidate.title for candidate in resolution.candidates]
    assert "Call of Duty: Warzone" in titles, titles
    assert "Call of Duty: Modern Warfare III" in titles, titles
    assert "Horizon Call of the Mountain" not in titles, titles


def test_resolver_does_not_match_short_alias_inside_long_word() -> None:
    resolution = resolve_game_entity("Gran Turismo 7 ปุ่ม", operation="controls")
    assert resolution.status == "exact", resolution
    assert resolution.top_candidate and resolution.top_candidate.title == "Gran Turismo 7", resolution
    titles = [candidate.title for candidate in resolution.candidates]
    assert "Super Mario Odyssey" not in titles, titles


def test_pipeline_clarifies_family_controls_but_allows_family_list() -> None:
    pipeline = AnswerQualityPipeline()

    call_of = pipeline.answer("Call of เล่นยังไง", experimental_allow_llm=False)
    assert call_of.mode == "pipeline:ambiguity_clarification", call_of.mode
    assert_contains(call_of.answer, ["Call of Duty: Warzone", "Call of Duty: Modern Warfare III"], "call of clarification")
    assert_not_contains(call_of.answer, ["Horizon Call of the Mountain"], "call of clarification")

    mario_controls = pipeline.answer("Mario ปุ่มอะไร", experimental_allow_llm=False)
    assert mario_controls.mode == "pipeline:ambiguity_clarification", mario_controls.mode
    assert_contains(mario_controls.answer, ["Mario Kart 8 Deluxe", "Mario Party Superstars"], "mario controls clarification")

    mario_list = pipeline.answer("Mario มีเกมอะไรบ้าง", experimental_allow_llm=False)
    assert mario_list.mode == "pipeline:structured_games_family", mario_list.mode
    assert_contains(mario_list.answer, ["Mario Kart 8 Deluxe", "Super Mario Odyssey"], "mario family list")


def test_exact_game_still_answers_controls() -> None:
    pipeline = AnswerQualityPipeline()
    result = pipeline.answer("Gran Turismo 7 ปุ่ม", experimental_allow_llm=False)
    assert result.mode == "pipeline:structured_game_controls", result.mode
    assert_contains(result.answer, ["Gran Turismo 7", "R2", "L2"], "gran turismo controls")


if __name__ == "__main__":
    test_resolver_blocks_incomplete_call_of_family()
    test_resolver_does_not_match_short_alias_inside_long_word()
    test_pipeline_clarifies_family_controls_but_allows_family_list()
    test_exact_game_still_answers_controls()
    print("OK entity resolver v2 smoke tests")

