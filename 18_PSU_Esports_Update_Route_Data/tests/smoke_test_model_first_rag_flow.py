from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.claim_validator import validate_grounded_claims  # noqa: E402
from app.pipeline.evidence_packer import pack_evidence  # noqa: E402
from app.pipeline.facts_composer import compose_structured_answer  # noqa: E402
from app.pipeline.hybrid_retrieval import retrieve_hybrid_guarded  # noqa: E402
from app.pipeline.model_gateway import plan_rag_model_path, preflight_llm_allowed, retrieval_budget  # noqa: E402
from app.pipeline.request_deadline import request_deadline  # noqa: E402
from app.pipeline.schemas import PipelineRoute, UniversalIntent  # noqa: E402


ROUTE = PipelineRoute("knowledge", "knowledge_lookup", 0.82, "summary", "medium", "smoke")
INTENT = UniversalIntent("knowledge", "lookup", "booking", 0.82, "smoke")


def test_default_model_first_is_off() -> None:
    previous = os.environ.pop("PSU_MODEL_FIRST_FLOW", None)
    try:
        plan = plan_rag_model_path(
            query="สรุปวิธีจอง",
            route=ROUTE,
            allow_llm=True,
            hit_count=3,
            retrieval_confidence=0.75,
        )
    finally:
        if previous is not None:
            os.environ["PSU_MODEL_FIRST_FLOW"] = previous
    assert plan.path == "deterministic_rag"
    assert plan.use_llm is False


def test_adaptive_budget_expands_for_compound_query() -> None:
    budget = retrieval_budget("สรุปวิธีจอง แล้วต้องชำระเงินภายในกี่นาที", ROUTE)
    assert budget["candidate_limit"] == 12
    assert budget["final_limit"] == 5
    assert budget["broad_or_complex"] is True


def test_high_confidence_structured_route_skips_preflight_llm() -> None:
    previous = os.environ.get("PSU_MODEL_FIRST_FLOW")
    os.environ["PSU_MODEL_FIRST_FLOW"] = "1"
    try:
        allowed, reason = preflight_llm_allowed(
            PipelineRoute("games", "list", 0.95, "list", "medium", "smoke"),
            True,
        )
    finally:
        if previous is None:
            os.environ.pop("PSU_MODEL_FIRST_FLOW", None)
        else:
            os.environ["PSU_MODEL_FIRST_FLOW"] = previous
    assert allowed is False
    assert reason == "high-confidence deterministic route"


def test_model_first_rag_route_reserves_budget_for_grounded_composer() -> None:
    previous = os.environ.get("PSU_MODEL_FIRST_FLOW")
    os.environ["PSU_MODEL_FIRST_FLOW"] = "1"
    try:
        allowed, reason = preflight_llm_allowed(
            PipelineRoute("knowledge", "knowledge_lookup", 0.84, "summary", "medium", "smoke"),
            True,
        )
    finally:
        if previous is None:
            os.environ.pop("PSU_MODEL_FIRST_FLOW", None)
        else:
            os.environ["PSU_MODEL_FIRST_FLOW"] = previous
    assert allowed is False
    assert "reserves budget" in reason


def test_source_conflict_disables_grounded_composer() -> None:
    previous = os.environ.get("PSU_MODEL_FIRST_FLOW")
    os.environ["PSU_MODEL_FIRST_FLOW"] = "1"
    try:
        plan = plan_rag_model_path(
            query="สรุปข้อมูล",
            route=ROUTE,
            allow_llm=True,
            hit_count=4,
            retrieval_confidence=0.84,
            source_conflict=True,
        )
    finally:
        if previous is None:
            os.environ.pop("PSU_MODEL_FIRST_FLOW", None)
        else:
            os.environ["PSU_MODEL_FIRST_FLOW"] = previous
    assert plan.use_llm is False
    assert plan.reason == "source conflict requires deterministic review"


