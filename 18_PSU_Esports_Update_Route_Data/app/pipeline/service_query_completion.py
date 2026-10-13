"""Explicit shop operations before broad semantic retrieval.

Quantities and subjects belong to each clause. These adapters use the
existing fee, calendar, catalog and booking sources, with their limitations.
"""
from __future__ import annotations
import math,re
from app.core.normalization import normalize_text
from app.pipeline.schemas import EntityBundle,PipelineRoute,PipelineTrace,ValidationResult
from app.session.conversation_plan import service_mentions,customer_filter,SERVICE_LABELS,is_fee_request

def _op(q):
    if re.search(r'เงินสด|\bcash\b',q,re.I):return 'cash'
    if is_fee_request(q) or (re.search(r'กี่บาท|เท่าไหร่|เท่าไร|\b(?:cost|how much)\b',q,re.I) and re.search(r'เล่น|ชั่วโมง|นาที|\b(?:play|hours?|minutes?)\b',q,re.I)):return 'fee'
    if re.search(r'ว่าง|ถูกจอง|\b(?:available|free|booked)\b',q,re.I) and service_mentions(q):return 'live'
    if service_mentions(q) and re.search(r'\d{1,2}\s*(?:โมง|:)',q):return 'live'
    if re.search(r'เปิด|ปิด|maintenance|opening hours|\b(?:open|close|opens|closes)\b',q,re.I):return 'schedule'
    if re.search(r'เกม(?:อะไร|ไร|ไหน|กี่)|มีเกม|\b(?:what|which|how many) games\b',q,re.I):return 'games'
    if re.search(r'ชำระ|โอน|\b(?:pay|payment|transfer)\b',q,re.I):return 'payment'
    if re.search(r'สมาชิก|จอดรถ|บัตร|ตึก|ที่อยู่|where.*studio|membership|parking|\bid\b|\bbuilding\b',q,re.I):return 'fact'
    return ''

def split_service_operations(question):
    q=normalize_text(question)
    parts=[p.strip(' ,?？') for p in re.split(r'\s*(?:และ|แล้ว|\band\b|[;?？])\s*',question,flags=re.I) if p.strip(' ,?？')]
    if len(parts)==1 and re.search(r'ชำระเงิน(?:ยังไง|อย่างไร).*จ่ายเงินสด',question):
        parts=[p.strip() for p in re.split(r'(?=จ่ายเงินสด)',question,maxsplit=1)]
    if not 2<=len(parts)<=6:return [question]
    operations=[_op(p) for p in parts]
    if not all(operations):return [question]
    if len(set(operations))==1 and operations[0]!='live':return [question]
    # Shared service may qualify games + price, but never carry the first
    # clause's clock to an explicitly timed second station.
    services=service_mentions(parts[0]);shared=SERVICE_LABELS[services[0]] if len(services)==1 else ''
    for i,p in enumerate(parts):
        if operations[i] in ('games','fee') and shared and not service_mentions(p):parts[i]=shared+' '+p
        if operations[i]=='live' and not re.search(r'ว่าง|ถูกจอง|\b(?:available|free|booked)\b',p,re.I):parts[i]+=' available?' if question.isascii() else ' ว่างไหม'
    if operations.count('live')>1:
        from app.booking.live_status import resolve_live_target_date
        if re.search(r'วันนี้|พรุ่งนี้|\d{4}-\d{2}-\d{2}|\b(?:today|tomorrow)\b',parts[0],re.I):
            date=resolve_live_target_date(parts[0])
            for i in range(1,len(parts)):
                if not re.search(r'วันนี้|พรุ่งนี้|\d{4}-\d{2}-\d{2}|\b(?:today|tomorrow)\b',parts[i],re.I):parts[i]=date+' '+parts[i]
    return parts

def _result(answer,hits,domain,operation,metadata,warnings=()):
    return dict(answer=answer,hits=hits,mode='pipeline:source_operation_'+operation,
        route=PipelineRoute(domain,operation,.98,'fact','low','explicit operation bound to recorded source'),
        validation=ValidationResult(True,(),tuple(warnings)),
        trace=[PipelineTrace('source_operation',operation,.98,'preserve requested subjects, units and source limits',metadata)])

