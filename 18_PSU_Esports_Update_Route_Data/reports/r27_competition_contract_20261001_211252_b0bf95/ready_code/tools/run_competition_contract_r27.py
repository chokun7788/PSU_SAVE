"""Rerunnable bounded clause contracts for the pipeline or an actual web API."""
from __future__ import annotations
import argparse, json, os, re, sys, time, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.run_competition_rules_rag_ground_truth import actual_status

def outline_normalized(text):
    return re.sub(r'\s+',' ',re.sub(r'^(?:\d+(?:\.\d+)+[.)]?|\d+[.)])\s*','',text.strip()).casefold()).strip()

def check_content_contract(case,response):
    answer=response.get('answer') or '';mode=response.get('mode') or '';failures=[]
    if actual_status(answer,mode)!=case['status']:failures.append('outcome_mismatch')
    if response.get('category')!='competition_rules':failures.append('route_mismatch')
    body=re.sub(r'\s+',' ',answer.split('แหล่งข้อมูล:')[0].split('Source:')[0].casefold())
    for clause in case['required_clauses']:
        if outline_normalized(clause) not in body:failures.append('missing_complete_clause:'+clause)
    if case['first_clause']:
        first=outline_normalized(answer.splitlines()[0].removeprefix('คำตอบ: ').removeprefix('Answer: '))
        if not any(first and (outline_normalized(c).startswith(first) or first.startswith(outline_normalized(c))) for c in case['required_clauses']):failures.append('first_line_off_topic')
        hits=response.get('hits') or []
        book=case['source_id'].rsplit('_s',1)[0]
        if not hits or any(book not in str(h.get('id',''))+str(h.get('url',''))+str(h.get('source_url','')) for h in hits):failures.append('wrong_game_evidence')
    if not response.get('valid',True):failures.append('validation_rejected')
    return failures

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--fixture',type=Path,required=True);parser.add_argument('--report',type=Path,required=True);parser.add_argument('--run',required=True);parser.add_argument('--url');parser.add_argument('--llm',action='store_true')
    args=parser.parse_args();os.environ['PSU_BILINGUAL_EN_ENABLED']='1'
    if not args.url:os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
    from app.pipeline.engine import answer_question_pipeline_debug
    data=json.loads(args.fixture.read_text(encoding='utf-8'));cases=data if isinstance(data,list) else data['cases'];records=[]
    with (args.report/(args.run+'_details.jsonl')).open('x',encoding='utf-8') as output:
        for n,case in enumerate(cases,1):
            start=time.perf_counter()
            if args.url:
                payload={'question':case['question'],'locale':case['locale'],'recent_history':[],'experimental_allow_llm':args.llm,'experimental_rag_fallback':True,'debug':True}
                raw=json.load(urllib.request.urlopen(urllib.request.Request(args.url.rstrip('/')+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
                response={'answer':raw['answer'],'mode':raw['mode'],'category':raw['route_category'],'hits':raw.get('sources',[]),'valid':raw.get('validation_ok',True),'raw':raw}
            else:
                result=answer_question_pipeline_debug(case['question'],locale=case['locale'],experimental_allow_llm=args.llm,experimental_rag_fallback=True,global_timeout_sec=20)
                response={'answer':result.answer,'mode':result.mode,'category':result.route.category,'hits':result.hits,'valid':result.validation.ok,'trace':[vars(t) for t in result.trace]}
            failures=check_content_contract(case,response)
            record={'id':case['id'],'anchor':case['anchor'],'question':case['question'],'locale':case['locale'],'mutation':case['mutation'],'passed':not failures,'failures':failures,'elapsed':round(time.perf_counter()-start,4),'response':response}
            records.append(record);output.write(json.dumps(record,ensure_ascii=False)+'\n');output.flush()
            if n%100==0:print(json.dumps({'completed':n,'failed':sum(not r['passed'] for r in records)}),flush=True)
    summary={'total':len(records),'passed':sum(r['passed'] for r in records),'failed_anchors':sorted({r['anchor'] for r in records if not r['passed']}),'max_elapsed':max(r['elapsed'] for r in records),'url':args.url,'llm':args.llm,'scope':'bounded complete-clause and first-line acceptance, not organizer policy confirmation'}
    with (args.report/(args.run+'_summary.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
    print(json.dumps(summary,ensure_ascii=False),flush=True)
    return int(summary['passed']!=summary['total'])

if __name__=='__main__':sys.exit(main())
