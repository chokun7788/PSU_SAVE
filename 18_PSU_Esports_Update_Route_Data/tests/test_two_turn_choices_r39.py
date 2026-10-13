"""Regression oracles for selected operation, topic switches and unsafe choices."""
import os
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0')
from app.session.context_resolver import resolve_question_with_context as resolve
from app.session.conversation_store import ConversationStore

def controls(lang='th'):
    return [{'role':'user','text':'Show me the game controls' if lang=='en' else 'ขอดูปุ่มควบคุมเกม'},
            {'role':'assistant','text':'Which game? Please provide the game title.' if lang=='en' else 'ขอชื่อเกมก่อนครับ',
             'mode':'pipeline:game_control_missing_game_context'+('_en' if lang=='en' else ''),
             'route_category':'games','route_intent':'game_control_lookup'}]

def catalog():
    return [{'role':'user','text':'What games can I play?'},
            {'role':'assistant','text':'PC, PlayStation 5 Zone, Nintendo Switch Zone, Cockpit, VR',
             'mode':'pipeline:structured_games_catalog_en','route_category':'games','route_intent':'games_lookup'}]

def family(control=False):
    return [{'role':'user','text':'What are the controls for Call of Duty?' if control else 'Tell me about Call of Duty'},
            {'role':'assistant','text':'Call of Duty: Modern Warfare III; Call of Duty: Warzone. Which title?',
             'mode':'pipeline:game_family_clarification_en' if control else 'pipeline:structured_games_family_en',
             'route_category':'games','route_intent':'ambiguous_game_controls' if control else 'game_family_clarification'}]

