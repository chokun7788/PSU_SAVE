from __future__ import annotations

import math
import re

from app.core.normalization import (
    CUSTOMER_GROUP_ALIASES,
    SERVICE_ALIASES,
    TIME_WORD_ALIASES,
    contains_alias,
    detect_from_aliases,
    has_price_intent,
    normalize_text,
)


SOURCE_URL = "https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png"


SERVICE_FEES = {
    "ps5": {
        "label": "PlayStation 5",
        "unit_label": "1 ชั่วโมง",
        "minutes_per_session": 60,
        "capacity": "1-2 คน",
        "prices": {"psu_student_staff": 0, "general_student": 50, "general_adult": 150},
    },
    "nintendo_switch_1_2": {
        "label": "Nintendo Switch",
        "unit_label": "1 ชั่วโมง",
        "minutes_per_session": 60,
        "capacity": "1-2 คน",
        "prices": {"psu_student_staff": 0, "general_student": 50, "general_adult": 140},
    },
    "nintendo_switch_3_4": {
        "label": "Nintendo Switch",
        "unit_label": "1 ชั่วโมง",
        "minutes_per_session": 60,
        "capacity": "3-4 คน",
        "prices": {"psu_student_staff": 0, "general_student": 100, "general_adult": 280},
    },
    "cockpit": {
        "label": "Cockpit",
        "unit_label": "1 ชั่วโมง",
        "minutes_per_session": 60,
        "capacity": "1 คน",
        "prices": {"psu_student_staff": 0, "general_student": 65, "general_adult": 200},
    },
    "vr_30": {
        "label": "VR",
        "unit_label": "30 นาที",
        "minutes_per_session": 30,
        "capacity": "1-5 คน",
        "prices": {"psu_student_staff": 0, "general_student": 190, "general_adult": 525},
    },
    "vr_60": {
        "label": "VR",
        "unit_label": "1 ชั่วโมง",
        "minutes_per_session": 60,
        "capacity": "1-5 คน",
        "prices": {"psu_student_staff": 0, "general_student": 375, "general_adult": 1050},
    },
}


GROUP_LABELS = {
    "psu_student_staff": "นักศึกษา/นักเรียน/บุคลากร PSU",
    "general_student": "ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student)",
    "general_adult": "บุคคลทั่วไป (General Adult)",
}


def _detect_minutes(query: str) -> int | None:
    q = normalize_text(query)
    if contains_alias(q, TIME_WORD_ALIASES["half_hour"], fuzzy=False)[0]:
        return 30
    if contains_alias(q, TIME_WORD_ALIASES["one_hour"], fuzzy=False)[0]:
        return 60

    hour_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:ชั่วโมง|ชม|hour|hr)", q)
    if hour_match:
        return int(float(hour_match.group(1)) * 60)
    minute_match = re.search(r"(\d+)\s*(?:นาที|min|minutes?)", q)
    if minute_match:
        return int(minute_match.group(1))
    return None


def _detect_people(query: str) -> int | None:
    q = normalize_text(query)
    match = re.search(r"(\d+)\s*(?:คน|persons?|people)", q)
    return int(match.group(1)) if match else None


def _select_service_key(query: str) -> tuple[str | None, str]:
    service = detect_from_aliases(query, SERVICE_ALIASES)
    service_key = service["key"]
    if service_key is None:
        return None, "ไม่พบบริการที่ตรงกับคำถาม"
    if service_key == "pc":
        return "pc", "พบคำว่า PC แต่ยังไม่มีราคาที่ตรวจยืนยันได้ใน Service Fee 2026"
    if service_key == "nintendo_switch":
        people = _detect_people(query)
        if people and people >= 3:
            return "nintendo_switch_3_4", "Nintendo Switch ระบุผู้ใช้ 3-4 คน"
        return "nintendo_switch_1_2", "Nintendo Switch ไม่ระบุจำนวนคนหรืออยู่ช่วง 1-2 คน"
    if service_key == "vr":
        minutes = _detect_minutes(query)
        if minutes is not None and minutes <= 30:
            return "vr_30", "VR ระบุระยะเวลาไม่เกิน 30 นาที"
        if minutes is not None and minutes > 30:
            return "vr_60", "VR ระบุระยะเวลาเกิน 30 นาที จึงใช้ราคา 1 ชั่วโมง"
        return "vr_30", "VR ไม่ระบุเวลา จึงเริ่มจากแพ็กเกจ 30 นาทีและควรแสดงตัวเลือก 1 ชั่วโมงประกอบ"
    return service_key, f"พบบริการ {service_key}"


