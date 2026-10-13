"""Explicit trusted-operator bundle importer; drafts only, no approval/publish."""
import argparse,json
from pathlib import Path
from .store import CommonStore
from .answer import database_path
def import_bundle(store,bundle,*,actor):
    if bundle.get('schema_version')!='studio-content-3.0':raise ValueError('Wrong bundle version')
    sources=bundle.get('sources',[]);records=bundle.get('records',[])
    if not isinstance(sources,list) or not isinstance(records,list) or len(records)>2000:raise ValueError('Bounded source/record lists required')
    if len({r['record_id'] for r in records})!=len(records):raise ValueError('Duplicate input record IDs')
    for item in sources:store.add_source(item['source'],item['snapshot'],actor=actor)
    pending=list(records);saved=[]
    while pending:
        remaining=[];failures={}
        for r in pending:
            try:
                # Existing identity requires explicit revision update through the UI.
                x=store.save(r,actor=actor,expected_version=0);saved.append(x)
            except ValueError as e:remaining.append(r);failures[r['record_id']]=str(e)
        if len(remaining)==len(pending):return {'saved':saved,'pending_errors':failures,'published':False}
        pending=remaining
    return {'saved':saved,'pending_errors':{},'published':False}
def main():
    p=argparse.ArgumentParser();p.add_argument('bundle',type=Path);p.add_argument('--db',type=Path,default=database_path());p.add_argument('--actor',required=True);a=p.parse_args()
    store=CommonStore(a.db);store.initialize();result=import_bundle(store,json.loads(a.bundle.read_text(encoding='utf-8')),actor=a.actor);print(json.dumps(result,ensure_ascii=False,indent=2))
    if result['pending_errors']:raise SystemExit(1)
if __name__=='__main__':main()
