"""Compare public WordPress CSV bookings with the local dashboard, without saving customer data.

This is a point-in-time diagnostic, not a fixture for future booking availability.
The output contains aggregate counts, hashes, and any slot mismatches only.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

CSV_BASE = "https://esports.computing.psu.ac.th/wp-content/uploads/powerbi-exports/"
BANGKOK = timezone(timedelta(hours=7))
HOURS = (9, 10, 11, 12, 13, 14, 15)


def fetch_csv(name: str) -> tuple[list[dict[str, str]], dict[str, str]]:
    url = CSV_BASE + name + ".csv?" + urlencode({"_psu_live_ts": int(datetime.now().timestamp() * 1000)})
    request = Request(url, headers={
        "User-Agent": "Mozilla/5.0 PSU-Booking-CSV-Live-Dashboard/2.0",
        "Accept": "text/csv,text/plain,*/*",
        "Cache-Control": "no-cache, no-store, max-age=0",
        "Pragma": "no-cache",
    })
    with urlopen(request, timeout=15) as response:
        raw = response.read()
        last_modified = response.headers.get("Last-Modified", "")
    text = raw.decode("utf-8-sig", errors="replace")
    return list(csv.DictReader(io.StringIO(text))), {
        "sha256_text_16": hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()[:16],
        "bytes": len(raw),
        "last_modified": last_modified,
    }


def fetch_dashboard(date: str, path: str, base_url: str) -> dict:
    request = Request(f"{base_url.rstrip('/')}{path}?{urlencode({'date': date})}", headers={"Accept": "application/json"})
    with urlopen(request, timeout=15) as response:
        result = json.load(response)
    if not isinstance(result, dict) or not result.get("ok") or result.get("date") != date:
        raise ValueError(f"Dashboard did not return a valid status for {date}")
    return result


def appointment_intervals(rows: list[dict[str, str]], dates: set[str]) -> tuple[dict[tuple[str, str], list[tuple[datetime, datetime]]], dict]:
    intervals: dict[tuple[str, str], list[tuple[datetime, datetime]]] = defaultdict(list)
    statuses: Counter[str] = Counter()
    invalid_time = 0
    for row in rows:
        raw_start = str(row.get("time") or "")
        if not raw_start.isdigit() or int(raw_start) <= 1_000_000_000:
            invalid_time += 1
            continue
        start = datetime.fromtimestamp(int(raw_start), BANGKOK)
        date = start.date().isoformat()
        if date not in dates:
            continue
        status = str(row.get("status") or "").strip().lower()
        statuses[date + "/" + status] += 1
        if any(term in status for term in ("cancel", "trash", "deleted", "rejected", "failed")):
            continue
        raw_end = str(row.get("end") or "")
        if raw_end.isdigit() and int(raw_end) > 1_000_000_000:
            end = datetime.fromtimestamp(int(raw_end), BANGKOK)
        else:
            raw_duration = str(row.get("duration") or "60")
            duration = int(raw_duration) if raw_duration.isdigit() else 60
            end = start + timedelta(minutes=duration)
        if end <= start:
            raise ValueError("A source appointment has an end time before its start time")
        service_id = str(int(row["service_id"])) if str(row.get("service_id") or "").isdigit() else str(row.get("service_id") or "")
        intervals[(date, service_id)].append((start, end))
    return intervals, {"statuses_for_selected_dates": dict(sorted(statuses.items())), "invalid_time_rows_all_dates": invalid_time}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dates", required=True, help="Comma-separated YYYY-MM-DD dates")
    parser.add_argument("--dashboard-url", default="http://127.0.0.1:8091")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"Output exists: {args.output}")
    dates = [value.strip() for value in args.dates.split(",") if value.strip()]
    if not dates:
        parser.error("At least one date is required")
    for date in dates:
        datetime.strptime(date, "%Y-%m-%d")

    appointments, appointment_meta = fetch_csv("wbk_appointments")
    services, service_meta = fetch_csv("wbk_services")
    service_ids = {str(int(row["id"])) for row in services if str(row.get("id") or "").isdigit()}
    intervals, appointment_stats = appointment_intervals(appointments, set(dates))
    mismatches: list[dict] = []
    snapshot_summaries: list[dict] = []
    checked = 0
    booked_slots = 0
    free_slots = 0
    closed_slots = 0
    for date in dates:
        detailed = fetch_dashboard(date, "/api/status", args.dashboard_url)
        sanitized = fetch_dashboard(date, "/api/chatbot-status", args.dashboard_url)
        diagnostics = detailed.get("diagnostics") or {}
        source_matches = (
            detailed.get("source") == sanitized.get("source") == "remote_csv_live"
            and diagnostics.get("appointments_meta", {}).get("hash") == appointment_meta["sha256_text_16"]
            and diagnostics.get("services_meta", {}).get("hash") == service_meta["sha256_text_16"]
        )
        if not source_matches:
            raise RuntimeError(f"Source changed or dashboard used fallback while checking {date}; rerun the audit")
        resources = {str(row["resource_id"]): row for row in sanitized.get("resources") or []}
        if set(resources) != service_ids:
            raise RuntimeError(f"Dashboard service IDs differ from WordPress CSV for {date}")
        for service_id, resource in resources.items():
            slots = {(str(slot["start"]), str(slot["end"])): slot for slot in resource.get("slots") or []}
            for hour in HOURS:
                start_hm, end_hm = f"{hour:02d}:00", f"{hour+1:02d}:00"
                slot = slots.get((start_hm, end_hm))
                if slot is None:
                    mismatches.append({"date": date, "service_id": service_id, "slot": start_hm, "reason": "hourly slot missing"})
                    continue
                start = datetime.fromisoformat(date + "T" + start_hm).replace(tzinfo=BANGKOK)
                end = start + timedelta(hours=1)
                booked = sum(a < end and b > start for a, b in intervals.get((date, service_id), []))
                periods = sanitized["center"].get("open_periods") or []
                closed = not sanitized["center"]["open"] or not any(
                    start_hm >= str(period[0]) and end_hm <= str(period[1])
                    for period in periods
                )
                expected_booked = 0 if closed else booked
                expected_available = 0 if closed else max(0, 1 - booked)
                if closed:
                    closed_slots += 1
                elif booked:
                    booked_slots += 1
                else:
                    free_slots += 1
                checked += 1
                if int(slot["booked_count"]) != expected_booked or int(slot["available_count"]) != expected_available or (closed and slot["status"] != "closed"):
                    mismatches.append({
                        "date": date,
                        "service_id": service_id,
                        "slot": start_hm + "-" + end_hm,
                        "expected_booked": expected_booked,
                        "actual_booked": slot["booked_count"],
                        "expected_available": expected_available,
                        "actual_available": slot["available_count"],
                        "actual_status": slot["status"],
                    })
        snapshot_summaries.append({
            "date": date,
            "source": sanitized.get("source"),
            "generated_at": sanitized.get("generated_at"),
            "center_open": sanitized["center"]["open"],
            "resources": len(resources),
            "csv_hash_match": source_matches,
        })

    result = {
        "checked_at": datetime.now(BANGKOK).isoformat(timespec="seconds"),
        "source": "direct WordPress CSV versus local Booking Dashboard chatbot-status",
        "dates": dates,
        "appointment_rows": len(appointments),
        "service_rows": len(services),
        "appointment_csv": appointment_meta,
        "service_csv": service_meta,
        "appointment_stats": appointment_stats,
        "snapshots": snapshot_summaries,
        "checked_hourly_resource_slots": checked,
        "booked_slots": booked_slots,
        "free_slots": free_slots,
        "closed_slots": closed_slots,
        "mismatches": mismatches,
        "limitations": [
            "The CSV is the source of truth for this comparison; it does not prove WordPress staff-confirmed booking policy.",
            "Pending and no-show appointments are treated as occupying a slot; cancelled and rejected rows are ignored.",
            "Customer names, emails, phone numbers, appointment IDs and raw CSV rows are not saved.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("dates", "appointment_rows", "service_rows", "checked_hourly_resource_slots", "booked_slots", "free_slots", "closed_slots", "mismatches")}, ensure_ascii=False))
    return 0 if not mismatches else 1


if __name__ == "__main__":
    raise SystemExit(main())
