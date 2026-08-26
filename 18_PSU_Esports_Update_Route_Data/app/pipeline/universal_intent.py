from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.chatbot_role import CHATBOT_ROLE_TH, INTENT_CLASSIFIER_ROLE
from app.pipeline.game_title_correction import game_alias_entries
from app.pipeline.llm_health import llm_call_allowed, record_llm_failure, record_llm_success, release_llm_slot
from app.pipeline.query_signals import (
    looks_like_clear_general_request,
    looks_like_game_zone_ranking_query,
    looks_like_general_concept_definition,
)
from app.pipeline.request_deadline import deadline_metadata, timeout_for_call
from app.pipeline.schemas import PipelineRoute, PipelineTrace, UniversalIntent


DOMAINS = {
    "members",
    "games",
    "game_controls",
    "equipment",
    "reservation",
    "service_fee",
    "schedule",
    "rules",
    "penalty",
    "competition_rules",
    "contact",
    "knowledge",
    "general",
}

OPERATIONS = {
    "count",
    "list",
    "group_count",
    "group_list",
    "role_lookup",
    "detail",
    "how_to",
    "control",
    "price_calculate",
    "schedule_lookup",
    "rule_lookup",
    "compare",
    "source_lookup",
    "availability",
    "recommendation",
    "general_answer",
    "unknown",
}

_INTENT_LLM_CACHE: dict[str, UniversalIntent | None] = {}

ROUTE_DOMAIN_MAP = {
    "overview": "members",
    "games": "games",
    "equipment": "equipment",
    "reservation": "reservation",
    "service_fee": "service_fee",
    "schedule": "schedule",
    "rules": "rules",
    "penalty": "penalty",
    "competition_rules": "competition_rules",
    "contact": "contact",
    "knowledge": "knowledge",
    "general": "general",
    "unknown": "general",
    "no_answer": "general",
}

DOMAIN_ROUTE_MAP = {
    "members": ("overview", "members_lookup"),
    "games": ("games", "games_lookup"),
    "game_controls": ("games", "game_control_lookup"),
    "equipment": ("equipment", "equipment_lookup"),
    "reservation": ("reservation", "booking_policy"),
    "service_fee": ("service_fee", "service_fee_query"),
    "schedule": ("schedule", "schedule_query"),
    "rules": ("rules", "studio_rules"),
    "penalty": ("penalty", "penalty_policy"),
    "competition_rules": ("competition_rules", "competition_rules_lookup"),
    "contact": ("contact", "contact_lookup"),
    "knowledge": ("knowledge", "knowledge_lookup"),
    "general": ("general", "general_knowledge_query"),
}

