from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.preprocess import extract_entities, preprocess_input  # noqa: E402
from app.pipeline.router import route_intent  # noqa: E402
from app.pipeline.universal_intent import _heuristic_intent, _skip_llm_first_for_strong_route  # noqa: E402


def _decision(question: str) -> tuple[bool, str]:
    pre = preprocess_input(question)
    entities = extract_entities(pre)
    route, _trace = route_intent(pre, entities)
    heuristic = _heuristic_intent(pre.clean_query, route)
    return _skip_llm_first_for_strong_route(route, heuristic, pre.clean_query)


def _heuristic(question: str):
    pre = preprocess_input(question)
    entities = extract_entities(pre)
    route, _trace = route_intent(pre, entities)
    return route, _heuristic_intent(pre.clean_query, route)


def main() -> int:
    skip, reason = _decision("เกมตอนนี้มีเกมอะไรบ้าง")
    if skip or "broad" not in reason:
        raise AssertionError(f"broad game list should get LLM intent review, got skip={skip}, reason={reason}")

    skip, reason = _decision("คนดูแลศูนย์มีใครบ้าง")
    if skip or "broad" not in reason:
        raise AssertionError(f"broad member list should get LLM intent review, got skip={skip}, reason={reason}")

    skip, reason = _decision("ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท")
    if not skip:
        raise AssertionError(f"specific price calculation should skip LLM intent, got reason={reason}")

    route, heuristic = _heuristic("ROV รอบชิงเล่นกี่เกม")
    if heuristic.domain != "competition_rules" or heuristic.operation != "rule_lookup":
        raise AssertionError(
            "competition round question should stay in competition_rules/rule_lookup, "
            f"got route={route.category}/{route.intent}, intent={heuristic.domain}/{heuristic.operation}"
        )

    skip, reason = _decision("PS5 มีเกมอะไรบ้าง")
    if not skip or "clear platform game catalog" not in reason:
        raise AssertionError(f"clear platform game catalog should skip LLM intent, got skip={skip}, reason={reason}")

    skip, reason = _decision("สตาฟเล่นเกมอะไรบ้าง")
    if skip or "people_or_role" not in reason:
        raise AssertionError(f"people/game mixed signal should get LLM intent review, got skip={skip}, reason={reason}")

    print("ADAPTIVE INTENT GATE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
