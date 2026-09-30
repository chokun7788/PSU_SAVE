from __future__ import annotations

import re

from app.core.normalization import normalize_text


_NEGATED_STUDENT = re.compile(
    r"ไม่ใช่\s*(?:นักศึกษา|นักเรียน|นิสิต|เด็ก)"
    r"|ไม่ได้เป็น\s*(?:นักศึกษา|นักเรียน|นิสิต)"
    r"|ไม่ใช่\s*(?:psu\s+)?student"
    r"|\b(?:not\s+(?:a\s+)?(?:psu\s+)?student|non[- ]?student)\b",
    flags=re.IGNORECASE,
)


def excludes_student_group(query: str) -> bool:
    return bool(_NEGATED_STUDENT.search(normalize_text(query)))