def _detect_group(query: str) -> tuple[str | None, bool, str]:
    q = normalize_text(query)
    for phrase in ("แบบภาษาคนทั่วไป", "ภาษาคนทั่วไป", "พูดแบบคนทั่วไป", "ตอบแบบคนทั่วไป"):
        q = q.replace(phrase, "")
    if any(term in q for term in [
        "นักศึกษา มอ", "นักเรียน มอ", "เด็ก มอ", "นิสิต มอ",
        "นักศึกษา psu", "นักเรียน psu", "เด็ก psu", "psu student", "psu staff",
        "บุคลากร psu", "บุคลากร มอ", "มหาวิทยาลัยสงขลานครินทร์", "สงขลานครินทร์",
    ]):
        return "psu_student_staff", False, "พบกลุ่มผู้ใช้ PSU Student and Staff"
    if any(term in q for term in ["ไม่ใช่มอ", "ไม่ใช่ มอ", "ไม่ได้เรียนมอ", "ไม่ได้เรียน มอ"]):
        return "general_student", False, "พบกลุ่มผู้ใช้ General Student จากคำว่าไม่ใช่/ไม่ได้เรียน มอ"
    group = detect_from_aliases(q, CUSTOMER_GROUP_ALIASES)
    if group["key"] == "psu_student_staff" and not group["ambiguous"]:
        return "psu_student_staff", False, "พบกลุ่มผู้ใช้ PSU Student and Staff"
    if group["key"] == "general_student" and not group["ambiguous"]:
        return "general_student", False, "พบกลุ่มผู้ใช้ General Student / นักศึกษาต่างสถาบัน"
    if group["key"] == "general_adult" and not group["ambiguous"]:
        return "general_adult", False, "พบกลุ่มผู้ใช้ General Adult"
    if group["ambiguous"]:
        return None, True, f"กลุ่มผู้ใช้กำกวม: {group['matches']}"
    # MVP policy: only separate PSU vs non-PSU. Student-like users who are not
    # identified as PSU are treated as General Student / external institution.
    if any(term in q for term in ["นักเรียน", "นักศึกษา", "นิสิต", "เด็ก", "student"]):
        return "general_student", False, "พบคำเรียกนักเรียน/นักศึกษาและไม่พบว่าเป็น PSU จึงจัดเป็น General Student"
    return None, False, "ไม่พบกลุ่มผู้ใช้"


def _group_detail_line(group_key: str | None, ambiguous: bool, query: str) -> str:
    if group_key == "psu_student_staff":
        return "กลุ่มผู้ใช้ที่ตรวจเจอ: นักศึกษา/นักเรียน/บุคลากร PSU"
    if group_key == "general_student":
        return "กลุ่มผู้ใช้ที่ตรวจเจอ: นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น (General Student)"
    if group_key == "general_adult":
        return "กลุ่มผู้ใช้ที่ตรวจเจอ: บุคคลทั่วไป (General Adult)"
    if ambiguous:
        return "กลุ่มผู้ใช้ยังไม่ชัดว่าเป็น PSU หรือต่างสถาบัน"
    return ""


def _sessions_for(service_key: str, requested_minutes: int | None) -> int:
    fee = SERVICE_FEES[service_key]
    if requested_minutes is None:
        return 1
    return max(1, math.ceil(requested_minutes / int(fee["minutes_per_session"])))


def _format_price_line(group_key: str, price: int, sessions: int, service_key: str) -> str:
    total = price * sessions
    fee = SERVICE_FEES[service_key]
    if sessions == 1:
        return f"- {GROUP_LABELS[group_key]}: {price} บาท/{fee['unit_label']}"
    return f"- {GROUP_LABELS[group_key]}: {price} บาท/{fee['unit_label']} x {sessions} = {total} บาท"


def _answer_multi_package_price(
    *,
    package_keys: list[str],
    group_key: str | None,
    ambiguous: bool,
    query: str,
    service_label: str,
    note: str,
) -> dict:
    lines: list[str] = []
    if group_key:
        summary_parts = []
        for key in package_keys:
            fee = SERVICE_FEES[key]
            summary_parts.append(f"{fee['unit_label']} {fee['prices'][group_key]} บาท")
        lines.append(f"ราคา {service_label} สำหรับ {GROUP_LABELS[group_key]}: " + ", ".join(summary_parts))
        for key in package_keys:
            fee = SERVICE_FEES[key]
            lines.append(f"- {fee['label']} {fee['unit_label']} ({fee['capacity']}) ราคา {fee['prices'][group_key]} บาท")
        group_line = _group_detail_line(group_key, ambiguous, query)
        if group_line:
            lines.append(group_line)
    else:
        if ambiguous:
            lines.append("คำถามยังไม่ชัดว่าเป็นนักเรียน/นักศึกษา PSU หรือผู้ใช้ต่างสถาบันครับ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน")
        else:
            lines.append(f"ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคา {service_label} ทุกกลุ่มให้เทียบก่อน")
        for key in package_keys:
            fee = SERVICE_FEES[key]
            lines.append(f"- {fee['label']} {fee['unit_label']} ({fee['capacity']})")
            for current_group in ["psu_student_staff", "general_student", "general_adult"]:
                lines.append(f"  - {GROUP_LABELS[current_group]}: {fee['prices'][current_group]} บาท")
    lines.append(note)
    lines.append(f"แหล่งข้อมูล: {SOURCE_URL}")
    return {
        "matched": True,
        "confidence": 0.94 if group_key else 0.86,
        "answer_type": "fact",
        "reason": "service has multiple packages and question did not specify package detail",
        "service_key": package_keys[0],
        "group_key": group_key,
        "requested_minutes": None,
        "sessions": 1,
        "answer": "\n".join(lines),
        "source_url": SOURCE_URL,
    }


