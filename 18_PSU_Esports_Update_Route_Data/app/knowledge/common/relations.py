"""Whitelisted FK traversal for explicitly requested related policy facts."""
from .registry import value
from .registry import CATALOG
READ_TARGETS={'resource':{'equipment_model','zone'},'service':{'resource'},'rate':{'service','audience'},'policy':{'procedure'},'game_service':{'policy'},'closure':{'policy'}}
def related_attributes(records,record,requested,*,full=False):
    """Read only declared factual FK paths, never infer a relationship from names."""
    root=record['record_id'];seen={root};queue=[record];result=[]
    for depth in range(4):
        next_level=[]
        for parent in queue:
            for field in CATALOG[parent['kind']]['fields']:
                if field['reference_kind'] not in READ_TARGETS.get(parent['kind'],set()):continue
                target=value(parent,field['key'])
                if target is None:continue
                for rid in target if isinstance(target,list) else [target]:
                    child=records.get(rid)
                    if rid in seen or not child:continue
                    seen.add(rid);next_level.append(child)
                    keys=list(child['fields']) if full else [key for key in requested if key in child['fields']]
                    if keys:result.append((child,keys,{'from':parent['record_id'],'via':field['key'],'to':rid}))
        queue=next_level
        if not queue:break
    return result
POLICY_LINKS={'game_service':'account_policy_id','closure':'resolution_policy_id'}
def linked_policies(records,record,requested,*,full=False):
    policy_fields={'decision','conditions_all','exceptions','details','consequence','procedure_id'}
    link=POLICY_LINKS.get(record['kind'])
    if not link or not (full or set(requested)&(policy_fields|{link})):return []
    target=value(record,link)
    if target is None:return []
    child=records.get(target)
    if not child or child['kind']!='policy':return []
    # A request for the FK alone asks for identity, not the whole policy.
    keys=list(child['fields']) if full else list(set(requested)&policy_fields)
    if not keys:return []
    return [(child,keys,{'from':record['record_id'],'via':link,'to':target})]

def related_rates(records,record,*,audiences=(),platform=None):
    services=set()
    if record['kind']=='service':services.add(record['record_id'])
    elif record['kind']=='resource':
        services={r['record_id'] for r in records.values() if r['kind']=='service' and record['record_id'] in (value(r,'resource_ids') or [])}
    elif record['kind']=='zone':
        resources={r['record_id'] for r in records.values() if r['kind']=='resource' and value(r,'zone_id')==record['record_id']}
        services={r['record_id'] for r in records.values() if r['kind']=='service' and resources.intersection(value(r,'resource_ids') or [])}
    elif record['kind']=='game':
        services={value(r,'service_id') for r in records.values() if r['kind']=='game_service' and value(r,'game_id')==record['record_id'] and value(r,'offered') is True}
    if platform:services={sid for sid in services if sid in records and value(records[sid],'platform')==platform}
    rates=[r for r in records.values() if r['kind']=='rate' and (value(r,'service_id') in services or record['kind']=='audience' and value(r,'audience_id')==record['record_id']) and (not audiences or value(r,'audience_id') in audiences)]
    return sorted(rates,key=lambda r:(str(value(r,'service_id')),str(value(r,'audience_id')),r['record_id']))
