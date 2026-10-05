"""Bounded facet vocabulary recovery, restricted to an explicit rulebook.
No complete question aliases, numbers, or short negations are candidates.
"""
import re
from functools import lru_cache

@lru_cache(maxsize=512)
def recover_facet_cue(query):
    from app.pipeline.competition_targets import resolve_competition_targets, looks_like_competition_rule_query
    target=resolve_competition_targets(query)
    if target.status!='exact' or not looks_like_competition_rule_query(query):return None
    if re.search(r'ไม่ใช่(?:กฎ|กฏ|กติกา)|not (?:competition |tournament )?rules',query,re.I):return None
    from app.pipeline.competition_taxonomy import FACET_ALIASES
    from app.pipeline.competition_name_recovery import recover_names
    aliases_with_valid_settings=FACET_ALIASES+(('match_settings',('game settings','การตั้งค่าในเกม')),('eligibility_registration',('คุณสมบัติ','eligibility')),('rulebook_identity',('event information','ใช้กับการแข่งขันไหน')), )
    registry=tuple((name,alias) for name,aliases in aliases_with_valid_settings for alias in aliases
                   if len(re.sub(r'\s+','',alias))>=6 and not re.search(r'\d',alias))
    _,edits=recover_names(query,registry,allow_same_target_overlap=True)
    # Preserve registered game spans and exact adjacent negation.
    for edit in edits:
        if re.search(r'[:;?!.,]',edit.original):continue
        # Preserve complete threshold words even when the candidate ends
        # before their last Thai letter. Otherwise หยุดเกิน becomes หยุดเกมน.
        if any(edit.start<m.end() and m.start()<edit.end for m in re.finditer(r'เกิน|การแข่งขันไหน',query)):continue
        # March is a valid month/verb, and may signal a timing ambiguity.
        # Whole-span distance does not authorize replacing a valid word.
        if re.search(r'\bmarch\b',edit.original,re.I):continue
        if edit.original.casefold() in {'game settings','การตั้งค่าในเกม'}:continue
        if re.search(r'\d',edit.original+edit.canonical):continue
        if re.search(r'\b(?:no|not|never|without)\b|ไม่',edit.original,re.I):continue
        connectors=[m for m in re.finditer(r'และ|กับ|\band\b',query,re.I) if edit.start<m.end() and m.start()<edit.end]
        if connectors:
            # A facet edit cannot consume the first letter of a conjunction.
            # Re-score the same facet with the conjunction as a hard boundary.
            boundary=connectors[0]
            if edit.start>=boundary.start():continue
            _,bounded=recover_names(query[:boundary.start()],registry,allow_same_target_overlap=True)
            same=[e for e in bounded if e.start==edit.start and e.game_id==edit.game_id and e.canonical==edit.canonical]
            if not same:continue
            edit=same[0]
        recovered=query[:edit.start]+edit.canonical+query[edit.end:]
        after=resolve_competition_targets(recovered)
        if after.status==target.status and after.targets==target.targets:
            return recovered,edit
    return None
