from __future__ import annotations

import os
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ["PSU_BILINGUAL_EN_ENABLED"] = "1"
os.environ["PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW"] = "0"
os.environ.pop("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH", None)

from app.core.locale import contains_thai_prose  # noqa: E402
from app.core.source_registry import (  # noqa: E402
    PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,
    SERVICE_FEE_IMAGE_2026_ID,
)
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.bilingual_english import requires_english_intent_review  # noqa: E402
from app.pipeline.schemas import PipelineRoute  # noqa: E402
from app.pipeline.universal_intent import _build_intent_candidates, _heuristic_intent  # noqa: E402


def _answer(question: str, **kwargs):
    options = {
        "experimental_allow_llm": False,
        "experimental_rag_fallback": False,
        "global_timeout_sec": 10.0,
    }
    options.update(kwargs)
    result = answer_question_pipeline_debug(
        question,
        **options,
    )
    assert result.elapsed < 10.0, (question, result.elapsed, result.mode)
    return result


def _source_ids(result) -> set[str]:
    ids: set[str] = set()
    for hit in result.hits:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        ids.update(str(value) for value in metadata.get("source_ids", []) if value)
    return ids


def main() -> int:
    catalog = _answer("What games are available?")
    assert catalog.language.effective == "en"
    assert catalog.route.category == "games"
    assert catalog.mode == "pipeline:structured_games_catalog_en"
    assert "There are currently 42 verified games available." in catalog.answer
    assert not contains_thai_prose(catalog.answer)

    casual_catalog = _answer("what game u have")
    assert casual_catalog.route.category == "games"
    assert casual_catalog.mode == "pipeline:structured_games_catalog_en"
    assert "There are currently 42 verified games available." in casual_catalog.answer
    assert not requires_english_intent_review(casual_catalog)

    repeated_key_catalog = _answer("what game you havve")
    assert repeated_key_catalog.route.category == "games"
    assert repeated_key_catalog.mode == "pipeline:structured_games_catalog_en"

    weak_game_route = PipelineRoute("general", "general_knowledge_query", 0.55, "fact", "low", "test")
    weak_game_intent = _heuristic_intent("could i see a game selection?", weak_game_route)
    weak_game_candidates = _build_intent_candidates("could i see a game selection?", weak_game_route, weak_game_intent)
    assert any(item["domain"] == "games" and item["operation"] == "list" for item in weak_game_candidates)

    price = _answer("How much is one hour on PC for a PSU student?")
    assert price.route.category == "service_fee"
    assert "0 THB" in price.answer
    assert not requires_english_intent_review(price)
    assert not contains_thai_prose(price.answer)
    assert {SERVICE_FEE_IMAGE_2026_ID, PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID} <= _source_ids(price)

    game_price = _answer("How much does PUBG: BATTLEGROUNDS cost?")
    assert game_price.route.category == "service_fee"
    assert "PC - 1 hour" in game_price.answer
    assert "available on" not in game_price.answer

    multi_service_price = _answer("What is the price of Resident Evil 4?")
    assert multi_service_price.mode == "pipeline:price_service_clarification_en"
    assert "Which service" in multi_service_price.answer

    price_comparison = _answer("Which is more expensive, PS5 or Nintendo?")
    assert price_comparison.route.category == "service_fee"
    assert "PlayStation 5" in price_comparison.answer

    vr_comparison = _answer("How are VR 30-minute sessions different from VR one-hour sessions?")
    assert vr_comparison.route.category == "service_fee"

    finals_game = _answer("Where can the finals be played?")
    assert finals_game.route.category == "games"

    walking_control = _answer("In Counter-Strike 2, what key do you press to walk slowly?")
    assert walking_control.route.category == "games"

    compared_controls = _answer("What buttons does Resident Evil Village have in comparison to TEKKEN 8?")
    assert compared_controls.route.category == "games"

    schedule = _answer("Is the studio open on Wednesday?")
    assert schedule.route.category == "schedule"
    assert "Wednesday" in schedule.answer

    always_open = _answer("Is the studio open 24 hours?")
    assert always_open.route.category == "schedule"
    assert "not open 24 hours" in always_open.answer

    morning = _answer("What time is the morning session?")
    assert "09:00-12:00" in morning.answer

    allowed = _answer("Are food and drinks allowed?")
    assert allowed.route.category != "schedule"
    assert "Wednesday" not in allowed.answer
    assert not contains_thai_prose(allowed.answer)

    damaged = _answer("What happens if I damage the equipment?")
    assert damaged.route.category == "penalty"
    assert "responsible" in damaged.answer.lower()
    assert damaged.mode != "pipeline:structured_equipment_catalog_en"

    booking = _answer("How do I make a booking?")
    assert booking.route.category == "reservation"
    assert "booking" in booking.answer.lower()
    assert not requires_english_intent_review(booking)

    payment_deadline = _answer("How long do I have to pay after booking?")
    assert payment_deadline.route.category == "reservation"
    assert "10 minutes" in payment_deadline.answer

    natural_payment_deadline = _answer("After booking, how many minutes do I have to pay?")
    assert natural_payment_deadline.route.category == "reservation"
    assert "10 minutes" in natural_payment_deadline.answer

    booking_change = _answer("Can I modify my booking after it is made?")
    assert booking_change.route.category == "reservation"
    assert "cannot be edited" in booking_change.answer

    booking_summary = _answer("Summarize the booking steps for me")
    assert booking_summary.route.category == "reservation"

    booking_advance = _answer("How many hours in advance must you book?")
    assert booking_advance.route.category == "reservation"

    late_checkin = _answer("What happens if I arrive late?")
    assert late_checkin.route.category == "reservation"

    multi_zone_games = _answer("Which game can be played across multiple zones?")
    assert multi_zone_games.route.category == "games"
    assert "multiple zones" in multi_zone_games.answer

    smoking = _answer("Can I smoke inside the studio?")
    assert smoking.route.category == "rules"
    assert "prohibited" in smoking.answer.lower()

    slot = _answer("Can you show the live available slots?")
    assert slot.route.category == "no_answer"
    assert slot.route.intent == "live_slot_unavailable"
    assert "live booking-slot" in slot.answer.lower()

    equipment = _answer("What equipment is available in VR Zone?")
    assert equipment.route.category == "equipment"
    assert "Verified equipment" in equipment.answer
    assert not contains_thai_prose(equipment.answer)

    technical_definition = _answer("What is a GPU in simple terms?")
    assert technical_definition.route.category == "no_answer"
    assert "Verified equipment" not in technical_definition.answer

    switch_equipment = _answer("What equipment is in the Nintendo Switch Zone?")
    assert switch_equipment.route.category == "equipment"
    assert "Nintendo Switch OLED" in switch_equipment.answer

    switch_offer = _answer("What does the Nintendo Switch Zone offer?")
    assert switch_offer.route.category == "equipment"

    equipment_detail = _answer("What is the Gaming PC used for?")
    assert equipment_detail.mode == "pipeline:missing_english_localization"

    cockpit = _answer("What is Racezone Full Cockpit V3?")
    assert cockpit.route.category == "equipment"
    assert cockpit.mode == "pipeline:structured_equipment_item_en"
    assert "Cockpit Zone" in cockpit.answer

    tv_location = _answer("Where is the 65-inch TV located?")
    assert tv_location.route.category == "equipment"
    assert tv_location.mode == "pipeline:structured_equipment_item_en"
    assert "Cockpit Zone" in tv_location.answer

    sofa_usage = _answer("What is the sofa with two seats used for?")
    assert sofa_usage.route.category == "equipment"
    assert sofa_usage.mode == "pipeline:missing_english_localization"

    headset_usage = _answer("What is the Pulse Elite Wireless Headset used for?")
    assert headset_usage.route.category == "equipment"
    assert headset_usage.mode == "pipeline:missing_english_localization"

    unknown_game = _answer("Can I play Minecraft at the studio?")
    assert "Minecraft" in unknown_game.answer
    assert "verified games available" not in unknown_game.answer.lower()
    assert "could not find" in unknown_game.answer.lower()

    controls = _answer("What are the controls for Beat Saber?")
    assert controls.mode == "pipeline:structured_game_controls_en"
    assert controls.route.intent == "game_control_lookup"
    assert "Beat Saber controls" in controls.answer
    assert not contains_thai_prose(controls.answer)

    ragnarok_controls = _answer("What are the controls for God of War Ragnarök?")
    assert ragnarok_controls.mode == "pipeline:structured_game_controls_en"
    assert "God of War Ragnarok controls" in ragnarok_controls.answer
    assert "L3: Sprint" in ragnarok_controls.answer

    overcooked_two_controls = _answer("What are the controls for Overcooked 2?")
    assert overcooked_two_controls.mode == "pipeline:structured_game_controls_en"
    assert "Cross: Pick Up / Drop" in overcooked_two_controls.answer
    assert "Circle: Dash" in overcooked_two_controls.answer

    delta_force_controls = _answer("What are the controls for Delta Force?")
    assert delta_force_controls.mode == "pipeline:game_controls_mapping_pending_en"
    assert "will not guess the controls" in delta_force_controls.answer
    assert "original source in Thai" not in delta_force_controls.answer
    assert "playstation.com/en-gb/games/delta-force" in delta_force_controls.answer

    unknown_non_domain = _answer(
        "what is a mechanical keyboard?",
        experimental_allow_llm=True,
        experimental_rag_fallback=True,
        global_timeout_sec=19.0,
    )
    assert unknown_non_domain.mode in {
        "pipeline:general_llm_direct",
        "pipeline:general_rag_miss_llm_unavailable",
    }, unknown_non_domain.mode
    if unknown_non_domain.mode == "pipeline:general_llm_direct":
        assert "mechanical keyboard" in unknown_non_domain.answer.lower()
        assert "not verified by the psu esports" in unknown_non_domain.answer.lower()
    else:
        assert "temporarily unavailable" in unknown_non_domain.answer.lower()

    it_takes_two_controls = _answer("In It Takes Two, what buttons are used for movement?")
    assert it_takes_two_controls.route.category == "games"
    assert it_takes_two_controls.mode == "pipeline:structured_game_controls_en"
    assert "L (Left Stick): Move" in it_takes_two_controls.answer
    assert not contains_thai_prose(it_takes_two_controls.answer)

    beat_saber_location = _answer("Can I play Beat Saber in the VR Zone?")
    assert beat_saber_location.route.category == "games"
    assert "Beat Saber is available on" in beat_saber_location.answer
    assert not contains_thai_prose(beat_saber_location.answer)

    switch_games = _answer("What games are on Nintendo Switch? Please use verified information.")
    assert switch_games.route.category == "games"
    assert "There are currently 17 verified games in Nintendo Switch Zone." in switch_games.answer
    assert "•    Mario Kart 8 Deluxe" in switch_games.answer

    unknown_called = _answer("Can I use an unknown game called Example Quest?")
    assert unknown_called.route.category == "games"
    assert "Example Quest" in unknown_called.answer
    assert "verified games available" not in unknown_called.answer.lower()

    untranslated_detail = _answer("Tell me about VALORANT")
    assert untranslated_detail.mode == "pipeline:missing_english_localization"
    assert "English localization" in untranslated_detail.answer
    assert not contains_thai_prose(untranslated_detail.answer)

    competition = _answer("What are the competition rules?")
    assert competition.mode == "pipeline:competition_target_clarification_en"
    assert competition.route.category == "competition_rules"
    assert not contains_thai_prose(competition.answer)

    unknown_competition_target = _answer("Does ROV require check-in before a match?")
    assert unknown_competition_target.route.category == "competition_rules"
    assert unknown_competition_target.mode in {
        "pipeline:missing_english_localization",
        "pipeline:competition_facet_not_covered_no_answer_en",
    }
    assert "VALORANT" not in unknown_competition_target.answer

    rov_restart = _answer("Can ROV request a restart?")
    assert rov_restart.route.category == "competition_rules"

    rov_lost_match = _answer("In ROV, what should I do if the game gets lost?")
    assert rov_lost_match.route.category == "competition_rules"

    paused_match = _answer("Can VALORANT be paused?")
    assert paused_match.route.category == "competition_rules"
    assert paused_match.mode in {"pipeline:structured_competition_rules_en", "pipeline:missing_english_localization"}

    final_fantasy = _answer("What is FINAL FANTASY XVI?")
    assert final_fantasy.route.category == "games"
    assert final_fantasy.mode in {"pipeline:structured_game_detail_en", "pipeline:missing_english_localization"}

    gaming_chair = _answer("Where is the gaming chair located?")
    assert gaming_chair.route.category == "equipment"
    assert gaming_chair.mode == "pipeline:structured_equipment_item_en"
    assert "PC Zone" in gaming_chair.answer

    vr2 = _answer("What is Sony PlayStation VR2?")
    assert vr2.route.category == "equipment"
    assert vr2.mode == "pipeline:structured_equipment_item_en"
    assert "VR Zone" in vr2.answer

    vice_chancellor = _answer("Who is the deputy vice-chancellor?")
    assert vice_chancellor.route.category == "overview"
    assert vice_chancellor.mode in {"pipeline:structured_members_en", "pipeline:structured_members_source_th"}
    assert "official Thai source" in vice_chancellor.answer
    assert "https://esports.phuket.psu.ac.th/about-us/Members" in vice_chancellor.answer

    member_position = _answer("What position does Prof. Dr. Nuwat Kao-pradab hold?")
    assert member_position.route.category == "overview"
    assert member_position.mode in {"pipeline:structured_members_en", "pipeline:structured_members_source_th"}

    unknown_member_role = _answer("Who is the referee?")
    assert unknown_member_role.route.category == "overview"
    assert unknown_member_role.mode == "pipeline:member_role_not_found_en"

    naruto_character_control = _answer("In NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS, what button changes the main character?")
    assert naruto_character_control.route.category == "games"

    private_phone = _answer("What is the personal phone number of the staff member?")
    assert private_phone.route.category == "no_answer"

    forced_english = _answer("มีเกมอะไรบ้าง", locale="en")
    assert forced_english.language.effective == "en"
    assert "There are currently 42 verified games available." in forced_english.answer
    assert "PC Zone (6 games)" in forced_english.answer
    assert "•    Call of Duty: Warzone" in forced_english.answer
    assert not contains_thai_prose(forced_english.answer)

    forced_thai = _answer("What games are available?", locale="th")
    assert forced_thai.language.effective == "th"
    assert contains_thai_prose(forced_thai.answer)

    follow_up = _answer(
        "and price?",
        recent_history=[{"answer_language": "en"}],
    )
    assert follow_up.language.effective == "en"
    assert not contains_thai_prose(follow_up.answer)

    print("OK bilingual deterministic routes, safe no-answer, source IDs, leakage guard, overrides, and follow-up")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
