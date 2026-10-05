import unittest

from app.session.context_resolver import resolve_question_with_context


def pending(question='ขอกฏการแข่ง', english=False):
    return [
        {'role': 'user', 'text': question},
        {'role': 'assistant', 'route_category': 'competition_rules',
         'route_intent': 'competition_rules_lookup', 'resolved_text': question,
         'text': "Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?" if english else 'ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT'},
    ]


class CompetitionSessionContextR35Tests(unittest.TestCase):
    def test_game_reply_completes_pending_task_in_both_languages(self):
        for locale in ('th', 'en'):
            for title, canonical in (('valorant', 'VALORANT'), ('cs2', 'Counter-Strike 2'), ('RoV', 'Arena of Valor (RoV)'), ('Tekken 8', 'Tekken 8'), ('วาโลครับ', 'VALORANT'), ('แล้ว RoV', 'Arena of Valor (RoV)')):
                with self.subTest(locale=locale, title=title):
                    r=resolve_question_with_context(title,pending('What are the tournament rules?' if locale=='en' else 'ขอกฏการแข่ง',locale=='en'),locale=locale)
                    self.assertTrue(r.used_context)
                    self.assertEqual(r.context_domain,'competition_rules')
                    self.assertEqual(r.context_game,canonical)
                    self.assertIn(canonical,r.resolved_question)
                    self.assertEqual(r.original_question,title)

    def test_pending_retains_facet_year_and_negation(self):
        for q in ('แข่งต้องใช้แผนที่อะไร','กฎแข่งปี 2024 ไม่ใช่ปี 2026','What are the rules about technical pauses for the 2024 tournament?'):
            r=resolve_question_with_context('cs2',pending(q),locale='en' if q.isascii() else 'th')
            self.assertTrue(r.used_context)
            self.assertTrue(r.resolved_question.startswith(q))

    def test_explicit_new_operation_bypasses_pending_task(self):
        for q in ('VALORANT คือเกมอะไร','What is VALORANT?','VALORANT เล่นยังไง','VALORANT ราคาเท่าไร','Is PC1 available at 13:00?','มีเกมอะไรบ้าง','ฉันไม่ต้องการกฎ VALORANT'):
            r=resolve_question_with_context(q,pending(),locale='en' if q.isascii() else 'th')
            self.assertFalse(r.used_context,q)
            self.assertEqual(r.resolved_question,q)

    def test_no_history_keeps_bare_title_as_detail(self):
        for q in ('VALORANT','cs2','RoV','Tekken 8'):
            self.assertFalse(resolve_question_with_context(q,[]).used_context)

    def test_missing_title_in_rules_uses_latest_explicit_game(self):
        for q in ('ขอกฏการแข่ง','Can I see the tournament rules?'):
            h=[{'role':'user','text':'VALORANT คืออะไร'},{'role':'assistant','text':'VALORANT เกมยิง','route_category':'games'}]
            r=resolve_question_with_context(q,h,locale='en' if q.isascii() else 'th')
            self.assertTrue(r.used_context)
            self.assertEqual(r.resolved_question,q+' VALORANT')

    def test_new_game_keeps_competition_facet(self):
        h=[{'role':'user','text':'กฎแข่ง VALORANT ใช้แผนที่อะไรปี 2024'},{'role':'assistant','text':'ไม่พบข้อมูลปีนี้','route_category':'competition_rules','resolved_text':'กฎแข่ง VALORANT ใช้แผนที่อะไรปี 2024'}]
        r=resolve_question_with_context('แล้ว cs2',h)
        self.assertTrue(r.used_context)
        self.assertEqual(r.resolved_question,'กฎแข่ง Counter-Strike 2 ใช้แผนที่อะไรปี 2024')

    def test_context_does_not_jump_back_over_topic_change(self):
        h=pending()+[{'role':'user','text':'เปิดกี่โมง'},{'role':'assistant','text':'ตารางบริการ','route_category':'schedule'}]
        self.assertFalse(resolve_question_with_context('VALORANT',h).used_context)
        self.assertFalse(resolve_question_with_context('ขอกฏการแข่ง',h).used_context)

    def test_multiple_targets_are_not_silently_selected(self):
        h=[{'role':'user','text':'VALORANT กับ Tekken 8 คืออะไร'},{'role':'assistant','text':'สองเกม','route_category':'games'}]
        self.assertFalse(resolve_question_with_context('ขอกฏการแข่ง',h).used_context)
        r=resolve_question_with_context('cs2 กับ RoV',pending())
        self.assertFalse(r.used_context)

    def test_unknown_game_edition_and_studio_policy_do_not_borrow_game(self):
        h=[{'role':'user','text':'VALORANT คืออะไร'},{'role':'assistant','text':'VALORANT เกมยิง','route_category':'games'}]
        for q in ('กฎแข่ง Tekken 7','กฎแข่ง Minecraft','ขอกฎศูนย์','Show the Minecraft tournament rules','ขอกฎ Free Fire'):
            r=resolve_question_with_context(q,h,locale='en' if q.isascii() else 'th')
            self.assertFalse(r.used_context,q)
            self.assertEqual(r.resolved_question,q)

    def test_rejected_turn_cannot_fill_pending(self):
        for field in ('contextEligible','context_eligible'):
            h=pending();h[-1][field]=False
            self.assertFalse(resolve_question_with_context('valorant',h).used_context)

    def test_latest_reply_not_assistant_example_list_supplies_game(self):
        self.assertFalse(resolve_question_with_context('ขอกฏการแข่ง',pending()).used_context)

    def test_resolved_target_is_available_after_short_alias_reply(self):
        h=[{'role':'user','text':'cs2'},{'role':'assistant','text':'กติกา','route_category':'competition_rules','resolved_text':'ขอกฎแข่ง Counter-Strike 2'}]
        r=resolve_question_with_context('ขอกฏการแข่ง',h)
        self.assertTrue(r.used_context)
        self.assertEqual(r.context_game,'Counter-Strike 2')

    def test_recorded_catalogue_reply_selects_rulebook(self):
        from app.pipeline.competition_overview import build_rulebook_catalog
        for locale, q in (('th','มีรายการแข่งอะไรบ้าง'),('en','What tournaments are there?')):
            catalog=build_rulebook_catalog(q,locale)
            self.assertIsNotNone(catalog)
            self.assertEqual(len(catalog.hits),4)
            self.assertIn('does not confirm' if locale=='en' else 'ไม่ได้ยืนยัน',catalog.answer)
            h=[{'role':'user','text':q},{'role':'assistant','text':catalog.answer,'route_category':'competition_rules','route_intent':'competition_rulebook_catalog'}]
            r=resolve_question_with_context('valorant',h,locale=locale)
            self.assertTrue(r.used_context)
            self.assertEqual(r.context_domain,'competition_rules')
            self.assertIn('VALORANT',r.resolved_question)

    def test_specific_or_future_event_is_not_stored_catalogue(self):
        from app.pipeline.competition_overview import build_rulebook_catalog
        for q in ('VALORANT มีรายการแข่งอะไรบ้าง','มีรายการแข่งเดือนหน้าหรือไม่','What tournaments are open for registration?','มีเกมอะไรบ้าง','เกมแข่งแนวไหน'):
            self.assertIsNone(build_rulebook_catalog(q,'th'),q)

    def test_short_overview_is_distinct_from_specific_facet(self):
        from app.pipeline.retrieval import looks_like_broad_competition_rules_query
        self.assertTrue(looks_like_broad_competition_rules_query('ขอกฏการแข่ง VALORANT'))
        self.assertTrue(looks_like_broad_competition_rules_query('กติกาการแข่งขัน VALORANT'))
        self.assertFalse(looks_like_broad_competition_rules_query('VALORANT เปลี่ยนกฎแข่งเองได้ไหม'))
        self.assertFalse(looks_like_broad_competition_rules_query('ขอกฏการแข่ง VALORANT ใช้แผนที่อะไร'))

    def test_known_game_identity_does_not_compete_with_catalogue(self):
        from app.pipeline.engine import answer_question_pipeline_debug
        from unittest.mock import patch
        import os
        with patch.dict(os.environ, {'PSU_BILINGUAL_EN_ENABLED':'1','PSU_SEMANTIC_RETRIEVAL':'0'}):
            r=answer_question_pipeline_debug('VALORANT คือเกมอะไร',locale='th',experimental_allow_llm=False,experimental_rag_fallback=False)
        self.assertEqual(r.route.category,'games')
        self.assertIn('Tactical FPS',r.answer)
        self.assertNotIn('คำถามนี้มีได้หลายความหมาย',r.answer)

    def test_canonical_parenthesized_game_keeps_overview(self):
        from app.pipeline.retrieval import looks_like_broad_competition_rules_query
        self.assertTrue(looks_like_broad_competition_rules_query('ขอกฎการแข่งขัน Arena of Valor (RoV)'))
        self.assertFalse(looks_like_broad_competition_rules_query('Arena of Valor (RoV) เปลี่ยนกฎแข่งเองได้ไหม'))

    def test_switch_from_parenthesized_title_does_not_leave_old_alias(self):
        h=[{'role':'user','text':'RoV'},{'role':'assistant','text':'กติกา','route_category':'competition_rules','resolved_text':'ขอกฎแข่ง Arena of Valor (RoV)'}]
        r=resolve_question_with_context('แล้ว cs2',h)
        self.assertTrue(r.used_context)
        self.assertEqual(r.resolved_question,'ขอกฎแข่ง Counter-Strike 2')
