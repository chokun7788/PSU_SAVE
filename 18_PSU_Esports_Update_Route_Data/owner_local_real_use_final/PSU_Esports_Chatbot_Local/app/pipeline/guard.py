from __future__ import annotations

from app.pipeline.schemas import EntityBundle, PipelineTrace, PreprocessedInput


NO_ANSWER_TERMS = (
    "ซ่อมคอมส่วนตัว", "ส่งอาหาร", "เช่าโน้ตบุ๊ก", "ห้องนอน", "พักค้างคืน",
    "ขายคีย์บอร์ด", "รับซ่อมจอย", "ส่งเครื่องเกมไปบ้าน", "ซื้อเกม steam", "คอร์สสอนเล่น",
    "จ่ายด้วยคริปโต", "ผ่อนชำระ", "ส่วนลดวันเกิด", "เหมาทั้งวัน",
    "pc ตัวเอง", "อาหารบุฟเฟต์", "งานแต่ง", "เช่าจอไปบ้าน", "แมว", "ถ่ายรูปโปรไฟล์", "สมาชิก รายปี", "สมาชิกรายปี",
    "เครื่องไหนดีที่สุด", "มีอะไรแนะนำไหม", "สรุปคือทำยังไง",
    "valorant mobile", "วาโลแรนท์ mobile", "วาโล mobile",
    "เบอร์โทรส่วนตัว", "ขอเบอร์โทรส่วนตัว", "ข้อมูลส่วนตัวเจ้าหน้าที่",
    "ข้อมูลที่ไม่ได้อยู่ในเว็บ", "ไม่ได้อยู่ในเว็บ psu esports",
    "ข่าวล่าสุด", "วันนี้มีข่าว", "อะไรล่าสุด",
)

DOMAIN_HINTS = (
    "esport", "esports", "psu", "มอ", "จอง", "เช็คอิน", "เชคอิน", "เล่น",
    "เกม", "กฎ", "ค่าบริการ", "ราคา", "vr", "nintendo", "switch", "ps5",
    "playstation", "cockpit", "ศูนย์", "อุปกรณ์", "คอม", "เปิด", "ปิด",
)


def guard_scope(pre: PreprocessedInput, entities: EntityBundle) -> tuple[str | None, float, PipelineTrace]:
    q = pre.normalized_query
    if any(term in q for term in NO_ANSWER_TERMS):
        return (
            "ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ",
            0.96,
            PipelineTrace("guard", "no_answer_known_out_of_scope", 0.96, "matched no-answer term"),
        )

    if not any(hint in q for hint in DOMAIN_HINTS):
        return (
            None,
            0.35,
            PipelineTrace("guard", "weak_domain_signal", 0.35, "no clear PSU Esports domain hint"),
        )

    return (
        None,
        0.90,
        PipelineTrace("guard", "domain_ok", 0.90, "domain hints found"),
    )
