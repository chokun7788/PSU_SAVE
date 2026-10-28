"""Select declared FAQ topics; the answer always comes from source fields."""
import re
from .registry import value
from .query_contract import normalize

def select(question,records,operation):
    q=normalize(question)
    damage=bool(re.search(r'เสียหาย|ทำ.{0,8}พัง|\b(?:damag\w*|broken)\b',q))
    payment=bool(re.search(r'ชำระ|จ่าย|\b(?:payment|pay|paid)\b',q))
    cancel_action=bool(re.search(r'(?:ยกเลิก.{0,30}(?:ยังไง|ยังงัย|อย่างไร|ได้ไหม)|(?:อยาก|ต้องการ|จะ)ยกเลิก)|\b(?:how (?:do|can|to)|can i|may i|want to)\b.{0,35}\bcancel\b',q))
    refund=bool(re.search(r'คืนเงิน|\brefund\b',q))
    required=bool(re.search(r'ไม่.{0,10}จอง|ต้องจอง|เดินเข้า|walk.in|without.{0,12}book|booking.required|need.{0,8}book',q))
    if operation=='policy' and damage:
        topic='damage';pattern=r'เสียหาย|damage|compensation'
    elif operation=='policy' and re.search(r'ปลั๊กไฟ|เสียบปลั๊ก|\b(?:plug\s+in|power\s+outlets?|charg\w*)\b',q):
        topic='personal_power';pattern=r'ปลั๊กไฟ|power\s+(?:outlet|plugs?|general)|personal\s+power'
    elif operation=='policy' and re.search(r'คืน|\breturn(?:ing)?\b',q) and re.search(r'อุปกรณ์|แผ่นเกม|จอย|\b(?:equipment|controllers?|discs?|games?)\b',q) and not re.search(r'คืนเงิน|\brefund\b',q):
        topic='return_equipment';pattern=r'คืน.{0,25}(?:อุปกรณ์|แผ่นเกม|จอย)|\breturn\b.{0,35}\b(?:equipment|controllers?|game discs?)\b'
    elif operation=='booking' and payment and not cancel_action and not refund:
        if re.search(r'บัญชี|ธนาคาร|สลิป|\b(?:bank|slip|receipt|account|transfer)\b',q):return []
        topic='payment';pattern=r'ชำระ.{0,12}หลังจอง|หลังจอง.{0,12}จ่าย|payment.timeout|pay.after.booking'
    elif operation=='booking' and required and not cancel_action:
        topic='booking_required';pattern=r'walk.in|เดินเข้า|booking.required|must.book.in.advance|ต้องจองล่วงหน้า'
    elif operation=='booking' and re.search(r'ยกเลิก|\bcancel',q) and (cancel_action or not re.search(r'อัตโนมัติ|ไม่จ่าย|ข้อมูลผิด|\b(?:automatic|unpaid|incorrect)\b',q)):
        topic='cancel';pattern=r'^ยกเลิก.*(?:จอง|ล่วงหน้า)|^cancel.*(?:reservation|advance)|^แก้ไข.*จอง|^edit.*booking'
    else:return []
    ranked=[]
    for rid,r in records.items():
        if r['kind']!='faq':continue
        heading=value(r,'question') or {};heading=' '.join(str(s or '') for s in heading.values()) if isinstance(heading,dict) else str(heading)
        heading=normalize(heading).replace('_',' ')
        if not re.search(pattern,heading):continue
        score=0
        if topic=='damage':
            severity=[p for p in (r'เล็กน้อย|minor',r'ปานกลาง|moderate|medium',r'ร้ายแรง|severe') if re.search(p,q)]
            if severity and not any(re.search(p,heading) for p in severity):continue
            if not severity and re.search(r'เล็กน้อย|ปานกลาง|ร้ายแรง|minor|moderate|medium|severe',heading):continue
            score+=bool(re.search(r'summary|responsib|รับผิดชอบ',heading))
        if topic=='payment':score+=bool(re.search(r'ชำระ.{0,12}หลังจอง|pay.after.booking',heading))
        if topic=='cancel':
            how=bool(re.search(r'ยังไง|ยังงัย|อย่างไร|\bhow\b',q))
            score+=bool(re.search(r'แก้ไข|^edit',heading)) if how else bool(re.search(r'^ยกเลิก|^cancel',heading))
        ranked.append((score,rid))
    if not ranked:return []
    best=max(score for score,_ in ranked)
    return [rid for score,rid in ranked if score==best]
