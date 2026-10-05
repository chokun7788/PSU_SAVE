import unittest
from tools.check_saved_booking_oracle_r32 import compare
class SavedOracleTests(unittest.TestCase):
 def fixture(self):
  return {'date':'2026-10-01','resources':[{'resource_id':'1','slots':[{'start':'10:00','end':'11:00','status':'busy','available_count':0}]}]}, {'transport':{'http_ok':True},'collection_status':'confirmed_fixture','oracle':{'confirmed_by':'synthetic fixture','confirmed_at_bangkok':'2026-10-01T10:05:00+07:00','source_snapshot_sha256':'hash','date':'2026-10-01','observed_resources':[{'resource_id':'1','start':'10:00','end':'11:00','expected_status':'busy','expected_available_count':0}]}}
 def test_transport_success_without_real_oracle_is_pending(self):
  s,o=self.fixture();o['collection_status']='paused_by_user';r=compare(s,o,'hash');self.assertTrue(r['transport_http_ok']);self.assertFalse(r['occupancy_verified']);self.assertEqual(r['grade'],'pending')
 def test_separately_known_slot_passes(self):
  s,o=self.fixture();self.assertTrue(compare(s,o,'hash')['occupancy_verified'])
 def test_wrong_count_is_detected_despite_successful_transport(self):
  s,o=self.fixture();s['resources'][0]['slots'][0]['available_count']=1;r=compare(s,o,'hash');self.assertEqual(r['grade'],'failed');self.assertFalse(r['occupancy_verified'])
 def test_unbound_oracle_and_wrong_day_are_rejected(self):
  s,o=self.fixture();self.assertFalse(compare(s,o,'different')['occupancy_verified']);s['date']='2026-10-02';self.assertEqual(compare(s,o,'hash')['grade'],'failed')
 def test_timestamp_must_include_thai_offset(self):
  s,o=self.fixture();o['oracle']['confirmed_at_bangkok']='2026-10-01T10:05:00';self.assertFalse(compare(s,o,'hash')['occupancy_verified'])
