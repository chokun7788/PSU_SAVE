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
    if not resolution.is_exact or resolution.top_candidate is None:
        answer=('Please specify the full game title and edition. I cannot select a booking service without a verified game-to-service match.' if english else
                'กรุณาระบุชื่อเกมและภาคให้ชัดเจนครับ ยังเลือกบริการให้ไม่ได้จนกว่าจะพบเกมที่ตรงกับรายการบริการที่ยืนยันได้')
        return StructuredToolResult(answer,[],'booking_game_target_clarification',.98,{'resolution':resolution.as_dict(),'no_inferred_booking_service':True})
    game=resolution.top_candidate.title;rows=_booking_services_for_game(game)
    if not rows:
        answer=(f'I could not find a recorded booking service for {game}. Please check with studio staff before booking for this game.' if english else
                f'ยังไม่พบบริการจองที่มี {game} ในรายการที่บันทึกไว้ครับ กรุณาตรวจสอบกับเจ้าหน้าที่ก่อนจองเพื่อเล่นเกมนี้')
        return StructuredToolResult(answer,[],'booking_game_service_no_answer',.98,{'game':game,'no_inferred_booking_service':True})
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

def _fee_catalog(query,locale):
    from app.core.normalization import has_price_intent,SERVICE_ALIASES,contains_alias
    if not (has_price_intent(query) or 'ค่าเล่น' in query or re.search(r'\b(?:prices?|fees?|costs?)\b',query,re.I)):return None
    if not re.search(r'แต่ละ(?:เครื่อง|โซน|บริการ)|ตาราง.*ราคา|ค่าบริการ.*ทั้งหมด|ราคา.*ทั้งหมด|ค่าเล่น.*(?:เครื่อง|โซน).*บ้าง|\b(?:each|all)\s+(?:service|zone|device|station)s?\b',query,re.I):return None
    if any(contains_alias(query,a,fuzzy=False)[0] for a in SERVICE_ALIASES.values()):return None
    from app.calculator.service_fee import SERVICE_FEES,GROUP_LABELS
    from app.pipeline.bilingual_english import _GROUP_LABELS_EN
    from app.core.source_registry import SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,make_source_hits
    en=locale=='en';labels=_GROUP_LABELS_EN if en else GROUP_LABELS
    lines=['Service Fee table (recorded package rates):' if en else 'ตาราง Service Fee สำหรับทุกบริการ (ราคาต่อแพ็กเกจ):']
    for key,fee in SERVICE_FEES.items():
        capacity=('1 person' if fee['capacity']=='1 คน' else fee['capacity'].replace('คน','people')) if en else fee['capacity']
        lines.append(f"\n{fee['label']} ({capacity}), {fee['minutes_per_session']} "+('minutes/session' if en else 'นาที/รอบ'))
        for group,price in fee['prices'].items():
            lines.append(f"•    {labels[group]}: {price:,} "+('THB' if en else 'บาท'))
    hits=make_source_hits([SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID])
    lines.append('PC rates include the local service fee update 2026-07-27.' if en else 'ราคา PC อ้างอิง local service fee update 2026-07-27')
    for url in dict.fromkeys(h.get('metadata',{}).get('source_url','') for h in hits):
        if url:lines.append(('Source: ' if en else 'แหล่งข้อมูล: ')+url)
    return StructuredToolResult('\n'.join(lines),hits,'structured_service_fee_catalog',.98,{'catalog_only':True,'prices_unchanged':True})

