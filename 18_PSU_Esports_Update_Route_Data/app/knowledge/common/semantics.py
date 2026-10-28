"""Developer meanings and presentation rules, separate from approved facts."""
import json
from pathlib import Path
from .registry import CATALOG
HOME=Path(__file__).resolve().parent
SEMANTICS=json.loads((HOME/'schema_descriptions.json').read_text(encoding='utf-8'))
PROFILES=json.loads((HOME/'answer_profiles.json').read_text(encoding='utf-8'))
def meaning(kind,key,lang):
    spec=next(f for f in CATALOG[kind]['fields'] if f['key']==key)
    item=SEMANTICS.get('kinds',{}).get(kind,{}).get(key,SEMANTICS['fields'].get(key,{}))
    return item.get('description_'+lang) or (spec['meaning_th'] if lang=='th' else key.replace('_',' '))
def label(kind,key,lang):
    return PROFILES.get('labels',{}).get(kind,{}).get(key,{}).get(lang) or (next(f['meaning_th'] for f in CATALOG[kind]['fields'] if f['key']==key) if lang=='th' else key.replace('_',' '))
def project(record,requested,*,full=False):
    """Keep necessary scope/conditions without expanding the whole record."""
    fields=record['fields'];kind=record['kind']
    if full:return list(fields),{k:'explicit_all' for k in fields}
    keys=[k for k in requested if k in fields];basis={k:'explicit' for k in keys}
    profile=PROFILES['kinds'].get(kind,{})
    for rule in profile.get('context',[]):
        if '*' not in rule['when'] and not set(keys)&set(rule['when']):continue
        for key in rule['include']:
            if key in fields and key not in keys and fields[key]['status'] not in {'unknown','not_applicable'}:keys.append(key);basis[key]='necessary_context'
    return keys,basis
