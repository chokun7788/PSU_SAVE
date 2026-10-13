"""Only high confidence unrelated tasks are rejected before studio routing.

Other unfamiliar service questions still reach source lookup or clarification.
"""
import re
from app.core.normalization import normalize_text

def is_explicit_unrelated_task(text: str) -> bool:
 q=normalize_text(text)
 anchored=bool(re.search(r'ศูนย์|ร้าน|ที่นี่|มหาวิทยาลัย|จอง|ค่าบริการ|กติกา|เกม|\b(?:psu|studio|gaming|games?|booking|reservation|pc|ps5|vr|nintendo|cockpit)\b',q,re.I))
 if anchored:return False
 meal=bool(re.search(r'(?:กิน|ทาน).{0,12}อะไร.{0,6}(?:ดี|คืนนี้|เย็นนี้)|\bwhat\s+(?:should|shall|can)\s+i\s+(?:eat|have\s+for\s+(?:dinner|lunch|breakfast))\b',q,re.I))
 origin=bool(('ไก่' in q and 'ไข่' in q and re.search(r'ก่อน|เกิด',q)) or re.search(r'\b(?:chicken.{0,30}egg|egg.{0,30}chicken)\b',q,re.I))
 writing=bool(re.search(r'^(?:ช่วย)?(?:เขียน|แต่ง|ร่าง)(?:บทความ|นิยาย|เรื่องสั้น|กลอน)|^(?:please\s+)?(?:write|draft|compose)\b',q,re.I))
 recipe=bool(re.search(r'สูตร(?:อาหาร|เค้ก)|\brecipe\b',q,re.I))
 return meal or origin or writing or recipe
