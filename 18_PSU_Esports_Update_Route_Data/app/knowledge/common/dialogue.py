"""Server-produced common context; holds IDs/needs, never answer facts."""
import re
from .query_contract import normalize,resolve_fields,broad_request,strip_names
def state_from_answer(answer):
    art=answer.decision_artifact or {};plan=art.get('query_plan',{})
    if art.get('catalog_scope')!='common_published':return None
    return {'schema_version':1,'record_ids':list(plan.get('record_ids',[])),'requested_fields':list(plan.get('requested_fields',[])),'all_fields':bool(plan.get('all_fields')),'release_id':art.get('release_id'),'pending_selection':plan.get('pending_selection')}
def previous_state(history,records):
    for turn in reversed((history or [])[-8:]):
        s=turn.get('common_read_state') if isinstance(turn,dict) and turn.get('role')=='assistant' else None
        if not isinstance(s,dict) or s.get('schema_version')!=1:continue
        ids=s.get('record_ids');fields=s.get('requested_fields')
        if not isinstance(ids,list) or not isinstance(fields,list) or len(ids)>100 or len(fields)>64 or any(not isinstance(x,str) for x in ids+fields):continue
        if ids and all(rid in records for rid in ids):return s
    return None
def changed_domain(question,prior_kinds):
    q=normalize(question)
    if re.search(r'เกม(?:ไหน|อะไร)|\b(?:which|what)\s+games\b',q) and 'game' not in prior_kinds:return True
    if re.search(r'ศูนย์อยู่|ที่ตั้งศูนย์|\bstudio location\b',q) and 'center' not in prior_kinds:return True
    if re.search(r'เปลี่ยนเรื่อง|อีกเรื่อง|\b(?:new topic|different topic)\b',q):return True
    return False
def resolve_state(question,history,records,names,explicit_ids):
    s=previous_state(history,records)
    if not s:return None
    prior=s['record_ids'];kinds={records[rid]['kind'] for rid in prior}
    if changed_domain(question,kinds):return None
    if explicit_ids:
        remainder=strip_names(question,explicit_ids,names)
        if {records[rid]['kind'] for rid in explicit_ids if rid in records}<={'audience'} and not remainder.strip(' ?!.,') and 'amount_minor' in s['requested_fields']:
            return {'record_ids':list(dict.fromkeys([rid for rid in prior if records[rid]['kind']!='audience']+explicit_ids)),'method':'state_audience_selection','previous_fields':s['requested_fields']}
        return None
    q=normalize(question)
    if len(q)>400:return None
    if resolve_fields(q,kinds)[0] or broad_request(q) or re.search(r'อันนี้|แบบนี้|เกมนี้|มัน|แล้ว|\b(?:it|this|that|and|also|then|so)\b',q):return {'record_ids':prior,'method':'typed_common_state','previous_fields':s['requested_fields']}
    return None
