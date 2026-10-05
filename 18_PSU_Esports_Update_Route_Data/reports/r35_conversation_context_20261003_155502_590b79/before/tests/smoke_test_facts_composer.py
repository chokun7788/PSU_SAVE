from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import app.pipeline.facts_composer as facts_composer
from app.pipeline.facts_composer import compose_structured_answer
from app.pipeline.schemas import PipelineRoute, UniversalIntent


ROUTE = PipelineRoute(
    category="games",
    intent="list",
    confidence=0.9,
    answer_type="list",
    risk="low",
    reason="smoke",
)
INTENT = UniversalIntent(
    domain="games",
    operation="list",
    target="ps5",
    confidence=0.9,
    method="smoke",
)
DRAFT = "PS5 มีเกมทั้งหมด 2 เกม:\n•    TEKKEN 8\n•    Minecraft\nแหล่งข้อมูล: local://games.json"
EVIDENCE = {"platform": "ps5", "games": ["TEKKEN 8", "Minecraft"]}


def test_disabled_returns_draft() -> None:
    previous = os.environ.get("PSU_FACTS_LLM_COMPOSER")
    os.environ["PSU_FACTS_LLM_COMPOSER"] = "0"
    try:
        result = compose_structured_answer(
            question="PS5 มีเกมอะไรบ้าง",
            draft_answer=DRAFT,
            evidence=EVIDENCE,
            route=ROUTE,
            intent=INTENT,
            mode="structured_games_catalog",
            allow_llm=True,
        )
    finally:
        if previous is None:
            os.environ.pop("PSU_FACTS_LLM_COMPOSER", None)
        else:
            os.environ["PSU_FACTS_LLM_COMPOSER"] = previous

    assert result.answer == DRAFT
    assert not result.used_llm
    assert result.trace.decision == "disabled"


def test_enabled_accepts_safe_composition() -> None:
    previous = os.environ.get("PSU_FACTS_LLM_COMPOSER")
    previous_call = facts_composer._call_ollama
    os.environ["PSU_FACTS_LLM_COMPOSER"] = "1"
    facts_composer._call_ollama = lambda _prompt: "PS5 มีเกมทั้งหมด 2 เกม\n•    TEKKEN 8\n•    Minecraft\nแหล่งข้อมูล: local://games.json"
    try:
        result = compose_structured_answer(
            question="PS5 มีเกมอะไรบ้าง",
            draft_answer=DRAFT,
            evidence=EVIDENCE,
            route=ROUTE,
            intent=INTENT,
            mode="structured_games_catalog",
            allow_llm=True,
        )
    finally:
        facts_composer._call_ollama = previous_call
        if previous is None:
            os.environ.pop("PSU_FACTS_LLM_COMPOSER", None)
        else:
            os.environ["PSU_FACTS_LLM_COMPOSER"] = previous

    assert result.used_llm
    assert result.trace.decision == "llm_composed"
    assert "TEKKEN 8" in result.answer


def test_enabled_rejects_changed_source_line() -> None:
    previous = os.environ.get("PSU_FACTS_LLM_COMPOSER")
    previous_call = facts_composer._call_ollama
    os.environ["PSU_FACTS_LLM_COMPOSER"] = "1"
    facts_composer._call_ollama = lambda _prompt: "PS5 มีเกมทั้งหมด 2 เกม\nแหล่งข้อมูล: local://wrong.json"
    try:
        result = compose_structured_answer(
            question="PS5 มีเกมอะไรบ้าง",
            draft_answer=DRAFT,
            evidence=EVIDENCE,
            route=ROUTE,
            intent=INTENT,
            mode="structured_games_catalog",
            allow_llm=True,
        )
    finally:
        facts_composer._call_ollama = previous_call
        if previous is None:
            os.environ.pop("PSU_FACTS_LLM_COMPOSER", None)
        else:
            os.environ["PSU_FACTS_LLM_COMPOSER"] = previous

    assert result.answer == DRAFT
    assert not result.used_llm
    assert result.trace.decision == "rejected"


def test_streaming_ollama_response_is_joined_and_closed() -> None:
    class FakeResponse:
        def __init__(self) -> None:
            self.closed = False

        def __iter__(self):
            return iter((
                b'{"response":"A","done":false}\n',
                b'{"response":"B","done":true}\n',
            ))

        def close(self) -> None:
            self.closed = True

    fake = FakeResponse()
    previous_urlopen = facts_composer.urllib.request.urlopen
    facts_composer.urllib.request.urlopen = lambda *_args, **_kwargs: fake
    try:
        assert facts_composer._call_ollama("test prompt") == "AB"
    finally:
        facts_composer.urllib.request.urlopen = previous_urlopen
    assert fake.closed


if __name__ == "__main__":
    test_disabled_returns_draft()
    print("OK facts composer disabled fallback")
    test_enabled_accepts_safe_composition()
    print("OK facts composer accepts safe composition")
    test_enabled_rejects_changed_source_line()
    print("OK facts composer rejects changed source line")
    test_streaming_ollama_response_is_joined_and_closed()
    print("OK facts composer streaming response closes cleanly")
    print("FACTS COMPOSER SMOKE TEST OK")