def _fee_comparison(query,locale):
    from app.core.normalization import SERVICE_ALIASES,contains_alias
    from app.pipeline.source_task_signals import fee_comparison_query
    if not fee_comparison_query(query):return None
    services=[key for key,aliases in SERVICE_ALIASES.items() if contains_alias(query,aliases,fuzzy=False)[0]]
    if len(services)<2:return None
    from app.calculator.service_fee import SERVICE_FEES,GROUP_LABELS
    from app.pipeline.bilingual_english import _GROUP_LABELS_EN
    from app.core.source_registry import SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,make_source_hits
    en=locale=='en';labels=_GROUP_LABELS_EN if en else GROUP_LABELS
    lines=['Recorded package prices for all requested services:' if en else 'ราคาต่อแพ็กเกจของทุกบริการที่ถาม:']
    # Do not assume an entitlement, duration or shared capacity to pick a winner.
    # Display each distinct source rate; ask what comparison the user needs.
    selected=[(key,fee) for key,fee in SERVICE_FEES.items() if any(key==service or key.startswith(service+'_') for service in services)]
    for key,fee in selected:
        capacity=('1 person' if fee['capacity']=='1 คน' else fee['capacity'].replace('คน','people')) if en else fee['capacity']
        lines.append(f"\n{fee['label']} ({capacity}), {fee['minutes_per_session']} "+('minutes/session' if en else 'นาที/รอบ'))
        for group,price in fee['prices'].items():lines.append(f"- {labels[group]}: {price:,} "+('THB' if en else 'บาท'))
    lines.append('Packages have different durations/capacities. Which user group, duration and number of players should I compare?' if en else 'แพ็กเกจมีระยะเวลาและจำนวนผู้เล่นต่างกัน ต้องการเทียบสำหรับกลุ่มผู้ใช้ใด เล่นนานเท่าไร และกี่คนครับ?')
    hits=make_source_hits([SERVICE_FEE_IMAGE_2026_ID]+([PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID] if 'pc' in services else []))
    for url in dict.fromkeys(h.get('metadata',{}).get('source_url','') for h in hits):
        if url:lines.append(('Source: ' if en else 'แหล่งข้อมูล: ')+url)
    return StructuredToolResult('\n'.join(lines),hits,'structured_service_fee_comparison',.98,{'services':services,'source_rates_only':True,'no_assumed_group_or_duration':True})

def _non_catalog_request(query,locale):
    en=locale=='en'
    personal=bool(re.search(r'คีย์บอร์ด.{0,6}(?:ตัวเอง|ดัวเอง|ส่วนตัว)|เมาส์.{0,6}(?:ตัวเอง|ส่วนตัว)|\b(?:my|own|personal)\s+(?:keyboard|mouse|controller)\b',query,re.I))
    permission=bool(re.search(r'มาใช้|นำ|เอา|ได้ไหม|\b(?:bring|use|allowed)\b',query,re.I))
    if personal and permission:
        answer=('I could not find a verified general studio policy allowing replacement of the studio keyboard, mouse or controller with a personal peripheral. Please ask staff whether your device is allowed and how it must be connected.' if en else 'ยังไม่พบนโยบายการใช้บริการทั่วไปที่ยืนยันได้ว่านำคีย์บอร์ด เมาส์ หรือคอนโทรลเลอร์ส่วนตัวมาสลับกับชุดของศูนย์ได้ครับ กรุณาถามเจ้าหน้าที่ว่าอุปกรณ์ของคุณใช้ได้หรือไม่ และต้องเชื่อมต่ออย่างไร')
        return StructuredToolResult(answer,[],'personal_peripheral_policy_no_answer',.97,{'missing_general_policy':True,'competition_policy_not_reused':True})
    if re.search(r'ส่งเครื่อง.*ไปบ้าน|\b(?:deliver|delivery|ship)\b.*\b(?:home|house)\b',query,re.I):
        answer=('I could not find verified information that the studio delivers gaming equipment to users at home. Please ask the studio directly about this service.' if en else 'ยังไม่พบข้อมูลที่ยืนยันได้ว่าศูนย์มีบริการส่งเครื่องเกมไปที่บ้านครับ กรุณาสอบถามศูนย์โดยตรงเกี่ยวกับบริการนี้')
        return StructuredToolResult(answer,[],'equipment_home_delivery_no_answer',.98,{'missing_service':'home_equipment_delivery'})
    return None

