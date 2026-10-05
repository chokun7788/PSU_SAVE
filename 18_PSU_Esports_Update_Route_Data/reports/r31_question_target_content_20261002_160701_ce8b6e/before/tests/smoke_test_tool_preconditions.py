from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.schemas import PipelineRoute, UniversalIntent  # noqa: E402
from app.pipeline.tool_preconditions import (  # noqa: E402
    evaluate_capability_precondition,
    evaluate_structured_tool_precondition,
)


def route(category: str, intent: str = "lookup") -> PipelineRoute:
    return PipelineRoute(category, intent, 0.86, "fact", "medium", "test route")


def intent(domain: str, operation: str = "unknown") -> UniversalIntent:
    return UniversalIntent(domain=domain, operation=operation, confidence=0.82)


def main() -> int:
    result = evaluate_capability_precondition(
        "structured.equipment",
        "จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม",
        route("reservation", "booking_policy"),
        intent("equipment", "count"),
    )
    assert not result.ok
    assert result.reason == "booking_query_must_not_use_equipment_tool"
    print("OK booking query rejects equipment tool")

    result = evaluate_structured_tool_precondition(
        "จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม",
        route("reservation", "booking_policy"),
        intent("equipment", "count"),
    )
    assert result.ok
    assert result.capability_id == "structured.reservation"
    print("OK booking query maps structured execution to reservation")

    result = evaluate_structured_tool_precondition(
        "แล้วจะเล่นต้องทำไง",
        route("general", "unknown_domain_query"),
        intent("general", "unknown"),
    )
    assert result.ok
    assert result.capability_id == "structured.reservation"
    print("OK play access query maps structured execution to reservation")

    result = evaluate_capability_precondition(
        "structured.games",
        "ROV รอบชิงเล่นกี่เกม",
        route("competition_rules", "competition_rules_lookup"),
        intent("games", "count"),
    )
    assert not result.ok
    assert result.reason == "competition_rule_query_must_not_use_game_catalog"
    print("OK competition rule rejects game catalog")

    result = evaluate_capability_precondition(
        "fast.price_calculator",
        "ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท",
        route("reservation", "booking_policy"),
        intent("reservation", "price_calculate"),
    )
    assert result.ok
    print("OK price query allows calculator")

    result = evaluate_capability_precondition(
        "fast.domain_handlers",
        "ROV รอบชิงเล่นกี่เกม",
        route("competition_rules", "competition_rules_lookup"),
        intent("games", "count"),
    )
    assert result.ok
    assert result.reason == "competition_fast_handler_applicable"
    print("OK competition query allows fast domain handler")

    result = evaluate_capability_precondition(
        "structured.games",
        "PS5 มีเกมอะไรบ้าง",
        route("games", "list"),
        intent("games", "list"),
    )
    assert result.ok
    print("OK game catalog query allows games tool")

    result = evaluate_capability_precondition(
        "structured.games",
        "สตาฟเล่นเกมอะไรบ้าง",
        route("games", "list"),
        intent("games", "list"),
    )
    assert not result.ok
    assert result.reason == "people_or_role_query_must_not_use_game_catalog"
    print("OK people/role query rejects game catalog")

    result = evaluate_structured_tool_precondition(
        "ตำแหน่ง Game and 3D Developer ใครทำ",
        route("games", "list"),
        intent("games", "list"),
    )
    assert result.ok
    assert result.capability_id == "structured.members"
    print("OK people/role query maps structured execution to members")

    result = evaluate_structured_tool_precondition(
        "Tekken 8 ราคาเท่าไหร่",
        route("service_fee", "service_fee_query"),
        intent("service_fee", "price_calculate"),
    )
    assert result.ok
    assert result.capability_id == "structured.service_fee"
    assert result.reason == "known_game_price_query_needs_zone_service_mapping"
    print("OK known game price maps to structured service fee")

    print("TOOL PRECONDITIONS SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
