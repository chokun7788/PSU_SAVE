from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.experimental_fallback import build_experimental_fallback  # noqa: E402
from app.pipeline.question_frame import FrameTarget, QuestionFrame  # noqa: E402
from app.pipeline.schemas import PipelineRoute  # noqa: E402
from app.pipeline.universal_intent import _build_intent_candidates, _heuristic_intent  # noqa: E402


def test_general_fallback_reads_rag_before_grounded_llm() -> None:
    route = PipelineRoute("general", "general_knowledge_query", 0.50, "summary", "low", "smoke")
    calls: list[str] = []
    rows = [{
        "id": "verified_game_catalog",
        "title": "Verified game catalogue",
        "category": "games",
        "text": "The studio has verified game information.",
        "source_url": "https://example.test/games",
        "_score": 0.91,
        "_experimental_kind": "curated",
    }]

    def fake_retrieval(*_args, **_kwargs):
        calls.append("rag")
        return rows, ["fake_rag"]

    def fake_llm(*_args, **_kwargs):
        calls.append("llm")
        return "The verified game catalogue is available."

    with (
        patch("app.pipeline.experimental_fallback._retrieve_experimental_rows", fake_retrieval),
        patch("app.pipeline.experimental_fallback._call_ollama", fake_llm),
        patch("app.pipeline.experimental_fallback.llm_call_allowed", lambda *_args, **_kwargs: (True, {})),
        patch("app.pipeline.experimental_fallback.record_llm_success", lambda *_args, **_kwargs: {}),
    ):
        result = build_experimental_fallback("what games are available", route, started=0.0, allow_llm=True)

    assert calls == ["rag", "llm"], calls
    assert result.mode == "experimental_rag_llm_fallback"
    assert result.hits


def test_general_llm_is_only_allowed_after_rag_miss() -> None:
    route = PipelineRoute("general", "general_knowledge_query", 0.50, "summary", "low", "smoke")
    calls: list[str] = []

    def fake_retrieval(*_args, **_kwargs):
        calls.append("rag")
        return [], ["fake_rag_miss"]

    def fake_general_llm(*_args, **_kwargs):
        calls.append("llm")
        return "Hello. How can I help?", {"llm_kind": "general_llm"}

    with (
        patch("app.pipeline.experimental_fallback._retrieve_experimental_rows", fake_retrieval),
        patch("app.pipeline.experimental_fallback._general_llm_answer_with_metadata", fake_general_llm),
    ):
        result = build_experimental_fallback("helllo", route, started=0.0, allow_llm=True)

    assert calls == ["rag", "llm"], calls
    assert result.mode == "general_llm_after_rag_miss"


def test_clear_non_psu_general_request_skips_unanchored_rag() -> None:
    route = PipelineRoute("general", "general_knowledge_query", 0.82, "summary", "low", "smoke")
    calls: list[str] = []

    def fake_retrieval(*_args, **_kwargs):
        calls.append("rag")
        raise AssertionError("clear general question must not query the PSU-only RAG index")

    def fake_general_llm(*_args, **_kwargs):
        calls.append("llm")
        return "Latency is the delay before a system responds.", {"llm_kind": "general_llm"}

    with (
        patch("app.pipeline.experimental_fallback._retrieve_experimental_rows", fake_retrieval),
        patch("app.pipeline.experimental_fallback._general_llm_answer_with_metadata", fake_general_llm),
    ):
        result = build_experimental_fallback(
            "อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ",
            route,
            started=0.0,
            allow_llm=True,
        )

    assert calls == ["llm"], calls
    assert result.mode == "general_llm_direct"
    assert result.trace.decision == "general_llm_direct"


def test_fallback_forwards_question_frame_and_locale_to_guarded_retrieval() -> None:
    route = PipelineRoute("games", "detail", 0.76, "detail", "medium", "smoke")
    frame = QuestionFrame(
        operation="game_detail",
        domain="games",
        expected_answer_types=("detail",),
        targets=(FrameTarget("tekken_8", "game", "games", "TEKKEN 8", 0.99),),
        target_status="matched",
        target_required=True,
        confidence=0.99,
        method="smoke",
    )
    captured: dict[str, object] = {}

    def fake_hybrid(_query, _route, **kwargs):
        captured.update(kwargs)
        return [], type("Trace", (), {"detail": "empty"})()

    with patch("app.pipeline.experimental_fallback.retrieve_hybrid_guarded", fake_hybrid):
        result = build_experimental_fallback(
            "TEKKEN 8 คืออะไร",
            route,
            started=0.0,
            allow_llm=False,
            question_frame=frame,
            locale="th",
        )

    assert captured["question_frame"] is frame
    assert captured["locale"] == "th"
    assert result.mode == "experimental_rag_no_context"


def test_short_conversation_offers_identity_and_greeting_to_intent_model() -> None:
    route = PipelineRoute("general", "unknown_domain_query", 0.50, "summary", "low", "smoke")
    for query in ("who r u", "what can u do", "what u can do", "helllo"):
        heuristic = _heuristic_intent(query, route)
        candidates = _build_intent_candidates(query, route, heuristic)
        targets = {str(item.get("target") or "") for item in candidates}
        assert "chatbot_greeting" in targets, (query, candidates)
    identity_candidates = _build_intent_candidates("who r u", route, _heuristic_intent("who r u", route))
    assert any(item.get("target") == "chatbot_identity" for item in identity_candidates)

    count_candidates = _build_intent_candidates(
        "how many game u have",
        route,
        _heuristic_intent("how many game u have", route),
    )
    assert any(item.get("domain") == "games" and item.get("operation") == "count" for item in count_candidates)


def main() -> int:
    test_general_fallback_reads_rag_before_grounded_llm()
    test_general_llm_is_only_allowed_after_rag_miss()
    test_fallback_forwards_question_frame_and_locale_to_guarded_retrieval()
    test_short_conversation_offers_identity_and_greeting_to_intent_model()
    print("RAG AFTER DETERMINISTIC FALLBACK SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
