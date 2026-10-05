from __future__ import annotations

"""Narrow routing gate for booking-policy evidence retrieval.

This is deliberately not an answer alias table.  It only identifies questions
whose intent is a policy exception rather than the broad "how do I book?"
flow.  The answer still has to come from approved Knowledge evidence and pass
the normal answer contract.
"""

from app.core.normalization import normalize_text
from app.pipeline.schemas import PipelineRoute, UniversalIntent


def is_specific_booking_policy_question(question: str, route: PipelineRoute) -> bool:
    """Return whether a reservation question needs policy evidence before Struct.

    A broad booking request remains on the fast structured path.  A question
    about an exception (transfer, post-booking change, late check-in, refund,
    or payment expiry) is allowed to ask RAG for a grounded policy record first.
    """
    if route.category != "reservation":
        return False

    q = normalize_text(question)
    if not q:
        return False

    transfer = (
        ("โอนสิทธิ์" in q or "transfer" in q)
        or ("จอง" in q and "แทน" in q and any(term in q for term in ("เพื่อน", "คนอื่น", "ผู้อื่น")))
    )
    post_booking_change = any(term in q for term in (
        "แก้ไขข้อมูล", "แก้ข้อมูล", "เปลี่ยนข้อมูล", "แก้ไขหลังจอง",
        "ยกเลิกหลังจอง", "cancel booking", "change booking",
    ))
    late_checkin = any(term in q for term in (
        "เช็คอินไม่ทัน", "เชคอินไม่ทัน", "ไม่เช็คอิน", "มาสาย",
        "ไปช้า", "ไปถึงช้า", "late checkin", "miss checkin",
    ))
    refund = any(term in q for term in ("คืนเงิน", "ขอเงินคืน", "refund"))
    payment_expiry = any(term in q for term in (
        "ไม่จ่าย", "ลืมจ่าย", "จ่ายไม่ทัน", "ชำระไม่ทัน", "payment expired",
    ))
    return transfer or post_booking_change or late_checkin or refund or payment_expiry


def booking_policy_semantic_route(route: PipelineRoute) -> PipelineRoute:
    """Create the internal evidence route without adding a public route per policy."""
    return PipelineRoute(
        "knowledge",
        "booking_policy_detail",
        max(0.91, route.confidence),
        "fact",
        "medium",
        f"{route.reason}; specific booking policy requires grounded knowledge evidence",
    )


def booking_policy_semantic_intent(intent: UniversalIntent) -> UniversalIntent:
    """Give the Question Frame the semantic evidence contract for this lookup."""
    return UniversalIntent(
        domain="knowledge",
        operation="semantic_evidence_lookup",
        target=intent.target,
        filters={
            **intent.filters,
            "semantic_route_category": "knowledge",
            "policy_scope": "booking",
        },
        needs=intent.needs,
        answer_style="direct",
        confidence=max(0.91, intent.confidence),
        method="semantic_evidence",
        reason="specific booking policy is answered from approved knowledge evidence",
    )
