from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.locale import contains_thai_prose  # noqa: E402


def _ask(base_url: str, index: int) -> dict[str, object]:
    english = index % 2 == 0
    question = "What games are available?" if english else "มีเกมอะไรบ้าง"
    payload = json.dumps({
        "question": question,
        "client_session_id": f"bilingual-concurrency-{index}",
        "locale": "auto",
        "recent_history": [],
        "debug": False,
        "experimental_allow_llm": False,
        "experimental_rag_fallback": False,
    }, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
        return {
            "index": index,
            "expected": "en" if english else "th",
            "status": response.status,
            "header": response.headers.get("Content-Language"),
            "effective": (data.get("language") or {}).get("effective"),
            "answer": str(data.get("answer") or ""),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check bilingual API isolation with concurrent sessions.")
    parser.add_argument("--url", default="http://127.0.0.1:8047")
    args = parser.parse_args()

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(lambda index: _ask(args.url, index), range(10)))

    for result in results:
        expected = str(result["expected"])
        assert result["status"] == 200, result
        assert result["header"] == expected, result
        assert result["effective"] == expected, result
        if expected == "en":
            assert not contains_thai_prose(str(result["answer"])), result
            assert "There are currently 42 verified games available." in str(result["answer"]), result
        else:
            assert contains_thai_prose(str(result["answer"])), result

    print("OK 10 concurrent bilingual API sessions with no locale leakage")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
