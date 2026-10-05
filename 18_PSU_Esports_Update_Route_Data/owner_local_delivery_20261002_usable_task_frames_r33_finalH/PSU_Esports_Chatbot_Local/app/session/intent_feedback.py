from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from app.core.normalization import normalize_text


ROOT = Path(__file__).resolve().parents[2]
FEEDBACK_DIR = ROOT / "data" / "logs"
ALLOWED_OUTCOMES = frozenset({"confirmed", "corrected", "unclear"})


def write_intent_feedback(payload: dict[str, Any]) -> dict[str, object]:
    """Persist a privacy-safe routing feedback record for later evaluation.

    Raw questions, answers, session IDs, contact data, booking data, and free
    text are intentionally excluded. A one-way normalized-text fingerprint lets
    evaluators group recurring patterns without reconstructing user content.
    """
    outcome = str(payload.get("outcome") or "").strip().lower()
    if outcome not in ALLOWED_OUTCOMES:
        raise ValueError("outcome must be confirmed, corrected, or unclear")
    expected_category = str(payload.get("expected_category") or "").strip()
    expected_intent = str(payload.get("expected_intent") or "").strip()
    if outcome == "corrected" and (not expected_category or not expected_intent):
        raise ValueError("corrected feedback requires expected_category and expected_intent")

    raw_question = str(payload.get("question") or "")
    fingerprint = hashlib.sha256(normalize_text(raw_question).encode("utf-8")).hexdigest()[:20]
    record = {
        "schema_version": 1,
        "timestamp": datetime.now(UTC).isoformat(),
        "outcome": outcome,
        "request_id": str(payload.get("request_id") or "").strip()[:80],
        "input_fingerprint": fingerprint,
        "observed_category": str(payload.get("observed_category") or "").strip()[:80],
        "observed_intent": str(payload.get("observed_intent") or "").strip()[:80],
        "expected_category": expected_category[:80],
        "expected_intent": expected_intent[:80],
        "locale": str(payload.get("locale") or "").strip()[:8],
        "input_recovery": payload.get("input_recovery") if isinstance(payload.get("input_recovery"), dict) else {},
    }
    FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
    path = FEEDBACK_DIR / f"intent_feedback_{datetime.now(UTC).strftime('%Y-%m-%d')}.jsonl"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return {"ok": True, "stored": True, "feedback_id": record["input_fingerprint"]}
