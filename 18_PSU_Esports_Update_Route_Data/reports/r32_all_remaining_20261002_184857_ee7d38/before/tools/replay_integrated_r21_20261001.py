"""Replay every r20 failure with the new runtime; preserve the original trace."""
from __future__ import annotations
import argparse
from dataclasses import asdict
import hashlib
import json
import os
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
sys.dont_write_bytecode=True

def read(p):return [json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--locale',choices=('th','en'),required=True)
    ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    if a.output.exists():ap.error('Refusing to overwrite evidence')
    os.environ.update(PSU_PERFORMANCE_TRACE='0',PSU_LIVE_BOOKING_ENABLED='0')
    from app.pipeline.engine import answer_question_pipeline_debug
    rows=read(ROOT/f'reports/reliability_flow_20261001/paired_{a.locale}_r20_gate.jsonl')
    rows=[r for r in rows if not r['noisy']['passed']]
    paths=sorted((ROOT/'app').rglob('*.py'))+[ROOT/'data/locales/en/CURRENT']
    snapshot={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    with a.output.open('x',encoding='utf-8') as f:
        for i,r in enumerate(rows,1):
            result=answer_question_pipeline_debug(r['noisy_question'],locale=a.locale,experimental_allow_llm=False,experimental_rag_fallback=False,global_timeout_sec=20.0)
            out={'id':r['id'],'locale':a.locale,'domain':r['domain'],'variant':'noisy','question':r['noisy_question'],'replay':asdict(result)}
            f.write(json.dumps(out,ensure_ascii=False,default=str)+'\n');f.flush()
            if i%25==0 or i==len(rows):print(a.locale,i,'/',len(rows),flush=True)
    changed=[path for path,digest in snapshot.items() if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest]
    with a.output.with_suffix('.summary.json').open('x',encoding='utf-8') as f:
        json.dump({'count':len(rows),'source_snapshot':snapshot,'changed_during_replay':changed,'human_review':False,'real_live_oracle':False},f,ensure_ascii=False,indent=2)
    if changed:raise RuntimeError('Runtime changed during replay')

if __name__=='__main__':main()
