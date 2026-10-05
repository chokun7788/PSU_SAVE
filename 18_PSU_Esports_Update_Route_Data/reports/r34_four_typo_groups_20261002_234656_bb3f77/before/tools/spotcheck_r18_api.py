"""HTTP spot checks for a separately launched candidate package."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from urllib.request import Request, urlopen


CASES = (
    ("th", "PUBG: BATTLEGROUNDS ราคเท่าไฟร่"),
    ("th", "PS5 ราคาเท่าไหร่ แล้วมีเกมะไรบ้าง"),
    ("th", "ช่วง 14:00-15:00 Cockpit Zone เครื่องไหนว่าบง้าง"),
    ("en", "What does the Tab buttno do in VALORANT on PC"),
    ("en", "What is the studio policy for teporary suspension"),
    ("en", "Is Cockpit Zone availble at 14:00-15:00?"),
    ("en", "How do you pay Moving Out 2"),
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"output exists: {args.output}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        for index, (locale, question) in enumerate(CASES, 1):
            body = json.dumps({"question": question, "locale": locale, "debug": True}).encode("utf-8")
            request = Request(
                args.base_url.rstrip("/") + "/api/chat", data=body,
                headers={"Content-Type": "application/json"}, method="POST",
            )
            started = time.perf_counter()
            with urlopen(request, timeout=30) as response:
                status_code = response.status
                result = json.loads(response.read().decode("utf-8"))
            record = {
                "case": index, "locale": locale, "question": question,
                "http_status": status_code, "wall_sec": round(time.perf_counter() - started, 3),
                "route_category": result.get("route_category"),
                "route_intent": result.get("route_intent"),
                "mode": result.get("mode"),
                "answer": result.get("answer"),
                "ok": result.get("ok"),
                "runtime": result.get("runtime"),
            }
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            stream.flush()
            print(f"{index}/{len(CASES)} {status_code} {record['route_category']} {record['mode']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
