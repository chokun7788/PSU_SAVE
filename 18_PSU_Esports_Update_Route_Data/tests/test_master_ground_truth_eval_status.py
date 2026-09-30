from __future__ import annotations

import unittest

from tools.run_master_ground_truth_eval import actual_status


class MasterGroundTruthEvalStatusTests(unittest.TestCase):
    def test_unverified_equipment_and_unavailable_booking_are_not_answers(self) -> None:
        self.assertEqual(actual_status("pipeline:equipment_spec_unverified_en", "GPU model not verified"), "no_answer")
        self.assertEqual(actual_status("pipeline:live_booking_status_unavailable", "ยังยืนยันสถานะสดไม่ได้"), "no_answer")
        self.assertEqual(actual_status("pipeline:live_booking_status_unavailable", "Cannot confirm live status"), "no_answer")


if __name__ == "__main__":
    unittest.main()