class TwoTurnChoicesTests(unittest.TestCase):
    def test_generic_english_control_paraphrases_ask_game_without_stealing_hardware_or_unknown_title(self):
        from app.pipeline.engine import answer_question_pipeline_debug as answer
        for q in ('Can I see the game controls?','What buttons can I use?','How do I control the game?','Show me the game control'):
            r=answer(q,locale='en',experimental_allow_llm=False)
            self.assertEqual(r.mode,'pipeline:game_control_missing_game_context_en',q)
        for q in ('How many controllers are available?','What are the controls for Minecraft?'):
            r=answer(q,locale='en',experimental_allow_llm=False)
            self.assertNotEqual(r.mode,'pipeline:game_control_missing_game_context_en',q)

    def test_bare_known_and_polite_names_keep_control_operation(self):
        for lang in ('th','en'):
            for q in ('VALORANT','Valoant','the VALORANT one','วาโลครับ'):
                with self.subTest(lang=lang,q=q):
                    r=resolve(q,controls(lang),locale=lang)
                    self.assertTrue(r.used_context)
                    self.assertEqual(r.context_operation,'control_lookup')
                    self.assertEqual(r.context_game,'VALORANT')

    def test_explicit_new_question_exits_controls(self):
        for q,lang in [('VALORANT คืออะไร','th'),('What is VALORANT?','en'),('VALORANT ราคาเท่าไร','th')]:
            r=resolve(q,controls(lang),locale=lang)
            self.assertEqual(r.resolved_question,q)
            self.assertFalse(r.used_context)

    def test_unknown_titles_and_editions_are_not_replaced(self):
        for q in ('TEKKEN 9','TEKKEN 7','PS55','What is Minecraft?'):
            r=resolve(q,controls('en'),locale='en')
            self.assertFalse(r.used_context,q)
            self.assertEqual(r.resolved_question,q)

    def test_unknown_control_choice_keeps_operation_without_confirming_game(self):
        from app.pipeline.engine import answer_question_pipeline_debug as answer
        for lang in ('th','en'):
            r=resolve('Minecraft',controls(lang),locale=lang)
            self.assertTrue(r.used_context)
            self.assertIsNone(r.context_game)
            self.assertEqual(r.context_operation,'control_lookup')
            response=answer(r.resolved_question,locale=lang,experimental_allow_llm=False)
            self.assertNotIn('games_catalog',response.mode)
            self.assertNotIn('structured_game_controls',response.mode)
            self.assertNotIn('missing_game_context',response.mode)

    def test_catalog_accepts_exact_and_bounded_typo_services(self):
        for q,label in [('PS5','PlayStation 5'),('the PS5 one','PlayStation 5'),('cockpik','Cockpit')]:
            r=resolve(q,catalog(),locale='en')
            self.assertTrue(r.used_context)
            self.assertEqual(r.context_operation,'list')
            self.assertIn(label,r.resolved_question)

    def test_catalog_does_not_correct_numbers_or_new_operations(self):
        for q in ('PS55','PS6','What is PS5?','PS5 price','PC1 available?'):
            self.assertFalse(resolve(q,catalog(),locale='en').used_context,q)

    def test_family_details_suffix_selects_offered_title(self):
        r=resolve('Modern Warfare III',family(),locale='en')
        self.assertTrue(r.used_context)
        self.assertEqual(r.context_operation,'game_detail')
        self.assertIn('Modern Warfare III',r.resolved_question)

    def test_family_controls_suffix_retains_controls(self):
        r=resolve('Modern Warfare III',family(True),locale='en')
        self.assertTrue(r.used_context)
        self.assertEqual(r.context_operation,'control_lookup')

    def test_family_choices_do_not_bind_outside_game_or_whole_zone(self):
        for h in (family(),family(True)):
            for q in ('VALORANT','PS5','Modern Warfare II'):
                r=resolve(q,h,locale='en')
                self.assertFalse(r.used_context,q)

    def test_latest_turn_and_rejection_limit_context(self):
        for field in ('contextEligible','context_eligible'):
            for index in (0,1):
                h=controls('en');h[index][field]=False
                self.assertFalse(resolve('VALORANT',h,locale='en').used_context)
        h=controls('en')+[{'role':'user','text':'When do you open?'},{'role':'assistant','text':'Service schedule','route_category':'schedule'}]
        self.assertFalse(resolve('VALORANT',h,locale='en').used_context)
        self.assertFalse(resolve('VALORANT',[],locale='en').used_context)

    def test_english_service_clarification_preserves_selected_operation(self):
        h=[{'role':'user','text':'What does PC have?'},{'role':'assistant','text':'Which topic about PC: games, equipment, prices, or booking?',
             'mode':'pipeline:service_broad_choice_en','route_category':'clarification','route_intent':'service_broad_choice'}]
        for q,fragment in [('games','games'),('equipment','equipment'),('prices','prices'),('fees','prices'),('booking','book')]:
            r=resolve(q,h,locale='en')
            self.assertTrue(r.used_context,q)
            self.assertIn(fragment,r.resolved_question.lower())
            self.assertIn('PC',r.resolved_question)
            self.assertTrue(r.resolved_question.isascii())

    def test_parent_store_preserves_mode_and_isolates_sessions(self):
        s=ConversationStore();h=controls('en');t=s.begin('one','a',h[0]['text'],locale='en')
        self.assertTrue(s.complete('one','a',t['revision'],dict(ok=True,answer=h[1]['text'],mode=h[1]['mode'],route_category='games',route_intent='game_control_lookup',request_id='a')))
        self.assertTrue(resolve('VALORANT',s.history('one'),locale='en').used_context)
        self.assertFalse(resolve('VALORANT',s.history('two'),locale='en').used_context)

    def test_expired_parent_memory_does_not_reuse_target(self):
        clock=[0.0];s=ConversationStore(ttl=10,clock=lambda:clock[0]);h=controls('en');t=s.begin('one','a',h[0]['text'])
        s.complete('one','a',t['revision'],dict(ok=True,answer=h[1]['text'],mode=h[1]['mode'],route_category='games',route_intent='game_control_lookup'))
        clock[0]=11
        self.assertFalse(resolve('VALORANT',s.history('one'),locale='en').used_context)

    def test_entire_pipeline_does_not_replace_unrecorded_numeric_edition(self):
        from app.pipeline.engine import answer_question_pipeline_debug as answer
        for lang in ('th','en'):
            for q in ('TEKKEN 9','Resident Evil 9'):
                r=answer(q,locale=lang,experimental_allow_llm=False)
                self.assertEqual(r.mode,'pipeline:game_edition_unconfirmed')
                self.assertNotIn('TEKKEN 8',r.answer)

    def test_numeric_guard_does_not_block_current_games_durations_or_event_years(self):
        from app.pipeline.game_edition_guard import unsupported_numbered_game
        for q in ('TEKKEN 8','CS2','Mario Kart 8 Deluxe','Gran Turismo 7','Resident Evil 4',
                  'กฎแข่ง TEKKEN 8 ปี 2026','ราคา PC1 2 ชั่วโมง','PS5 มีเกมอะไร','TEKKEN 8 2 hours'):
            self.assertIsNone(unsupported_numbered_game(q),q)

if __name__=='__main__':unittest.main(verbosity=2)
