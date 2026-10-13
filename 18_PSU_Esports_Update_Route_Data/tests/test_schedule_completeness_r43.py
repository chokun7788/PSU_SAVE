import os,sys,unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0')
from app.pipeline.bilingual_english import _answer_schedule,_regular_week_summary_en
from app.pipeline.schemas import EntityBundle
from app.calendar.service_calendar import ClosureInfo
from app.pipeline.engine import answer_question_pipeline_debug

class ScheduleCompletenessR43Tests(unittest.TestCase):
    def test_generic_opening_questions_include_every_day_and_lunch(self):
        for q in ('What are the studio opening hours?','When is the studio open?','Opening timetable please','What is the service schedule?','What days are available?','Please list opening hours for every day.','Show service hours for all days'):
            with self.subTest(q=q):
                r=answer_question_pipeline_debug(q,locale='en',experimental_allow_llm=False)
                for name in ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'):
                    self.assertIn(name+':',r.answer)
                self.assertIn('12:00-13:00',r.answer);self.assertIn('not live device availability',r.answer);self.assertEqual(r.route.category,'schedule')
    def test_monday_and_friday_maintenance_have_correct_windows(self):
        text=_regular_week_summary_en();m=next(s for s in text.splitlines() if 'Monday:' in s);f=next(s for s in text.splitlines() if 'Friday:' in s)
        self.assertIn('09:00-12:00 is maintenance',m);self.assertIn('13:00-16:00 is open',m)
        self.assertIn('09:00-12:00 is open',f);self.assertIn('13:00-16:00 is maintenance',f)
    def test_changed_calendar_fixture_is_reflected_without_hardcoded_windows(self):
        slots=[dict(time_range='10:00-11:00',state='open')]
        with patch('app.pipeline.bilingual_english.regular_service_slots',return_value=slots):
            text=_regular_week_summary_en();self.assertEqual(text.count('10:00-11:00 is open'),7);self.assertNotIn('09:00-12:00',text)
    def test_specific_day_is_not_replaced_with_whole_week(self):
        r=_answer_schedule('Monday opening hours',EntityBundle());self.assertIn('09:00-12:00 is maintenance',r.answer);self.assertNotIn('Tuesday:',r.answer)
    def test_monday_morning_and_friday_afternoon_stay_unavailable(self):
        for q in ('Monday morning opening hours','Friday afternoon opening hours'):
            r=_answer_schedule(q,EntityBundle());self.assertIn('maintenance',r.answer);self.assertIn('not a regular play session',r.answer)
    def test_special_closure_still_overrides_regular_day(self):
        closed=ClosureInfo('2026-10-06','fixture closed','closed','fixture','fixture')
        with patch('app.pipeline.bilingual_english.closure_for',return_value=closed):
            r=_answer_schedule('Opening hours on 2026-10-06',EntityBundle());self.assertIn('closed due to a registered special closure',r.answer);self.assertIn('overrides',r.answer)
    def test_public_holiday_not_automatically_closure(self):
        text=_regular_week_summary_en();self.assertIn('public holiday alone does not automatically close',text)
    def test_weather_not_routed_as_schedule(self):self.assertIsNone(_answer_schedule('weather tomorrow',EntityBundle()))
    def test_explicit_schedule_leaves_active_price_task(self):
        from app.session.conversation_plan import resolve_request_plan
        active=resolve_request_plan('PC prices for external users',locale='en')['tasks'][0]
        self.assertIsNone(resolve_request_plan('Please list opening hours for every day.',active_task=active,locale='en'))
        self.assertIsNone(resolve_request_plan('Show service hours for all days',active_task=active,locale='en'))
    def test_all_services_with_duration_still_fills_price_task(self):
        from app.session.conversation_plan import resolve_request_plan
        active=resolve_request_plan('PC prices for external users',locale='en')['tasks'][0]
        p=resolve_request_plan('all services 2 hours',active_task=active,locale='en')
        self.assertEqual(p['tasks'][0]['domain'],'service_fee');self.assertEqual(p['tasks'][0]['filters']['duration_minutes'],120)
        self.assertEqual(len(p['tasks'][0]['targets']),5)
    def test_bare_all_without_context_remains_clarification(self):
        from app.session.conversation_plan import resolve_request_plan
        self.assertEqual(resolve_request_plan('all',locale='en')['missing'],'scope')

if __name__=='__main__':unittest.main()
