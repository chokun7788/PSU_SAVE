import unittest
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard

class GuardContextR29Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.guard=RuntimeInputQualityGuard.from_environment()
        cls.guard.mode='enforce';cls.guard.repeat_policy='warn_and_continue'

    def test_thai_word_and_missing_button_letter_are_not_wrong_layout(self):
        for q in ('ขอข้อมูลเรื่องนำอุปกรณ์ แผ่นเกม คืน','ใเนกม Little Nightmares II บน PlayStation / PS5 ปุ่ม Options ใช้ทำอะไร','ในเกม TEKKEN 8 บน PlayStation / PS5 ปุม R1 ใช้ทำอะไร','ตอนนีเ VR Station ว่างไหม ครบ'):
            self.assertFalse(self.guard.inspect(q).should_short_circuit,q)

    def test_english_typo_in_readable_sentence_can_continue(self):
        for q in ('How do I bok a cockpit','How much does it csot for a general visitor to play VR for 1 hour or 2 hours','Could you please helo me wih this: Where can you play League of Legends','Please answer fom verified studio information: Can I get a refund? I need the official answer'):
            self.assertFalse(self.guard.inspect(q).should_short_circuit,q)

    def test_real_layout_projections_still_ask_for_retyping(self):
        for q in ('g]jo','ขอข้อมูลทีายืนยันได้น่อยครับ: g]jo','ะ้ฟะ รน ฟ ไำืพ','Could you check this using verified information: ะ้ฟะ รน ะฟ ไำืะ'):
            self.assertTrue(self.guard.inspect(q).should_short_circuit,q)

    def test_english_neighbor_needs_sentence_context(self):
        self.assertTrue(self.guard.inspect('wih').should_short_circuit)
        self.assertFalse(self.guard.inspect('Could you help me wih this question?').should_short_circuit)

    def test_values_and_negation_are_not_rewritten(self):
        q='Do not change PC1, 2026-10-03, 13:00 or 30 minutes. Is it available?'
        decision=self.guard.inspect(q)
        self.assertEqual(decision.features.input_text,q)
        self.assertFalse(decision.should_short_circuit)

    def test_thai_member_title_and_noisy_surname_can_continue(self):
        for q in ('รศ.ดร.พันธ์ ทงชุมนุม ทำตำแหน่งอะไร',"Whay is ผศ.ดร.นิวัติ แก้วประดับ's roe",'ผศ.ดร.ณัฐงศ์ ทอวเทพ ทำตำแหน่งอะไร'):
            self.assertFalse(self.guard.inspect(q).should_short_circuit,q)
