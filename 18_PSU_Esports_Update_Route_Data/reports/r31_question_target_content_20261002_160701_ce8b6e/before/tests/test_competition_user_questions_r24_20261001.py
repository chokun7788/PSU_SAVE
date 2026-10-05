import os
import unittest
from unittest.mock import patch

from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from app.pipeline.competition_overview import build_competition_overview, substantive_lines
from app.pipeline.competition_targets import looks_like_competition_rule_query, resolve_competition_targets
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.preprocess import preprocess_input
from app.pipeline.retrieval import looks_like_broad_competition_rules_query


class CompetitionUserQuestions(unittest.TestCase):
    def test_known_lowercase_codes_do_not_trigger_layout_rejection(self):
        with patch.dict(os.environ, {'PSU_INPUT_QUALITY_GUARD_MODE': 'enforce'}):
            guard = RuntimeInputQualityGuard.from_environment()
        for code in ('cs2', 'CS2', 'ps5', 'pc1'):
            with self.subTest(code=code):
                decision = guard.inspect(f'กฏตอนเเข่ง {code} มีอะไรมั่ง')
                self.assertFalse(decision.should_short_circuit)

    def test_visual_vowel_normalization_keeps_game_and_raw(self):
        raw = 'กฏตอนเเข่ง tekken 8 มีอะไรมั่ง'
        pre = preprocess_input(raw)
        self.assertEqual(pre.raw_query, raw)
        self.assertIn('แข่ง', pre.clean_query)
        self.assertEqual(resolve_competition_targets(pre.clean_query).targets[0].game_id, 'tekken8')
        self.assertTrue(looks_like_competition_rule_query(pre.clean_query))

    def test_broad_and_focused_requests_are_distinct(self):
        self.assertTrue(looks_like_broad_competition_rules_query('กฏตอนแข่งวาโลมีอะไรมั่ง'))
        self.assertFalse(looks_like_broad_competition_rules_query('What rules apply to CS2 technical pause?'))
        self.assertFalse(looks_like_broad_competition_rules_query('กฎ CS2 เรื่องอุปกรณ์มีอะไรบ้าง'))

    def test_metadata_and_headings_are_not_substantive_rules(self):
        self.assertEqual(substantive_lines('Update: 17/02/2026\nEnglish below\nอุปกรณ์และอุปกรณ์ต่อพ่วง\nกฎระเบียบและรูปแบบการแข่งขัน VALORANT'), ())

    def test_overviews_contain_real_clauses_and_same_game_evidence(self):
        for game, rulebook in (('cs2', 'cs2_psu_phuket_2026'), ('rov', 'rov_blueket_2025_men'), ('tekken 8', 'tekken8_psu_esports'), ('วาโล', 'valorant_psu_phuket_2026')):
            with self.subTest(game=game):
                result = build_competition_overview(f'กติกา {game} มีอะไรบ้าง', 'th')
                self.assertIsNotNone(result)
                self.assertGreaterEqual(len(result.section_ids), 3)
                self.assertTrue(all(id.startswith('competition_rules_' + rulebook + '_s') for id in result.section_ids))
                self.assertNotIn('English below', result.answer)
                self.assertNotIn('Update:', result.answer)

    def test_unknown_and_multi_game_overviews_cannot_pick_one_game(self):
        self.assertIsNone(build_competition_overview('Free Fire competition rules?', 'th'))
        self.assertIsNone(build_competition_overview('CS2 and VALORANT rules overview', 'th'))

    def test_pause_overview_keeps_rule_kind_and_allowance(self):
        result = build_competition_overview('กฎแข่งวาโลมีอะไรมั่ง', 'th')
        self.assertIn('Tactical Timeout', result.answer)
        self.assertIn('60 วินาที', result.answer)
        self.assertIn('Technical Pause', result.answer)

    def test_user_questions_enter_competition_not_catalog(self):
        for game in ('cs2', 'rov', 'tekken 8', 'วาโล'):
            with self.subTest(game=game):
                result = answer_question_pipeline_debug(f'กฏตอนเเข่ง {game} มีอะไรมั่ง', locale='th', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
                self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
                self.assertEqual(result.route.category, 'competition_rules')
                self.assertTrue(result.validation.ok)
                self.assertNotIn('42 เกม', result.answer)

    def test_english_overviews_use_recorded_localization(self):
        with patch.dict(os.environ, {'PSU_BILINGUAL_EN_ENABLED': '1'}):
            for game in ('cs2', 'rov', 'tekken 8', 'valorant'):
                with self.subTest(game=game):
                    result = answer_question_pipeline_debug(f'What are the {game} tournament rules?', locale='en', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
                    self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
                    self.assertIn('Selected', result.answer)
                    self.assertTrue(result.validation.ok)

    def test_exact_game_survives_thai_connective_and_typo_recovery(self):
        for query, game in (('อยากทราบว่า สรุปกฎการแข่งขัน cs2 ทั้งหมด ครับ', 'cs2'), ('อยากทราบว่า กติกกา rov มีอะไรบ้าง ครับ', 'rov'), ('สอบถามหน่อยครับ ตาม rulebook อารีน่าออฟเวเลอร์ การหลุดจากเกมหรือการเชื่อมต่อ ต้องทำยังไง ครับ', 'rov')):
            with self.subTest(query=query):
                pre = preprocess_input(query)
                self.assertEqual([t.game_id for t in resolve_competition_targets(pre.clean_query).targets], [game])
                self.assertTrue(looks_like_competition_rule_query(pre.clean_query))

    def test_competition_schedule_cannot_use_booking_schedule(self):
        result = answer_question_pipeline_debug('ตาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางบทลงโทษ ต้องทำยังไง', locale='th', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
        self.assertEqual(result.route.category, 'competition_rules')
        self.assertNotIn('Maintenance', result.answer)

    def test_known_numeric_and_negative_clauses(self):
        # Assertions checked against literal source sections, rather than the
        # runtime selector or a merely correct game title/citation.
        cases = (
            ('CS2 แข่งทีมละกี่คน', ('5 คน',)),
            ('Tekken 8 รูปแบบการแข่งขันเป็นอย่างไร', ('FT2', '60', '3')),
            ('RoV ใช้ Tablet หรือ iPad แข่งได้ไหม', ('ไม่อนุญาต', 'Tablet', 'iPad')),
            ('VALORANT technical pause สื่อสารได้ไหม', ('ห้าม', 'สื่อสาร', 'เว้นแต่ได้รับอนุญาต')),
        )
        for query, expected in cases:
            with self.subTest(query=query):
                result = answer_question_pipeline_debug(query, locale='th', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
                self.assertEqual(result.route.category, 'competition_rules')
                for text in expected:
                    self.assertIn(text, result.answer)


if __name__ == '__main__':
    unittest.main()
