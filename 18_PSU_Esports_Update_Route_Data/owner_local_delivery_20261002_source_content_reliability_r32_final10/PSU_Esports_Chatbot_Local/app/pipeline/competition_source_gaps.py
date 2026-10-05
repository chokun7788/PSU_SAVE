"""Source gaps and conflicting clauses for one explicitly named rulebook.

This reads source text, never confirms policy or supplies missing values.
"""
from __future__ import annotations
import re
from app.knowledge.localization import approved_localization
from app.pipeline.competition_detail import CompetitionDetail, lookup_competition_detail
from app.pipeline.competition_targets import looks_like_competition_rule_query,resolve_competition_targets
from app.pipeline.competition_presentation import render_rule_reply,source_clause_lines,is_rule_clause

def _rows(rulebook_id):
    from app.pipeline.retrieval import load_curated_rows
    return sorted((r for r in load_curated_rows() if not r.get('_canonical_projection') and str(r.get('id','')).startswith(rulebook_id+'_s')),key=lambda r:(int(r.get('section_index') or 0),int(r.get('chunk_index') or 0)))

def _text(row,locale):
    return (approved_localization(row,'text') or '') if locale=='en' else str(row.get('text') or '')

def _source_gap(query,locale,rows):
    numbered=re.search(r'(?:ข้อ|\bclause|\brule|\bsection)\s*(\d+(?:\.\d+){1,5})(?![\d.])',query,re.I)
    if numbered:
        number=numbered.group(1)
        source_matches=[(row,line) for row in rows for line in source_clause_lines(str(row.get('text') or '')) if re.match(r'^'+re.escape(number)+r'(?:\.|\s)',line)]
        # A final dangling preposition cannot substantiate a complete rule.
        if source_matches and any(re.search(r'ดังกล่าวออกจาก\s*$',line) for _,line in source_matches):
            note=(f'I could not find verified complete text for clause {number}: the recorded source ends mid-sentence. The organizer must provide the complete source.' if locale=='en' else f'ยังไม่พบข้อความฉบับเต็มที่ยืนยันได้สำหรับข้อ {number} เพราะต้นฉบับจบไม่ครบ ต้องขอเอกสารฉบับเต็มจากผู้จัดครับ')
            return CompetitionDetail(note,(),(), 'no_answer',('source_clause_incomplete',))
        if source_matches:
            translated=[(row,line) for row,_ in source_matches for line in source_clause_lines(_text(row,locale)) if re.match(r'^'+re.escape(number)+r'(?:\.|\s)',line) and is_rule_clause(line)]
            if translated:
                selected=list(dict.fromkeys(line for _,line in translated));used=tuple({row['id']:row for row,_ in translated}.values())
                return CompetitionDetail(render_rule_reply(selected[0],selected[1:],used[0],locale),used,('explicit_clause',))
        note=(f'I could not find verified complete clause {number} in this rulebook.' if locale=='en' else f'ยังไม่พบข้อความข้อ {number} ฉบับเต็มที่ยืนยันได้ในเอกสารของเกมนี้ครับ')
        return CompetitionDetail(note,(),(), 'no_answer',('explicit_clause_not_covered',))
    missing=[]
    if re.search(r'ค่าสมัคร|ค่าลงทะเบียน|(?:registration|entry|participation) fee',query,re.I):
        money=[(r,line) for r in rows for line in source_clause_lines(_text(r,locale)) if re.search(r'ค่าสมัคร|ค่าลงทะเบียน|(?:registration|entry|participation) fee',line,re.I) and re.search(r'\d',line)]
        if money:
            selected=list(dict.fromkeys(line for _,line in money));used=tuple({r['id']:r for r,_ in money}.values())
            return CompetitionDetail(render_rule_reply(selected[0],selected[1:],used[0],locale),used,('registration_fee',))
        missing.append(('registration_fee_not_in_source','I could not find verified registration-fee information in this game\'s recorded rulebook.' if locale=='en' else 'ยังไม่พบข้อมูลค่าสมัครการแข่งขันในเอกสารของเกมนี้ครับ'))
    if re.search(r'minimum age|age requirement|อายุขั้นต่ำ|อายุอย่างน้อย',query,re.I):
        age_clauses=[(r,line) for r in rows for line in source_clause_lines(_text(r,locale)) if re.search(r'อายุ.*(?:ขั้นต่ำ|อย่างน้อย|ไม่ต่ำกว่า)|minimum age|(?:must be at least|minimum|aged at least).*years (?:old|of age)',line,re.I) and re.search(r'\d',line)]
        if age_clauses:
            selected=list(dict.fromkeys(line for _,line in age_clauses));used=tuple({r['id']:r for r,_ in age_clauses}.values())
            return CompetitionDetail(render_rule_reply(selected[0],selected[1:],used[0],locale),used,('minimum_age',))
        missing.append(('minimum_age_not_in_source','I could not find a verified minimum-age requirement in this game\'s recorded rulebook.' if locale=='en' else 'ยังไม่พบข้อมูลอายุขั้นต่ำในเอกสารของเกมนี้ครับ'))
    if not missing:
        return None
    supported_query=re.sub(r'ค่าสมัคร|ค่าลงทะเบียน|(?:registration|entry|participation) fee','',query,flags=re.I)
    detail=lookup_competition_detail(supported_query,locale)
    notes=' '.join(note for _,note in missing);reasons=tuple(reason for reason,_ in missing)
    if detail is None:
        return CompetitionDetail(notes,(),(), 'no_answer',reasons)
    # Keep every supported proposition and make the unresolved one visible.
    marker='\nRulebook:' if locale=='en' else '\nอ้างอิงจากกติกา:'
    label='Additional requested information: ' if locale=='en' else 'ประเด็นที่ยังไม่พบข้อมูล: '
    answer=detail.answer.replace(marker,'\n'+label+notes+marker,1)
    return CompetitionDetail(answer,detail.rows,detail.concepts,'partial',reasons)