def test_document_reranker_uses_bge_contract_with_mock_model() -> None:
    import app.pipeline.document_reranker as document_reranker

    previous_enabled = os.environ.get("PSU_DOCUMENT_RERANKER")
    previous_loader = document_reranker._load_model

    class FakeCrossEncoder:
        def predict(self, pairs, **_kwargs):
            return [0.10, 0.95]

    os.environ["PSU_DOCUMENT_RERANKER"] = "1"
    document_reranker._load_model = lambda: FakeCrossEncoder()
    hits = [
        {"id": "weak", "title": "weak", "text": "weak"},
        {"id": "strong", "title": "strong", "text": "strong"},
    ]
    try:
        reranked, trace = document_reranker.rerank_documents("query", hits, limit=2)
    finally:
        document_reranker._load_model = previous_loader
        if previous_enabled is None:
            os.environ.pop("PSU_DOCUMENT_RERANKER", None)
        else:
            os.environ["PSU_DOCUMENT_RERANKER"] = previous_enabled
    assert reranked[0]["id"] == "strong"
    assert trace.decision == "bge_reranked"


def test_document_reranker_skips_cold_start_inside_product_deadline() -> None:
    import app.pipeline.document_reranker as document_reranker

    previous_enabled = os.environ.get("PSU_DOCUMENT_RERANKER")
    previous_cold_minimum = os.environ.get("PSU_DOCUMENT_RERANKER_COLD_START_MIN_REMAINING_SEC")
    previous_loader = document_reranker._load_model
    os.environ["PSU_DOCUMENT_RERANKER"] = "1"
    os.environ["PSU_DOCUMENT_RERANKER_COLD_START_MIN_REMAINING_SEC"] = "30"
    document_reranker._load_model = lambda: None
    try:
        with request_deadline(10):
            _, trace = document_reranker.rerank_documents(
                "query",
                [{"id": "a", "text": "a"}, {"id": "b", "text": "b"}],
                limit=2,
            )
    finally:
        document_reranker._load_model = previous_loader
        if previous_enabled is None:
            os.environ.pop("PSU_DOCUMENT_RERANKER", None)
        else:
            os.environ["PSU_DOCUMENT_RERANKER"] = previous_enabled
        if previous_cold_minimum is None:
            os.environ.pop("PSU_DOCUMENT_RERANKER_COLD_START_MIN_REMAINING_SEC", None)
        else:
            os.environ["PSU_DOCUMENT_RERANKER_COLD_START_MIN_REMAINING_SEC"] = previous_cold_minimum
    assert trace.decision == "skipped_cold_start"


def test_source_guard_does_not_confuse_numbers_from_separate_news_sources() -> None:
    from app.pipeline.source_guard import assess_sources

    quality = assess_sources([
        {"id": "news_a", "category": "events_news", "text": "กิจกรรมมีผู้เข้าร่วม 21 คน"},
        {"id": "news_b", "category": "events_news", "text": "กิจกรรมจัดวันที่ 27 กุมภาพันธ์ 2569 มีผู้เข้าร่วม 11 คน"},
    ])
    assert quality.conflict is False


def test_source_guard_detects_conflicting_values_for_same_claim() -> None:
    from app.pipeline.source_guard import assess_sources

    quality = assess_sources([
        {"id": "price_a", "category": "service_fee", "claim_key": "pc_hourly_price", "text": "ราคา 25 บาท"},
        {"id": "price_b", "category": "service_fee", "claim_key": "pc_hourly_price", "text": "ราคา 70 บาท"},
        {"id": "price_c", "category": "service_fee", "claim_key": "pc_hourly_price", "text": "ราคา 90 บาท"},
        {"id": "price_d", "category": "service_fee", "claim_key": "pc_hourly_price", "text": "ราคา 100 บาท"},
    ])
    assert quality.conflict is True


