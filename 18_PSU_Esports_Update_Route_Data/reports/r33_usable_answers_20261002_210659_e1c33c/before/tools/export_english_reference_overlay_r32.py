"""Export current English reference metadata separately from frozen v2 Gold.
References remain descriptive and are not exact-match answer oracles.
"""
import argparse,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def export(output):
    gold=ROOT/'data/eval/master_ground_truth_en_5000_v2.jsonl';source=ROOT/'data/curated/rule_patterns.jsonl'
    rules={r['id']:r for r in map(json.loads,source.read_text(encoding='utf-8').splitlines()) if r.get('id')}
    changes=[]
    for row in map(json.loads,gold.read_text(encoding='utf-8').splitlines()):
        rule=rules.get(row.get('origin_id')) if row.get('origin')=='rule_patterns' else None
        if rule is None:continue
        old=row.get('metadata',{}).get('reference_answer');current=str(rule.get('answer_en') or '')
        if old!=current:changes.append(dict(id=row['id'],origin_id=rule['id'],reference_answer_frozen=old,reference_answer_current=current,reference_answer_is_exact_match_required=False))
    data=dict(overlay_version='english-reference-r32-v1',gold_sha256=hashlib.sha256(gold.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),changes=changes,owner_human_review='not_asserted',usage='Current descriptive reference only; frozen Gold contracts and runtime source policy are not overwritten.')
    with output.open('x',encoding='utf-8') as out:json.dump(data,out,ensure_ascii=False,indent=2)
    return data
def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args();data=export(args.output);print(json.dumps({'changes':len(data['changes']),'output':str(args.output)}))
if __name__=='__main__':main()
