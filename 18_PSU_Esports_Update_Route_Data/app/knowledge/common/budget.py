"""Budget arithmetic over confirmed service rates. No guessed discounts or tax."""
import re
from decimal import Decimal,InvalidOperation
from .registry import value
from .query_contract import normalize,live_request,semantic_clauses
def budget_request(question,records,selected_ids):
    q=normalize(question)
    if live_request(q) or not re.search(r'งบ|มีเงิน|เงิน.*เล่น|\b(?:budget|afford|spend|i have)\b',q):return None
    match=re.search(r'(\d[\d,]*(?:\.\d{1,2})?)\s*(?:บาท|baht|thb)(?![a-z])',q)
    if not match:return None
    try:amount=int(Decimal(match[1].replace(',',''))*100)
    except (ValueError,InvalidOperation):return None
    if not 0<=amount<=10**9:return None
    audiences={rid for rid in selected_ids if records[rid]['kind']=='audience'}
    services={rid for rid in selected_ids if records[rid]['kind']=='service'}
    resources={rid for rid in selected_ids if records[rid]['kind']=='resource'}
    if resources:services.update(r['record_id'] for r in records.values() if r['kind']=='service' and resources.intersection(value(r,'resource_ids') or []))
    rental=bool(re.search(r'เหมา|ครึ่งวัน|เต็มวัน|\b(?:rental|rent|package|half.day|full.day)\b',q))
    zones={rid for rid in selected_ids if records[rid]['kind']=='zone'}
    if rental:
        resources.update(rid for sid in services for rid in value(records[sid],'resource_ids') or [])
        zones.update(value(records[rid],'zone_id') for rid in resources if rid in records and value(records[rid],'zone_id'))
    period='full_day' if re.search(r'เต็มวัน|full.day',q) else 'half_day' if re.search(r'ครึ่งวัน|half.day',q) else None
    party=re.search(r'(\d+)\s*(?:คน|people|persons|players)',q)
    party_count=int(party[1]) if party else None
    unresolved=[]
    if party_count and party_count>1:unresolved.append('party_size:'+str(party_count))
    for clause in semantic_clauses(q):
        if not re.search(r'งบ|มีเงิน|เงิน.*เล่น|\b(?:budget|afford|spend|i have)\b',clause):
            if not re.fullmatch(r'\s*(?:เล่น(?:อะไร|ได้นาน|ได้กี่นาที)?(?:ได้บ้าง)?|what can i play|how long can i play|how many minutes)\s*[?!.]*',clause):unresolved.append(clause)
    results=[];unknown=[]
    for rate in records.values():
        if rate['kind']!=('rental_package' if rental else 'rate'):continue
        if not rental and services and value(rate,'service_id') not in services:continue
        if rental and zones and not zones.intersection(value(rate,'zone_ids') or []):continue
        if rental and period and value(rate,'period_label')!=period:continue
        if audiences and value(rate,'audience_id') not in audiences:continue
        price=value(rate,'amount_minor');currency=value(rate,'currency');rule=value(rate,'calculation_rule');duration=value(rate,'duration_minutes')
        if type(price) is not int or currency!='THB':unknown.append(rate['record_id']);continue
        if price>amount:continue
        row={'rate_id':rate['record_id'],'amount_minor':price,'currency':currency,'service_id':value(rate,'service_id'),'audience_id':value(rate,'audience_id'),'rule':rule,'duration_minutes':duration,'max_minutes':None,'max_units':None}
        if not unresolved and rule in {'linear','session_ceil'} and price>0 and type(duration) is int and duration>0:
            row['max_units']=amount//price;row['max_minutes']=row['max_units']*duration
        # Fixed/no-extrapolation/free prices are listed without invented repeatability.
        results.append(row)
    return {'budget_minor':amount,'currency':'THB','rows':results,'unknown_rate_ids':unknown,'audience_unspecified':not audiences,'party_count':party_count,'unresolved_qualifiers':unresolved,'kind_scope':'rental_package' if rental else 'rate','method':'confirmed_rate_budget'}
