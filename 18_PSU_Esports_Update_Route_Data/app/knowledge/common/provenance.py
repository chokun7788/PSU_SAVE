"""Read-only source priority; never changes trust, approval or factual values."""
import json,hashlib
from pathlib import Path
from .registry import pointer

def owner_basis(record,store,release):
    refs=[ref for f in record['fields'].values() for ref in f.get('evidence_refs',[])]
    metadata=release.get('sources',{})
    if any(metadata.get(ref['source_id'],{}).get('trust')=='owner_confirmed' for ref in refs):return True
    # Compatibility only: verify immutable migration lineage against the exact
    # byte-backed original confirmed owner-claim document, not an ID prefix.
    root=Path(__file__).resolve().parents[3]
    try:
        with store.connect() as c:sources=store.sources(c)
        visited=set()
        def visit(sid,depth=0):
            if sid in visited or depth>4 or sid not in sources:return False
            visited.add(sid);src,raw=sources[sid]
            if src.get('trust')=='owner_confirmed':return True
            data=json.loads(raw)
            for item in data.get('field_lineage',[]):
                rel=item.get('source_path');locator=item.get('locator','')
                if not rel or not locator.startswith('/claims/'):continue
                p=(root/rel).resolve()
                if not p.is_relative_to(root/'data') or not p.is_file():continue
                original=p.read_bytes()
                if hashlib.sha256(original).hexdigest()!=item.get('source_sha256'):continue
                doc=json.loads(original.decode('utf-8-sig'))
                if doc.get('basis')!='user_provided_in_this_chat':continue
                claim_key=locator.split('/')[2]
                if doc.get('claims',{}).get(claim_key,{}).get('status')!='user_confirmed':continue
                if pointer(doc,locator)==item.get('source_value'):return True
            for item in data.get('translation_lineage',[]):
                if any(visit(ref['source_id'],depth+1) for ref in item.get('original_field_evidence',[])):return True
            return False
        return any(visit(ref['source_id']) for ref in refs)
    except (OSError,ValueError,KeyError,TypeError):return False
