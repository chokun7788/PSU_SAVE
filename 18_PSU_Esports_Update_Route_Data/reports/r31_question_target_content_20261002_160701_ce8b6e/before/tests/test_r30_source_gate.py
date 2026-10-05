import unittest
from app.pipeline.schemas import EntityBundle,PipelineRoute
from app.pipeline.validator import validate_answer
class R30SourceGateTests(unittest.TestCase):
    def test_price_claim_still_requires_local_pc_source(self):
        route=PipelineRoute("service_fee","service_fee_query",.98,"fact","medium","test")
        result=validate_answer("PC 1 ชั่วโมงกี่บาท","ราคา PC: 0 บาท",route,EntityBundle(),hits=[],mode="pipeline:structured_service_fee")
        self.assertIn("pc_price_answer_missing_pc_local_update_source",result.errors)
    def test_group_clarification_does_not_claim_a_pc_price(self):
        route=PipelineRoute("clarification","service_fee_query",.98,"clarification","medium","test")
        result=validate_answer("PC 1 ชั่วโมงกี่บาท","กรุณาระบุกลุ่มผู้ใช้ก่อนครับ",route,EntityBundle(),hits=[],mode="pipeline:service_fee_customer_group_clarification")
        self.assertNotIn("pc_price_answer_missing_pc_local_update_source",result.errors)
