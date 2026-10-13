"""Exercise Windows launcher behavior against a local HTTP oracle, not Ollama."""
import copy,hashlib,json,os,struct,subprocess,sys,tempfile,threading,unittest
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from contextlib import contextmanager

ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT/'deployment_templates/Runtime-Readiness.ps1'
IDENTITY=dict(executable_id=hashlib.sha256(os.path.normcase(os.path.realpath(sys.executable)).encode()).hexdigest()[:16],version=list(sys.version_info[:3]),bits=struct.calcsize('P')*8)
ANSWER=dict(ok=True,validation_ok=True,timed_out=False,route_category='reservation',route_intent='booking_advance_time',mode='pipeline:rule_en',answer='Users must book at least 1 hour before use. Source: https://esports.computing.psu.ac.th/')
TEST_DIR=Path(os.getenv('PSU_CHAT_LOG_DIR') or tempfile.gettempdir())/'launcher_fixtures'
TEST_DIR.mkdir(parents=True,exist_ok=True)
def quote(value):return "'"+str(value).replace("'","''")+"'"
def health(installation='fixture'):
    return dict(ok=True,service='psu-esports-chat-web',runtime=dict(version='r43-fixture',installation_id=installation,python=IDENTITY,local_llm=dict(enabled=True)),warmup=dict(ok=True),llm_preflight=dict(ok=True),pipeline_workers=dict(enabled=True,started=True,workers=[dict(alive=True,ready=True)]))
def ps(code,check=True):
    p=subprocess.run(['powershell.exe','-NoProfile','-ExecutionPolicy','Bypass','-Command',"$ErrorActionPreference='Stop'; . "+quote(HELPER)+'; '+code],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=40)
    if check and p.returncode:raise AssertionError(p.stdout+p.stderr)
    return p
@contextmanager
def fixture(h,b=None,status=200):
    events=[]
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args):pass
        def do_GET(self):self.send(h,200)
        def do_POST(self):
            events.append(json.loads(self.rfile.read(int(self.headers['Content-Length']))));self.send(b or ANSWER,status)
        def send(self,body,status):
            raw=json.dumps(body).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(raw)));self.end_headers();self.wfile.write(raw)
    s=ThreadingHTTPServer(('127.0.0.1',0),Handler);t=threading.Thread(target=s.serve_forever,daemon=True);t.start()
    try:yield s.server_port,events
    finally:s.shutdown();s.server_close();t.join()

