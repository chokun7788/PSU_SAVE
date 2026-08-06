from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.entity_resolver import resolve_game_entity  # noqa: E402


def _with_env(name: str, value: str):
    previous = os.environ.get(name)
    os.environ[name] = value
    return previous


def _restore_env(name: str, previous: str | None) -> None:
    if previous is None:
        os.environ.pop(name, None)
    else:
        os.environ[name] = previous


def test_reranker_disabled_by_default_path() -> None:
    previous = _with_env("PSU_ENTITY_RERANKER", "0")
    try:
        resolution = resolve_game_entity("Modern Warfare III ปุ่มอะไร", operation="controls")
    finally:
        _restore_env("PSU_ENTITY_RERANKER", previous)

    reranker = resolution.metadata.get("reranker", {})
    assert reranker.get("action") == "skipped", resolution.as_dict()
    assert reranker.get("reason") == "disabled", resolution.as_dict()


def test_reranker_skips_generic_family_question() -> None:
    previous = _with_env("PSU_ENTITY_RERANKER", "1")
    try:
        resolution = resolve_game_entity("Mario เล่นยังไง", operation="gameplay")
    finally:
        _restore_env("PSU_ENTITY_RERANKER", previous)

    reranker = resolution.metadata.get("reranker", {})
    assert resolution.status == "ambiguous", resolution.as_dict()
    assert reranker.get("action") == "skipped", resolution.as_dict()
    assert reranker.get("reason") == "generic_family_query", resolution.as_dict()


def test_reranker_skips_high_confidence_exact_game() -> None:
    previous = _with_env("PSU_ENTITY_RERANKER", "1")
    try:
        resolution = resolve_game_entity("Gran Turismo 7 ปุ่ม", operation="controls")
    finally:
        _restore_env("PSU_ENTITY_RERANKER", previous)

    reranker = resolution.metadata.get("reranker", {})
    assert resolution.status == "exact", resolution.as_dict()
    assert resolution.top_candidate and resolution.top_candidate.title == "Gran Turismo 7", resolution.as_dict()
    assert reranker.get("action") == "skipped", resolution.as_dict()
    assert reranker.get("reason") == "already_exact_alias", resolution.as_dict()


def test_cross_domain_target_blocks_service_query_from_game_rerank() -> None:
    previous = _with_env("PSU_ENTITY_RERANKER", "1")
    previous_target = os.environ.get("PSU_TARGET_RERANKER")
    os.environ.pop("PSU_TARGET_RERANKER", None)
    try:
        resolution = resolve_game_entity("Nintendo Switch ราคาเท่าไหร่", operation="price")
    finally:
        _restore_env("PSU_ENTITY_RERANKER", previous)
        _restore_env("PSU_TARGET_RERANKER", previous_target)

    reranker = resolution.metadata.get("reranker", {})
    target = reranker.get("cross_domain_target_resolution", {})
    top_target = target.get("top_candidate", {})
    assert resolution.status == "unknown", resolution.as_dict()
    assert reranker.get("action") == "skipped", resolution.as_dict()
    assert str(reranker.get("reason", "")).startswith("cross_domain_target_not_game"), resolution.as_dict()
    assert top_target.get("domain") == "service_fee", resolution.as_dict()


if __name__ == "__main__":
    test_reranker_disabled_by_default_path()
    test_reranker_skips_generic_family_question()
    test_reranker_skips_high_confidence_exact_game()
    test_cross_domain_target_blocks_service_query_from_game_rerank()
    print("OK entity reranker gate smoke tests")
