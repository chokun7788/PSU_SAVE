"""Resolve explicit rejected-task prefixes only when the new task is named.

This does not rewrite ordinary negative facts (not a student, not allowed),
free-form quoted text, or device exclusions. Preserve the original in trace.
"""
from __future__ import annotations
import re

def explicit_request_focus(question: str):
    patterns = (
        r'^\s*ไม่(?:เอา|ต้องการ|ใช่)\s*(?:ราคา|ค่าบริการ|กฎ(?:การแข่งขัน|แข่ง)?|กติกา(?:แข่ง)?)[ ,.;]*\s*((?:ขอ|เอา|บอก).+)$',
        r'^\s*(?:i\s+(?:do\s+not|don\W?t)\s+want|not|no)\s+(?:the\s+)?(?:prices?|fees?|(?:tournament|competition)\s+rules?)[ ,.;]*\s*((?:(?:just\s+)?(?:list|show|tell|give)|how\s+do\s+i|what\s+games).+)$',
    )
    for pattern in patterns:
        m = re.match(pattern,question,re.I)
        if not m:continue
        focused=m.group(1).strip()
        # Both explicit negation and an affirmative task anchor are needed.
        if not re.search(r'รายชื่อเกม|ปุ่ม|เกม.*(?:ทั้งหมด|อะไร)|\b(?:games?|shoot|reload|controls?)\b',focused,re.I):continue
        return focused,dict(original=question,focused=focused,rejected_prefix=question[:m.start(1)],method='explicit_task_correction')
    return question,None