def answer_budget(question,locale):
    q=normalize_text(question);en=locale=='en'
    money=re.search(r'(?<![\d.,])((?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?)\s*(?:บาท|thb\b|baht\b)',q,re.I)
    # Keep costs, transfers, discounts and refunds outside affordability.
    if not money or not re.search(r'งบ|มี\s*\d|เล่น.*(?:ได้|กี่)|\b(?:budget|afford|have|can.*play)\b',q,re.I) or re.search(r'คืนเงิน|โอน|จ่ายแล้ว|refund|transfer|discount|paid',q,re.I):return None
    from app.calculator.service_fee import SERVICE_FEES,_detect_people
    from app.pipeline.conversation_fee import expected_packages,recorded_expiry,GROUP_EN
    from app.core.source_registry import make_source_hits,SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID
    amount=float(money.group(1).replace(',',''));scope,groups=customer_filter(q)
    targets=service_mentions(q) or list(SERVICE_LABELS)
    if len(groups)!=1:
        return _result('Which customer group should I use for this budget: PSU students/staff, students from other institutions, or general adults?' if en else 'ต้องการคิดงบสำหรับกลุ่มใดครับ: นักศึกษา/บุคลากร PSU นักศึกษาต่างสถาบัน หรือบุคคลทั่วไป?',[], 'clarification','budget_group',dict(missing_fields=['customer_group'],budget=amount),('missing_customer_group',))
    group=groups[0];packages=expected_packages(dict(targets=targets,filters={'people_count':_detect_people(q)},per_target_filters={}))
    rows=[];lines=[f'Budget: {amount:g} THB — {GROUP_EN[group]} (recorded package rates).' if en else f'งบ {amount:g} บาท — '+{'general_adult':'บุคคลทั่วไป','general_student':'นักศึกษาต่างสถาบัน/ศิษย์เก่า PSU','psu_student_staff':'นักศึกษา/บุคลากร PSU'}[group]+' (คำนวณจากอัตราที่บันทึกไว้)']
    for key in packages:
        fee=SERVICE_FEES[key];unit=fee['prices'][group]
        if unit==0:
            lines.append(f"• {fee['label']} ({fee['minutes_per_session']} minutes/package): the recorded fee is 0 THB; money does not establish unlimited booking or availability." if en else f"• {fee['label']} ({fee['minutes_per_session']} นาที/แพ็กเกจ): ราคาที่บันทึก 0 บาท ไม่ได้หมายถึงจองได้ไม่จำกัดหรือมีเครื่องว่าง")
            rows.append(dict(package=key,unit_price=unit,sessions=None));continue
        count=math.floor(amount/unit)
        if count==0 and len(targets)>1:continue
        remainder=round(amount-count*unit,2)
        capacity=fee['capacity'].replace('คน','people') if en else fee['capacity']
        lines.append(f"• {fee['label']} ({capacity}), {fee['minutes_per_session']} minutes/package: {count} whole package(s), {unit:g} THB each, {count*fee['minutes_per_session']} minutes total; {remainder:g} THB left." if en else f"• {fee['label']} ({capacity}), {fee['minutes_per_session']} นาที/แพ็กเกจ: ได้ {count} แพ็กเกจเต็ม แพ็กเกจละ {unit:g} บาท รวม {count*fee['minutes_per_session']} นาที เหลือ {remainder:g} บาท")
        rows.append(dict(package=key,unit_price=unit,sessions=count,remainder=remainder))
    if not rows:lines.append('No paid recorded package fits this budget.' if en else 'ไม่มีแพ็กเกจที่มีค่าบริการตามอัตราบันทึกอยู่ในงบนี้ครับ')
    sources=[PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID] if targets==['pc'] else [SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID]
    if targets!=['pc']:
        expiry=recorded_expiry()
        if expiry:lines.append(f'Original non-PC fee table validity: {expiry.isoformat()}; current renewal is not confirmed.' if en else f'ตารางเดิมของบริการอื่นมีผลถึง {expiry.isoformat()} ยังไม่ยืนยันการต่ออายุราคา')
    lines.append('This is an affordability calculation, not a reservation. Booking limits, eligibility and live slots still apply.' if en else 'นี่เป็นการคำนวณงบ ไม่ใช่การจอง ยังต้องตรวจสิทธิ์ จำนวนรอบที่จองได้และสถานะรอบว่างจริงครับ')
    hits=make_source_hits(sources)
    for hit in hits:lines.append(('Source: ' if en else 'แหล่งข้อมูล: ')+hit.get('metadata',{}).get('source_url',''))
    return _result('\n'.join(lines),hits,'service_fee','affordability',dict(budget=amount,group=group,packages=rows,not_live=True))

