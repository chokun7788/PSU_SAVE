from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from app.core.normalization import normalize_text


BANGKOK_TZ = ZoneInfo("Asia/Bangkok")
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CLOSURES_PATH = PROJECT_ROOT / "data" / "calendar" / "service_closures.jsonl"
THAI_HOLIDAYS_PATH = PROJECT_ROOT / "data" / "calendar" / "thai_holidays_2026.jsonl"
THAI_HOLIDAY_SOURCE_URL = "https://www.timeanddate.com/holidays/thailand"

THAI_WEEKDAYS = {
    0: "วันจันทร์",
    1: "วันอังคาร",
    2: "วันพุธ",
    3: "วันพฤหัสบดี",
    4: "วันศุกร์",
    5: "วันเสาร์",
    6: "วันอาทิตย์",
}

THAI_MONTHS = {
    "มกราคม": 1,
    "มกรา": 1,
    "ม.ค.": 1,
    "มค": 1,
    "กุมภาพันธ์": 2,
    "กุมภา": 2,
    "ก.พ.": 2,
    "กพ": 2,
    "มีนาคม": 3,
    "มีนา": 3,
    "มี.ค.": 3,
    "มีค": 3,
    "เมษายน": 4,
    "เมษา": 4,
    "เม.ย.": 4,
    "เมย": 4,
    "พฤษภาคม": 5,
    "พฤษภา": 5,
    "พ.ค.": 5,
    "พค": 5,
    "มิถุนายน": 6,
    "มิถุนา": 6,
    "มิ.ย.": 6,
    "มิย": 6,
    "กรกฎาคม": 7,
    "ก.ค.": 7,
    "กค": 7,
    "กรกฎา": 7,
    "สิงหาคม": 8,
    "สิงหา": 8,
    "ส.ค.": 8,
    "สค": 8,
    "กันยายน": 9,
    "กันยา": 9,
    "ก.ย.": 9,
    "กย": 9,
    "ตุลาคม": 10,
    "ตุลา": 10,
    "ต.ค.": 10,
    "ตค": 10,
    "พฤศจิกายน": 11,
    "พฤศจิกา": 11,
    "พ.ย.": 11,
    "พย": 11,
    "ธันวาคม": 12,
    "ธันวา": 12,
    "ธ.ค.": 12,
    "ธค": 12,
}


@dataclass(frozen=True)
class DateResolution:
    target_date: date
    label: str
    reason: str


@dataclass(frozen=True)
class MonthResolution:
    year: int
    month: int
    label: str
    reason: str


@dataclass(frozen=True)
class YearResolution:
    year: int
    label: str
    reason: str


@dataclass(frozen=True)
class ClosureInfo:
    date: str
    title: str
    status: str
    note: str = ""
    source: str = "manual_admin_config"


@dataclass(frozen=True)
class HolidayInfo:
    date: str
    title: str
    type: str
    note: str = ""
    source: str = "thai_holiday_calendar"
    source_url: str = THAI_HOLIDAY_SOURCE_URL


def now_bangkok() -> datetime:
    override = os.environ.get("PSU_ESPORTS_NOW", "").strip()
    if override:
        clean = override.replace("Z", "+00:00")
        parsed = datetime.fromisoformat(clean)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=BANGKOK_TZ)
        return parsed.astimezone(BANGKOK_TZ)

    today_override = os.environ.get("PSU_ESPORTS_TODAY", "").strip()
    current = datetime.now(BANGKOK_TZ)
    if today_override:
        target = date.fromisoformat(today_override)
        return current.replace(year=target.year, month=target.month, day=target.day)
    return current


def today_bangkok() -> date:
    override = os.environ.get("PSU_ESPORTS_TODAY", "").strip()
    if override:
        return date.fromisoformat(override)
    return now_bangkok().date()


def thai_weekday_name(value: date) -> str:
    return THAI_WEEKDAYS[value.weekday()]


def format_thai_date(value: date) -> str:
    return f"{value.day:02d}/{value.month:02d}/{value.year} ({thai_weekday_name(value)})"


