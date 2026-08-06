from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.entity_resolver import resolve_game_entity
from app.pipeline.schemas import PipelineRoute, UniversalIntent
from app.pipeline.target_resolver import resolve_target_candidate
from app.pipeline.tool_preconditions import (
    looks_like_damage_penalty_query,
    looks_like_equipment_query,
    looks_like_play_access_query,
    looks_like_studio_rules_query,
)


@dataclass(frozen=True)
class FrameTarget:
    target_id: str
    target_type: str
    domain: str
    label: str
    score: float

    def as_dict(self) -> dict[str, Any]:
        return {
            "target_id": self.target_id,
            "target_type": self.target_type,
            "domain": self.domain,
            "label": self.label,
            "score": round(self.score, 3),
        }


@dataclass(frozen=True)
class QuestionFrame:
    operation: str
    domain: str
    expected_answer_types: tuple[str, ...]
    targets: tuple[FrameTarget, ...] = ()
    target_status: str = "unknown"
    target_margin: float = 0.0
    target_required: bool = False
    allows_multiple_targets: bool = False
    needs_clarification: bool = False
    confidence: float = 0.0
    method: str = "heuristic"
    metadata: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "operation": self.operation,
            "domain": self.domain,
            "expected_answer_types": list(self.expected_answer_types),
            "targets": [target.as_dict() for target in self.targets],
            "target_status": self.target_status,
            "target_margin": round(self.target_margin, 3),
            "target_required": self.target_required,
            "allows_multiple_targets": self.allows_multiple_targets,
            "needs_clarification": self.needs_clarification,
            "confidence": round(self.confidence, 3),
            "method": self.method,
            **self.metadata,
        }


def _has(text: str, *terms: str) -> bool:
    clean = normalize_text(text)
    return any(normalize_text(term) in clean for term in terms)


