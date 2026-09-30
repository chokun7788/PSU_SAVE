from __future__ import annotations

import json
import os
import re
import threading
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Any
from urllib.error import URLError
from urllib.parse import urlencode, urlparse, urlunparse
from urllib.request import Request, urlopen

from app.calendar.service_calendar import closure_for, regular_service_slots, resolve_date_from_text, today_bangkok
from app.core.normalization import normalize_text
from app.pipeline.protected_intents import is_weekly_booking_window_query


DEFAULT_STATUS_URL = "http://127.0.0.1:8091/api/chatbot-status"
BOOKING_SOURCE_URL = "https://esports.computing.psu.ac.th/reservation"
_CACHE_LOCK = threading.Lock()
_CACHE: dict[str, tuple[float, "LiveBookingSnapshot"]] = {}
_FETCH_LOCK = threading.Lock()


def _truthy(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def live_booking_enabled() -> bool:
    return _truthy(os.getenv("PSU_LIVE_BOOKING_ENABLED"), True)


def _timeout_sec() -> float:
    try:
        return max(0.2, min(8.0, float(os.getenv("PSU_LIVE_BOOKING_TIMEOUT_SEC", "5.0"))))
    except ValueError:
        return 5.0


def _cache_sec() -> float:
    try:
        return max(0.0, min(30.0, float(os.getenv("PSU_LIVE_BOOKING_CACHE_SEC", "10"))))
    except ValueError:
        return 10.0


def _status_url() -> str:
    return os.getenv("PSU_LIVE_BOOKING_STATUS_URL", DEFAULT_STATUS_URL).strip() or DEFAULT_STATUS_URL


@dataclass(frozen=True)
class LiveSlot:
    start: str
    end: str
    status: str
    booked_count: int
    no_show_count: int
    available_count: int

    def as_dict(self) -> dict[str, Any]:
        return {
            "start": self.start,
            "end": self.end,
            "status": self.status,
            "booked_count": self.booked_count,
            "no_show_count": self.no_show_count,
            "available_count": self.available_count,
        }


@dataclass(frozen=True)
class LiveResource:
    resource_id: str
    resource_name: str
    capacity: int
    status: str
    available_now: int
    slots: tuple[LiveSlot, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "resource_id": self.resource_id,
            "resource_name": self.resource_name,
            "capacity": self.capacity,
            "status": self.status,
            "available_now": self.available_now,
            "slots": [slot.as_dict() for slot in self.slots],
        }


@dataclass(frozen=True)
class LiveBookingSnapshot:
    ok: bool
    date: str
    now: str
    generated_at: str
    source: str
    center_open: bool
    center_reason: str
    open_periods: tuple[tuple[str, str], ...]
    resources: tuple[LiveResource, ...]
    error: str = ""
    cached: bool = False

    def as_public_dict(self) -> dict[str, Any]:
        """Return only aggregate booking facts. Never return appointment or user fields."""
        return {
            "ok": self.ok,
            "date": self.date,
            "now": self.now,
            "generated_at": self.generated_at,
            "source": self.source,
            "center": {
                "open": self.center_open,
                "reason": self.center_reason,
                "open_periods": [list(period) for period in self.open_periods],
            },
            "resources": [resource.as_dict() for resource in self.resources],
            "cached": self.cached,
            "error": self.error or None,
            "privacy": "aggregate_only",
        }


@dataclass(frozen=True)
class TimeWindow:
    """A Bangkok service-time target. ``end`` is absent for a point lookup."""

    start: str
    end: str | None = None
    explicit: bool = False

    @property
    def label(self) -> str:
        return f"{self.start}-{self.end}" if self.end else self.start

    @property
    def is_range(self) -> bool:
        return self.end is not None


def _as_nonnegative_int(value: object) -> int:
    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return 0


def _build_url(base: str, selected_date: str) -> str:
    parsed = urlparse(base)
    query = dict()
    if parsed.query:
        from urllib.parse import parse_qsl

        query.update(parse_qsl(parsed.query, keep_blank_values=True))
    query["date"] = selected_date
    return urlunparse(parsed._replace(query=urlencode(query)))


def _snapshot_from_payload(payload: dict[str, Any]) -> LiveBookingSnapshot:
    source = str(payload.get("source") or "")
    if not payload.get("ok"):
        raise ValueError(str(payload.get("error") or "booking dashboard returned ok=false"))
    # The dashboard deliberately uses this marker only after both WordPress CSV
    # sources were fetched. Sample data must never be presented as a live slot.
    if source != "remote_csv_live":
        raise ValueError(f"booking dashboard source is not live: {source or 'unknown'}")

    center = payload.get("center")
    if not isinstance(center, dict) or not isinstance(center.get("open"), bool):
        raise ValueError("booking dashboard returned no valid center state")
    periods: list[tuple[str, str]] = []
    for raw in center.get("open_periods") or []:
        if isinstance(raw, (list, tuple)) and len(raw) == 2:
            start, end = str(raw[0]).strip(), str(raw[1]).strip()
            if re.fullmatch(r"\d{2}:\d{2}", start) and re.fullmatch(r"\d{2}:\d{2}", end):
                periods.append((start, end))

    resources: list[LiveResource] = []
    for raw_resource in payload.get("resources") or []:
        if not isinstance(raw_resource, dict):
            continue
        resource_id = str(raw_resource.get("resource_id") or "").strip()
        resource_name = str(raw_resource.get("resource_name") or "").strip()
        if not resource_id or not resource_name:
            continue
        slots: list[LiveSlot] = []
        for raw_slot in raw_resource.get("slots") or []:
            if not isinstance(raw_slot, dict):
                continue
            start, end = str(raw_slot.get("start") or ""), str(raw_slot.get("end") or "")
            if not re.fullmatch(r"\d{2}:\d{2}", start) or not re.fullmatch(r"\d{2}:\d{2}", end):
                continue
            slots.append(LiveSlot(
                start=start,
                end=end,
                status=str(raw_slot.get("status") or "unknown"),
                booked_count=_as_nonnegative_int(raw_slot.get("booked_count")),
                no_show_count=_as_nonnegative_int(raw_slot.get("no_show_count")),
                available_count=_as_nonnegative_int(raw_slot.get("available_count")),
            ))
        resources.append(LiveResource(
            resource_id=resource_id,
            resource_name=resource_name,
            capacity=max(1, _as_nonnegative_int(raw_resource.get("capacity"))),
            status=str(raw_resource.get("status") or "unknown"),
            available_now=_as_nonnegative_int(raw_resource.get("available_now")),
            slots=tuple(slots),
        ))

    if not resources:
        raise ValueError("booking dashboard returned no valid resources")

    return LiveBookingSnapshot(
        ok=True,
        date=str(payload.get("date") or ""),
        now=str(payload.get("now") or ""),
        generated_at=str(payload.get("generated_at") or ""),
        source=source,
        center_open=bool(center.get("open")),
        center_reason=str(center.get("reason") or ""),
        open_periods=tuple(periods),
        resources=tuple(resources),
    )


def _unavailable(selected_date: str, error: str) -> LiveBookingSnapshot:
    return LiveBookingSnapshot(
        ok=False,
        date=selected_date,
        now="",
        generated_at="",
        source="unavailable",
        center_open=False,
        center_reason="",
        open_periods=(),
        resources=(),
        error=error[:240],
    )


def get_live_booking_status(selected_date: str) -> LiveBookingSnapshot:
    """Fetch a sanitized snapshot with a short, per-date in-process cache."""
    if not live_booking_enabled():
        return _unavailable(selected_date, "live booking integration is disabled")

    cache_seconds = _cache_sec()
    now_mono = time.monotonic()
    with _CACHE_LOCK:
        cached = _CACHE.get(selected_date)
        if cached and now_mono - cached[0] <= cache_seconds:
            snapshot = cached[1]
            return LiveBookingSnapshot(**{**snapshot.__dict__, "cached": True})

    # Concurrent browser requests must share one external fetch.  The second
    # cache check is essential: another request may have finished while this
    # one waited for the fetch lock.
    with _FETCH_LOCK:
        now_mono = time.monotonic()
        with _CACHE_LOCK:
            cached = _CACHE.get(selected_date)
            if cached and now_mono - cached[0] <= cache_seconds:
                snapshot = cached[1]
                return LiveBookingSnapshot(**{**snapshot.__dict__, "cached": True})
        try:
            request = Request(
                _build_url(_status_url(), selected_date),
                headers={"Accept": "application/json", "Cache-Control": "no-cache"},
                method="GET",
            )
            with urlopen(request, timeout=_timeout_sec()) as response:  # noqa: S310 - URL is local-owner configuration.
                raw = response.read(2_000_000)
            payload = json.loads(raw.decode("utf-8"))
            if not isinstance(payload, dict):
                raise ValueError("booking dashboard returned a non-object payload")
            returned_date = str(payload.get("date") or "")
            if returned_date != selected_date:
                raise ValueError(f"booking dashboard returned date {returned_date!r}, expected {selected_date!r}")
            snapshot = _snapshot_from_payload(payload)
        except (OSError, TimeoutError, URLError, ValueError, json.JSONDecodeError) as exc:
            snapshot = _unavailable(selected_date, f"{type(exc).__name__}: {exc}")
        except Exception as exc:  # pragma: no cover - safe boundary around external adapter.
            snapshot = _unavailable(selected_date, f"{type(exc).__name__}: {exc}")

        with _CACHE_LOCK:
            _CACHE[selected_date] = (time.monotonic(), snapshot)
        return snapshot


def reset_live_booking_cache() -> None:
    with _CACHE_LOCK:
        _CACHE.clear()


def _normalized_tokens(value: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+|[\u0E00-\u0E7F]+", normalize_text(value)))


def is_live_booking_question(query: str) -> bool:
    q = normalize_text(query)
    if is_weekly_booking_window_query(q):
        return False
    tokens = _normalized_tokens(q)
    # "What equipment is available in VR Zone?" asks about the static
    # inventory, not whether a reservable VR slot is free right now. Keep
    # that catalogue wording out of the live dashboard adapter.
    inventory_question = bool(re.search(
        r"\b(?:what|which)\s+equipment\b|\bequipment\s+(?:is|are)\s+available\b",
        q,
    )) or any(phrase in q for phrase in ("อุปกรณ์อะไร", "มีอุปกรณ์", "อุปกรณ์มีอะไร"))
    if inventory_question:
        return False
    broad_catalog_question = bool(re.search(
        r"\bwhat\s+(?:pc\s+)?hardware\b"
        r"|\bwhat\s+(?:does|do)\s+(?:ps5|playstation|nintendo|vr|cockpit)\s+have\b"
        r"|\bwhat\s+(?:vr|pc|ps5|playstation|nintendo|cockpit)\s+options?\b"
        r"|\bwhat(?:'s|\s+is)\s+in\s+(?:the\s+)?(?:pc|ps5|playstation|nintendo|vr|cockpit)\b",
        q,
    ))
    if broad_catalog_question:
        return False
    # "Which days are available/open?" asks for the published weekly
    # schedule. It is not a live resource-slot lookup unless the user also
    # gives a concrete date/time or says now/today/tomorrow.
    if re.search(r"\b(?:what|which)\s+days?\s+(?:are|is)\s+(?:available|open|opening)\b", q) and not any(
        signal in q for signal in ("right now", "currently", "today", "tomorrow", "ตอนนี้", "วันนี้", "พรุ่งนี้")
    ) and not re.search(r"\b\d{1,2}:\d{2}\b|\b\d{4}-\d{2}-\d{2}\b", q):
        return False
    if re.search(r"\bis\s+there\b.+\bavailable\b", q) and not any(
        signal in q for signal in ("right now", "currently", "today", "tomorrow", "ตอนนี้", "วันนี้", "พรุ่งนี้")
    ):
        return False
    game_catalog_question = bool(re.search(
        r"\b(?:what|which)\s+games?\b|\bgames?\s+(?:is|are)\s+available\b",
        q,
    )) or any(phrase in q for phrase in ("มีเกมอะไร", "เกมอะไรบ้าง", "เกมไหนมี", "รายชื่อเกม"))
    booking_duration_question = bool(re.search(
        r"\bhow\s+long\b.*\b(?:booking\s+)?slot\b|\bslot\b.*\bhow\s+long\b",
        q,
    )) or any(phrase in q for phrase in ("รอบละกี่นาที", "หนึ่งรอบกี่นาที", "slot นานเท่าไหร่"))
    if game_catalog_question or booking_duration_question:
        return False
    price_question = any(term in q for term in (
        "ราคา", "ค่าบริการ", "ค่าใช้จ่าย", "ค่าใช้บริการ", "กี่บาท", "ต้องจ่าย", "เสียเงิน", "ฟรีไหม",
        "how much", "price", "cost", "fee", "pay", "for free", "free of charge", "free to use",
    ))
    explicit_slot = any(term in q for term in ("ว่าง", "ถูกจอง", "จองแล้ว", "available", "availability", "booked", "vacant"))
    if price_question and not explicit_slot:
        return False
    current_signals = (
        "ตอนนี้", "ขณะนี้", "เวลานี้", "current", "currently", "right now", "now",
    )
    availability_signals = (
        "slotว่าง", "ว่าง", "จองแล้ว", "ถูกจอง",
        "available", "availability", "booked", "free", "vacant", "เปิดไหม", "ปิดไหม",
        "open now", "closed now", "slot open", "slots open", "station open",
    )
    asks_live = any(
        signal in tokens if signal.isascii() and " " not in signal else signal in q
        for signal in current_signals
    )
    asks_availability = any(signal in q for signal in availability_signals) or bool(re.search(
        r"จอง(?:ได้|ทัน|ว่าง)(?:ไหม|มั้ย|หรือเปล่า|รึเปล่า)?", q,
    ))
    # A named zone or station implies "now" when the user did not specify a
    # date/time.  This covers natural compact input such as "pc2 ว่างไหม" and
    # "is ps5 1 free?" without confusing a general booking-how-to question
    # with a live availability request.
    asks_resource_availability = asks_availability and bool(_resource_scopes(q))
    # A precise time is a live-slot request only with an availability word.
    asks_time_availability = bool(re.search(r"\b\d{1,2}:\d{2}\b", q)) and asks_availability
    asks_center_use_now = asks_live and any(
        phrase in q for phrase in ("ตอนนี้เล่นได้ไหม", "ตอนนี้เล่นได้มั้ย", "ตอนนี้ใช้ได้ไหม", "ตอนนี้ใช้ได้มั้ย")
    )
    asks_use_now = asks_live and bool(_resource_scopes(q)) and (
        bool(re.search(r"(?:ใช้|เล่น).{0,24}(?:ตอนนี้|ขณะนี้).{0,12}ได้(?:ไหม|มั้ย|หรือเปล่า)?", q))
        or bool(re.search(r"\bcan\b.{0,35}\b(?:use|play)\b.{0,35}\b(?:now|right now)\b", q))
    )
    return asks_resource_availability or asks_use_now or asks_center_use_now or (asks_live and asks_availability) or asks_time_availability or (
        asks_live and bool(tokens & {"open", "closed", "เปิด", "ปิด"})
    )


def resolve_live_target_date(query: str) -> str:
    """Resolve Thai/English relative dates without using the computer locale."""
    q = normalize_text(query)
    today = today_bangkok()
    if "yesterday" in q or "เมื่อวาน" in q:
        return (today - timedelta(days=1)).isoformat()
    if "day after tomorrow" in q or "มะรืน" in q:
        return (today + timedelta(days=2)).isoformat()
    if "tomorrow" in q or "พรุ่งนี้" in q:
        return (today + timedelta(days=1)).isoformat()
    iso_match = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", q)
    if iso_match:
        try:
            return date.fromisoformat(iso_match.group(1)).isoformat()
        except ValueError:
            pass
    resolved = resolve_date_from_text(q, today=today)
    if resolved is not None:
        return resolved.target_date.isoformat()
    weekdays = (
        (0, ("จันทร์", "monday", "mon")),
        (1, ("อังคาร", "tuesday", "tue")),
        (2, ("พุธ", "wednesday", "wed")),
        (3, ("พฤหัส", "thursday", "thu")),
        (4, ("ศุกร์", "friday", "fri")),
        (5, ("เสาร์", "saturday", "sat")),
        (6, ("อาทิตย์", "sunday", "sun")),
    )
    for weekday, names in weekdays:
        if any(name in q if not name.isascii() else re.search(rf"\b{re.escape(name)}\b", q) for name in names):
            this_weekday = any(f"{name}นี้" in q for name in names if not name.isascii()) or any(
                re.search(rf"\bthis\s+{re.escape(name)}\b", q) for name in names if name.isascii()
            )
            if this_weekday and today.weekday() == weekday:
                return today.isoformat()
            days_ahead = (weekday - today.weekday()) % 7 or 7
            if "หน้า" in q or re.search(r"\bnext\b", q):
                if days_ahead < 7 and today.weekday() < weekday:
                    days_ahead += 7
            return (today + timedelta(days=days_ahead)).isoformat()
    return today.isoformat()


def _clock(hour: str, minute: str = "00", suffix: str = "") -> str | None:
    value = int(hour)
    if suffix.lower() == "pm" and value < 12:
        value += 12
    if suffix.lower() == "am" and value == 12:
        value = 0
    if not 0 <= value <= 23 or not 0 <= int(minute) <= 59:
        return None
    return f"{value:02d}:{int(minute):02d}"


_THAI_AFTERNOON_HOURS = {
    "โมง": 13, "หนึ่ง": 13, "1": 13, "สอง": 14, "2": 14,
    "สาม": 15, "3": 15, "สี่": 16, "4": 16, "ห้า": 17, "5": 17,
    "หก": 18, "6": 18,
}


def _thai_afternoon_clock(token: str, half: bool = False) -> str | None:
    hour = _THAI_AFTERNOON_HOURS.get(token)
    if hour is None:
        return None
    return _clock(str(hour), "30" if half else "00")


def requested_time_window(query: str, snapshot: LiveBookingSnapshot) -> TimeWindow | None:
    """Read numeric and conversational Thai time expressions into a time target."""
    q = normalize_text(query)
    colon_range = re.search(
        r"\b([01]?\d|2[0-3]):([0-5]\d)\s*(?:-|–|to|until|ถึง)\s*([01]?\d|2[0-3]):([0-5]\d)\b",
        q,
    )
    if colon_range:
        start = _clock(colon_range.group(1), colon_range.group(2))
        end = _clock(colon_range.group(3), colon_range.group(4))
        if start and end and start < end:
            return TimeWindow(start, end, explicit=True)

    hour_range = re.search(
        r"\b([01]?\d|2[0-3])\s*(?:โมง)?\s*(?:-|–|to|until|ถึง)\s*([01]?\d|2[0-3])\s*(?:โมง)?\b",
        q,
    )
    if hour_range:
        start = _clock(hour_range.group(1))
        end = _clock(hour_range.group(2))
        if start and end and start < end:
            return TimeWindow(start, end, explicit=True)

    afternoon_range = re.search(
        r"(?:ตอน)?บ่าย\s*(โมง|หนึ่ง|1|สอง|2|สาม|3|สี่|4|ห้า|5|หก|6)\s*(?:โมง)?\s*(ครึ่ง)?\s*(?:-|–|to|until|ถึง)\s*(?:ตอน)?บ่าย\s*(โมง|หนึ่ง|1|สอง|2|สาม|3|สี่|4|ห้า|5|หก|6)\s*(?:โมง)?\s*(ครึ่ง)?",
        q,
    )
    if afternoon_range:
        start = _thai_afternoon_clock(afternoon_range.group(1), bool(afternoon_range.group(2)))
        end = _thai_afternoon_clock(afternoon_range.group(3), bool(afternoon_range.group(4)))
        if start and end and start < end:
            return TimeWindow(start, end, explicit=True)

    afternoon_point = re.search(
        r"(?:ตอน)?บ่าย\s*(โมง|หนึ่ง|1|สอง|2|สาม|3|สี่|4|ห้า|5|หก|6)\s*(?:โมง)?\s*(ครึ่ง)?",
        q,
    )
    if afternoon_point:
        value = _thai_afternoon_clock(afternoon_point.group(1), bool(afternoon_point.group(2)))
        if value:
            return TimeWindow(value, explicit=True)

    noon = re.search(r"เที่ยง\s*(ครึ่ง)?", q)
    if noon:
        return TimeWindow("12:30" if noon.group(1) else "12:00", explicit=True)

    # Thai often joins the time to the preceding word ("ตอน10โมง").
    point = re.search(r"(?<!\d)([01]?\d|2[0-3]):([0-5]\d)(?!\d)", q)
    if point:
        value = _clock(point.group(1), point.group(2))
        return TimeWindow(value, explicit=True) if value else None
    hour = re.search(r"(?<![a-z0-9])([01]?\d|2[0-3])\s*(โมง|am|pm)(ครึ่ง)?", q)
    if hour:
        value = _clock(hour.group(1), "30" if hour.group(3) else "00", hour.group(2))
        return TimeWindow(value, explicit=True) if value else None
    if snapshot.now:
        # Anchor the fallback to the time portion of the timestamp. A word
        # boundary can otherwise select its minutes/seconds as the hour.
        time_match = re.search(r"(?:T|\s)(\d{2}:\d{2})(?::\d{2})?", snapshot.now)
        if time_match:
            return TimeWindow(time_match.group(1), explicit=False)
    return None


def requested_time(query: str, snapshot: LiveBookingSnapshot) -> str | None:
    """Compatibility helper for callers which need the start of a time target."""
    window = requested_time_window(query, snapshot)
    return window.start if window else None


def _resource_family(resource: LiveResource) -> str:
    name = normalize_text(resource.resource_name)
    if "playstation" in name:
        return "ps5"
    if "nintendo" in name:
        return "switch"
    if "cockpit" in name:
        return "cockpit"
    if "vr station" in name:
        return "vr"
    if "pc #" in name:
        return "pc"
    return "other"


_RESOURCE_GROUPS = (
    ("ps5", ("playstation 5", "play station 5", "playstation", "play station", "ps5", "ps 5", "เพลย์ห้า", "เพลย์ 5", "เพลย์"), "PlayStation 5 Zone", "โซน PlayStation 5"),
    ("switch", ("nintendo switch", "nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์"), "Nintendo Switch Zone", "โซน Nintendo Switch"),
    ("cockpit", ("cockpit", "racing", "ค็อกพิท", "คอกพิท", "พวงมาลัย"), "Cockpit Zone", "โซน Cockpit"),
    ("vr", ("psvr", "virtual reality", "vr", "วีอาร์", "แว่น"), "VR Zone", "โซน VR"),
    ("pc", ("computer", "pc", "คอมพิวเตอร์", "เครื่องคอม", "เครื่อง pc", "คอม"), "PC Zone", "โซน PC"),
)


def _resource_scopes(query: str) -> tuple[str, ...]:
    """Return every requested equipment family, not just the first one.

    A question such as ``PC กับ VR ว่างไหม`` therefore stays a two-target
    status lookup rather than being silently narrowed to one zone.
    """
    q = normalize_text(query)
    tokens = _normalized_tokens(q)
    positions: dict[str, int] = {}
    # Compact station names are common in chat. They are intentionally
    # recognized before token matching because "pc2" is one token, not
    # "pc" + "2".
    compact_station_patterns = (
        ("ps5", r"\bps\s*5\s*#?\s*0?\d{1,2}\b|\bplaystation\s*5\s*#?\s*0?\d{1,2}\b"),
        ("cockpit", r"\bcockpit\s*#?\s*0?\d{1,2}\b"),
        ("pc", r"\b(?:pc|computer)\s*#?\s*0?\d{1,2}\b"),
    )
    for family, pattern in compact_station_patterns:
        match = re.search(pattern, q)
        if match:
            positions[family] = match.start()
    for family, signals, _, _ in _RESOURCE_GROUPS:
        for signal in signals:
            # Short English labels must be whole tokens: "pc" must not match
            # an unrelated word such as "space".
            matches = signal in tokens if signal.isascii() and len(signal) <= 3 else signal in q
            if matches:
                position = q.find(signal)
                positions[family] = min(positions.get(family, position), position)
                break
    return tuple(family for family, _ in sorted(positions.items(), key=lambda item: item[1]))


def _resource_scope(query: str) -> str | None:
    """Compatibility helper for callers that only need the first scope."""
    scopes = _resource_scopes(query)
    return scopes[0] if scopes else None


def _scope_label(family: str | None, locale: str) -> str | None:
    for candidate, _, english_label, thai_label in _RESOURCE_GROUPS:
        if candidate == family:
            return english_label if locale == "en" else thai_label
    return None


def _requested_resource_number(query: str, family: str | None) -> int | None:
    if family is None:
        return None
    q = normalize_text(query)
    family_patterns = {
        "pc": r"\b(?:pc|computer)\s*(?:#|station|เครื่อง)?\s*0?(\d{1,2})\b|(?:คอม|คอมพิวเตอร์)\s*(?:เครื่อง)?\s*0?(\d{1,2})\b",
        "ps5": r"\b(?:ps5|playstation\s*5)\s*(?:#|station|เครื่อง)?\s*0?(\d{1,2})\b",
        "cockpit": r"\bcockpit\s*(?:#|station|เครื่อง)?\s*0?(\d{1,2})\b|ค็อกพิท\s*(?:เครื่อง)?\s*0?(\d{1,2})\b",
        "switch": r"\b(?:nintendo(?:\s+switch)?|switch)\s*(?:#|station|เครื่อง)?\s*0?(\d{1,2})\b",
        "vr": r"\bvr\s*(?:#|station|เครื่อง)?\s*0?(\d{1,2})\b",
    }
    pattern = family_patterns.get(family)
    if not pattern:
        return None
    match = re.search(pattern, q)
    if not match:
        return None
    return int(next(value for value in match.groups() if value is not None))


def _resources_for_family(snapshot: LiveBookingSnapshot, query: str, family: str | None) -> tuple[LiveResource, ...]:
    """Filter one family and, when requested, one numbered station."""
    selected = tuple(resource for resource in snapshot.resources if family is None or _resource_family(resource) == family)
    number = _requested_resource_number(query, family)
    if number is not None:
        numbered = tuple(
            resource for resource in selected
            if re.search(rf"#0?{number}(?!\d)", normalize_text(resource.resource_name))
        )
        # A requested-but-unknown station must not fall back to the whole
        # zone. Doing so could falsely answer that PC #99 is available.
        selected = numbered
    if family in {"switch", "vr"}:
        q = normalize_text(query)
        period = "morning" if any(signal in q for signal in ("morning", "เช้า")) else "afternoon" if any(signal in q for signal in ("afternoon", "บ่าย")) else ""
        if period:
            period_selected = tuple(resource for resource in selected if period in normalize_text(resource.resource_name))
            if period_selected:
                selected = period_selected
    return selected


def _resource_groups_for_query(snapshot: LiveBookingSnapshot, query: str) -> tuple[tuple[str | None, tuple[LiveResource, ...]], ...]:
    """Group requested resources by family; preserve every mentioned zone."""
    scopes = _resource_scopes(query)
    if not scopes:
        return ((None, tuple(snapshot.resources)),)
    return tuple((family, _resources_for_family(snapshot, query, family)) for family in scopes)


def _resources_for_query(snapshot: LiveBookingSnapshot, query: str) -> tuple[tuple[LiveResource, ...], str | None]:
    """Compatibility helper used by older callers; multi-scope callers use groups."""
    family = _resource_scope(query)
    return _resources_for_family(snapshot, query, family), family


def resource_slots_at(resources: tuple[LiveResource, ...], when: str | None) -> list[tuple[LiveResource, LiveSlot]]:
    if not when:
        return []
    return [
        (resource, slot)
        for resource in resources
        for slot in resource.slots
        if slot.start <= when < slot.end
    ]


def _slot_window_for_resources(resources: tuple[LiveResource, ...], window: TimeWindow | None) -> TimeWindow | None:
    """Turn an explicit point such as 13:00 into its dashboard Slot range.

    The dashboard is authoritative for Slot boundaries: PC may be hourly while
    another resource can have a shorter slot. No promotion is made for an
    implicit "now" lookup.
    """
    if window is None or window.is_range or not window.explicit:
        return window
    boundaries = {
        (slot.start, slot.end)
        for resource in resources
        for slot in resource.slots
        if slot.start <= window.start < slot.end
    }
    if len(boundaries) == 1:
        start, end = next(iter(boundaries))
        return TimeWindow(start, end, explicit=True)
    return window


def _historical_window(snapshot: LiveBookingSnapshot, window: TimeWindow | None) -> bool:
    """Whether the selected Slot ended before the dashboard snapshot time."""
    if window is None or not window.end or not snapshot.date or not snapshot.now:
        return False
    try:
        target_end = datetime.strptime(f"{snapshot.date} {window.end}", "%Y-%m-%d %H:%M")
        snapshot_now = datetime.strptime(snapshot.now[:19], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return False
    return target_end <= snapshot_now


def _resource_booking_history_for_range(resource: LiveResource, window: TimeWindow) -> str:
    """Return historical booking evidence without labelling a past Slot bookable."""
    assert window.end is not None
    slots = sorted(
        (slot for slot in resource.slots if slot.start < window.end and slot.end > window.start),
        key=lambda slot: (slot.start, slot.end),
    )
    if not slots:
        return "no_matching_slot"
    cursor = window.start
    for slot in slots:
        if slot.start > cursor:
            return "incomplete_coverage"
        cursor = max(cursor, slot.end)
        if slot.status == "closed":
            return "closed"
        if slot.booked_count > 0 or slot.no_show_count > 0:
            return "booked"
    if cursor < window.end:
        return "incomplete_coverage"
    return "not_booked"


def _resource_is_free_for_range(resource: LiveResource, window: TimeWindow) -> tuple[bool, int, str]:
    """A range is free only when every overlapping slot is covered and free."""
    assert window.end is not None
    slots = sorted(
        (slot for slot in resource.slots if slot.start < window.end and slot.end > window.start),
        key=lambda slot: (slot.start, slot.end),
    )
    if not slots:
        return False, 0, "no_matching_slot"
    cursor = window.start
    availability: list[int] = []
    for slot in slots:
        if slot.start > cursor:
            return False, 0, "incomplete_coverage"
        cursor = max(cursor, slot.end)
        if slot.status in {"closed", "no_show", "past"} or slot.available_count <= 0:
            return False, 0, slot.status
        availability.append(slot.available_count)
    if cursor < window.end:
        return False, 0, "incomplete_coverage"
    return True, min(availability), "available"


def is_open_for_window(snapshot: LiveBookingSnapshot, window: TimeWindow | None) -> bool:
    if not snapshot.center_open or window is None:
        return False
    if window.end is None:
        return any(start <= window.start < period_end for start, period_end in snapshot.open_periods)
    return any(start <= window.start and window.end <= period_end for start, period_end in snapshot.open_periods)


def live_booking_calendar_conflict(query: str, snapshot: LiveBookingSnapshot) -> str | None:
    """Flag a claimed open Dashboard window that the recorded calendar does not support.

    This does not choose which source controls bookings; it prevents a false
    availability claim until the owner reconciles the two schedules.
    """
    if not snapshot.ok or not snapshot.center_open:
        return None
    window = requested_time_window(query, snapshot)
    if window is None or not is_open_for_window(snapshot, window):
        return None
    try:
        target = date.fromisoformat(snapshot.date)
    except ValueError:
        return None
    closure = closure_for(target)
    if closure is not None and closure.status == "closed":
        return "recorded_special_closure"
    for period in regular_service_slots(target):
        if period["state"] != "open":
            continue
        start, end = period["start"], period["end"]
        if start <= window.start and (window.end <= end if window.end else window.start < end):
            return None
    return "published_service_hours"


def _time_context(snapshot: LiveBookingSnapshot, window: TimeWindow | None, locale: str) -> str:
    if window is None:
        return "--:--"
    target_date = snapshot.date or "unknown date"
    if locale == "en":
        return f"{target_date}, {window.label} (Asia/Bangkok)"
    return f"วันที่ {target_date} ช่วง {window.label} น. (เวลาไทย)"


def _asks_resource_list(query: str) -> bool:
    """Return true only when the wording asks to enumerate resources."""
    q = normalize_text(query)
    list_signals = (
        "อะไรบ้าง", "อะไรว่าง", "ว่างบ้าง", "อันไหน", "ไหนบ้าง", "ไหนว่าง", "ไหน ",
        "ทั้งหมด", "ทุกเครื่อง", "แต่ละเครื่อง", "รายชื่อ", "slots", "list", "which",
        "show", "all stations", "what stations",
    )
    return any(signal in q for signal in list_signals)


def _point_slot_status(resource: LiveResource, window: TimeWindow | None) -> LiveSlot | None:
    if window is None:
        return None
    for slot in resource.slots:
        if slot.start <= window.start < slot.end:
            return slot
    return None


def _single_resource_answer(
    resource: LiveResource,
    snapshot: LiveBookingSnapshot,
    window: TimeWindow | None,
    locale: str,
) -> str | None:
    """Give a direct answer for one explicitly named resource, without a list."""
    window = _slot_window_for_resources((resource,), window)
    if window is None:
        return None

    english = locale == "en"
    if not is_open_for_window(snapshot, window):
        if english:
            return f"{resource.resource_name} is not bookable at {window.label} because the studio is not open then."
        return f"{resource.resource_name} ยังจองไม่ได้ช่วง {window.label} น. เพราะศูนย์ไม่เปิดให้บริการในเวลานั้นครับ"

    if _historical_window(snapshot, window):
        history = _resource_booking_history_for_range(resource, window)
        if history == "booked":
            return (
                f"{resource.resource_name} was booked during {window.label} (Asia/Bangkok)."
                if english
                else f"{resource.resource_name} ถูกจองในช่วง {window.label} น. (เวลาไทย) ครับ"
            )
        if history == "not_booked":
            return (
                f"{resource.resource_name} had no booking during {window.label} (Asia/Bangkok)."
                if english
                else f"{resource.resource_name} ไม่มีรายการจองในช่วง {window.label} น. (เวลาไทย) ครับ"
            )
        if history == "closed":
            return (
                f"{resource.resource_name} was not open for booking during {window.label} (Asia/Bangkok)."
                if english
                else f"{resource.resource_name} ไม่เปิดให้จองในช่วง {window.label} น. (เวลาไทย) ครับ"
            )
        return (
            f"{resource.resource_name}: booking history cannot be confirmed for {window.label}."
            if english
            else f"{resource.resource_name}: ยังยืนยันประวัติการจองช่วง {window.label} น. ไม่ได้ครับ"
        )

    if window.is_range:
        free, _, _ = _resource_is_free_for_range(resource, window)
        if english:
            return (
                f"{resource.resource_name} is available for the full period {window.label} (Asia/Bangkok)."
                if free
                else f"{resource.resource_name} is not available for the full period {window.label} (Asia/Bangkok)."
            )
        return (
            f"{resource.resource_name} ว่างตลอดช่วง {window.label} น. (เวลาไทย) ครับ"
            if free
            else f"{resource.resource_name} ไม่ว่างตลอดช่วง {window.label} น. (เวลาไทย) ครับ"
        )

    slot = _point_slot_status(resource, window)
    available = bool(slot and slot.available_count > 0 and slot.status not in {"no_show", "closed", "past"})
    if english:
        return (
            f"{resource.resource_name} is available right now ({window.start}, Asia/Bangkok)."
            if available
            else f"{resource.resource_name} is not available right now ({window.start}, Asia/Bangkok)."
        )
    return (
        f"{resource.resource_name} ว่างอยู่ตอนนี้ ณ {window.start} น. (เวลาไทย) ครับ"
        if available
        else f"{resource.resource_name} ไม่ว่างตอนนี้ ณ {window.start} น. (เวลาไทย) ครับ"
    )


def _targeted_group_answer(
    family: str,
    resources: tuple[LiveResource, ...],
    query: str,
    snapshot: LiveBookingSnapshot,
    window: TimeWindow | None,
    locale: str,
) -> str:
    """Render one requested zone or one requested station concisely."""
    window = _slot_window_for_resources(resources, window)
    english = locale == "en"
    label = _scope_label(family, "en" if english else "th") or family
    requested_number = _requested_resource_number(query, family)

    if not resources:
        if english:
            requested = f"{label} station #{requested_number}" if requested_number is not None else label
            return f"I could not find {requested} in the live Booking Dashboard."
        requested = f"{label} เครื่อง #{requested_number}" if requested_number is not None else label
        return f"ไม่พบ {requested} ใน Booking Dashboard ครับ"

    if requested_number is not None and len(resources) == 1:
        direct = _single_resource_answer(resources[0], snapshot, window, locale)
        if direct is not None:
            return direct

    if not is_open_for_window(snapshot, window):
        if english:
            return f"{label} is not bookable at {window.label if window else 'this time'} because the studio is not open then."
        return f"{label} ยังจองไม่ได้ช่วง {window.label if window else 'เวลานี้'} เพราะศูนย์ไม่เปิดให้บริการครับ"

    if _historical_window(snapshot, window):
        assert window is not None and window.end is not None
        history = [_resource_booking_history_for_range(resource, window) for resource in resources]
        booked = sum(1 for state in history if state == "booked")
        no_booking = sum(1 for state in history if state == "not_booked")
        if english:
            return f"{label}: {booked}/{len(resources)} resources were booked during {window.label}; {no_booking}/{len(resources)} had no booking."
        return f"{label}: ช่วง {window.label} น. ถูกจอง {booked}/{len(resources)} รายการ และไม่มีรายการจอง {no_booking}/{len(resources)} รายการ"

    if window is not None and window.is_range:
        rows = [(_resource_is_free_for_range(resource, window)) for resource in resources]
        available = sum(1 for free, _, _ in rows if free)
        if english:
            return f"{label}: {available}/{len(resources)} resources are available for the full period {window.label}."
        if available == 0:
            return f"{label}: ไม่ว่างตลอดช่วง {window.label} น. (ว่าง 0/{len(resources)} รายการ)"
        return f"{label}: ว่างตลอดช่วง {window.label} น. {available}/{len(resources)} รายการ"

    rows = resource_slots_at(resources, window.start if window else None)
    if not rows:
        if english:
            return f"{label}: the live dashboard did not return a matching slot, so availability cannot be confirmed."
        return f"{label}: Dashboard ไม่พบ Slot ที่ตรงกับเวลานี้ จึงยังยืนยันความว่างไม่ได้ครับ"
    available = sum(
        1
        for _, slot in rows
        if slot.available_count > 0 and slot.status not in {"no_show", "closed", "past"}
    )
    if english:
        return f"{label}: {available}/{len(rows)} resources are available right now ({window.start}, Asia/Bangkok)."
    if available == 0:
        return f"{label}: ไม่ว่าง ณ {window.start} น. (ว่าง 0/{len(rows)} รายการ, เวลาไทย)"
    return f"{label}: ว่าง {available}/{len(rows)} รายการ ณ {window.start} น. (เวลาไทย)"


def render_live_booking_answer(query: str, snapshot: LiveBookingSnapshot, locale: str) -> str:
    """Render only aggregate facts. The request is read-only and cannot reserve a slot."""
    english = locale == "en"
    if not snapshot.ok:
        if english:
            return (
                f"For {snapshot.date} (Asia/Bangkok), I cannot confirm the live opening or booking status because the Booking Dashboard is unavailable. "
                "I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.\n"
                f"Source: {BOOKING_SOURCE_URL}"
            )
        return (
            f"วันที่ {snapshot.date} (เวลาไทย) ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ\n"
            "ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง\n"
            f"แหล่งข้อมูล: {BOOKING_SOURCE_URL}"
        )

    conflict = live_booking_calendar_conflict(query, snapshot)
    if conflict is not None:
        window = requested_time_window(query, snapshot)
        when = window.label if window is not None else "the requested time"
        if english:
            return (
                f"For {snapshot.date} at {when} (Asia/Bangkok), the Booking Dashboard and the recorded service calendar disagree. "
                "I cannot confirm whether this period is bookable or available. Please check with the studio.\n"
                f"Source: {BOOKING_SOURCE_URL}"
            )
        return (
            f"วันที่ {snapshot.date} ช่วง {when} น. (เวลาไทย) ข้อมูลจาก Booking Dashboard ขัดกับปฏิทินบริการที่บันทึกไว้ "
            "จึงยังยืนยันไม่ได้ว่าช่วงนี้จองได้หรือมีเครื่องว่าง กรุณาตรวจสอบกับศูนย์ครับ\n"
            f"แหล่งข้อมูล: {BOOKING_SOURCE_URL}"
        )

    window = requested_time_window(query, snapshot)
    resource_groups = _resource_groups_for_query(snapshot, query)
    requested_scopes = _resource_scopes(query)
    # For direct availability questions, answer only the requested targets.
    # Lists remain available for wording such as "มีอะไรบ้าง" / "which
    # stations" and use the detailed rendering below.
    if requested_scopes and not _asks_resource_list(query):
        targeted = [
            _targeted_group_answer(family, resources, query, snapshot, window, "en" if english else "th")
            for family, resources in resource_groups
            if family is not None
        ]
        if targeted:
            date_line = f"Date: {snapshot.date} (Asia/Bangkok)" if english else f"วันที่ตรวจสอบ: {snapshot.date} (เวลาไทย)"
            updated = f"Updated: {snapshot.generated_at or snapshot.now}" if english else f"อัปเดต: {snapshot.generated_at or snapshot.now}"
            source = f"Source: {BOOKING_SOURCE_URL}" if english else f"แหล่งข้อมูล: {BOOKING_SOURCE_URL}"
            return "\n".join((date_line, *targeted, updated, source))

    selected_resources = tuple(
        resource
        for _, resources in resource_groups
        for resource in resources
    )
    window = _slot_window_for_resources(selected_resources, window)
    service_open = is_open_for_window(snapshot, window)
    scope_family = requested_scopes[0] if len(requested_scopes) == 1 else None
    scope_label = _scope_label(scope_family, "en" if english else "th")
    requested_number = _requested_resource_number(query, scope_family)
    # A direct station question should stay direct: "pc2 ว่างไหม" answers
    # only PC #02.  It must not be expanded into a whole-zone report.
    if requested_number is not None and len(selected_resources) == 1:
        direct = _single_resource_answer(selected_resources[0], snapshot, window, "en" if english else "th")
        if direct is not None:
            return direct
    slot_rows = resource_slots_at(selected_resources, window.start if window else None)
    asks_list = _asks_resource_list(query)
    time_context = _time_context(snapshot, window, "en" if english else "th")
    refreshed = snapshot.generated_at or snapshot.now

    if window is not None and window.is_range:
        range_rows = [
            (resource, *_resource_is_free_for_range(resource, window))
            for resource in selected_resources
        ]
    else:
        range_rows = []

    if english:
        headline = (
            f"Live status for {time_context}: the studio is open for this requested time."
            if service_open
            else f"Live status for {time_context}: the studio is not open for this requested time."
        )
        lines = [headline]
        if snapshot.center_reason:
            # An owner can enter a Thai free-text closure note in the dashboard.
            # Do not leak it into an English response or translate it at runtime.
            # The bounded English wording still preserves the verified state.
            if re.search(r"[\u0E00-\u0E7F]", snapshot.center_reason):
                lines.append("Reason: A maintenance period or special closure is recorded for this date.")
            else:
                lines.append(f"Reason: {snapshot.center_reason}")
        if service_open and range_rows:
            available = sum(1 for _, free, _, _ in range_rows if free)
            scope = scope_label or "All resource groups"
            lines.append(f"{scope}: {available}/{len(range_rows)} resources are available for the full requested period.")
            if asks_list:
                lines.append("")
                lines.append("Resource status for the full period:")
                for resource, free, available_count, reason in range_rows:
                    if free:
                        label = f"available for the full period ({available_count} unit)"
                    elif reason == "no_show":
                        label = "not bookable (no-show hold)"
                    elif reason in {"closed", "past"}:
                        label = "not bookable for this period"
                    else:
                        label = "booked or unavailable during part of the period"
                    lines.append(f"•    {resource.resource_name}: {label}")
        elif service_open and slot_rows:
            available = sum(1 for _, slot in slot_rows if slot.available_count > 0 and slot.status not in {"no_show", "closed", "past"})
            scope = scope_label or "All resource groups"
            lines.append(f"{scope}: {available}/{len(slot_rows)} resources have at least one available unit.")
            if asks_list:
                lines.append("")
                lines.append("Slot status:")
                for resource, slot in slot_rows:
                    if slot.available_count > 0 and slot.status not in {"no_show", "closed", "past"}:
                        label = f"available ({slot.available_count} unit)"
                    elif slot.status == "no_show":
                        label = "not bookable (no-show hold)"
                    elif slot.status in {"closed", "past"}:
                        label = "not bookable"
                    else:
                        label = "booked"
                    lines.append(f"•    {resource.resource_name}: {label}")
        elif service_open:
            lines.append("The dashboard did not return a matching slot for this time, so availability cannot be confirmed.")
        lines.extend([
            f"Updated: {refreshed} (live WordPress booking export{' cached briefly' if snapshot.cached else ''})",
            f"Source: {BOOKING_SOURCE_URL}",
        ])
        return "\n".join(lines)

    headline = (
        f"สถานะสด {time_context}: ศูนย์เปิดให้บริการในช่วงเวลาที่ถามครับ"
        if service_open
        else f"สถานะสด {time_context}: ศูนย์ยังไม่เปิดให้บริการในช่วงเวลาที่ถามครับ"
    )
    lines = [headline]
    if snapshot.center_reason:
        lines.append(f"เหตุผล: {snapshot.center_reason}")
    if service_open and range_rows:
        available = sum(1 for _, free, _, _ in range_rows if free)
        scope = scope_label or "ทุกโซน"
        lines.append(f"{scope}: ว่างตลอดช่วงเวลาที่ถาม {available}/{len(range_rows)} รายการ")
        if asks_list:
            lines.append("")
            lines.append("สถานะทรัพยากรตลอดช่วงเวลา:")
            for resource, free, available_count, reason in range_rows:
                if free:
                    label = f"ว่างตลอดช่วง ({available_count} เครื่อง/หน่วย)"
                elif reason == "no_show":
                    label = "ยังจองไม่ได้ (สถานะ no-show)"
                elif reason in {"closed", "past"}:
                    label = "ใช้ไม่ได้ในช่วงเวลานี้"
                else:
                    label = "ถูกจองหรือไม่ว่างบางส่วนของช่วงเวลา"
                lines.append(f"•    {resource.resource_name}: {label}")
    elif service_open and slot_rows:
        available = sum(1 for _, slot in slot_rows if slot.available_count > 0 and slot.status not in {"no_show", "closed", "past"})
        scope = scope_label or "ทุกโซน"
        lines.append(f"{scope}: ว่างอย่างน้อย {available}/{len(slot_rows)} รายการ ณ เวลานี้")
        if asks_list:
            lines.append("")
            lines.append("สถานะ Slot:")
            for resource, slot in slot_rows:
                if slot.available_count > 0 and slot.status not in {"no_show", "closed", "past"}:
                    label = f"ว่าง ({slot.available_count} เครื่อง/หน่วย)"
                elif slot.status == "no_show":
                    label = "ยังจองไม่ได้ (สถานะ no-show)"
                elif slot.status in {"closed", "past"}:
                    label = "ใช้ไม่ได้ในช่วงเวลานี้"
                else:
                    label = "ถูกจองแล้ว"
                lines.append(f"•    {resource.resource_name}: {label}")
    elif service_open:
        lines.append("Dashboard ไม่พบ Slot ที่ตรงกับเวลานี้ จึงยังยืนยันความว่างไม่ได้ครับ")
    lines.extend([
        f"อัปเดต: {refreshed} (ข้อมูลจองสดจาก WordPress{' ใช้ cache ระยะสั้น' if snapshot.cached else ''})",
        f"แหล่งข้อมูล: {BOOKING_SOURCE_URL}",
    ])
    return "\n".join(lines)
