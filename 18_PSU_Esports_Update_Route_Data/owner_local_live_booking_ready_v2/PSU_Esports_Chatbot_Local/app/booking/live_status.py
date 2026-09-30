from __future__ import annotations

import json
import os
import re
import threading
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from urllib.error import URLError
from urllib.parse import urlencode, urlparse, urlunparse
from urllib.request import Request, urlopen

from app.core.normalization import normalize_text


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

    center = payload.get("center") if isinstance(payload.get("center"), dict) else {}
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
    tokens = _normalized_tokens(q)
    current_signals = (
        "ตอนนี้", "ขณะนี้", "เวลานี้", "current", "currently", "right now", "now",
    )
    availability_signals = (
        "slot", "slots", "สลอต", "slotว่าง", "ว่าง", "จอง", "จองแล้ว", "ถูกจอง",
        "available", "availability", "booked", "free", "vacant", "เปิดไหม", "ปิดไหม",
        "open now", "closed now",
    )
    asks_live = any(signal in q for signal in current_signals)
    asks_availability = any(signal in q for signal in availability_signals)
    # A precise time is a live-slot request only with an availability word.
    asks_time_availability = bool(re.search(r"\b\d{1,2}:\d{2}\b", q)) and asks_availability
    return (asks_live and asks_availability) or asks_time_availability or (
        asks_live and bool(tokens & {"open", "closed", "เปิด", "ปิด"})
    )


def requested_time(query: str, snapshot: LiveBookingSnapshot) -> str | None:
    match = re.search(r"\b([01]?\d|2[0-3]):([0-5]\d)\b", normalize_text(query))
    if match:
        return f"{int(match.group(1)):02d}:{match.group(2)}"
    match = re.search(r"\b([01]?\d|2[0-3])\s*(?:โมง|am|pm)\b", normalize_text(query))
    if match:
        hour = int(match.group(1))
        if "pm" in match.group(0) and hour < 12:
            hour += 12
        return f"{hour:02d}:00"
    if snapshot.now:
        time_match = re.search(r"\b(\d{2}:\d{2})", snapshot.now)
        if time_match:
            return time_match.group(1)
    return None


def resource_slots_at(snapshot: LiveBookingSnapshot, when: str | None) -> list[tuple[LiveResource, LiveSlot]]:
    if not when:
        return []
    return [
        (resource, slot)
        for resource in snapshot.resources
        for slot in resource.slots
        if slot.start <= when < slot.end
    ]


def _resources_for_query(snapshot: LiveBookingSnapshot, query: str) -> tuple[LiveResource, ...]:
    """Limit a live list to the requested resource family when it is explicit."""
    q = normalize_text(query)
    groups = (
        (("playstation", "ps5", "เพลย์", "play station"), ("playstation",)),
        (("nintendo", "switch", "นินเทนโด", "สวิตช์"), ("nintendo",)),
        (("cockpit", "ค็อกพิท", "พวงมาลัย"), ("cockpit",)),
        (("vr", "แว่น"), ("vr station",)),
        (("pc", "computer", "คอม", "คอมพิวเตอร์"), ("pc #",)),
    )
    for signals, name_fragments in groups:
        if any(signal in q for signal in signals):
            selected = tuple(
                resource
                for resource in snapshot.resources
                if any(fragment in normalize_text(resource.resource_name) for fragment in name_fragments)
            )
            if selected:
                return selected
    return snapshot.resources


def is_open_at(snapshot: LiveBookingSnapshot, when: str | None) -> bool:
    return bool(snapshot.center_open and when and any(start <= when < end for start, end in snapshot.open_periods))