def _operation_from_question(question: str, intent: UniversalIntent | None) -> tuple[str, str, float]:
    if looks_like_damage_penalty_query(question):
        return "penalty_lookup", "penalty", 0.98
    if _has(question, "ปุ่ม", "controls", "control", "controller", "กดอะไร", "ใช้จอย", "บังคับยังไง"):
        return "control_lookup", "game_controls", 0.98
    if (
        _has(question, "ต่างกัน", "เปรียบเทียบ", "เทียบ", "กับ")
        and _has(question, "30 นาที", "1 ชั่วโมง", "ชั่วโมง", "นาที")
        and _has(question, "vr", "วีอาร์", "pc", "ps5", "playstation", "nintendo", "switch", "cockpit")
    ):
        return "price_lookup", "service_fee", 0.97
    if _has(question, "ราคา", "กี่บาท", "ค่าบริการ", "คิดเงิน", "คำนวณ", "เสียเงิน", "จ่ายเท่า"):
        return "price_lookup", "service_fee", 0.98
    if looks_like_play_access_query(question) or _has(
        question,
        "จอง",
        "booking",
        "book",
        "เข้าใช้บริการ",
        "เข้าเล่นยังไง",
        "จะเล่นต้องทำไง",
        "จะเล่นต้องทำยังไง",
        "ต้องทำยังไงถึงจะเล่น",
    ):
        return "booking_lookup", "reservation", 0.96
    if _has(question, "เปิดกี่โมง", "ปิดกี่โมง", "เปิดไหม", "วันไหน", "ตารางเวลา", "เวลาเปิด", "เวลา ปิด"):
        return "schedule_lookup", "schedule", 0.96
    if (
        _has(question, "เล่นได้กี่ชั่วโมง", "กี่ชั่วโมงต่อวัน", "เล่นกี่ชั่วโมง", "สูงสุดกี่ session", "จองได้กี่ session")
        or (intent is not None and intent.domain == "reservation" and intent.operation == "booking_session_limit")
    ):
        return "booking_session_limit", "reservation", 0.96
    if _has(question, "เกมเยอะสุด", "เกมมากสุด", "มีเกมเยอะกว่า", "จำนวนเกมตามโซน", "เกมกี่เกมแต่ละโซน"):
        return "game_zone_rank", "games", 0.98
    if looks_like_studio_rules_query(question) or (intent is not None and intent.domain == "rules"):
        return "studio_rule_lookup", "rules", max(0.94, intent.confidence if intent is not None else 0.0)
    if (
        _has(question, "เกม", "game", "games")
        and _has(
            question,
            "แข่งรถ",
            "เกมยิง",
            "fps",
            "ต่อสู้",
            "กีฬา",
            "ฟุตบอล",
            "party",
            "co-op",
            "จังหวะ",
            "rpg",
            "สยอง",
            "เกมผี",
        )
        and _has(question, "มีอะไรบ้าง", "มีเกมอะไร", "เกมอะไรบ้าง", "รายชื่อ", "ทั้งหมด", "แนะนำ")
    ):
        return "game_catalog", "games", 0.96
    if _has(question, "กติกา", "แข่ง", "แข่งขัน", "การแข่งขัน", "bo1", "bo3", "best of", "รอบชิง", "รอบรอง"):
        return "competition_rule_lookup", "competition_rules", 0.96
    if (
        intent is not None
        and intent.domain in {"competition_rules", "rules"}
        and intent.operation in {"rule_lookup", "count", "list", "lookup"}
    ):
        return "competition_rule_lookup", "competition_rules", max(0.90, intent.confidence)
    if _has(question, "สมาชิก", "ทีมงาน", "ตำแหน่ง", "ใครทำ", "ใครเป็น", "staff"):
        return "member_lookup", "members", 0.94
    if _has(question, "คือเกมอะไร", "เกมแนวไหน", "แนวเกม", "เกี่ยวกับอะไร"):
        return "game_detail", "games", 0.94
    if (
        intent is not None
        and intent.domain == "games"
        and intent.operation == "availability"
        and _has(question, "เครื่องไหน", "โซนไหน", "อยู่ไหน", "อยู่ที่ไหน", "เล่นได้ที่ไหน", "มีในเครื่อง")
    ):
        return "game_detail", "games", max(0.94, intent.confidence)
    if _has(question, "มีเกมอะไร", "เกมอะไรบ้าง", "รายชื่อเกม", "รายการเกม", "เกมทั้งหมด"):
        return "game_catalog", "games", 0.96
    if looks_like_equipment_query(question):
        return "equipment_lookup", "equipment", 0.92
    if _has(question, "เล่นยังไง", "วิธีเล่น", "เล่นอย่างไร"):
        return "game_how_to", "games", 0.88

    if intent is not None and intent.operation and intent.operation != "unknown":
        domain = intent.domain if intent.domain and intent.domain != "unknown" else "general"
        normalized_operation = {
            "control": "control_lookup",
            "controls": "control_lookup",
            "price_calculate": "price_calculate",
            "price_lookup": "price_lookup",
            "booking": "booking_lookup",
            "reservation": "booking_lookup",
            "detail": {
                "games": "game_detail",
                "game_controls": "game_detail",
                "equipment": "equipment_lookup",
                "members": "member_lookup",
                "reservation": "booking_lookup",
                "schedule": "schedule_lookup",
            }.get(domain, "detail"),
            "availability": {
                "games": "game_detail",
                "equipment": "equipment_lookup",
                "schedule": "schedule_lookup",
            }.get(domain, "availability"),
            "how_to": {
                "games": "game_how_to",
                "game_controls": "control_lookup",
                "equipment": "equipment_lookup",
                "reservation": "booking_lookup",
                "schedule": "schedule_lookup",
            }.get(domain, "how_to"),
            "list": {
                "games": "game_catalog",
                "equipment": "equipment_lookup",
                "members": "member_lookup",
                "schedule": "schedule_lookup",
                "reservation": "booking_lookup",
                "rules": "studio_rule_lookup",
                "competition_rules": "competition_rule_lookup",
            }.get(domain, "list"),
            "rule_lookup": (
                "competition_rule_lookup"
                if domain == "competition_rules"
                else "penalty_lookup"
                if domain == "penalty"
                else "booking_lookup"
                if domain == "reservation"
                else "studio_rule_lookup"
                if domain == "rules"
                else "rule_lookup"
            ),
            "role_lookup": "member_lookup",
            "group_count": "member_lookup",
        }.get(intent.operation, intent.operation)
        return normalized_operation, domain, max(0.55, intent.confidence)
    return "unknown", "general", 0.35