def test_evidence_packer_labels_and_deduplicates_sources() -> None:
    hits = [
        {"id": "reservation", "title": "Booking", "text": "ชำระเงินภายใน 10 นาที", "category": "reservation", "_hybrid_score": 9.2},
        {"id": "reservation", "title": "Booking", "text": "ชำระเงินภายใน 10 นาที", "category": "reservation", "_hybrid_score": 8.1},
    ]
    packed = pack_evidence("ชำระเงินภายในกี่นาที", hits)
    assert packed["item_count"] == 1
    assert packed["source_ids"] == ["reservation"]
    assert packed["items"][0]["text"] == "ชำระเงินภายใน 10 นาที"


def test_grounding_validator_rejects_unsupported_number() -> None:
    evidence = {"items": [{"source_id": "reservation", "text": "ชำระเงินภายใน 10 นาที"}]}
    result = validate_grounded_claims("ต้องชำระเงินภายใน 15 นาที", evidence)
    assert result.ok is False
    assert "15" in result.unsupported_numbers


def test_grounded_rag_composer_can_be_enabled_with_mocked_ollama() -> None:
    import app.pipeline.facts_composer as facts_composer

    previous_model_first = os.environ.get("PSU_MODEL_FIRST_FLOW")
    previous_call = facts_composer._call_ollama
    os.environ["PSU_MODEL_FIRST_FLOW"] = "1"
    facts_composer._call_ollama = lambda _prompt: "ชำระเงินภายใน 10 นาทีครับ\nแหล่งข้อมูล: local://reservation"
    evidence = {
        "items": [{
            "source_id": "reservation",
            "text": "ชำระเงินภายใน 10 นาที",
            "source_url": "local://reservation",
            "category": "reservation",
        }],
    }
    try:
        result = compose_structured_answer(
            question="ต้องชำระเงินภายในกี่นาที",
            draft_answer="ชำระเงินภายใน 10 นาทีครับ\nแหล่งข้อมูล: local://reservation",
            evidence=evidence,
            route=ROUTE,
            intent=INTENT,
            mode="hybrid_guarded_rerank",
            allow_llm=True,
        )
    finally:
        facts_composer._call_ollama = previous_call
        if previous_model_first is None:
            os.environ.pop("PSU_MODEL_FIRST_FLOW", None)
        else:
            os.environ["PSU_MODEL_FIRST_FLOW"] = previous_model_first
    assert result.used_llm is True
    assert result.trace.decision == "llm_composed"


def test_hybrid_retrieval_keeps_default_path_healthy() -> None:
    previous = os.environ.pop("PSU_MODEL_FIRST_FLOW", None)
    try:
        hits, trace = retrieve_hybrid_guarded("เกมแนวแข่งรถมีอะไรบ้าง", PipelineRoute("games", "game_catalog_lookup", 0.9, "list", "low", "smoke"))
    finally:
        if previous is not None:
            os.environ["PSU_MODEL_FIRST_FLOW"] = previous
    assert isinstance(hits, list)
    assert trace.stage == "hybrid_retrieval"
    assert "retrieval_budget" in trace.metadata


if __name__ == "__main__":
    test_default_model_first_is_off()
    test_adaptive_budget_expands_for_compound_query()
    test_high_confidence_structured_route_skips_preflight_llm()
    test_model_first_rag_route_reserves_budget_for_grounded_composer()
    test_source_conflict_disables_grounded_composer()
    test_document_reranker_uses_bge_contract_with_mock_model()
    test_document_reranker_skips_cold_start_inside_product_deadline()
    test_source_guard_does_not_confuse_numbers_from_separate_news_sources()
    test_source_guard_detects_conflicting_values_for_same_claim()
    test_evidence_packer_labels_and_deduplicates_sources()
    test_grounding_validator_rejects_unsupported_number()
    test_grounded_rag_composer_can_be_enabled_with_mocked_ollama()
    test_hybrid_retrieval_keeps_default_path_healthy()
    print("MODEL-FIRST RAG FLOW SMOKE TEST OK")