def thai_month_name(month: int) -> str:
    names = {
        1: "มกราคม",
        2: "กุมภาพันธ์",
        3: "มีนาคม",
        4: "เมษายน",
        5: "พฤษภาคม",
        6: "มิถุนายน",
        7: "กรกฎาคม",
        8: "สิงหาคม",
        9: "กันยายน",
        10: "ตุลาคม",
        11: "พฤศจิกายน",
        12: "ธันวาคม",
    }
    return names[month]


def format_thai_month(year: int, month: int) -> str:
    return f"เดือน{thai_month_name(month)} {year} (พ.ศ. {year + 543})"


def format_thai_year(year: int) -> str:
    return f"ปี {year} (พ.ศ. {year + 543})"


def _parse_year(value: str | None, current_year: int) -> int:
    if not value:
        return current_year
    year = int(value)
    if year >= 2400:
        return year - 543
    if year < 100:
        return 2000 + year
    return year


def resolve_date_from_text(query: str, *, today: date | None = None) -> DateResolution | None:
    base = today or today_bangkok()
    q = normalize_text(query)

    relative_day_match = re.search(r"(?:อีก|หลังจากนี้)\s*(\d{1,4})\s*วัน", q)
    if relative_day_match:
        amount = int(relative_day_match.group(1))
        target = base + timedelta(days=amount)
        return DateResolution(target, f"อีก {amount} วันคือ {format_thai_date(target)}", "relative_day_offset")

    forward_day_match = re.search(r"(\d{1,4})\s*วัน(?:ข้างหน้า|ถัดไป)", q)
    if forward_day_match:
        amount = int(forward_day_match.group(1))
        target = base + timedelta(days=amount)
        return DateResolution(target, f"อีก {amount} วันคือ {format_thai_date(target)}", "relative_day_offset")

    backward_day_match = re.search(r"(?:ย้อนหลัง|ก่อนหน้า|เมื่อ)\s*(\d{1,4})\s*วัน|(\d{1,4})\s*วันก่อน", q)
    if backward_day_match:
        amount = int(backward_day_match.group(1) or backward_day_match.group(2))
        target = base - timedelta(days=amount)
        return DateResolution(target, f"{amount} วันก่อนคือ {format_thai_date(target)}", "relative_day_offset")

    relative_week_match = re.search(r"(?:อีก|หลังจากนี้)\s*(\d{1,3})\s*(?:สัปดาห์|อาทิตย์)", q)
    if relative_week_match:
        amount = int(relative_week_match.group(1))
        target = base + timedelta(days=amount * 7)
        return DateResolution(target, f"อีก {amount} สัปดาห์คือ {format_thai_date(target)}", "relative_week_offset")

    if "มะรืน" in q:
        target = base + timedelta(days=2)
        return DateResolution(target, f"มะรืนนี้ {format_thai_date(target)}", "relative_day")
    if "พรุ่งนี้" in q:
        target = base + timedelta(days=1)
        return DateResolution(target, f"พรุ่งนี้ {format_thai_date(target)}", "relative_day")
    if "วันนี้" in q or "today" in q:
        return DateResolution(base, f"วันนี้ {format_thai_date(base)}", "relative_day")

    numeric_match = re.search(r"\b(\d{1,2})[/-](\d{1,2})(?:[/-](\d{2,4}))?\b", q)
    if numeric_match:
        day = int(numeric_match.group(1))
        month = int(numeric_match.group(2))
        year = _parse_year(numeric_match.group(3), base.year)
        try:
            target = date(year, month, day)
        except ValueError:
            return None
        return DateResolution(target, f"วันที่ {format_thai_date(target)}", "explicit_date")

    month_pattern = "|".join(re.escape(name) for name in sorted(THAI_MONTHS, key=len, reverse=True))
    thai_match = re.search(rf"(?:วันที่\s*)?(\d{{1,2}})\s*({month_pattern})(?:\s*(\d{{2,4}}))?", q)
    if thai_match:
        day = int(thai_match.group(1))
        month = THAI_MONTHS[thai_match.group(2)]
        year = _parse_year(thai_match.group(3), base.year)
        try:
            target = date(year, month, day)
        except ValueError:
            return None
        return DateResolution(target, f"วันที่ {format_thai_date(target)}", "explicit_date")

    return None


def _add_month(year: int, month: int, amount: int) -> tuple[int, int]:
    index = (year * 12 + (month - 1)) + amount
    return index // 12, index % 12 + 1


