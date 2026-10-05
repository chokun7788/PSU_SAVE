import threading, time, unittest
from unittest.mock import Mock, patch
from app.web_api.pipeline_supervisor import PipelineWorkerSupervisor, _WorkerSlot

def slot(pid,ready):
    event=threading.Event()
    if ready:event.set()
    process=Mock();process.pid=pid;process.is_alive.return_value=True
    return _WorkerSlot(0,Mock(),Mock(),event,process,threading.Lock())

class PlannedRecycleTests(unittest.TestCase):
    def supervisor(self,old):
        obj=object.__new__(PipelineWorkerSupervisor)
        obj._guard=threading.Lock();obj._slots=[old];obj._performance=Mock();obj._cursor=0
        return obj

    def test_warming_replacement_does_not_remove_available_worker(self):
        old=slot(1,True);pending=slot(2,False);obj=self.supervisor(old)
        with patch.object(obj,'_new_slot',return_value=pending),patch.object(obj,'_stop_slot') as stop:
            obj._maybe_recycle_slot(old)
            self.assertIs(obj._slots[0],old);self.assertIs(old.replacement,pending)
            obj._maybe_recycle_slot(old)
            stop.assert_not_called()
            acquired=obj._acquire_slot(wait_sec=0)
            self.assertIs(acquired,old);acquired.lock.release()

    def test_ready_replacement_is_promoted_before_old_worker_stops(self):
        old=slot(1,True);pending=slot(2,True);old.replacement=pending;obj=self.supervisor(old)
        def stop(current):
            self.assertIs(current,old);self.assertIs(obj._slots[0],pending)
            self.assertIsNone(old.replacement)
        with patch.object(obj,'_stop_slot',side_effect=stop):obj._maybe_recycle_slot(old)
        acquired=obj._acquire_slot(wait_sec=0)
        self.assertIs(acquired,pending);acquired.lock.release()

    def test_failed_warmup_preserves_active_worker_and_bounds_retry(self):
        old=slot(1,True);pending=slot(2,False);old.replacement=pending;old.replacement_started=time.perf_counter()-100;obj=self.supervisor(old)
        with patch.object(obj,'_stop_slot') as stop,patch.object(obj,'_new_slot') as new:
            obj._maybe_recycle_slot(old)
            stop.assert_called_once_with(pending);self.assertIs(obj._slots[0],old)
            self.assertIsNone(old.replacement)
            obj._maybe_recycle_slot(old);new.assert_not_called()

    def test_stale_retired_slot_is_never_returned(self):
        old=slot(1,True);replacement=slot(2,True);obj=self.supervisor(old)
        class SwapLock:
            def __init__(self):self.released=False
            def acquire(self,blocking=False):obj._slots=[replacement];return True
            def release(self):self.released=True
        old.lock=SwapLock()
        acquired=obj._acquire_slot(wait_sec=.1)
        self.assertIs(acquired,replacement);self.assertTrue(old.lock.released)
        acquired.lock.release()
