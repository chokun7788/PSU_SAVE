"""Single-operator loopback editor. The OS account owns the capability token.
Never bind this server to a LAN/public interface. Use managed identity for shared admins.
"""
from __future__ import annotations
import argparse,getpass,hashlib,hmac,json,os,secrets,threading,webbrowser
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import urlparse,parse_qs
from .registry import CATALOG,VERSION,template,now,source_errors,validate,content_hash,value
from .store import CommonStore,Conflict
from .answer import CommonAnswerer,database_path
from .build_info import LOADED_BUILD
from app.knowledge.records import canonical_json
HOME=Path(__file__).resolve().parent
MAX_BODY=2*1024*1024

def preview_answer(store,question,*,locale='th',history=None,draft=False):
    """Use the chat's optional local field planner against published facts only."""
    from .planner import plan_fields
    from app.pipeline.request_deadline import request_deadline
    from dataclasses import replace
    enabled=os.getenv('PSU_LOCAL_LLM_ASSIST_ENABLED','1').strip().lower() in {'1','true','yes','on'}
    audits=[]
    original_store=store
    if draft:
        class DraftView:
            def snapshot(self):
                s=original_store.snapshot()
                with original_store.connect() as c:
                    records=original_store.heads(c);sources={sid:pair[0] for sid,pair in original_store.sources(c).items()}
                from .answer import title
                names={rid:list(dict.fromkeys(r['aliases']['th']+r['aliases']['en']+[title(r,'th'),title(r,'en')])) for rid,r in records.items()}
                s={**s,'release':{'records':records,'sources':sources,'names':names},'active':'draft-preview','withdrawn':[],'allow_demo':True}
                return s
            def still_current(self,s):return original_store.snapshot()['epoch']==s['epoch']
        store=DraftView()
    def traced_plan(q,records,ids):return plan_fields(q,records,ids,diagnostic=audits.append)
    with request_deadline(10):
        result=CommonAnswerer(store).answer(question,locale=locale,history=history or [],planner=traced_plan if enabled else None)
    if result is not None:
        updates={'decision_artifact':{**(result.decision_artifact or {}),'draft_preview_only':draft,'preview_llm_enabled':enabled,'planner_audits':audits}}
        if draft:updates['answer']='ทดสอบร่าง — ยังไม่เผยแพร่ / DRAFT PREVIEW — NOT PUBLISHED\n\n'+result.answer
        result=replace(result,**updates)
    return result

def save_owner_record(store,record,expected_version,actor,source_title='ข้อมูลที่เจ้าของกรอกผ่านฟอร์ม',translation_reviewed=False,change_note=None):
    if change_note is not None and (not isinstance(change_note,str) or len(change_note)>1000):raise ValueError('Change note must be text of at most 1000 characters')
    # Attestations are immutable value snapshots, separate from publication approval.
    snapshot=canonical_json({k:f['value'] for k,f in record.get('fields',{}).items() if f.get('status')=='known'})
    sid='owner_'+secrets.token_hex(12)
    source={'source_id':sid,'kind':'owner_document','path':'owner-form://'+sid,'sha256':hashlib.sha256(snapshot.encode('utf-8')).hexdigest(),
            'authority_for':[record['kind']],'observed_at':now(),'trust':'owner_confirmed','public_url':None}
    for key,f in record['fields'].items():
        if f.get('note') is None:f['note']=''
        if f['status']=='known':f['evidence_refs']=[{'source_id':sid,'locator':'/'+key}]
    record.update(revision=expected_version+1,lifecycle='draft',review={'actor_id':None,'reviewed_at':None,'revision_sha256':None})
    if translation_reviewed and record.get('localization',{}).get('en_status')=='reviewed':record['localization']['source_revision_hash']=content_hash(record)
    store.add_source(source,snapshot,actor=actor)
    result=store.save(record,expected_version=expected_version,actor=actor,change_note=change_note)
    return {**result,'record':store.get(result['record_id'])['record'],'source_title':source_title}

