"""Typed intent diagnostics. Schema validity is not semantic correctness."""
from .registry import CATALOG
from .query_contract import scope_kinds,semantic_clauses,resolve_fields
def build_needs(question,kinds,requested,*,model=False,unresolved=()):
    result=[];scope=scope_kinds(kinds)
    for index,field in enumerate(requested):
        owners=[kind for kind in sorted(scope) if any(f['key']==field for f in CATALOG[kind]['fields'])]
        spans=[c for c in semantic_clauses(question) if field in resolve_fields(c,kinds)[0]]
        result.append({'id':'n'+str(index+1),'field_refs':[{'kind':k,'key':field} for k in owners],'source_span':spans[0] if spans else question,'resolution':'model_proposed' if model else 'typed_supported','ambiguous_kind':len(owners)>1})
    return {'schema_version':'common_read_plan_v1','needs':result,'unresolved_spans':list(unresolved),'semantic_correctness_verified':False}
