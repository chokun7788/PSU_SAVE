import unittest,os,copy
from concurrent.futures import ThreadPoolExecutor
from contextvars import copy_context
from unittest.mock import patch
from urllib.error import HTTPError
from app.booking.live_status import get_live_booking_status,booking_request_snapshots,reset_live_booking_cache,render_live_booking_answer
from app.booking.wordpress_status import fetch_wordpress_status,BookingFetchError

def payload(day='2026-10-14'):
    return dict(ok=True,date=day,now=day+' 08:00:00',generated_at=day+' 08:00:00',source='remote_csv_live',center=dict(open=False,reason='',open_periods=[['09:00','12:00'],['13:00','16:00']]),resources=[dict(resource_id='1',resource_name='PC #01',capacity=1,status='available',available_now=1,slots=[dict(start='10:00',end='11:00',status='available',available_count=1,booked_count=0,no_show_count=0)])])

class BookingFaults(unittest.TestCase):
    def setUp(self):
        reset_live_booking_cache();self.env=patch.dict(os.environ,{'PSU_LIVE_BOOKING_ENABLED':'1','PSU_LIVE_BOOKING_FETCH_MODE':'wordpress','PSU_LIVE_BOOKING_CACHE_SEC':'0'});self.env.start()
    def tearDown(self):self.env.stop();reset_live_booking_cache()
    def test_same_answer_uses_one_snapshot_next_answer_refreshes(self):
        with patch('app.booking.wordpress_status.fetch_wordpress_status',return_value=payload()) as fetch:
            with booking_request_snapshots():
                contexts=[copy_context() for _ in range(4)]
                with ThreadPoolExecutor(4) as pool:rows=list(pool.map(lambda c:c.run(get_live_booking_status,'2026-10-14'),contexts))
                self.assertEqual(fetch.call_count,1);self.assertEqual(sum(r.request_reused for r in rows),3)
            with booking_request_snapshots():get_live_booking_status('2026-10-14')
            self.assertEqual(fetch.call_count,2)
    def test_wrong_date_cannot_be_reported_available(self):
        with patch('app.booking.wordpress_status.fetch_wordpress_status',return_value=payload('2026-10-15')):
            s=get_live_booking_status('2026-10-14');self.assertFalse(s.ok);self.assertEqual(s.error_code,'invalid_payload')
            for l,q in [('th','PC1 วันที่2026-10-14 เวลา10โมงว่างไหม'),('en','Is PC1 available on 2026-10-14 at 10:00?')]:
                answer=render_live_booking_answer(q,s,l);self.assertNotIn('1/1',answer)
    def test_sample_is_not_live(self):
        p=payload();p['source']='sample'
        with patch('app.booking.wordpress_status.fetch_wordpress_status',return_value=p):
            s=get_live_booking_status('2026-10-14');self.assertFalse(s.ok);self.assertEqual(s.error_code,'non_live_data')
    def test_failure_not_cached_across_questions(self):
        with patch('app.booking.wordpress_status.fetch_wordpress_status',side_effect=[TimeoutError('upstream'),payload()]) as fetch:
            with booking_request_snapshots():
                a=get_live_booking_status('2026-10-14');b=get_live_booking_status('2026-10-14');self.assertFalse(a.ok);self.assertFalse(b.ok);self.assertEqual(fetch.call_count,1)
            with booking_request_snapshots():self.assertTrue(get_live_booking_status('2026-10-14').ok)
            self.assertEqual(fetch.call_count,2)
    def test_both_exports_required_and_invalid_html_rejected(self):
        appointments='service_id,day,time,duration,status\n'
        for exports in ([('<html>login</html>',{} )],[(appointments,{}),('id,name,duration\n',{})]):
            with self.subTest(exports=exports),patch('booking_dashboard.server.read_url',side_effect=exports):
                with self.assertRaises(BookingFetchError):fetch_wordpress_status('2026-10-14',5)
    def test_http_401_and_timeout_explicit_unavailable(self):
        for error,code in [(HTTPError('https://example.test',401,'unauthorized',{},None),'upstream_unavailable'),(TimeoutError('late'),'timeout')]:
            with self.subTest(code=code),patch('booking_dashboard.server.read_url',side_effect=error):
                with self.assertRaises(BookingFetchError) as caught:fetch_wordpress_status('2026-10-14',5)
                self.assertEqual(caught.exception.code,code)