def answer_explicit_source_operation(question,locale,matcher):
    q=normalize_text(question);en=locale=='en'
    budget=answer_budget(q,locale)
    if budget:return budget
    if re.search(r'เงินสด|\bcash\b',q,re.I) and re.search(r'จ่าย|ชำระ|\bpay\b',q,re.I):
        return _result('Acceptance of cash has not been confirmed. Please check with the studio before choosing this payment method.' if en else 'ยังไม่มีข้อมูลยืนยันว่าชำระเงินสดได้หรือไม่ครับ กรุณาตรวจสอบกับศูนย์ก่อนเลือกวิธีชำระนี้',[],'reservation','cash_policy_unconfirmed',dict(missing_fields=['cash_payment']),('cash_payment_unconfirmed',))
    from app.runtime.fast_answer import HITS
    services=service_mentions(q)
    game_list=bool(re.search(r'เกม.{0,18}กี่เกม|(?:มี)?เกม(?:อะไร|ไร|ไหน|กี่)|เกมทั้งหมดกี่|(?:เล่นเกมอะไร)|\b(?:what|which|how many) games\b',q,re.I))
    if game_list and not re.search(r'ติดตั้ง|โหลด|ลง.{0,15}เกม|เกม.{0,15}เพิ่ม|ลงเพิ่ม|ห้าม|ไม่เอา|ปุ่ม|กฎ|กติกา|แข่ง|ราคา|จ่าย|บัญชี|\b(?:controls?|rules?|competition|price|cost|pay|account)\b',q,re.I):
        from app.pipeline.entity_resolver import resolve_game_entity
        from app.runtime.fast_answer import is_known_unsupported_game_query
        if is_known_unsupported_game_query(q):return None
        from app.runtime.fast_answer import _format_game_zone_sections,_catalog_summary,_game_catalog_by_zone
        if not resolve_game_entity(q,operation='games').is_exact:
            keys=[('nintendo' if s=='nintendo_switch' else s) for s in services]
            by_zone=_game_catalog_by_zone()
            zones={'pc':'PC Zone','ps5':'PlayStation 5 Zone','nintendo':'Nintendo Switch Zone','cockpit':'Cockpit Zone','vr':'VR Zone'}
            chosen={name:games for name,games in by_zone.items() if not keys or name in [zones[k] for k in keys]}
            if en:
                from app.pipeline.bilingual_english import _format_game_catalog
                answer=_format_game_catalog([dict(zone=z,games=g) for z,g in chosen.items()],zones[keys[0]] if len(keys)==1 else None)
            else:answer=(_format_game_zone_sections(keys=keys,intro='เกมที่มีข้อมูลยืนยันในโซนที่ถาม') if keys else _catalog_summary())+'\nแหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games'
            return _result(answer,HITS['our_games'],'games','game_list',dict(targets=services,game_count=len({g.casefold() for games in chosen.values() for g in games}),not_live=True))
    if en and services==['pc'] and re.search(r'\b(?:specifications?|specs?|cpu|gpu|ram)\b',q) and not re.search(r'\b(?:what is|compare|difference|my pc)\b',q):
        from app.runtime.fast_answer import answer_equipment
        import time
        source=answer_equipment('PC สเปค',time.perf_counter())
        if source:
            # Translate only the existing local hardware specification line.
            text=source.answer.split('\n',1)[0]
            replacements={'สเปก PC ที่บันทึกไว้ตอนนี้:':'Recorded PC specifications:', 'รุ่น':'model','และใน PC Zone มี Gaming PC ทั้งหมด 10 เครื่อง':'PC Zone has 10 Gaming PCs'}
            for a,b in replacements.items():text=text.replace(a,b)
            text+='\nSource: local hardware/CPU-Z specifications recorded in the project; the website Home inventory does not independently confirm these internal components.'
            return _result(text,source.hits,'equipment','equipment_spec_lookup',dict(basis='existing_local_hardware_specifications',not_live=True))
    if (re.search(r'maintenance',q,re.I) or re.fullmatch(r'(?:what (?:are|is) (?:your|the) (?:opening|service|business) hours|opening hours|เปิดกี่โมง ปิดกี่โมง|วันอาทิตย์เปิดไหม)[ ?!.]*',q,re.I)) and not re.search(r'วันนี้|พรุ่งนี้|\d{4}-\d{2}-\d{2}|\b(?:today|tomorrow)\b',q,re.I):
        from app.pipeline.protected_intents import _weekly_schedule,RESERVATION_URL
        return _result(_weekly_schedule(locale)+'\n'+('Source: ' if en else 'แหล่งข้อมูล: ')+RESERVATION_URL,HITS['reservation'],'schedule','schedule_query',dict(basis='regular_service_calendar',not_live=True))
    if en and re.search(r'\b(?:when|what|which|opening|business|service)\b.*\b(?:open|opens|hours|schedule)\b',q) and not re.search(r'\b(?:today|tomorrow|now|available|free|price|cost)\b|\d{4}-\d{2}-\d{2}',q):
        from app.pipeline.bilingual_english import _answer_schedule
        value=_answer_schedule(q,EntityBundle())
        if value:return _result(value.answer,value.hits,'schedule','schedule_query',dict(basis='regular_service_calendar',not_live=True))
    if not en and re.search(r'ปุ่ม|ควบคุม',q) and not re.search(r'กฎ|กฏ|กติกา|แข่ง|ราคา|จอง|เสีย|พัง',q):
        from app.pipeline.structured_tools import _control_answer,_detect_game
        from app.pipeline.competition_targets import resolve_competition_targets
        # The control handler's catalog already recognizes CS2 and merges
        # the Tekken title variants. Reuse it rather than a session alias list.
        named=_detect_game(q,allow_fuzzy=False)
        multiple=resolve_competition_targets(q).status=='multiple'
        if named and not multiple and not re.search(r'และ|หรือ|เทียบ|\b(?:and|or|versus|compare)\b',q):
            from app.pipeline.schemas import UniversalIntent
            value=_control_answer(q,UniversalIntent('game_controls','control_lookup',target=named['game']))
            if value:return _result(value.answer,value.hits,'game_controls','control_lookup',{'basis':'existing_structured_control_handler',**value.evidence})
    if en and re.search(r'\b(?:shoot|reload)\b',q):
        from app.pipeline.bilingual_english import _answer_game_controls,_known_game
        game=_known_game(q)
        if game:
            control=_answer_game_controls(q,game)
            if control:return _result(control.answer,control.hits,'game_controls','control_lookup',dict(game=game,basis='recorded_control_mapping'),control.validation.warnings)
    if re.search(r'maintenance',q,re.I) and not re.search(r'วันนี้|พรุ่งนี้|\d{4}-\d{2}-\d{2}|\b(?:today|tomorrow|available|free)\b',q,re.I):
        from app.pipeline.protected_intents import _weekly_schedule,RESERVATION_URL
        return _result(_weekly_schedule(locale)+'\n'+('Source: ' if en else 'แหล่งข้อมูล: ')+RESERVATION_URL,HITS['reservation'],'schedule','schedule_query',dict(basis='regular_service_calendar',not_live=True))
    if re.search(r'จอง(?:เครื่อง|อุปกรณ์)?(?:ยังไง|อย่างไร)|วิธีจอง|ขั้นตอนจอง',q) and not re.search(r'ผิด|เปลี่ยน|ยกเลิก|สลิป|เหมา|คืนเงิน',q):
        from app.runtime.fast_answer import _booking_howto_answer
        import time
        value=_booking_howto_answer(q,time.perf_counter())
        if value:return _result(value.answer,value.hits,'reservation','booking_how_to',dict(basis='recorded_booking_procedure'))
    # Fee children of compound requests do not pass through the entry plan.
    if is_fee_request(q):
        from app.session.conversation_plan import resolve_request_plan
        from app.pipeline.conversation_fee import build_price_plan_answer
        plan=resolve_request_plan(question,[],locale=locale)
        result=build_price_plan_answer(plan,locale) if plan else None
        if result:return result
    return None
