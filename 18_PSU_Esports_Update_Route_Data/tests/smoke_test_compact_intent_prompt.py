from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.schemas import PipelineRoute, UniversalIntent  # noqa: E402
from app.pipeline.universal_intent import _build_compact_intent_prompt, _compact_candidates_for_llm  # noqa: E402


def main() -> int:
    route = PipelineRoute("games", "games_lookup", 0.55, "fact", "low", "test")
    fallback = UniversalIntent("general", "unknown", "", {}, (), "direct", 0.45, "heuristic", "test")
    candidates = [
        {"id": "c1", "domain": "general", "operation": "unknown", "target": "", "reason": "long internal reason", "confidence": 0.45},
        {"id": "c2", "domain": "games", "operation": "list", "target": "", "reason": "another internal reason", "confidence": 0.66},
    ]
    compact = _compact_candidates_for_llm(candidates)
    if any("reason" in item or "confidence" in item for item in compact):
        raise AssertionError(f"compact choices exposed internal scoring: {compact}")
    prompt = _build_compact_intent_prompt("what game u have", route, fallback, candidates)
    if '"candidate_id":"c1","confidence":0.90' not in prompt:
        raise AssertionError(f"prompt does not require compact JSON: {prompt}")
    if "long internal reason" in prompt or "another internal reason" in prompt:
        raise AssertionError("prompt includes verbose candidate reasons")
    if "Do not answer, translate, explain, or add fields." not in prompt:
        raise AssertionError("prompt is missing output boundary")
    print("COMPACT INTENT PROMPT SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
