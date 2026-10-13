"""Resolve short service follow-ups from the last acknowledged server answer."""
from __future__ import annotations
import re
from dataclasses import asdict,is_dataclass
from app.core.normalization import normalize_text

def service_fact_state(response):
    if response.get('mode') not in {'pipeline:user_service_facts','pipeline:service_fact_scope_clarification'}:return None
    trace=[asdict(t) if is_dataclass(t) else t for t in response.get('trace',[])]
    if response.get('mode')=='pipeline:service_fact_scope_clarification':
        return next((t.get('metadata',{}).get('service_fact_state') for t in trace if isinstance(t,dict) and t.get('stage')=='service_fact_scope_guard'),None)
    meta=next((t.get('metadata',{}) for t in trace if isinstance(t,dict)
               if t.get('stage')=='user_service_facts'),{})
    return dict(claim_ids=list(meta.get('claim_ids',[])),missing_fields=list(meta.get('missing_fields',[]))) if meta else None

def ambiguous_fee_followup(question,history):
    if not isinstance(history,list):return None
    previous=next((h for h in reversed(history) if isinstance(h,dict) and h.get('role')=='assistant'),{})
    if previous.get('delivery_status')!='client_acknowledged':return None
    state=previous.get('service_fact_state') or {};keys=set(state.get('claim_ids',[]))
    q=normalize_text(question).strip(' ?!.')
    if not re.fullmatch(r'(?:แล้ว)?ฟรี(?:ไหม|มั้ย|ปะ)|is it free|free|what does it cost',q):return None
    if not keys or keys=={'parking'} and set(state.get('missing_fields',[]))<= {'parking_fee'}:return None
    if len(keys)>1 or state.get('missing_fields'):
        return dict(claim_ids=sorted(keys),missing_fields=state.get('missing_fields',[]),pending_field='fee')
    return None

def resolve_service_fact_followup(question,history,locale='th'):
    if not isinstance(history,list) or not history:return None
    previous=next((h for h in reversed(history) if isinstance(h,dict) and h.get('role')=='assistant'),{})
    if previous.get('delivery_status')!='client_acknowledged':return None
    state=previous.get('service_fact_state') or {};keys=set(state.get('claim_ids',[]))
    if not keys:return None
    q=normalize_text(question).strip(' ?!.');en=locale=='en';query=None
    q=re.sub(r'\s*(?:ครับ|ค่ะ|นะ|หน่อย|please)$','',q).strip()
    if ambiguous_fee_followup(question,history):
        from app.session.context_resolver import ResolvedQuestion
        return ResolvedQuestion(question,question,True,context_domain='service_policy',context_operation='service_fact_clarification',reason='multiple_acknowledged_service_subjects')
    def whole(pattern):return re.fullmatch(pattern,q,re.I) is not None
    if state.get('pending_field')=='fee':
        if whole(r'ที่จอดรถ|parking') and 'parking' in keys:query='Is parking free?' if en else 'ค่าจอดรถฟรีไหม'
        elif whole(r'นั่งดูเพื่อน|ดูเพื่อน|watching|spectators?') and 'spectators' in keys:query='Can I watch my friends for free?' if en else 'นั่งดูเพื่อนฟรีไหม'
        elif whole(r'สมาชิก|membership') and 'membership' in keys:query='Is membership free?' if en else 'ค่าสมาชิกฟรีไหม'
        if query:
            from app.session.context_resolver import ResolvedQuestion
            return ResolvedQuestion(question,query,True,context_domain='service_policy',context_operation='service_fact_followup',reason='selected_service_fee_clarification')
    if 'parking' in keys:
        if whole(r'(?:แล้ว)?\s*(?:มอเตอร์ไซค์|มอไซค์|รถยนต์)(?:ล่ะ|ละ|ด้วย|ไหม|อะ|อ่ะ)?|(?:what about|and) (?:motorcycles?|cars?)'):
            query='Is there parking for cars and motorcycles?' if en else 'มีที่จอดรถสำหรับรถยนต์และมอเตอร์ไซค์ไหม'
        elif keys=={'parking'} and set(state.get('missing_fields',[]))<= {'parking_fee'} and whole(r'(?:แล้ว)?(?:จอด)?ฟรี(?:ไหม|มั้ย|ปะ)|(?:is (?:it|parking) free|free|what does it cost)'):
            query='Is parking free?' if en else 'ค่าจอดรถฟรีไหม'
    if keys=={'spectators'} and not state.get('missing_fields') and whole(r'ฟรี(?:ไหม|มั้ย|ปะ)|is it free'):
        query='Can I watch my friends for free?' if en else 'นั่งดูเพื่อนฟรีไหม'
    if keys=={'location'} and whole(r'(?:ขอ)?ลิง(?:ก์|ค์)?(?:หน่อย|ด้วย)?|(?:can i get (?:the |a )?link|the link|link please)'):
        query='Can I have the studio map link?' if en else 'ขอลิงก์แผนที่ศูนย์'
    if 'checkin_documents' in keys and whole(r'(?:แล้ว)?\s*(?:passport|พาสปอร์ต|บัตรนักศึกษา|บัตรนักเรียน)(?:\s*(?:ล่ะ|ละ|ใช้ได้ไหม))?|(?:and|what about) (?:a )?(?:passport|student card)'):
        query='What identification can I show when I arrive?' if en else 'ตอนมาถึงต้องแสดงบัตรหรือ passport อะไรได้บ้าง'
    if 'personal_keyboard_mouse' in keys:
        if whole(r'(?:แล้ว)?\s*(?:เมาส์|เม้าส์|คีย์บอร์ด|จอย)(?:ล่ะ|ละ|ใช้ได้ไหม|อะ|อ่ะ)?|(?:what about|and) (?:a |my )?(?:mouse|keyboard|controller)'):
            controller=bool(re.search(r'จอย|controller',q))
            query=('Can I bring my own controller for studio use?' if controller else 'Can I bring my own keyboard or mouse?') if en else ('เอาจอยส่วนตัวมาใช้ในศูนย์ได้ไหม' if controller else 'เอาคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ได้ไหม')
    if 'combined_transfer' in keys and re.fullmatch(r'(?:ต้อง)?(?:เขียน|ใส่).{0,15}note|what (?:should|do) i (?:write|put) in (?:the )?note',q,re.I):
        query='Can I make one transfer for multiple machines, and what should I write in the booking note?' if en else 'จองหลายเครื่องโอนครั้งเดียวได้ไหม ต้องเขียนอะไรใน note'
    if 'wrong_slip' in keys and whole(r'(?:แล้ว)?ส่ง(?:ที่ไหน|ทางไหน|ให้ใคร)|where (?:should|do) i send it'):
        query='I uploaded the wrong payment slip image. Where should I send it?' if en else 'แนบสลิปผิดรูปต้องส่งที่ไหน'
    if 'rest_seating' in keys and whole(r'ถ้าไปก่อนเวลาจองรอที่นั่นได้ไหม|can i wait there before my booking'):
        query='Where should I wait before my booked slot?' if en else 'ไปถึงก่อนเวลาจองต้องรอตรงไหน'
    if 'change_time' in keys and whole(r'(?:แล้ว)?เปลี่ยนวัน(?:ล่ะ|ละ|ได้ไหม)?|what about changing the date'):
        query='Can I change my booking date?' if en else 'เปลี่ยนวันจองได้ไหม'
    if not query:return None
    from app.session.context_resolver import ResolvedQuestion
    return ResolvedQuestion(question,query,True,context_domain='service_policy',context_operation='service_fact_followup',reason='acknowledged_service_fact_followup')

