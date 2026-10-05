"""Check requested targets through the HTTP API of a separate candidate package."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from urllib.request import Request, urlopen

CASES = (
    ("th", "จอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร", "equipment", ("Sofa 2 seats",), ("TV 86 นิ้ว:",)),
    ("th", "ตำแหน่ง รอวประธาน คือใร", "overview", ("นายนพัทธ์ ฝอยทอง", "รองประธาน"), ("นายษุภากรณ์",)),
    ("th", "ตำแหน่ง ประธาน ึือใคร", "overview", ("นายษุภากรณ์",), ("นายนพัทธ์",)),
    ("th", "ตำแหน่ง ผู้ช่วยประธาน คือใคร", "clarification", ("ยังยืนยันตำแหน่ง",), ("นายษุภากรณ์", "นายนพัทธ์")),
    ("th", "คนทำแชทบอทคือใคร", "overview", ("นายภาสวุฒิ ชูติประชากิจ",), ("ผมคือ PSU Esports Assistant",)),
    ("th", "จอ PC เป็นรุ่นอะไร", "equipment", ("Gaming Monitor",), ("Gaming PC:",)),
    ("en", "What is Sofa 2 seats", "equipment", ("Sofa 2 seats",), ("TV 86",)),
    ("en", "Who are you", "knowledge", ("PSU Esports",), ("AI Chat Bot Developer",)),
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Refusing to overwrite existing evidence")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    failures = 0
    with args.output.open("x", encoding="utf-8") as stream:
        for index, (locale, question, route, required, forbidden) in enumerate(CASES, 1):
            request = Request(
                args.base_url.rstrip("/") + "/api/chat",
                data=json.dumps({"question": question, "locale": locale, "debug": True}).encode("utf-8"),
                headers={"Content-Type": "application/json"}, method="POST",
            )
            started = time.perf_counter()
            with urlopen(request, timeout=30) as response:
                status, result = response.status, json.loads(response.read().decode("utf-8"))
            answer = str(result.get("answer") or "")
            passed = status == 200 and result.get("route_category") == route and all(
                text.casefold() in answer.casefold() for text in required
            ) and not any(text.casefold() in answer.casefold() for text in forbidden)
            failures += not passed
            record = {
                "case": index, "question": question, "locale": locale,
                "expected_route": route, "required": required, "forbidden": forbidden,
                "http_status": status, "route": result.get("route_category"),
                "mode": result.get("mode"), "answer": answer,
                "wall_sec": round(time.perf_counter() - started, 3), "passed": passed,
            }
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            stream.flush()
            print(f"{index}/{len(CASES)} passed={passed} route={record['route']}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
