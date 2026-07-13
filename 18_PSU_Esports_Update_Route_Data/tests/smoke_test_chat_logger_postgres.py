from __future__ import annotations

import os
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main() -> int:
    os.environ["DATABASE_URL"] = "postgresql://user:pass@example.invalid/db"
    os.environ["PSU_CHAT_LOG_POSTGRES"] = "1"
    os.environ["PSU_CHAT_LOG_SQLITE"] = "0"
    os.environ["PSU_CHAT_LOG_LOCAL_JSONL"] = "0"

    from app.session import chat_logger

    calls: list[dict] = []

    def fake_write_postgres(record: dict) -> None:
        calls.append(record)

    original = chat_logger._write_postgres
    chat_logger._write_postgres = fake_write_postgres
    try:
        sinks = chat_logger.write_chat_log({
            "channel": "web",
            "client_session_id": "neon-test-session",
            "question": "PS5 มีเกมอะไรบ้าง",
            "resolved_question": "PS5 มีเกมอะไรบ้าง",
            "answer": "PlayStation 5 Zone มีเกม...",
            "mode": "equipment_game_catalog_fast_path",
            "route_category": "equipment",
            "route_intent": "equipment_game_catalog",
            "confidence": 0.96,
        })
    finally:
        chat_logger._write_postgres = original

    if sinks.get("postgres") is not True:
        raise AssertionError(f"postgres sink not marked successful: {sinks}")
    if len(calls) != 1:
        raise AssertionError(f"postgres sink was not called exactly once: {calls}")
    if calls[0].get("client_session_id") != "neon-test-session":
        raise AssertionError(f"unexpected logged record: {calls[0]}")

    print("CHAT LOGGER POSTGRES SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