def _pause_conflict(query,locale,rows,game_id):
    if game_id!='tekken8' or not re.search(r'หยุดเกม|\bpaus(?:e|ing)',query,re.I):
        return None
    prohibitions=[];permissions=[];penalties=[]
    for row in rows:
        for line in source_clause_lines(_text(row,locale)):
            if re.search(r'เริ่มเกม.*ห้ามหยุดเกม.*เหตุผล|(?:Once|After).*game.*(?:no.*pausing|paus.*(?:prohibited|not permitted))',line,re.I):prohibitions.append((row,line))
            if re.search(r'การกดหยุดเกม.*ผู้เล่นทุกคนยินยอม|game may be paused.*all players agree',line,re.I):permissions.append((row,line))
            if re.search(r'กดหยุดเกม.*(?:ปรับแพ้|โทษ)|(?:intentional.*pause|Pausing the game without).*penalty',line,re.I):penalties.append((row,line))
    if not prohibitions or not permissions:
        return None
    first=('The recorded pause clauses conflict. The organizer must confirm the exception conditions and penalty level before a definite ruling can be given.' if locale=='en' else 'ข้อกฎเรื่องการหยุดเกมในเอกสารขัดกัน ต้องให้ผู้จัดยืนยันเงื่อนไขข้อยกเว้นและระดับโทษก่อนจึงจะสรุปได้ครับ')
    pairs=prohibitions+permissions+penalties;used=tuple({row['id']:row for row,_ in pairs}.values())
    answer=render_rule_reply(first,list(dict.fromkeys(line for _,line in pairs)),used[0],locale)
    return CompetitionDetail(answer,used,('pause_conflict',),'conflict',('source_clauses_conflict',))

def _recorded_year_guard(query, locale, rulebook_id):
    # Bind explicit Gregorian edition years to the registered source identity.
    # An update date, game number, or source with no edition year is not evidence.
    recorded = set(re.findall(r"(?:^|_)((?:19|20)\d{2})(?=_|$)", rulebook_id))
    requested = set()
    for match in re.finditer(r"(?<![\d.])(?:19|20)\d{2}(?![\d.])", query):
        before = query[max(0, match.start() - 40):match.start()]
        after = query[match.end():match.end() + 24]
        # Four-digit amounts and birth years do not request a rulebook edition.
        if re.search(r"(?:born(?:\s+in)?|birth\s+year|เกิด(?:ใน)?\s*(?:ปี)?|ราคา|fee(?:\s+of)?|costs?)\s*$", before, re.I):
            continue
        if re.match(r"\s*(?:บาท|baht\b|THB\b|USD\b|years? old\b)", after, re.I):
            continue
        requested.add(match.group(0))
    if not recorded or not requested or requested <= recorded:
        return None
    have = ", ".join(sorted(recorded)); want = ", ".join(sorted(requested))
    note = (
        f"The available rulebook is recorded for {have}; it does not verify the requested {want} edition. The organizer must provide that edition before its rules can be confirmed."
        if locale == 'en' else
        f"เอกสารกติกาที่มีระบุปี {have} จึงยังยืนยันกติกาฉบับปี {want} ที่ถามไม่ได้ ต้องขอเอกสารฉบับปีนั้นจากผู้จัดก่อนครับ"
    )
    return CompetitionDetail(note, (), (), 'no_answer', ('requested_rulebook_year_not_in_source', 'event_year_not_covered'))

def lookup_competition_reply(query,locale):
    target=resolve_competition_targets(query)
    if target.status!='exact' or not looks_like_competition_rule_query(query):return None
    year_guard=_recorded_year_guard(query,locale,target.targets[0].rulebook_id)
    if year_guard is not None:return year_guard
    rows=_rows(target.targets[0].rulebook_id)
    gap=_source_gap(query,locale,rows)
    if gap is not None:return gap
    conflict=_pause_conflict(query,locale,rows,target.targets[0].game_id)
    if conflict is not None:return conflict
    return lookup_competition_detail(query,locale)
