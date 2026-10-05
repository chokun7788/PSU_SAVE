from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.answer_contracts import validate_answer_contract  # noqa: E402
from app.pipeline.capability_registry import build_candidate_decisions  # noqa: E402
from app.pipeline.entity_resolver import resolve_game_entity  # noqa: E402
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.preprocess import preprocess_input  # noqa: E402
from app.pipeline.question_frame import build_question_frame  # noqa: E402
from app.pipeline.schemas import PipelineRoute, UniversalIntent  # noqa: E402
from app.pipeline.target_resolver import resolve_target_candidate  # noqa: E402
from app.pipeline.vector_retrieval import looks_like_game_control_query  # noqa: E402


def route(category: str, intent: str = "lookup") -> PipelineRoute:
    return PipelineRoute(category, intent, 0.92, "fact", "low", "correctness control flow smoke")


def universal(domain: str, operation: str) -> UniversalIntent:
    return UniversalIntent(domain=domain, operation=operation, confidence=0.88)


def selected_capability(question: str, current_route: PipelineRoute, intent: UniversalIntent) -> tuple[str, dict]:
    accepted, _rejected, trace = build_candidate_decisions(current_route, intent, question=question)
    assert accepted
    return accepted[0].capability_id, trace.metadata["selection"]


def main() -> int:
    frame = build_question_frame(
        "ถ้าจะเล่น Naruto ต้องทำไง",
        route("reservation", "booking_policy"),
        universal("reservation", "how_to"),
    )
    assert frame.operation == "booking_lookup", frame.as_dict()
    assert frame.expected_answer_types == ("booking", "how_to")
    print("OK play-access frame stays booking")

    frame = build_question_frame(
        "Logitech G923 คืออะไร ใช้ยังไง",
        route("equipment", "how_to"),
        universal("equipment", "how_to"),
    )
    assert frame.operation == "equipment_lookup", frame.as_dict()
    assert frame.targets and frame.targets[0].target_type == "equipment"
    print("OK named equipment how-to frame stays equipment")

    frame = build_question_frame(
        "Overcooked 2 มีปุ่มอะไรบ้าง",
        route("games", "game_control_lookup"),
        universal("game_controls", "control"),
    )
    assert frame.target_status == "exact", frame.as_dict()
    assert frame.targets and "Overcooked" in frame.targets[0].label and "2" in frame.targets[0].label
    print("OK explicit sequel beats parent alias")

    resident_evil = resolve_target_candidate(
        "Resident Evil 4 มีข้อมูลไหม",
        operation="detail",
        preferred_domains=("games",),
    )
    assert resident_evil.status == "exact", resident_evil.as_dict()
    assert resident_evil.top_candidate and resident_evil.top_candidate.label == "Resident Evil 4"
    print("OK exact title beats a clipped token-overlap candidate")

    for question, expected in (
        ("Call of Duty: Warzone คือเกมอะไร", "Call of Duty: Warzone"),
        ("The Last of Us Part I เป็นเกมแนวไหน", "The Last of Us Part I"),
        ("The Legend of Zelda เล่นยังไง", "The Legend of Zelda: Breath of The Wild"),
    ):
        exact_title = resolve_target_candidate(
            question,
            operation="detail",
            preferred_domains=("games",),
        )
        assert exact_title.status == "exact", exact_title.as_dict()
        assert exact_title.top_candidate and exact_title.top_candidate.label == expected, exact_title.as_dict()
    print("OK domain bias cannot promote token overlap above exact titles")

    no_controls = resolve_game_entity("Overcooked 2 มีปุ่มอะไรบ้าง", operation="controls")
    assert no_controls.status == "exact", no_controls.as_dict()
    assert no_controls.top_candidate and no_controls.top_candidate.title == "Overcooked! 2"
    assert not no_controls.top_candidate.has_controls
    print("OK exact game without controls beats parent game with controls")

    parent_controls = resolve_game_entity("Overcooked! มีปุ่มอะไรบ้าง", operation="controls")
    assert parent_controls.status == "exact", parent_controls.as_dict()
    assert parent_controls.top_candidate and parent_controls.top_candidate.title == "Overcooked!"
    assert parent_controls.top_candidate.has_controls
    print("OK explicit canonical parent title beats normalized sequel alias")

    protected_service = preprocess_input("Nintendo Switch มีเกมอะไรบ้าง")
    assert "Nintendo Switch Sports" not in protected_service.clean_query, protected_service.clean_query
    print("OK service name is not autocorrected into a game title")

    assert not looks_like_game_control_query("Sony PlayStation VR2 คืออะไร")
    assert looks_like_game_control_query("R2 ใน TEKKEN 8 ใช้ทำอะไร")
    print("OK short controller token uses token boundaries")

    for question, expected_mode, expected_text in (
        ("Mario Party Superstars คือเกมอะไร", "pipeline:structured_game_detail", "Mario Party Superstars"),
        ("Tekken 8 มีในเครื่องไหน", "pipeline:structured_service_game_availability", "PC #01-#02"),
        ("อุปกรณ์ไหนเกมเยอะสุด", "pipeline:structured_game_zone_ranking", "จำนวนเกมตามโซน"),
        ("Sony PlayStation VR2 ใช้ทำอะไร", "pipeline:structured_equipment_item", "Sony PlayStation VR2"),
        ("Overcooked! ปุ่มทั้งหมดมีอะไรบ้าง", "pipeline:structured_game_controls", "L (Left Stick)"),
        ("ทำจอยพังโดนปรับเท่าไหร่", "pipeline:penalty_fast_path", "ค่าปรับ"),
        ("PC เครื่อง 1 รายการเกมมีอะไรบ้าง", "pipeline:structured_service_game_availability", "TEKKEN 8"),
    ):
        result = answer_question_pipeline_debug(
            question,
            experimental_allow_llm=False,
            global_timeout_sec=20.0,
        )
        assert result.mode == expected_mode, (question, result.mode, result.answer)
        assert expected_text in result.answer, (question, result.answer)
        assert result.validation.ok, (question, result.validation.errors)
    print("OK operation and exact target beat broad noun and substring conflicts")

    capability_id, _selection = selected_capability(
        "Gran Turismo ปุ่ม",
        route("games", "game_control_lookup"),
        universal("game_controls", "control"),
    )
    assert capability_id == "structured.game_controls", capability_id
    print("OK control question selects control capability")

    capability_id, _selection = selected_capability(
        "Gran Turismo เล่นยังไง",
        route("games", "game_detail_lookup"),
        universal("games", "how_to"),
    )
    assert capability_id == "structured.games", capability_id
    print("OK gameplay question selects game-detail capability")

    capability_id, selection = selected_capability(
        "อุปกรณ์ไหนเกมเยอะสุด",
        route("games", "game_zone_ranking"),
        universal("games", "count"),
    )
    assert capability_id == "structured.games", capability_id
    assert float(selection["margin"]) > 0.0, selection
    print("OK game-count ranking does not select equipment catalog")

    wrong_target = validate_answer_contract(
        "Gran Turismo ปุ่มอะไร",
        "NARUTO X BORUTO มีข้อมูลปุ่มควบคุม: Circle = โจมตี",
        route("games", "game_control_lookup"),
        hits=[{"category": "game_controls"}],
        mode="pipeline:structured_game_controls",
        intent=universal("game_controls", "control"),
    )
    assert not wrong_target.ok
    assert any(error.startswith("answer_contract_target_missing:") for error in wrong_target.errors)
    print("OK answer contract rejects wrong-game controls")

    wrong_source = validate_answer_contract(
        "Gran Turismo ปุ่มอะไร",
        "Gran Turismo 7 มีข้อมูลปุ่มควบคุม: R2 = เร่งเครื่อง",
        route("games", "game_control_lookup"),
        hits=[{"category": "games"}],
        mode="pipeline:structured_game_controls",
        intent=universal("game_controls", "control"),
    )
    assert not wrong_source.ok
    assert any(error.startswith("answer_contract_source_domain_mismatch:") for error in wrong_source.errors)
    print("OK answer contract rejects wrong evidence domain")

    correct = validate_answer_contract(
        "Gran Turismo ปุ่มอะไร",
        "Gran Turismo 7 มีข้อมูลปุ่มควบคุม: R2 = เร่งเครื่อง",
        route("games", "game_control_lookup"),
        hits=[{"category": "game_controls"}],
        mode="pipeline:structured_game_controls",
        intent=universal("game_controls", "control"),
    )
    assert correct.ok, correct.errors
    print("OK answer contract accepts aligned route-target-source-answer")

    print("CORRECTNESS CONTROL FLOW V1 SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
