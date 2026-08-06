from __future__ import annotations

import sys
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.calculator.service_fee import answer_service_fee  # noqa: E402
from app.core.source_registry import (  # noqa: E402
    PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,
    SERVICE_FEE_IMAGE_2026_ID,
)
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def source_ids_from_hits(hits: list[dict[str, Any]]) -> list[str]:
    ids: list[str] = []
    for hit in hits:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        source_ids = metadata.get("source_ids")
        values = source_ids if isinstance(source_ids, list) else [hit.get("id")]
        for value in values:
            text = str(value or "")
            if text and text not in ids:
                ids.append(text)
    return ids


def assert_has(ids: list[str], expected: str, label: str) -> None:
    if expected not in ids:
        raise AssertionError(f"{label}: missing source id {expected}; got {ids}")


def assert_not_has(ids: list[str], forbidden: str, label: str) -> None:
    if forbidden in ids:
        raise AssertionError(f"{label}: forbidden source id {forbidden}; got {ids}")


def main() -> int:
    pc_calc = answer_service_fee("ราคา PC ต่อชั่วโมงเท่าไหร่")
    assert pc_calc.get("matched")
    assert_has(list(pc_calc.get("source_ids") or []), SERVICE_FEE_IMAGE_2026_ID, "pc calculator")
    assert_has(list(pc_calc.get("source_ids") or []), PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID, "pc calculator")
    print("OK calculator PC source ids")

    ps5_calc = answer_service_fee("ราคา PS5 ต่อชั่วโมงเท่าไหร่")
    assert ps5_calc.get("matched")
    assert_has(list(ps5_calc.get("source_ids") or []), SERVICE_FEE_IMAGE_2026_ID, "ps5 calculator")
    assert_not_has(list(ps5_calc.get("source_ids") or []), PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID, "ps5 calculator")
    print("OK calculator PS5 source ids")

    pc_result = answer_question_pipeline_debug(
        "ราคา PC ต่อชั่วโมงเท่าไหร่",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    pc_ids = source_ids_from_hits(pc_result.hits)
    assert_has(pc_ids, SERVICE_FEE_IMAGE_2026_ID, "pc pipeline")
    assert_has(pc_ids, PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID, "pc pipeline")
    assert any(
        str(hit.get("metadata", {}).get("source_url", "")) == "local://service_fee/pc_price_update_20260727"
        for hit in pc_result.hits
    ), pc_result.hits
    print("OK pipeline PC source ids")

    ps5_result = answer_question_pipeline_debug(
        "ราคา PS5 ต่อชั่วโมงเท่าไหร่",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    ps5_ids = source_ids_from_hits(ps5_result.hits)
    assert_has(ps5_ids, SERVICE_FEE_IMAGE_2026_ID, "ps5 pipeline")
    assert_not_has(ps5_ids, PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID, "ps5 pipeline")
    print("OK pipeline PS5 source ids")

    tekken_price = answer_question_pipeline_debug(
        "Tekken 8 ราคาเท่าไหร่",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    tekken_ids = source_ids_from_hits(tekken_price.hits)
    assert_has(tekken_ids, SERVICE_FEE_IMAGE_2026_ID, "tekken price")
    assert_has(tekken_ids, PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID, "tekken price")
    assert any("TEKKEN 8" in str(source_id) or "tekken" in str(source_id).lower() for source_id in tekken_ids)
    print("OK game price source ids")

    print("SOURCE CONTRACT SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
