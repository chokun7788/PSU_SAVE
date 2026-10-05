"""Compare a saved aggregate snapshot with separately confirmed slot facts.
No network, booking writes, or inferred oracle values. Output JSON to stdout.
"""
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timedelta

def compare(snapshot,oracle,snapshot_sha256):
    transport=oracle.get('transport',{})
    result={'transport_http_ok':transport.get('http_ok'), 'occupancy_verified':False,'grade':'pending','errors':[],'checked_slots':0}
    known=oracle.get('oracle',{})
    if oracle.get('collection_status')=='paused_by_user' or not known.get('observed_resources'):
        result['reason']='no_separately_confirmed_occupancy_oracle';return result
    if not known.get('confirmed_by') or known.get('source_snapshot_sha256')!=snapshot_sha256:
        result['errors'].append('unconfirmed_or_mismatched_snapshot');return result
    try:
        observed=datetime.fromisoformat(known['confirmed_at_bangkok'])
        if observed.utcoffset()!=timedelta(hours=7):raise ValueError('explicit Thai offset required')
    except (KeyError,ValueError,TypeError):
        result['errors'].append('missing_thai_confirmation_timestamp');return result
    if known.get('date')!=snapshot.get('date'):
        result['errors'].append('wrong_snapshot_date');result['grade']='failed';return result
    resources={str(r.get('resource_id')):r for r in snapshot.get('resources',[])}
    seen=set()
    for expected in known['observed_resources']:
        key=(str(expected.get('resource_id')),expected.get('start'),expected.get('end'))
        if key in seen:result['errors'].append('duplicate_oracle_slot:'+str(key));continue
        seen.add(key)
        if expected.get('expected_status') is None or not isinstance(expected.get('expected_available_count'),int):
            result['errors'].append('unconfirmed_slot:'+str(key));continue
        actual=next((s for s in resources.get(key[0],{}).get('slots',[]) if s.get('start')==key[1] and s.get('end')==key[2]),None)
        result['checked_slots']+=1
        if actual is None:result['errors'].append('missing_slot:'+str(key));continue
        if actual.get('status')!=expected['expected_status']:result['errors'].append('wrong_status:'+str(key))
        if actual.get('available_count')!=expected['expected_available_count']:result['errors'].append('wrong_available_count:'+str(key))
    result['grade']='failed' if result['errors'] else 'passed'
    result['occupancy_verified']=bool(result['checked_slots']) and not result['errors']
    result['scope']='Only listed confirmed slots in the exact saved snapshot; no claim for unlisted stations or future times.'
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--snapshot-json',type=Path,required=True);parser.add_argument('--oracle-json',type=Path,required=True)
    args=parser.parse_args();raw=args.snapshot_json.read_bytes();result=compare(json.loads(raw),json.loads(args.oracle_json.read_text(encoding='utf-8-sig')),hashlib.sha256(raw).hexdigest())
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['grade']=='passed' else 2
if __name__=='__main__':raise SystemExit(main())
