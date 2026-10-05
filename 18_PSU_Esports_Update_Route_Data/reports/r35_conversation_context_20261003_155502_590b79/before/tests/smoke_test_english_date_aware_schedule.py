from __future__ import annotations

import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.bilingual_english import _date_aware_schedule_text  # noqa: E402


def main() -> int:
    friday = _date_aware_schedule_text(date(2026, 9, 11), relative_label="Tomorrow")
    required = (
        "Tomorrow, Friday, 11/09/2026",
        "09:00-12:00 is open for play and booking",
        "13:00-16:00 is a maintenance period",
        "play and booking are unavailable",
        "System reference date:",
        "Thai calendar for this date:",
        "Regular schedule details:",
    )
    for value in required:
        if value not in friday:
            raise AssertionError(f"missing date-aware English schedule detail: {value}\n{friday}")
    print("ENGLISH DATE-AWARE SCHEDULE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
