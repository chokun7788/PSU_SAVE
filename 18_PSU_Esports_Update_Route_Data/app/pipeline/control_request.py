"""Recognize a missing control target without guessing an unknown game title.

Only generic request words may remain. Hardware faults, booking buttons,
negation, editions and explicit names continue through their existing paths.
"""
import re
from app.core.normalization import normalize_text

_EN_GENERIC = frozenset(('show list me the game games controls control buttons button '
    'please what are which keys key controller keyboard mouse i want see can how do use '
    'tell need to for of in on about all every my give could would you explain').split())
_TH_GENERIC = tuple(sorted(('ปุ่มควบคุม','ควบคุม','บังคับ','ปุ่ม','เกม','เล่น','กด','ทั้งหมด',
    'ทุก','อะไร','ไหน','อย่างไร','ยังไง','อย่างไง','มี','ใช้','ต้อง','ขอ','ดู','ช่วย','บอก',
    'สอน','แสดง','อยาก','รู้','วิธี','รายการ','หน่อย','ครับ','ค่ะ','คับ','นะ','ได้','บ้าง',
    'มั่ง','ไหม','ของ','การ','จะ','ให้','กี่'), key=len, reverse=True))

def is_generic_control_request(query: str) -> bool:
    q = normalize_text(query)
    if re.search(r'\d|ไม่|ห้าม|อย่า|\b(?:not|no|without|except|instead)\b', q):
        return False
    if not re.search(r'ปุ่ม|ควบคุม|บังคับ|\b(?:controls?|buttons?|keys?)\b', q):
        return False
    rest = q
    for word in _TH_GENERIC:
        rest = rest.replace(word, ' ')
    tokens = re.findall(r'[a-z]+|[\u0e00-\u0e7f]+', rest)
    return bool(q.strip()) and all(token in _EN_GENERIC for token in tokens)

def is_booking_button_request(query: str) -> bool:
    q = normalize_text(query)
    if re.search(r'ไม่|ห้าม|\b(?:not|without|except)\b', q):
        return False
    # A navigation shortcut may answer only a navigation request, not a
    # second operation sharing the same sentence.
    if re.search(r'ราคา|ค่าบริการ|กฎ|กฏ|กติกา|ว่าง|อุปกรณ์|ควบคุม|\b(?:prices?|fees?|cost|rules?|available|equipment|hardware|controls?)\b', q):
        return False
    return bool(re.search(r'ปุ่มจอง|(?:จอง.*ปุ่ม|ปุ่ม.*จอง)|\b(?:booking|reservation|reserve|book)\b.*\bbutton\b|\bbutton\b.*\b(?:booking|reservation|reserve|book)\b', q))
