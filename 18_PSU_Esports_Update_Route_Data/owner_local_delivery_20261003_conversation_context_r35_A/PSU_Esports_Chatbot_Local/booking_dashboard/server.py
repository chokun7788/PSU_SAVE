#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PSU Booking CSV Auto Refresh Dashboard

Run this file, then open http://127.0.0.1:8080/
The frontend polls /api/status every REFRESH_SECONDS.
Each API call fetches the remote CSV URLs again with no-cache headers and a cache-buster query string.
When the CSV export changes, the next poll returns the new status.

No external Python packages required.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import socket
import sys
import threading
import time
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime, time as dtime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PSU_BOOKING_PORT", "8080"))
TIMEZONE_NAME = "Asia/Bangkok"
os.environ["TZ"] = TIMEZONE_NAME
if hasattr(time, "tzset"):
    time.tzset()

# ใช้เวลาไทยแบบ fix UTC+7 โดยตรง เพื่อไม่ให้ Windows/เครื่องผู้ใช้แปลง timezone ผิด
# Thailand ไม่มี DST จึงใช้ fixed offset ได้ปลอดภัยกว่า datetime.fromtimestamp() เฉย ๆ
THAI_TZ = timezone(timedelta(hours=7), name="ICT")

def now_bangkok() -> datetime:
    return datetime.now(THAI_TZ).replace(tzinfo=None)

def thai_from_timestamp(seconds: int) -> datetime:
    return datetime.fromtimestamp(int(seconds), THAI_TZ).replace(tzinfo=None)

# CSV URLs from the existing PowerBI export plugin.
APPOINTMENTS_CSV_URL = "https://esports.computing.psu.ac.th/wp-content/uploads/powerbi-exports/wbk_appointments.csv"
SERVICES_CSV_URL = "https://esports.computing.psu.ac.th/wp-content/uploads/powerbi-exports/wbk_services.csv"

# The dashboard refreshes automatically. Every poll asks the server to read CSV again.
REFRESH_SECONDS = int(os.environ.get("PSU_REFRESH_SECONDS", "10"))
REMOTE_TIMEOUT_SECONDS = int(os.environ.get("PSU_REMOTE_TIMEOUT", "8"))

# Opening period for timeline view. Change this if the studio hours differ.
OPEN_CLOSE_PERIODS = [("09:00", "16:00")]
SLOT_MINUTES = 60

SAMPLE_APPOINTMENTS = ROOT / "sample_data" / "wbk_appointments.csv"
SAMPLE_SERVICES = ROOT / "sample_data" / "wbk_services.csv"
CENTER_SCHEDULE_FILE = ROOT / "center_schedule.json"
ADMIN_PIN = os.environ.get("PSU_ADMIN_PIN", "1234")



def default_center_schedule() -> Dict[str, Any]:
    return {
        "mode": "weekly_auto",
        "default_hours": {"start": "09:00", "end": "16:00"},
        "weekly": {
            "0": {"open": True, "open_periods": [["12:00", "16:00"]], "reason": "Maintenance ช่วงเช้า 09:00-12:00"},
            "1": {"open": True, "open_periods": [["09:00", "16:00"]], "reason": ""},
            "2": {"open": True, "open_periods": [["09:00", "16:00"]], "reason": ""},
            "3": {"open": True, "open_periods": [["09:00", "16:00"]], "reason": ""},
            "4": {"open": True, "open_periods": [["09:00", "13:00"]], "reason": "Maintenance ช่วงบ่าย 13:00-16:00"},
            "5": {"open": False, "open_periods": [], "reason": "ปิดให้บริการวันเสาร์"},
            "6": {"open": False, "open_periods": [], "reason": "ปิดให้บริการวันอาทิตย์"},
        },
        "dates": {},
    }


