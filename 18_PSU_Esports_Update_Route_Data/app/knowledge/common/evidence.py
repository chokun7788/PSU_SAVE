"""Evidence identity from explicit FKs and immutable migration pointers."""
import hashlib,json
from pathlib import Path
from functools import lru_cache
from .registry import value

@lru_cache(maxsize=4)
def _chunk_index(path,mtime,size):
    rows={}
    for line in Path(path).read_text(encoding='utf-8-sig').splitlines():
        if not line.strip():continue
        row=json.loads(line)
        key=(row.get('document_id'),str(row.get('section_index')),row.get('text'))
        rows.setdefault(key,[]).append(row)
    return rows

def enrich_hit(hit,snapshot,store):
    records=snapshot['release']['records'];r=records.get(hit.get('record_id'))
    if not r:return hit
    comp=r if r['kind']=='competition' else records.get(value(r,'competition_id'))
    gid=value(r,'game_id') or (value(comp,'game_id') if comp else None)
    game=records.get(gid);name=value(game,'title') if game else None
    meta={**hit.get('metadata',{}),'common_record_id':r['record_id'],'common_field':hit.get('field'),'common_revision':r['revision']}
    if game:
        meta['common_game_id']=gid
        meta['game']=(name.get('en') or name.get('th')) if isinstance(name,dict) else name
    if comp and comp['kind']=='competition':
        meta['common_competition_id']=comp['record_id'];meta['rulebook_release']=value(comp,'rulebook_release')
        # A version label alone is not a legacy document ID. Require the
        # migration's explicit /facts/document_id source mapping.
        field=comp['fields'].get('rulebook_release',{})
        try:
            with store.connect() as c:
                for ref in field.get('evidence_refs',[]):
                    row=c.execute('SELECT payload,snapshot FROM cc_sources WHERE source_id=?',(ref['source_id'],)).fetchone()
                    if not row:continue
                    src=json.loads(row['payload']);raw=row['snapshot']
                    if hashlib.sha256(raw.encode()).hexdigest()!=src['sha256']:continue
                    for lineage in json.loads(raw).get('field_lineage',[]):
                        if lineage.get('field')=='rulebook_release' and lineage.get('locator')=='/facts/document_id' and lineage.get('mapped_value')==value(comp,'rulebook_release') and lineage.get('source_value')==value(comp,'rulebook_release'):
                            root=Path(__file__).resolve().parents[3]
                            original=(root/lineage.get('source_path','')).resolve()
                            if not original.is_relative_to(root/'data') or not original.is_file() or hashlib.sha256(original.read_bytes()).hexdigest()!=lineage.get('source_sha256'):continue
                            meta['document_id']=value(comp,'rulebook_release');meta['legacy_document_identity_proven']=True
                            meta['source_ids']=[meta['document_id']]
        except (OSError,ValueError,KeyError,TypeError):pass
        if meta.get('legacy_document_identity_proven') and r['kind']=='competition_rule' and hit.get('field') in {'heading','text'}:
            # Recover an existing chunk identity only on an exact source-text,
            # document and section match. Never construct canonical rule IDs.
            try:
                source=Path(__file__).resolve().parents[3]/'data/competition_rules/competition_rule_chunks.jsonl';stat=source.stat()
                raw=value(r,'text');thai=raw.get('th') if isinstance(raw,dict) else raw
                matches=_chunk_index(str(source),stat.st_mtime_ns,stat.st_size).get((meta['document_id'],str(value(r,'section_number')),thai),[])
                if len(matches)==1:
                    chunk=matches[0];meta['source_chunk_id']=chunk['id'];meta['source_chunk_identity_basis']='exact immutable migrated document / section / Thai text'
                    meta['original_chunk_text_sha256']=hashlib.sha256(chunk['text'].encode()).hexdigest()
            except (OSError,ValueError,KeyError,TypeError):pass
    return {**hit,'metadata':meta}
