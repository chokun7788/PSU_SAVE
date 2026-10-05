from __future__ import annotations

from dataclasses import dataclass

from app.core.normalization import normalize_text
from app.pipeline.entity_resolver import EntityResolution, resolve_game_entity
from app.pipeline.schemas import PipelineRoute


_COMPETITION_SIGNALS = (
    "competition", "tournament", "bracket", "match", "round", "ban", "pause",
    "penalty", "forfeit", "rules", "กติกา", "การแข่งขัน", "แข่ง", "บทลงโทษ",
    "ผู้เล่นกี่คน", "ตัวสำรอง", "มาสาย", "เกมหลุด", "รีสตาร์ท", "restart",
)
_NON_DETAIL_SIGNALS = (
    "price", "cost", "fee", "บาท", "ราคา", "ค่าบริการ",
    "booking", "book", "reserve", "จอง", "ชำระ", "payment",
    # These are access/booking requests when they appear with a named game.
    # They need the game as a target for service selection, but must keep the
    # booking answer contract rather than being forced into game detail.
    "อยากเล่น", "อยากลองเล่น", "จะเล่น", "ขอเล่น", "เข้าใช้",
    "ต้องทำยังไง", "ต้องทำอย่างไร", "วิธีเข้าใช้", "how do i play",
)
_CONTROL_SIGNALS = (
    "controls", "control", "controller", "buttons", "ปุ่ม", "จอย", "ควบคุม",
)
_AVAILABILITY_SIGNALS = (
    "available", "availability", "can i play", "where can", "where is", "which zone",
    "เล่นได้ไหม", "เล่นที่ไหน", "โซนไหน", "มีไหม", "อยู่ที่ไหน",
)


@dataclass(frozen=True)
class TargetLockDecision:
    locked: bool
    route: PipelineRoute
    resolution: EntityResolution | None
    reason: str

    def as_dict(self) -> dict:
        return {
            "locked": self.locked,
            "route_category": self.route.category,
            "route_intent": self.route.intent,
            "reason": self.reason,
            "resolution": self.resolution.as_dict() if self.resolution is not None else None,
        }


def _contains_any(query: str, values: tuple[str, ...]) -> bool:
    normalized = normalize_text(query)
    return any(normalize_text(value) in normalized for value in values)


def lock_explicit_game_target(query: str, route: PipelineRoute) -> TargetLockDecision:
    """Pin an exact game-detail request before broad semantic route discovery.

    Pricing, booking, controls, and competition questions retain their own
    deterministic paths. This lock therefore protects only the narrow class
    where a known title itself is the target of a detail question.
    """
    if _contains_any(query, _COMPETITION_SIGNALS):
        return TargetLockDecision(False, route, None, "explicit_competition_signal")
    if _contains_any(query, _NON_DETAIL_SIGNALS):
        return TargetLockDecision(False, route, None, "price_or_booking_signal")

    operation = (
        "controls"
        if _contains_any(query, _CONTROL_SIGNALS)
        else "availability"
        if _contains_any(query, _AVAILABILITY_SIGNALS)
        else "detail"
    )
    try:
        resolution = resolve_game_entity(query, operation=operation)
    except Exception as exc:  # Target locking must never make the request fail.
        return TargetLockDecision(False, route, None, f"game_resolution_error:{type(exc).__name__}")
    if not resolution.is_exact or resolution.top_candidate is None:
        return TargetLockDecision(False, route, resolution, f"game_resolution_{resolution.status}")

    intent = {
        "controls": "game_control_lookup",
        "availability": "game_availability_lookup",
    }.get(operation, "game_detail_lookup")
    locked_route = PipelineRoute(
        "games",
        intent,
        max(route.confidence, 0.94),
        "fact",
        "low",
        f"exact game target locked: {resolution.top_candidate.title}",
    )
    return TargetLockDecision(True, locked_route, resolution, "exact_known_game_target")
