"""Calculate each explicit duration choice from the unchanged fee table."""
import math,re
from app.core.duration_alternatives import parse_duration_alternatives
from app.core.normalization import SERVICE_ALIASES,contains_alias,has_price_intent
from app.calculator.service_fee import SERVICE_FEES,GROUP_LABELS,_detect_group
from app.core.source_registry import SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,make_source_hits
from app.pipeline.structured_tools import StructuredToolResult

def answer_fee_alternatives(query,locale):
    choices=parse_duration_alternatives(query)
    if choices is None or not (has_price_intent(query) or 'much' in query.casefold()):return None
    services=[key for key,aliases in SERVICE_ALIASES.items() if contains_alias(query,aliases,fuzzy=False)[0]]
    if len(services)!=1:return None
    service=services[0]
    english=locale=='en'
    if re.search(r'ไม่(?:เอา|ใช่|ต้องการ)?\s*$|\b(?:not|without|except)\s*$',query[max(0,choices.start-18):choices.start],re.I):
        answer=('Which duration should I price? Your question negates one of the listed durations.' if english else
                'ต้องการให้คิดราคาสำหรับระยะเวลาใดครับ ในคำถามมีการปฏิเสธหนึ่งในระยะเวลาที่ระบุ')
        return StructuredToolResult(answer,[],'duration_alternatives_clarification',.98,{'duration_choices':list(choices.minutes),'reason':'negated_duration'})
    if english:
        from app.pipeline.bilingual_english import _detect_group as detect_group,_GROUP_LABELS_EN,_people
        group=detect_group(query);labels=_GROUP_LABELS_EN;people=_people(query)
    else:
        from app.calculator.service_fee import _detect_people
        group,_,_=_detect_group(query);labels=GROUP_LABELS;people=_detect_people(query)
    lines=['Prices for each requested duration:' if english else 'ราคาสำหรับแต่ละระยะเวลาที่ถาม:'];calculations=[]
    for minutes in choices.minutes:
        keys=([('vr_30' if minutes<=30 else 'vr_60')] if service=='vr' else
              (['nintendo_switch_3_4'] if people and people>=3 else ['nintendo_switch_1_2'] if people else ['nintendo_switch_1_2','nintendo_switch_3_4']) if service=='nintendo_switch' else [service])
        lines.append(f'\nDuration: {minutes} minutes' if english else f'\nระยะเวลา: {minutes} นาที')
        if service=='nintendo_switch' and not people:
            lines.append('The number of players is unspecified; both packages are shown.' if english else 'ยังไม่ระบุจำนวนผู้เล่น จึงแสดงทั้งสองแพ็กเกจ')
        for key in keys:
            fee=SERVICE_FEES[key];sessions=max(1,math.ceil(minutes/fee['minutes_per_session']))
            capacity=fee['capacity'].replace('คน','people') if english else fee['capacity']
            lines.append(f"{fee['label']} ({capacity})")
            for g in [group] if group else ['psu_student_staff','general_student','general_adult']:
                price=fee['prices'][g];total=price*sessions
                lines.append(f'- {labels[g]}: {total:,} THB ({price:,} THB x {sessions} session(s))' if english else f'•    {labels[g]}: {total:,} บาท ({price:,} บาท x {sessions} session)')
                calculations.append({'minutes':minutes,'service_key':key,'group':g,'base_price':price,'sessions':sessions,'total':total})
    source_ids=[SERVICE_FEE_IMAGE_2026_ID]+([PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID] if service=='pc' else [])
    hits=make_source_hits(source_ids)
    for url in dict.fromkeys(h.get('metadata',{}).get('source_url','') for h in hits):
        if url:lines.append(('Source: ' if english else 'แหล่งข้อมูล: ')+url)
    return StructuredToolResult('\n'.join(lines),hits,'structured_service_fee_alternatives',.98,{'duration_choices':list(choices.minutes),'calculations':calculations,'scope':'prices only; booking occupancy is separate'})
