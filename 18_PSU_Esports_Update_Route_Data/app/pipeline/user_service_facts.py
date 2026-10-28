"""Scope-limited service facts supplied by the user on 2026-10-08."""
from __future__ import annotations
import json,re
from functools import lru_cache
from pathlib import Path
from app.core.normalization import normalize_text
from app.core.source_registry import make_source_hit
from app.pipeline.schemas import PipelineRoute,PipelineTrace,ValidationResult

PATH=Path(__file__).resolve().parents[2]/'data/curated/user_service_facts_20261008.json'
SOURCE_ID='user_service_answers_20261008'
@lru_cache(maxsize=1)
def load_facts():
    data=json.loads(PATH.read_text(encoding='utf-8'))
    if data.get('schema_version')!=1 or data.get('source_id')!=SOURCE_ID or data.get('basis')!='user_provided_in_this_chat':raise ValueError('invalid user service facts provenance')
    for claim in data['claims'].values():
        if claim.get('status')!='user_confirmed' or not claim.get('source_items') or not all(claim.get('answers',{}).get(k) for k in ('th','en')):raise ValueError('invalid confirmed service claim')
    return data

def _has(q,pattern):return bool(re.search(pattern,q,re.I))

def answer_user_service_facts(question,locale='th',recent_history=None):
    from app.pipeline.service_fact_query import recover_service_fact_query
    q,recoveries=recover_service_fact_query(question);en=locale=='en'
    if _has(q,r'สลิป|payment slip'):
        candidate=re.sub(r'ผืด','ผิด',q)
        if candidate!=q:recoveries.append(dict(observed='ผืด',intended='ผิด',method='payment_subject_anchored_diacritic_substitution'));q=candidate
    from app.session.service_fact_dialogue import ambiguous_fee_followup
    ambiguous=ambiguous_fee_followup(question,recent_history)
    if ambiguous:
        labels={'parking':('ที่จอดรถ','parking'),'spectators':('การนั่งดูเพื่อน','watching friends'),'membership':('สมาชิก','membership')}
        offered=[labels[k][en] for k in ambiguous['claim_ids'] if k in labels]
        subject=' / '.join(offered)
        answer=(f'Which item do you mean is free: {subject}?' if en else f'ต้องการถามว่าอะไรฟรีครับ: {subject}?') if len(offered)>1 else ('The previous answer covered more than one condition. Which item do you mean is free?' if en else 'คำตอบก่อนหน้ามีหลายเรื่องหรือเงื่อนไข ต้องการถามค่าใช้จ่ายเรื่องใดครับ?')
        return dict(answer=answer,hits=[],mode='pipeline:service_fact_scope_clarification',route=PipelineRoute('clarification','ambiguous_service_fee',.98,'clarification','low','multiple prior service subjects'),validation=ValidationResult(True,(),('ambiguous_service_fee',)),trace=[PipelineTrace('service_fact_scope_guard','clarification',.98,'do not choose the first prior subject',{'service_fact_state':ambiguous})])
    # Resolve competition semantics before homonyms such as maps/membership.
    from app.pipeline.competition_targets import looks_like_competition_rule_query
    if looks_like_competition_rule_query(q):return None
    # Tournament rules and zone-hire contracts are separate sources/scopes.
    if _has(q,r'แข่งขัน|ลงแข่ง|ตอนแข่ง|กฎแข่ง|กติกา|\b(?:competition|tournament|esports event|rental|hire)\b|เหมา'):return None
    if _has(q,r'สมาชิกทีม|\bmembers\b.*\bteam\b'):
        from app.pipeline.competition_targets import looks_like_competition_rule_query
        if looks_like_competition_rule_query(q):return None
    if _has(q,r'parking (?:area )?in bangkok|(?:ศูนย์|ที่จอดรถ).{0,20}(?:ที่|ใน)กรุงเทพ'):
        return dict(answer='The verified service facts cover PSU Esports Studio in Phuket. They do not confirm parking in Bangkok.' if en else 'ข้อมูลบริการที่ยืนยันเป็นของ PSU Esports Studio วิทยาเขตภูเก็ต ยังใช้ยืนยันที่จอดรถของศูนย์ในกรุงเทพไม่ได้ครับ',hits=[],mode='pipeline:service_fact_scope_clarification',route=PipelineRoute('clarification','external_location_scope',.98,'clarification','low','explicit outside-location request'),validation=ValidationResult(True,(),('external_location_scope',)),trace=[PipelineTrace('service_fact_scope_guard','clarification',.98,'do not apply Phuket facts to a different location',{})])
    if _has(q,r'แผนที่.*(?:เกม|valorant|cs2)|(?:เกม|valorant|cs2).*แผนที่|\b(?:game map|map in|maps?.*(?:valorant|cs2))\b'):return None
    if _has(q,r'(?:how many|number of).{0,25}(?:member groups|groups of members|members\b)|กลุ่มสมาชิก|รายชื่อสมาชิก|สมาชิก(?:ของศูนย์)?กี่(?:คน|กลุ่ม)') and not _has(q,r'steam|สมาชิกทีม|\bteam\b'):
        return None  # Directory quantities are distinct from access membership.
    if _has(q,r'สมาชิก|\b(?:membership|members?)\b') and _has(q,r'steam|สมาชิกทีม|\b(?:team|xbox live|nintendo online)\b'):
        answer=('Studio membership requirements do not establish game-account or team membership requirements. Please specify the account service or competition rule you want to check.' if en else 'เงื่อนไขสมาชิกของศูนย์ใช้แทนข้อกำหนดบัญชีเกมหรือสมาชิกทีมไม่ได้ครับ ต้องตรวจข้อกำหนดของบัญชีเกมหรือรายการแข่งขันนั้นแยกกัน')
        return dict(answer=answer,hits=[],mode='pipeline:service_fact_scope_clarification',route=PipelineRoute('clarification','external_membership_scope',.98,'clarification','low','studio access is not game account or team membership'),validation=ValidationResult(True,(),('external_membership_scope',)),trace=[PipelineTrace('service_fact_scope_guard','clarification',.98,'separate studio membership from account and team membership',{})])
    keys=[];missing=[]
    if _has(q,r'เป็นของ.{0,12}มหาวิทยาลัย|ร้านเกมทั่วไป|ศูนย์.*ของมหา(?:ลัย|วิทยาลัย)|\b(?:university[- ](?:facility|owned)|regular gaming (?:cafe|shop)|owned by.*university|who owns (?:the )?studio)\b'):keys.append('university')
    membership_query = re.sub(r'\bmembers?\s+of\s+(?:the\s+)?public\b','',q,flags=re.I)
    if _has(membership_query,r'สมาชิก|\b(?:membership|members?|nonmembers?)\b') and not _has(q,r'ทีมงาน|บุคลากร|\bstaff\b'):keys.append('membership')
    if _has(q,r'ดูเพื่อน|นั่งดู|\b(?:watch (?:my |our |your |a )?friends?|spectat\w*|just watch)\b'):keys.append('spectators')
    if _has(q,r'walk[ -]?in|เดินเข้า|เดินไปใช้|ไปหน้าร้าน|ไม่จอง.{0,10}(?:ไป|เข้า|เล่น)|\bturn up\b'):keys.append('walk_in')
    if _has(q,r'ที่จอด|จอดรถ|(?:รถ|มอไซค์|มอเตอร์ไซค์).*จอด|\b(?:parking|park.*(?:car|motorcycle))\b'):keys.append('parking')
    if _has(q,r'แผนที่|\b(?:map|maps)\b'):keys.append('map')
    if _has(q,r'ตึก|อาคาร|ชั้นไหน|อยู่ตรงไหน|ที่อยู่ศูนย์|ศูนย์อยู่ที่ไหน|ศูนย์อยู่ไหน|ศูนย์อยู่ที่ใด|ที่ตั้ง.*(?:ศูนย์|psu)|\b(?:building|floor|studio (?:address|location)|(?:venue|studio|centre|center) address|address of.*(?:studio|psu esports)|where (?:is|can i find) (?:the )?(?:venue|studio|centre|center|psu esports)|how do i get to the venue)\b'):
        if not _has(q,r'ทีวี|จอ(?!ด)|คีย์บอร์ด|เมาส์|\b(?:tv|monitor|screen|keyboard|mouse|xbox|bangkok|floor plan|game map|floor price)\b'):keys.append('location')
    if _has(q,r'หาศูนย์ไม่เจอ|ติดต่อ|แจ้งใคร|\b(?:contact|notify|cannot find the studio)\b'):
        if not _has(q,r'อีเมล|เบอร์|โทร|\b(?:email|phone|telephone)\b'):keys.append('contact')
    if _has(q,r'(?:มา|กัน|กลุ่ม|มี).{0,8}(?:4|สี่)\s*คน|\b(?:four|4) (?:of us|people|friends|ppl)|\bgroup of (?:four|4)\b') and _has(q,r'เลือก|เล่น(?:อะไร|อันไหน)|แนะนำ|\b(?:choose|recommend|which service|what.*play)\b') and not _has(q,r'สลับ|2คน|2 คน|\b(?:swap|take turns|two people)\b'):keys.append('four_people')
    if _has(q,r'คนจอง.*คนเล่น|คนเล่น.*(?:คนจอง|ไม่มีชื่อ)|จองชื่อ.*แต่.*คนเล่น|จองแทน|ใช้แทน|รายชื่อ.*จอง|ไม่มีชื่อ.*(?:จอง|เล่น)|จองชื่อ.*(?:เพื่อน|เล่นแทน)|\b(?:someone.*(?:booking|instead)|not listed|transfer.*booking|play instead|named in)\b'):keys.append('player_identity')
    if _has(q,r'หลักฐาน|แสดง.*บัตร|บัตร.*แสดง|(?:เอา|นำ|พก).*บัตร|บัตรอะไร.*(?:ไป|เช็คอิน|เช็กอิน)|ใช้.*(?:passport|พาสปอร์ต)|เอกสาร.*(?:มาถึง|เช็คอิน|เช็กอิน)|\b(?:identification|passport|id(?: card)?|student card|documents?.*(?:arrive|check.?in))\b') and not _has(q,r'สลิป|โอน|ชื่อจริง|ตรงกับบัตร|\b(?:slip|transfer|name.*match|real name)\b'):keys.append('checkin_documents')
    wrong_machine=_has(q,r'ผิดเครื่อง|เครื่องผิด|จองผิดอุปกรณ์|\b(?:wrong machine|wrong device|wrong equipment|wrong console)\b')
    active_session=_has(q,r'เล่นอยู่|ระหว่างเล่น|อัปเดต|อัพเดต|\b(?:while playing|during.*(?:play|update)|updat\w*)\b')
    if wrong_machine or (_has(q,r'เปลี่ยน.{0,8}(?:เครื่อง|อุปกรณ์)|\bchange.*machine\b') and not active_session):keys.append('change_machine')
    if _has(q,r'(?:เปลี่ยน|ย้าย).{0,8}เวลา|(?:เปลี่ยน|ย้าย).{0,8}รอบ.*จอง|เลื่อน.{0,8}(?:เวลา|รอบ)|\b(?:change.*booking time|change.*time|reschedul\w*.*time|move.*reservation.*time)\b'):keys.append('change_time')
    if _has(q,r'คีย์บอร์ด|เมาส์|เม้าส์|\b(?:keyboard|mouse)\b') and _has(q,r'ตัวเอง|ส่วนตัว|ของผม|เอา|นำ|\b(?:own|personal|bring)\b'):keys.append('personal_keyboard_mouse')
    payment_image=_has(q,r'หลักฐานโอน.*(?:ผิด|รูป)|\b(?:transfer|payment).*(?:receipt|proof).*(?:image|picture|photo)\b')
    if (_has(q,r'สลิป|\b(?:slip|payment image)\b') or payment_image) and _has(q,r'ผิด|เปลี่ยน|\b(?:wrong|incorrect|replace)\b'):keys.append('wrong_slip')
    if _has(q,r'โอน|จ่าย|\b(?:transfer|pay)\b') and _has(q,r'ครั้งเดียว|รวม|\b(?:one|single|combined)\b') and _has(q,r'หลายเครื่อง|หลายรายการ|\d+\s*เครื่อง|\b(?:multiple|several|machines|bookings)\b'):keys.append('combined_transfer')
    if _has(q,r'เช[็ค็กค]+อิน|check(?:[ -]?in| everyone in)') and _has(q,r'ทั้ง(?:กลุ่ม|แก๊ง|ทีม)|แทน|รายคน|\b(?:whole group|on behalf|individually|first person|everyone)\b'):keys.append('group_checkin')
    if _has(q,r'ที่นั่งพัก|นั่งพัก|นั่งรอพัก|(?:ที่|ตรง).{0,6}นั่งรอ|โซนกลาง|\b(?:sit and rest|seating.*rest|rest seating|rest area|re(?:st)? area|place to rest|waiting area.*rest)\b'):keys.append('rest_seating')
    if _has(q,r'ก่อนเวลาจอง.*รอ|รอ.*ก่อนเวลา|\bwhere.*wait.*(?:booking|booked|slot)\b'):
        keys.append('rest_seating');missing.append('designated_waiting_point')
    date_boundary=_has(q,r'ผิดวัน|เปลี่ยนวัน|เลื่อน.{0,10}(?:วัน|คืนเงิน)|\b(?:wrong date|change.*date|reschedul\w*.*(?:day|date)|another day.*refund)\b')
    if date_boundary:
        keys=[key for key in keys if key not in ('change_time','change_machine')]
        missing.append('date_change_exception_and_channel')
        # Preserve both supplied statements; do not choose their scope silently.
        explanation=('The supplied answers say a paid booking with the wrong date can change date, but also say rescheduling instead of a refund is not allowed. The exception and processing channel still need clarification.' if en else 'ข้อมูลที่ให้มาระบุว่าจองผิดวันและจ่ายแล้วเปลี่ยนวันได้ แต่ระบุอีกข้อว่าเลื่อนวันแทนคืนเงินไม่ได้ จึงยังต้องยืนยันขอบเขตข้อยกเว้นและช่องทางดำเนินการครับ')
    else:explanation=''
    # A similar word does not establish a policy for an unanswered condition.
    pending_conditions=[
        ('personal_controller_permission',r'จอย|\bcontroller\b',r'ตัวเอง|ส่วนตัว|เอา|\b(?:own|personal|bring)\b',
         'ข้อมูลที่ยืนยันห้ามเฉพาะคีย์บอร์ดและเมาส์ส่วนตัว ยังไม่ได้ยืนยันสิทธิ์นำจอยส่วนตัวมาใช้ครับ',
         'The confirmed restriction covers personal keyboards and mice. Permission to bring a personal controller has not been confirmed.'),
        ('combined_transfer_note_format',r'note|โน้ต',r'เขียนอะไร|ใส่อะไร|\bwhat.*(?:write|put)\b',
         'ยืนยันว่าต้องเขียน Note ตอนจองเพื่อให้ศูนย์ตรวจสอบ แต่ยังไม่ได้กำหนดข้อความหรือรูปแบบ Note ที่ต้องเขียนครับ',
         'A note is required at booking for studio verification, but the exact wording or note format has not been specified.'),
        ('multiplayer_game_modes',r'เกม|\bgames?\b',r'เล่นกับเพื่อน|เล่นด้วยกัน|\b(?:with friends|multiplayer|play together)\b',
         'มีรายการเกมของศูนย์ แต่ยังไม่ได้ยืนยันโหมดเล่นร่วมกันและจำนวนผู้เล่นของแต่ละเกมครับ ต้องการเล่นเกมหรือโซนไหน?',
         'The studio has a game catalog, but multiplayer modes and supported player counts have not been verified for each game. Which game or zone would you like?'),
        ('two_person_recommendation',r'สองคน|2\s*คน|\b(?:two|2) (?:of us|people)\b',r'เล่นด้วยกัน|เล่นอะไร|\b(?:play together|what.*play|choose)\b',
         'ยังไม่ได้ยืนยันคำแนะนำเกมสำหรับเล่นพร้อมกันสองคนครับ ต้องการเล่นเกมหรือโซนไหน?',
         'A recommendation for two people playing together has not been confirmed. Which game or zone would you like?'),
        ('game_installation_permission',r'ลงเพิ่ม|(?:ขอ|ได้ไหม|ได้มั้ย).*ลง.{0,15}เกม|ลง.{0,15}เกม.*(?:ได้ไหม|ได้มั้ย|เพิ่ม)|โหลดเกม.*เอง|ติดตั้ง.{0,40}(?:เอง|ได้ไหม)|\b(?:can|may).*(?:install|add)\b|\b(?:install|add).*(?:myself|allowed)\b',r'เกม|โปรแกรม|mod|\b(?:game|program|mod)\b',
         'ยังไม่ได้ยืนยันว่าให้ขอลงเกมเพิ่มหรือติดตั้งเกม โปรแกรม หรือ mod เองได้หรือไม่ครับ',
         'Permission to request additional games or install games, programs, or mods yourself has not been confirmed.'),
        ('session_extension',r'ต่อเวลา|\b(?:extend|extension)\b',r'เล่น|เวลา|\b(?:play|time|session)\b',
         'ยังไม่ได้ยืนยันขั้นตอนต่อเวลาระหว่างเล่น ต้องจองเพิ่มหรือติดต่อเจ้าหน้าที่อย่างไรครับ',
         'The procedure for extending play time, including whether to book again or ask staff, has not been confirmed.'),
        ('cross_zone_change',r'(?:pc|ps5|playstation).*(?:ไป|to|switch).*(?:pc|ps5|playstation)',r'เปลี่ยน|\b(?:change|switch)\b',
         'ยังไม่ได้ยืนยันขั้นตอนย้ายจาก PC ไป PS5 ระหว่างใช้บริการครับ ถ้าเป็นการจองผิดเครื่อง ข้อมูลข้อ 18 ระบุให้ยกเลิกผ่านอีเมลแล้วจองใหม่ แต่ยังสรุปไม่ได้ว่าใช้ขั้นตอนเดียวกันระหว่างเล่น',
         'Changing from PC to PS5 during a visit has not been confirmed. Item 18 covers a wrong-machine booking: cancel through email and book again. It does not establish the procedure during play.'),
        ('game_account_policy',r'บัญชี|account|steam.*(?:ตัวเอง|ล็อกอิน|log.?in|own)',r'steam|บัญชีเกม|game account|(?:own|borrow|loan).*(?:account)',
         'ยังไม่ได้ยืนยันว่าศูนย์มีบัญชีเกมให้ใช้หรือต้องใช้บัญชี Steam ของตนเองครับ',
         'Whether the studio provides game accounts or requires your own Steam account has not been confirmed.'),
        ('technical_fault_compensation',r'ค้าง|ดับ|\b(?:crash\w*|shut down|power failure)\b',r'เวลา|ชดเชย|\b(?:time|compensat)\w*',
         'ยังไม่ได้ยืนยันวิธีคิดหรือชดเชยเวลาที่เสียไปเมื่อเครื่องค้างหรือดับครับ',
         'How lost time is charged or compensated after a crash or shutdown has not been confirmed.'),
        ('forgotten_logout_procedure',r'ลืม.*(?:ออกจากบัญชี|log.?out|sign.?out)|\bforgot.*(?:log.?out|sign.?out)\b',r'บัญชี|\b(?:account|log.?out|sign.?out)\b',
         'ติดต่อเพจศูนย์เพื่อแจ้งปัญหาได้ แต่ยังไม่ได้ยืนยันขั้นตอนออกจากบัญชีแทนผู้ใช้ครับ',
         'You can report the problem to the studio page, but logging out on a user\'s behalf has not been confirmed.'),
        ('photo_video_permission',r'ถ่ายรูป|อัดวิดีโอ|\b(?:photos?|record.*video|film)\b',r'ได้ไหม|ไหม|อนุญาต|\b(?:can|allowed|may|permission)\b',
         'ยังไม่ได้ยืนยันเงื่อนไขถ่ายรูปหรืออัดวิดีโอภายในศูนย์ครับ',
         'Permission and conditions for photography or video recording in the studio have not been confirmed.'),
        ('streaming_permission',r'สตรีม|\bstream\w*\b',r'ศูนย์|เครื่อง|เกม|\b(?:studio|machine|game|pc)\b',
         'ยังไม่ได้ยืนยันว่าอนุญาตให้สตรีมจากเครื่องของศูนย์ได้หรือไม่ครับ',
         'Permission to stream from the studio machines has not been confirmed.'),
        ('minor_guardian_policy',r'เด็ก|ผู้ปกครอง|\b(?:child|children|minor|guardian)\b',r'ใช้บริการ|เข้า|ผู้ปกครอง|\b(?:access|use|play|guardian)\b',
         'ยังไม่ได้ยืนยันข้อกำหนดอายุและการมีผู้ปกครองสำหรับเด็กครับ การเปิดให้บุคคลทั่วไปใช้บริการยังใช้ยืนยันข้อนี้ไม่ได้',
         'Age and guardian requirements for children have not been confirmed. General public access does not establish this policy.'),
        ('seat_capacity_definition',r'ที่นั่ง|\bseats?|seating\b',r'จำนวนคนเล่น|พร้อมกัน|ในห้อง|\b(?:players|simultaneous|room)\b',
         'ข้อมูลจำนวนที่นั่งกับจำนวนเครื่องเป็นคนละช่องข้อมูล ยังไม่ได้ยืนยันว่าจำนวนที่นั่งหมายถึงผู้เล่นพร้อมกันครับ',
         'Seat counts and equipment counts are separate fields; seats have not been confirmed as simultaneous player capacity.'),
        ('quotation_receipt_procedure',r'ใบเสนอราคา|ใบเสร็จ|\bquotation\b|^(?!.*(?:payment|transfer).*image).*\breceipt\b',r'ขอ|ได้ไหม|\b(?:can|request|get|issue)\b',
         'ยังไม่ได้ยืนยันขั้นตอนขอใบเสนอราคาหรือใบเสร็จครับ',
         'The procedure for obtaining a quotation or receipt has not been confirmed.'),
        ('game_version_status',r'อัปเดต|อัพเดต|\b(?:updat\w*|version)\b',r'ล่าสุด|เวอร์ชัน|\b(?:latest|version|up.to.date)\b',
         'ยังไม่มีข้อมูลสดที่ยืนยันเวอร์ชันเกมบนเครื่องจริง จึงยืนยันว่าอัปเดตล่าสุดแล้วไม่ได้ครับ',
         'There is no live verification of the game versions on the machines, so the latest update cannot be confirmed.'),
        ('update_time_charging',r'อัปเดต|อัพเดต|\bupdat\w*\b',r'นับ|คิดเวลา|\b(?:count\w*|charg\w*|start.*time)\b',
         'ยังไม่ได้ยืนยันว่าช่วงอัปเดตเกมคิดเวลาใช้บริการอย่างไรครับ',
         'How service time is charged while a game updates has not been confirmed.'),
        ('booking_phone_correction',r'เบอร์โทร|\b(?:phone|telephone)\b',r'ผิด|แก้|\b(?:wrong|incorrect|correct)\b',
         'ยังไม่ได้ยืนยันขั้นตอนแก้เบอร์โทรในรายการจองหรือว่าต้องจองใหม่ครับ',
         'Correcting a booking phone number, and whether a new booking is needed, have not been confirmed.'),
        ('overpayment_resolution',r'โอนเกิน|\boverpa(?:id|y\w*)\b|transferred too much',r'โอน|\b(?:overpa\w*|transfer\w*)\b',
         'ยังไม่ได้ยืนยันขั้นตอนจัดการเงินที่โอนเกินครับ ข้อมูลแก้สลิปไม่ได้ระบุเงื่อนไขคืนเงินส่วนเกิน',
         'The procedure for overpayments has not been confirmed. Correcting a slip does not establish an excess-payment refund.'),
        ('underpayment_resolution',r'โอนขาด|\bunderpa(?:id|y\w*)\b|transferred too little',r'โอน|\b(?:underpa\w*|transfer\w*)\b',
         'ยังไม่ได้ยืนยันว่าโอนขาดต้องโอนเพิ่มหรือจองใหม่ครับ',
         'Whether an underpayment requires another transfer or a new booking has not been confirmed.'),
        ('special_closure_booking_resolution',r'ปิดพิเศษ|\b(?:special closure|unexpected.*clos\w*|studio closes)\b',r'จอง|\b(?:book\w*|reservation)\b',
         'ยังไม่ได้ยืนยันว่าถ้าศูนย์ปิดพิเศษหลังจองแล้ว จะคืนเงินหรือเลื่อนรายการอย่างไรครับ',
         'Refunding or moving a booking after a special closure has not been confirmed.'),
        ('capacity_rotation',r'สลับ|\b(?:take turns|swap)\b',r'4|สี่|\bfour\b',
         'ยังไม่ได้ยืนยันว่า 4 คนสลับเล่นเครื่องที่รองรับ 2 คนได้หรือไม่ครับ',
         'It has not been confirmed whether four people may take turns on a two-person service.'),
        ('weather_reschedule',r'ฝน|\b(?:rain|storm|weather)\b',r'เปลี่ยน|เลื่อน|\b(?:change|reschedul|move)\w*',
         'ยังไม่ได้ยืนยันเงื่อนไขเปลี่ยนรอบเมื่อเดินทางไม่ได้เพราะสภาพอากาศครับ',
         'Rescheduling when weather prevents travel has not been confirmed.'),
        ('active_session_machine_change',r'เปลี่ยน.{0,10}(?:เครื่อง|อุปกรณ์)|\bchange.*machines?\b',r'เล่นอยู่|ระหว่างเล่น|อัปเดต|อัพเดต|\b(?:while playing|during.*play|updat\w*)\b',
         'ยังไม่ได้ยืนยันขั้นตอนเปลี่ยนเครื่องระหว่างเล่นหรือระหว่างเกมอัปเดตครับ',
         'The procedure for changing machines during play or a game update has not been confirmed.'),
        ('payer_identity',r'บัญชี.*เพื่อน|\b(?:friend\W*s (?:bank )?account|someone else\W*s (?:bank )?account|friend.*their account)\b',r'จ่าย|โอน|\b(?:pay|transfer)\b',
         'ยังไม่ได้ยืนยันว่าใช้บัญชีธนาคารของเพื่อนชำระเงินได้หรือไม่ครับ ข้อมูลการโอนรวมหลายเครื่องไม่ครอบคลุมเรื่องเจ้าของบัญชี',
         'Payment from a friend\'s bank account has not been confirmed. Permission for one transfer covering multiple machines does not establish who may pay.'),
        ('name_matches_id',r'ชื่อจริง|ตรงกับบัตร|\b(?:real name|name.*match.*(?:id|card))\b',r'ชื่อ|\bname\b',
         'ยังไม่ได้ยืนยันว่าชื่อในรายการจองต้องตรงกับบัตรหรือแก้ไขอย่างไรครับ',
         'Whether the booking name must match the ID, and how to correct it, have not been confirmed.'),
    ]
    for field,subject,condition,th_message,en_message in pending_conditions:
        subject_present=_has(q,subject)
        condition_present=_has(q,condition)
        if field=='game_installation_permission' and _has(q,r'\b(?:install|add)\b'):
            from app.runtime.fast_answer import is_known_unsupported_game_query
            from app.session.context_resolver import detect_game
            condition_present=condition_present or bool(detect_game(q) or is_known_unsupported_game_query(q))
        if subject_present and condition_present:
            if field in ('weather_reschedule','active_session_machine_change'):
                keys=[key for key in keys if key not in ('change_time','change_machine')]
            missing.append(field)
            explanation+='\n\n'+(en_message if en else th_message)
    supplemental=[]
    recorded_rule_ids=[]
    if any(field in missing for field in ('technical_fault_compensation','special_closure_booking_resolution')) or (keys and _has(q,r'คืนเงิน|เงินคืน|refund') and not date_boundary):
        recorded_rule_ids.append('rule_refund_policy')
    if _has(q,r'ไปสาย|มาสาย|ถึงช้า|\b(?:arrive|arrival|show up).*late\b'):
        recorded_rule_ids.append('rule_checkin_late')
        missing.append('late_grace_exception')
        explanation+='\n\n'+('No separate grace period or exception for arriving 15 minutes late has been confirmed.' if en else 'ยังไม่ได้ยืนยันเวลาผ่อนผันหรือข้อยกเว้นสำหรับการมาสาย 15 นาทีครับ')
    if recorded_rule_ids:
        rule_path=PATH.parents[1]/'rules/reservation_rules.jsonl'
        recorded_rules={row['id']:row for row in (json.loads(line) for line in rule_path.read_text(encoding='utf-8').splitlines())}
        supplemental=[recorded_rules[rule_id] for rule_id in dict.fromkeys(recorded_rule_ids)]
    if not keys and not missing:return None
    data=load_facts();keys=list(dict.fromkeys(keys))
    lines=[data['claims'][key]['answers']['en' if en else 'th'] for key in keys]
    for rule in supplemental:
        lines.append(('Recorded booking rule: ' if en else 'กฎการจองที่บันทึกไว้เดิม: ')+rule['answer_en' if en else 'answer_th']+'\n'+rule['source_url'])
    if explanation:lines.append(explanation)
    if 'designated_waiting_point' in missing:lines.append('The central rest seating has not been confirmed as the designated waiting point for an upcoming booking.' if en else 'ยังไม่ได้ยืนยันว่าโซนกลางห้องเป็นจุดรอรอบจองโดยเฉพาะครับ')
    if keys and _has(q,r'คืนเงิน|เงินคืน|refund') and not date_boundary:
        missing.append('refund_conditions');lines.append('The recorded general refund rule does not confirm eligibility or processing for this particular booking.' if en else 'กฎคืนเงินทั่วไปที่บันทึกไว้ยังใช้รับรองว่ารายการจองนี้จะได้รับเงินคืนหรือดำเนินการอย่างไรไม่ได้ครับ')
    if 'parking' in keys and _has(q,r'ฟรี|ราคา|ค่าจอด|\b(?:free|fee|cost|charge)\b'):
        missing.append('parking_fee');lines.append('Parking fees have not been specified.' if en else 'ยังไม่ได้ระบุค่าจอดรถ จึงยืนยันว่าจอดฟรีไม่ได้ครับ')
    if 'membership' in keys and _has(q,r'ค่าสมาชิก|ราคา|ฟรี|\b(?:fee|cost|paid|price|free)\b'):
        missing.append('membership_fee');lines.append('A membership fee has not been specified; membership is not required for access.' if en else 'ยังไม่ได้ระบุเรื่องค่าสมาชิก แต่การเข้าใช้บริการไม่จำเป็นต้องเป็นสมาชิกครับ')
    if 'spectators' in keys and _has(q,r'ฟรี|ราคา|ค่าเข้า|เสียเงิน|จ่ายเงิน|\b(?:free|fee|cost|charge|price)\b'):
        missing.append('spectator_fee');lines.append('A spectator fee or free admission has not been confirmed.' if en else 'ยังไม่ได้ระบุค่าเข้าชมหรือยืนยันว่าเข้าดูเพื่อนฟรีครับ')
    if 'walk_in' in keys and _has(q,r'ทันที|ตอนนี้|\b(?:immediately|right now)\b'):
        missing.append('immediate_walk_in_slot');lines.append('This does not confirm an immediately available slot or waive the booking lead time.' if en else 'ข้อมูลนี้ยังไม่ยืนยันว่ามีรอบว่างให้เล่นทันทีหรือยกเว้นเวลาจองล่วงหน้าครับ')
    lines+=['Source: user-provided service answers (2026-10-08)' if en else 'แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)',data['source_url']]
    status='partial' if (keys or supplemental) and missing else 'missing' if missing else 'answered'
    category=data['claims'][keys[0]]['category'] if keys else 'reservation' if supplemental else 'clarification'
    meta=dict(claim_ids=keys,source_items=sorted({n for key in keys for n in data['claims'][key]['source_items']}),missing_fields=missing,basis=data['basis'],english_status=data['english_status'],outcome='answered_partial' if status=='partial' else 'no_answer' if status=='missing' else 'answered_complete')
    route=PipelineRoute(category,'user_service_facts',.98,'clarification' if not keys else 'fact','low','explicit user-supplied facts with bounded policy scope')
    hits=[make_source_hit(SOURCE_ID)]+[dict(id=rule['id'],metadata=dict(
        source_url=rule['source_url'],source_ids=rule['source_ids'],category=rule['category'],
        source_type='recorded_booking_rule',title=rule['id'],origin='data/rules/reservation_rules.jsonl',
        trust_level='curated',description='Previously recorded booking rule; grace exceptions are unconfirmed'))
        for rule in supplemental]
    meta['recorded_rule_ids']=[rule['id'] for rule in supplemental]
    meta['lexical_recoveries']=recoveries
    meta['normalized_service_question']=q
    return dict(answer='\n\n'.join(lines).strip(),hits=hits,route=route,validation=ValidationResult(True,(),tuple(missing)),mode='pipeline:user_service_facts',trace=[PipelineTrace('user_service_facts',status,.98,'do not infer unanswered policies',meta),PipelineTrace('task_answer_contract',meta['outcome'],1.0,'known versus missing user-confirmed fields',dict(schema_version=1,kind='single',status=status,outcome=meta['outcome'],category=category,intent='user_service_facts',source_count=len(hits),coverage_meaning='user_confirmed_fields_not_live_status'))])
