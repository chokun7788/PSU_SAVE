from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.input_recovery import inspect_surface_input  # noqa: E402
from app.pipeline.model_gateway import preflight_llm_allowed  # noqa: E402
from app.pipeline.schemas import PipelineRoute  # noqa: E402
from app.pipeline.universal_intent import _build_intent_candidates, _heuristic_intent  # noqa: E402
from app.core.locale import resolve_locale  # noqa: E402


def main() -> int:
    clean = inspect_surface_input("นายเป็นใคร")
    typo = inspect_surface_input("นยเปนใค")
    normal_fact = inspect_surface_input("ราคา PC เท่าไหร่")
    if not typo.should_review_intent:
        raise AssertionError(f"expected a bounded typo review signal: {typo}")
    if clean.should_review_intent:
        raise AssertionError(f"clean identity wording must not need recovery: {clean}")
    if normal_fact.should_review_intent:
        raise AssertionError(f"normal price request must not need recovery: {normal_fact}")

    locale = resolve_locale(
        "นยเปนใค",
        requested="auto",
        keyboard_layout_direction="english_intended_thai_active",
        surface_language=typo.language,
    )
    if locale.effective != "th":
        raise AssertionError(f"malformed Thai must not leak into English locale: {locale}")

    weak_route = PipelineRoute("general", "unknown_domain_query", 0.55, "fact", "medium", "weak wording")
    allowed, reason = preflight_llm_allowed(weak_route, True, "นยเปนใค")
    if not allowed or "surface typo" not in reason:
        raise AssertionError(f"surface typo must open bounded LLM review: {allowed}, {reason}")

    heuristic = _heuristic_intent("นยเปนใค", weak_route)
    candidates = _build_intent_candidates("นยเปนใค", weak_route, heuristic)
    if not any(item.get("target") == "chatbot_identity" for item in candidates):
        raise AssertionError(f"identity candidate missing for typo recovery: {candidates}")

    recovered = answer_question_pipeline_debug(
        "นายเปนไค",
        experimental_rag_fallback=True,
        experimental_allow_llm=False,
    )
    if recovered.route.intent != "chatbot_identity":
        raise AssertionError(f"prototype/fast recovery regressed: {recovered.route}")
    if "PSU Esports Assistant" not in recovered.answer:
        raise AssertionError(f"expected deterministic identity answer: {recovered.answer}")

    prototype_recovered = answer_question_pipeline_debug(
        "นยเปนใค",
        experimental_rag_fallback=True,
        experimental_allow_llm=False,
    )
    if prototype_recovered.route.intent != "chatbot_identity":
        raise AssertionError(f"prototype route was not selected: {prototype_recovered.route}")
    if "PSU Esports Assistant" not in prototype_recovered.answer:
        raise AssertionError(f"trusted prototype route did not return identity answer: {prototype_recovered.answer}")

    print("SURFACE INPUT RECOVERY SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
