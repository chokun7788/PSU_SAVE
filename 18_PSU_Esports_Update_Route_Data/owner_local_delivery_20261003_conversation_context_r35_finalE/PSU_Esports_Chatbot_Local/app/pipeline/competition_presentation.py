"""Source-only presentation helpers; never publish or alter rulebook policy."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from app.knowledge.localization import approved_localization


_PAUSE_KINDS = (
    ('technical', ('technical pause', 'หยุดเกมทางเทคนิค')),
    ('tactical', ('tactical timeout', 'เวลานอกทางยุทธวิธี')),
    ('emergency', ('emergency pause', 'หยุดกรณีฉุกเฉิน', 'พักฉุกเฉิน')),
)


def requested_pause_kind(query: str) -> str | None:
    q = query.casefold()
    kinds = [kind for kind, terms in _PAUSE_KINDS if any(term in q for term in terms)]
    return kinds[0] if len(kinds) == 1 else None


def pause_rows_for_query(query: str, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    kind = requested_pause_kind(query)
    if not kind:
        return rows
    terms = dict(_PAUSE_KINDS)[kind]
    matching = [row for row in rows if any(term in str(row.get('section_title') or row.get('title') or row.get('text') or '').casefold() for term in terms)]
    return matching


def source_clause_lines(text: str) -> list[str]:
    # Approved English overlays sometimes retain bullets but flatten newlines.
    # Multi-level rule numbers delimit clauses; decimals/time values do not.
    return [line.strip().lstrip('*-•· ').strip() for line in re.split(r'\n|\s+\*\s+|\s+(?=\d+(?:\.\d+)+\.?\s*[^\W\d_])', text) if line.strip()]


def is_rule_clause(line: str) -> bool:
    body = re.sub(r'^\d+(?:\.\d+)*[.)]?\s*', '', line)
    if re.match(r'(?i)^(?:อุปกรณ์ที่อนุญาต$|การตั้งค่า(?:ใน)?เกม$|ประเภทบทลงโทษในเกม$|in.game penalty types$|penalty types in the game$|กติกาการแข่งขัน|กฎระเบียบและรูปแบบการแข่งขัน|competition rules(?: for| and format|$))', body):
        return False
    return bool(re.search(r'ต้อง|ห้าม|อนุญาต|ปรับแพ้|เท่านั้น|ประกอบด้วย|ขอได้|ใช้เมื่อ|ทำได้|ไม่สามารถ|สามารถ|ชนะ|\b(?:must|shall|may|can|no|not|cannot|allowed|permitted|prohibited|required|uses?|used|played|winner|forfeit|consists|elimination|penalty|losing|requested|warning|rollback)\b', body, re.I) or re.search(r'\d', body))


# Display scope is checked at clause level, without a broad section heading.
# These predicates neither change source policy nor grant V2 publication.
_CLAUSE_FACETS = {
    'competition_format': r'single elimination|double elimination|best[- ]of[- ]\d|\bBO[1357]\b|\bFT2\b|1v1|1 ต่อ 1|ตัวต่อตัว|offline mode|โหมดออฟไลน์',
    'team_size': r'องค์ประกอบทีม|ผู้เล่น\s*\d+\s*คน|ทีมละ\s*\d+\s*คน|team composition|each team consists of \d+ players',
    'eligibility_registration': r'คุณสมบัติ|รับเฉพาะ|ลงทะเบียน|รับสมัคร|สมัครแข่งขัน|\beligib|\bregister|\bregistration|roster submission',
    'equipment': r'คีย์บอร์ด|เมาส์|หูฟัง|โทรศัพท์|แท็บเล็ต|สมาร์ทวอทช์|อุปกรณ์|keyboard|mouse|headset|ear headphones|mobile phone|tablets?|ipad|smartwatch|controller|playstation|snap tap|SOCD',
    'match_settings': r'การตั้งค่า|เวอร์ชัน|เงินเริ่มต้น|เวลาต่อรอบ|เวลาแข่งขันต่อรอบ|จำนวนรอบ|competitive.{0,8}5v5|freeze time|starting money|round time|rounds per game|time per round|latest version|\bR3\b|\b60S\b|overtime|advantage:',
    'pre_match_on_site': r'รายงานตัว|มาถึงสนาม|ก่อนเวลาแข่ง|ช่วงเตรียมตัว|ก่อนการแข่งขันทุกครั้ง|check.in|arriv.{0,25}venue|match prep|before.{0,20}match|until the match (?:ends|concludes)|จนกว่าจะจบแมตช์',
    'pause_timeout': r'หยุดเกม|หยุดพัก|เวลานอก|ขอได้ \d+ ครั้ง|technical pause|tactical timeout|emergency.pause|\bpaus(?:e[ds]?|ing)\b|\btimeouts?\b',
    'conduct': r'น้ำใจนักกีฬา|ก้าวร้าว|วาจา|หยาบคาย|ไม่สุภาพ|เสียดสี|ดูถูก|hate speech|sportsman|sportsmanship|aggressi|rude|disrespect|offensive',
    'penalty': r'ปรับแพ้|ตัดสิทธิ์|แบนถาวร|ตักเตือน|\bforfeit|\bdisqualif|round loss|round rollback|\bwarning\b|map loss|permanent ban',
    'dispute': r'ข้อโต้แย้ง|ข้อพิพาท|ประท้วง|\bdispute|\bprotest|\bobjection',
    'schedule': r'เวลา \d[.:]\d|วันแข่งขัน|แข่งขันออฟไลน์ วันที่|\b\d{2}:\d{2}-\d{2}:\d{2}\b',
}


def clause_supports_facet(line: str, facet: str) -> bool:
    facet = {'match_configuration': 'match_settings', 'registration': 'eligibility_registration',
             'fair_play_conduct': 'conduct', 'protest_dispute': 'dispute', 'disconnect': 'pause_timeout'}.get(facet, facet)
    expression = _CLAUSE_FACETS.get(facet)
    if facet in ('equipment', 'match_settings') and re.search(_CLAUSE_FACETS['pause_timeout'], line, re.I):
        return False
    return bool(expression and re.search(expression, line, re.I))


def focused_rule_lines(query: str, text: str, facet: str | None) -> list[str]:
    pause = focused_pause_lines(query, text)
    if pause is not None:
        return pause
    lines = source_clause_lines(text)
    clauses = [line for line in lines if is_rule_clause(line)]
    if not clauses and facet == 'map_pool' and len(lines) >= 4 and re.search(r'\bmaps?\b', lines[0], re.I):
        return ['; '.join(lines[1:])]
    if facet:
        scoped = [line for line in clauses if clause_supports_facet(line, facet)]
        if scoped:
            clauses = scoped
    # Device questions name the requested device; other equipment clauses are
    # context only, and cannot replace the permission/prohibition requested.
    device_terms = [term for term in ('tablet', 'ipad', 'keyboard', 'mouse', 'controller', 'snap tap', 'socd') if term in query.casefold()]
    if device_terms:
        clauses = [line for line in clauses if any(term in line.casefold() for term in device_terms)]
    return clauses


def focused_pause_lines(query: str, text: str) -> list[str] | None:
    """None means no special scope; [] means no clause supports that scope."""
    if not requested_pause_kind(query):
        return None
    clauses = [line for line in source_clause_lines(text) if is_rule_clause(line)]
    if re.search(r'สื่อสาร|communicat|\btalk\b|\bchat\b', query, re.I):
        return [line for line in clauses if re.search(r'สื่อสาร|communicat|\btalk\b|\bchat\b', line, re.I)][:1]
    if re.search(r'กี่(?:ครั้ง|นาที|วินาที)|how (?:many|long)|duration|allowance|quota', query, re.I):
        return [line for line in clauses if re.search(r'\d|\b(?:one|two|three|four|five|ten)\b', line, re.I)]
    return clauses


def render_rule_reply(first: str, details: list[str], row: dict[str, Any], locale: str) -> str:
    english = locale == 'en'
    game = str(row.get('game') or '')
    event = approved_localization(row, 'tournament') if english else str(row.get('tournament') or '')
    label = game + (f' / {event}' if event else '')
    lines = [('Answer: ' if english else 'คำตอบ: ') + first.strip().lstrip('*-•· ').strip()]
    unique = list(dict.fromkeys(line.strip().lstrip('*-•· ').strip() for line in details if line.strip()))
    unique = [line for line in unique if line != first.strip().lstrip('*-•· ').strip()]
    if unique:
        lines.extend(['', 'Details:' if english else 'รายละเอียดที่เกี่ยวข้อง:'])
        lines.extend('• ' + line for line in unique)
    lines.extend(['', ('Rulebook: ' if english else 'อ้างอิงจากกติกา: ') + label,
                  ('Source: ' if english else 'แหล่งข้อมูล: ') + str(row.get('source_url') or '')])
    return '\n'.join(lines)


@dataclass(frozen=True)
class SourcePenaltyTable:
    answer: str
    rows: tuple[dict[str, Any], ...]
    pairs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class SourcePenaltyTypes:
    answer: str
    rows: tuple[dict[str, Any], ...]


def build_penalty_types(query: str, rows: list[dict[str, Any]]) -> SourcePenaltyTypes | None:
    """Read a complete numbered source list only for a general types question."""
    if not re.search(r'บทลงโทษ.{0,25}(?:ประเภท|อะไรบ้าง|ไหนบ้าง|อย่างไร|ยังไง)|ประเภท.{0,15}บทลงโทษ', query):
        return None
    if re.search(r'โกง|ช่องโหว่|บัค|มาสาย|สตรีม|หยุด|pause|cheat|exploit', query, re.I):
        return None
    from app.pipeline.retrieval import load_curated_rows
    heading = next((row for row in rows if str(row.get('text') or '').strip() == 'ประเภทบทลงโทษในเกม'), None)
    if heading is None:
        return None
    document = str(heading['id']).rsplit('_s', 1)[0]
    origin = sorted([row for row in load_curated_rows() if not row.get('_canonical_projection') and str(row.get('id') or '').startswith(document + '_s')], key=_order)
    kinds = ('Warning', 'Round Rollback', 'Round Loss', 'Map Forfeit', 'Match Forfeit')
    selected = []
    section, chunk = _order(heading)
    for index, kind in enumerate(kinds, 1):
        row = next((row for row in origin if _order(row) == (section + index, 1)), None)
        text = str(row.get('text') or '').strip() if row else ''
        if row is None or not re.match(rf'^{index}\.\s', text) or f'({kind})' not in text:
            return None
        selected.append(row)
    clauses = [str(row['text']).strip() for row in selected]
    return SourcePenaltyTypes(render_rule_reply(clauses[0], clauses[1:], selected[0], 'th'), tuple(selected))


def _order(row: dict[str, Any]) -> tuple[int, int]:
    match = re.search(r'_s(\d+)_c(\d+)$', str(row.get('id') or ''))
    return (int(match[1]), int(match[2])) if match else (0, 0)


def build_penalty_table(query: str, locale: str, rows: list[dict[str, Any]]) -> SourcePenaltyTable | None:
    if not re.search(r'ตารางบทลงโทษ|penalty\s+(?:matrix|table)|penalties\s+table', query, re.I):
        return None
    table = next((row for row in rows if 'การละเมิด\nบทลงโทษ\n' in str(row.get('text') or '')), None)
    if table is None:
        return None
    # Read adjoining source records only to finish a pair cut by the importer.
    from app.pipeline.retrieval import load_curated_rows
    record_id = str(table['id'])
    document = record_id.rsplit('_s', 1)[0]
    document_rows = sorted([row for row in load_curated_rows() if not row.get('_canonical_projection') and str(row.get('id') or '').startswith(document + '_s')], key=_order)
    body = str(table['text']).split('การละเมิด\nบทลงโทษ\n', 1)[1]
    cells = [line.strip() for line in body.splitlines() if line.strip()]
    used = [table]
    if len(cells) % 2:
        successor = next((row for row in document_rows if _order(row) == (_order(table)[0] + 1, 1)), None)
        continuation = str(successor.get('text') or '').strip() if successor else ''
        if successor and '\n' not in continuation and re.fullmatch(r'(?:แบนถาวร|ปรับแพ้[^\n]{0,100}|ตัดสิทธิ์[^\n]{0,100}|ตักเตือน)', continuation):
            cells.append(continuation)
            used.append(successor)
    if len(cells) < 2 or len(cells) % 2:
        return None
    pairs = list(zip(cells[::2], cells[1::2]))
    english = locale == 'en'
    if english:
        translations = [approved_localization(row, 'text') for row in used]
        if any(text is None for text in translations):
            return None
        flat = ' '.join(' '.join(text.split()) for text in translations if text)
        flat = re.sub(r'^.*?\bViolation\s+Penalty\s+', '', flat, count=1, flags=re.I)
        # Boundaries use only penalty expressions present in approved text.
        expression = re.compile(r'Warning(?:\s*→\s*Loss in that round)?(?:\s*→\s*Disqualification)?|Loss in that (?:round(?: or match)?|match)(?:\s*(?:/|→)\s*Disqualification(?: from competition)?)?|Permanent ban', re.I)
        translated_pairs = []
        start = 0
        for match in expression.finditer(flat):
            violation = flat[start:match.start()].strip()
            if not violation:
                return None
            translated_pairs.append((violation, match.group(0)))
            start = match.end()
        if flat[start:].strip() or len(translated_pairs) != len(pairs):
            return None
        pairs = translated_pairs
    def cell(text: str) -> str:
        return text.replace('|', '\\|')
    header = 'Answer: Penalties listed in this competition rulebook:' if english else 'คำตอบ: ตารางบทลงโทษตามกติกาของรายการนี้:'
    lines = [header, '', '| Violation | Penalty |' if english else '| การละเมิด | บทลงโทษ |', '| --- | --- |']
    lines.extend(f'| {cell(left)} | {cell(right)} |' for left, right in pairs)
    label = str(table.get('game') or '')
    event = approved_localization(table, 'tournament') if english else str(table.get('tournament') or '')
    if event:
        label += ' / ' + event
    lines.extend(['', ('Rulebook: ' if english else 'อ้างอิงจากกติกา: ') + label,
                  ('Source: ' if english else 'แหล่งข้อมูล: ') + str(table.get('source_url') or '')])
    return SourcePenaltyTable('\n'.join(lines), tuple(used), tuple(pairs))