def resolve_month_from_text(query: str, *, today: date | None = None) -> MonthResolution | None:
    base = today or today_bangkok()
    q = normalize_text(query)

    if "เดือนที่แล้ว" in q or "เดือนก่อน" in q:
        year, month = _add_month(base.year, base.month, -1)
        return MonthResolution(year, month, format_thai_month(year, month), "relative_month")
    if "เดือนหน้า" in q:
        year, month = _add_month(base.year, base.month, 1)
        return MonthResolution(year, month, format_thai_month(year, month), "relative_month")
    if "เดือนนี้" in q:
        return MonthResolution(base.year, base.month, format_thai_month(base.year, base.month), "relative_month")

    numeric_match = re.search(r"เดือน\s*(\d{1,2})(?:\s*[/-]\s*(\d{2,4}))?", q)
    if numeric_match:
        month = int(numeric_match.group(1))
        if not 1 <= month <= 12:
            return None
        year = _parse_year(numeric_match.group(2), base.year)
        return MonthResolution(year, month, format_thai_month(year, month), "explicit_month")

    month_pattern = "|".join(re.escape(name) for name in sorted(THAI_MONTHS, key=len, reverse=True))
    thai_match = re.search(rf"({month_pattern})(?:\s*(\d{{2,4}}))?", q)
    if thai_match:
        month = THAI_MONTHS[thai_match.group(1)]
        year = _parse_year(thai_match.group(2), base.year)
        return MonthResolution(year, month, format_thai_month(year, month), "explicit_month")

    return None


def resolve_year_from_text(query: str, *, today: date | None = None) -> YearResolution | None:
    base = today or today_bangkok()
    q = normalize_text(query)

    if "ปีที่แล้ว" in q or "ปีก่อน" in q:
        year = base.year - 1
        return YearResolution(year, format_thai_year(year), "relative_year")
    if "ปีหน้า" in q:
        year = base.year + 1
        return YearResolution(year, format_thai_year(year), "relative_year")
    if "ปีนี้" in q:
        return YearResolution(base.year, format_thai_year(base.year), "relative_year")

    year_match = re.search(r"(?:ปี|พ\.ศ\.|พศ|ค\.ศ\.|คศ)?\s*(\d{4})", q)
    if year_match and _has_year_context(q):
        year = _parse_year(year_match.group(1), base.year)
        return YearResolution(year, format_thai_year(year), "explicit_year")

    return None


def _has_year_context(q: str) -> bool:
    return any(term in q for term in ("ปี", "พ.ศ.", "พศ", "ค.ศ.", "คศ", "วันหยุด", "เทศกาล", "ปฏิทิน", "ราชการ"))


def load_closures(path: Path = CLOSURES_PATH) -> dict[str, ClosureInfo]:
    closures: dict[str, ClosureInfo] = {}
    if not path.exists():
        return closures
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        info = ClosureInfo(
            date=str(item["date"]),
            title=str(item.get("title", "วันปิดให้บริการ")),
            status=str(item.get("status", "closed")),
            note=str(item.get("note", "")),
            source=str(item.get("source", "manual_admin_config")),
        )
        closures[info.date] = info
    return closures


def closure_for(value: date) -> ClosureInfo | None:
    return load_closures().get(value.isoformat())


def closures_for_month(year: int, month: int) -> list[ClosureInfo]:
    items: list[ClosureInfo] = []
    for info in load_closures().values():
        try:
            value = date.fromisoformat(info.date)
        except ValueError:
            continue
        if value.year == year and value.month == month and info.status == "closed":
            items.append(info)
    return sorted(items, key=lambda item: item.date)


def closures_for_year(year: int) -> list[ClosureInfo]:
    items: list[ClosureInfo] = []
    for info in load_closures().values():
        try:
            value = date.fromisoformat(info.date)
        except ValueError:
            continue
        if value.year == year and info.status == "closed":
            items.append(info)
    return sorted(items, key=lambda item: item.date)


