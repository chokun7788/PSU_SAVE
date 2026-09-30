from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import get_pipeline  # noqa: E402
from app.pipeline.entity_resolver import resolve_game_entity  # noqa: E402
from app.pipeline.question_frame import build_question_frame  # noqa: E402
from app.pipeline.request_deadline import RequestBudget, StageDeadlineExceeded, request_deadline  # noqa: E402
from app.pipeline.schemas import PipelineRoute  # noqa: E402


def _route(category: str, intent: str) -> PipelineRoute:
    return PipelineRoute(category, intent, 0.90, "fact", "low", "test")


def main() -> int:
    budget = RequestBudget(started=0.0, timeout_sec=1.0, finalizer_reserve_sec=0.0, deadline=0.0)
    try:
        budget.checkpoint("synthetic_loop")
    except StageDeadlineExceeded as exc:
        assert exc.stage == "synthetic_loop"
    else:
        raise AssertionError("expired RequestBudget must stop a stage")
    print("OK RequestBudget stops an expired stage")

    frame = build_question_frame("ใครเป็นผู้จัดการ", _route("games", "games_lookup"))
    assert frame.operation == "member_lookup"
    assert frame.domain == "overview"
    assert frame.metadata["runtime_route"] == "overview"
    assert frame.metadata["evidence_category"] == "about_us"
    print("OK member QuestionFrame is a closed overview route")

    with request_deadline(3.0):
        first = resolve_game_entity("Tekken 8 ราคาเท่าไหร่", operation="detail")
        second = resolve_game_entity("Tekken 8 ราคาเท่าไหร่", operation="detail")
    assert first.status == "exact" and first.top_candidate is not None
    assert second.metadata.get("request_cache_hit") is True
    assert int(second.metadata.get("comparison_count") or 0) <= 64
    assert float(second.metadata.get("elapsed_ms") or 9999) < 250
    print("OK GameResolver reuses bounded per-request resolution")

    answer = get_pipeline().answer("ตำแหน่งผู้จัดการคือใคร", global_timeout_sec=3.0)
    assert answer.route.category == "overview"
    assert answer.mode.startswith("pipeline:structured_members_")
    decisions = [item.decision for item in answer.trace]
    assert "member_closed_route" in decisions
    assert "skipped_member_closed_route" in decisions
    print("OK member request bypasses semantic route lock and resolves deterministically")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
