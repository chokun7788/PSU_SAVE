"""Release ownership decisions. Draft heads never become answer authority."""
from .registry import value
from .query_contract import live_request,normalize,strip_names,resolve_fields
import re
def scoped_names(snapshot):
    current=(snapshot.get('release') or {}).get('names',{})
    result={rid:list(names) for rid,names in current.items()}
    current_owners={normalize(name):rid for rid,names in current.items() for name in names}
    for rid,names in snapshot.get('historical_names',snapshot.get('retired_names',{})).items():
        for name in names:
            if normalize(name) in current_owners and current_owners[normalize(name)]!=rid:continue
            if name not in result.setdefault(rid,[]):result[rid].append(name)
    return result

def field_ownership(snapshot,ids,fields):
    records=(snapshot.get('release') or {}).get('records',{})
    return [{'record_id':rid,'field':field,'authority':'common','status':records[rid]['fields'][field]['status'],'revision':records[rid]['revision']} for rid in ids if rid in records for field in fields if field in records[rid]['fields']]

def filter_legacy_hits(snapshot,hits):
    """Filter explicitly mapped or exactly named facts before model composition.

    Unknown mappings remain unmanaged. No fuzzy match can suppress another title.
    """
    records=(snapshot.get('release') or {}).get('records',{});names=scoped_names(snapshot)
    by_name={normalize(name):rid for rid,aliases in names.items() for name in aliases}
    kept=[];blocked=[]
    for hit in hits:
        meta=hit.get('metadata') or {};rid=meta.get('common_record_id') or hit.get('common_record_id')
        rid=rid or by_name.get(normalize(meta.get('entity_name') or hit.get('entity_name') or hit.get('title') or ''))
        field=meta.get('common_field') or hit.get('common_field')
        if rid and (rid in snapshot.get('withdrawn',[]) or rid not in records):blocked.append(hit);continue
        if rid in records and field in records[rid]['fields']:blocked.append(hit);continue
        # Only matching migrated source locators imply field ownership.
        source_id=hit.get('source_id') or meta.get('source_id');locator=hit.get('locator') or meta.get('locator')
        if rid in records and source_id and locator and any(any(e.get('source_id')==source_id and e.get('locator')==locator for e in f.get('evidence_refs',[])) for f in records[rid]['fields'].values()):blocked.append(hit);continue
        kept.append(hit)
    return kept,blocked
def classify(question,snapshot,ids):
    scoped_question=strip_names(question,ids,scoped_names(snapshot))
    from .query_scope import scoped_live_request
    if live_request(scoped_question) or scoped_live_request(question,ids,(snapshot.get('release') or {}).get('records',{})):return {'decision':'defer','reason':'live_adapter_authority'}
    release=snapshot.get('release')
    if not release:return {'decision':'defer','reason':'no_published_common_release'}
    records=release['records'];withdrawn=set(snapshot['withdrawn'])
    if any(rid in withdrawn or rid not in records for rid in ids):return {'decision':'blocked','reason':'retired_published_target','record_ids':ids}
    if not ids:return {'decision':'defer','reason':'no_resolved_common_target'}
    q=normalize(scoped_question)
    # Owning a zone description does not transfer ownership of every old price.
    rental=bool(re.search(r'เหมา|ครึ่งวัน|เต็มวัน|\b(?:rental|rent|package|half.day|full.day)\b',q))
    price='amount_minor' in resolve_fields(q,{records[rid]['kind'] for rid in ids})[0]
    if price and not rental and all(records[rid]['kind']=='zone' for rid in ids):
        from .relations import related_rates
        linked=[rate for rid in ids for rate in related_rates(records,records[rid])]
        if linked and all(rate['record_id'] in withdrawn for rate in linked):
            return {'decision':'blocked','reason':'related_regular_price_withdrawn','record_ids':ids}
        if not linked:
            return {'decision':'defer','reason':'regular_price_scope_not_migrated','record_ids':ids}
    competition=bool(re.search(r'แข่ง|การแข่งขัน|กติกา|กฎ|กฏ|\b(?:rules|competition|tournament)\b',q))
    games=[rid for rid in ids if records[rid]['kind']=='game']
    if games and competition and not any(r['kind']=='competition' and value(r,'game_id') in games for r in records.values()):
        return {'decision':'defer','reason':'competition_scope_not_migrated','record_ids':games}
    return {'decision':'common','reason':'published_target_owned','record_ids':ids,'release_id':snapshot['active'],'epoch':snapshot['epoch']}