@unittest.skipUnless(os.name=='nt','Windows launcher')
class RuntimeReadinessR43Tests(unittest.TestCase):
    def test_server_reports_actual_interpreter_and_memory_snapshot(self):
        from app.web_api.server import _runtime_status
        r=_runtime_status();self.assertEqual(r['python']['executable_id'],IDENTITY['executable_id']);self.assertEqual(r['python']['version'],IDENTITY['version']);self.assertEqual(r['python']['pid'],os.getpid())
        if r['system_memory']['available']:
            self.assertGreaterEqual(r['system_memory']['available_physical_mb'],0);self.assertGreaterEqual(r['system_memory']['available_commit_mb'],0)
    def probe(self,h,b=None,status=200):
        with fixture(h,b,status) as (port,events):
            code=f"$p=Get-ChatbotPython {quote(ROOT)} {quote(sys.executable)}; Invoke-ChatbotReadiness 'http://127.0.0.1:{port}' 'r43-fixture' 'fixture' $p.Identity | ConvertTo-Json -Depth 12 -Compress"
            return json.loads(ps(code).stdout),events
    def test_success_requires_real_post_and_isolated_probe_session(self):
        r,e=self.probe(health());self.assertTrue(r['Ready']);self.assertEqual(len(e),1);self.assertTrue(e[0]['client_session_id'].startswith('startup-probe-'))
    def test_health_ok_but_http_500_does_not_become_ready(self):
        r,e=self.probe(health(),dict(error='server_error'),500);self.assertFalse(r['Ready']);self.assertEqual(r['Stage'],'transport');self.assertEqual(len(e),1)
    def test_http_200_timeout_does_not_become_ready(self):
        r,_=self.probe(health(),{**ANSWER,'timed_out':True});self.assertFalse(r['Ready'])
    def test_http_200_wrong_quantity_does_not_become_ready(self):
        r,_=self.probe(health(),{**ANSWER,'answer':'Book at least 3 hours before use.'});self.assertFalse(r['Ready']);self.assertIn('answer_oracle',r['Reasons'])
    def test_invalid_validation_does_not_become_ready(self):
        r,_=self.probe(health(),{**ANSWER,'validation_ok':False});self.assertFalse(r['Ready'])
    def test_wrong_package_or_interpreter_blocks_post(self):
        for field in ('installation_id','python'):
            h=health();h['runtime'][field]='wrong' if field=='installation_id' else {**IDENTITY,'executable_id':'wrong'}
            with self.subTest(field=field):r,e=self.probe(h);self.assertFalse(r['Ready']);self.assertEqual(e,[])
    def test_failed_warmup_preflight_and_dead_worker_block_post(self):
        for stage in ('warmup','llm_preflight','worker'):
            h=health()
            if stage=='worker':h['pipeline_workers']['workers'][0]['alive']=False
            else:h[stage]['ok']=False
            with self.subTest(stage=stage):r,e=self.probe(h);self.assertFalse(r['Ready']);self.assertEqual(e,[])
    def test_explicit_python_overrides_bad_environment_and_manifest(self):
        with tempfile.TemporaryDirectory(dir=TEST_DIR) as tmp:
            Path(tmp,'package_manifest.json').write_text(json.dumps(dict(python_runtime=dict(path='missing.exe'))))
            p=ps(f"$env:PSU_PYTHON_EXE='also-missing.exe';Get-ChatbotPython {quote(tmp)} {quote(sys.executable)} | ConvertTo-Json -Depth 4 -Compress")
            r=json.loads(p.stdout);self.assertEqual(r['Origin'],'explicit');self.assertEqual(r['Identity']['executable_id'],IDENTITY['executable_id'])
    def test_missing_selected_python_never_silently_falls_back(self):
        p=ps(f"Get-ChatbotPython {quote(ROOT)} 'missing-python.exe'",False);self.assertNotEqual(p.returncode,0);self.assertIn('No silent fallback',p.stderr)
    def test_manifest_binding_is_used_without_path_change(self):
        with tempfile.TemporaryDirectory(dir=TEST_DIR) as tmp:
            Path(tmp,'package_manifest.json').write_text(json.dumps(dict(python_runtime=dict(path=sys.executable))))
            r=json.loads(ps(f"$env:PSU_PYTHON_EXE='';Get-ChatbotPython {quote(tmp)} | ConvertTo-Json -Depth 4 -Compress").stdout)
            self.assertEqual(r['Origin'],'manifest');self.assertEqual(r['Identity']['executable_id'],IDENTITY['executable_id'])
    def test_background_reuses_only_after_oracle_and_keeps_old_logs(self):self.background_case(ANSWER,True)
    def test_background_rejects_bad_existing_answer_and_preserves_process(self):self.background_case({**ANSWER,'answer':'no answer'},False)
    def background_case(self,body,ready):
        with tempfile.TemporaryDirectory(dir=TEST_DIR) as tmp:
            package=Path(tmp)
            for name in ('Runtime-Readiness.ps1','Booking-Dashboard-Probe.ps1','Open-PSU-Esports-Background.ps1'):
                (package/name).write_bytes((ROOT/'deployment_templates'/name).read_bytes())
            (package/'package_manifest.json').write_text(json.dumps(dict(runtime_version='r43-fixture',python_runtime=dict(path=sys.executable))))
            installation=hashlib.sha256(os.path.normcase(str(package.resolve())).encode()).hexdigest()[:16]
            logs=package/'data/logs/launcher';logs.mkdir(parents=True);old=logs/'old.log';old.write_text('preserve')
            with fixture(health(installation),body) as (port,events):
                p=ps(f"& {quote(package/'Open-PSU-Esports-Background.ps1')} -Port {port} -NoBrowser",False)
                self.assertEqual(p.returncode==0,ready,p.stdout+p.stderr);self.assertEqual(len(events),1)
                self.assertEqual(old.read_text(),'preserve');records=list(logs.glob('readiness_*.json'));self.assertEqual(len(records),1)
                record=json.loads(records[0].read_text(encoding='utf-8-sig'));self.assertEqual(record['result']['Ready'],ready);self.assertEqual(record['action'],'reuse')
                # The HTTP fixture remains reachable after a failed gate.
                self.assertTrue(ps(f"(Invoke-RestMethod 'http://127.0.0.1:{port}/health').ok").stdout.strip()=='True')

if __name__=='__main__':unittest.main()
