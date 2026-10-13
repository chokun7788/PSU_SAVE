"""Bounded meaning checks with explicit scope; not a universal entailment model."""
from __future__ import annotations
import json,re
from pathlib import Path
from functools import lru_cache

def translation_request(question):
    q=question.strip()
    if not re.match(r'^(?:please\s+)?translate\b|^(?:ช่วย)?แปล',q,re.I):return None
    patterns=[
        r'^(?:please\s+)?translate\s+(?:into|to)\s+(Thai|English)\s*:\s*(.+)$',
        r'^(?:ช่วย)?แปล(?:เป็น|ไปเป็น)\s*(?:ภาษา)?(ไทย|อังกฤษ)\s*[:：]\s*(.+)$',
        r'^(?:please\s+)?translate\s+(?:the\s+(?:Thai|English)\s+(?:sentence|text)\s+)?(.+?)\s+(?:into|to)\s+(Thai|English)\s*[.!?]*$',
        r'^(?:ช่วย)?แปล(?:ประโยค|ข้อความ|คำว่า)?\s*(.+?)\s*(?:เป็น|ไปเป็น)\s*(?:ภาษา)?(ไทย|อังกฤษ)\s*(?:ให้หน่อย|ด้วย|ครับ|ค่ะ)?\s*$',
    ]
    for index,pattern in enumerate(patterns):
        m=re.search(pattern,q,re.I|re.S)
        if m:
            source_group,target_group=(2,1) if index<2 else (1,2)
            source=m.group(source_group).strip().strip('"\'“”‘’` ')
            target='th' if m.group(target_group).casefold() in ('thai','ไทย') else 'en'
            return dict(source=source,target=target,extraction='explicit_source_target')
    return dict(source='',target=None,extraction='unresolved')

def _numbers(text):
    text=text.translate(str.maketrans('๐๑๒๓๔๕๖๗๘๙','0123456789'))
    return sorted(re.findall(r'(?<!\w)\d+(?:[.,:]\d+)*(?!\w)',text))

def _negative(text):
    return bool(re.search(r"\b(?:not|no|never|cannot|can't|mustn't|don't|doesn't|without)\b|ไม่|ห้าม",text,re.I))

def translation_errors(source,answer,target):
    errors=[]
    def add(reason):errors.append(dict(type='accuracy',reason=reason,severity='major'))
    if _numbers(source)!=_numbers(answer):add('number_preservation')
    entities=re.findall(r'\b(?:PC\s*\d+|PS\s*5|VR\s*\d*|Cockpit\s*#?\s*\d+)\b',source,re.I)
    for entity in entities:
        compact=re.sub(r'\s','',entity)
        if not re.search(r'(?<![A-Za-z0-9])'+re.escape(compact)+r'(?![A-Za-z0-9])',re.sub(r'\s','',answer),re.I):add('entity_preservation')
    if _negative(source)!=_negative(answer):add('negation_preservation')
    # Check numeric uncertainty only; polite words are not treated as additions.
    approximation=r'\b(?:about|approximately|roughly|around)\s+\d|ประมาณ\s*[๐-๙0-9]'
    if bool(re.search(approximation,source,re.I))!=bool(re.search(approximation,answer,re.I)):
        add('numeric_approximation_changed')
    terms=[(r'\bnetworks?\b|เครือข่าย',r'เครือข่าย|เน็ตเวิร์ก',r'\bnetworks?\b'),
           (r'\binternet\b|อินเทอร์เน็ต|อินเตอร์เน็ต',r'อินเทอร์เน็ต|อินเตอร์เน็ต',r'\binternet\b'),
           (r'\bminutes?\b|นาที',r'นาที',r'\bminutes?\b'),
           (r'\bhours?\b|ชั่วโมง',r'ชั่วโมง',r'\bhours?\b')]
    for src,th,en in terms:
        if re.search(src,source,re.I) and not re.search(th if target=='th' else en,answer,re.I):add('term_or_unit_preservation')
    if re.search(r'\bnetworks?\b|เครือข่าย',source,re.I) and not re.search(r'\binternet\b|อินเทอร์เน็ต|อินเตอร์เน็ต',source,re.I):
        if re.search(r'อินเทอร์เน็ต|อินเตอร์เน็ต|\binternet\b',answer,re.I):add('network_scope_narrowed')
    if target=='th' and not re.search(r'[ก-๙]',answer):add('target_language')
    if target=='en' and re.search(r'[ก-๙]',answer):add('target_language')
    return errors