def load_center_schedule() -> Dict[str, Any]:
    base = default_center_schedule()
    if not CENTER_SCHEDULE_FILE.exists():
        save_center_schedule(base)
        return base
    try:
        data = json.loads(CENTER_SCHEDULE_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            if isinstance(data.get("default_hours"), dict):
                base["default_hours"].update(data["default_hours"])
            if isinstance(data.get("weekly"), dict):
                for key, value in data["weekly"].items():
                    if key in base["weekly"] and isinstance(value, dict):
                        base["weekly"][key].update(value)
            if isinstance(data.get("dates"), dict):
                base["dates"] = data["dates"]
    except Exception:
        pass
    return base


def save_center_schedule(data: Dict[str, Any]) -> Dict[str, Any]:
    base = default_center_schedule()
    incoming = data or {}
    if isinstance(incoming.get("default_hours"), dict):
        base["default_hours"].update(incoming["default_hours"])
    if isinstance(incoming.get("weekly"), dict):
        for key, value in incoming["weekly"].items():
            if key in base["weekly"] and isinstance(value, dict):
                base["weekly"][key].update(value)
    if isinstance(incoming.get("dates"), dict):
        base["dates"] = incoming["dates"]
    tmp = CENTER_SCHEDULE_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(base, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(CENTER_SCHEDULE_FILE)
    return base


def normalize_hm(value: Any, fallback: str) -> str:
    s = str(value or "").strip()
    m = re.match(r"^(\d{1,2}):(\d{2})$", s)
    if not m:
        return fallback
    h, mi = int(m.group(1)), int(m.group(2))
    if 0 <= h <= 23 and 0 <= mi <= 59:
        return f"{h:02d}:{mi:02d}"
    return fallback


def normalize_periods(periods: Any) -> List[List[str]]:
    cleaned: List[List[str]] = []
    if not isinstance(periods, list):
        return cleaned
    for period in periods:
        if isinstance(period, dict):
            st, en = period.get("start"), period.get("end")
        elif isinstance(period, (list, tuple)) and len(period) >= 2:
            st, en = period[0], period[1]
        else:
            continue
        st = normalize_hm(st, "")
        en = normalize_hm(en, "")
        ps = parse_time_seconds(st)
        pe = parse_time_seconds(en)
        if st and en and ps is not None and pe is not None and pe > ps:
            cleaned.append([st, en])
    return cleaned


def exclude_lunch_break(periods: List[List[str]]) -> List[List[str]]:
    """Keep owner opening bounds while excluding the confirmed 12:00-13:00 booking break."""
    bookable: List[List[str]] = []
    for start, end in periods:
        if start < "12:00":
            morning_end = min(end, "12:00")
            if start < morning_end:
                bookable.append([start, morning_end])
        if end > "13:00":
            afternoon_start = max(start, "13:00")
            if afternoon_start < end:
                bookable.append([afternoon_start, end])
    return bookable


def weekday_key_from_date(selected_date: str) -> str:
    try:
        return str(datetime.strptime(selected_date, "%Y-%m-%d").weekday())
    except Exception:
        return str(now_bangkok().weekday())


def center_status_for_date(selected_date: str) -> Dict[str, Any]:
    schedule = load_center_schedule()
    dates = schedule.get("dates") or {}
    if selected_date in dates and isinstance(dates[selected_date], dict):
        cfg = dates[selected_date]
        is_open = bool(cfg.get("open", False))
        periods = normalize_periods(cfg.get("open_periods"))
        if is_open and not periods:
            hours = cfg.get("hours") if isinstance(cfg.get("hours"), dict) else schedule.get("default_hours", {})
            periods = normalize_periods([[hours.get("start", "09:00"), hours.get("end", "16:00")]])
        periods = exclude_lunch_break(periods)
        return {
            "date": selected_date,
            "open": is_open and bool(periods),
            "reason": clean_text(cfg.get("reason", "")),
            "hours": {"start": periods[0][0] if periods else "09:00", "end": periods[-1][1] if periods else "16:00"},
            "open_periods": periods,
            "source": "date_override",
            "weekday": weekday_key_from_date(selected_date),
            "schedule": schedule,
        }

    wk = weekday_key_from_date(selected_date)
    cfg = (schedule.get("weekly") or {}).get(wk, {})
    is_open = bool(cfg.get("open", False))
    periods = exclude_lunch_break(normalize_periods(cfg.get("open_periods")))
    return {
        "date": selected_date,
        "open": is_open and bool(periods),
        "reason": clean_text(cfg.get("reason", "")),
        "hours": {"start": periods[0][0] if periods else "09:00", "end": periods[-1][1] if periods else "16:00"},
        "open_periods": periods,
        "source": "weekly_auto",
        "weekday": wk,
        "schedule": schedule,
    }


def with_cache_buster(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    q.append(("_psu_live_ts", str(int(time.time() * 1000))))
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(q)))


def sha_short(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()[:16]


def read_url(url: str, timeout: int = REMOTE_TIMEOUT_SECONDS) -> Tuple[str, Dict[str, Any]]:
    final_url = with_cache_buster(url)
    req = urllib.request.Request(
        final_url,
        headers={
            "User-Agent": "Mozilla/5.0 PSU-Booking-CSV-Live-Dashboard/2.0",
            "Accept": "text/csv,text/plain,*/*",
            "Cache-Control": "no-cache, no-store, max-age=0",
            "Pragma": "no-cache",
        },
    )
    started = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
        headers = dict(resp.headers.items())
        status = getattr(resp, "status", 200)
        resolved_url = resp.geturl()
    elapsed_ms = int((time.time() - started) * 1000)
    text = raw.decode("utf-8-sig", errors="replace")
    meta = {
        "status": status,
        "bytes": len(raw),
        "elapsed_ms": elapsed_ms,
        "last_modified": headers.get("Last-Modified", ""),
        "etag": headers.get("ETag", ""),
        "content_type": headers.get("Content-Type", ""),
        "resolved_url": resolved_url,
        "hash": sha_short(text),
    }
    return text, meta


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def fetch_csv_pair(force_sample: bool = False) -> Tuple[str, str, Dict[str, Any]]:
    diag: Dict[str, Any] = {
        "appointments_url": APPOINTMENTS_CSV_URL,
        "services_url": SERVICES_CSV_URL,
        "fetch_policy": "fresh_on_every_api_call_with_cache_buster",
        "refresh_seconds": REFRESH_SECONDS,
    }

    if force_sample:
        appt = read_file(SAMPLE_APPOINTMENTS)
        svc = read_file(SAMPLE_SERVICES)
        diag.update({
            "mode": "sample_forced",
            "appointments_fetch": "sample_forced",
            "services_fetch": "sample_forced",
            "appointments_meta": {"hash": sha_short(appt)},
            "services_meta": {"hash": sha_short(svc)},
        })
        return appt, svc, diag

    remote_ok = True
    try:
        appt, appt_meta = read_url(APPOINTMENTS_CSV_URL)
        diag["appointments_fetch"] = "remote_ok"
        diag["appointments_meta"] = appt_meta
    except Exception as exc:  # noqa: BLE001
        remote_ok = False
        appt = read_file(SAMPLE_APPOINTMENTS)
        diag["appointments_fetch"] = "sample_fallback"
        diag["appointments_error"] = f"{type(exc).__name__}: {exc}"
        diag["appointments_meta"] = {"hash": sha_short(appt)}

    try:
        svc, svc_meta = read_url(SERVICES_CSV_URL)
        diag["services_fetch"] = "remote_ok"
        diag["services_meta"] = svc_meta
    except Exception as exc:  # noqa: BLE001
        remote_ok = False
        svc = read_file(SAMPLE_SERVICES)
        diag["services_fetch"] = "sample_fallback"
        diag["services_error"] = f"{type(exc).__name__}: {exc}"
        diag["services_meta"] = {"hash": sha_short(svc)}

    diag["mode"] = "remote_csv_live" if remote_ok else "sample_fallback"
    return appt, svc, diag


def parse_csv(text: str) -> List[Dict[str, str]]:
    text = text.lstrip("\ufeff")
    if not text.strip():
        return []
    reader = csv.DictReader(io.StringIO(text))
    rows: List[Dict[str, str]] = []
    for row in reader:
        clean: Dict[str, str] = {}
        for k, v in row.items():
            if k is None:
                continue
            clean[str(k).strip()] = "" if v is None else str(v).strip()
        if any(str(v).strip() for v in clean.values()):
            rows.append(clean)
    return rows


def key_map(row: Dict[str, Any]) -> Dict[str, str]:
    return {str(k).lower().strip(): str(k) for k in row.keys()}


def get_val(row: Dict[str, Any], candidates: List[str], default: str = "") -> str:
    km = key_map(row)
    for cand in candidates:
        k = km.get(cand.lower())
        if k is not None:
            return str(row.get(k, default)).strip()
    return default


def clean_text(value: Any) -> str:
    s = re.sub(r"<[^>]*>", " ", str(value or ""))
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def normalize_duration(value: Any, fallback: int = 60) -> int:
    s = str(value or "").strip()
    if not s:
        return fallback
    m = re.search(r"\d+", s)
    try:
        n = int(m.group(0) if m else s)
    except Exception:  # noqa: BLE001
        return fallback
    if n <= 0:
        return fallback
    if n > 1440 and n % 60 == 0:  # sometimes seconds instead of minutes
        n = n // 60
    return max(1, n)


def parse_time_seconds(value: Any) -> Optional[int]:
    s = str(value or "").strip()
    if not s:
        return None
    if re.fullmatch(r"\d+", s):
        n = int(s)
        if 0 <= n <= 86400:
            return n
    m = re.match(r"^(\d{1,2}):(\d{2})(?::(\d{2}))?$", s)
    if m:
        h, mi, sec = int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)
        if 0 <= h < 24 and 0 <= mi < 60 and 0 <= sec < 60:
            return h * 3600 + mi * 60 + sec
    m = re.match(r"^([01]?\d|2[0-3])([0-5]\d)$", s)
    if m:
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60
    return None


def parse_date_any(value: Any) -> Optional[datetime]:
    s = str(value or "").strip()
    if not s:
        return None
    if re.fullmatch(r"\d+", s):
        n = int(s)
        if n > 1_000_000_000:  # Unix seconds
            return thai_from_timestamp(n)
        if 19000101 <= n <= 30000101:  # YYYYMMDD
            try:
                return datetime.strptime(s, "%Y%m%d")
            except ValueError:
                pass
    for fmt in (
        "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d",
        "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M", "%d/%m/%Y",
        "%m/%d/%Y %H:%M:%S", "%m/%d/%Y %H:%M", "%m/%d/%Y",
    ):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00").replace(" ", "T")).replace(tzinfo=None)
    except Exception:  # noqa: BLE001
        return None


def parse_booking_start(row: Dict[str, Any]) -> Optional[datetime]:
    """
    ใช้ schema จริงของ CSV:
    id,name,service_id,day,time,...,quantity,duration,created_on,...,end,...

    สำคัญ:
    - day = วันที่ของการจอง เช่น 1788454800 = 2026-09-04 00:00
    - time = เวลาเริ่มจองจริง เช่น 1788494400 = 2026-09-04 11:00
    - created_on = เวลาที่กดสร้างรายการ ไม่ใช่เวลาเริ่มใช้งาน
    - end = เวลาจบ ถ้ามี แต่ start หลักต้องมาจาก column time
    """
    day_value = get_val(row, ["day", "date", "appointment_date", "booking_date", "start_date"])
    time_value = get_val(row, ["time", "start_time", "appointment_time", "booking_time"])

    # Priority 1: column time คือเวลาเริ่มจองจริง
    if time_value:
        tv = str(time_value).strip()

        # Webba Booking usually stores "time" as Unix timestamp in seconds.
        if re.fullmatch(r"\d+", tv):
            n = int(tv)

            # Full Unix timestamp, e.g. 1788494400
            if n > 1_000_000_000:
                return thai_from_timestamp(n)

            # Seconds from midnight, e.g. 32400 = 09:00
            if 0 <= n <= 86400 and day_value:
                base = parse_date_any(day_value)
                if base:
                    return datetime.combine(base.date(), dtime(0, 0)) + timedelta(seconds=n)

        # HH:MM or HH:MM:SS, combine with day
        seconds = parse_time_seconds(tv)
        if seconds is not None and day_value:
            base = parse_date_any(day_value)
            if base:
                return datetime.combine(base.date(), dtime(0, 0)) + timedelta(seconds=seconds)

        # Full datetime string in time column
        parsed = parse_date_any(tv)
        if parsed:
            return parsed

    # Fallback เท่านั้น: ถ้าไม่มี time จริง ๆ ค่อยลอง datetime/start column อื่น
    dt = get_val(row, [
        "start_datetime", "start_date_time", "datetime", "date_time",
        "appointment_datetime", "appointment_date_time", "booking_datetime",
        "booking_date_time", "start", "starts_at",
    ])
    if dt:
        parsed = parse_date_any(dt)
        if parsed:
            return parsed

    return None

def is_cancelled(row: Dict[str, Any]) -> bool:
    status = get_val(row, ["status", "appointment_status", "booking_status", "payment_status"]).lower()
    return any(x in status for x in ["cancel", "canceled", "cancelled", "trash", "deleted", "rejected", "failed"])


def is_no_show(row: Dict[str, Any]) -> bool:
    """No Show = slot remains locked / not bookable."""
    status = get_val(row, ["status", "appointment_status", "booking_status", "payment_status"]).lower().strip()
    normalized = re.sub(r"[\s_-]+", "", status)
    return "noshow" in normalized


def service_id_from_booking(row: Dict[str, Any]) -> Optional[str]:
    v = get_val(row, ["service_id", "service", "serviceid", "wbk_service_id", "appointment_service_id", "service_ids"])
    if not v:
        return None
    m = re.search(r"\d+", v)
    return str(int(m.group(0))) if m else v.strip()


def hm(dt: datetime) -> str:
    return dt.strftime("%H:%M")


def iso_local(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def period_for_service(name: str) -> List[Tuple[str, str]]:
    # Show a full-day timeline for every equipment category.
    # Bookings outside this period are added as exact slots below.
    return OPEN_CLOSE_PERIODS


def build_status(appointments_rows: List[Dict[str, str]], services_rows: List[Dict[str, str]], selected_date: str, diag: Dict[str, Any]) -> Dict[str, Any]:
    if not selected_date:
        selected_date = now_bangkok().strftime("%Y-%m-%d")
    try:
        day = datetime.strptime(selected_date, "%Y-%m-%d").date()
    except ValueError:
        day = now_bangkok().date()
        selected_date = day.strftime("%Y-%m-%d")

    now = now_bangkok()
    day_start = datetime.combine(day, dtime(0, 0))
    day_end = datetime.combine(day, dtime(23, 59, 59))
    center_status = center_status_for_date(selected_date)
    open_periods = [tuple(p) for p in center_status.get("open_periods", [])] or [(center_status["hours"]["start"], center_status["hours"]["end"])]

    services: Dict[str, Dict[str, Any]] = {}
    for i, row in enumerate(services_rows):
        raw_id = get_val(row, ["id", "ID", "service_id"], str(i + 1)) or str(i + 1)
        m = re.search(r"\d+", str(raw_id))
        sid = str(int(m.group(0))) if m else str(raw_id).strip()
        name = clean_text(get_val(row, ["name", "service_name", "title"], f"Service {sid}"))
        duration = normalize_duration(get_val(row, ["duration", "length", "minutes"], "60"), SLOT_MINUTES)
        desc = clean_text(get_val(row, ["description", "desc", "games_list"], ""))
        services[sid] = {
            "id": sid,
            "name": name,
            "description": desc,
            "duration_minutes": duration,
            "capacity": 1,
            "booked_now": 0,
            "available_now": 1,
            "status": "available",
            "current_bookings": [],
            "next_booking": None,
            "today_bookings": [],
            "slots": [],
        }

    if not center_status["open"]:
        for svc in services.values():
            svc["booked_now"] = 0
            svc["available_now"] = 0
            svc["status"] = "closed"
            svc["current_bookings"] = []
            svc["next_booking"] = None
            svc["today_bookings"] = []
            t = parse_time_seconds("09:00") or 0
            pe = parse_time_seconds("16:00") or (16 * 3600)
            while t < pe:
                slot_start = day_start + timedelta(seconds=t)
                slot_end = min(day_start + timedelta(seconds=t + SLOT_MINUTES * 60), day_start + timedelta(seconds=pe))
                svc["slots"].append({
                    "start": hm(slot_start),
                    "end": hm(slot_end),
                    "booked_count": 0,
                    "no_show_count": 0,
                    "available_count": 0,
                    "status": "closed",
                    "closed_reason": center_status.get("reason") or "ปิดให้บริการ",
                })
                t += SLOT_MINUTES * 60
            svc["slots"].sort(key=lambda x: (x["start"], x["end"]))

        services_list = sorted(services.values(), key=lambda x: x["name"])
        appt_hash = diag.get("appointments_meta", {}).get("hash", "")
        svc_hash = diag.get("services_meta", {}).get("hash", "")
        combined_hash = sha_short(appt_hash + ":" + svc_hash + ":closed:" + selected_date)
        summary = {
            "total_services": len(services_list),
            "available_services": 0,
            "busy_services": 0,
            "closed_services": len(services_list),
            "today_bookings": 0,
            "no_show_bookings": 0,
            "total_units": sum(int(s["capacity"]) for s in services_list),
            "available_units": 0,
        }
        diag.update({
            "appointment_rows": len(appointments_rows),
            "service_rows": len(services_rows),
            "appointment_columns": list(appointments_rows[0].keys()) if appointments_rows else [],
            "service_columns": list(services_rows[0].keys()) if services_rows else [],
            "combined_csv_hash": combined_hash,
            "computed_at": iso_local(now_bangkok()),
            "center_calendar_logic": "closed day => all 09:00-16:00 slots are gray closed/not bookable",
        })
        return {
            "ok": True,
            "date": selected_date,
            "now": iso_local(now),
            "generated_at": iso_local(now_bangkok()),
            "refresh_seconds": REFRESH_SECONDS,
            "source": diag.get("mode", "unknown"),
            "services": services_list,
            "summary": summary,
            "diagnostics": diag,
            "center": center_status,
        }

    ignored = 0
    unmatched = 0
    today_count = 0

    for row in appointments_rows:
        if is_cancelled(row):
            ignored += 1
            continue
        sid = service_id_from_booking(row)
        if not sid or sid not in services:
            unmatched += 1
            continue
        start = parse_booking_start(row)
        if not start:
            ignored += 1
            continue
        duration = normalize_duration(
            get_val(row, ["duration", "appointment_duration", "booking_duration", "length"], ""),
            int(services[sid]["duration_minutes"]),
        )

        # ใช้ column end เป็นเวลาจบถ้ามีจริง แต่ start ยังล็อกที่ column time เท่านั้น
        end_value = get_val(row, ["end", "end_time", "ends_at", "appointment_end", "booking_end"])
        end = None
        if end_value:
            ev = str(end_value).strip()
            if re.fullmatch(r"\d+", ev):
                n = int(ev)
                if n > 1_000_000_000:
                    end = thai_from_timestamp(n)
                elif 0 <= n <= 86400:
                    day_base = get_val(row, ["day", "date", "appointment_date", "booking_date", "start_date"])
                    base = parse_date_any(day_base)
                    if base:
                        end = datetime.combine(base.date(), dtime(0, 0)) + timedelta(seconds=n)
            if end is None:
                parsed_end = parse_date_any(ev)
                if parsed_end:
                    end = parsed_end

        if end is None or end <= start:
            end = start + timedelta(minutes=duration)
        if end < day_start or start > day_end:
            continue

        today_count += 1
        status_value = get_val(row, ["status", "appointment_status", "booking_status"], "")
        no_show_value = is_no_show(row)
        item = {
            "id": get_val(row, ["id", "ID", "appointment_id"], ""),
            "start": hm(start),
            "end": hm(end),
            "start_full": iso_local(start),
            "end_full": iso_local(end),
            "status": status_value,
            "status_key": "no_show" if no_show_value else str(status_value).lower().strip(),
            "is_no_show": no_show_value,
            "customer": get_val(row, ["name", "customer", "customer_name", "email"], ""),
        }
        services[sid]["today_bookings"].append(item)
        if start <= now < end:
            services[sid]["booked_now"] += 1
            services[sid]["current_bookings"].append(item)
        if start > now:
            nb = services[sid]["next_booking"]
            if nb is None or start < datetime.strptime(nb["start_full"], "%Y-%m-%d %H:%M:%S"):
                services[sid]["next_booking"] = item

    for svc in services.values():
        svc["today_bookings"].sort(key=lambda x: x["start_full"])
        svc["available_now"] = max(0, int(svc["capacity"]) - int(svc["booked_now"]))
        svc["status"] = "busy" if svc["available_now"] <= 0 else ("partial" if svc["booked_now"] > 0 else "available")

        def slot_is_open(slot_start: datetime, slot_end: datetime) -> bool:
            for start_s, end_s in open_periods:
                ps = parse_time_seconds(start_s)
                pe = parse_time_seconds(end_s)
                if ps is None or pe is None:
                    continue
                os = day_start + timedelta(seconds=ps)
                oe = day_start + timedelta(seconds=pe)
                if slot_start >= os and slot_end <= oe:
                    return True
            return False

        def slot_is_open(slot_start: datetime, slot_end: datetime) -> bool:
            for start_s, end_s in open_periods:
                ps = parse_time_seconds(start_s)
                pe = parse_time_seconds(end_s)
                if ps is None or pe is None:
                    continue
                os = day_start + timedelta(seconds=ps)
                oe = day_start + timedelta(seconds=pe)
                if slot_start >= os and slot_end <= oe:
                    return True
            return False

        def add_slot(slot_start: datetime, slot_end: datetime) -> None:
            if slot_end <= slot_start:
                return
            key = (hm(slot_start), hm(slot_end))
            for existing in svc["slots"]:
                if existing["start"] == key[0] and existing["end"] == key[1]:
                    return

            if not slot_is_open(slot_start, slot_end):
                svc["slots"].append({
                    "start": hm(slot_start),
                    "end": hm(slot_end),
                    "booked_count": 0,
                    "no_show_count": 0,
                    "available_count": 0,
                    "status": "closed",
                    "closed_reason": center_status.get("reason") or "ปิด Maintenance",
                })
                return

            booked = 0
            no_show = 0
            for bk in svc["today_bookings"]:
                bs = datetime.strptime(bk["start_full"], "%Y-%m-%d %H:%M:%S")
                be = datetime.strptime(bk["end_full"], "%Y-%m-%d %H:%M:%S")
                if bs < slot_end and be > slot_start:
                    booked += 1
                    if bk.get("is_no_show"):
                        no_show += 1

            avail = max(0, int(svc["capacity"]) - booked)
            slot_status = "busy" if avail <= 0 else ("partial" if booked > 0 else "available")
            if slot_end <= now and booked == 0:
                slot_status = "past"

            svc["slots"].append({
                "start": hm(slot_start),
                "end": hm(slot_end),
                "booked_count": booked,
                "no_show_count": no_show,
                "available_count": avail,
                "status": "no_show" if no_show > 0 and avail <= 0 else slot_status,
            })

        t = parse_time_seconds("09:00") or 0
        pe = parse_time_seconds("16:00") or (16 * 3600)
        while t < pe:
            slot_start = day_start + timedelta(seconds=t)
            slot_end = min(day_start + timedelta(seconds=t + SLOT_MINUTES * 60), day_start + timedelta(seconds=pe))
            add_slot(slot_start, slot_end)
            t += SLOT_MINUTES * 60
        svc["slots"].sort(key=lambda x: (x["start"], x["end"]))

    services_list = sorted(services.values(), key=lambda x: x["name"])
    summary = {
        "total_services": len(services_list),
        "available_services": sum(1 for s in services_list if s["available_now"] > 0),
        "busy_services": sum(1 for s in services_list if s["available_now"] <= 0),
        "today_bookings": today_count,
        "no_show_bookings": sum(1 for s in services_list for b in s.get("today_bookings", []) if b.get("is_no_show")),
        "total_units": sum(int(s["capacity"]) for s in services_list),
        "available_units": sum(int(s["available_now"]) for s in services_list),
    }

    appt_hash = diag.get("appointments_meta", {}).get("hash", "")
    svc_hash = diag.get("services_meta", {}).get("hash", "")
    combined_hash = sha_short(appt_hash + ":" + svc_hash)
    diag.update({
        "appointment_rows": len(appointments_rows),
        "service_rows": len(services_rows),
        "appointment_columns": list(appointments_rows[0].keys()) if appointments_rows else [],
        "service_columns": list(services_rows[0].keys()) if services_rows else [],
        "ignored_rows": ignored,
        "unmatched_service_rows": unmatched,
        "combined_csv_hash": combined_hash,
        "computed_at": iso_local(now_bangkok()),
        "no_show_logic": "no show/no-show/noshow is not bookable; cancel/cancelled/canceled is free",
        "time_logic": "start = CSV column time, date = CSV column day, end = CSV column end if valid else time + duration",
        "timezone_logic": "all Unix timestamps are converted using fixed Bangkok time UTC+7, not the computer local timezone",
        "center_calendar_logic": "if center is closed for selected date, all slots become gray closed/not bookable",
    })

    return {
        "ok": True,
        "date": selected_date,
        "now": iso_local(now),
        "generated_at": iso_local(now_bangkok()),
        "refresh_seconds": REFRESH_SECONDS,
        "source": diag.get("mode", "unknown"),
        "csv_hash": combined_hash,
        "appointments_hash": appt_hash,
        "services_hash": svc_hash,
        "center": {k: v for k, v in center_status.items() if k != "schedule"},
        "summary": summary,
        "services": services_list,
        "diagnostics": diag,
    }


def send_json(handler: BaseHTTPRequestHandler, data: Dict[str, Any], status: int = 200) -> None:
    body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
    handler.send_header("Pragma", "no-cache")
    handler.send_header("Expires", "0")
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def chatbot_status_payload(status: Dict[str, Any]) -> Dict[str, Any]:
    """Return a read-only aggregate view suitable for a public chatbot.

    ``/api/status`` powers the owner dashboard and intentionally includes
    appointment detail.  A chatbot must never receive a customer name, email,
    phone number, appointment id, or booking token.  This projection keeps
    only resource and slot aggregates.
    """
    resources: List[Dict[str, Any]] = []
    for service in status.get("services") or []:
        if not isinstance(service, dict):
            continue
        slots: List[Dict[str, Any]] = []
        for slot in service.get("slots") or []:
            if not isinstance(slot, dict):
                continue
            slots.append({
                "start": str(slot.get("start") or ""),
                "end": str(slot.get("end") or ""),
                "status": str(slot.get("status") or "unknown"),
                "booked_count": int(slot.get("booked_count") or 0),
                "no_show_count": int(slot.get("no_show_count") or 0),
                "available_count": int(slot.get("available_count") or 0),
            })
        resources.append({
            "resource_id": str(service.get("id") or ""),
            "resource_name": str(service.get("name") or ""),
            "capacity": int(service.get("capacity") or 0),
            "status": str(service.get("status") or "unknown"),
            "available_now": int(service.get("available_now") or 0),
            "slots": slots,
        })
    return {
        "ok": bool(status.get("ok")),
        "date": str(status.get("date") or ""),
        "now": str(status.get("now") or ""),
        "generated_at": str(status.get("generated_at") or ""),
        "source": str(status.get("source") or "unknown"),
        "center": status.get("center") if isinstance(status.get("center"), dict) else {},
        "resources": resources,
        "privacy": "aggregate_only",
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "PSUBookingCSVAutoRefresh/2.0"

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stdout.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))


    def do_POST(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        if path not in ("/api/center-schedule", "/api/center-schedule/"):
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0") or "0")
            raw = self.rfile.read(min(length, 200_000)).decode("utf-8")
            payload = json.loads(raw or "{}")
            if str(payload.get("pin", "")) != str(ADMIN_PIN):
                send_json(self, {"ok": False, "error": "PIN ไม่ถูกต้อง"}, status=403)
                return
            schedule = payload.get("schedule")
            if not isinstance(schedule, dict):
                send_json(self, {"ok": False, "error": "schedule ต้องเป็น object"}, status=400)
                return
            saved = save_center_schedule(schedule)
            send_json(self, {"ok": True, "schedule": saved})
        except Exception as exc:  # noqa: BLE001
            send_json(self, {"ok": False, "error": f"{type(exc).__name__}: {exc}", "hint": "ใช้ v14: แก้ runtime ของ weekly calendar แล้ว"}, status=500)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path == "/health":
            send_json(self, {"ok": True, "service": "psu-booking-dashboard", "calendar_contract": "lunch-closed-v1"})
            return

        if path in ("/api/center-schedule", "/api/center-schedule/"):
            send_json(self, {"ok": True, "schedule": load_center_schedule(), "admin_pin_hint": "default 1234; set PSU_ADMIN_PIN before hosting"})
            return

        if path in ("/api/chatbot-status", "/api/chatbot-status/"):
            selected_date = query.get("date", [now_bangkok().strftime("%Y-%m-%d")])[0]
            try:
                appt_text, services_text, diag = fetch_csv_pair(force_sample=False)
                status = build_status(parse_csv(appt_text), parse_csv(services_text), selected_date, diag)
                send_json(self, chatbot_status_payload(status))
            except Exception as exc:  # noqa: BLE001
                send_json(self, {"ok": False, "error": f"{type(exc).__name__}: {exc}"}, status=500)
            return

        if path in ("/api/status", "/api/status/"):
            selected_date = query.get("date", [now_bangkok().strftime("%Y-%m-%d")])[0]
            force_sample = query.get("sample", ["0"])[0] == "1"
            try:
                appt_text, services_text, diag = fetch_csv_pair(force_sample=force_sample)
                data = build_status(parse_csv(appt_text), parse_csv(services_text), selected_date, diag)
                send_json(self, data)
            except Exception as exc:  # noqa: BLE001
                send_json(self, {"ok": False, "error": f"{type(exc).__name__}: {exc}", "hint": "ใช้ v14: แก้ runtime ของ weekly calendar แล้ว"}, status=500)
            return

        if path in ("/api/raw-check", "/api/raw-check/"):
            try:
                appt_text, svc_text, diag = fetch_csv_pair(force_sample=False)
                send_json(self, {
                    "ok": True,
                    "mode": diag.get("mode"),
                    "appointments_first_300_chars": appt_text[:300],
                    "services_first_300_chars": svc_text[:300],
                    "diagnostics": diag,
                })
            except Exception as exc:  # noqa: BLE001
                send_json(self, {"ok": False, "error": f"{type(exc).__name__}: {exc}", "hint": "ใช้ v14: แก้ runtime ของ weekly calendar แล้ว"}, status=500)
            return

        file_path = ROOT / "index.html" if path == "/" else (ROOT / path.lstrip("/")).resolve()
        if not str(file_path).startswith(str(ROOT.resolve())):
            self.send_error(403)
            return
        if not file_path.exists() or not file_path.is_file():
            self.send_error(404)
            return

        ctype = "text/plain; charset=utf-8"
        if file_path.suffix == ".html":
            ctype = "text/html; charset=utf-8"
        elif file_path.suffix == ".css":
            ctype = "text/css; charset=utf-8"
        elif file_path.suffix == ".js":
            ctype = "application/javascript; charset=utf-8"
        elif file_path.suffix == ".csv":
            ctype = "text/csv; charset=utf-8"
        elif file_path.suffix == ".json":
            ctype = "application/json; charset=utf-8"

        body = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def find_free_port(preferred: int) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("127.0.0.1", preferred))
            return preferred
        except OSError:
            pass
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PSU Booking CSV Auto Refresh Dashboard")
    parser.add_argument("--no-browser", action="store_true", help="do not open browser automatically")
    parser.add_argument("--host", default="127.0.0.1", help="host to bind, default 127.0.0.1")
    parser.add_argument("--port", type=int, default=PORT, help="preferred port, default 8080")
    args = parser.parse_args()

    port = find_free_port(args.port)
    url = f"http://{args.host}:{port}/"
    httpd = ThreadingHTTPServer((args.host, port), Handler)
    print("=" * 76)
    print("PSU Booking CSV Auto Refresh Dashboard is running")
    print(url)
    print(f"Frontend polls /api/status every {REFRESH_SECONDS} seconds")
    print("Every API call fetches the CSV again with no-cache + cache-buster")
    print("Press Ctrl+C to stop")
    print("=" * 76)
    if not args.no_browser:
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    httpd.serve_forever()


if __name__ == "__main__":
    main()
