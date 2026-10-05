"""Fetch booking exports on demand; return only the existing slot aggregates."""
from __future__ import annotations

import csv
import io
import time
from datetime import date
from typing import Any
from urllib.error import HTTPError, URLError


class BookingFetchError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


def _csv_rows(text: str, kind: str) -> list[dict[str, str]]:
    # Reject an HTML/login/error response or a truncated schema before it
    # could be interpreted as an empty appointment list and false vacancy.
    required = {"service_id", "day", "time", "duration", "status"} if kind == "appointments" else {"id", "name", "duration"}
    allowed = required | {"end", "quantity"} if kind == "appointments" else required
    reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff")), strict=True)
    fields = [str(field).strip().lower() for field in reader.fieldnames or []]
    if not required.issubset(fields) or len(fields) != len(set(fields)):
        raise BookingFetchError("invalid_export", f"{kind} export has an invalid CSV schema")
    rows: list[dict[str, str]] = []
    try:
        for raw in reader:
            if None in raw or any(value is None for value in raw.values()):
                raise BookingFetchError("invalid_export", f"{kind} export contains a malformed CSV row")
            # Personal names, tokens, email, telephone and appointment IDs
            # stay outside the status calculator and pipeline.
            clean = {str(key).strip().lower(): str(value).strip() for key, value in raw.items() if str(key).strip().lower() in allowed}
            if any(clean.values()):
                rows.append(clean)
    except csv.Error as exc:
        raise BookingFetchError("invalid_export", f"{kind} export is not valid CSV") from exc
    if kind == "services" and (not rows or any(not row["id"] or not row["name"] for row in rows)):
        raise BookingFetchError("invalid_export", "services export has no valid resources")
    return rows


def fetch_wordpress_status(selected_date: str, timeout_seconds: float) -> dict[str, Any]:
    """Use the Dashboard's source URLs, recorded calendar and slot calculator.

    No web server or sample fallback is started. Both exports must succeed
    within one shared network budget; no raw export is written to disk.
    """
    from booking_dashboard import server as dashboard

    if date.fromisoformat(selected_date).isoformat() != selected_date:
        raise BookingFetchError("invalid_date", "booking date must be YYYY-MM-DD")
    # load_center_schedule otherwise creates a default file when missing.
    # An absent or corrupt owner calendar must never be guessed or rewritten.
    import json

    try:
        schedule = json.loads(dashboard.CENTER_SCHEDULE_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise BookingFetchError("calendar_unavailable", "recorded booking calendar is unavailable") from exc
    if not isinstance(schedule, dict) or not isinstance(schedule.get("weekly"), dict):
        raise BookingFetchError("calendar_unavailable", "recorded booking calendar is invalid")

    deadline = time.monotonic() + timeout_seconds
    exports: dict[str, list[dict[str, str]]] = {}
    diag: dict[str, Any] = {"mode": "remote_csv_live", "fetch_policy": "on_demand_wordpress_no_sample"}
    for kind, url in (("appointments", dashboard.APPOINTMENTS_CSV_URL), ("services", dashboard.SERVICES_CSV_URL)):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise BookingFetchError("timeout", "live booking fetch exceeded its network budget")
        try:
            text, meta = dashboard.read_url(url, timeout=remaining)
        except HTTPError as exc:
            raise BookingFetchError("upstream_unavailable", f"WordPress {kind} export returned HTTP {exc.code}") from exc
        except (OSError, URLError, TimeoutError) as exc:
            reason = getattr(exc, "reason", exc)
            code = "network_permission" if getattr(reason, "winerror", None) == 10013 else "timeout" if isinstance(reason, TimeoutError) else "upstream_unavailable"
            raise BookingFetchError(code, f"WordPress {kind} export could not be fetched") from exc
        exports[kind] = _csv_rows(text, kind)
        diag[f"{kind}_meta"] = meta
    status = dashboard.build_status(exports["appointments"], exports["services"], selected_date, diag)
    return dashboard.chatbot_status_payload(status)
