from __future__ import annotations

import os
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ["PSU_BILINGUAL_EN_ENABLED"] = "1"

from app.core.locale import contains_thai_prose, resolve_locale  # noqa: E402
from app.rules.matcher import RuleMatcher  # noqa: E402
from app.session.context_resolver import resolve_question_with_context  # noqa: E402


def main() -> int:
    english = resolve_locale("How much is one hour on PC?")
    assert english.detected == "en" and english.effective == "en"

    thai = resolve_locale("พีซีหนึ่งชั่วโมงราคาเท่าไหร่")
    assert thai.detected == "th" and thai.effective == "th"

    mixed_thai = resolve_locale("Beat Saber เล่นที่ไหน")
    assert mixed_thai.detected == "mixed" and mixed_thai.effective == "th"

    mixed_english = resolve_locale("Where is VR โซน")
    assert mixed_english.detected == "mixed" and mixed_english.effective == "en"

    forced_english = resolve_locale("มีเกมอะไรบ้าง", requested="en")
    assert forced_english.effective == "en" and forced_english.confidence == 1.0

    forced_thai = resolve_locale("What games are available?", requested="th")
    assert forced_thai.effective == "th" and forced_thai.confidence == 1.0

    follow_up = resolve_locale(
        "and price?",
        recent_history=[{"answer_language": "en"}],
    )
    assert follow_up.effective == "en" and follow_up.reason.startswith("session_followup_en")

    intended_thai = resolve_locale("g]jo", keyboard_layout_direction="thai_intended_english_active")
    assert intended_thai.detected == "th" and intended_thai.effective == "th"

    intended_english = resolve_locale("ฟสสนไำก", keyboard_layout_direction="english_intended_thai_active")
    assert intended_english.detected == "en" and intended_english.effective == "en"

    thai_with_game_title = resolve_locale(
        "TEKKEN 8 คืออะไร",
        keyboard_layout_direction="english_intended_thai_active",
    )
    assert thai_with_game_title.effective == "th", thai_with_game_title

    assert contains_thai_prose("English answer แหล่งเดิม") is True
    assert contains_thai_prose("English answer แหล่งเดิม", allowed_fragments=("แหล่งเดิม",)) is False

    matcher = RuleMatcher([
        {
            "id": "wednesday",
            "priority": 10,
            "category": "schedule",
            "intent": "weekday",
            "patterns": ["wed"],
            "answer_th": "วันพุธ",
            "answer_en": "Wednesday",
        },
        {
            "id": "thai_only",
            "priority": 5,
            "category": "rules",
            "intent": "thai_only",
            "patterns": ["thai only"],
            "answer_th": "คำตอบไทย",
        },
        {
            "id": "booking_th_only",
            "priority": 20,
            "category": "reservation",
            "intent": "booking_th_only",
            "patterns": ["booking test"],
            "answer_th": "คำตอบไทยลำดับสูง",
        },
        {
            "id": "booking_en",
            "priority": 4,
            "category": "reservation",
            "intent": "booking_en",
            "patterns": ["booking test"],
            "answer_th": "คำตอบไทยลำดับต่ำ",
            "answer_en": "English booking answer",
        },
    ])
    assert matcher.match("Are drinks allowed?", locale="en") is None
    assert matcher.match("Open on Wed?", locale="en")["answer"] == "Wednesday"
    assert matcher.match("thai only", locale="en") is None
    assert matcher.match("booking test", locale="en")["rule_id"] == "booking_en"

    resolved = resolve_question_with_context(
        "and controls?",
        [
            {"role": "user", "text": "Can I play Beat Saber?", "answer_language": "en"},
            {
                "role": "assistant",
                "text": "VR Station games include Beat Saber and Horizon Call of the Mountain.",
                "route_category": "games",
                "route_intent": "vr_specific_games",
                "answer_language": "en",
            },
        ],
        locale="en",
    )
    assert resolved.used_context is True
    assert resolved.context_game == "Beat Saber"
    assert resolved.resolved_question == "What are the controls for Beat Saber?"

    gameplay_followup = resolve_question_with_context(
        "How do I play it?",
        [
            {"role": "user", "text": "What is TEKKEN 8?", "answer_language": "en"},
            {"role": "assistant", "text": "TEKKEN 8 is available at the studio.", "answer_language": "en"},
        ],
        locale="en",
    )
    assert gameplay_followup.used_context is True
    assert gameplay_followup.context_game == "TEKKEN 8"
    assert gameplay_followup.resolved_question == "How do I play TEKKEN 8?"

    ambiguous_history = resolve_question_with_context(
        "and controls?",
        [
            {"role": "user", "text": "What games are available in VR?", "answer_language": "en"},
            {
                "role": "assistant",
                "text": "VR games include Beat Saber and Horizon Call of the Mountain.",
                "route_category": "games",
                "answer_language": "en",
            },
        ],
        locale="en",
    )
    assert ambiguous_history.used_context is False
    assert ambiguous_history.resolved_question == "and controls?"

    os.environ["PSU_BILINGUAL_EN_ENABLED"] = "0"
    disabled = resolve_locale("What games are available?", requested="en")
    assert disabled.detected == "en" and disabled.effective == "th"
    assert "english_feature_disabled" in disabled.reason
    os.environ["PSU_BILINGUAL_EN_ENABLED"] = "1"

    print("OK bilingual locale resolution, feature flag, target-safe session inheritance, keyboard intent, and token-aware rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
