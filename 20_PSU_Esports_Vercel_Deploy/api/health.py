from __future__ import annotations

from datetime import UTC, datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.after_request
def add_common_headers(response):
    response.headers["Cache-Control"] = "no-store"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/", methods=["GET"])
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "ok": True,
        "service": "psu-esports-chat-vercel",
        "runtime": "vercel-python-function",
        "time": datetime.now(UTC).isoformat(),
    })
