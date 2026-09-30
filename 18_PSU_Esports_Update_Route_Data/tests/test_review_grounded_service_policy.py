from __future__ import annotations

import json
import unittest

from app.pipeline.service_policy_claims import POLICY_PATH, get_service_policy_answer
from tools.analyze_review_grounded_400 import _check_protected


class ServicePolicyTests(unittest.TestCase):
    def test_bilingual_claims_share_source_and_expose_basis(self) -> None:
        data = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(set(data["claims"]), {"public_access", "food_bring", "personal_power", "checkin_required"})
        for claim_id, claim in data["claims"].items():
            for variant in claim["answers"]:
                with self.subTest(claim=claim_id, variant=variant):
                    th = get_service_policy_answer(claim_id, locale="th", variant=variant, service="บริการ PC ")
                    en = get_service_policy_answer(claim_id, locale="en", variant=variant, service="a PC station")
                    self.assertIsNotNone(th)
                    self.assertIsNotNone(en)
                    self.assertEqual(th.source_id, en.source_id)
                    self.assertEqual(th.source_url, en.source_url)
                    self.assertEqual(th.basis, en.basis)
                    self.assertNotIn("{service}", th.answer + en.answer)
                    self.assertNotIn("150 บาท", th.answer)

    def test_contract_rejects_inventory_and_generic_no_answer(self) -> None:
        row = {
            "id": "INTENT-TRAP-EN-0401", "locale": "en", "domain": "equipment_access_trap",
            "actual_route": "reservation", "mode": "pipeline:protected_public_access",
            "answer": "Yes. Public visitors can book and use studio services. Source: https://esports.computing.psu.ac.th/",
            "elapsed_sec": 0.1,
        }
        self.assertEqual(_check_protected(row), [])
        row["answer"] = "Verified equipment: PC, VR. Source: https://esports.computing.psu.ac.th/"
        self.assertIn("generic_inventory_or_unverified_fallback", _check_protected(row))
        row["answer"] = "I cannot verify whether outsiders can use equipment."
        self.assertIn("missing_direct_access_answer", _check_protected(row))

    def test_contract_requires_direct_food_answer(self) -> None:
        row = {
            "id": "INTENT-TRAP-TH-0236", "locale": "th", "domain": "food_bring_scope",
            "actual_route": "rules", "mode": "pipeline:protected_food_bring_permission",
            "answer": "นำอาหารหรือเครื่องดื่มเข้ามาได้ เฉพาะพื้นที่ที่ศูนย์กำหนด แหล่งข้อมูล: https://esports.computing.psu.ac.th/",
            "elapsed_sec": 0.1,
        }
        self.assertEqual(_check_protected(row), [])
        row["answer"] = "กฎการใช้บริการทั่วไป แหล่งข้อมูล: https://esports.computing.psu.ac.th/"
        self.assertIn("missing_direct_bring_answer_or_area_limit", _check_protected(row))


if __name__ == "__main__":
    unittest.main()
