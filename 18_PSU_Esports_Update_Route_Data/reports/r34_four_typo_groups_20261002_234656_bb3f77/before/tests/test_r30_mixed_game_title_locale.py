import unittest
from app.core.locale import resolve_locale
class R30MixedTitleLocaleTests(unittest.TestCase):
    def test_thai_task_survives_english_function_words_in_source_titles(self):
        for q in ['The Last of Us Part I / Part II ราคาเท่าไหร่', 'Horizon Call of the Mountain ราคาเท่าไหร่', 'The Legend of Zelda: Breath of The Wild ราคาเท่าไหร่', 'It Takes Two ปุ่มอะไรบ้าง']:
            with self.subTest(q=q):self.assertEqual(resolve_locale(q,requested='auto').effective,'th')
    def test_english_sentences_keep_english_with_a_thai_noun(self):
        for q in ['Can I play เกม at the studio?', 'What are the ปุ่ม in The Last of Us Part II?', 'Is The Last of Us Part II available?']:
            with self.subTest(q=q):self.assertEqual(resolve_locale(q,requested='auto').effective,'en')
    def test_explicit_language_toggle_is_preserved(self):
        q='The Last of Us Part I / Part II ราคาเท่าไหร่'
        self.assertEqual(resolve_locale(q,requested='en').effective,'en')
        self.assertEqual(resolve_locale(q,requested='th').effective,'th')
