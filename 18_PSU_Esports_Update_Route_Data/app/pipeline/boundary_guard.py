from __future__ import annotations

from dataclasses import dataclass

from app.core.normalization import normalize_text


@dataclass(frozen=True)
class BoundaryDecision:
    action: str
    confidence: float
    flags: tuple[str, ...] = ()
    answer: str = ""
    reason: str = ""


_SENSITIVE_TERMS = (
    "รหัสผ่าน", "password", "wifi password", "พาสเวิร์ด",
    "พิกัดบ้าน", "พิกัดผม", "ตำแหน่งบ้าน", "ส่งพิกัด", "location บ้าน",
    "เบอร์โทรส่วนตัว", "ข้อมูลส่วนตัวเจ้าหน้าที่", "ข้อมูลส่วนตัว",
)

_UNSUPPORTED_FACILITY_TERMS = (
    "มีกลิ่น", "กลิ่นไหม", "ปวดหลัง", "ร้องไห้", "ปลอบ", "เก้าอี้เด้ง",
    "เก้าอี้ที่เด้ง", "ที่ซ่อนตัว", "ซ่อนตัวจากเพื่อน", "ห้องลับ", "เกมเถื่อน",
    "โสดตลอดไป", "ชนะตลอดวัน", "ส่วนลดถ้าชนะ", "คุณชอบ", "ชอบสี",
    "กล้องวงจรปิดกี่ตัว",
    "เจ้าหน้าที่นอน", "เกม gta 6", "gta 6",
)

_UNSAFE_OR_ABUSIVE_TERMS = (
    "วิธีโกงเกม", "โกงเกม", "แฮกเกม", "ใช้โปรโกง", "โกงเกมส์",
)

_CLEAR_OUT_OF_SCOPE_TERMS = (
    "อากาศวันนี้", "พยากรณ์อากาศ", "เมนูอาหาร", "อาหารเย็น",
    "ใครเป็นนายก", "นายกรัฐมนตรี", "ข่าวการเมือง", "การเมือง",
    "ทำนายดวง", "ดูดวง", "สอนเขียน python", "python programming",
)

_EMERGENCY_TERMS = (
    "ไฟไหม้", "ไฟไหม", "เกิดเพลิงไหม้", "เหตุฉุกเฉิน",
)


def _has(query: str, terms: tuple[str, ...]) -> bool:
    return any(term in query for term in terms)


def evaluate_boundary(query: str) -> BoundaryDecision:
    """Classify requests that must not reach a broad catalog/general answer.

    This guard only handles high-confidence boundaries. It deliberately does not
    classify every unusual sentence, so normal PSU facts can still reach the
    existing router and source validation layers.
    """
    clean = normalize_text(query)
    if not clean:
        return BoundaryDecision("allow", 0.0, reason="empty query handled by existing pipeline")

    if _has(clean, _SENSITIVE_TERMS):
        return BoundaryDecision(
            "no_answer_sensitive",
            0.99,
            ("sensitive_private_or_credential_request",),
            "ขออภัยครับ ผมไม่มีช่องทางให้เบอร์โทรส่วนตัวหรือข้อมูลส่วนตัวเจ้าหน้าที่ และไม่สามารถเปิดเผยรหัสผ่านหรือพิกัดส่วนตัวได้ครับ",
            "sensitive/private data request must be blocked before retrieval",
        )

    if _has(clean, _UNSAFE_OR_ABUSIVE_TERMS):
        return BoundaryDecision(
            "no_answer_unsafe",
            0.99,
            ("cheating_or_abuse_request",),
            "ผมช่วยเรื่องการโกงเกม การแฮก หรือการใช้โปรโกงไม่ได้ครับ แต่ช่วยแนะนำข้อมูลเกม ปุ่ม และการใช้งานที่ถูกต้องได้",
            "unsafe gaming request must not reach general LLM",
        )

    if _has(clean, _CLEAR_OUT_OF_SCOPE_TERMS):
        return BoundaryDecision(
            "no_answer_out_of_scope",
            0.98,
            ("clear_out_of_scope_request",),
            "ตอนนี้ผมตอบได้เฉพาะข้อมูลของ PSU Esports Studio - Phuket เช่น เกม ปุ่ม อุปกรณ์ ราคา การจอง ตารางเวลา กฎ และสมาชิกครับ",
            "clear non-PSU request must stay inside the chatbot scope",
        )

    if _has(clean, _EMERGENCY_TERMS):
        return BoundaryDecision(
            "safety_redirect",
            0.96,
            ("emergency_safety_query",),
            "ถ้าเป็นเหตุฉุกเฉิน ให้หยุดใช้งาน แจ้งเจ้าหน้าที่ทันที และปฏิบัติตามทางหนีไฟหรือคำแนะนำของหน่วยฉุกเฉินครับ ระบบยังไม่มีขั้นตอนฉุกเฉินเฉพาะของสาขาที่ยืนยันได้",
            "emergency query needs staff/emergency escalation without inventing PSU procedure",
        )

    if _has(clean, _UNSUPPORTED_FACILITY_TERMS):
        return BoundaryDecision(
            "no_answer_unsupported",
            0.96,
            ("unsupported_facility_detail",),
            "ตอนนี้ยังไม่มีข้อมูลที่ยืนยันได้เกี่ยวกับรายละเอียดนี้ของ PSU Esports Studio - Phuket ครับ แนะนำสอบถามเจ้าหน้าที่หน้างานโดยตรง",
            "unusual facility detail has no verified source and must not borrow a catalog answer",
        )

    return BoundaryDecision("allow", 0.90, reason="no high-confidence boundary matched")
