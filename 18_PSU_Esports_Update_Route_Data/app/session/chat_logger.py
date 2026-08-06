from __future__ import annotations

import json
import os
import sqlite3
import sys
import urllib.request
from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LOG_DIR = ROOT / "data" / "logs"
DEFAULT_SQLITE_PATH = DEFAULT_LOG_DIR / "chat_history.sqlite3"
MAX_WEBHOOK_BYTES = 64 * 1024
WEBHOOK_TIMEOUT_SEC = 2.0
POSTGRES_CONNECT_TIMEOUT_SEC = 2


def _plain(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _enabled(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() not in {"0", "false", "no", "off", ""}


def _local_log_dir() -> Path:
    override = os.getenv("PSU_CHAT_LOG_DIR", "").strip()
    return Path(override) if override else DEFAULT_LOG_DIR


def _sqlite_path() -> Path:
    override = os.getenv("PSU_CHAT_LOG_SQLITE_PATH", "").strip()
    return Path(override) if override else DEFAULT_SQLITE_PATH


def _postgres_url() -> str:
    for name in ("DATABASE_URL", "POSTGRES_URL", "POSTGRES_PRISMA_URL", "POSTGRES_URL_NON_POOLING"):
        value = os.getenv(name, "").strip()
        if value:
            return value
    return ""


def _write_local_jsonl(record: dict[str, Any]) -> None:
    log_dir = _local_log_dir()
    log_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(UTC).astimezone().strftime("%Y-%m-%d")
    log_path = log_dir / f"web_chat_{today}.jsonl"
    with log_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False, default=_plain) + "\n")


def _init_sqlite(conn: sqlite3.Connection) -> None:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS chat_sessions (
      session_id TEXT PRIMARY KEY,
      channel TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      last_route_category TEXT,
      last_route_intent TEXT,
      last_mode TEXT,
      message_count INTEGER NOT NULL DEFAULT 0
    )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS chat_messages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      session_id TEXT NOT NULL,
      role TEXT NOT NULL,
      content TEXT NOT NULL,
      resolved_question TEXT,
      route_category TEXT,
      route_intent TEXT,
      mode TEXT,
      confidence REAL,
      latency_sec REAL,
      sources_json TEXT,
      metadata_json TEXT,
      created_at TEXT NOT NULL
    )
    """)
    conn.execute("""
    CREATE INDEX IF NOT EXISTS idx_chat_messages_session_id
    ON chat_messages(session_id, id)
    """)


def _insert_sqlite_message(conn: sqlite3.Connection, record: dict[str, Any], role: str, content: str) -> None:
    conn.execute(
        """
        INSERT INTO chat_messages (
          session_id, role, content, resolved_question, route_category, route_intent,
          mode, confidence, latency_sec, sources_json, metadata_json, created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            str(record.get("client_session_id") or "anonymous").strip() or "anonymous",
            role,
            content,
            str(record.get("resolved_question") or ""),
            str(record.get("route_category") or ""),
            str(record.get("route_intent") or ""),
            str(record.get("mode") or ""),
            record.get("confidence") if isinstance(record.get("confidence"), (int, float)) else None,
            record.get("latency_sec") if isinstance(record.get("latency_sec"), (int, float)) else None,
            json.dumps(_plain(record.get("sources") or []), ensure_ascii=False),
            json.dumps(_plain({
                "schema_version": record.get("schema_version"),
                "context_resolution": record.get("context_resolution"),
                "query_debug": record.get("query_debug"),
                "decision_artifact": record.get("decision_artifact"),
                "recent_history_count": record.get("recent_history_count"),
                "experimental": record.get("experimental"),
                "validation_ok": record.get("validation_ok"),
                "error": record.get("error"),
                "wall_sec": record.get("wall_sec"),
            }), ensure_ascii=False),
            str(record.get("timestamp") or datetime.now(UTC).isoformat()),
        ),
    )


