"""Server-produced common context; holds IDs/needs, never answer facts."""
import re
from .query_contract import normalize,resolve_fields,broad_request,strip_names
def state_from_answer(answer):
    art=answer.decision_artifact or {};plan=art.get('query_plan',{})
    if art.get('catalog_scope')!='common_published':return None
    minutes={c['requested_minutes'] for c in plan.get('price_calculations',[]) if type(c.get('requested_minutes')) is int and 0<c['requested_minutes']<=1440}
    constraints={'duration_minutes':next(iter(minutes))} if len(minutes)==1 else {}
    comparison=plan.get('price_comparison')
    return {'schema_version':1,'record_ids':list(plan.get('record_ids',[])),'requested_fields':list(plan.get('requested_fields',[])),'all_fields':bool(plan.get('all_fields')),'release_id':art.get('release_id'),'pending_selection':plan.get('pending_selection'),'scope_ids':plan.get('scope_ids',[]),'operation':'price_comparison' if comparison else plan.get('operation'),'platform':plan.get('platform'),'constraints':constraints,'price_comparison':{k:comparison[k] for k in ('scope_ids','audience_ids','missing','axis') if k in comparison} if isinstance(comparison,dict) else None}
def previous_state(history,records):
    for turn in reversed((history or [])[-8:]):
        s=turn.get('common_read_state') if isinstance(turn,dict) and turn.get('role')=='assistant' else None
        if not isinstance(s,dict) or s.get('schema_version')!=1:continue
        ids=s.get('record_ids');fields=s.get('requested_fields')
        if not isinstance(ids,list) or not isinstance(fields,list) or len(ids)>100 or len(fields)>64 or any(not isinstance(x,str) for x in ids+fields):continue
        if ids and all(rid in records for rid in ids):return s
        comp=s.get('price_comparison')
        if not ids and s.get('operation')=='price_comparison' and isinstance(comp,dict) and all(isinstance(comp.get(k),list) and len(comp[k])<=100 and all(isinstance(rid,str) and rid in records for rid in comp[k]) for k in ('scope_ids','audience_ids')):return s
    return None
def changed_domain(question,prior_kinds):
    q=normalize(question)
    if re.search(r'เกม(?:ไหน|อะไร)|\b(?:which|what)\s+games\b',q) and not prior_kinds.intersection({'game','service','resource','zone'}):return True
    if re.search(r'ศูนย์อยู่|ที่ตั้งศูนย์|\bstudio location\b',q) and 'center' not in prior_kinds:return True
    if re.search(r'เปลี่ยนเรื่อง|อีกเรื่อง|\b(?:new topic|different topic)\b',q):return True
    return False
def resolve_state(question,history,records,names,explicit_ids):
    s=previous_state(history,records)
    if not s:return None
    prior=s['record_ids'];kinds={records[rid]['kind'] for rid in prior}
    if changed_domain(question,kinds):return None
    if 'amount_minor' in s['requested_fields']:
        from .audience_scope import resolve
        audiences,audit=resolve(question,records)
        tail=normalize(question)
        for span in sorted(audit['matched_spans'],key=len,reverse=True):tail=tail.replace(normalize(span),' ')
        framing=r'(?:\s|[?!.,]|แล้ว|ถ้าเป็น|ถ้า|เป็น|งั้น|ล่ะ|ละครับ|ครับ|ค่ะ|คะ|หน่อย|what about|how about|if|as|instead|then|and|for|please|so)*'
        comp=s.get('price_comparison') if s.get('operation')=='price_comparison' else None
        if isinstance(comp,dict):
            roots=[rid for rid in comp.get('scope_ids',[]) if rid in records];groups=[rid for rid in comp.get('audience_ids',[]) if rid in records]
            if audiences and re.fullmatch(framing,tail):
                return {'record_ids':list(dict.fromkeys(roots+groups+audiences)),'method':'state_comparison_selection','previous_fields':['amount_minor'],'query':'price compare'}
            root_ids=[rid for rid in explicit_ids if records[rid]['kind'] in {'service','resource','zone','game'}]
            if root_ids and re.fullmatch(framing,strip_names(question,root_ids,names)):
                return {'record_ids':list(dict.fromkeys(root_ids+groups)),'method':'state_comparison_selection','previous_fields':['amount_minor'],'query':'price compare'}
        if audiences and re.fullmatch(framing,tail):
            return {'record_ids':list(dict.fromkeys([rid for rid in prior if records[rid]['kind']!='audience']+audiences)),'method':'state_audience_selection','previous_fields':s['requested_fields'],'query':'price'}
        quantity=re.sub(r'\d+(?:\.\d+)?\s*(?:ชั่วโมง|นาที|hours?|hrs?|minutes?|mins?)',' ',normalize(question))
        if quantity!=normalize(question) and re.fullmatch(framing,quantity) and len(re.findall(r'\d+(?:\.\d+)?\s*(?:ชั่วโมง|นาที|hours?|hrs?|minutes?|mins?)',normalize(question)))==1:
            return {'record_ids':prior,'method':'state_comparison_selection' if comp else 'typed_price_duration_selection','previous_fields':s['requested_fields'],'query':'price compare' if comp else 'price'}
    if explicit_ids:
        remainder=strip_names(question,explicit_ids,names)
        if {records[rid]['kind'] for rid in explicit_ids if rid in records}<={'audience'} and not remainder.strip(' ?!.,') and 'amount_minor' in s['requested_fields']:
            return {'record_ids':list(dict.fromkeys([rid for rid in prior if records[rid]['kind']!='audience']+explicit_ids)),'method':'state_audience_selection','previous_fields':s['requested_fields']}
        if not remainder.strip(' ?!.,') and 'amount_minor' in s['requested_fields'] and {records[rid]['kind'] for rid in explicit_ids if rid in records}.intersection({'service','resource','zone'}):
            return {'record_ids':list(dict.fromkeys(explicit_ids+[rid for rid in prior if records[rid]['kind']=='audience'])),'method':'state_service_selection','previous_fields':s['requested_fields']}
        return None
    q=normalize(question)
    if len(q)>400:return None
    if s.get('operation')=='booking' and re.search(r'สรุป|ทำ(?:ไง|ยังไง|อย่างไร)|\b(?:summary|summarize|so how|then how|steps)\b',q):
        return {'record_ids':prior,'method':'typed_common_state','previous_fields':s['requested_fields']}
    from .query_scope import operation
    if len(q)<100 and operation(q):return {'record_ids':prior,'method':'typed_common_state','previous_fields':s['requested_fields']}
    if resolve_fields(q,kinds)[0] or broad_request(q) or re.search(r'อันนี้|แบบนี้|เกมนี้|มัน|แล้ว|\b(?:it|this|that|and|also|then|so)\b',q):return {'record_ids':prior,'method':'typed_common_state','previous_fields':s['requested_fields']}
    return None
