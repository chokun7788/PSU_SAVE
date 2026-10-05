"""Independent source-clause requirements for quantities and event venue.

Requirements originate in the question, not in the answer's selected facets.
Unknown source facts are never supplied by this contract.
"""
from __future__ import annotations
from functools import lru_cache
import re
import unicodedata

def cs2_timeout_requested(query: str) -> bool:
    # Technical timeout is not tactical time. A separate tactical/bare request
    # elsewhere in a compound question is retained after local masking.
    q=re.sub(r'\btechnical\s+(?:timeouts?|pause)\b|เวลานอกทางเทคนิค',' ',query,flags=re.I)
    return bool(re.search(r'(?<![a-z])timeouts?(?![a-z])|เวลานอก',q,re.I))

def freeze_is_timeout_context(query: str) -> bool:
    return cs2_timeout_requested(query) and bool(re.search(r'(?:timeouts?|เวลานอก).{0,20}(?:during|in|ตอน|ระหว่าง|ช่วง)\s*(?:the\s+)?freeze\s*time',query,re.I))

def cs2_venue_requested(query: str) -> bool:
    pattern=r'สถานที่(?:จัด|แข่ง|แข่งขัน)|สนาม(?:แข่งขัน)?\s*(?:อยู่)?\s*(?:ที่ใด|ที่ไหน)|(?:แข่ง(?:ขัน)?|จัด(?:การแข่งขัน|แข่ง(?:ขัน)?)?)\s*(?:CS2|Counter-Strike 2)?\s*(?:ที่ใด|ที่ไหน)|(?:location|venue).{0,40}(?:competition|tournament)|(?:competition|tournament).{0,40}(?:location|venue|take place)|where.{0,45}(?:competition|tournament).{0,25}(?:held|take place)'
    return any(not re.search(r'ปุ่ม|ตั้งค่า|ตำแหน่ง|\b(?:buttons?|controls?|settings?|crosshair|menu)\b',match.group(),re.I) for match in re.finditer(pattern,query,re.I))

def request_requirements(query: str,game_id: str) -> tuple[tuple[str,str],...]:
    if game_id!='cs2':return ()
    result=[]
    if cs2_timeout_requested(query):result.append(('tactical_timeout',r'การขอเวลานอก.*Freeze|Tactical timeouts:'))
    if cs2_venue_requested(query):result.append(('event_duration_venue',r'การแข่งขันจะแข่งขันทั้งหมด 1 วัน|(?:competition|tournament).{0,55}(?:1 day|one day)'))
    return tuple(result)

def _flat(text):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',text).casefold()).strip()

@lru_cache(maxsize=1)
def _source_rows():
    from app.pipeline.retrieval import load_curated_rows
    return {str(r.get('id')):r for r in load_curated_rows() if not r.get('_canonical_projection')}

def validate_requested_clauses(query: str,answer: str,hits,locale: str,mode: str) -> tuple[str,...]:
    if any(s in mode for s in ('no_answer','clarification','conflict')):return ()
    from app.pipeline.competition_targets import resolve_competition_targets,looks_like_competition_rule_query
    target=resolve_competition_targets(query)
    if target.status!='exact' or not looks_like_competition_rule_query(query):return ()
    requirements=request_requirements(query,target.targets[0].game_id)
    if not requirements:return ()
    from app.knowledge.localization import approved_localization
    from app.pipeline.competition_presentation import source_clause_lines
    rows=_source_rows();selected=[rows[str(h.get('id'))] for h in (hits or []) if str(h.get('id')) in rows and str(h.get('id')).startswith(target.targets[0].rulebook_id+'_s')]
    errors=[];body=_flat(answer)
    for name,source_pattern in requirements:
        clauses=[line for row in selected for line in source_clause_lines((approved_localization(row,'text') or '') if locale=='en' else str(row.get('text') or '')) if re.search(source_pattern,line,re.I)]
        # A clause alone does not substantiate every request. Preserve its
        # quantities and limiting condition together in the displayed answer.
        if not clauses:errors.append('competition_requested_clause_source_missing:'+name)
        elif not any(_flat(line) in body for line in clauses):errors.append('competition_requested_clause_incomplete:'+name)
    return tuple(errors)
