import unittest,time
from unittest.mock import patch
from app.pipeline.schemas import PipelineRoute
from app.pipeline.experimental_fallback import build_experimental_fallback
from app.pipeline.engine import AnswerQualityPipeline
class StudioScope(unittest.TestCase):
 def test_general_knowledge_never_uses_free_llm_or_catalog(self):
  route=PipelineRoute('general','general_knowledge_query',1.,'fact','low','scope fixture')
  for q in ('ไก่กับไข่อะไรเกิดก่อนกัน','เย็นนี้กินอะไรดี','Which came first, chicken or egg?','What should I have for dinner?','Explain quantum gravity.','Tell me a birthday cake recipe.'):
   with self.subTest(q=q),patch('app.pipeline.experimental_fallback._call_ollama') as model,patch('app.pipeline.experimental_fallback._retrieve_experimental_rows') as retrieval:
    r=build_experimental_fallback(q,route,started=time.perf_counter(),allow_llm=True)
    self.assertEqual(r.mode,'studio_scope_no_answer');model.assert_not_called();retrieval.assert_not_called()
 def test_entry_generic_creation_and_translation_do_not_call_model(self):
  p=AnswerQualityPipeline()
  for q in ('ช่วยเขียนโพสต์ชวนเพื่อนมาเล่นเกมด้วยกัน 80 คำ','Write an 80 word scene about two friends playing games.','Translate to English: เย็นนี้กินอะไรดี'):
   with self.subTest(q=q),patch('app.pipeline.experimental_fallback._call_ollama') as model:
    r=p.answer(q,locale='th',experimental_allow_llm=True)
    self.assertEqual(r.mode,'pipeline:studio_scope_no_answer');model.assert_not_called()
 def test_studio_missing_source_never_invents_a_general_answer(self):
  route=PipelineRoute('general','detail',.8,'fact','low','scope fixture')
  with patch('app.pipeline.experimental_fallback._retrieve_experimental_rows',return_value=([],['fixture no source'])) as retrieval,patch('app.pipeline.experimental_fallback._general_llm_fallback') as model:
   r=build_experimental_fallback('Does the PSU studio have a swimming pool?',route,started=time.perf_counter(),allow_llm=True)
   retrieval.assert_called_once();model.assert_not_called();self.assertEqual(r.mode,'general_psu_scope_no_answer')

 def test_explicit_meal_choice_not_food_permission(self):
  from app.pipeline.studio_scope import is_explicit_unrelated_task
  for q in ('เย็นนี้กินอะไรดี','What should I eat tonight?','Which came first, chicken or egg?','ช่วยเขียนบทความเรื่องจักรวาล 500 คำ','Tell me a birthday cake recipe.'):
   self.assertTrue(is_explicit_unrelated_task(q))
  for q in ('Can I bring food to the studio?','Where can I eat in the studio?','กินอาหารตรงไหนในศูนย์ได้บ้าง','มีเกม Overcooked ไหม','PC กี่บาท','ทั้งหมด','สวัสดี'):
   self.assertFalse(is_explicit_unrelated_task(q))

 def test_capability_question_does_not_capture_a_service_request(self):
  from app.pipeline.chatbot_identity import is_chatbot_identity_query
  for q in ('What can you help me with?','How can you help me?','What topics can I ask about?'):
   self.assertTrue(is_chatbot_identity_query(q))
  for q in ('Can you help me book PC?','What can staff help me with?','How can you help me fix my PC?'):
   self.assertFalse(is_chatbot_identity_query(q))
