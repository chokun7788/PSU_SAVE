"""Bounded lexical candidates for service facts, preserving original input.

Only canonical service nouns are candidates. Numbers, dates, equipment IDs,
negations and proper names are never correction targets. One edit and an
independent sentence anchor are required; this is not a general spell checker.
"""
from __future__ import annotations
import re
from app.core.normalization import normalize_text,THAI_SOFT_MATCH_REMOVE
from app.core.typo_similarity import osa_distance

LEXICON=(
 ('เครื่อง',r'จอง|จออง|หลาย|เปลี่ยน|โอน'),
 ('สมาชิก',r'สมัคร|เข้า|เล่น|ใช้'),('แผนที่',r'ลิง|ไป|ขอ'),
 ('จอดรถ',r'มี|รถ|มอเตอร์|มอไซ'),('คีย์บอร์ด',r'ส่วนตัว|ตัวเอง|นำ|เอา'),
 ('เมาส์',r'ส่วนตัว|ของผม|ตัวเอง|นำ|เอา'),('สลิป',r'แนบ|รูป|ผิด|โอน|อัพ|ส่ง'),
 ('ผิดเครื่อง',r'จอง|เปลี่ยน|แก้'),('ครั้งเดียว',r'โอน|จ่าย|เครื่อง|จอง'),
 ('ที่นั่งพัก',r'มี|พัก'),
 ('membership',r'\b(?:need|play|use|sign|join)\b'),
 ('parking',r'\b(?:car|motorcycle|there|is|free)\b'),
 ('keyboard',r'\b(?:own|personal|bring)\b'),
 ('documents',r'\b(?:bring|check.?in|arriv\w*)\b'),
 ('slip',r'\b(?:payment|wrong|image|uploaded|attach\w*)\b'),
 ('building',r'\b(?:floor|studio|which)\b'),
 ('machine',r'\b(?:wrong|booking|booked|reservation)\b'),
 ('transfer',r'\b(?:one|single|multiple|pay|booking\w*)\b'),
 ('whole',r'\b(?:group|check)\b'),('rest',r'\b(?:area|place|seating)\b'),
 ('watch',r'\b(?:friend\w*|play|just)\b'),
 ('walk',r'\b(?:in|booking|book)\b'),('map',r'\b(?:link|studio|google)\b'),
)
PROTECTED={'not','no','yes','may','can','cant','cannot','dont','without','own','my',
           'rent','best','test','past','seat','seats','maps','game','games','note',
           'team','teams','cash','card','cards','site','staff','state','rate','while'}

def recover_service_fact_query(question):
    q=normalize_text(question);edits=[];spans=[]
    if len(q)>256:return q,edits
    for target,anchor in LEXICON:
        latin=target.isascii()
        if (re.search(r'\b'+re.escape(target)+r'\b',q) if latin else target in q) or not re.search(anchor,q,re.I):continue
        if latin:
            observations=[(m.start(),m.end(),m.group()) for m in re.finditer(r'[a-z]+',q)]
        else:
            observations=[(i,i+n,q[i:i+n]) for n in range(len(target)-2,len(target)+2)
                          for i in range(max(0,len(q)-n+1))
                          if all('\u0e00'<=ch<='\u0e7f' for ch in q[i:i+n])]
        candidates=[]
        for start,end,observed in observations:
            if observed in PROTECTED or not observed or (len(target)==3 and len(observed)<4) or any(t in observed for t in ('ไม่','ห้าม')):continue
            distance=osa_distance(observed,target) if latin else osa_distance(observed.translate(THAI_SOFT_MATCH_REMOVE),target.translate(THAI_SOFT_MATCH_REMOVE))
            if (latin and abs(len(observed)-len(target))<=1 and distance==1) or (not latin and distance<=1):
                candidates.append((start,end,observed))
        # Different windows for one dropped character may overlap. Prefer the
        # longest single span; separated alternatives make the recovery unsafe.
        if not candidates:continue
        candidates.sort(key=lambda x: (osa_distance(x[2] if latin else x[2].translate(THAI_SOFT_MATCH_REMOVE),target if latin else target.translate(THAI_SOFT_MATCH_REMOVE)),osa_distance(x[2],target),-(x[1]-x[0]),x[0]))
        start,end,observed=candidates[0]
        if any(a>=end or b<=start for a,b,_ in candidates[1:]):continue
        if any(a<end and start<b for a,b,_ in spans):continue
        spans.append((start,end,target));edits.append(dict(observed=observed,intended=target,start=start,end=end,distance=osa_distance(observed,target),method='anchored_osa_one_edit' if latin else 'anchored_osa_one_edit_with_diacritic_fold'))
    for start,end,target in sorted(spans,reverse=True):q=q[:start]+target+q[end:]
    return q,edits
