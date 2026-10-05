"""Parse bounded competition requests and context-dependent continuations."""
from __future__ import annotations
import re
import unicodedata
from app.core.typo_similarity import osa_distance

_THAI_WORDS = r"(?:ขอ|ดู|เอา|แล้ว|อยากรู้|อยากดู|บอก|สรุป|มี|เรื่อง|ของ|เกมนี้|เกม|กฎ|กติกา|ระเบียบ|การ|ตอน|แข่งขัน|แข่ง|ทัวร์นาเมนต์|อะไร|ไร|บ้าง|มั่ง|อื่น|เพิ่มเติม|เพิ่ม|อีก|ทั้งหมด|ไหม|มั้ย|หน่อย|ครับ|ค่ะ|คับ|\s|[?!.,])+"
_ENGLISH_WORDS = r"(?:can|could|i|we|you|see|show|tell|give|me|please|pls|what|which|are|is|there|the|a|an|and|any|about|it|its|this|game|of|for|tournament|competition|rules|rule|regulations|other|more|additional|all|overview|summarize|\s|[?!.,])+"

def _clean(query: str) -> str:
    q=unicodedata.normalize('NFC',str(query or '')).casefold().strip(' ?!.,')
    return re.sub(r'(?:รายการ)+(?=แข่ง)','รายการ',q).replace('กฏ','กฎ')

def is_rulebook_catalog_request(query: str) -> bool:
    q=re.sub(r'\s+','',_clean(query))
    thai=re.fullmatch(
        r'(?:ตอนนี้)?(?:มี)?(?:รายการแข่ง|รายการแข่งขัน|เกมแข่ง|เกมแข่งขัน)(?:มี)?(?:อะไรบ้าง|ไรบ้าง|อะไรมั่ง|ไรมั่ง|ไหนบ้าง)(?:ครับ|ค่ะ|คับ)?'
        r'|(?:ตอนนี้)?(?:มี)?เกม(?:อะไร|ไร|ไหน)(?:ให้|ที่)?(?:รายการ)?(?:แข่ง|แข่งขัน)(?:ได้)?(?:บ้าง|มั่ง)?(?:ครับ|ค่ะ|คับ)?'
        r'|(?:ตอนนี้)?(?:รายการ)?(?:แข่ง|แข่งขัน)เกม(?:อะไร|ไร|ไหน)(?:ได้)?(?:บ้าง|มั่ง)(?:ครับ|ค่ะ|คับ)?',q)
    english=re.fullmatch(
        r'(?:what|which) (?:tournaments|competitions|competition games)(?: are (?:there|available|recorded))?'
        r'|list (?:the )?(?:tournaments|competitions|competition games)'
        r'|(?:what|which) games (?:can (?:we|i) compete in|are (?:there|available) for competition)',_clean(query))
    return bool(thai or english)

def competition_choice_text(query: str) -> str:
    q=_clean(query)
    q=re.sub(r'^(?:(?:แล้ว|ขอ|เลือก|เอา|เกม)\s*)+|^(?:and|then|what about|for|the game)\s+', '', q).strip()
    return re.sub(r'(?:ครับ+|ค่ะ+|คับ+|หน่อย+|ล่ะ|please|pls)\s*$', '', q).strip(' ?!.,')

def _generic_rule_text(query: str) -> str:
    from app.pipeline.competition_targets import resolve_competition_targets,replace_competition_target_mentions
    resolution=resolve_competition_targets(query)
    if resolution.status=='exact':query=replace_competition_target_mentions(query,resolution,'')
    elif resolution.status!='absent':return ''
    q=_clean(query)
    if re.search(r'กฎ|กติกา',q):
        # Repeated courtesy letters carry no policy, edition or entity data.
        q=re.sub(r'(?:ครับ+|ค่ะ+|คับ+)\s*$','',q).rstrip()
        q=re.sub(r'หน+่?อ+ย+$','หน่อย',q)
        for size in (5,4,6):
            suffix=q[-size:];prefix=q[:-size].rstrip()
            if re.fullmatch(_THAI_WORDS,prefix) and re.search(r'กฎ|กติกา',prefix) and osa_distance(suffix,'หน่อย')<=1:
                q=prefix;break
    # A misspelled rule word requires independent request grammar. Ordinary
    # real words are protected; this is not a global nearest-word rewrite.
    if re.search(r'\b(?:can|could|show|give|tell|any|other|more|competition|tournament)\b',q):
        for match in reversed(list(re.finditer(r'[a-z]+',q))):
            word=match.group()
            if word not in {'rules','rule','roles','runes','rues','ruse'} and len(word)>=4 and osa_distance(word,'rules')==1:
                candidate=q[:match.start()]+'rules'+q[match.end():]
                if re.fullmatch(_ENGLISH_WORDS,candidate):q=candidate
    return q.strip(' ?!.,')

def is_broad_rule_request(query: str) -> bool:
    q=_generic_rule_text(query)
    return bool(q and re.search(r'กฎ|กติกา|\brules?\b|\bregulations\b',q) and (re.fullmatch(_THAI_WORDS,q) or re.fullmatch(_ENGLISH_WORDS,q)))

def is_contextual_more_request(query: str) -> bool:
    """A continuation shape only; the caller must supply an active rulebook."""
    q=_clean(query)
    thai=re.fullmatch(r'(?:แล้ว|ขอ|มี|ข้อ|อัน|อื่น|อีก|เพิ่มเติม|เพิ่ม|ต่อ|หน่อย|ยัง|เหลือ|อะไร|ไร|บ้าง|มั่ง|ไหม|มั้ย|เปล่า|ป่าว|ปะ|ล่ะ|ครับ|ค่ะ|คับ|\s)+',q)
    english=re.fullmatch(r'(?:anything else|(?:any )?(?:more|other)(?: please| pls)?|(?:please )?(?:continue|go on))',q)
    return bool((thai and re.search(r'อื่น|เพิ่มเติม|เพิ่ม|อีก|ต่อ',q)) or english)

def is_more_rule_request(query: str) -> bool:
    q=_generic_rule_text(query)
    return (is_broad_rule_request(query) and bool(re.search(r'อื่น|เพิ่มเติม|เพิ่ม|อีก|\b(?:more|other|additional)\b',q))) or is_contextual_more_request(query)
