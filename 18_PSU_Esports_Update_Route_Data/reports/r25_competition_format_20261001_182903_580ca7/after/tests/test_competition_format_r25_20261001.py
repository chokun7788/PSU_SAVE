"""Meaning/content acceptance checks read against the recorded source rules.

These are assistant-reviewed tests, not organizer approval of rulebook policy.
"""
import os
import re
import unittest
from unittest.mock import patch

from app.pipeline.competition_overview import build_competition_overview
from app.pipeline.competition_presentation import build_penalty_table
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.retrieval import load_curated_rows


class CompetitionFormatAcceptance(unittest.TestCase):
    def setUp(self):
        self.env = patch.dict(os.environ, {'PSU_BILINGUAL_EN_ENABLED': '1', 'PSU_SEMANTIC_RETRIEVAL': '0'})
        self.env.start()
        self.addCleanup(self.env.stop)

    def answer(self, question, locale):
        result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
        self.assertEqual(result.route.category, 'competition_rules')
        self.assertTrue(result.validation.ok)
        return result

    def test_technical_communication_first_sentence_and_no_other_pause_type(self):
        for locale, question, required in (
            ('th', 'VALORANT technical pause สื่อสารได้ไหม', ('ห้าม', 'สื่อสาร', 'เว้นแต่ได้รับอนุญาต')),
            ('en', 'Can players communicate during a VALORANT technical pause?', ('may not communicate', 'unless permitted')),
        ):
            with self.subTest(locale=locale):
                result = self.answer(question, locale)
                first = result.answer.splitlines()[0]
                self.assertTrue(first.startswith('Answer:' if locale == 'en' else 'คำตอบ:'))
                for term in required:
                    self.assertIn(term, first)
                for term in ('Tactical', 'Overtime', '60', 'Major Bug', '10 นาที', '10 minutes'):
                    self.assertNotIn(term, result.answer)
                self.assertEqual(result.answer.casefold().count('communicate' if locale == 'en' else 'สื่อสาร'), 1)

    def test_unknown_technical_duration_does_not_borrow_tactical_or_emergency(self):
        for locale, question in (
            ('th', 'VALORANT technical pause ได้กี่นาที'),
            ('en', 'How long is a VALORANT technical pause?'),
        ):
            with self.subTest(locale=locale):
                answer = self.answer(question, locale).answer
                self.assertIn('ยังไม่พบข้อกฎ' if locale == 'th' else 'could not find a clause', answer)
                for term in ('60', '2 timeouts', '10 minutes', '10 นาที', 'Tactical'):
                    self.assertNotIn(term, answer)

    def test_cs2_table_contains_all_nine_correct_thai_pairs(self):
        result = self.answer('ขอตารางบทลงโทษ CS2', 'th')
        expected = (
            ('การด่าทอ/ใช้ความรุนแรงทางวาจา', 'ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์'),
            ('การโกงทุกรูปแบบ', 'ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน'),
            ('ดูสตรีมระหว่างแข่ง', 'ปรับแพ้ในแมตช์นั้น'),
            ('หยุดเกมโดยไม่ได้รับอนุญาต', 'ปรับแพ้ในรอบนั้น'),
            ('การใช้บัค', 'ปรับแพ้ในรอบหรือแมตช์นั้น'),
            ('พฤติกรรมผิดจริยธรรม', 'ปรับแพ้ในรอบนั้น → ตัดสิทธิ์'),
            ('เพิกเฉยต่อคำตัดสินของเจ้าหน้าที่', 'ปรับแพ้ในรอบนั้น / ตัดสิทธิ์'),
            ('การพิมพ์แชทในเกมที่ไม่เหมาะสม', 'ปรับแพ้ในรอบหรือแมตช์นั้น'),
            ('การหมิ่นศาสนา', 'แบนถาวร'),
        )
        table = [line for line in result.answer.splitlines() if line.startswith('|')][2:]
        self.assertEqual(len(table), 9)
        self.assertEqual(table, [f'| {left} | {right} |' for left, right in expected])
        self.assertTrue(any(h['id'].endswith('_s55_c01') for h in result.hits))

    def test_cs2_english_table_preserves_pairs_and_continuation_reference(self):
        result = self.answer('Show the CS2 penalty table', 'en')
        table = [line for line in result.answer.splitlines() if line.startswith('|')][2:]
        self.assertEqual(len(table), 9)
        self.assertEqual(table[2], '| Watching streams during gameplay | Loss in that match |')
        self.assertEqual(table[3], '| Stopping the game without permission | Loss in that round |')
        self.assertEqual(table[-1], '| Offensive religious remarks | Permanent ban |')
        self.assertEqual({h['id'].rsplit('_s', 1)[-1] for h in result.hits}, {'54_c01', '55_c01'})

    def test_incomplete_table_cannot_invent_last_penalty(self):
        row = next(row for row in load_curated_rows() if str(row.get('id', '')).endswith('cs2_psu_phuket_2026_s54_c01'))
        with patch('app.pipeline.retrieval.load_curated_rows', return_value=[row]):
            self.assertIsNone(build_penalty_table('CS2 penalty table', 'th', [row]))

    def test_unapproved_english_table_is_not_translated_live(self):
        rows = [row for row in load_curated_rows() if str(row.get('id', '')).endswith('cs2_psu_phuket_2026_s54_c01')]
        with patch('app.pipeline.competition_presentation.approved_localization', return_value=None):
            self.assertIsNone(build_penalty_table('CS2 penalty table', 'en', rows))

    def test_rovs_ipad_answer_is_permission_clause_not_document_heading(self):
        result = self.answer('Can I use a tablet or iPad in the RoV tournament?', 'en')
        first = result.answer.splitlines()[0]
        self.assertIn('may not be used', first)
        self.assertIn('disqualification', first)
        self.assertNotIn('Global Ban', result.answer)
        self.assertNotIn('Disconnection and Rematch', result.answer)

    def test_team_number_is_in_first_english_sentence(self):
        result = self.answer('How many players are in a CS2 team?', 'en')
        self.assertIn('5 players', result.answer.splitlines()[0])
        self.assertTrue(result.answer.startswith('Answer:'))
        self.assertNotIn('Verified Counter', result.answer)

    def test_valorant_penalty_types_keep_all_five_source_conditions_once(self):
        result = self.answer('What do the VALORANT tournament rules say about penalties?', 'en')
        for term in ('Warning', 'Round Rollback', 'Round Loss', 'Map Forfeit', 'Match Forfeit'):
            self.assertEqual(result.answer.count(term), 1, result.answer)
        self.assertIn('intent cannot be determined', result.answer)
        self.assertNotIn('• Penalty types in the game', result.answer)

    def test_thai_english_tekken_settings_match_source_values(self):
        for locale, question, timer in (
            ('th', 'Tekken 8 การตั้งค่าเกมเป็นยังไง', '60 วินาที'),
            ('en', 'What are the Tekken 8 in-game settings?', '60 seconds'),
        ):
            with self.subTest(locale=locale):
                result = self.answer(question, locale)
                self.assertIn('3', result.answer.splitlines()[0])
                self.assertIn(timer, result.answer)
                self.assertNotIn('VALORANT', result.answer)
                self.assertNotIn('•    การตั้งค่าเกม', result.answer)

    def test_overview_uses_stable_categories_with_actual_values(self):
        for locale in ('th', 'en'):
            for game in ('CS2', 'RoV', 'Tekken 8', 'VALORANT'):
                with self.subTest(locale=locale, game=game):
                    result = build_competition_overview(f'{game} tournament rules overview', locale)
                    self.assertIsNotNone(result)
                    self.assertGreaterEqual(len(result.section_ids), 3)
                    self.assertNotIn('English below', result.answer)
                    self.assertNotIn('Update:', result.answer)
                    self.assertRegex(result.answer, r'\*\*[^*]+\*\*\n•')
                    if game == 'VALORANT':
                        for term in ('Technical Pause', 'Tactical Timeout', '60'):
                            self.assertIn(term, result.answer)
                        settings = re.search(r'\*\*(?:Match settings|การตั้งค่าแมตช์)\*\*(.*?)(?:\n\*\*|$)', result.answer, re.S)
                        if settings:
                            self.assertNotIn('timeout', settings[1].casefold())
                    if game == 'RoV':
                        self.assertIn('5 ครั้ง' if locale == 'th' else 'five times', result.answer)
                        self.assertIn('Tablet' if locale == 'th' else 'Tablets', result.answer)
                    if game == 'Tekken 8':
                        self.assertIn('60', result.answer)
                        self.assertIn('ผู้จัดยืนยัน' if locale == 'th' else 'organizer to confirm', result.answer)
                        self.assertIn('ห้ามหยุด' if locale == 'th' else 'no game pausing', result.answer)
                        equipment = re.search(r'\*\*(?:Competition equipment|อุปกรณ์การแข่งขัน)\*\*(.*?)(?:\n\*\*|$)', result.answer, re.S)
                        if equipment:
                            self.assertNotIn('Pause', equipment[1])
                            self.assertNotIn('หยุดเกม', equipment[1])
                    if game == 'CS2':
                        self.assertNotIn('•    หยุดเกมโดยไม่ได้รับอนุญาต', result.answer)


if __name__ == '__main__':
    unittest.main()