def load_thai_holidays(path: Path = THAI_HOLIDAYS_PATH) -> dict[str, list[HolidayInfo]]:
    holidays: dict[str, list[HolidayInfo]] = {}
    paths = sorted(path.parent.glob("thai_holidays_*.jsonl")) if path.parent.exists() else []
    if path.exists() and path not in paths:
        paths.append(path)
    if not paths:
        return holidays
    seen: set[tuple[str, str, str]] = set()
    for source_path in paths:
        for line in source_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            info = HolidayInfo(
                date=str(item["date"]),
                title=str(item.get("title", "วันหยุด/เทศกาลไทย")),
                type=str(item.get("type", "observance")),
                note=str(item.get("note", "")),
                source=str(item.get("source", "thai_holiday_calendar")),
                source_url=str(item.get("source_url", THAI_HOLIDAY_SOURCE_URL)),
            )
            key = (info.date, info.title, info.type)
            if key in seen:
                continue
            seen.add(key)
            holidays.setdefault(info.date, []).append(info)
    return holidays


def holidays_for_date(value: date) -> list[HolidayInfo]:
    return load_thai_holidays().get(value.isoformat(), [])


def holidays_for_month(year: int, month: int) -> list[HolidayInfo]:
    items: list[HolidayInfo] = []
    for values in load_thai_holidays().values():
        for info in values:
            try:
                value = date.fromisoformat(info.date)
            except ValueError:
                continue
            if value.year == year and value.month == month:
                items.append(info)
    return sorted(items, key=lambda item: item.date)


def holidays_for_year(year: int) -> list[HolidayInfo]:
    items: list[HolidayInfo] = []
    for values in load_thai_holidays().values():
        for info in values:
            try:
                value = date.fromisoformat(info.date)
            except ValueError:
                continue
            if value.year == year:
                items.append(info)
    return sorted(items, key=lambda item: item.date)


def next_holidays(start: date | None = None, limit: int = 5) -> list[HolidayInfo]:
    base = start or today_bangkok()
    items: list[HolidayInfo] = []
    for values in load_thai_holidays().values():
        for info in values:
            try:
                value = date.fromisoformat(info.date)
            except ValueError:
                continue
            if value >= base:
                items.append(info)
    return sorted(items, key=lambda item: item.date)[:limit]


def _minutes(value: datetime) -> int:
    return value.hour * 60 + value.minute


def _slot(code: str, label: str, start: str, end: str, state: str, note: str = "") -> dict[str, str]:
    return {
        "code": code,
        "label": label,
        "start": start,
        "end": end,
        "time_range": f"{start}-{end}",
        "state": state,
        "note": note,
    }


def regular_service_slots(value: date) -> list[dict[str, str]]:
    weekday = value.weekday()
    if weekday == 0:
        return [
            _slot("morning", "Morning", "09:00", "12:00", "maintenance", "วันจันทร์ช่วงเช้าเป็น Maintenance*"),
            _slot("afternoon", "Afternoon", "13:00", "16:00", "open", "เปิดให้บริการ"),
        ]
    if weekday in {1, 2, 3}:
        return [
            _slot("morning", "Morning", "09:00", "12:00", "open", "เปิดให้บริการ"),
            _slot("afternoon", "Afternoon", "13:00", "16:00", "open", "เปิดให้บริการ"),
        ]
    if weekday == 4:
        return [
            _slot("morning", "Morning", "09:00", "12:00", "open", "เปิดให้บริการ"),
            _slot("afternoon", "Afternoon", "13:00", "16:00", "maintenance", "วันศุกร์ช่วงบ่ายเป็น Maintenance"),
        ]
    return []


