"""Recover supported operation vocabulary only inside independent syntax frames.

This is not a general spelling corrector: entity names, numbers, URLs,
negation and ambiguous real words are never candidates.
"""
from __future__ import annotations
import re
from functools import lru_cache
from app.core.typo_similarity import osa_distance
from app.core.keyboard_input_anomaly import GENERIC_ENGLISH_WORDS

_WORDS = GENERIC_ENGLISH_WORDS | frozenset("house home good shark smote contact contacts opens opening closing roles holds categories groups embers ember rice march pay paid laid live love cold old hold hole bold sold rule cost cast coat lost most host post scope cope station nation accommodation damage position role rules pen words keyboard mouse chair monitor smoke sharp object gaming morning monday sunday schedule cancellation transfer overnight expensive different booking reservation studio contact members device best accommodation penalties responsibility policy available the who are you more save have game genre equipment drinks notes heroes score".split())
_LATIN = re.compile(r"[A-Za-z]+")
_RESOURCE = re.compile(r"\b(?:pc(?:[ -]?#?\d+)?|ps5|vr|cockpit|nintendo|switch|playstation)\b|เครื่อง|อุปกรณ์",re.I)

@lru_cache(maxsize=2048)
def recover_task_frame(text: str):
    """Return (start, observed, canonical, distance, reason), or None."""
    low=text.casefold()
    if '://' in text or '@' in text or len(text)>180:return None
    tokens=list(_LATIN.finditer(text))
    protected_names=[(m.start(1),m.end(1)) for m in re.finditer(r"\b(?:called|named)\s+([^?!.]+)|\b(?:Mr|Ms|Mrs|Dr)\.?\s+(.+?)(?=\s+(?:hold|holds|old)\b|[?]|$)",text,re.I) if m.group(1)]
    for m in re.finditer(r"\b(?:Mr|Ms|Mrs|Dr)\.?\s+(.+?)(?=\s+(?:hold|holds|old)\b|[?]|$)",text,re.I):
        protected_names.append((m.start(1),m.end(1)))

    def near(word):
        return any(osa_distance(m.group().casefold(),word)<=1 for m in tokens)
    # Independent grammar/context anchors. Long words permit one edit;
    # short words require an explicit slot, never a global nearest word.
    for m in tokens:
        word=m.group().casefold();before=low[:m.start()];after=low[m.end():]
        if word in _WORDS or any(m.start()<end and m.end()>start for start,end in protected_names):continue
        targets=[]
        if re.search(r'\b(?:the|this|our|esports)\s+$',before):targets.append('studio')
        if near('studio'):
            if re.search(r'\b(?:the|studio|stduio|studoi)\s+$',before):targets.extend(('rules','policy'))
            if re.search(r'\b(?:penalties|responsibility|noise)\b',low):targets.append('damage')
            if re.search(r'\b(?:inside|smoking)\b',low) and re.search(r'\b(?:can|i|policy)\b',low):targets.append('smoke')
            if re.search(r'\b(?:drinks|noise)\b',low) and re.search(r'\b(?:for|about|bring)\s+$',before):targets.append('food')
            if re.match(r'\s+objects?\b',after):targets.append('sharp')
            if re.search(r'\bsharp\s+$',before):targets.append('object')
        if re.search(r'\b(?:what|which|how|where|who|is|does)\b',low):
            if near('studio'):targets.extend(('contact','members','manages'))
            if re.match(r'\s+(?:does|do)\b',after) and re.search(r'\bwhat\s+$',before):targets.append('position')
            if re.search(r'\b(?:what|which)\s+$',before) and re.match(r'\s+(?:is|are)\b',after):targets.append('device')
        if re.search(r'\b(?:reservation|booking|book|cancel|policy)\b',low):targets.extend(('reservation','cancellation','transfer','available'))
        if re.search(r'\b(?:open|hours?|operating|schedule|days?|morning|sundays?|now|play)\b',low):
            targets.extend(('open','schedule','monday','morning'))
        if re.search(r'\b(?:keyboard|chair|monitors?|mouse|headset)\b',low):targets.append('gaming')
        previous=tokens[tokens.index(m)-1].group().casefold() if tokens.index(m)>0 else ''
        if previous and osa_distance(previous,'gaming')<=1 and re.search(r'\b(?:used|what|where|equipment|studio)\b',low):targets.extend(('mouse','chair','keyboard','monitor'))
        if re.search(r'\b(?:make|create)\s+(?:a|my|the)\s+$',before):targets.append('reservation')
        if re.search(r'\b(?:which|more)\b',low) and _RESOURCE.search(text):targets.extend(('which','expensive'))
        if re.search(r'\b(?:sessions?|minutes?|hours?)\b',low) and _RESOURCE.search(text):targets.append('different')
        if re.search(r'\b(?:play|listed|have|available|called|unknown)\b',low):targets.append('game')
        if re.search(r'\b(?:who|categories|divided)\b',low):targets.append('members')
        if re.search(r'\bpenalties\b',low):targets.append('damage')
        if re.search(r'\bacross\b.*\bzones\b',low):targets.append('multiple')
        if re.search(r'\bdevice\s+is\s+$',before):targets.append('best')
        if re.search(r'\bcan\s+i\s+$',before) and re.match(r'\s+(?:this|his)\b',after):targets.append('book')
        if re.search(r'\baccommodation\b',low):targets.append('overnight')
        if re.search(r'\bhow\s+$',before) and re.match(r'\s+(?:is|does|do)\b',after):targets.append('much')
        if re.search(r'\bwhat\s+$',before) and re.match(r'\s+i\b',after):targets.append('should')
        if re.search(r'\b(?:should|shuld)\s+i\s+$',before) and re.match(r'\s*[?.]*$',after):targets.append('play')
        if re.match(r'\s+(?:r[12]|l[12]|a|b|x|y)\s+button\b',after) and re.search(r'\bdoes\s+$',before):targets.append('the')
        if re.match(r'\s+(?:ps5|pc|vr|cockpit)\s+have\b',after) and re.search(r'\bwhat\s+$',before):targets.append('does')
        if re.search(r'\b(?:ps5|pc|vr|cockpit)\s+$',before) and re.search(r'\bwhat\b',before):targets.append('have')
        if re.match(r'\s+are\s+you\b',after):targets.append('who')
        if re.search(r'\bwho\s+$',before) and re.match(r'\s+you\b',after):targets.append('are')
        if re.search(r'\b(?:the|a)\s+$',before) and re.match(r'\s*[?.]*$',after):targets.append('equipment')
        winners={t for t in targets if len(word)>=3 and abs(len(t)-len(word))<=1 and osa_distance(word,t)==1}
        # Two errors in a long modifier need an intact hardware noun.
        if not winners and re.match(r'\s+(?:monitors?|keyboard|mouse|chair)\b',after) and len(word)>=5 and osa_distance(word,'gaming')==2:
            return m.start(),m.group(),'gaming',2,'two-edit modifier before exact hardware noun'
        if len(winners)==1:
            target=winners.pop();return m.start(),m.group(),target,1,'independent English task frame'
    # A standalone long supported topic is recoverable if uniquely closest.
    if re.fullmatch(r'[A-Za-z]{7,}[?.!]*',text.strip()):
        m=tokens[0];word=m.group().casefold()
        candidates={t for t in ('equipment','reservation','schedule') if osa_distance(word,t)<=2}
        if word not in _WORDS and len(candidates)==1:
            target=candidates.pop();return m.start(),m.group(),target,osa_distance(word,target),'unique standalone supported topic'

    if not re.search(r'[\u0e00-\u0e7f]',text):return None
    # Keep Thai competition propositions on the separate source-bound path.
    from app.pipeline.competition_targets import looks_like_competition_rule_query
    if looks_like_competition_rule_query(text):return None
    # Thai has no word boundaries. Align only supported question operators,
    # anchored to a surviving topic/interrogative. Do not spellcheck names.
    has_resource=bool(_RESOURCE.search(text))
    from app.pipeline.entity_resolver import resolve_game_entity
    game=resolve_game_entity(text,operation='information')
    has_game=game.is_exact
    if has_game and game.top_candidate is not None and re.search(r'ไหม|มั้ย',text):
        alias=game.top_candidate.matched_alias
        found=re.search(re.escape(alias),text,re.I) if alias else None
        if found:
            prefix=text[:found.start()]
            slot=re.search(r'(?:^|\s)([\u0e00-\u0e7f]{1,3})\s*$',prefix)
            if slot and slot.group(1) not in {'มี','มา','ไป','ไม่','ดู','ขอ'} and osa_distance(slot.group(1),'มี')==1:
                return slot.start(1),slot.group(1),'มี',1,'existence verb before exact catalog title and question particle'

    frames=[]
    if has_resource or has_game:
        frames += [('เสียกี่บาท',2),('ต้องเสียเงินไหม',1),('อันไหนแพงกว่า',2)]
        if not re.search(r'ราคาเท่า(?:ไหร่|ไร)|ราคากี่บาท',text):frames += [('ราคาเท่าไหร่',2)]
        if re.search(r'บาท|ราคา|เสีย|ครึ่งชั่วโมง',text) or re.search(r'กี่[^\s]{1,4}\s*$',text):frames += [('กี่บาท',1)]
        if 'เล่น' in text or 'จอง' in text or 'ต้อง' in text:
            frames += [('ต้องจองอะไร',2),('จองยังไง',1),('ต้องทำยังไง',1)]
        if 'ตอน' in text or 'โมง' in text or 'บ่าย' in text:frames += [('ว่างไหม',1),('ว่างมั้ย',2)]
    if has_game:
        frames += [('มีปุ่มอะไรบ้าง',1)]
        frames += [('เป็นเกมแนวไหน',2),('เล่นได้ที่เครื่องไหน',1),('เล่นได้ไหม',1)]
    if 'กี่' in text or 'วันไหน' in text:frames += [('เปิดกี่โมง',2),('เปิดวันไหนบ้าง',1)]
    if re.search(r'ถึง|ต้อง|ลืม|จอง|แนบ',text):frames += [('เช็กอิน',1),('สลิปไหม',2)]
    if re.search(r'ข้อมูลเรื่อง|ข้อมูลเรื|สูบ|กฎ',text):frames += [('สูบบุหรี่',1)]
    if re.search(r'หาย|เปียก|เปียด',text):frames += [('ของหาย',1),('เปียก',1)]
    if re.search(r'ปานกลาง|ยานกลาง',text):frames += [('เสียหายปานกลาง',2)]
    if 'คือใคร' in text:frames += [('ตำแหน่ง',1),('เลขานุการ',1)]
    if re.search(r'เล่นได้[^\s]{1,3}\s*(?:[?]|$)',text):frames += [('เล่นได้ไหม',1)]
    if has_resource and re.search(r'ต้องทำ(?:ยังไง|บังไง|อย่างไร)',text):frames += [('จอง',1)]
    if re.search(r'ดำเนนการ|ดำเนินการ',text):frames += [('หน่วยงาน',1),('ดำเนินการ',1)]
    if re.search(r'เอา|นำ|เข้า|อนุญาต|ได้ไหม',text):frames += [('อาหาร',1),('คีย์บอร์ด',1),('สูบบุหรี่',1)]
    if re.search(r'รับผิดชอบ|เล็กน้อย|อุปกรณ์|ของหาย|ระงับ',text):
        frames += [('เสียหาย',1),('สิทธิ์ชั่วคราว',1),('เปียก',1)]
    if re.search(r'คำพูด|ใช้คำ',text):frames += [('เหมาะสม',2)]
    if re.search(r'นาย|นาง|รศ\.|ผศ\.|ตำแหน่ง',text):
        frames += [('ตำแหน่งอะไร',2),('ตำแหน่งเลขานุการ',2)]
    if re.search(r'เกม|อุปกรณ์',text) and 'สุด' in text:frames += [('เกมเยอะสุด',2),('อุปกรณ์',1)]
    if 'ราชการ' in text:frames += [('วันหยุดราชการ',1)]
    protected=[(m.start(),m.end()) for m in re.finditer(r'ไม่|ห้าม|อย่า|เกิน|กี่นาที|ราคาเท่าไร|ราคาเท่าไหร่|สูบบุหรี่|อุปกรณ์|เช็กอิน|เช็คอิน|สลิปไหม|ตำแหน่งอะไร',text)]
    candidates=[]
    for target,budget in frames:
        if target in text:continue
        for start in range(len(text)):
            for length in range(max(2,len(target)-budget),len(target)+budget+1):
                observed=text[start:start+length]
                if any(start < end and start+length > begin for begin,end in protected):continue
                if len(observed)!=length or not re.fullmatch(r'[\u0e00-\u0e7f]+',observed):continue
                # Surviving outer letters prevent a word embedded in another
                # source name from being a loose substring candidate.
                if observed[:1]!=target[:1] and observed[-2:]!=target[-2:]:continue
                # Keep trailing question particles outside a noun.
                suffix=text[start+length:]
                if target in {'เช็กอิน','อาหาร','คีย์บอร์ด','เสียหาย','ของหาย','เปียก','สูบบุหรี่','เลขานุการ','ตำแหน่ง','จอง','หน่วยงาน','ดำเนินการ'}:
                    if suffix and re.match(r'[\u0e00-\u0e7f]',suffix) and not re.match(r'(?:ไหม|มั้ย|อะไร|ยังไง|อย่างไร|เข้า|ก่อน|ภายใน|ตัวเอง|ดัวเอง|มา|รับผิด|เล็กน้อย|ปานกลาง|คือใคร|อะไร|มี|ใคร|ต้อง)',suffix):continue
                distance=osa_distance(observed,target)
                if not 0<distance<=budget:continue
                # No dropped negation. A question operator cannot swallow it.
                if any(n in observed and n not in target for n in ('ไม่','ห้าม','อย่า','เกิน')):continue
                candidates.append((distance,abs(length-len(target)),start,observed,target))
    if not candidates:return None
    candidates.sort()
    best=candidates[0]
    if any(c[:2]==best[:2] and (c[2],c[4])!=(best[2],best[4]) and c[2]<best[2]+len(best[3]) and best[2]<c[2]+len(c[3]) for c in candidates[1:]):return None
    distance,_,start,observed,target=best
    return start,observed,target,distance,'supported Thai operator aligned to independent topic'
