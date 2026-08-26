from __future__ import annotations

from dataclasses import dataclass

from app.core.normalization import normalize_text
from app.pipeline.query_signals import (
    looks_like_game_zone_ranking_query,
    looks_like_general_concept_definition,
    looks_like_price_amount_query,
)
from app.pipeline.schemas import PipelineRoute, UniversalIntent


@dataclass(frozen=True)
class ToolPreconditionResult:
    capability_id: str
    ok: bool
    reason: str
    severity: str = "policy"

    def as_dict(self) -> dict[str, object]:
        return {
            "capability_id": self.capability_id,
            "ok": self.ok,
            "reason": self.reason,
            "severity": self.severity,
        }


def _has(text: str, *terms: str) -> bool:
    clean = normalize_text(text)
    return any(normalize_text(term) in clean for term in terms)


def looks_like_play_access_query(question: str) -> bool:
    q = normalize_text(question)
    if _has(q, "ปุ่ม", "กดอะไร", "controller", "controls", "ใช้จอย"):
        return False
    if _has(q, "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "สอนเล่น"):
        return False
    has_play_access_signal = _has(
        q,
        "จะเล่น",
        "ถ้าจะเล่น",
        "เข้าเล่น",
        "ไปเล่น",
        "อยากเล่น",
        "เล่นต้องทำ",
        "เล่น ต้องทำ",
        "ต้องการเล่น",
    )
    has_how_to_action = _has(
        q,
        "ต้องทำไง",
        "ต้องทำยังไง",
        "ต้องทำอย่างไร",
        "ทำไง",
        "ทำยังไง",
        "ทำอย่างไร",
        "ต้องจอง",
        "จองยังไง",
    )
    return has_play_access_signal and has_how_to_action


def looks_like_booking_query(question: str) -> bool:
    if looks_like_play_access_query(question):
        return True
    return _has(
        question,
        "จอง",
        "booking",
        "book",
        "เลือกบริการ",
        "ต้องเลือก",
        "ต้องระบุ",
        "จำนวนผู้เล่น",
        "ผู้เล่น",
        "รอบเวลา",
        "จองโซน",
        "ต้องจอง",
    )


def looks_like_price_query(question: str) -> bool:
    if _has(
        question,
        "จ่ายเงินผ่าน",
        "ชำระเงินผ่าน",
        "ช่องทางชำระ",
        "ช่องทางการชำระ",
        "ช่องทางไหน",
        "โอนเงิน",
        "เลขบัญชี",
        "บัญชีธนาคาร",
        "ชื่อบัญชี",
        "ธนาคาร",
        "สลิป",
        "แนบสลิป",
        "หลังจองต้องจ่าย",
        "จ่ายภายใน",
        "ชำระภายใน",
        "ไม่จ่าย",
        "ลืมจ่าย",
        "payment timeout",
    ):
        return False
    return looks_like_price_amount_query(question)


def looks_like_known_game_price_query(question: str) -> bool:
    if not looks_like_price_query(question):
        return False
    try:
        from app.pipeline.entity_resolver import resolve_game_entity
    except Exception:
        return False
    resolution = resolve_game_entity(question, operation="detail")
    return resolution.status in {"exact", "confident"}


def looks_like_damage_penalty_query(question: str) -> bool:
    return _has(
        question,
        "เสียหาย",
        "พัง",
        "ค่าปรับ",
        "โดนปรับ",
        "ปรับเท่าไหร่",
        "ชดเชย",
        "จอแตก",
        "จอยพัง",
        "คอมพัง",
        "เมาส์พัง",
        "คีย์บอร์ดพัง",
        "อุปกรณ์เสีย",
    )


def looks_like_specific_game_detail_query(question: str) -> bool:
    if _has(question, "มีเกมอะไร", "เกมอะไรบ้าง", "เกมไรบ้าง", "รายชื่อเกม", "เกมทั้งหมด", "เล่นเกมอะไรได้บ้าง"):
        return False
    return _has(question, "คือเกมอะไร", "อะไรคือเกม", "คืออะไร", "เป็นเกมแนวไหน", "แนวอะไร", "แนวไหน", "เกี่ยวกับอะไร")


def looks_like_game_catalog_query(question: str) -> bool:
    return _has(
        question,
        "มีเกมอะไร",
        "เกมอะไรบ้าง",
        "เกมไรบ้าง",
        "รายชื่อเกม",
        "รายการเกม",
        "เกมทั้งหมด",
        "เล่นเกมอะไรได้บ้าง",
        "มีอะไรให้เล่น",
    )


def looks_like_studio_rules_query(question: str) -> bool:
    explicit = _has(
        question,
        "กติกาในศูนย์",
        "กฎในศูนย์",
        "กติกาการใช้บริการ",
        "กฎการใช้บริการ",
        "ข้อห้ามในศูนย์",
        "ในศูนย์ห้าม",
        "ศูนย์ห้าม",
        "ห้ามอะไรในศูนย์",
        "ระเบียบในศูนย์",
        "กฎของศูนย์",
    )
    broad_rule = _has(question, "กติกา", "กฎ", "ข้อห้าม", "ห้าม", "ระเบียบ")
    studio_scope = _has(question, "ศูนย์", "studio", "ใช้บริการ")
    return explicit or (broad_rule and studio_scope)


def looks_like_competition_rule_query(question: str) -> bool:
    if looks_like_studio_rules_query(question):
        return False
    return _has(
        question,
        "รอบชิง",
        "รอบรอง",
        "รอบแบ่งกลุ่ม",
        "กติกา",
        "แข่ง",
        "แข่งขัน",
        "ทัวร์",
        "tournament",
        "bo1",
        "bo3",
        "best of",
        "ทีมละ",
        "ตัวสำรอง",
        "มาสาย",
        "voice chat",
        "บัญชี",
        "เช็คอิน",
        "แบน",
        "ban",
    )


def looks_like_control_query(question: str) -> bool:
    return _has(question, "ปุ่ม", "จอย", "controller", "controls", "กดอะไร", "บังคับ", "เล่นยังไง", "วิธีเล่น")


def looks_like_explicit_control_query(question: str) -> bool:
    return _has(question, "ปุ่ม", "จอย", "controller", "controls", "กดอะไร", "กดปุ่มไหน", "บังคับ")


def looks_like_equipment_query(question: str) -> bool:
    if looks_like_general_concept_definition(question) or looks_like_game_zone_ranking_query(question):
        return False
    return _has(
        question,
        "อุปกรณ์",
        "เครื่อง",
        "รุ่น",
        "จำนวน",
        "กี่เครื่อง",
        "อยู่ที่ไหน",
        "โซนไหน",
        "จอ",
        "ทีวี",
        "เมาส์",
        "คีย์บอร์ด",
        "หูฟัง",
        "พวงมาลัย",
        "เก้าอี้",
        "sofa",
        "logitech",
        "g923",
        "gaming pc",
        "gaming monitor",
        "gaming keyboard",
        "gaming mouse",
        "gaming headset",
        "gaming chair",
        "sony playstation vr2",
        "playstation vr2",
        "psvr2",
        "racezone full cockpit",
        "driving force shifter",
        "pulse elite wireless headset",
        "nintendo switch oled",
        "playstation 5 slim",
    )


def looks_like_schedule_query(question: str) -> bool:
    return _has(question, "เปิด", "ปิด", "เวลา", "กี่โมง", "รอบ", "morning", "afternoon", "วันจันทร์", "วันศุกร์")


def looks_like_member_query(question: str) -> bool:
    return _has(question, "สมาชิก", "member", "members", "staff", "สตาฟ", "เจ้าหน้าที่", "คนดูแล", "ทีมงาน", "บุคลากร", "ทีม", "ตำแหน่ง", "หมวด", "กลุ่ม", "สหกิจ", "ฝึกงาน", "ชมรม")


def looks_like_people_or_role_query(question: str) -> bool:
    return _has(
        question,
        "สมาชิก",
        "member",
        "members",
        "staff",
        "สตาฟ",
        "เจ้าหน้าที่",
        "คนดูแล",
        "ทีมงาน",
        "บุคลากร",
        "ตำแหน่ง",
        "ผู้จัดการ",
        "สหกิจ",
        "ฝึกงาน",
        "ใคร",
        "ใครบ้าง",
        "ใครทำ",
        "ใครเป็น",
    )


def structured_capability_id_for(question: str, route: PipelineRoute, intent: UniversalIntent | None) -> str | None:
    domain = intent.domain if intent and intent.domain else route.category

    if looks_like_general_concept_definition(question):
        return None
    if looks_like_game_zone_ranking_query(question):
        return "structured.games"

    if domain in {"competition_rules", "rules"} or route.category == "competition_rules":
        return None

    # Booking-selection questions should be owned by reservation, even if entity
    # detection sees Nintendo/PS5/Cockpit as equipment.
    if looks_like_booking_query(question) and not looks_like_price_query(question):
        return "structured.reservation"
    if looks_like_people_or_role_query(question):
        return "structured.members"
    if looks_like_explicit_control_query(question):
        return "structured.game_controls"

    if domain == "members" or route.category == "members":
        return "structured.members"
    if domain == "game_controls":
        return "structured.game_controls"
    if domain == "games":
        return "structured.games"
    if domain == "equipment" or route.category == "equipment":
        return "structured.equipment"
    if domain == "service_fee" or route.category == "service_fee":
        return "structured.service_fee"
    if domain == "schedule" or route.category == "schedule":
        return "structured.schedule"
    if domain == "reservation" or route.category == "reservation":
        return "structured.reservation"
    return None


def evaluate_capability_precondition(
    capability_id: str,
    question: str,
    route: PipelineRoute,
    intent: UniversalIntent | None,
) -> ToolPreconditionResult:
    domain = intent.domain if intent and intent.domain else route.category
    operation = intent.operation if intent else route.intent

    if capability_id == "structured.members":
        if domain in {"competition_rules", "rules"} or route.category == "competition_rules":
            return ToolPreconditionResult(capability_id, False, "competition_query_must_not_use_member_directory")
        if domain == "members" or route.category == "members" or looks_like_member_query(question) or looks_like_people_or_role_query(question):
            return ToolPreconditionResult(capability_id, True, "member_query_applicable")
        return ToolPreconditionResult(capability_id, False, "not_a_member_query")

    if capability_id == "structured.games":
        if looks_like_booking_query(question):
            return ToolPreconditionResult(capability_id, False, "booking_query_must_not_use_game_tool")
        if looks_like_explicit_control_query(question):
            return ToolPreconditionResult(capability_id, False, "control_query_must_not_use_game_detail")
        if looks_like_price_query(question):
            return ToolPreconditionResult(capability_id, False, "price_query_must_not_use_game_tool")
        if looks_like_people_or_role_query(question):
            return ToolPreconditionResult(capability_id, False, "people_or_role_query_must_not_use_game_catalog")
        if route.category == "competition_rules" and looks_like_competition_rule_query(question):
            return ToolPreconditionResult(capability_id, False, "competition_rule_query_must_not_use_game_catalog")
        if looks_like_game_zone_ranking_query(question):
            return ToolPreconditionResult(capability_id, True, "game_zone_ranking_requires_game_catalog")
        if looks_like_specific_game_detail_query(question):
            return ToolPreconditionResult(capability_id, True, "specific_game_detail_allowed")
        if looks_like_game_catalog_query(question) or domain == "games":
            return ToolPreconditionResult(capability_id, True, "game_domain_or_catalog_query")
        return ToolPreconditionResult(capability_id, False, "not_a_game_query")

    if capability_id == "structured.game_controls":
        if looks_like_damage_penalty_query(question):
            return ToolPreconditionResult(capability_id, False, "damage_penalty_query_must_not_use_game_controls")
        if domain == "game_controls" or operation == "control" or looks_like_explicit_control_query(question):
            return ToolPreconditionResult(capability_id, True, "game_control_query_applicable")
        return ToolPreconditionResult(capability_id, False, "not_a_game_control_query")

    if capability_id == "structured.equipment":
        if looks_like_general_concept_definition(question):
            return ToolPreconditionResult(capability_id, False, "general_definition_must_not_use_equipment_inventory")
        if looks_like_game_zone_ranking_query(question):
            return ToolPreconditionResult(capability_id, False, "game_zone_ranking_must_not_use_equipment_inventory")
        if looks_like_damage_penalty_query(question):
            return ToolPreconditionResult(capability_id, False, "damage_penalty_query_must_not_use_equipment_tool")
        if looks_like_booking_query(question):
            return ToolPreconditionResult(capability_id, False, "booking_query_must_not_use_equipment_tool")
        if looks_like_price_query(question):
            return ToolPreconditionResult(capability_id, False, "price_query_must_not_use_equipment_tool")
        if looks_like_competition_rule_query(question):
            return ToolPreconditionResult(capability_id, False, "competition_query_must_not_use_equipment_tool")
        if domain == "equipment" or route.category == "equipment" or looks_like_equipment_query(question):
            return ToolPreconditionResult(capability_id, True, "equipment_preconditions_passed")
        return ToolPreconditionResult(capability_id, False, "not_an_equipment_query")

    if capability_id == "structured.reservation":
        if looks_like_price_query(question):
            return ToolPreconditionResult(capability_id, False, "price_query_should_use_calculator_or_service_fee")
        if looks_like_booking_query(question) or domain == "reservation":
            return ToolPreconditionResult(capability_id, True, "reservation_or_booking_query")
        return ToolPreconditionResult(capability_id, False, "not_a_reservation_query")

    if capability_id == "structured.service_fee":
        if looks_like_damage_penalty_query(question):
            return ToolPreconditionResult(capability_id, False, "damage_penalty_query_must_not_use_service_fee")
        if looks_like_known_game_price_query(question):
            return ToolPreconditionResult(capability_id, True, "known_game_price_query_needs_zone_service_mapping")
        if operation == "price_calculate":
            return ToolPreconditionResult(capability_id, False, "price_calculation_should_use_fast_calculator")
        if looks_like_price_query(question) or domain == "service_fee" or operation in {"price_calculate", "price_lookup"}:
            return ToolPreconditionResult(capability_id, True, "service_fee_or_price_query")
        return ToolPreconditionResult(capability_id, False, "not_a_price_query")

    if capability_id == "structured.schedule":
        if looks_like_competition_rule_query(question):
            return ToolPreconditionResult(capability_id, False, "competition_round_query_must_not_use_schedule_tool")
        if looks_like_price_query(question):
            return ToolPreconditionResult(capability_id, False, "price_query_must_not_use_schedule_tool")
        if domain == "schedule" or route.category == "schedule" or looks_like_schedule_query(question):
            return ToolPreconditionResult(capability_id, True, "schedule_query_applicable")
        return ToolPreconditionResult(capability_id, False, "not_a_schedule_query")

    if capability_id == "fast.price_calculator":
        if looks_like_damage_penalty_query(question):
            return ToolPreconditionResult(capability_id, False, "damage_penalty_query_must_not_use_price_calculator")
        if looks_like_price_query(question) or operation in {"price_calculate", "price_lookup"}:
            return ToolPreconditionResult(capability_id, True, "price_calculator_applicable")
        return ToolPreconditionResult(capability_id, False, "not_a_price_or_calculation_query")

    if capability_id == "fast.domain_handlers":
        if route.category == "games" and looks_like_people_or_role_query(question):
            return ToolPreconditionResult(capability_id, False, "people_or_role_query_must_not_use_game_fast_handler")
        if route.category == "competition_rules" and looks_like_competition_rule_query(question):
            return ToolPreconditionResult(capability_id, True, "competition_fast_handler_applicable")
        if route.category not in {"general", "unknown", "no_answer"}:
            return ToolPreconditionResult(capability_id, True, "domain_fast_handler_applicable")
        return ToolPreconditionResult(capability_id, False, "general_route_should_not_use_domain_fast_handler")

    if capability_id == "retrieval.competition_fact_cards":
        if route.category == "competition_rules" or looks_like_competition_rule_query(question):
            return ToolPreconditionResult(capability_id, True, "competition_rule_retrieval_applicable")
        return ToolPreconditionResult(capability_id, False, "not_a_competition_rule_query")

    if capability_id == "llm.general_answer":
        if route.category == "general" and domain in {"general", "knowledge", "unknown"}:
            return ToolPreconditionResult(capability_id, True, "general_llm_applicable")
        return ToolPreconditionResult(capability_id, False, "general_llm_only_for_general_route")

    return ToolPreconditionResult(capability_id, True, "no_specific_precondition")


def evaluate_structured_tool_precondition(
    question: str,
    route: PipelineRoute,
    intent: UniversalIntent | None,
) -> ToolPreconditionResult:
    capability_id = structured_capability_id_for(question, route, intent)
    if capability_id is None:
        return ToolPreconditionResult("structured.unknown", False, "no_structured_capability_for_route")
    return evaluate_capability_precondition(capability_id, question, route, intent)
