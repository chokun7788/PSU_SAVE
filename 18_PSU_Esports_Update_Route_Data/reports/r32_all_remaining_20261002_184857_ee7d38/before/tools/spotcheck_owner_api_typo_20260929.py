"""Small live-API spot check against the running r15 owner package."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports/bilingual_typo_2000_20260929"
OUTPUT = REPORT_DIR / "api_spotcheck_owner_r15.jsonl"
IDS = (
    "MASTER-GT-TH-00890", "MASTER-GT-TH-00085", "MASTER-GT-TH-04867",
    "MASTER-GT-EN-03895", "MASTER-GT-EN-02806", "MASTER-GT-EN-02255",
)


def main() -> int:
    if OUTPUT.exists():
        raise SystemExit(f"Output already exists: {OUTPUT}")
    rows = {}
    for locale in ("th", "en"):
        path = REPORT_DIR / f"paired_{locale}_r15.jsonl"
        for line in path.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            if row["id"] in IDS:
                rows[row["id"]] = row
    if set(rows) != set(IDS):
        raise SystemExit(f"Missing selected IDs: {set(IDS) - set(rows)}")

    with OUTPUT.open("x", encoding="utf-8") as stream:
        for case_id in IDS:
            row = rows[case_id]
            for variant in ("clean", "noisy"):
                question = row[f"{variant}_question"]
                payload = json.dumps({
                    "question": question, "locale": row["locale"], "debug": True,
                    "recent_history": [], "experimental_rag_fallback": False,
                    "client_session_id": f"typo-eval-{uuid.uuid4()}",
                }, ensure_ascii=False).encode("utf-8")
                request = urllib.request.Request(
                    "http://127.0.0.1:8095/api/chat", data=payload,
                    headers={"Content-Type": "application/json; charset=utf-8"}, method="POST",
                )
                try:
                    with urllib.request.urlopen(request, timeout=30) as response:
                        data = json.loads(response.read().decode("utf-8"))
                        http_status = response.status
                except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                    data = {"error": f"{type(exc).__name__}: {exc}"}
                    http_status = getattr(exc, "code", None)
                result = {
                    "id": case_id, "variant": variant, "locale": row["locale"],
                    "question": question, "http_status": http_status,
                    "ok": data.get("ok"), "route_category": data.get("route_category"),
                    "route_intent": data.get("route_intent"), "mode": data.get("mode"),
                    "answer": data.get("answer", ""), "latency_sec": data.get("latency_sec"),
                    "error": data.get("error", ""),
                }
                stream.write(json.dumps(result, ensure_ascii=False) + "\n")
                stream.flush()
                print(case_id, variant, http_status, result["route_category"], result["mode"], flush=True)
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
