"""Source-bound answers for explicit price choices, booking targets and gaps."""
import json,re
from pathlib import Path
from functools import lru_cache
from app.pipeline.structured_tools import StructuredToolResult,_booking_services_for_game,_availability_source_hits
from app.pipeline.entity_resolver import resolve_game_entity
from app.pipeline.service_fee_alternatives import answer_fee_alternatives

_ROOT=Path(__file__).resolve().parents[2]
_MEDIA=re.compile(r'ถ่าย(?:รูป|ภาพ|วิดีโอ|วีดีโอ)|\b(?:photo(?:graph)?s?|video|filming|recording)\b',re.I)

@lru_cache(maxsize=1)
def _recorded_media_policy_present():
    data=json.loads((_ROOT/'data/curated/service_policy_answers.json').read_text(encoding='utf-8'))
    for claim in data.get('claims',{}).values():
        if _MEDIA.search(json.dumps(claim,ensure_ascii=False)):return True
    for relative in ('data/rules/reservation_rules.jsonl','data/curated/rule_patterns.jsonl'):
        p=_ROOT/relative
        if not p.exists():continue
        for line in p.read_text(encoding='utf-8').splitlines():
            row=json.loads(line)
            if row.get('category') not in ('reservation','rules','policy'):continue
            answer=str(row.get('answer') or row.get('text') or '')
            if _MEDIA.search(answer):return True
    return False

def _media_policy_gap(query,locale):
    context=bool(re.search(r'ศูนย์|สตูดิโอ|ภายใน|\b(?:studio|inside)\b',query,re.I))
    permission=bool(re.search(r'ได้ไหม|ได้มั้ย|อนุญาต|กฎ|นโยบาย|\b(?:may|can|allowed|permission|policy)\b',query,re.I))
    if not (context and permission and _MEDIA.search(query)) or _recorded_media_policy_present():return None
    english=locale=='en'
    answer=('I could not find a verified studio policy on taking photos or recording video. Please ask the studio staff whether recording is allowed and what consent or area restrictions apply.' if english else
            'ยังไม่พบนโยบายของศูนย์ที่ยืนยันได้เกี่ยวกับการถ่ายภาพหรือวิดีโอครับ กรุณาสอบถามเจ้าหน้าที่ว่าถ่ายได้หรือไม่ ต้องขอความยินยอมจากใคร และมีพื้นที่ใดที่จำกัดการถ่าย')
    return StructuredToolResult(answer,[],'studio_media_policy_no_answer',.98,{'missing_original_policy':'photo_video_permission','owner_question':'permission, consent and restricted areas','not_a_translation_gap':True})

def _booking_resource(query,locale):
    english=locale=='en'
    explicit=bool(re.search(r'\b(?:what|which)\b.*\b(?:need\s+to\s+book|(?:service|zone|station|device).*\bbook)\b.*\bplay\b',query,re.I)) if english else bool(re.search(r'(?:ต้องจองอะไร|จอง(?:โซน|เครื่อง|บริการ)ไหน|จองอะไร.*เล่น|เล่น.*จองอะไร)',query))
    if not explicit:return None
    resolution=resolve_game_entity(query,operation='availability')
    if not resolution.is_exact or resolution.top_candidate is None:return None
    game=resolution.top_candidate.title;rows=_booking_services_for_game(game)
    if not rows:return None
    lines=[f'To play {game}, select one of these recorded services when booking:' if english else f'ถ้าจะเล่น {game} ให้เลือกบริการที่มีเกมนี้ตอนจอง:']
    seen=set()
    for row in rows:
        label=str(row.get('service_label') or row.get('machine_label') or row.get('zone') or '')
        zone=str(row.get('zone') or '')
        value=f'{zone} - {label}' if zone and zone.casefold() not in label.casefold() else label
        if english:
            value=re.sub(r'(\d+)\s*ชั่วโมง',r'\1 hour(s)',value)
            value=re.sub(r'(\d+)\s*นาที',r'\1 minutes',value)
        if value and value not in seen:lines.append(('• ' if english else '•    ')+value);seen.add(value)
    if not seen:return None
    lines += (['Booking steps:','• Select a service.','• Choose a date and time.','• Fill in your user information.','• Review the details.','• Pay by bank transfer.','• Upload the payment slip.','These are catalog choices; live slot availability must be checked for your date and time.'] if english else
              ['ขั้นตอนจอง: เลือกบริการ วันและรอบเวลา กรอกข้อมูล ตรวจสอบรายละเอียด ชำระเงินและแนบสลิป','รายการนี้เป็นบริการที่มีเกมตามข้อมูลที่บันทึกไว้ สถานะว่างต้องตรวจตามวันที่และเวลาที่ต้องการอีกครั้ง'])
    hits=_availability_source_hits(rows)
    for url in dict.fromkeys(h.get('metadata',{}).get('source_url','') for h in hits):
        if url:lines.append(('Source: ' if english else 'แหล่งข้อมูล: ')+url)
    return StructuredToolResult('\n'.join(lines),hits,'structured_booking_game_service_selection',.97,{'game':game,'services':sorted(seen),'catalog_only':True})

def answer_closed_query_improvement(query,locale):
    for category,resolver in [('service_fee',answer_fee_alternatives),('reservation',_booking_resource),('no_answer',_media_policy_gap)]:
        result=resolver(query,locale)
        if result is not None:return ('clarification' if 'clarification' in result.mode else category),result
    return None
