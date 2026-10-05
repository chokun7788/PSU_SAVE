"""Check the immutable package through HTTP with the real input guard.

This isolates deterministic behavior and does not certify LLM assistance or
real WordPress booking state. It terminates only the child it created.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import time
from urllib.request import Request,urlopen
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tests.test_integrated_improvement_r21_20261001 import CASES

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--package',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);ap.add_argument('--port',type=int,default=8096);a=ap.parse_args()
    outputs=[a.output,a.output.with_suffix('.health.json'),a.output.with_suffix('.server.log'),a.output.with_suffix('.summary.json')]
    if any(p.exists() for p in outputs):ap.error('Refusing to overwrite evidence')
    package=a.package.resolve();base=f'http://127.0.0.1:{a.port}'
    with socket.socket() as probe:probe.bind(('127.0.0.1',a.port))
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PSU_RUNTIME_VERSION':'2026.10.01-integrated-r21',
         'PSU_RUNTIME_PROFILE':'r21-package-deterministic-api-check','PSU_LOCAL_LLM_ASSIST_ENABLED':'0',
         'PSU_PIPELINE_WORKER_SUPERVISOR':'0','PSU_LLM_PREFLIGHT':'0','PSU_PIPELINE_WARMUP':'0',
         'PSU_LIVE_BOOKING_ENABLED':'0','PSU_PERFORMANCE_TRACE':'0','PSU_BILINGUAL_EN_ENABLED':'1',
         'PSU_MODEL_FIRST_FLOW':'0','PSU_SEMANTIC_RETRIEVAL':'0','PSU_RAG_LLM_COMPOSER':'0',
         'PSU_INPUT_QUALITY_GUARD_ENABLED':'1','PSU_INPUT_QUALITY_GUARD_MODE':'enforce',
         'PSU_INPUT_QUALITY_REPEAT_POLICY':'warn_and_continue',
         'PSU_PRODUCT_BACKEND_TIMEOUT_SEC':'20','PSU_PIPELINE_GLOBAL_TIMEOUT_SEC':'19',
         'PSU_CHAT_LOG_DIR':str(package/'data/logs'),'PSU_CHAT_LOG_SQLITE_PATH':str(package/'data/logs/chat_history.sqlite3')}
    results=[]
    with outputs[2].open('xb') as log:
        child=subprocess.Popen([sys.executable,'-B','-m','app.web_api.server','--host','127.0.0.1','--port',str(a.port)],cwd=package,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            health=None;deadline=time.monotonic()+45
            while time.monotonic()<deadline:
                if child.poll() is not None:raise RuntimeError('Test server exited before readiness')
                try:
                    with urlopen(base+'/health',timeout=1) as response:health=json.loads(response.read())
                    break
                except OSError:time.sleep(.25)
            if health is None:raise RuntimeError('Package API not ready')
            outputs[1].write_text(json.dumps(health,ensure_ascii=False,indent=2),encoding='utf-8')
            if '2026.10.01-integrated-r21' not in json.dumps(health):raise RuntimeError('Wrong runtime served')
            cases=list(CASES)+[
                ('live-disabled-en','en','Is Cockpit available at 14:00 on 2026-10-01','schedule',(('cannot confirm',),),('1/2','Cockpit #1: available'),False),
                ('live-disabled-th','th','Cockpit ว่างไหม 14:00 วันที่ 2026-10-01','schedule',(('ยังยืนยันสถานะ',),),('1/2','Cockpit #1: ว่าง'),False),
            ]
            with a.output.open('x',encoding='utf-8') as f:
                for i,(cid,locale,q,route,groups,forbidden,_) in enumerate(cases,1):
                    started=time.perf_counter()
                    req=Request(base+'/api/chat',method='POST',headers={'Content-Type':'application/json'},data=json.dumps({'question':q,'locale':locale,'client_session_id':f'r21-package-{i}','debug':True}).encode())
                    try:
                        with urlopen(req,timeout=30) as response:status=response.status;result=json.loads(response.read())
                        text=str(result.get('answer') or '')
                        passed=status==200 and result.get('route_category')==route and all(any(term.casefold() in text.casefold() for term in group) for group in groups) and not any(term.casefold() in text.casefold() for term in forbidden)
                        row={'id':cid,'locale':locale,'question':q,'http_status':status,'passed':passed,'result':result,'elapsed_sec':round(time.perf_counter()-started,3)}
                    except Exception as exc:row={'id':cid,'passed':False,'exception':repr(exc)}
                    f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n');f.flush();results.append(row)
                    print(i,'/',len(cases),cid,row['passed'],flush=True)
        finally:
            child.terminate()
            try:child.wait(timeout=10)
            except subprocess.TimeoutExpired:child.kill();child.wait(timeout=10)
    summary={'count':len(results),'passed':sum(r['passed'] for r in results),'test_server_pid':child.pid,'test_server_terminated':child.poll() is not None,'runtime_profile':env['PSU_RUNTIME_PROFILE'],'input_guard':'enforce/warn_and_continue','LLM_assist_tested':False,'real_live_oracle':False}
    with outputs[3].open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
    print(json.dumps(summary));return 0 if all(r['passed'] for r in results) else 1

if __name__=='__main__':raise SystemExit(main())
