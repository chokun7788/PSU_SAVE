"""Behavioral contracts for clarified selections, editions and negation."""
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1', PSU_SEMANTIC_RETRIEVAL='0', PSU_CANONICAL_KNOWLEDGE='0')
from app.pipeline.control_request import is_generic_control_request, is_booking_button_request
from app.pipeline.game_edition_guard import unsupported_numbered_game
from app.session.context_resolver import resolve_question_with_context as resolve
from app.session.conversation_plan import excluded_services, resolve_request_plan
from app.pipeline.engine import answer_question_pipeline_debug as answer


def pending(operation, locale='en'):
    controls = operation == 'control_lookup'
    return [{'role': 'user', 'text': 'Show me the game controls' if controls else 'What games can I play?'},
            {'role': 'assistant', 'text': 'Which game?' if controls else 'PC, PS5, Nintendo Switch, Cockpit, VR',
             'mode': 'pipeline:game_control_missing_game_context_en' if controls else 'pipeline:structured_games_catalog_en',
             'route_category': 'games', 'route_intent': 'game_control_lookup' if controls else 'games_lookup'}]


class TargetedDialogueR40Tests(unittest.TestCase):
    def test_missing_controls_fast_path_is_bilingual_and_does_not_call_model(self):
        for q, lang in [('Tell me the keyboard controls please','en'), ('List all game buttons','en'),
                        ('ขอดู controls ทั้งหมดหน่อย','th'), ('ช่วยแสดงปุ่มของเกมให้หน่อยค่ะ','th')]:
            with self.subTest(q=q):
                r = answer(q, locale=lang, experimental_allow_llm=False)
                self.assertIn('game_control_missing_game_context', r.mode)
                stage = next(t for t in r.trace if t.stage == 'closed_control_request')
                self.assertEqual(stage.metadata['missing_slots'], ['game'])
                self.assertEqual(stage.metadata['model_calls'], 0)
                self.assertFalse(any(t.stage == 'universal_intent' for t in r.trace))

    def test_control_detector_does_not_steal_named_games_hardware_numbers_or_negation(self):
        for q in ['What are the controls for Minecraft?', 'VALORANT มีปุ่มอะไรบ้าง',
                  'What controller model does the PS5 zone use?', 'คีย์บอร์ดพังต้องทำยังไง',
                  'Where is the booking button?', 'ไม่เอาปุ่ม ขอราคาของ PC',
                  'Show me the controls for TEKKEN IX', 'controls for 2 people']:
            self.assertFalse(is_generic_control_request(q), q)

    def test_booking_navigation_is_not_game_controls(self):
        for q, lang in [('Where is the booking button?', 'en'), ('ปุ่มจองอยู่ตรงไหน', 'th')]:
            self.assertTrue(is_booking_button_request(q))
            r = answer(q, locale=lang, experimental_allow_llm=False)
            self.assertEqual(r.mode, 'pipeline:booking_navigation')
            self.assertIn('/reservation', r.answer)
            self.assertNotIn('structured_game_controls', r.mode)
        self.assertFalse(is_booking_button_request('ไม่เอาปุ่มจอง'))

    def test_multiple_controls_keep_operation_order_and_deduplicate(self):
        r = resolve('VALORANT, VALORANT and Beat Saber', pending('control_lookup'), locale='en')
        plan = r.to_selection_plan()
        self.assertEqual(plan['operation'], 'control_lookup')
        self.assertEqual(plan['targets'], ['VALORANT', 'Beat Saber'])
        self.assertEqual(len(plan['requests']), 2)
        result = answer(r.resolved_question, locale='en', request_plan=plan, experimental_allow_llm=False)
        self.assertEqual(result.mode, 'pipeline:multi_question_splitter')
        self.assertIn('VALORANT controls:', result.answer)
        self.assertIn('Beat Saber', result.answer)
        children = [t for t in result.trace if t.stage == 'multi_question_child']
        self.assertEqual(len(children), 2)
        self.assertTrue(all('control' in t.metadata['mode'] for t in children))

    def test_multiple_catalog_targets_do_not_drop_second_zone(self):
        r = resolve('PC and cockpik please', pending('list'), locale='en')
        self.assertEqual(r.to_selection_plan()['targets'], ['pc', 'cockpit'])
        result = answer(r.resolved_question, locale='en', request_plan=r.to_selection_plan(), experimental_allow_llm=False)
        self.assertIn('PC Zone', result.answer)
        self.assertIn('Cockpit Zone', result.answer)
        self.assertNotIn('PlayStation 5 Zone', result.answer)

    def test_unresolved_catalog_part_requires_confirmation_instead_of_silent_partial(self):
        r = resolve('PC and washing machine', pending('list'), locale='en')
        plan = r.to_selection_plan()
        self.assertEqual(plan['selection_errors'], ['washing machine'])
        result = answer(r.resolved_question, locale='en', request_plan=plan, experimental_allow_llm=False)
        self.assertEqual(result.mode, 'pipeline:games_catalog_selection_clarification')
        self.assertIn('washing machine', result.answer)
        self.assertFalse(any(t.stage == 'multi_question_child' for t in result.trace))

    def test_unknown_thai_selection_preserves_control_operation_without_inventing_title(self):
        r = resolve('มายคราฟต์', pending('control_lookup'), locale='th')
        self.assertTrue(r.used_context)
        self.assertIsNone(r.context_game)
        self.assertEqual(r.context_operation, 'control_lookup')
        result = answer(r.resolved_question, locale='th', experimental_allow_llm=False)
        self.assertIn('unconfirmed', result.mode)
        self.assertNotIn('structured_game_controls', result.mode)

    def test_guard_also_runs_for_each_compound_child(self):
        for unknown in ('Minecraft', 'TEKKEN IX'):
            r = resolve('VALORANT and '+unknown, pending('control_lookup'), locale='en')
            result = answer(r.resolved_question, locale='en', request_plan=r.to_selection_plan(), experimental_allow_llm=False)
            self.assertIn('VALORANT controls:', result.answer)
            self.assertNotIn('TEKKEN 8 controls:', result.answer)
            children = [t for t in result.trace if t.stage == 'multi_question_child']
            self.assertEqual(len(children), 2)
            self.assertIn('unconfirmed', children[1].metadata['mode'])
            self.assertEqual(children[1].metadata['answer_type'], 'no_answer')

    def test_roman_and_arabic_editions_are_preserved(self):
        for q in ('TEKKEN IX controls', 'TEKKEN 9 controls'):
            self.assertEqual(unsupported_numbered_game(q)['normalized_version'], '9')
        for q in ('TEKKEN VIII controls', 'Final Fantasy XVI controls',
                  'Call of Duty: Modern Warfare III controls', 'Tekken I want to play',
                  'VALORANT controls for 2 people for 30 minutes'):
            self.assertIsNone(unsupported_numbered_game(q), q)

    def test_negation_stops_before_new_request_but_still_excludes_real_target(self):
        self.assertEqual(excluded_services('ไม่เอาปุ่ม ขอราคาของ PC'), [])
        self.assertEqual(excluded_services('ไม่เอา PC ขอราคา VR'), ['pc'])
        self.assertEqual(excluded_services('not controls, show PC prices'), [])
        self.assertEqual(excluded_services('except PC but show VR prices'), ['pc'])
        r = resolve('ไม่เอาปุ่ม ขอราคาของ PC', pending('control_lookup'), locale='th')
        self.assertFalse(r.used_context)
        result = answer(r.resolved_question, locale='th', experimental_allow_llm=False)
        self.assertIn('service_fee', result.mode)
        self.assertIn('PC', result.answer)

    def test_explicit_new_operation_and_ineligible_history_do_not_bind_pending_controls(self):
        for q in ('What is VALORANT?', 'VALORANT คืออะไร', 'PC price'):
            self.assertFalse(resolve(q, pending('control_lookup'), locale='en').used_context, q)
        h = pending('control_lookup')
        h[-1]['contextEligible'] = False
        self.assertFalse(resolve('VALORANT and Beat Saber', h, locale='en').used_context)

    def test_single_turn_has_no_synthetic_selection_plan(self):
        self.assertIsNone(resolve('VALORANT controls', [], locale='en').to_selection_plan())

    def test_excess_selections_clarify_without_executing_partial_scope(self):
        for operation, q in [('control_lookup','VALORANT, Beat Saber, Mario Kart 8 Deluxe, TEKKEN 8 and Gran Turismo 7'),
                             ('list','PC, PS5, Nintendo Switch, Cockpit and VR')]:
            r = resolve(q, pending(operation), locale='en')
            self.assertEqual(r.to_selection_plan()['selection_limit'], 4)
            result = answer(r.resolved_question, locale='en', request_plan=r.to_selection_plan(), experimental_allow_llm=False)
            self.assertEqual(result.mode, 'pipeline:dialogue_selection_clarification')
            self.assertIn('up to 4', result.answer)
            self.assertFalse(any(t.stage == 'multi_question_child' for t in result.trace))

    def test_booking_shortcut_does_not_swallow_second_price_operation(self):
        for q,lang in [('Where is the booking button and what are the PC prices?', 'en'),
                       ('ปุ่มจองอยู่ไหนและราคาของ PC เท่าไหร่','th')]:
            self.assertFalse(is_booking_button_request(q))
            self.assertIsNone(resolve_request_plan(q, [], locale=lang))
            from app.session.conversation_store import ConversationStore
            self.assertIsNone(ConversationStore().begin('r40', 'turn', q, locale=lang, history=[])['plan'])
            result = answer(q, locale=lang, experimental_allow_llm=False)
            self.assertEqual(result.mode, 'pipeline:multi_question_splitter')
            children = [t for t in result.trace if t.stage == 'multi_question_child']
            self.assertEqual(len(children), 2)
            self.assertEqual(children[0].metadata['mode'], 'pipeline:booking_navigation')
            self.assertTrue(children[1].decision.startswith('service_fee/'), children[1].decision)
            self.assertIn('/reservation', result.answer)
            self.assertIn('PC', result.answer)

    def test_compound_price_and_controls_preserve_both_orders_and_languages(self):
        for lang, pair in [('en', ('What are the controls for VALORANT', 'what are the PC prices')),
                           ('th', ('VALORANT มีปุ่มอะไรบ้าง', 'PC ราคาเท่าไหร่'))]:
            join = ' and ' if lang == 'en' else ' และ '
            for parts in (pair, pair[::-1]):
                q = join.join(parts)
                self.assertIsNone(resolve_request_plan(q, [], locale=lang))
                result = answer(q, locale=lang, experimental_allow_llm=False)
                self.assertEqual(result.mode, 'pipeline:multi_question_splitter')
                children = [t for t in result.trace if t.stage == 'multi_question_child']
                self.assertEqual(len(children), 2)
                self.assertEqual({t.decision.split('/')[0] for t in children}, {'games','service_fee'})
                self.assertIn('VALORANT', result.answer)
                self.assertIn('PC', result.answer)


if __name__ == '__main__':
    unittest.main()