def current_service_slot(now: datetime | None = None) -> dict[str, object]:
    current = now.astimezone(BANGKOK_TZ) if now else now_bangkok()
    target = current.date()
    closure = closure_for(target)
    base = {
        "date": target.isoformat(),
        "time": current.strftime("%H:%M"),
        "weekday": thai_weekday_name(target),
        "timezone": "Asia/Bangkok",
    }

    if closure and closure.status == "closed":
        return {
            **base,
            "status": "closed",
            "playable": False,
            "slot": None,
            "next_open_slot": None,
            "reason": closure.title,
            "note": closure.note,
            "source": closure.source,
        }

    slots = regular_service_slots(target)
    if not slots:
        return {
            **base,
            "status": "closed",
            "playable": False,
            "slot": None,
            "next_open_slot": None,
            "reason": "no_regular_service",
            "note": "ยังไม่พบช่วงให้บริการในตารางประจำของวันนี้",
            "source": "reservation_schedule",
        }

    minute_now = _minutes(current)
    for slot in slots:
        start_hour, start_minute = [int(part) for part in slot["start"].split(":")]
        end_hour, end_minute = [int(part) for part in slot["end"].split(":")]
        start_minutes = start_hour * 60 + start_minute
        end_minutes = end_hour * 60 + end_minute
        if start_minutes <= minute_now < end_minutes:
            state = slot["state"]
            return {
                **base,
                "status": "open" if state == "open" else "maintenance",
                "playable": state == "open",
                "slot": slot,
                "next_open_slot": None,
                "reason": state,
                "note": slot.get("note", ""),
                "source": "reservation_schedule",
            }

    next_open = None
    for slot in slots:
        start_hour, start_minute = [int(part) for part in slot["start"].split(":")]
        if minute_now < start_hour * 60 + start_minute and slot["state"] == "open":
            next_open = slot
            break

    return {
        **base,
        "status": "outside_hours",
        "playable": False,
        "slot": None,
        "next_open_slot": next_open,
        "reason": "outside_regular_service_hours",
        "note": "อยู่นอกช่วงเวลาให้บริการตามตารางประจำ",
        "source": "reservation_schedule",
    }


def _holiday_dict(info: HolidayInfo) -> dict[str, str]:
    return {
        "date": info.date,
        "title": info.title,
        "type": info.type,
        "note": info.note,
        "source": info.source,
        "source_url": info.source_url,
    }


def _closure_dict(info: ClosureInfo | None) -> dict[str, str] | None:
    if info is None:
        return None
    return {
        "date": info.date,
        "title": info.title,
        "status": info.status,
        "note": info.note,
        "source": info.source,
    }


def calendar_context(now: datetime | None = None) -> dict[str, object]:
    current = now.astimezone(BANGKOK_TZ) if now else now_bangkok()
    target = current.date()
    return {
        "date": target.isoformat(),
        "label": format_thai_date(target),
        "weekday": thai_weekday_name(target),
        "time": current.strftime("%H:%M"),
        "datetime_iso": current.isoformat(),
        "timezone": "Asia/Bangkok",
        "service_slot": current_service_slot(current),
        "service_closure": _closure_dict(closure_for(target)),
        "thai_holidays": [_holiday_dict(info) for info in holidays_for_date(target)],
        "upcoming_thai_holidays": [_holiday_dict(info) for info in next_holidays(target, limit=5)],
    }


def has_date_or_holiday_intent(query: str) -> bool:
    q = normalize_text(query)
    if any(term in q for term in ("วันนี้", "พรุ่งนี้", "มะรืน", "today", "วันหยุด", "เทศกาล", "ราชการ", "หยุด", "หยุดไหม", "ปฏิทิน", "เดือนนี้", "เดือนหน้า", "เดือนที่แล้ว", "เดือนก่อน", "ปีนี้", "ปีหน้า", "ปีที่แล้ว", "ปีก่อน", "สัปดาห์หน้า", "อาทิตย์หน้า", "อาทิตย์นี้", "ตอนนี้", "ขณะนี้", "เวลานี้", "กี่โมง")):
        return True
    if re.search(r"(?:อีก|หลังจากนี้)\s*\d{1,4}\s*(?:วัน|สัปดาห์|อาทิตย์)|\d{1,4}\s*วัน(?:ข้างหน้า|ถัดไป|ก่อน)", q):
        return True
    if re.search(r"\b\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?\b", q):
        return True
    if re.search(r"(?:ปี|พ\.ศ\.|พศ|ค\.ศ\.|คศ)?\s*\d{4}", q) and _has_year_context(q):
        return True
    return any(month in q for month in THAI_MONTHS)


def regular_service_summary(value: date) -> str:
    weekday = value.weekday()
    if weekday == 0:
        return "วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*"
    if weekday in {1, 2, 3}:
        return f"{thai_weekday_name(value)}เปิดให้เล่น 09:00-12:00 และ 13:00-16:00"
    if weekday == 4:
        return "วันศุกร์เปิดช่วงเช้า 09:00-12:00 แต่ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์"
    return f"{thai_weekday_name(value)}ยังไม่พบช่วงให้บริการในตารางประจำที่มีอยู่ จึงควรตรวจสอบกับศูนย์ก่อนเดินทาง"
