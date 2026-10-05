"""Test the package API; live-down results are not fixture truth assertions."""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tests.test_reliability_flow_20261001 import CASES


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Refusing to overwrite evidence")
    with urlopen(args.base_url + "/health", timeout=10) as response:
        health = json.loads(response.read().decode("utf-8"))
    print("health", json.dumps(health, ensure_ascii=False)[:700], flush=True)
    cases = [case for case in CASES if not case[-1]]
    cases.extend((
        ("api-live-down-en", "en", "Is Cockpit availble at 14:00 on 2026-09-30", "schedule",
         (("cannot confirm",),), ("1/2", "Cockpit #1: available"), False),
        ("api-live-down-th", "th", "Cockpit ว่งไหม ตอนนี้", "schedule",
         (("ยังยืนยันสถานะ",),), ("1/2", "Cockpit #1: ว่าง"), False),
    ))
    results = []
    with args.output.open("x", encoding="utf-8") as stream:
        for index, (case_id, locale, question, route, groups, forbidden, _) in enumerate(cases, 1):
            started = time.perf_counter()
            request = Request(args.base_url + "/api/chat", method="POST", headers={"Content-Type": "application/json"},
                              data=json.dumps({"question": question, "locale": locale,
                                               "client_session_id": f"r20-test-{index}", "debug": index % 2 == 0}).encode("utf-8"))
            with urlopen(request, timeout=30) as response:
                status, result = response.status, json.loads(response.read().decode("utf-8"))
            answer = str(result.get("answer") or "")
            passed = status == 200 and result.get("route_category") == route and all(
                any(term.casefold() in answer.casefold() for term in group) for group in groups
            ) and not any(term.casefold() in answer.casefold() for term in forbidden)
            row = {"id": case_id, "question": question, "locale": locale, "http_status": status,
                   "route": result.get("route_category"), "mode": result.get("mode"), "answer": answer,
                   "wall_sec": round(time.perf_counter() - started, 3), "passed": passed,
                   "truth_level": "static candidate contract or safe live unavailable; no real booking truth"}
            results.append(row)
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.flush()
            print(f"{index}/{len(cases)} {case_id} {passed}", flush=True)
    with args.output.with_suffix(".health.json").open("x", encoding="utf-8") as stream:
        json.dump(health, stream, ensure_ascii=False, indent=2)
    return 0 if all(row["passed"] for row in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
