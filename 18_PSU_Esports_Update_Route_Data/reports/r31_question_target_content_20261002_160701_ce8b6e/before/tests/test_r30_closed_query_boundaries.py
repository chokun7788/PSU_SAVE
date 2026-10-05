import unittest
from app.core.duration_alternatives import parse_duration_alternatives
from app.pipeline.control_button_target import explicit_button_selection
from app.pipeline.closed_query_improvements import answer_closed_query_improvement
from app.pipeline.service_fee_alternatives import answer_fee_alternatives
from app.pipeline.engine import answer_question_pipeline_debug

class R30BoundaryTests(unittest.TestCase):
    def test_durations_keep_each_unit(self):
        for q,v in [('VR 30 minutes or 1 hour cost?',(30,60)),('PC 1 or 2 hours cost?',(60,120)),('PC หนึ่งชั่วโมงหรือสองชั่วโมงกี่บาท',(60,120)),('PC 1.5 hours and 2.5 hours cost?',(90,150))]:
            with self.subTest(q=q):self.assertEqual(parse_duration_alternatives(q).minutes,v)
    def test_dates_clocks_ids_and_ranges_not_choices(self):
        for q in ['PC1 or PC2 price?','PC 9:00 or 10:00 cost?','PC on 2026-10-01 or 2026-10-02 price?','PC 1-2 hours price?','PC 1 hour price?']:
            with self.subTest(q=q):self.assertIsNone(parse_duration_alternatives(q))
    def test_multiple_services_do_not_get_mixed(self):
        self.assertIsNone(answer_fee_alternatives('How much do PC and PS5 cost for 1 or 2 hours?','en'))
    def test_button_identifier_never_corrected_to_other_number(self):
        rows=[{'button':'R1','action_en':'shoot'},{'button':'R2','action_en':'jump'}]
        self.assertEqual(explicit_button_selection('What does the R2 button do?',rows).rows,(rows[1],))
        self.assertEqual(explicit_button_selection('What does the R9 button do?',rows).rows,())
    def test_unique_typo_on_named_button(self):
        rows=[{'button':'Options','action_en':'Pause'},{'button':'Cross','action_en':'Jump'}]
        self.assertEqual(explicit_button_selection('What does the Optinos button do?',rows).rows,(rows[0],))
    def test_all_controls_remains_a_broad_question(self):
        self.assertIsNone(explicit_button_selection('What are all controls for Gran Turismo 7?',[]))
    def test_negated_duration_clarifies(self):
        for q,l in [('PC ไม่เอา 1 หรือ 2 ชั่วโมงคิดราคาเท่าไร','th'),('How much is PC for not 1 or 2 hours?','en')]:
            with self.subTest(q=q):self.assertEqual(answer_closed_query_improvement(q,l)[0],'clarification')
    def test_unknown_button_returns_no_mapping(self):
        for q,l in [('ปุ่ม R9 ใน Gran Turismo 7 ใช้ทำอะไร','th'),('What does the R9 button do in Gran Turismo 7?','en')]:
            with self.subTest(q=q):
                r=answer_question_pipeline_debug(q,locale=l,experimental_allow_llm=False,experimental_rag_fallback=True)
                self.assertIn('no_answer',r.mode);self.assertNotIn('Accelerate',r.answer);self.assertNotIn('•    R2:',r.answer)
    def test_booking_service_is_catalog_not_occupancy(self):
        for q,l in [('ต้องจองอะไรถ้าจะเล่น Beat Saber','th'),('What do I need to book to play Beat Saber?','en')]:
            with self.subTest(q=q):
                category,r=answer_closed_query_improvement(q,l)
                self.assertEqual(category,'reservation');self.assertTrue(r.evidence['catalog_only']);self.assertIn('VR',r.answer)
    def test_missing_original_media_policy_is_not_translation_gap(self):
        for q,l in [('ถ่ายวิดีโอภายในศูนย์ได้ไหม','th'),('Can I record a video inside the studio?','en')]:
            with self.subTest(q=q):
                _,r=answer_closed_query_improvement(q,l);self.assertTrue(r.evidence['not_a_translation_gap']);self.assertEqual(r.hits,[])
