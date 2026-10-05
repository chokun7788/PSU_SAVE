from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.schemas import PipelineRoute  # noqa: E402
from app.pipeline.target_lock import lock_explicit_game_target  # noqa: E402
from app.pipeline.question_frame import build_question_frame  # noqa: E402


def _route(category: str = "events_news", intent: str = "news_lookup") -> PipelineRoute:
    return PipelineRoute(category, intent, 0.62, "summary", "low", "test")


def main() -> int:
    detail = lock_explicit_game_target("Tell me about VALORANT", _route())
    assert detail.locked
    assert detail.route.category == "games"
    assert detail.route.intent == "game_detail_lookup"
    assert detail.resolution is not None and detail.resolution.top_candidate is not None
    assert detail.resolution.top_candidate.title == "VALORANT"
    frame = build_question_frame("Tell me about VALORANT", detail.route)
    assert frame.operation == "game_detail"
    assert frame.target_required
    assert frame.target_status == "exact"
    assert frame.targets and frame.targets[0].target_id == "valorant"

    controls = lock_explicit_game_target("What are the controls for Beat Saber?", _route())
    assert controls.locked
    assert controls.route.intent == "game_control_lookup"

    availability = lock_explicit_game_target("Can I play Beat Saber in VR Zone?", _route())
    assert availability.locked
    assert availability.route.intent == "game_availability_lookup"

    tournament = lock_explicit_game_target("What are the VALORANT tournament rules?", _route("competition_rules", "competition_rule_lookup"))
    assert not tournament.locked
    assert tournament.reason == "explicit_competition_signal"

    price = lock_explicit_game_target("How much does VALORANT cost?", _route("service_fee", "service_fee_query"))
    assert not price.locked
    assert price.reason == "price_or_booking_signal"

    unknown = lock_explicit_game_target("Tell me about Example Quest", _route())
    assert not unknown.locked
    assert unknown.reason.startswith("game_resolution_")

    print("OK explicit game target lock preserves detail/control paths and excludes price, booking, competition, and unknown titles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