def render_live_booking_answer(query: str, snapshot: LiveBookingSnapshot, locale: str) -> str:
    """Render only aggregate facts. The request is read-only and cannot reserve a slot."""
    english = locale == "en"
    if not snapshot.ok:
        if english:
            return (
                "I cannot confirm the live opening or booking status right now because the Booking Dashboard is unavailable. "
                "I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.\n"
                f"Source: {BOOKING_SOURCE_URL}"
            )
        return (
            "ขณะนี้ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ\n"
            "ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง\n"
            f"แหล่งข้อมูล: {BOOKING_SOURCE_URL}"
        )

    when = requested_time(query, snapshot)
    open_now = is_open_at(snapshot, when)
    selected_snapshot = LiveBookingSnapshot(**{**snapshot.__dict__, "resources": _resources_for_query(snapshot, query)})
    slot_rows = resource_slots_at(selected_snapshot, when)
    asks_list = any(signal in normalize_text(query) for signal in (
        "slot", "slots", "สลอต", "ว่าง", "ถูกจอง", "จองแล้ว", "available", "booked", "which", "อะไร", "ไหน",
    ))
    status_time = when or "--:--"
    refreshed = snapshot.generated_at or snapshot.now

    if english:
        headline = (
            f"Live status at {status_time} (Asia/Bangkok): the studio is open."
            if open_now
            else f"Live status at {status_time} (Asia/Bangkok): the studio is not open for service."
        )
        lines = [headline]
        if snapshot.center_reason:
            lines.append(f"Reason: {snapshot.center_reason}")
        if open_now and slot_rows:
            available = sum(1 for _, slot in slot_rows if slot.available_count > 0)
            lines.append(f"Current resource slots: {available}/{len(slot_rows)} have at least one available unit.")
            if asks_list:
                lines.append("")
                lines.append("Slot status:")
                for resource, slot in slot_rows:
                    if slot.available_count > 0:
                        label = f"available ({slot.available_count} unit)"
                    elif slot.status == "no_show":
                        label = "not bookable (no-show hold)"
                    else:
                        label = "booked"
                    lines.append(f"•    {resource.resource_name}: {label}")
        elif open_now:
            lines.append("The dashboard did not return a matching slot for this time, so availability cannot be confirmed.")
        lines.extend([
            f"Updated: {refreshed} (live WordPress booking export{' cached briefly' if snapshot.cached else ''})",
            f"Source: {BOOKING_SOURCE_URL}",
        ])
        return "\n".join(lines)

    headline = (
        f"สถานะสด ณ {status_time} น. (เวลาไทย): ศูนย์เปิดให้บริการครับ"
        if open_now
        else f"สถานะสด ณ {status_time} น. (เวลาไทย): ศูนย์ยังไม่เปิดให้บริการในช่วงเวลานี้ครับ"
    )
    lines = [headline]
    if snapshot.center_reason:
        lines.append(f"เหตุผล: {snapshot.center_reason}")
    if open_now and slot_rows:
        available = sum(1 for _, slot in slot_rows if slot.available_count > 0)
        lines.append(f"Slot ของทรัพยากร ณ เวลานี้: ว่างอย่างน้อย {available}/{len(slot_rows)} รายการ")
        if asks_list:
            lines.append("")
            lines.append("สถานะ Slot:")
            for resource, slot in slot_rows:
                if slot.available_count > 0:
                    label = f"ว่าง ({slot.available_count} เครื่อง/หน่วย)"
                elif slot.status == "no_show":
                    label = "ยังจองไม่ได้ (สถานะ no-show)"
                else:
                    label = "ถูกจองแล้ว"
                lines.append(f"•    {resource.resource_name}: {label}")
    elif open_now:
        lines.append("Dashboard ไม่พบ Slot ที่ตรงกับเวลานี้ จึงยังยืนยันความว่างไม่ได้ครับ")
    lines.extend([
        f"อัปเดต: {refreshed} (ข้อมูลจองสดจาก WordPress{' ใช้ cache ระยะสั้น' if snapshot.cached else ''})",
        f"แหล่งข้อมูล: {BOOKING_SOURCE_URL}",
    ])
    return "\n".join(lines)