def resolve_service_fact_resume(question,record):
    """Explicit subject selection may return to an older acknowledged fact."""
    q=normalize_text(question).strip(' ?!.')
    match=re.fullmatch(r'(?:กลับไป(?:เรื่อง|ที่)?|กลับมาเรื่อง|ย้อนกลับไปเรื่อง|(?:please )?(?:back to|return to|go back to))\s*(.+)',q,re.I)
    if not match:return None
    tail=match[1]
    subjects={
      'parking':r'(?:เรื่อง)?(?:ที่จอดรถ|จอดรถ)|(?:the )?parking',
      'personal_keyboard_mouse':r'(?:เรื่อง)?(?:คีย์บอร์ดส่วนตัว|เมาส์ส่วนตัว|อุปกรณ์ส่วนตัว)|(?:my |the )?(?:own |personal )?(?:keyboard|mouse|personal equipment)',
      'membership':r'(?:การ)?สมัครสมาชิก|(?:the )?(?:studio )?membership',
      'wrong_slip':r'(?:รูป)?สลิป(?:ผิด)?|(?:the )?(?:wrong |payment )?slip',
      'combined_transfer':r'โอนรวม|โอนหลายเครื่อง|(?:the )?(?:combined|single) transfer',
      'checkin_documents':r'เอกสารเช็กอิน|บัตรเช็กอิน|(?:the )?(?:check.in documents|identification)',
    }
    tail=re.sub(r'\s*(?:เมื่อกี้|เดิม|ครับ|ค่ะ|earlier|please)$','',tail).strip()
    selected=next((key for key,pattern in subjects.items() if re.fullmatch(pattern,tail,re.I)),None)
    if selected is None:return None
    acknowledged={turn['response'].get('request_id') for turn in record.get('turns',{}).values() if turn.get('delivery')=='client_acknowledged' and turn.get('response')}
    for h in reversed(record.get('history',[])):
        if h.get('role')!='assistant' or h.get('request_id') not in acknowledged:continue
        state=h.get('service_fact_state') or {};keys=state.get('claim_ids',[])
        if selected not in keys:continue
        from app.session.context_resolver import ResolvedQuestion
        ambiguous=len(keys)!=1 or state.get('pending_field') is not None
        return ResolvedQuestion(question,question if ambiguous else h.get('resolved_text',question),True,context_domain='service_policy',context_operation='service_fact_lookup',reason='ambiguous_service_resume' if ambiguous else 'explicitly_resumed_acknowledged_service_fact')
    from app.session.context_resolver import ResolvedQuestion
    return ResolvedQuestion(question,question,True,context_domain='service_policy',context_operation='service_fact_lookup',reason='no_acknowledged_service_resume')
