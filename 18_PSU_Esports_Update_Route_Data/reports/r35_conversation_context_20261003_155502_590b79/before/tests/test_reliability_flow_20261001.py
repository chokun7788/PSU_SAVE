from __future__ import annotations

import os
import json
import unittest
from unittest.mock import patch

from app.booking.live_status import is_live_booking_question, _unavailable
from app.booking.live_status import get_live_booking_status, reset_live_booking_cache
from app.core.intent_cue_recovery import recover_intent_cues
from app.pipeline.engine import answer_question_pipeline_debug
from tests.test_live_booking_typo_fixture_20260930 import snapshot
from tests.smoke_test_live_booking_status import LIVE_PAYLOAD, _Response
from tools.eval_contract_v2 import answer_outcome, rescore_result


# Expectations use existing catalog/FAQ records; these are source-supported
# software checks, not owner-approved ground truth or real booking claims.
CASES = (
    ("catalog-en-delete", "en", "What gmes are available in Cockpit", "games", (("Gran Turismo 7",),), (), False),
    ("catalog-en-duplicate", "en", "What gammes are available in Cockpit now", "games", (("Gran Turismo 7",),), (), False),
    ("catalog-en-swap", "en", "What gaems are available in PS5", "games", (("PlayStation 5", "PS5"),), (), False),
    ("equipment-en-delete", "en", "What equipmnt is available in VR Zone", "equipment", (("VR",),), (), False),
    ("equipment-en-swap", "en", "What equpiment is available in PC Zone", "equipment", (("Gaming Monitor",),), (), False),
    ("catalog-th", "th", "Cockpit มีเกมะไรบ้าง", "games", (("Gran Turismo 7",),), (), False),
    ("booking-information", "en", "What iformation do I need to book", "reservation", (("Student ID",), ("phone number",)), (), False),
    ("booking-information-multi", "en", "What informaton do I need for a bokking", "reservation", (("Student ID",), ("phone number",)), (), False),
    ("payment-deadline", "en", "How long do I have to pay after bokking", "reservation", (("10 minutes",), ("cancel",)), (), False),
    ("payment-multi", "en", "How long do I have to pay after bokking? What informaton do I need to book", "multi_question", (("10 minutes",), ("Student ID",), ("phone number",)), (), False),
    ("drinks-two-errors", "en", "Are drins allowwd", "rules", (("designated areas",),), ("Smoking and alcoholic",), False),
    ("alcohol-negative", "en", "Are alcoholic drins allowwd", "rules", (("prohibited",),), ("allowed only in designated",), False),
    ("game-zone-typo", "en", "Which studio zonw has FINAL FANTASY XVI", "games", (("PlayStation 5 Zone",),), (), False),
    ("compound-th-connector", "th", "บุคคลทั่วไป เล่น PS5 30 นาที เสียกี่บาท อล้วจองยังไง", "multi_question", (("บาท",), ("สลิป",)), (), False),
    ("compound-th-tight", "th", "PS5 ราคาเท่าไหร่อล้วมีเกมอะไรบ้าง", "multi_question", (("บาท",), ("FINAL FANTASY XVI",)), (), False),
    ("compound-th-three", "th", "PS5 ราคาเท่าไหร่ อล้วมีเกมะไรบ้าง แล้วจองยังไง", "multi_question", (("บาท",), ("FINAL FANTASY XVI",), ("สลิป",)), (), False),
    ("compound-en", "en", "How much is PS5 and what gmes are available in PS5", "multi_question", (("THB", "baht"), ("FINAL FANTASY XVI",)), (), False),
    ("live-specific-en", "en", "Is Cockpit 1 availble at 14:00 on 2026-09-30", "schedule", (("Cockpit #1",), ("available",)), ("Cockpit #2",), True),
    ("live-specific-th", "th", "Cockpit เครื่อง 2 ว่างไหม 14:00 วันที่ 2026-09-30", "schedule", (("Cockpit #2",), ("ถูกจอง", "ไม่ว่าง")), ("Cockpit #1",), True),
    ("live-broad-en", "en", "Is Cockpit available at 14:00 on 2026-09-30", "schedule", (("1/2",), ("Cockpit #1: available",), ("Cockpit #2: booked",)), (), True),
    ("live-broad-th", "th", "Cockpit ว่างไหม 14:00 วันที่ 2026-09-30", "schedule", (("1/2",), ("Cockpit #1: ว่าง",), ("Cockpit #2: ถูกจอง",)), (), True),
    ("r19-sofa", "th", "จอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร", "equipment", (("Sofa 2 seats",),), ("TV 86 นิ้ว:",), False),
    ("r19-role", "th", "ตำแหน่ง รอวประธาน คือใร", "overview", (("นายนพัทธ์",), ("รองประธาน",)), ("นายษุภากรณ์",), False),
    ("r19-creator", "th", "คนทำแชทบอทคือใคร", "overview", (("นายภาสวุฒิ",),), ("ผมคือ PSU Esports Assistant",), False),
    ("posttest-two-service-games", "en", "What gaes are available fot PS5 and Nintendo Switch", "multi_question", (("FINAL FANTASY XVI",), ("Mario Kart 8 Deluxe",)), (), False),
    ("posttest-price-session-count", "en", "What is the PC price, and how many sessions van be booked", "multi_question", (("THB", "baht"), ("3 sessions", "3 Sessions")), (), False),
    ("posttest-pay-method", "en", "How do I py for my booking", "reservation", (("bank",),), ("Booking steps:",), False),
    ("posttest-book-verb", "en", "How do I bok a cockpit", "reservation", (("payment slip",),), (), False),
    ("posttest-book-verb-duplicate", "en", "How do I boook a Cockpit", "reservation", (("payment slip",),), (), False),
    ("posttest-conjunction", "en", "How to book Cockpit snd what days is it open", "multi_question", (("payment slip",), ("Monday",)), (), False),
    ("posttest-payment-not-price", "en", "How long do I have to pay after booking PC", "reservation", (("10 minutes",),), ("PSU Student and Staff:",), False),
)