@lru_cache(maxsize=1)
def _cards():
    path=Path(__file__).resolve().parents[2]/'data/general_evidence/technical_facts_20261009.json'
    data=json.loads(path.read_text(encoding='utf-8'))
    if data.get('scope')!='general_technical_knowledge_not_studio_policy':raise ValueError('invalid general evidence scope')
    return data['cards']

def evidence_for(question,profile):
    if profile in ('translation','short_creation') or re.search(r'\b(?:write|draft|compose|invite|invitation)\b|ช่วยเขียน|ชวน|เชิญ',question,re.I):return []
    if re.search(r'psu|studio|ศูนย์|ค่าบริการ|จอง|กติกา|\b(?:booking|price|tournament)\b',question,re.I):return []
    return [c for c in _cards() if re.search(c['pattern'],question,re.I)]

def evidence_prompt(cards):
    if not cards:return ''
    return '\nREFERENCE FACTS (reviewed general technical sources, not studio policy):\n'+'\n'.join(f"[{c['id']}] {c['facts']} Source: {', '.join(c['sources'])}" for c in cards)+'\nUse these facts and their qualifiers. Do not claim details unsupported by this reference.\n'

def semantic_errors(question,answer,profile):
    errors=[]
    tr=translation_request(question) if profile=='translation' else None
    if tr and tr['source']:
        errors.extend(translation_errors(tr['source'],answer,tr['target']))
    # Literal quoted Note/QUESTION is valid translation data. Never strip it.
    if profile!='translation':
        if re.search(r'(?:the term|important term|keyword).{0,65}(?:preserv|retain)|(?:ตาม|from|part of).{0,35}(?:original query|prompt)|คงคำสำคัญ.{0,25}(?:ตามคำถาม|ตามคำสั่ง)|^(?:QUESTION|ANSWER):',answer,re.I|re.M):
            errors.append(dict(type='addition',reason='instruction_commentary',severity='major'))
        if re.search(r'clarifying question\s*:|คำถาม(?:เพื่อ)?(?:ชี้แจง|เพิ่มเติม)\s*:',answer,re.I):
            errors.append(dict(type='addition',reason='unnecessary_clarifying_tail',severity='major'))
    if profile=='two_sentences' and re.search(r'\b(?:invitation|invite)\b|เชิญ|ชวน',question,re.I):
        if re.search(r'^(?:Hi|Hello|Hey)(?:\s+everyone)?[!.]|^สวัสดี[^\n]*[!\n]',answer,re.I):
            errors.append(dict(type='coverage',reason='greeting_consumes_invitation_sentence',severity='minor'))
    cards=evidence_for(question,profile);ids={c['id'] for c in cards}
    if 'ping' in ids and not _negative(answer):
        if re.search(r'\b(?:measures?|tests?)\b.{0,30}(?:bandwidth|throughput)|ทดสอบความเร็ว|วัดความเร็ว',answer,re.I) and not re.search(r'ICMP|round.?trip|RTT|เวลาตอบกลับ|เวลาไปกลับ',answer,re.I):
            errors.append(dict(type='factuality',reason='ping_bandwidth_claim',severity='major'))
    if 'http' in ids:
        if re.search(r'(?:HTTP|TLS).{0,35}(?:operates?|runs?|works?|requires?|ทำงาน|ใช้).{0,20}(?:over\s+|on\s+top\s+of\s+)?TCP',answer,re.I) and not re.search(r'HTTP[/ -]?[123]|QUIC|commonly|typically|usually|โดยทั่วไป|มัก',answer,re.I):
            errors.append(dict(type='factuality',reason='transport_version_qualifier_missing',severity='major'))
    if 'memory' in ids:
        if re.search(r'RAM\s+(?:retains?|keeps?|preserves?).{0,35}(?:after|without).{0,20}power|RAM.{0,20}(?:คง|เก็บ).{0,25}ข้อมูล.{0,15}(?:หลังปิด|ไม่มีไฟ)',answer,re.I):
            errors.append(dict(type='factuality',reason='ram_nonvolatile_claim',severity='major'))
    return errors,dict(translation_extraction=tr['extraction'] if tr else None,
                       evidence_ids=[c['id'] for c in cards],
                       sources=list(dict.fromkeys(s for c in cards for s in c['sources'])),
                       semantic_verification='bounded_constraints_only',all_claims_verified=False)