def answer_service_fee(query: str) -> dict:
    q = normalize_text(query)
    if not has_price_intent(q) and not any(contains_alias(q, aliases, fuzzy=False)[0] for aliases in SERVICE_ALIASES.values()):
        return {"matched": False, "confidence": 0.0, "reason": "ไม่พบเจตนาถามราคา/บริการ"}

    service_key, service_reason = _select_service_key(q)
    if service_key is None:
        return {"matched": False, "confidence": 0.0, "reason": service_reason}

    group_key, ambiguous, group_reason = _detect_group(q)

    if service_key == "pc":
        group_line = _group_detail_line(group_key, ambiguous, q)
        group_suffix = f"\n{group_line}" if group_line else ""
        return {
            "matched": True,
            "confidence": 0.88,
            "answer_type": "fact_missing_data",
            "reason": service_reason,
            "answer": (
                "ราคา PC: ยังไม่พบราคาที่ตรวจยืนยันได้ใน Service Fee 2026 ครับ"
                + group_suffix +
                "\n"
                "ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR\n"
                "ดังนั้นยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง ควรถามเจ้าหน้าที่หรืออัปเดตตารางราคา PC เพิ่มก่อน\n"
                f"แหล่งข้อมูล: {SOURCE_URL}"
            ),
            "source_url": SOURCE_URL,
        }

    requested_minutes = _detect_minutes(q)
    if service_key == "vr_30" and requested_minutes is None and contains_alias(q, SERVICE_ALIASES["vr"], fuzzy=False)[0]:
        return _answer_multi_package_price(
            package_keys=["vr_30", "vr_60"],
            group_key=group_key,
            ambiguous=ambiguous,
            query=q,
            service_label="VR",
            note="หมายเหตุ: คำถามยังไม่ระบุระยะเวลา จึงแสดงทั้งราคา 30 นาทีและ 1 ชั่วโมง",
        )
    if service_key == "nintendo_switch_1_2" and _detect_people(q) is None and contains_alias(q, SERVICE_ALIASES["nintendo_switch"], fuzzy=False)[0]:
        return _answer_multi_package_price(
            package_keys=["nintendo_switch_1_2", "nintendo_switch_3_4"],
            group_key=group_key,
            ambiguous=ambiguous,
            query=q,
            service_label="Nintendo Switch",
            note="หมายเหตุ: คำถามยังไม่ระบุจำนวนผู้เล่น จึงแสดงทั้งราคา 1-2 คนและ 3-4 คน",
        )
    sessions = _sessions_for(service_key, requested_minutes)
    fee = SERVICE_FEES[service_key]

    header = f"{fee['label']} ({fee['capacity']}) ราคาอ้างอิงตามแพ็กเกจ {fee['unit_label']}"
    lines = []

    if ambiguous:
        lines.append("คำถามยังไม่ชัดว่าเป็นนักเรียน/นักศึกษา PSU หรือผู้ใช้ต่างสถาบันครับ")
        lines.append(header)
        for key in ["psu_student_staff", "general_student", "general_adult"]:
            lines.append(_format_price_line(key, fee["prices"][key], sessions, service_key))
        lines.append("ถ้าหมายถึงนักเรียน/นักศึกษา PSU ให้ดูแถว PSU Student and Staff แต่ถ้าเป็นต่างสถาบันให้ดูแถว General Student")
    elif group_key:
        price = fee["prices"][group_key]
        total = price * sessions
        lines.append(f"{header} สำหรับ {GROUP_LABELS[group_key]} ราคา {total} บาท")
        if sessions > 1:
            lines.append(f"คำนวณจาก {price} บาท/{fee['unit_label']} x {sessions} session")
    else:
        lines.append("ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน")
        lines.append(header)
        for key in ["psu_student_staff", "general_student", "general_adult"]:
            lines.append(_format_price_line(key, fee["prices"][key], sessions, service_key))

    if requested_minutes is not None:
        lines.append(f"ระยะเวลาที่ถามประมาณ {requested_minutes} นาที ใช้ {sessions} session ตามแพ็กเกจนี้")
    lines.append(f"แหล่งข้อมูล: {SOURCE_URL}")

    return {
        "matched": True,
        "confidence": 0.95 if group_key else 0.86,
        "answer_type": "calculation" if requested_minutes else "fact",
        "reason": f"{service_reason}; {group_reason}",
        "service_key": service_key,
        "group_key": group_key,
        "requested_minutes": requested_minutes,
        "sessions": sessions,
        "answer": "\n".join(lines),
        "source_url": SOURCE_URL,
    }
