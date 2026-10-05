from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.chatbot_identity import is_chatbot_identity_query  # noqa: E402
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.schemas import PipelineRoute  # noqa: E402
from app.pipeline.universal_intent import (  # noqa: E402
    _build_intent_candidates,
    _heuristic_intent,
    _intent_from_candidate,
    refine_route_with_universal_intent,
)


def main() -> int:
    if not is_chatbot_identity_query("นายเปนไค"):
        raise AssertionError("minor typo should match the closed chatbot identity intent")
    if is_chatbot_identity_query("นายเล่นเกมอะไร"):
        raise AssertionError("ordinary game question must not match chatbot identity")

    result = answer_question_pipeline_debug(
        "นายเปนไค",
        experimental_rag_fallback=True,
        experimental_allow_llm=False,
    )
    if result.route.intent != "chatbot_identity":
        raise AssertionError(f"expected chatbot_identity route, got {result.route}")
    if result.mode != "pipeline:chatbot_identity_fast_path":
        raise AssertionError(f"expected fast identity answer, got {result.mode}")
    if "PSU Esports Assistant" not in result.answer:
        raise AssertionError(f"identity answer missing expected content: {result.answer}")

    weak_route = PipelineRoute("general", "general_knowledge_query", 0.55, "summary", "low", "weak wording")
    fallback = _heuristic_intent("นายเปนไค", weak_route)
    candidates = _build_intent_candidates("นายเปนไค", weak_route, fallback)
    identity_candidate = next((item for item in candidates if item.get("target") == "chatbot_identity"), None)
    if identity_candidate is None:
        raise AssertionError(f"missing local LLM identity candidate: {candidates}")
    selected = _intent_from_candidate(
        {"candidate_id": identity_candidate["id"], "confidence": 0.91, "reason": "typo recovered"},
        candidates,
        fallback,
    )
    refined, _ = refine_route_with_universal_intent(weak_route, selected)
    if refined.intent != "chatbot_identity":
        raise AssertionError(f"LLM-selected identity candidate did not refine route: {refined}")

    print("TYPO IDENTITY RECOVERY SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
