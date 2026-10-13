"""One registry for forms, schema validation, publication and query fields."""
from __future__ import annotations
import json, sys, re, hashlib
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse

HOME=Path(__file__).resolve().parent
sys.path.insert(0,str(HOME/'vendor'))
from jsonschema import Draft202012Validator, FormatChecker
from app.knowledge.records import canonical_json, digest
VERSION='studio-content-3.0'
CATALOG={x['kind']:x for x in json.loads((HOME/'catalog.json').read_text(encoding='utf-8'))}
SCHEMAS={k:json.loads((HOME/'schemas'/f'{k}.schema.json').read_text(encoding='utf-8')) for k in CATALOG}
for s in SCHEMAS.values(): Draft202012Validator.check_schema(s)
FORMAT=FormatChecker()

def now(): return datetime.now(timezone.utc).isoformat()
def value(record,key):
    f=record['fields'].get(key,{})
    return f.get('value') if f.get('status')=='known' else None
def content_hash(record):
    return digest({k:v for k,v in record.items() if k not in ('review','lifecycle','localization')})
def template(kind):
    if kind not in CATALOG: raise ValueError('Unknown content kind')
    return json.loads((HOME/'templates'/f'{kind}.draft.json').read_text(encoding='utf-8'))
def pointer(document,locator):
    if not isinstance(locator,str) or (locator and not locator.startswith('/')): raise ValueError('Evidence requires a JSON pointer')
    x=document
    for part in locator.split('/')[1:]:
        key=part.replace('~1','/').replace('~0','~')
        x=x[int(key)] if isinstance(x,list) else x[key]
    return x
def aware(text):
    d=datetime.fromisoformat(text.replace('Z','+00:00'))
    if d.tzinfo is None: raise ValueError('Timezone required')
    return d
def schema_errors(record):
    if not isinstance(record,dict) or record.get('kind') not in CATALOG: return ['Unsupported kind']
    return [('/'.join(map(str,e.absolute_path)) or '$')+': '+e.message for e in Draft202012Validator(SCHEMAS[record['kind']],format_checker=FORMAT).iter_errors(record)]
def safe_url(s):
    p=urlparse(s)
    return p.scheme=='https' and p.hostname and not p.username and not p.password and not re.search(r'[\s<>\[\]()]',s)
def translated_texts(v):
    if isinstance(v,dict):
        if set(v)=={'th','en'}:return bool(v['th'] and v['en'] and v['th']!=v['en'])
        return any(translated_texts(x) for x in v.values())
    if isinstance(v,list):return any(translated_texts(x) for x in v)
    return False
def source_errors(source, snapshot, *, demo=False):
    schema=json.loads((HOME/'schemas/source.schema.json').read_text(encoding='utf-8'))
    errors=[e.message for e in Draft202012Validator(schema,format_checker=FORMAT).iter_errors(source)]
    if errors: return errors
    if hashlib.sha256(snapshot.encode('utf-8')).hexdigest()!=source['sha256']: errors.append('Source snapshot hash mismatch')
    try: json.loads(snapshot);aware(source['observed_at'])
    except (ValueError,TypeError): errors.append('Invalid source JSON/timezone')
    if any(k not in CATALOG for k in source['authority_for']):errors.append('Unknown source authority')
    if source['public_url'] is not None and not safe_url(source['public_url']):errors.append('Unsafe public source URL')
    if (source['trust']=='synthetic' or source['kind']=='fixture') and not demo:errors.append('Fixture source cannot enter production database')
    return errors

