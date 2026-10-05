"""Frozen complete-clause checks for single/composite competition questions."""
import argparse,json,os,re,sys,time,urllib.request,urllib.error
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from tools.run_competition_rules_rag_ground_truth import actual_status

def norm(value):
    return re.sub(r'\s+',' ',re.sub(r'^(?:\d+(?:\.\d+)+[.)]?|\d+[.)])\s*','',value.strip()).casefold()).strip()

def check(case,response):
    errors=[];answer=response.get('answer') or '';mode=response.get('mode') or ''
    status=actual_status(answer,mode);body=norm(answer.split('แหล่งข้อมูล:')[0].split('Source:')[0])
    if response.get('http_status',200)!=200:errors.append('transport_failure')
    if response.get('category')!='competition_rules':errors.append('wrong_category')
    if case['status']=='answer':
        if status!='answer':errors.append('wrong_outcome')
        for clause in case['clauses']:
            if norm(clause) not in body:errors.append('missing_complete_clause:'+clause)
        first=norm((answer.splitlines()[0] if answer else '').removeprefix('Answer: ').removeprefix('คำตอบ: '))
        if not any(first and (norm(c).startswith(first) or first.startswith(norm(c))) for c in case['clauses']):errors.append('first_line_off_topic')
        ids=[str(h.get('id','')).removeprefix('canonical::') for h in response.get('hits',[])]
        if not ids or any(case['sources'][0].rsplit('_s',1)[0] not in i for i in ids):errors.append('wrong_game_source')
    elif case['status']=='conflict':
        marker=r'ขัด|ยืนยัน' if case['locale']=='th' else r'conflict|confirm'
        if not re.search(marker,answer,re.I):errors.append('missing_conflict_notice')
        if not ('pause' in answer.casefold() or 'หยุดเกม' in answer):errors.append('missing_pause_context')
    elif case['status']=='safe_unknown_fee':
        if status!='no_answer' and not re.search(r'(?:ไม่พบ|ยังไม่มี).{0,80}(?:ค่าสมัคร|ข้อมูล)|(?:could not find|not.*recorded|not available|unavailable|not found)',answer,re.I):errors.append('silently_omitted_unknown_fee')
    elif status!=case['status']:errors.append('wrong_outcome:'+status)
    for term in case.get('forbidden',[]):
        if term.casefold() in body:errors.append('unsupported_fact:'+term)
    if not response.get('valid',True):errors.append('validation_rejected')
    return errors

def main():
    p=argparse.ArgumentParser();p.add_argument('--fixture',type=Path,required=True);p.add_argument('--report',type=Path,required=True);p.add_argument('--run',required=True);p.add_argument('--url');p.add_argument('--llm',action='store_true');args=p.parse_args()
    os.environ['PSU_BILINGUAL_EN_ENABLED']='1'
    if not args.url:os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
    from app.pipeline.engine import answer_question_pipeline_debug
    data=json.loads(args.fixture.read_text(encoding='utf-8'));cases=data['cases'];records=[]
    with (args.report/(args.run+'_details.jsonl')).open('x',encoding='utf-8') as output:
        for index,case in enumerate(cases,1):
            started=time.perf_counter()
            if args.url:
                payload={'question':case['question'],'locale':case['locale'],'recent_history':[],'experimental_allow_llm':args.llm,'experimental_rag_fallback':True,'debug':True}
                try:
                    raw=json.load(urllib.request.urlopen(urllib.request.Request(args.url+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
                    response={'answer':raw.get('answer',''),'mode':raw.get('mode',''),'category':raw.get('route_category',''),'hits':raw.get('sources',[]),'valid':raw.get('validation_ok',True),'http_status':200,'raw':raw}
                except urllib.error.HTTPError as exc:
                    response={'answer':'','mode':'http_error','category':'http_error','http_status':exc.code,'valid':False,'raw':exc.read().decode('utf-8')}
                except (urllib.error.URLError,TimeoutError) as exc:
                    response={'answer':'','mode':'transport_error','category':'transport_error','http_status':None,'valid':False,'raw':str(exc)}
            else:
                result=answer_question_pipeline_debug(case['question'],locale=case['locale'],experimental_allow_llm=args.llm,experimental_rag_fallback=True,global_timeout_sec=20)
                response={'answer':result.answer,'mode':result.mode,'category':result.route.category,'hits':result.hits,'valid':result.validation.ok,'trace':[vars(t) for t in result.trace]}
            failures=check(case,response);elapsed=time.perf_counter()-started
            if elapsed>20:failures.append('latency_failure')
            record={'id':case['id'],'anchor':case['anchor'],'locale':case['locale'],'kind':case['kind'],'mutation':case['mutation'],'question':case['question'],'passed':not failures,'failures':failures,'elapsed':round(elapsed,4),'response':response}
            records.append(record);output.write(json.dumps(record,ensure_ascii=False)+'\n');output.flush()
            if index%64==0:print(json.dumps({'completed':index,'failed':sum(not r['passed'] for r in records)}),flush=True)
    groups={}
    for r in records:
        key=r['locale']+'/'+r['kind']+'/'+r['mutation'];g=groups.setdefault(key,{'passed':0,'total':0});g['total']+=1;g['passed']+=r['passed']
    summary={'run':args.run,'total':len(records),'passed':sum(r['passed'] for r in records),'failed_anchors':sorted({r['anchor'] for r in records if not r['passed']}),'failure_types':dict(Counter(f.split(':')[0] for r in records for f in r['failures'])),'groups':groups,'max_elapsed':max(r['elapsed'] for r in records),'url':args.url,'scope':data['scope']}
    with (args.report/(args.run+'_summary.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
    print(json.dumps(summary,ensure_ascii=False),flush=True);return int(summary['passed']!=summary['total'])
if __name__=='__main__':sys.exit(main())
