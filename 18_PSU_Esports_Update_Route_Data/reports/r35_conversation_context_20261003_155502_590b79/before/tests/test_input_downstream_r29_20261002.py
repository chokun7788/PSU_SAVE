import unittest
from app.core.intent_cue_recovery import recover_intent_cues
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.structured_tools import _member_person_match, _member_rows


def answer(q, locale='en'):
    return answer_question_pipeline_debug(q, locale=locale, experimental_allow_llm=False,
                                         experimental_rag_fallback=True, global_timeout_sec=20)


class InputDownstreamR29Tests(unittest.TestCase):
    def test_price_words_can_recover_two_errors_with_values_unchanged(self):
        raw='How muc does it xost for a PSU student to play VR for 1 hour'
        self.assertEqual(recover_intent_cues(raw), raw.replace('muc ', 'much ').replace('xost', 'cost'))
        result=answer(raw)
        self.assertIn('PSU students and staff: 0 THB', result.answer)
        self.assertIn('60 minutes, charged as 1 session', result.answer)

    def test_eligibility_label_and_duration_are_kept_in_compound_price(self):
        result=answer('How much does it cot for a PSU stydent to play Nintendo Switch for 2 hours, and how do I book')
        self.assertIn('120 minutes, charged as 2 session', result.answer)
        self.assertNotIn('General adults:', result.answer)
        self.assertIn('Booking steps:', result.answer)

    def test_alumni_price_does_not_fall_back_to_all_groups(self):
        result=answer('Slumni play Nintendo Switch for one hour. How much des it cost')
        self.assertIn('PSU alumni and students from other institutions: 50 THB',result.answer)
        self.assertIn('PSU alumni and students from other institutions: 100 THB',result.answer)
        self.assertNotIn('General adults:',result.answer)

    def test_booking_verb_in_need_to_frame_keeps_operation(self):
        for typo in ('ook','bok','boook'):
            q=f'What do you need to {typo} to play Beat Saber'
            self.assertEqual(recover_intent_cues(q), q.replace(typo, 'book'))
            self.assertIn('Booking steps:',answer(q).answer)

    def test_valid_words_names_negation_and_numbers_are_not_rewritten(self):
        for q in ('How much does it host for VR', 'How much does it cast for VR',
                  'Alumni play Nintendo Switch for 1 hour', 'How do I cook to play Beat Saber',
                  'How much does PC1 cost on 2026-10-03 at 13:00 for 30 minutes?',
                  'PSU stuff is interesting', 'ผศ.ดร.ณัฐงศ์ ทอวเทพ ทำตำแหน่งอะไร'):
            self.assertEqual(q,recover_intent_cues(q))
        q='How much does it cost for a PSU stydent? I am not a student. VR for 1 hour'
        recovered=recover_intent_cues(q)
        self.assertIn('not a student',recovered)
        self.assertIn('VR for 1 hour',recovered)

    def test_full_name_suggestion_is_conditional_and_source_spelling_is_exact(self):
        q='ผศ.ดร.ณัฐงศ์ ทอวเทพ ทำตำแหน่งอะไร'
        row=_member_person_match(q,list(_member_rows()))
        self.assertEqual('ผศ.ดร.ณัฐพงศ์ ทองเทพ',row['name'])
        self.assertEqual(2,row['_name_suggestion']['distance'])
        result=answer(q,'th')
        self.assertIn('หากหมายถึง ผศ.ดร.ณัฐพงศ์ ทองเทพ',result.answer)
        self.assertIn('ผู้ช่วยอธิการบดีฝ่ายวิชาการ',result.answer)

    def test_name_suggestion_requires_unique_full_span_and_explicit_role(self):
        rows=[{'name':'ผศ.ดร.ณัฐพงศ์ ทองเทพ'}, {'name':'ผศ.ดร.ณัฐงษ์ ทองเทพ'}]
        self.assertIsNone(_member_person_match('ผศ.ดร.ณัฐงศ์ ทอวเทพ ทำตำแหน่งอะไร',rows))
        self.assertIsNone(_member_person_match('ผศ.ดร.สมชาย ใจดี ทำตำแหน่งอะไร',list(_member_rows())))
        self.assertIsNone(_member_person_match('ผศ.ดร.ณัฐงศ์ ทอวเทพ เล่นเกมอะไร',list(_member_rows())))

    def test_vector_control_answer_keeps_secondary_source_review_note(self):
        result=answer('ปุมควบคุมของ Super Mario Odyssey บน Nintendo Switch มีอะไรบ้่ง','th')
        self.assertIn('D-Pad Down',result.answer)
        self.assertIn('ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง',result.answer)


if __name__=='__main__': unittest.main()