def validate(record, records, sources, *, publish=False, demo=False):
    errors=schema_errors(record)
    if errors:return errors
    kind=record['kind']; fields=record['fields']; v=record['validity']
    try:
        dates=[aware(x) if x else None for x in (v['effective_from'],v['effective_until'])]
        if v['state']=='unknown' and any(dates):errors.append('Unknown validity cannot assert dates')
        if v['state']=='known' and not dates[0]:errors.append('Known validity requires effective_from')
        if all(dates) and dates[0]>=dates[1]:errors.append('Invalid validity interval')
    except (TypeError,ValueError):errors.append('Timezone-aware validity required')
    if publish and kind in {'rate','rental_package','schedule','closure','competition','competition_rule','news'} and v['state']!='known':errors.append('Time-sensitive content requires confirmed validity')
    for spec in CATALOG[kind]['fields']:
        key=spec['key']; field=fields[key]; val=value(record,key)
        empty_is_meaningful=key in {'conditions_all','preconditions','required_documents','open_periods','bookable_periods'} or (kind in {'schedule','closure'} and key=='zone_ids')
        if publish and spec['publish_core'] and (field['status']!='known' or (val==[] and not empty_is_meaningful)):
            errors.append(key+': required before publication')
        if publish and field['status']=='conflicted':errors.append(key+': unresolved conflict')
        for ref in field['evidence_refs']:
            pair=sources.get(ref['source_id'])
            if pair is None:errors.append(key+': missing source');continue
            src,snapshot=pair
            errors.extend(key+': '+e for e in source_errors(src,snapshot,demo=demo))
            if kind not in src['authority_for']:errors.append(key+': source authority mismatch')
            if publish and src['trust'] not in ({'owner_confirmed','official','internal_verified','synthetic'} if demo else {'owner_confirmed','official','internal_verified'}):errors.append(key+': source needs factual review')
            try:
                actual=pointer(json.loads(snapshot),ref['locator'])
                if field['status']=='known' and actual!=val:errors.append(key+': value does not match source pointer')
            except (KeyError,IndexError,ValueError,TypeError):errors.append(key+': invalid evidence pointer')
        if field['status']=='known' and spec['reference_kind']:
            targets=val if isinstance(val,list) else [val]
            for target in targets:
                other=records.get(target)
                if other is None:errors.append(key+': missing reference '+str(target))
                elif spec['reference_kind']!='*' and other['kind']!=spec['reference_kind']:errors.append(key+': wrong reference kind')
        if field['status']=='known' and key.endswith('_url') and not safe_url(val):errors.append(key+': HTTPS URL required')
    for mn,mx in [('capacity_min','capacity_max'),('persons_min','persons_max'),('players_min','players_max')]:
        a,b=value(record,mn),value(record,mx)
        if a is not None and b is not None and a>b:errors.append('Inverted capacity '+mn)
    for key in ('open_periods','bookable_periods','maintenance_periods'):
        periods=value(record,key) or []
        if any(p['start']>=p['end'] for p in periods):errors.append(key+': inverted period')
        ordered=sorted(periods,key=lambda p:p['start'])
        if any(a['end']>b['start'] for a,b in zip(ordered,ordered[1:])):errors.append(key+': overlapping periods')
    if kind=='schedule':
        for p in value(record,'bookable_periods') or []:
            if not any(o['start']<=p['start'] and p['end']<=o['end'] for o in value(record,'open_periods') or []):errors.append('Booking period outside opening')
            if any(p['start']<m['end'] and m['start']<p['end'] for m in value(record,'maintenance_periods') or []):errors.append('Booking overlaps maintenance')
    if kind=='closure' and value(record,'state')=='closed' and (value(record,'open_periods') or value(record,'bookable_periods')):errors.append('Closed date cannot assert opening/booking periods')
    if kind=='service' and value(record,'occupancy_minutes') is not None and value(record,'session_minutes') is not None and value(record,'occupancy_minutes')<value(record,'session_minutes'):errors.append('Occupancy shorter than session')
    if kind=='game_service' and value(record,'installed_resource_ids'):
        service=records.get(value(record,'service_id'))
        if service and not set(value(record,'installed_resource_ids'))<=set(value(service,'resource_ids') or []):errors.append('Installed resource outside service')
    if kind=='procedure':
        orders=[s['order'] for s in value(record,'steps') or []]
        if len(set(orders))!=len(orders):errors.append('Duplicate procedure step order')
        for step in value(record,'steps') or []:
            target=step.get('contact_id')
            if target and (target not in records or records[target]['kind']!='contact'):errors.append('Step contact reference invalid')
    if kind=='control_set' and any(not b['buttons'] for b in value(record,'bindings') or []):errors.append('Control row requires input buttons')
    if record['localization']['en_status']=='reviewed' and record['localization']['source_revision_hash']!=content_hash(record):errors.append('Stale English review')
    if publish:
        for k,f in fields.items():
            if f['status']=='known' and translated_texts(f['value']) and record['localization']['en_status'] not in {'reviewed','agent_translated'}:errors.append(k+': English translation needs review or explicit machine-translation status')
    return errors

def release_errors(records,sources,*,demo=False):
    errors=[]
    for r in records.values():errors += [r['record_id']+': '+e for e in validate(r,records,sources,publish=True,demo=demo)]
    def visit(k,stack):
        if k in stack:raise ValueError('Cyclic competition dependency')
        if len(stack)>20:raise ValueError('Competition dependency too deep')
        for child in value(records[k],'depends_on_ids') or []:
            if child in records:visit(child,stack|{k})
    for r in records.values():
        if r['kind']=='competition_rule':
            try:visit(r['record_id'],set())
            except ValueError as e:errors.append(str(e))
            for child in value(r,'depends_on_ids') or []:
                if child in records and value(records[child],'competition_id')!=value(r,'competition_id'):errors.append('Cross-competition rule dependency')
        if r['kind']=='control_set':
            game=records.get(value(r,'game_id'))
            if game and value(game,'supported_platforms') and value(r,'platform') not in value(game,'supported_platforms'):errors.append('Controls platform outside game platforms')
    rates=[r for r in records.values() if r['kind']=='rate']
    for i,a in enumerate(rates):
        for b in rates[i+1:]:
            keys=('service_id','audience_id','unit','duration_minutes','persons_min','persons_max')
            if all(value(a,k)==value(b,k) for k in keys):
                av,bv=a['validity'],b['validity']
                starts=[aware(x) for x in (av['effective_from'],bv['effective_from']) if x]
                ends=[aware(x) for x in (av['effective_until'],bv['effective_until']) if x]
                if starts and (not ends or max(starts)<min(ends)):errors.append('Overlapping rates in identical scope')
    return errors
