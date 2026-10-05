from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.booking_policy_rag import (  # noqa: E402
    booking_policy_semantic_intent,
    booking_policy_semantic_route,
    is_specific_booking_policy_question,
)
from app.pipeline.question_frame import build_question_frame  # noqa: E402
from app.pipeline.schemas import PipelineRoute, UniversalIntent  # noqa: E402
from app.pipeline.semantic_vector_retrieval import retrieve_semantic_guarded  # noqa: E402


def _reservation_route() -> PipelineRoute:
    return PipelineRoute("reservation", "booking_policy", 0.94, "fact", "medium", "smoke")


def _reservation_intent() -> UniversalIntent:
    return UniversalIntent("reservation", "booking", confidence=0.94, method="heuristic")


def _policy_row() -> dict:
    return {
        "id": "booking_transfer_policy",
        "category": "knowledge",
        "title": "โอนสิทธิ์การจอง",
        "text": "ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้",
        "source_url": "local://tests/booking-policy",
        "trust_level": "internal_verified",
        "status": "published",
        "language": "th",
        "facets": ["policy"],
        "entity_ids": [],
    }


def test_gate_only_defers_specific_policy_exceptions() -> None:
    route = _reservation_route()
    for question in (
        "จองไว้ให้เพื่อนใช้แทนได้ไหม",
        "แก้ไขข้อมูลหลังจองได้หรือเปล่า",
        "ถ้ามาช้าแล้วไม่เช็คอินก่อนเวลาจะเป็นยังไง",
        "ขอเงินคืนได้ไหม",
    ):
        assert is_specific_booking_policy_question(question, route), question

    for question in ("มีวิธีจองแบบละเอียดไหม", "จองยังไง", "ต้องจองล่วงหน้ากี่ชั่วโมง"):
        assert not is_specific_booking_policy_question(question, route), question


def test_gate_uses_semantic_evidence_contract() -> None:
    route = booking_policy_semantic_route(_reservation_route())
    intent = booking_policy_semantic_intent(_reservation_intent())
    frame = build_question_frame("จองไว้ให้เพื่อนใช้แทนได้ไหม", route, intent)
    assert route.category == "knowledge"
    assert frame.operation == "semantic_evidence_lookup", frame
    assert frame.domain == "knowledge", frame


def test_gate_retrieves_only_knowledge_policy_evidence() -> None:
    row = _policy_row()
    index = {
        "model": "test-embedding",
        "dimensions": 2,
        "doc_count": 1,
        "docs": [{
            "id": row["id"],
            "category": "knowledge",
            "title": row["title"],
            "row": row,
            "vector": [1.0, 0.0],
        }],
    }
    hits, _trace = retrieve_semantic_guarded(
        "จองไว้ให้เพื่อนใช้แทนได้ไหม",
        booking_policy_semantic_route(_reservation_route()),
        query_vector=(1.0, 0.0),
        index=index,
        locale="th",
    )
    assert hits and hits[0]["id"] == "booking_transfer_policy", hits


def main() -> int:
    test_gate_only_defers_specific_policy_exceptions()
    test_gate_uses_semantic_evidence_contract()
    test_gate_retrieves_only_knowledge_policy_evidence()
    print("BOOKING POLICY RAG GATE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
