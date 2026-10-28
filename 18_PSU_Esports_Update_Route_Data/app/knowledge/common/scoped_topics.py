"""Secondary topic lookup for records with declared, non-conflicting scope."""
import re
from .registry import value,CATALOG
from .query_contract import normalize,strip_names,semantic_clauses
from .entity_search import candidates,topic_alignment,select as model_select

KINDS={'faq','policy','procedure'}
SCOPE_KINDS={'game','resource','service','zone','equipment_model'}
def closure(roots,records):
    found=set(roots);queue=list(roots)
    for _ in range(3):
        next_level=[]
        for rid in queue:
            r=records[rid]
            for f in CATALOG[r['kind']]['fields']:
                if f['reference_kind'] not in SCOPE_KINDS:continue
                v=value(r,f['key']);refs=v if isinstance(v,list) else [v]
                for ref in refs:
                    if isinstance(ref,str) and ref in records and ref not in found:found.add(ref);next_level.append(ref)
            for k,child in records.items():
                if child['kind']=='service' and rid in roots and records[rid]['kind']=='resource' and rid in (value(child,'resource_ids') or []) or child['kind']=='game_service' and value(child,'game_id')==rid:
                    if k not in found:found.add(k);next_level.append(k)
        queue=next_level
        if not queue:break
    return found
def scoped(record,scope):
    if record['kind']=='faq':
        refs=record['fields']['related_ids']
        return refs['status']=='known' and (not refs['value'] or bool(set(refs['value'])&scope))
    if record['kind'] in {'policy','procedure'}:
        conditions=record['fields']['conditions_all' if record['kind']=='policy' else 'preconditions']
        if conditions['status']!='known':return False
        for c in conditions['value']:
            if c['field'] not in {'service_id','resource_id','zone_id','game_id','equipment_model_id'}:continue
            values=c['value'] if isinstance(c['value'],list) else [c['value']]
            if c['operator'] not in {'eq','in'} or not any(isinstance(v,str) and v in scope for v in values):return False
        return True
    return False
def lookup(question,records,names,roots,*,allow_llm=False):
    from .answer import named
    if not roots:return None,{'attempted':False,'reason':'no_named_scope'}
    if re.search(r'\b(?:pc|ps|vr|cockpit)\s*#?\s*\d+',question,re.I) and not any(records[rid]['kind']=='resource' for rid in roots):return None,{'attempted':False,'reason':'numbered_target_unresolved'}
    scope=closure(roots,records);scope_names={rid:a for rid,a in names.items() if rid in records and records[rid]['kind'] in SCOPE_KINDS}
    masked=strip_names(question,roots,names);eligible={};evidence={}
    for rid,r in records.items():
        if r['kind'] not in KINDS or not scoped(r,scope):continue
        heading=[]
        for key in ('question','subject','title','topic'):
            v=value(r,key);heading.extend(s for s in v.values() if isinstance(s,str)) if isinstance(v,dict) else heading.append(str(v or ''))
        named_scope,_=named(' '.join(heading),scope_names,allow_fuzzy=False)
        if named_scope and not set(named_scope)&scope:continue
        eligible[rid]=r;evidence[rid]={'declared_scope_compatible':True,'header_scope_ids':named_scope}
    rows=candidates(masked,eligible,{rid:names[rid] for rid in eligible})
    aligned=[row for row in rows if topic_alignment(masked,eligible[row['record_id']])[0]]
    if aligned and aligned[0]['score']>=.45 and (len(aligned)==1 or aligned[0]['score']-aligned[1]['score']>=.15) and len(semantic_clauses(masked))==1:
        rid=aligned[0]['record_id'];return [rid],{'attempted':False,'method':'unique_scoped_topic','candidate_ids':[r['record_id'] for r in rows],'score':aligned[0]['score'],'scope_ids':sorted(scope),'evidence':{rid:evidence[rid]},'semantic_correctness_verified':False}
    if not allow_llm:return None,{'attempted':False,'method':'scoped_topic_unresolved','candidate_ids':[r['record_id'] for r in rows]}
    chosen,audit=model_select(masked,eligible,{rid:names[rid] for rid in eligible})
    if not isinstance(chosen,list):return None,{**audit,'method':'scoped_topic_unresolved'}
    if not all(topic_alignment(masked,eligible[rid])[0] for rid in chosen):return None,{**audit,'method':'scoped_topic_rejected','reason':'target_name_alone_is_not_topic_evidence'}
    return chosen,{**audit,'method':'bounded_scoped_topic_model','scope_ids':sorted(scope),'evidence':{rid:evidence[rid] for rid in chosen},'semantic_correctness_verified':False}
