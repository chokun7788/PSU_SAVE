from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.normalization import build_query_variants  # noqa: E402
from app.pipeline.router import route_intent  # noqa: E402
from app.pipeline.preprocess import extract_entities, preprocess_input  # noqa: E402


def main() -> int:
    variants = build_query_variants("helllo")
    assert "hello" in variants, variants
    assert "ราคา 202666 บาท" in build_query_variants("ราคา 202666 บาท")

    recovered = preprocess_input("helllo")
    routes = []
    for candidate in recovered.query_variants:
        candidate_pre = preprocess_input(candidate)
        route, _trace = route_intent(candidate_pre, extract_entities(candidate_pre))
        routes.append(route)
    assert any(route.intent == "chatbot_greeting" for route in routes), [route.intent for route in routes]
    print("OK repeated English letters add non-mutating routing variants without changing numbers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
