"""One local inference lane shared by Windows worker processes.

OS byte locks are released when a process exits. No owner facts or tokens live
in this file. The per-thread semaphore preserves the existing acquire/release API.
"""
import os,tempfile,time,threading,hashlib
from pathlib import Path
from urllib.parse import urlparse
class SharedModelGate:
 def __init__(self,path=None):
  self.local=threading.BoundedSemaphore(1);self.held=threading.local()
  endpoint=urlparse(os.getenv('OLLAMA_URL','http://127.0.0.1:11434'))
  host='loopback' if endpoint.hostname in {'localhost','127.0.0.1','::1'} else endpoint.hostname
  namespace=hashlib.sha256((str(host)+':'+str(endpoint.port or 80)).encode()).hexdigest()[:16]
  self.path=Path(path) if path else Path(tempfile.gettempdir())/'psu_esports_model_gate'/('ollama_'+namespace+'.lock')
 def acquire(self,blocking=True,timeout=None):
  start=time.monotonic();limit=float('inf') if timeout is None or timeout<0 else max(0,timeout)
  if not blocking:got=self.local.acquire(False)
  else:got=self.local.acquire(timeout=None if limit==float('inf') else limit)
  if not got:return False
  handle=None
  try:
   self.path.parent.mkdir(parents=True,exist_ok=True);handle=self.path.open('a+b');handle.seek(0,2)
   if handle.tell()==0:handle.write(b'0');handle.flush()
   while True:
    try:
     handle.seek(0)
     if os.name=='nt':
      import msvcrt;msvcrt.locking(handle.fileno(),msvcrt.LK_NBLCK,1)
     else:
      import fcntl;fcntl.flock(handle.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
     self.held.handle=handle;return True
    except (OSError,BlockingIOError):
     if not blocking or time.monotonic()-start>=limit:handle.close();self.local.release();return False
     time.sleep(min(.02,max(0,limit-(time.monotonic()-start))))
  except OSError:
   if handle:handle.close()
   self.local.release();return False
 def release(self):
  handle=getattr(self.held,'handle',None)
  if handle is None:raise RuntimeError('Model gate not held by this thread')
  try:
   handle.seek(0)
   if os.name=='nt':
    import msvcrt;msvcrt.locking(handle.fileno(),msvcrt.LK_UNLCK,1)
   else:
    import fcntl;fcntl.flock(handle.fileno(),fcntl.LOCK_UN)
  finally:
   handle.close();self.held.handle=None;self.local.release()
