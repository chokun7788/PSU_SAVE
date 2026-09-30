from __future__ import annotations

from app.calculator.service_fee import answer_service_fee
from app.core.normalization import SERVICE_ALIASES, detect_from_aliases, has_price_intent, normalize_text
from app.core.schemas import RouteDecision
from app.rules.matcher import RuleMatcher


DOMAIN_HINTS = [
    "esport", "esports", "psu", "มอ", "จอง", "เช็คอิน", "เชคอิน", "เล่น", "เกม", "กฎ", "ค่าบริการ",
    "ราคา", "vr", "nintendo", "switch", "ps5", "playstation", "cockpit", "ศูนย์",
]


def is_domain_related(query: str) -> bool:
    q = normalize_text(query)
    return any(hint in q for hint in DOMAIN_HINTS)


def route_question(query: str, matcher: RuleMatcher | None = None) -> RouteDecision:
    q = normalize_text(query)
    matcher = matcher or RuleMatcher.default()

    if not is_domain_related(q):
        return RouteDecision(
            route="no_answer",
            confidence=0.40,
            reason="ไม่พบ keyword ที่เกี่ยวกับ PSU Esports หรือบริการของศูนย์",
            answer_type="handoff",
            category="out_of_domain",
        )

    service_match = detect_from_aliases(q, SERVICE_ALIASES)
    if has_price_intent(q) or service_match["key"] in {"ps5", "nintendo_switch", "cockpit", "vr", "pc"}:
        fee_answer = answer_service_fee(query)
        if fee_answer["matched"]:
            return RouteDecision(
                route="deterministic_calculator",
                confidence=fee_answer["confidence"],
                reason=fee_answer["reason"],
                answer_type=fee_answer["answer_type"],
                category="service_fee",
                metadata=fee_answer,
            )

    rule = matcher.match(query)
    if rule is not None:
        return RouteDecision(
            route="rule_fast_path",
            confidence=0.90,
            reason=f"matched rule_id={rule.get('rule_id')} pattern={rule.get('matched_pattern')}",
            answer_type="fact",
            category=rule.get("category", "rule"),
            metadata=rule,
        )

    if any(word in q for word in ["ขั้นตอน", "สรุป", "รายละเอียด", "ทำยังไง", "อย่างไร"]):
        return RouteDecision(
            route="rag_llm",
            confidence=0.70,
            reason="คำถามต้องเรียบเรียงหลายส่วน ควร retrieve ก่อนแล้วให้ LLM สรุป",
            answer_type="explanation",
            category="general",
        )

    return RouteDecision(
        route="rag_direct_curated",
        confidence=0.65,
        reason="เป็นคำถามในโดเมน แต่ไม่เข้า calculator/rule ตรง ควรค้น curated facts ก่อน",
        answer_type="fact",
        category="general",
    )