OPERATION_INTENT_HINTS = {
    "count": ("กี่", "จำนวน", "ทั้งหมดกี่", "มีกี่", "how many", "count"),
    "group_count": ("กี่หมวด", "กี่กลุ่ม", "กี่หัวข้อ", "แบ่งเป็นกี่", "มีกี่หมวด", "มีกี่กลุ่ม"),
    "group_list": ("หมวดอะไร", "กลุ่มอะไร", "หัวข้ออะไร", "แยกหมวด", "แยกกลุ่ม", "ประเภทอะไร"),
    "role_lookup": (
        "ใครเป็น", "ใครทำ", "คนทำ", "ผู้ทำ", "คนพัฒนา", "ผู้พัฒนา",
        "ใครทำตำแหน่ง", "ตำแหน่ง", "หน้าที่", "รับผิดชอบ", "ทำแชทบอท", "ทำ chatbot",
        "พัฒนาแชทบอท", "พัฒนา chatbot", "สร้างแชทบอท", "สร้าง chatbot",
        "chatbot developer", "ai chat bot developer", "position", "role", "who is",
    ),
    "list": ("มีอะไรบ้าง", "มีอะไรมั่ง", "มีไรบ้าง", "มีไรมั่ง", "มีใครบ้าง", "รายชื่อ", "รายการ", "list", "ทั้งหมด"),
    "detail": ("คืออะไร", "อะไรคือ", "รายละเอียด", "เกี่ยวกับอะไร", "อธิบาย", "รุ่นไหน", "เครื่องรุ่นไหน", "สเปค", "สเป็ค", "spec", "พวงมาลัยอะไร", "แว่นอะไร"),
    "how_to": ("วิธี", "ยังไง", "อย่างไร", "สอน", "ใช้งาน", "เล่นยังไง", "จองยังไง", "ต้องใช้อะไร", "ใช้อะไร", "ใช้อุปกรณ์อะไร"),
    "control": ("ปุ่ม", "จอย", "คอนโทรล", "controller", "control", "กดอะไร"),
    "price_calculate": ("ราคา", "ค่าบริการ", "กี่บาท", "บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "คำนวณ", "ฟรี", "ต้องจ่าย", "จ่ายไหม", "คิดเงิน"),
    "schedule_lookup": ("เปิด", "ปิด", "กี่โมง", "เวลา", "วันไหน", "วันนี้", "พรุ่งนี้"),
    "rule_lookup": ("กฎ", "กติกา", "ห้าม", "ข้อห้าม", "บทลงโทษ", "ลงโทษ", "ค่าปรับ", "โดนปรับ", "ปรับเท่าไหร่", "ของหาย", "อาหาร", "เครื่องดื่ม"),
    "compare": ("ต่างกัน", "เทียบ", "เปรียบเทียบ", "ดีกว่า", "แพงกว่า"),
    "source_lookup": ("แหล่งข้อมูล", "ที่มา", "มาจากไหน", "source"),
    "availability": ("มีไหม", "มีมั้ย", "เล่นได้ไหม", "อยู่ไหม", "ให้เล่นไหม"),
    "recommendation": ("แนะนำ", "ควร", "เหมาะกับ", "ไหนดี"),
}

DOMAIN_HINTS = {
    "members": (
        "สมาชิก", "member", "members", "staff", "สตาฟ", "เจ้าหน้าที่", "คนดูแล", "ทีมงาน", "บุคลากร", "ตำแหน่ง", "อธิการบดี",
        "คณบดี", "ผู้จัดการ", "สหกิจ", "ฝึกงาน", "ชมรม", "กรรมการ",
    ),
    "game_controls": ("ปุ่ม", "จอย", "คอนโทรล", "controller", "control", "กดอะไร"),
    "games": (
        "เกม", "game", "games", "moba", "โมบ้า", "valorant", "rov", "cs2", "tekken",
        "minecraft", "mario", "ps5 มีเกม", "nintendo มีเกม",
    ),
    "equipment": (
        "อุปกรณ์", "เครื่อง", "โซน", "zone", "pc", "ps5", "nintendo", "switch",
        "vr", "cockpit", "พวงมาลัย", "จอ", "เมาส์", "คีย์บอร์ด",
        "logitech", "g923", "racezone", "driving force", "shifter", "tv", "ทีวี",
        "headset", "หูฟัง", "sofa", "โซฟา", "playstation vr2", "ps vr2", "vr2",
        "monitor", "chair", "keyboard", "mouse",
    ),
    "service_fee": ("ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "ฟรี"),
    "schedule": ("เปิด", "ปิด", "กี่โมง", "เวลา", "วันนี้", "พรุ่งนี้", "จันทร์", "ศุกร์"),
    "reservation": ("จอง", "เช็คอิน", "check in", "booking", "session", "รอบ"),
    "rules": ("กฎ", "ห้าม", "ข้อห้าม", "อาหาร", "เครื่องดื่ม", "ของหาย"),
    "penalty": ("เสียหาย", "พัง", "ค่าปรับ", "โดนปรับ", "ชดเชย", "จอแตก", "จอยพัง"),
    "competition_rules": ("กติกา", "แข่งขัน", "ทัวร์", "tournament", "pause", "แผนที่", "ทีมละ"),
    "contact": ("ติดต่อ", "เบอร์", "โทร", "email", "อีเมล", "facebook", "ที่ตั้ง"),
    "knowledge": ("อีสปอร์ต", "esports คือ", "ประเภทเกม", "เกมยอดนิยม", "ประวัติ"),
}


def _truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def _has(q: str, terms: tuple[str, ...]) -> bool:
    return any(term in q for term in terms)


def _compact(value: str) -> str:
    return "".join(ch for ch in normalize_text(value) if ch.isalnum() or "\u0E00" <= ch <= "\u0E7F")


def _has_known_game_alias(q: str) -> bool:
    q_key = _compact(q)
    if not q_key:
        return False
    for entry in game_alias_entries():
        alias_key = entry.compact
        if len(alias_key) < 6:
            continue
        if alias_key in q_key:
            return True
    return False


def _looks_like_game_catalog_request(q: str) -> bool:
    return _has(
        q,
        (
            "มีเกม",
            "เกมอะไร",
            "เกมไร",
            "กี่เกม",
            "รายชื่อเกม",
            "รายการเกม",
            "เกมทั้งหมด",
            "เล่นอะไรได้บ้าง",
            "เล่นเกมอะไร",
            "game list",
            "list game",
            "all games",
        ),
    )


def _has_people_or_role_signal(q: str) -> bool:
    return _has(
        q,
        (
            "สมาชิก", "member", "members", "staff", "สตาฟ", "เจ้าหน้าที่", "คนดูแล",
            "ทีมงาน", "บุคลากร", "ตำแหน่ง", "ผู้จัดการ", "สหกิจ", "ฝึกงาน",
            "ใคร", "ใครบ้าง", "ใครทำ", "ใครเป็น", "คนทำ", "ผู้ทำ", "คนพัฒนา", "ผู้พัฒนา",
            "แชทบอท", "chatbot", "chat bot", "บอท",
        ),
    )


def _has_member_game_relation_signal(q: str) -> bool:
    if _has(q, ("ตำแหน่ง", "position", "role")):
        return False
    if _has(q, OPERATION_INTENT_HINTS["price_calculate"]):
        return False
    has_relation = _has(q, ("เล่น", "ดูแล", "รับผิดชอบ", "ประจำ", "คุม"))
    has_game_or_zone = _has(
        q,
        (
            "เกม", "game", "games", "ps5", "playstation", "nintendo", "switch",
            "pc", "vr", "cockpit", "โซน", "เครื่อง",
        ),
    )
    return _has_people_or_role_signal(q) and has_relation and has_game_or_zone


def _has_known_equipment_item_alias(q: str) -> bool:
    return _has(
        q,
        (
            "gaming pc", "msi mag infinite", "gaming monitor", "gaming keyboard", "gaming mouse",
            "gaming headset", "gaming chair", "logitech g923", "trueforce", "racing wheel",
            "driving force shifter", "gear shifter", "shifter", "racezone", "full cockpit",
            "pulse elite", "wireless headset", "nintendo switch oled", "switch oled",
            "playstation 5 slim", "ultra hd blu-ray", "playstation vr2", "psvr2", "vr2",
            "tv 65", "tv 86", "ทีวี 65", "ทีวี 86", "65 นิ้ว", "86 นิ้ว",
            "sofa 2", "sofa", "โซฟา",
        ),
    )


def _score_domain(q: str, route: PipelineRoute) -> tuple[str, float, str]:
    game_operation_terms = (
        "มีเกม", "เกมใน", "เกมบน", "เกมของ", "เกมอะไร", "เกมไร", "เกมกี่", "กี่เกม", "รายชื่อเกม",
        "รายการเกม", "เล่นเกมอะไร", "เล่นอะไรได้บ้าง", "list game", "games",
    )
    if _has_member_game_relation_signal(q):
        return "members", 0.90, "member-game responsibility/play relation needs member-domain no-data policy"
    if (
        _has(q, game_operation_terms)
        and not _has(q, ("อุปกรณ์อะไร", "เครื่องอะไร", "มีอุปกรณ์"))
        and not _has_people_or_role_signal(q)
    ):
        return "games", 0.90, "game catalog/count terms override zone/equipment domain"
    if _has_known_equipment_item_alias(q):
        return "equipment", 0.92, "known equipment item alias found"
    if _has_known_game_alias(q):
        return "games", 0.90, "known game alias found"

    scores: dict[str, int] = {}
    for domain, terms in DOMAIN_HINTS.items():
        scores[domain] = sum(1 for term in terms if term in q)

    route_domain = ROUTE_DOMAIN_MAP.get(route.category, "general")
    scores[route_domain] = scores.get(route_domain, 0) + 2

    best_domain, best_score = max(scores.items(), key=lambda item: item[1])
    if best_score <= 0:
        return route_domain, 0.45, "no domain terms; using route domain"
    confidence = min(0.94, 0.58 + best_score * 0.08)
    return best_domain, confidence, f"domain_terms={best_score}"


def _score_operation(q: str) -> tuple[str, float, str, tuple[str, ...]]:
    scores: dict[str, int] = {}
    for operation, terms in OPERATION_INTENT_HINTS.items():
        scores[operation] = sum(1 for term in terms if term in q)

    # More specific operations should beat broad operations.
    if _has(q, ("จ่ายภายใน", "ชำระภายใน", "โอนเงิน", "สลิป", "เลขบัญชี", "ธนาคาร", "ลืมจ่าย", "ไม่จ่าย", "หลังจองต้องจ่าย")):
        if _has(q, ("กี่นาที", "กี่ นาที", "ภายในกี่")):
            return "count", 0.91, "payment deadline count terms found", ("lookup_payment_deadline",)
        return "rule_lookup", 0.89, "payment policy terms found", ("lookup_payment_policy",)
    game_name_availability_terms = (
        "minecraft", "มายคราฟ", "roblox", "โรบล็อก", "tekken", "เทคเคน", "mario", "มาริโอ",
        "fortnite", "valorant", "rov", "beat saber", "gran turismo", "warzone", "pubg",
    )
    if _has(q, ("ไหม", "มั้ย", "มีไหม", "มีมั้ย", "ให้เล่นไหม", "เล่นได้ไหม")) and _has(q, game_name_availability_terms):
        return "availability", 0.88, "named game availability terms found", ("check_availability",)
    if _has(q, ("เครื่องไหน", "โซนไหน", "zone ไหน", "เล่นที่ไหน", "เล่นได้ที่ไหน", "อยู่โซน", "อยู่เครื่อง")) and _has_known_game_alias(q):
        return "availability", 0.88, "named game location/availability terms found", ("check_availability",)
    if scores.get("group_count", 0) or (_has(q, ("กี่", "มีกี่")) and _has(q, ("หมวด", "กลุ่ม", "หัวข้อ", "ประเภท"))):
        return "group_count", 0.94, "group count terms found", ("count_groups", "list_group_names", "count_items_per_group")
    if scores.get("group_list", 0):
        return "group_list", 0.92, "group list terms found", ("list_group_names", "count_items_per_group")
    if scores.get("role_lookup", 0):
        return "role_lookup", 0.92, "role/position lookup terms found", ("lookup_people_by_role",)
    if scores.get("price_calculate", 0):
        return "price_calculate", 0.93, "price terms found", ("calculate_price", "show_price_breakdown")
    if scores.get("control", 0):
        return "control", 0.91, "control terms found", ("list_controls",)
    if scores.get("schedule_lookup", 0):
        return "schedule_lookup", 0.90, "schedule terms found", ("lookup_schedule",)
    if scores.get("rule_lookup", 0):
        return "rule_lookup", 0.89, "rule terms found", ("lookup_rule",)
    if scores.get("how_to", 0):
        return "how_to", 0.87, "how-to terms found", ("steps", "controls_if_game")
    if scores.get("compare", 0):
        return "compare", 0.86, "compare terms found", ("compare_items",)
    if scores.get("source_lookup", 0):
        return "source_lookup", 0.86, "source terms found", ("show_sources",)
    if scores.get("availability", 0):
        return "availability", 0.86, "availability terms found", ("check_availability",)
    if scores.get("count", 0):
        return "count", 0.84, "count terms found", ("count_items",)
    if scores.get("list", 0) or _has(q, ("มีเกมอะไรบ้าง", "มีเกมไรบ้าง", "เล่นเกมอะไรได้บ้าง", "เล่นอะไรได้บ้าง")):
        return "list", 0.82, "list terms found", ("list_items",)
    if scores.get("detail", 0):
        return "detail", 0.80, "detail terms found", ("summarize_detail",)
    if scores.get("recommendation", 0):
        return "recommendation", 0.72, "recommendation terms found", ("recommend",)
    return "unknown", 0.45, "no clear operation terms", ()


def _operation_signal_scores(q: str) -> dict[str, int]:
    return {
        operation: sum(1 for term in terms if term in q)
        for operation, terms in OPERATION_INTENT_HINTS.items()
    }


def _answer_style_for(operation: str) -> str:
    if operation in {"list", "group_list", "group_count", "compare"}:
        return "summary_bullets"
    if operation in {"how_to", "control", "price_calculate", "schedule_lookup", "role_lookup"}:
        return "direct_then_details"
    return "direct"


def _heuristic_intent(query: str, route: PipelineRoute) -> UniversalIntent:
    if route.intent == "chatbot_greeting":
        return UniversalIntent(
            domain="knowledge",
            operation="detail",
            target="chatbot_greeting",
            filters={},
            needs=("greet_user", "offer_capabilities"),
            answer_style="direct",
            confidence=0.98,
            method="heuristic",
            reason="chatbot greeting route is locked to assistant role",
        )
    if route.intent == "chatbot_identity":
        return UniversalIntent(
            domain="knowledge",
            operation="detail",
            target="chatbot_identity",
            filters={},
            needs=("describe_capabilities", "state_scope"),
            answer_style="summary_bullets",
            confidence=0.97,
            method="heuristic",
            reason="chatbot identity route is locked to assistant role",
        )
    q = normalize_text(query)
    if looks_like_game_zone_ranking_query(q):
        return UniversalIntent(
            domain="games",
            operation="list",
            target="game_zone_counts",
            needs=("rank_game_counts_by_zone",),
            answer_style="summary_bullets",
            confidence=0.99,
            method="heuristic",
            reason="deterministic game-zone ranking operation overrides equipment words",
        )
    if route.category == "general" and (
        looks_like_general_concept_definition(q) or looks_like_clear_general_request(q)
    ):
        return UniversalIntent(
            domain="general",
            operation="detail",
            target="general_concept",
            needs=("answer_general_question",),
            answer_style="direct",
            confidence=0.94,
            method="heuristic",
            reason="general concept definition overrides equipment entity words",
        )
    domain, domain_confidence, domain_reason = _score_domain(q, route)
    operation, operation_confidence, operation_reason, needs = _score_operation(q)
    if route.category in {"rules", "penalty"} or route.intent in {"studio_rules", "penalty_policy"}:
        domain = "penalty" if route.category == "penalty" or route.intent == "penalty_policy" else "rules"
        operation = "rule_lookup"
        domain_confidence = max(domain_confidence, 0.92)
        operation_confidence = max(operation_confidence, 0.90)
        domain_reason = f"{domain_reason}; rules/penalty route overrides price/control ambiguity"
        operation_reason = f"{operation_reason}; policy lookup forced by rules/penalty route"
        needs = ("lookup_rule",)
    elif route.category == "competition_rules" or route.intent == "competition_rules_lookup":
        domain = "competition_rules"
        operation = "rule_lookup"
        domain_confidence = max(domain_confidence, 0.94)
        operation_confidence = max(operation_confidence, 0.90)
        domain_reason = f"{domain_reason}; competition route overrides game/count ambiguity"
        operation_reason = f"{operation_reason}; competition route forces rule lookup"
        needs = ("lookup_competition_rule",)
    elif route.category == "overview" or route.intent in {"members_lookup", "group_count", "group_list"}:
        domain = "members"
        domain_confidence = max(domain_confidence, 0.90)
        domain_reason = f"{domain_reason}; member route keeps members domain"
        if operation == "unknown":
            if route.intent == "group_count":
                operation = "group_count"
                needs = ("count_groups", "list_group_names")
            elif route.intent == "group_list":
                operation = "group_list"
                needs = ("list_group_names", "count_items_per_group")
            else:
                operation = "list"
                needs = ("list_people",)
            operation_confidence = max(operation_confidence, 0.82)
            operation_reason = f"{operation_reason}; member route supplied operation={operation}"
    elif route.category == "reservation" or route.intent in {"booking_policy", "booking_session_limit", "checkin_policy", "payment_policy"}:
        domain = "reservation"
        domain_confidence = max(domain_confidence, 0.90)
        domain_reason = f"{domain_reason}; reservation route overrides entity/game domain"
        if operation == "unknown":
            operation = "how_to"
            operation_confidence = max(operation_confidence, 0.82)
            operation_reason = f"{operation_reason}; reservation unknown treated as how_to/policy"
            needs = ("steps", "policy")
    elif route.category == "equipment" and operation in {"unknown", "count", "list"}:
        domain = "equipment"
        operation = "count" if operation == "count" else "list"
        domain_confidence = max(domain_confidence, 0.86)
        operation_confidence = max(operation_confidence, 0.82)
        domain_reason = f"{domain_reason}; equipment route keeps equipment domain"
        operation_reason = f"{operation_reason}; equipment route supplies equipment operation"
        needs = ("count_items",) if operation == "count" else ("list_items",)
    elif route.category == "schedule" and operation == "unknown":
        domain = "schedule"
        operation = "schedule_lookup"
        domain_confidence = max(domain_confidence, 0.88)
        operation_confidence = max(operation_confidence, 0.86)
        domain_reason = f"{domain_reason}; schedule route keeps schedule domain"
        operation_reason = f"{operation_reason}; schedule unknown treated as schedule_lookup"
        needs = ("lookup_schedule",)
    elif route.category == "service_fee" and operation == "unknown":
        domain = "service_fee"
        operation = "price_calculate"
        domain_confidence = max(domain_confidence, 0.88)
        operation_confidence = max(operation_confidence, 0.84)
        domain_reason = f"{domain_reason}; service fee route keeps service_fee domain"
        operation_reason = f"{operation_reason}; service fee unknown treated as price_calculate"
        needs = ("calculate_price", "show_price_breakdown")
    elif route.category == "service_fee" and operation in {"price_calculate", "compare"}:
        domain = "service_fee"
        operation = "price_calculate"
        domain_confidence = max(domain_confidence, 0.93)
        operation_confidence = max(operation_confidence, 0.90)
        domain_reason = f"{domain_reason}; service fee route overrides member/equipment hints"
        operation_reason = f"{operation_reason}; service fee route keeps price operation"
        needs = ("calculate_price", "show_price_breakdown")
    elif _has_member_game_relation_signal(q):
        domain = "members"
        operation = "list"
        domain_confidence = max(domain_confidence, 0.90)
        operation_confidence = max(operation_confidence, 0.82)
        domain_reason = f"{domain_reason}; member-game relation keeps members domain"
        operation_reason = f"{operation_reason}; member-game relation uses no-data list policy"
        needs = ("list_people", "report_missing_member_game_relation")
    elif domain == "games" and operation == "unknown" and _has_known_game_alias(q) and not _looks_like_game_catalog_request(q):
        operation = "detail"
        domain_confidence = max(domain_confidence, 0.88)
        operation_confidence = max(operation_confidence, 0.84)
        domain_reason = f"{domain_reason}; known game title keeps games domain"
        operation_reason = f"{operation_reason}; bare known game title treated as detail"
        needs = ("summarize_detail", "check_availability")
    elif route.intent in {"game_availability_lookup", "games_lookup", "game_catalog_lookup", "competition_game_list"} and operation == "unknown":
        domain = "games"
        if route.intent == "game_availability_lookup":
            operation = "availability"
        elif _has_known_game_alias(q) and not _looks_like_game_catalog_request(q):
            operation = "detail"
        else:
            operation = "list"
        domain_confidence = max(domain_confidence, 0.86)
        operation_confidence = max(operation_confidence, 0.84)
        domain_reason = f"{domain_reason}; game route keeps games domain"
        operation_reason = f"{operation_reason}; game route intent supplies operation"
        if operation == "availability":
            needs = ("check_availability",)
        elif operation == "detail":
            needs = ("summarize_detail", "check_availability")
        else:
            needs = ("list_items",)
    elif route.category == "general" and operation == "schedule_lookup":
        domain = "general"
        operation = "detail"
        domain_confidence = max(domain_confidence, 0.80)
        operation_confidence = max(operation_confidence, 0.80)
        domain_reason = f"{domain_reason}; general route keeps general domain"
        operation_reason = f"{operation_reason}; schedule-like word in general query treated as detail"
        needs = ("answer_general_question",)
    elif operation == "price_calculate" or route.intent == "service_fee_query":
        domain = "service_fee"
        domain_confidence = max(domain_confidence, 0.92)
        domain_reason = f"{domain_reason}; price operation overrides entity/game domain"
    elif operation == "control":
        domain = "game_controls"
        domain_confidence = max(domain_confidence, 0.90)
        domain_reason = f"{domain_reason}; control operation overrides domain"
    confidence = min(domain_confidence, operation_confidence)
    if operation == "unknown":
        confidence = min(confidence, 0.50)
    return UniversalIntent(
        domain=domain,
        operation=operation,
        target="",
        filters={},
        needs=needs,
        answer_style=_answer_style_for(operation),
        confidence=round(confidence, 3),
        method="heuristic",
        reason=f"{domain_reason}; {operation_reason}",
    )


def _extract_json_object(text: str) -> dict[str, Any] | None:
    text = text.strip()
    if not text:
        return None
    try:
        value = json.loads(text)
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        value = json.loads(text[start:end + 1])
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        return None


def _coerce_llm_intent(data: dict[str, Any], fallback: UniversalIntent) -> UniversalIntent:
    domain = str(data.get("domain") or fallback.domain).strip().lower()
    operation = str(data.get("operation") or fallback.operation).strip().lower()
    if domain not in DOMAINS:
        domain = fallback.domain
    if operation not in OPERATIONS:
        operation = fallback.operation
    if operation == "control" and domain != "game_controls":
        operation = "how_to" if domain == "equipment" else fallback.operation
    raw_confidence = data.get("confidence", fallback.confidence)
    try:
        confidence = float(raw_confidence)
    except (TypeError, ValueError):
        confidence = fallback.confidence
    confidence = max(0.0, min(0.98, confidence))
    needs_raw = data.get("needs") or fallback.needs
    if isinstance(needs_raw, list):
        needs = tuple(str(item) for item in needs_raw if str(item).strip())
    elif isinstance(needs_raw, tuple):
        needs = tuple(str(item) for item in needs_raw if str(item).strip())
    else:
        needs = fallback.needs
    filters = data.get("filters") if isinstance(data.get("filters"), dict) else fallback.filters
    return UniversalIntent(
        domain=domain,
        operation=operation,
        target=str(data.get("target") or fallback.target or "").strip(),
        filters=filters,
        needs=needs,
        answer_style=str(data.get("answer_style") or _answer_style_for(operation)),
        confidence=round(confidence, 3),
        method="llm",
        reason=str(data.get("reason") or "llm json parser"),
    )


def _intent_candidate(
    candidate_id: str,
    domain: str,
    operation: str,
    reason: str,
    confidence: float,
) -> dict[str, Any]:
    if domain not in DOMAINS:
        domain = "general"
    if operation not in OPERATIONS:
        operation = "unknown"
    if operation == "control" and domain != "game_controls":
        operation = "how_to" if domain == "equipment" else "unknown"
    return {
        "id": candidate_id,
        "domain": domain,
        "operation": operation,
        "answer_style": _answer_style_for(operation),
        "confidence": round(max(0.0, min(0.98, confidence)), 3),
        "reason": reason,
    }


def _add_candidate(
    candidates: list[dict[str, Any]],
    seen: set[tuple[str, str]],
    domain: str,
    operation: str,
    reason: str,
    confidence: float,
) -> None:
    if operation == "control" and domain != "game_controls":
        operation = "how_to" if domain == "equipment" else "unknown"
    key = (domain, operation)
    if key in seen or domain not in DOMAINS or operation not in OPERATIONS:
        return
    seen.add(key)
    candidates.append(_intent_candidate(f"c{len(candidates) + 1}", domain, operation, reason, confidence))


def _candidate_operation_from_query(q: str, fallback_operation: str) -> str:
    if _has(q, ("ปุ่ม", "กดปุ่ม", "จอย", "controller", "button", "control")):
        return "control"
    if _has(q, ("ราคา", "กี่บาท", "เสียเงิน", "cost", "fee", "price")):
        return "price_calculate"
    if _has(q, ("กี่โมง", "เปิด", "ปิด", "เวลา", "schedule", "open")):
        return "schedule_lookup"
    if _has(q, ("เล่นยังไง", "ใช้ยังไง", "ต้องใช้อะไร", "วิธี", "how")):
        return "how_to"
    if _has(q, ("มีอะไร", "อะไรบ้าง", "มีไร", "list", "บ้าง")):
        return "list"
    return fallback_operation if fallback_operation != "unknown" else "detail"


def _build_intent_candidates(query: str, route: PipelineRoute, fallback: UniversalIntent) -> list[dict[str, Any]]:
    q = normalize_text(query)
    candidates: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    _add_candidate(candidates, seen, fallback.domain, fallback.operation, "heuristic fallback", fallback.confidence)

    route_domain = ROUTE_DOMAIN_MAP.get(route.category, fallback.domain)
    query_operation = _candidate_operation_from_query(q, fallback.operation)
    _add_candidate(candidates, seen, route_domain, query_operation, "router category candidate", route.confidence)

    domain_scores = _domain_signal_scores(q)
    for domain, score in sorted(domain_scores.items(), key=lambda item: item[1], reverse=True):
        if score <= 0 or len(candidates) >= 6:
            continue
        _add_candidate(candidates, seen, domain, query_operation, f"domain keyword score={score}", min(0.92, 0.58 + score * 0.08))

    operation_scores = _operation_signal_scores(q)
    for operation, score in sorted(operation_scores.items(), key=lambda item: item[1], reverse=True):
        if score <= 0 or len(candidates) >= 6:
            continue
        _add_candidate(candidates, seen, fallback.domain, operation, f"operation keyword score={score}", min(0.92, 0.58 + score * 0.08))

    if _has(q, ("รถแข่ง", "พวงมาลัย", "cockpit", "logitech", "g923", "แข่งรถ")):
        _add_candidate(candidates, seen, "equipment", "how_to", "racing/cockpit equipment phrase", 0.88)
        if not _has(q, ("ต้องใช้อะไร", "ใช้อะไร", "ใช้อุปกรณ์อะไร", "อุปกรณ์อะไร", "เครื่องอะไร")):
            _add_candidate(candidates, seen, "games", "recommendation", "racing game phrase", 0.74)
    if _has(q, ("คนดูแล", "สตาฟ", "staff", "ทีมงาน", "บุคลากร")):
        _add_candidate(candidates, seen, "members", "list", "staff/member phrase", 0.88)
    if _has_member_game_relation_signal(q):
        _add_candidate(candidates, seen, "members", "list", "member-game relation phrase", 0.90)
    if _has(q, ("ตีป้อม", "โมบ้า", "moba")):
        _add_candidate(candidates, seen, "games", "list", "MOBA/game genre phrase", 0.88)
    if _has(q, ("ปุ่ม", "จอย", "controller", "button")):
        _add_candidate(candidates, seen, "game_controls", "control", "controller/button phrase", 0.88)
        _add_candidate(candidates, seen, "equipment", "how_to", "controller equipment phrase", 0.72)

    if not candidates:
        _add_candidate(candidates, seen, "general", "general_answer", "fallback general answer", 0.55)
    return candidates[:6]


def _intent_from_candidate(data: dict[str, Any], candidates: list[dict[str, Any]], fallback: UniversalIntent) -> UniversalIntent:
    by_id = {str(candidate["id"]): candidate for candidate in candidates}
    selected = by_id.get(str(data.get("candidate_id") or data.get("selected") or "").strip())
    if selected is None:
        domain = str(data.get("domain") or "").strip().lower()
        operation = str(data.get("operation") or "").strip().lower()
        selected = next(
            (
                candidate
                for candidate in candidates
                if candidate["domain"] == domain and candidate["operation"] == operation
            ),
            None,
        )
    if selected is None:
        return _coerce_llm_intent(data, fallback)

    try:
        confidence = float(data.get("confidence", selected.get("confidence", fallback.confidence)))
    except (TypeError, ValueError):
        confidence = float(selected.get("confidence", fallback.confidence))
    confidence = max(0.0, min(0.98, confidence))
    needs_raw = data.get("needs") or []
    needs = tuple(str(item) for item in needs_raw if str(item).strip()) if isinstance(needs_raw, list) else ()
    return UniversalIntent(
        domain=str(selected["domain"]),
        operation=str(selected["operation"]),
        target=str(data.get("target") or "").strip(),
        filters=data.get("filters") if isinstance(data.get("filters"), dict) else {},
        needs=needs,
        answer_style=str(data.get("answer_style") or selected.get("answer_style") or _answer_style_for(str(selected["operation"]))),
        confidence=round(confidence, 3),
        method="llm",
        reason=f"candidate_intent:{selected['id']} {data.get('reason') or selected.get('reason') or ''}".strip(),
    )


def _llm_intent(query: str, route: PipelineRoute, fallback: UniversalIntent) -> tuple[UniversalIntent | None, dict[str, Any]]:
    url = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/") + "/api/generate"
    model = os.getenv("PSU_INTENT_LLM_MODEL") or os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
    configured_timeout = float(os.getenv("PSU_INTENT_LLM_TIMEOUT_SEC", "8"))
    timeout = timeout_for_call(configured_timeout)
    num_predict = int(os.getenv("PSU_INTENT_LLM_NUM_PREDICT", "50"))
    num_ctx = max(
        1024,
        int(os.getenv("PSU_INTENT_LLM_NUM_CTX", os.getenv("PSU_GENERAL_LLM_NUM_CTX", "3072"))),
    )
    candidates = _build_intent_candidates(query, route, fallback)
    cache_key = json.dumps(
        {
            "model": model,
            "version": "candidate_v3_adaptive_default",
            "query": normalize_text(query),
            "route": f"{route.category}/{route.intent}",
            "fallback": f"{fallback.domain}/{fallback.operation}",
            "candidates": [(item["id"], item["domain"], item["operation"]) for item in candidates],
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    call_metadata: dict[str, Any] = {
        "llm_kind": "universal_intent",
        "llm_model": model,
        "llm_timeout_sec": timeout,
        "llm_configured_timeout_sec": configured_timeout,
        "llm_num_predict": num_predict,
        "llm_num_ctx": num_ctx,
        "llm_cache_hit": False,
        **deadline_metadata(),
    }
    if cache_key in _INTENT_LLM_CACHE:
        cached = _INTENT_LLM_CACHE[cache_key]
        return cached, {
            **call_metadata,
            "llm_cache_hit": True,
            "llm_elapsed_ms": 0.0,
            "llm_response_chars": 0,
            "llm_parsed": cached is not None,
        }
    allowed, health = llm_call_allowed("universal_intent", model)
    call_metadata.update(health)
    if not allowed:
        return None, {
            **call_metadata,
            "llm_prompt_chars": 0,
            "llm_elapsed_ms": 0.0,
            "llm_response_chars": 0,
            "llm_parsed": False,
            "llm_skipped_by_health": True,
            **health,
        }
    if timeout <= 0:
        release_llm_slot()
        return None, {
            **call_metadata,
            "llm_prompt_chars": 0,
            "llm_elapsed_ms": 0.0,
            "llm_response_chars": 0,
            "llm_parsed": False,
            "llm_skipped_by_deadline": True,
        }

    candidates_json = json.dumps(candidates, ensure_ascii=False, separators=(",", ":"))
    prompt = f"""Select the best intent candidate for a PSU Esports chatbot. Return JSON only.
Question: {query}
Router: {route.category}/{route.intent}
Heuristic: {fallback.domain}/{fallback.operation}
Candidates: {candidates_json}
Rules:
- Choose exactly one candidate_id from Candidates.
- If asking what equipment/device to use, prefer equipment/how_to.
- If the question contains "ต้องใช้อะไร" or "ใช้อุปกรณ์อะไร", choose equipment/how_to.
- If asking controller buttons for a named game, prefer game_controls/control.
- If asking people/staff/roles, prefer members.
- If asking available games or game genres, prefer games.
Return exactly: {{"candidate_id":"c1","confidence":0.9,"reason":"short"}}"""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "keep_alive": os.getenv("PSU_OLLAMA_KEEP_ALIVE", "10m"),
        "options": {
            "temperature": 0,
            "num_predict": num_predict,
            "num_ctx": num_ctx,
        },
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    request_started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
    except (OSError, TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
        elapsed_ms = (time.perf_counter() - request_started) * 1000
        health = record_llm_failure(
            "universal_intent",
            model,
            error_type=type(exc).__name__,
            error=str(exc),
            elapsed_ms=elapsed_ms,
        )
        return None, {
            **call_metadata,
            "llm_prompt_chars": len(prompt),
            "llm_elapsed_ms": round(elapsed_ms, 2),
            "llm_response_chars": 0,
            "llm_parsed": False,
            "llm_error_type": type(exc).__name__,
            "llm_error": str(exc),
            **health,
        }
    response_text = str(data.get("response") or "")
    parsed = _extract_json_object(response_text)
    elapsed_ms = (time.perf_counter() - request_started) * 1000
    if parsed:
        health = record_llm_success("universal_intent", model, elapsed_ms=elapsed_ms)
    else:
        health = record_llm_failure(
            "universal_intent",
            model,
            error_type="NoParse",
            error="llm returned no parseable JSON",
            elapsed_ms=elapsed_ms,
        )
    response_metadata = {
        **call_metadata,
        "llm_prompt_chars": len(prompt),
        "llm_elapsed_ms": round(elapsed_ms, 2),
        "llm_response_chars": len(response_text),
        "llm_done_reason": data.get("done_reason") or "",
        "llm_parsed": bool(parsed),
        **health,
    }
    if not parsed:
        return None, response_metadata
    result = _intent_from_candidate(parsed, candidates, fallback)
    _INTENT_LLM_CACHE[cache_key] = result
    return result, response_metadata


def _llm_first_enabled(allow_llm: bool) -> bool:
    return (
        allow_llm
        and _truthy(os.getenv("PSU_UNIVERSAL_INTENT_LLM", "1"))
        and _truthy(os.getenv("PSU_UNIVERSAL_INTENT_LLM_FIRST", "1"))
    )


def _llm_first_only_for_weak_routes() -> bool:
    return _truthy(os.getenv("PSU_INTENT_LLM_FIRST_ONLY_WEAK", "1"))


def _domain_signal_scores(q: str) -> dict[str, int]:
    return {
        domain: sum(1 for term in terms if term in q)
        for domain, terms in DOMAIN_HINTS.items()
    }


def _has_competing_domain_signals(q: str) -> bool:
    positive = sorted(
        (score for score in _domain_signal_scores(q).values() if score > 0),
        reverse=True,
    )
    return len(positive) >= 2 and positive[1] >= max(1, positive[0] - 1)


def _looks_like_clear_platform_game_catalog(q: str) -> bool:
    return (
        _has(q, ("มีเกม", "เกมอะไร", "เกมไร", "รายชื่อเกม", "รายการเกม", "เล่นเกมอะไร"))
        and _has(q, ("ps5", "playstation", "nintendo", "switch", "pc", "vr", "cockpit", "โซน"))
        and not _has(q, ("อุปกรณ์", "เครื่อง", "รุ่น", "จอย", "ปุ่ม"))
    )


def _intent_candidate_margin(candidates: list[dict[str, Any]]) -> float | None:
    ranked = sorted(
        (
            candidate
            for candidate in candidates
            if isinstance(candidate.get("confidence"), (int, float))
        ),
        key=lambda item: float(item["confidence"]),
        reverse=True,
    )
    if len(ranked) < 2:
        return None
    return float(ranked[0]["confidence"]) - float(ranked[1]["confidence"])


def _intent_review_risk_flags(query: str, route: PipelineRoute, heuristic: UniversalIntent) -> tuple[str, ...]:
    q = normalize_text(query)
    flags: list[str] = []
    broad_operations = {"list", "detail", "how_to", "availability", "recommendation", "unknown"}

    if _looks_like_clear_platform_game_catalog(q):
        return ()

    if _has_member_game_relation_signal(q):
        flags.append("people_or_role_signal_conflicts_with_domain")

    if _has_competing_domain_signals(q):
        flags.append("competing_domain_signals")

    if _has_people_or_role_signal(q) and heuristic.domain != "members":
        flags.append("people_or_role_signal_conflicts_with_domain")

    competition_terms = (
        "รอบชิง", "รอบรอง", "รอบแบ่งกลุ่ม", "กติกา", "แข่งขัน", "ทัวร์",
        "tournament", "bo1", "bo3", "best of", "ทีมละ", "ตัวสำรอง",
    )
    if _has(q, competition_terms) and heuristic.domain not in {"competition_rules", "rules", "penalty"}:
        flags.append("competition_signal_conflicts_with_domain")

    candidates = _build_intent_candidates(query, route, heuristic)
    margin = _intent_candidate_margin(candidates)
    if (
        margin is not None
        and margin < float(os.getenv("PSU_INTENT_REVIEW_CANDIDATE_MARGIN", "0.12"))
        and heuristic.operation in broad_operations
    ):
        flags.append("low_candidate_margin")

    return tuple(dict.fromkeys(flags))


def _needs_llm_intent_review(query: str, route: PipelineRoute, heuristic: UniversalIntent) -> tuple[bool, str]:
    if not _truthy(os.getenv("PSU_INTENT_REVIEW_BROAD_ROUTES", "1")):
        return False, ""
    q = normalize_text(query)
    if looks_like_game_zone_ranking_query(q) and heuristic.confidence >= 0.90:
        return False, ""
    exact_operations = {
        "price_calculate",
        "control",
        "schedule_lookup",
        "role_lookup",
        "group_count",
    }
    if heuristic.operation in exact_operations and heuristic.confidence >= 0.80:
        return False, ""
    if (
        route.category == "general"
        and route.intent == "general_knowledge_query"
        and heuristic.domain == "general"
        and heuristic.operation != "unknown"
        and heuristic.confidence >= 0.70
    ):
        return False, ""
    if route.category in {"general", "unknown", "no_answer"}:
        return True, "weak route should be reviewed by LLM intent"
    risk_flags = _intent_review_risk_flags(query, route, heuristic)
    if risk_flags:
        return True, f"{', '.join(risk_flags)} should be reviewed by LLM intent"
    if heuristic.domain == "games" and heuristic.operation == "list" and _looks_like_clear_platform_game_catalog(q):
        return False, ""

    broad_operations = {"list", "detail", "how_to", "availability", "recommendation", "unknown"}
    broad_route_intents = {
        "members_lookup",
        "games_lookup",
        "game_catalog_lookup",
        "game_detail_lookup",
        "equipment_lookup",
        "equipment_game_catalog",
        "knowledge_lookup",
        "overview_lookup",
        "related_guidance",
    }
    broad_terms = (
        "อะไร", "อะไรบ้าง", "มีไร", "มีอะไร", "ยังไง", "อย่างไร", "เล่นยังไง",
        "อยาก", "ขอ", "แนะนำ", "ตอนนี้", "บ้าง", "ไหน", "ทำอะไร",
        "what", "how", "which", "list", "recommend",
    )
    if (
        heuristic.operation in broad_operations
        and (route.intent in broad_route_intents or _has(q, broad_terms))
    ):
        return True, "broad list/detail/how-to route should be reviewed by LLM intent"
    return False, ""


def _skip_llm_first_for_strong_route(route: PipelineRoute, heuristic: UniversalIntent, query: str = "") -> tuple[bool, str]:
    if not _llm_first_only_for_weak_routes():
        return False, ""
    if route.intent == "booking_session_limit" and heuristic.domain == "reservation":
        return True, "booking session limit skips LLM-first"
    if looks_like_game_zone_ranking_query(query) and heuristic.confidence >= 0.90:
        return True, "deterministic game-zone ranking skips LLM intent review"
    if route.category == "general" and looks_like_clear_general_request(query):
        return True, "clear general request reserves the single LLM call for answer generation"
    if (
        heuristic.operation == "how_to"
        and heuristic.domain in {"reservation", "service_fee", "schedule", "equipment"}
        and route.category in {"reservation", "service_fee", "schedule", "equipment"}
        and route.confidence >= 0.88
        and heuristic.confidence >= 0.86
    ):
        return True, "strong operational how-to route skips LLM-first"
    exact_skip_operations = {
        "price_calculate",
        "control",
        "schedule_lookup",
        "role_lookup",
        "group_count",
    }
    if (
        heuristic.operation in exact_skip_operations
        and heuristic.confidence >= 0.80
        and route.confidence >= 0.88
    ):
        return True, "specific exact operation skips LLM-first"
    if (
        route.category == "general"
        and route.intent == "general_knowledge_query"
        and heuristic.domain == "general"
        and heuristic.operation != "unknown"
        and heuristic.confidence >= 0.70
    ):
        return True, "clear general knowledge route skips LLM-first"
    needs_review, review_reason = _needs_llm_intent_review(query, route, heuristic)
    if needs_review:
        return False, review_reason
    q = normalize_text(query)
    if (
        heuristic.domain == "games"
        and heuristic.operation == "list"
        and _looks_like_clear_platform_game_catalog(q)
        and route.confidence >= 0.88
        and heuristic.confidence >= 0.80
    ):
        return True, "clear platform game catalog skips LLM-first"
    high_trust_categories = {
        "overview",
        "games",
        "equipment",
        "reservation",
        "service_fee",
        "schedule",
        "knowledge",
        "contact",
        "competition_rules",
    }
    route_threshold = float(os.getenv("PSU_INTENT_STRONG_ROUTE_SKIP_LLM_CONFIDENCE", "0.88"))
    heuristic_threshold = float(os.getenv("PSU_INTENT_STRONG_HEURISTIC_SKIP_LLM_CONFIDENCE", "0.86"))
    if (
        route.category in high_trust_categories
        and route.confidence >= route_threshold
        and heuristic.confidence >= heuristic_threshold
        and heuristic.operation != "unknown"
    ):
        return True, "strong heuristic route skips LLM-first"
    return False, ""


def _accept_llm_intent(llm_intent: UniversalIntent, heuristic: UniversalIntent, *, llm_first: bool) -> bool:
    if llm_first:
        min_confidence = float(os.getenv("PSU_INTENT_LLM_FIRST_MIN_CONFIDENCE", "0.55"))
        if llm_intent.confidence < min_confidence:
            return False
        # Keep deterministic high-confidence routes when the LLM is unsure and disagrees.
        if (
            heuristic.confidence >= 0.92
            and llm_intent.domain != heuristic.domain
            and llm_intent.confidence < float(os.getenv("PSU_INTENT_LLM_FIRST_OVERRIDE_CONFIDENCE", "0.82"))
        ):
            return False
        return True
    return llm_intent.confidence >= max(0.55, heuristic.confidence - 0.05)


def resolve_universal_intent(query: str, route: PipelineRoute, *, allow_llm: bool = False) -> tuple[UniversalIntent, PipelineTrace]:
    heuristic = _heuristic_intent(query, route)
    intent_candidates = _build_intent_candidates(query, route, heuristic)
    intent = heuristic
    llm_attempted = False
    locked_route = route.intent in {"chatbot_identity", "chatbot_greeting"}
    llm_first_skip_reason = ""
    llm_first_review_reason = ""
    llm_call_metadata: dict[str, Any] = {}
    llm_first = _llm_first_enabled(allow_llm) and not locked_route
    if llm_first:
        skip_llm_first, gate_reason = _skip_llm_first_for_strong_route(route, heuristic, query)
        if skip_llm_first:
            llm_first = False
            llm_first_skip_reason = gate_reason
        else:
            llm_first_review_reason = gate_reason
    llm_rejected_reason = ""

    should_call_llm = (
        not locked_route
        and not llm_first_skip_reason
        and (
            llm_first
            or (
                allow_llm
                and _truthy(os.getenv("PSU_UNIVERSAL_INTENT_LLM", "1"))
                and heuristic.confidence < float(os.getenv("PSU_INTENT_HEURISTIC_SKIP_LLM_CONFIDENCE", "0.80"))
            )
        )
    )
    if should_call_llm:
        llm_attempted = True
        llm_result, llm_call_metadata = _llm_intent(query, route, heuristic)
        if llm_result is not None:
            if _accept_llm_intent(llm_result, heuristic, llm_first=llm_first):
                intent = llm_result
            else:
                llm_rejected_reason = (
                    f"llm rejected: confidence={llm_result.confidence}; "
                    f"domain={llm_result.domain}; operation={llm_result.operation}"
                )
        else:
            llm_rejected_reason = "llm unavailable or invalid json"

    trace = PipelineTrace(
        "universal_intent",
        f"{intent.domain}/{intent.operation}",
        intent.confidence,
        intent.reason,
        {
            "method": intent.method,
            "llm_attempted": llm_attempted,
            "llm_first": llm_first,
            "llm_first_skip_reason": llm_first_skip_reason,
            "llm_first_review_reason": llm_first_review_reason,
            "llm_call": llm_call_metadata,
            "intent_risk_flags": list(_intent_review_risk_flags(query, route, heuristic)),
            "llm_rejected_reason": llm_rejected_reason,
            "intent_candidates": [
                {
                    "id": item["id"],
                    "domain": item["domain"],
                    "operation": item["operation"],
                    "confidence": item["confidence"],
                    "reason": item["reason"],
                }
                for item in intent_candidates
            ],
            "target": intent.target,
            "filters": intent.filters,
            "needs": list(intent.needs),
            "answer_style": intent.answer_style,
            "heuristic": {
                "domain": heuristic.domain,
                "operation": heuristic.operation,
                "confidence": heuristic.confidence,
                "reason": heuristic.reason,
            },
        },
    )
    return intent, trace


def refine_route_with_universal_intent(route: PipelineRoute, intent: UniversalIntent) -> tuple[PipelineRoute, PipelineTrace | None]:
    if route.intent in {"chatbot_greeting", "chatbot_identity"}:
        return route, None
    if intent.confidence < 0.78:
        return route, None
    mapped = DOMAIN_ROUTE_MAP.get(intent.domain)
    if not mapped:
        return route, None

    category, default_intent = mapped
    operation_intent = {
        "group_count": "group_count",
        "group_list": "group_list",
        "role_lookup": "members_lookup",
        "count": "count",
        "list": "list",
        "detail": "detail",
        "how_to": "how_to",
        "control": "game_control_lookup",
        "price_calculate": "service_fee_query",
        "schedule_lookup": "schedule_query",
        "rule_lookup": "competition_rules_lookup",
        "availability": "game_availability_lookup" if category == "games" else "availability_lookup",
        "compare": "compare",
        "source_lookup": "source_lookup",
    }.get(intent.operation, default_intent)
    if category == "rules" and intent.operation == "rule_lookup":
        operation_intent = "studio_rules"
    elif category == "penalty" and intent.operation == "rule_lookup":
        operation_intent = "penalty_policy"

    if category == route.category and operation_intent == route.intent:
        return route, None

    # Keep high-confidence high-risk deterministic routes unless universal intent is very clear.
    if route.confidence >= 0.94 and route.risk in {"medium", "high"} and intent.confidence < 0.90:
        return route, PipelineTrace(
            "universal_route_refine",
            "kept_existing_high_risk_route",
            intent.confidence,
            f"existing={route.category}/{route.intent}; universal={intent.domain}/{intent.operation}",
        )

    refined = PipelineRoute(
        category,
        operation_intent,
        max(route.confidence, intent.confidence),
        route.answer_type,
        route.risk,
        f"{route.reason}; universal_intent={intent.domain}/{intent.operation}",
    )
    return refined, PipelineTrace(
        "universal_route_refine",
        f"{route.category}/{route.intent} -> {refined.category}/{refined.intent}",
        intent.confidence,
        "route refined by universal intent",
        {"domain": intent.domain, "operation": intent.operation, "method": intent.method},
    )