def run_focused_case(case):
    case_id, locale, question, route, groups, forbidden, expected_fetch = case
    with patch("app.runtime.fast_answer.get_live_booking_status", return_value=snapshot()) as fast_fetch, patch(
        "app.pipeline.bilingual_english.get_live_booking_status", return_value=snapshot()
    ) as english_fetch:
        result = answer_question_pipeline_debug(
            question, locale=locale, experimental_allow_llm=False,
            experimental_rag_fallback=False, global_timeout_sec=20,
        )
    fetches = fast_fetch.call_count + english_fetch.call_count
    text = result.answer.casefold()
    failures = []
    if result.route.category != route:
        failures.append(f"route {result.route.category} != {route}")
    for group in groups:
        if not any(term.casefold() in text for term in group):
            failures.append(f"missing group {group}")
    for term in forbidden:
        if term.casefold() in text:
            failures.append(f"forbidden {term}")
    if bool(fetches) != expected_fetch:
        failures.append(f"fetch_count={fetches}, expected_fetch={expected_fetch}")
    if not result.validation.ok:
        failures.append(f"validation: {result.validation.errors}")
    return {
        "id": case_id, "locale": locale, "question": question,
        "expected_route": route, "required_groups": groups, "forbidden": forbidden,
        "expected_live_fetch": expected_fetch, "live_fetches": fetches,
        "route": result.route.category, "mode": result.mode, "answer": result.answer,
        "elapsed_sec": result.elapsed, "passed": not failures, "failures": failures,
        "trace": [vars(item) for item in result.trace],
    }