def _contact_fields(query,locale):
    if not (re.search(r'อีเมล|\be-?mail\b',query,re.I) and re.search(r'เบอร์|โทร|\b(?:phone|telephone|tel)\b',query,re.I)):return None
    if re.search(r'ส่วนตัว|\b(?:personal|private)\b',query,re.I):return None
    if not re.search(r'ศูนย์|สตูดิโอ|ติดต่อ|\b(?:studio|contact)\b',query,re.I):return None
    from app.rules.matcher import RuleMatcher
    from app.pipeline.bilingual_english import _rule_answer
    from app.core.source_registry import make_source_hits
    matcher=RuleMatcher.default()
    if locale=='en':
        result=_rule_answer('How can I contact the studio',matcher)
        if result is None:return None
        return StructuredToolResult(result.answer,result.hits,'structured_contact_fields',.98,{'required_fields':['email','phone'],'approved_contact_rule':True})
    results=[matcher.match(q,category='contact',locale='th') for q in ('อีเมล','เบอร์โทร')]
    if not all(results):return None
    source_ids=list(dict.fromkeys(source for result in results for source in result.get('source_ids',[])))
    from app.pipeline.retrieval import load_curated_rows,hit_from_curated
    rows={}
    for row in load_curated_rows():
        if row.get('id') and row.get('language','th')=='th' and row.get('text'):
            rows.setdefault(row.get('content_id') or row['id'],row)
    if not source_ids or any(source not in rows for source in source_ids):return None
    if any(result['answer'].strip() not in str(rows[source]['text']) for result in results for source in result.get('source_ids',[])):return None
    hits=[hit_from_curated(rows[source]) for source in source_ids]
    answer='\n'.join(result['answer'] for result in results)
    for url in dict.fromkeys(result.get('source_url','') for result in results):
        if url:answer+='\nแหล่งข้อมูล: '+url
    return StructuredToolResult(answer,hits,'structured_contact_fields',.98,{'required_fields':['email','phone']})

def _recorded_catalog_gap(query,locale):
    # Only a literal title and an explicit studio availability request. General
    # game descriptions, prices, controls and competition questions stay separate.
    if not re.search(r'ศูนย์|สตูดิโอ|\b(?:studio|centre|center)\b',query,re.I):return None
    if re.search(r'ราคา|ค่าบริการ|เท่าไหร่|แนว|กฎ|กติกา|แข่งขัน|\b(?:price|cost|fee|genre|rules?|tournament|controls?|how)\b',query,re.I):return None
    availability=bool(re.search(r'มี.+(?:ไหม|มั้ย|หรือเปล่า)|เล่นได้(?:ไหม|มั้ย)|\b(?:available|offer|have)\b',query,re.I))
    if not availability:return None
    from app.runtime.fast_answer import _match_known_unsupported_game,_verified_game_catalog,HITS,OUR_GAMES_URL
    title=_match_known_unsupported_game(query.casefold())
    if not title:return None
    # The historical name list is only a recognition aid. Absence must be
    # checked against the current verified catalog on every new process.
    candidates={part.strip().casefold() for part in title.split('/')}
    catalog=_verified_game_catalog()
    if not catalog or any(str(row.get('name','')).casefold() in candidates for row in catalog):return None
    answer=(f'I could not find {title} in the studio\'s verified game catalog. Please ask staff before booking to play this game. This does not confirm that the studio cannot offer it.\nSource: {OUR_GAMES_URL}' if locale=='en' else
            f'ยังไม่พบ {title} ในรายการเกมของศูนย์ที่ยืนยันได้ครับ กรุณาสอบถามเจ้าหน้าที่ก่อนจองเพื่อเล่นเกมนี้ ข้อมูลนี้ยังไม่ใช่การยืนยันว่าศูนย์ไม่มีเกมดังกล่าว\nแหล่งข้อมูล: {OUR_GAMES_URL}')
    return StructuredToolResult(answer,HITS['our_games'],'recorded_game_catalog_no_answer',.97,{'game':title,'catalog_titles_checked':len(catalog),'absence_only':True,'not_live_occupancy':True})

def answer_closed_query_improvement(query,locale):
    for category,resolver in [('games',_recorded_catalog_gap),('contact',_contact_fields),('no_answer',_non_catalog_request),('service_fee',_fee_comparison),('service_fee',answer_fee_alternatives),('service_fee',_fee_catalog),('reservation',_booking_resource),('no_answer',_media_policy_gap)]:
        result=resolver(query,locale)
        if result is not None:return ('clarification' if 'clarification' in result.mode else category),result
    return None
