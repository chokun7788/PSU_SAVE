from __future__ import annotations

import os
import json
import sqlite3
import sys
import tempfile
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        db_path = Path(tmp) / "chat_history.sqlite3"
        os.environ["PSU_CHAT_LOG_SQLITE"] = "1"
        os.environ["PSU_CHAT_LOG_SQLITE_PATH"] = str(db_path)
        os.environ["PSU_CHAT_LOG_LOCAL_JSONL"] = "0"

        from app.session.chat_logger import write_chat_log

        sinks = write_chat_log({
            "channel": "web",
            "client_session_id": "test-session-1",
            "question": "Mario Kart Live คืออะไร",
            "resolved_question": "Mario Kart Live คืออะไร",
            "answer": "Mario Kart Live: Home Circuit คือเกมแข่งรถ",
            "mode": "test_mode",
            "route_category": "games",
            "route_intent": "game_detail",
            "confidence": 0.91,
            "latency_sec": 0.12,
            "sources": [{"id": "our_games", "url": "local://test"}],
            "query_debug": {
                "original_question": "เกมทนิฟยอดนิยมมีอะไรบ้าง",
                "resolved_question": "เกมทนิฟยอดนิยมมีอะไรบ้าง",
                "normalized_query": "เกมทนิฟยอดนิยมมีอะไรบ้าง เกมmobaยอดนิยมมีอะไรบ้าง",
                "query_variants": ["เกมทนิฟยอดนิยมมีอะไรบ้าง", "เกมmobaยอดนิยมมีอะไรบ้าง"],
                "active_query": "เกมmobaยอดนิยมมีอะไรบ้าง",
                "active_query_changed": True,
            },
        })
        if "sqlite" not in sinks:
            raise AssertionError(f"sqlite sink not enabled: {sinks}")

        conn = sqlite3.connect(db_path)
        try:
            session = conn.execute(
                "SELECT session_id, message_count, last_route_category FROM chat_sessions WHERE session_id = ?",
                ("test-session-1",),
            ).fetchone()
            if session != ("test-session-1", 2, "games"):
                raise AssertionError(f"unexpected session row: {session}")

            rows = conn.execute(
                "SELECT role, content FROM chat_messages WHERE session_id = ? ORDER BY id",
                ("test-session-1",),
            ).fetchall()
            if rows != [
                ("user", "Mario Kart Live คืออะไร"),
                ("assistant", "Mario Kart Live: Home Circuit คือเกมแข่งรถ"),
            ]:
                raise AssertionError(f"unexpected message rows: {rows}")
            metadata_json = conn.execute(
                "SELECT metadata_json FROM chat_messages WHERE session_id = ? AND role = ? ORDER BY id LIMIT 1",
                ("test-session-1", "user"),
            ).fetchone()[0]
            metadata = json.loads(metadata_json)
            if not metadata.get("query_debug", {}).get("active_query_changed"):
                raise AssertionError(f"query_debug not persisted: {metadata}")
        finally:
            conn.close()

    print("CHAT LOGGER SQLITE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
