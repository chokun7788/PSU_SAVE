from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.game_title_correction import detect_game_title_correction  # noqa: E402
from app.pipeline.preprocess import preprocess_input  # noqa: E402


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item.lower() not in text.lower()]
    if missing:
        raise AssertionError(f"{label}: missing {missing}\n{text}")


def assert_not_contains(text: str, forbidden: list[str], label: str) -> None:
    found = [item for item in forbidden if item.lower() in text.lower()]
    if found:
        raise AssertionError(f"{label}: forbidden {found}\n{text}")


def check_answer(question: str, must_contain: list[str], *, must_not_contain: list[str] | None = None) -> None:
    result = answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert_contains(result.answer, must_contain, question)
    assert_not_contains(result.answer, must_not_contain or ["ยังไม่พบ Tekkrn8", "ยังไม่พบ Valornat"], question)
    if not result.validation.ok:
        raise AssertionError(f"{question}: validation errors {result.validation.errors}\n{result.answer}")
    print(f"OK {result.mode} {result.route.category}/{result.route.intent} | {question}")


def main() -> int:
    correction = detect_game_title_correction("อยากเล่น tekkrn8 ต้องทำยังไง")
    if correction is None or correction.game != "TEKKEN 8":
        raise AssertionError(f"expected TEKKEN 8 correction, got {correction}")
    broad_correction = detect_game_title_correction("msrio มีข้อมูลไหม")
    if broad_correction is None or broad_correction.game != "Mario":
        raise AssertionError(f"expected broad Mario correction, got {broad_correction}")
    cod_thai_correction = detect_game_title_correction("เกม คอลออฟดูตี้ มีข้อมูลไหม")
    if cod_thai_correction is None or cod_thai_correction.game != "Call of Duty":
        raise AssertionError(f"expected broad Call of Duty correction, got {cod_thai_correction}")
    for question, expected_game in [
        ("mariokrt 8 มีข้อมูลไหม", "Mario Kart 8 Deluxe"),
        ("valrant คือเกมอะไร", "VALORANT"),
        ("overcookd2 มีปุ่มอะไรบ้าง", "Overcooked 2"),
        ("resdent evil มีข้อมูลไหม", "Resident Evil"),
        ("resdent evil 4 มีข้อมูลไหม", "Resident Evil 4"),
        ("call of dutty warzone มีข้อมูลไหม", "Call of Duty: Warzone"),
        ("เกม msrio มีข้อมูลไหม", "Mario"),
        ("เกม mqrio มีข้อมูลไหม", "Mario"),
        ("เกม คอลออฟดูตี้ มีข้อมูลไหม", "Call of Duty"),
    ]:
        typo_correction = detect_game_title_correction(question)
        if typo_correction is None or typo_correction.game != expected_game:
            raise AssertionError(f"expected {expected_game} correction for {question}, got {typo_correction}")
    if detect_game_title_correction("music มีข้อมูลไหม") is not None:
        raise AssertionError("non-game word 'music' should not be corrected as a game title")
    if detect_game_title_correction("accelerate คืออะไร") is not None:
        raise AssertionError("control/action word 'accelerate' should not be corrected as a game title")
    if detect_game_title_correction("Resident Evil มีข้อมูลไหม") is not None:
        raise AssertionError("exact broad title 'Resident Evil' should remain a family query")

    pre = preprocess_input("tekkrn8 มีปุ่มอะไรบ้าง")
    if "TEKKEN 8" not in pre.clean_query:
        raise AssertionError(f"expected active corrected query, got {pre}")

    bare_tekken = answer_question_pipeline_debug(
        "Tekken 8",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    if bare_tekken.mode != "pipeline:structured_game_detail":
        raise AssertionError(f"Tekken 8 should answer as game detail, got {bare_tekken.mode}\n{bare_tekken.answer}")
    assert_contains(bare_tekken.answer, ["TEKKEN 8", "PlayStation 5 Zone"], "bare Tekken 8")
    assert_not_contains(bare_tekken.answer, ["44", "Local LLM"], "bare Tekken 8 should not list all games or use fallback")

    spaced_overcooked = answer_question_pipeline_debug(
        "Over cook",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    if spaced_overcooked.mode != "pipeline:structured_games_family":
        raise AssertionError(f"Over cook should answer as Overcooked family, got {spaced_overcooked.mode}\n{spaced_overcooked.answer}")
    assert_contains(spaced_overcooked.answer, ["Overcooked!", "Overcooked! 2"], "spaced Over cook")
    assert_not_contains(spaced_overcooked.answer, ["44", "Local LLM"], "spaced Over cook should not list all games or use fallback")

    check_answer(
        "อยากเล่น tekkrn8 ต้องทำยังไง",
        ["TEKKEN 8", "PC #01-#02", "PlayStation 5 #01-#02", "เลือกวัน", "รอบเวลา"],
    )
    check_answer(
        "tekkrn8 มีปุ่มอะไรบ้าง",
        ["TEKKEN 8", "Square", "Triangle", "Cross", "Circle", "Options"],
    )
    check_answer(
        "valornat คือเกมอะไร",
        ["VALORANT", "Tactical FPS", "PC Zone"],
    )
    check_answer(
        "fortnte มีข้อมูลไหม",
        ["Fortnite", "PlayStation 5 Zone"],
    )
    check_answer(
        "mario krta 8 มีข้อมูลไหม",
        ["Mario Kart 8 Deluxe", "Nintendo Switch Zone"],
        must_not_contain=["พบเกมที่เกี่ยวข้องกับ Mario", "New Super Mario Bros."],
    )
    check_answer(
        "mariokrt 8 มีข้อมูลไหม",
        ["Mario Kart 8 Deluxe", "Nintendo Switch Zone"],
        must_not_contain=["พบเกมที่เกี่ยวข้องกับ Mario", "New Super Mario Bros."],
    )
    check_answer(
        "มาริโอคาท 8 มีข้อมูลไหม",
        ["Mario Kart 8 Deluxe", "Nintendo Switch Zone"],
        must_not_contain=["พบเกมที่เกี่ยวข้องกับ Mario", "New Super Mario Bros."],
    )
    check_answer(
        "มาริโอคาส มีข้อมูลไหม",
        ["Mario Kart 8 Deluxe", "Nintendo Switch Zone"],
        must_not_contain=["พบเกมที่เกี่ยวข้องกับ Mario", "New Super Mario Bros."],
    )
    check_answer(
        "mqrio kart มีข้อมูลไหม",
        ["Mario Kart 8 Deluxe", "Nintendo Switch Zone"],
        must_not_contain=["พบเกมที่เกี่ยวข้องกับ Mario", "New Super Mario Bros."],
    )
    check_answer(
        "msrio มีข้อมูลไหม",
        ["พบเกมที่เกี่ยวข้องกับ Mario", "Mario Kart 8 Deluxe", "Super Mario Odyssey"],
    )
    check_answer(
        "mqrio มีข้อมูลไหม",
        ["พบเกมที่เกี่ยวข้องกับ Mario", "Mario Kart 8 Deluxe", "Super Mario Odyssey"],
    )
    check_answer(
        "zeldq มีข้อมูลไหม",
        ["The Legend of Zelda: Breath of the Wild", "Nintendo Switch Zone"],
    )
    check_answer(
        "resdent evil มีข้อมูลไหม",
        ["Resident Evil มีหลายเกม", "ยังไม่ชัด", "Resident Evil 4", "Resident Evil Village"],
    )
    check_answer(
        "เกม คอลออฟดูตี้ มีข้อมูลไหม",
        ["Call of Duty มีหลายเกม", "ยังไม่ชัด", "Call of Duty: Modern Warfare III", "Call of Duty: Warzone"],
    )
    check_answer(
        "คอลออฟดูตี้ มีเกมอะไรบ้าง",
        ["พบเกมที่เกี่ยวข้องกับ Call of Duty", "Call of Duty: Modern Warfare III", "Call of Duty: Warzone"],
    )
    check_answer(
        "resdent evil 4 มีข้อมูลไหม",
        ["Resident Evil 4", "PlayStation 5 Zone"],
        must_not_contain=["พบเกมที่เกี่ยวข้องกับ Resident Evil", "Resident Evil Village"],
    )
    check_answer(
        "overcookd 2 มีปุ่มอะไรบ้าง",
        ["Overcooked 2", "มีอยู่ในรายการเกมที่ยืนยันได้", "Nintendo Switch Zone", "ยังไม่พบข้อมูลปุ่มควบคุม"],
    )
    check_answer(
        "Mario มีข้อมูลไหม",
        ["พบเกมที่เกี่ยวข้องกับ Mario", "Mario Kart 8 Deluxe", "Super Mario Odyssey"],
    )

    print("GAME TITLE TYPO CORRECTION SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