def _write_sqlite(record: dict[str, Any]) -> None:
    db_path = _sqlite_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    session_id = str(record.get("client_session_id") or "anonymous").strip() or "anonymous"
    timestamp = str(record.get("timestamp") or datetime.now(UTC).isoformat())
    conn = sqlite3.connect(db_path)
    try:
        _init_sqlite(conn)
        conn.execute(
            """
            INSERT INTO chat_sessions (
              session_id, channel, created_at, updated_at,
              last_route_category, last_route_intent, last_mode, message_count
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, 0)
            ON CONFLICT(session_id) DO UPDATE SET
              updated_at = excluded.updated_at,
              channel = excluded.channel,
              last_route_category = excluded.last_route_category,
              last_route_intent = excluded.last_route_intent,
              last_mode = excluded.last_mode
            """,
            (
                session_id,
                str(record.get("channel") or ""),
                timestamp,
                timestamp,
                str(record.get("route_category") or ""),
                str(record.get("route_intent") or ""),
                str(record.get("mode") or ""),
            ),
        )

        question = str(record.get("question") or "").strip()
        answer = str(record.get("answer") or "").strip()
        error = str(record.get("error") or "").strip()
        inserted = 0
        if question:
            _insert_sqlite_message(conn, record, "user", question)
            inserted += 1
        if answer:
            _insert_sqlite_message(conn, record, "assistant", answer)
            inserted += 1
        if error and not answer:
            _insert_sqlite_message(conn, record, "system", error)
            inserted += 1
        if inserted:
            conn.execute(
                "UPDATE chat_sessions SET message_count = message_count + ? WHERE session_id = ?",
                (inserted, session_id),
            )
        conn.commit()
    finally:
        conn.close()


def _postgres_connect(url: str):
    try:
        import psycopg  # type: ignore
    except ImportError as exc:  # pragma: no cover - depends on deploy env
        raise RuntimeError("psycopg is required for Postgres logging; install psycopg[binary]") from exc
    return psycopg.connect(url, autocommit=False, connect_timeout=POSTGRES_CONNECT_TIMEOUT_SEC)


def _init_postgres(conn: Any) -> None:
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS chat_sessions (
          session_id TEXT PRIMARY KEY,
          channel TEXT,
          created_at TIMESTAMPTZ NOT NULL,
          updated_at TIMESTAMPTZ NOT NULL,
          last_route_category TEXT,
          last_route_intent TEXT,
          last_mode TEXT,
          message_count INTEGER NOT NULL DEFAULT 0
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS chat_messages (
          id BIGSERIAL PRIMARY KEY,
          session_id TEXT NOT NULL REFERENCES chat_sessions(session_id) ON DELETE CASCADE,
          role TEXT NOT NULL,
          content TEXT NOT NULL,
          resolved_question TEXT,
          route_category TEXT,
          route_intent TEXT,
          mode TEXT,
          confidence DOUBLE PRECISION,
          latency_sec DOUBLE PRECISION,
          sources_json TEXT,
          metadata_json TEXT,
          created_at TIMESTAMPTZ NOT NULL
        )
        """)
        cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_chat_messages_session_id
        ON chat_messages(session_id, id)
        """)


def _insert_postgres_message(conn: Any, record: dict[str, Any], role: str, content: str) -> None:
    session_id = str(record.get("client_session_id") or "anonymous").strip() or "anonymous"
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO chat_messages (
              session_id, role, content, resolved_question, route_category, route_intent,
              mode, confidence, latency_sec, sources_json, metadata_json, created_at
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                session_id,
                role,
                content,
                str(record.get("resolved_question") or ""),
                str(record.get("route_category") or ""),
                str(record.get("route_intent") or ""),
                str(record.get("mode") or ""),
                record.get("confidence") if isinstance(record.get("confidence"), (int, float)) else None,
                record.get("latency_sec") if isinstance(record.get("latency_sec"), (int, float)) else None,
                json.dumps(_plain(record.get("sources") or []), ensure_ascii=False),
                json.dumps(_plain({
                    "schema_version": record.get("schema_version"),
                    "context_resolution": record.get("context_resolution"),
                    "query_debug": record.get("query_debug"),
                    "decision_artifact": record.get("decision_artifact"),
                    "recent_history_count": record.get("recent_history_count"),
                    "experimental": record.get("experimental"),
                    "validation_ok": record.get("validation_ok"),
                    "error": record.get("error"),
                    "wall_sec": record.get("wall_sec"),
                }), ensure_ascii=False),
                str(record.get("timestamp") or datetime.now(UTC).isoformat()),
            ),
        )


