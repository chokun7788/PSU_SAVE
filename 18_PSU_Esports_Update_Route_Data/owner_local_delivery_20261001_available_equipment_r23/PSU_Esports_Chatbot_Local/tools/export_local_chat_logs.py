from __future__ import annotations

import argparse
import html
import json
import sqlite3
from pathlib import Path


def text(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def parse_json(value: object, fallback: object) -> object:
    try:
        return json.loads(str(value or ""))
    except (TypeError, ValueError):
        return fallback


def render_report(database: Path, output: Path, session_limit: int, message_limit: int) -> int:
    if not database.exists():
        raise SystemExit(f"Chat database not found: {database}")

    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    try:
        session_query = """
            SELECT session_id, session_number, channel, created_at, updated_at,
                   last_route_category, last_route_intent, last_mode, message_count
            FROM chat_sessions
            ORDER BY session_number DESC, updated_at DESC
        """
        sessions = connection.execute(
            session_query if session_limit <= 0 else f"{session_query} LIMIT ?",
            () if session_limit <= 0 else (session_limit,),
        ).fetchall()
    except sqlite3.OperationalError as exc:
        raise SystemExit(f"Chat database has not been initialized yet: {exc}") from exc

    blocks: list[str] = []
    for session in sessions:
        message_query = """
            SELECT id, role, content, route_category, route_intent, mode, confidence,
                   latency_sec, sources_json, metadata_json, created_at
            FROM chat_messages
            WHERE session_id = ?
            ORDER BY id DESC
        """
        messages = connection.execute(
            message_query if message_limit <= 0 else f"{message_query} LIMIT ?",
            (session["session_id"],) if message_limit <= 0 else (session["session_id"], message_limit),
        ).fetchall()
        rows: list[str] = []
        for message in reversed(messages):
            sources = parse_json(message["sources_json"], [])
            metadata = parse_json(message["metadata_json"], {})
            language = metadata.get("language", {}) if isinstance(metadata, dict) else {}
            language_label = language.get("effective", "") if isinstance(language, dict) else ""
            source_links = " ".join(
                f'<a href="{text(item.get("url", ""))}" target="_blank" rel="noreferrer">{text(item.get("id") or item.get("url") or "source")}</a>'
                for item in sources if isinstance(item, dict) and item.get("url")
            )
            details = " | ".join(filter(None, [
                str(message["created_at"] or ""),
                f"message_id={message['id']}",
                str(message["mode"] or ""),
                "/".join(filter(None, [str(message["route_category"] or ""), str(message["route_intent"] or "")])),
                f'{float(message["latency_sec"]):.2f}s' if message["latency_sec"] is not None else "",
                language_label,
                f"request={metadata.get('request_id', '')}" if isinstance(metadata, dict) and metadata.get("request_id") else "",
                f"exchange={metadata.get('exchange_id', '')}" if isinstance(metadata, dict) and metadata.get("exchange_id") else "",
            ]))
            rows.append(
                "<article class='message'>"
                f"<div class='role'>{text(message['role'])}</div>"
                f"<div class='content'>{text(message['content'])}</div>"
                f"<div class='details'>{text(details)}</div>"
                + (f"<div class='sources'>Sources: {source_links}</div>" if source_links else "")
                + "</article>"
            )
        blocks.append(
            "<section class='session'>"
            f"<h2>Session #{text(session['session_number'] or '?')}: <code>{text(session['session_id'])}</code></h2>"
            f"<p>Created: {text(session['created_at'])} | Updated: {text(session['updated_at'])} | Stored messages: {text(session['message_count'])}</p>"
            + "".join(rows)
            + "</section>"
        )
    report = """<!doctype html>
<html lang="th"><head><meta charset="utf-8"><title>PSU Esports Chat Log Report</title>
<style>
body{font-family:Arial,'TH Sarabun New',sans-serif;background:#f4f7fb;color:#17233b;margin:0;padding:32px;line-height:1.45}
header,.session{max-width:1040px;margin:0 auto 20px;background:#fff;border:1px solid #d5dfeb;border-radius:8px;padding:22px}
h1,h2{margin:0 0 10px}h1{color:#0d4f91}.session h2{font-size:18px}.session p,.details{color:#52637a;font-size:13px}.message{border-top:1px solid #e5ebf3;padding:12px 0}.role{font-weight:700;text-transform:uppercase;font-size:12px;color:#2368ad}.content{white-space:pre-wrap;margin:4px 0}.sources{font-size:12px;margin-top:6px}a{color:#075ea8}code{word-break:break-all}
</style></head><body><header><h1>PSU Esports Chat Log Report</h1><p>Local-only report. Treat this file as confidential because it contains user-entered chat messages.</p></header>""" + "".join(blocks) + "</body></html>"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"Created report: {output}")
    print(f"Sessions included: {len(sessions)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Export the local PSU Esports chatbot transcript to HTML.")
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--session-limit", type=int, default=0, help="0 means every stored session")
    parser.add_argument("--message-limit", type=int, default=0, help="0 means every stored message per session")
    args = parser.parse_args()
    return render_report(args.database, args.output, args.session_limit, args.message_limit)


if __name__ == "__main__":
    raise SystemExit(main())