class ReliabilityFlowTests(unittest.TestCase):
    def test_wrong_date_snapshot_is_not_usable_even_with_http_success(self):
        reset_live_booking_cache()
        try:
            with patch.dict(os.environ, {"PSU_LIVE_BOOKING_ENABLED": "1", "PSU_LIVE_BOOKING_CACHE_SEC": "0"}), patch(
                "app.booking.live_status.urlopen", return_value=_Response(json.dumps(LIVE_PAYLOAD).encode("utf-8"))
            ):
                result = get_live_booking_status("2026-09-30")
            self.assertFalse(result.ok)
            self.assertIn("expected '2026-09-30'", result.error)
        finally:
            reset_live_booking_cache()

    def test_canonical_flag_does_not_swallow_recovered_compound(self):
        for question in ("PS5 ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง", "PS5 ราคาเท่าไหร่ อล้วมีเกมอะไรบ้าง"):
            with self.subTest(question=question), patch.dict(os.environ, {"PSU_CANONICAL_KNOWLEDGE": "1"}), patch(
                "app.knowledge.answer.try_canonical_answer", return_value=None
            ) as canonical:
                result = answer_question_pipeline_debug(
                    question, locale="th", experimental_allow_llm=False, experimental_rag_fallback=False,
                )
                self.assertEqual("multi_question", result.route.category)
                if "อล้ว" in question:
                    canonical.assert_not_called()

    def test_evaluator_does_not_certify_unchecked_content_or_live_claims(self):
        result = {"actual_route": "games", "mode": "pipeline:structured_games_catalog_en",
                  "answer": "anything", "latency_ok": True}
        score = rescore_result(result, ["games"], "answer_available", {})
        self.assertTrue(score["passed"])
        self.assertEqual("content_not_checked", score["evidence_level"])
        self.assertFalse(score["positive_contract_present"])
        self.assertEqual("unknown", answer_outcome("pipeline:new_unclassified_handler", "some answer", "games"))
        score = rescore_result({**result, "actual_route": "schedule",
                                "mode": "pipeline:live_booking_status_unavailable"},
                               ["schedule"], "live_lookup_required", {})
        self.assertTrue(score["passed"])
        self.assertEqual("external_blocked", score["evidence_level"])
        self.assertFalse(score["live_claim_verified"])

    def test_source_supported_focused_cases(self):
        for case in CASES:
            with self.subTest(id=case[0]):
                result = run_focused_case(case)
                self.assertTrue(result["passed"], result["failures"])

    def test_static_live_classifier(self):
        for query in (
            "What gmes are available in Cockpit", "What equipmnt is available in VR Zone",
            "What games are available in Cockpit today", "What games are available now in PS5",
        ):
            with self.subTest(query=query):
                self.assertFalse(is_live_booking_question(query))
        for query in ("Is PC1 available now", "PC11 ว่างไหม", "Cockpit available?", "Is PS5 1 free?"):
            with self.subTest(query=query):
                self.assertTrue(is_live_booking_question(query))

    def test_noisy_unavailable_never_makes_fixture_claim(self):
        with patch("app.runtime.fast_answer.get_live_booking_status", side_effect=lambda date: _unavailable(date, "down")):
            result = answer_question_pipeline_debug(
                "Is Cockpit availble at 14:00 on 2026-09-30", locale="en",
                experimental_allow_llm=False, experimental_rag_fallback=False,
            )
        self.assertIn("unavailable", result.mode)
        self.assertNotIn("1/2", result.answer)

    def test_negative_controls_and_idempotence(self):
        cases = (
            "How do you pay Moving Out 2", "How do you pay for a booking?",
            "Is PC11 available at 09:00 on 2026-09-30", "PC1 ไม่ว่างใช่ไหม 10:00",
            "I like rice and play games", "What does the bottom shelf hold?",
            "PS5 จองแล้วแต่ไม่ได้จ่ายเงิน", "conduct and sportsmanship rules in VALORANT",
            "https://example.test/gaems?q=informtion", "Can I bring alcoholic drinks?",
            "เกม FINAL FANTASY XVI คืออะไร", "PC1/PC11 09:00 10:00 ไม่ใช่นักศึกษา",
            "How do I boot a PC", "How do I boot PS5", "How do I cook on PC",
            "How do I hook a PC", "What games are available far from Cockpit?",
        )
        for raw in cases:
            with self.subTest(raw=raw):
                self.assertEqual(raw, recover_intent_cues(raw))
        for case in CASES:
            once = recover_intent_cues(case[2])
            self.assertEqual(once, recover_intent_cues(once))

    def test_flag_off(self):
        raw = "Are drins allowwd"
        with patch.dict(os.environ, {"PSU_INTENT_CUE_RECOVERY": "0"}):
            self.assertEqual(raw, recover_intent_cues(raw))


if __name__ == "__main__":
    unittest.main()