def _write_postgres(record: dict[str, Any]) -> None:
    url = _postgres_url()
    if not url:
        return

    session_id = str(record.get("client_session_id") or "anonymous").strip() or "anonymous"
    timestamp = str(record.get("timestamp") or datetime.now(UTC).isoformat())
    conn = _postgres_connect(url)
    try:
        _init_postgres(conn)
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO chat_sessions (
                  session_id, channel, created_at, updated_at,
                  last_route_category, last_route_intent, last_mode, message_count
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, 0)
                ON CONFLICT(session_id) DO UPDATE SET
                  updated_at = EXCLUDED.updated_at,
                  channel = EXCLUDED.channel,
                  last_route_category = EXCLUDED.last_route_category,
                  last_route_intent = EXCLUDED.last_route_intent,
                  last_mode = EXCLUDED.last_mode
                """,
                (
                    session_id,
                    str(record.get("channel") or ""),
                    timestamp,
                    timestamp,
                    str(record.get("route_category") or ""),
                    str(record.get("route_intent") or ""),
                    str(record.get("mode") or ""),
                ),
            )

        question = str(record.get("question") or "").strip()
        answer = str(record.get("answer") or "").strip()
        error = str(record.get("error") or "").strip()
        inserted = 0
        if question:
            _insert_postgres_message(conn, record, "user", question)
            inserted += 1
        if answer:
            _insert_postgres_message(conn, record, "assistant", answer)
            inserted += 1
        if error and not answer:
            _insert_postgres_message(conn, record, "system", error)
            inserted += 1
        if inserted:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE chat_sessions SET message_count = message_count + %s WHERE session_id = %s",
                    (inserted, session_id),
                )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def _write_stdout(record: dict[str, Any]) -> None:
    payload = {"event": "psu_chat_log", **record}
    print(json.dumps(payload, ensure_ascii=False, default=_plain), file=sys.stdout, flush=True)


def _post_webhook(record: dict[str, Any]) -> None:
    url = os.getenv("PSU_CHAT_LOG_WEBHOOK_URL", "").strip()
    if not url:
        return
    payload = json.dumps(record, ensure_ascii=False, default=_plain).encode("utf-8")
    if len(payload) > MAX_WEBHOOK_BYTES:
        trimmed = dict(record)
        answer = str(trimmed.get("answer") or "")
        trimmed["answer"] = answer[:2000] + ("..." if len(answer) > 2000 else "")
        payload = json.dumps(trimmed, ensure_ascii=False, default=_plain).encode("utf-8")

    headers = {"Content-Type": "application/json; charset=utf-8"}
    token = os.getenv("PSU_CHAT_LOG_WEBHOOK_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=WEBHOOK_TIMEOUT_SEC) as response:
        response.read(256)


def write_chat_log(record: dict[str, Any]) -> dict[str, Any]:
    """Write a chat log record to configured sinks.

    Local JSONL is useful for local development. stdout/webhook are better for
    serverless production where writing to the project filesystem is not durable.
    Logging failures are returned as metadata and must not break chat answers.
    """
    enriched = {
        "timestamp": datetime.now(UTC).isoformat(),
        "schema_version": 1,
        **record,
    }
    sinks: dict[str, Any] = {}

    if _enabled("PSU_CHAT_LOG_LOCAL_JSONL", default=True):
        try:
            _write_local_jsonl(enriched)
            sinks["local_jsonl"] = True
        except Exception as exc:  # pragma: no cover - defensive runtime guard
            sinks["local_jsonl_error"] = repr(exc)

    if _enabled("PSU_CHAT_LOG_SQLITE", default=True):
        try:
            _write_sqlite(enriched)
            sinks["sqlite"] = str(_sqlite_path())
        except Exception as exc:  # pragma: no cover
            sinks["sqlite_error"] = repr(exc)

    if _enabled("PSU_CHAT_LOG_POSTGRES", default=bool(_postgres_url())) and _postgres_url():
        try:
            _write_postgres(enriched)
            sinks["postgres"] = True
        except Exception as exc:  # pragma: no cover
            sinks["postgres_error"] = repr(exc)

    if _enabled("PSU_CHAT_LOG_STDOUT", default=False):
        try:
            _write_stdout(enriched)
            sinks["stdout"] = True
        except Exception as exc:  # pragma: no cover
            sinks["stdout_error"] = repr(exc)

    if os.getenv("PSU_CHAT_LOG_WEBHOOK_URL", "").strip():
        try:
            _post_webhook(enriched)
            sinks["webhook"] = True
        except Exception as exc:  # pragma: no cover
            sinks["webhook_error"] = repr(exc)

    return sinks