def _expected_answer_types(operation: str) -> tuple[str, ...]:
    return {
        "control_lookup": ("controls",),
        "price_lookup": ("price", "calculation"),
        "price_calculate": ("price", "calculation"),
        "booking_lookup": ("booking", "how_to"),
        "booking_session_limit": ("booking", "fact"),
        "schedule_lookup": ("schedule",),
        "game_zone_rank": ("ranking", "list", "calculation"),
        "game_catalog": ("game_catalog", "list"),
        "game_detail": ("game_detail",),
        "game_how_to": ("game_detail", "controls", "how_to"),
        "equipment_lookup": ("equipment", "list"),
        "member_lookup": ("member", "list"),
        "studio_rule_lookup": ("fact", "list", "summary", "rule"),
        "competition_rule_lookup": ("competition_rule",),
        "penalty_lookup": ("penalty", "rule"),
    }.get(operation, ("fact", "summary"))


def _target_operation(operation: str) -> str:
    return {
        "control_lookup": "controls",
        "price_lookup": "price",
        "booking_lookup": "booking",
        "booking_session_limit": "booking",
        "game_detail": "detail",
        "game_how_to": "gameplay",
        "game_catalog": "list",
        "game_zone_rank": "count",
        "equipment_lookup": "equipment",
    }.get(operation, operation)


def build_question_frame(
    question: str,
    route: PipelineRoute,
    intent: UniversalIntent | None = None,
) -> QuestionFrame:
    operation, detected_domain, confidence = _operation_from_question(question, intent)
    domain = detected_domain
    if domain == "general" and intent is not None and intent.domain not in {"", "unknown", "general"}:
        domain = intent.domain
    if domain == "general" and route.category not in {"", "unknown", "general", "no_answer"}:
        domain = route.category

    target_required = operation in {"control_lookup", "game_detail"}
    allows_multiple = operation in {"price_lookup", "price_calculate", "game_catalog", "game_zone_rank"}
    preferred_domains = (domain,) if domain not in {"general", "unknown"} else ()
    resolution = resolve_target_candidate(
        question,
        operation=_target_operation(operation),
        preferred_domains=preferred_domains,
    )

    family_resolution = None
    family_override = False
    if operation == "game_detail" and domain == "games":
        family_resolution = resolve_game_entity(question, operation="list")
        target_match_type = (
            resolution.top_candidate.match_type
            if resolution.top_candidate is not None
            else ""
        )
        target_is_specific_alias = (
            resolution.status == "exact"
            and target_match_type.startswith(("exact_alias", "compact_alias", "fuzzy"))
        )
        if (
            family_resolution.metadata.get("family")
            and len(family_resolution.candidates) > 1
            and not target_is_specific_alias
        ):
            family_override = True
            operation = "game_catalog"
            allows_multiple = True
            target_required = False

    targets: list[FrameTarget] = []
    if resolution.top_candidate is not None and not family_override:
        candidate = resolution.top_candidate
        targets.append(FrameTarget(
            target_id=candidate.target_id,
            target_type=candidate.target_type,
            domain=candidate.domain,
            label=candidate.label,
            score=candidate.score,
        ))

    same_domain_candidates = {
        candidate.domain for candidate in resolution.candidates[:4]
    }
    ambiguous_but_usable_family = allows_multiple and len(same_domain_candidates) == 1
    needs_clarification = (
        target_required
        and resolution.status in {"ambiguous", "incomplete", "unknown"}
        and not ambiguous_but_usable_family
    )

    return QuestionFrame(
        operation=operation,
        domain=domain,
        expected_answer_types=_expected_answer_types(operation),
        targets=tuple(targets),
        target_status=family_resolution.status if family_override and family_resolution is not None else resolution.status,
        target_margin=family_resolution.margin if family_override and family_resolution is not None else resolution.margin,
        target_required=target_required,
        allows_multiple_targets=allows_multiple,
        needs_clarification=needs_clarification,
        confidence=confidence,
        method="operation_first",
        metadata={
            "route_category": route.category,
            "route_intent": route.intent,
            "intent_operation": intent.operation if intent is not None else "",
            "target_reason": family_resolution.reason if family_override and family_resolution is not None else resolution.reason,
            "target_candidate_count": len(family_resolution.candidates) if family_override and family_resolution is not None else len(resolution.candidates),
            "game_family": family_resolution.metadata.get("family") if family_resolution is not None else "",
        },
    )