def make_handler(store,token,actor,port):
    origins={f'http://127.0.0.1:{port}'}
    class Handler(BaseHTTPRequestHandler):
        protocol_version='HTTP/1.1'
        def log_message(self,fmt,*args):pass # No token/body request logging.
        def reply(self,code,data,ctype='application/json; charset=utf-8'):
            body=json.dumps(data,ensure_ascii=False).encode('utf-8') if isinstance(data,(dict,list)) else data
            self.send_response(code);self.send_header('Content-Type',ctype);self.send_header('Content-Length',str(len(body)))
            self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.send_header('Referrer-Policy','no-referrer')
            self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
            self.end_headers();self.wfile.write(body)
        def allowed(self,auth=True):
            if self.client_address[0]!='127.0.0.1' or self.headers.get('Host')!=f'127.0.0.1:{port}':self.reply(403,{'error':'Loopback host required'});return False
            origin=self.headers.get('Origin')
            if origin and origin not in origins:self.reply(403,{'error':'Origin rejected'});return False
            if auth and not hmac.compare_digest(self.headers.get('Authorization',''), 'Bearer '+token):self.reply(401,{'error':'Open this page using Open-Owner-Content.cmd'});return False
            return True
        def do_GET(self):
            parsed=urlparse(self.path);path=parsed.path
            if path in ('/','/owner.js','/owner.css'):
                if not self.allowed(False):return
                p=HOME/'ui'/({'/':'index.html','/owner.js':'owner.js','/owner.css':'owner.css'}[path])
                return self.reply(200,p.read_bytes(),{'/':'text/html; charset=utf-8','/owner.js':'text/javascript; charset=utf-8','/owner.css':'text/css; charset=utf-8'}[path])
            if not self.allowed():return
            try:
                if path=='/api/registry':return self.reply(200,{'version':VERSION,'catalog':list(CATALOG.values()),'actor':actor,'scope':'local operator','db':str(store.path),'kinds':24})
                if path=='/api/status':
                    snap=store.snapshot();return self.reply(200,{'build':LOADED_BUILD,'active':snap['active'],'epoch':snap['epoch'],'records':store.list_heads(),'published_ids':list((snap['release'] or {}).get('records',{})),'demo':snap['allow_demo']})
                if path=='/api/template':
                    kind=parse_qs(parsed.query).get('kind',[''])[0];draft=template(kind)
                    draft['record_id']=kind+'_'+secrets.token_hex(6)
                    return self.reply(200,draft)
                if path=='/api/edit-context':return self.reply(200,store.edit_context(parse_qs(parsed.query).get('id',[''])[0]))
                if path=='/api/revision':return self.reply(200,store.revision(parse_qs(parsed.query).get('id',[''])[0],int(parse_qs(parsed.query).get('version',['0'])[0])))
                if path=='/api/record':return self.reply(200,store.get(parse_qs(parsed.query).get('id',[''])[0]))
                return self.reply(404,{'error':'Unknown endpoint'})
            except (ValueError,KeyError) as e:return self.reply(400,{'error':str(e)})
        def do_POST(self):
            if not self.allowed():return
            try:
                if self.headers.get('Content-Type','').split(';')[0]!='application/json':raise ValueError('JSON body required')
                length=int(self.headers.get('Content-Length','0'))
                if not 0<length<=MAX_BODY:self.reply(413,{'error':'Request too large or empty'});return
                body=json.loads(self.rfile.read(length));path=urlparse(self.path).path
                if not isinstance(body,dict):raise ValueError('Object required')
                if path=='/api/save':
                    if body.get('attest') is not True:raise ValueError('Confirm that these values come from center information')
                    return self.reply(200,save_owner_record(store,body['record'],body['expected_version'],actor,translation_reviewed=body.get('translation_reviewed') is True,change_note=body.get('change_note')))
                if path=='/api/translate':
                    from .translation import translate_draft
                    from app.pipeline.request_deadline import request_deadline
                    with request_deadline(35):result=translate_draft(body['record'],replace_existing=body.get('replace_existing') is True)
                    return self.reply(200,result)
                if path=='/api/approve':
                    if body.get('confirm') is not True:raise ValueError('Explicit factual review required')
                    store.approve(body['id'],body['version'],body['hash'],actor=actor);return self.reply(200,{'approved':True})
                if path=='/api/publish':
                    release=store.publish(body['ids'],actor=actor,expected_active=body['expected_active'],request_key=body['request_key']);return self.reply(200,{'release_id':release})
                if path=='/api/withdraw':store.withdraw(body['id'],actor=actor);return self.reply(200,{'withdrawn':True})
                if path=='/api/rollback':store.rollback(body['release_id'],actor=actor,expected_active=body['expected_active']);return self.reply(200,{'rolled_back':True})
                if path=='/api/preview':
                    answer=preview_answer(store,body['question'],locale=body.get('locale','th'),history=body.get('history',[]),draft=body.get('draft') is True)
                    from .dialogue import state_from_answer
                    return self.reply(200,{'answer':answer.answer if answer else 'ยังไม่มีรายการที่เผยแพร่ตรงคำถามนี้ / No matching published record','trace':answer.decision_artifact if answer else None,'common_read_state':state_from_answer(answer) if answer else None})
                return self.reply(404,{'error':'Unknown endpoint'})
            except Conflict as e:return self.reply(409,{'error':str(e)})
            except (ValueError,KeyError,TypeError) as e:return self.reply(400,{'error':str(e)})
            except Exception:return self.reply(500,{'error':'Owner store operation failed; original release remains active'})
    return Handler

def main():
    p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8097);p.add_argument('--db',type=Path,default=database_path());p.add_argument('--no-browser',action='store_true');a=p.parse_args()
    if not 1024<=a.port<=65535:raise SystemExit('Invalid owner port')
    token=secrets.token_urlsafe(32);actor=getpass.getuser();store=CommonStore(a.db);store.initialize()
    server=ThreadingHTTPServer(('127.0.0.1',a.port),make_handler(store,token,actor,a.port));server.daemon_threads=True
    url=f'http://127.0.0.1:{a.port}/#token={token}'
    # Capability goes only to the user's browser or the OS-private token file.
    run=store.path.parent/'owner-session.json';tmp=run.with_suffix('.tmp')
    tmp.write_text(json.dumps({'pid':os.getpid(),'port':a.port,'url':url,'db':str(store.path)},ensure_ascii=False),encoding='utf-8');os.replace(tmp,run)
    if not a.no_browser:webbrowser.open(url)
    print(f'Owner content editor on 127.0.0.1:{a.port}; close this process to stop',flush=True)
    try:server.serve_forever()
    finally:
        server.server_close()
        try:
            if json.loads(run.read_text(encoding='utf-8'))['pid']==os.getpid():run.unlink()
        except (OSError,ValueError,KeyError):pass
if __name__=='__main__':main()
