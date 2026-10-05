"""Render a bounded overview from substantive clauses of one locked rulebook."""
from __future__ import annotations

import re
from dataclasses import dataclass

from app.knowledge.localization import approved_localization
from app.pipeline.competition_source_facets import source_row_supports_facet
from app.pipeline.competition_targets import resolve_competition_targets


@dataclass(frozen=True)
class CompetitionOverview:
    answer: str
    hits: list[dict]
    section_ids: tuple[str, ...]


_FACETS = (
    'eligibility_registration', 'team_size', 'competition_format',
    'equipment', 'pre_match_on_site', 'match_settings', 'pause_timeout',
    'penalty', 'conduct', 'dispute', 'schedule',
)
_CLAUSE = re.compile(
    r'ต้อง|ห้าม|อนุญาต|เท่านั้น|ไม่สามารถ|ปรับแพ้|ผู้ตัดสิน|ประกอบด้วย|ทีมละ|กำหนด|ขอได้|ทำได้|สามารถ|ใช้เมื่อ|'
    r'เวลา\s*\d|ผู้ชนะ|รอบละ|\b(?:must|shall|may|allowed|required|prohibited|'
    r'can|consists|requested|forfeit|winner|elimination|bo[1357])\b', re.I,
)


def substantive_lines(text: str) -> tuple[str, ...]:
    """Preserve complete source lines; headings and export metadata are not rules."""
    lines = []
    for raw in text.splitlines():
        line = raw.strip().lstrip('*-•· ').strip()
        if not 32 <= len(line) <= 640 or not _CLAUSE.search(line):
            continue
        if re.match(r'(?i)^(?:update:|english below|กฎระเบียบและรูปแบบการแข่งขัน)', line):
            continue
        if line not in lines:
            lines.append(line)
    return tuple(lines)


def build_competition_overview(query: str, locale: str) -> CompetitionOverview | None:
    # Import lazily: retrieval itself uses competition target resolution.
    from app.pipeline.retrieval import hit_from_curated, load_curated_rows

    resolution = resolve_competition_targets(query)
    if resolution.status != 'exact':
        return None
    target = resolution.targets[0]
    rows = [
        row for row in load_curated_rows()
        if row.get('category') == 'competition_rules'
        and not row.get('_canonical_projection')
        and str(row.get('id', '')).startswith(target.rulebook_id + '_s')
        and target.rulebook_id in row.get('source_ids', [])
    ]
    clauses = {}
    for row in rows:
        text = approved_localization(row, 'text') if locale == 'en' else str(row.get('text', ''))
        if text:
            lines = substantive_lines(text)
            if lines:
                clauses[str(row['id'])] = lines
    selected = []
    seen = set()
    for facet in _FACETS:
        candidate = next((row for row in rows if row['id'] in clauses and row['id'] not in seen and source_row_supports_facet(row, facet)), None)
        if candidate:
            selected.append(candidate)
            seen.add(candidate['id'])
        if len(selected) >= 8:
            break
    for row in rows:
        if len(selected) >= 8:
            break
        if row['id'] in clauses and row['id'] not in seen:
            selected.append(row)
            seen.add(row['id'])
    if len(selected) < 3:
        return None
    english = locale == 'en'
    tournament = str(selected[0].get('tournament', ''))
    if english:
        localized_tournament = approved_localization(selected[0], 'tournament')
        years = re.findall(r'\b20\d{2}\b', tournament)
        tournament = localized_tournament or (target.label + (' / ' + years[0] if years else ''))
    title = f'Selected {target.label} competition rules from the recorded rulebook:' if english else f'สรุปกติกา {target.label} บางประเด็นจากเอกสารที่มี:'
    lines = [title, f'Tournament: {tournament}' if english else f'รายการ: {tournament}', '']
    emitted = set()
    used = []
    for row in selected:
        row_lines = [line for line in clauses[row['id']][:2] if line not in emitted]
        if row_lines:
            used.append(row)
            label = approved_localization(row, 'section_title') if english else str(row.get('section_title', ''))
            if label and len(label) <= 100 and not any(label.casefold() in line.casefold() for line in row_lines):
                lines.append('\n**' + label + '**')
            for line in row_lines:
                emitted.add(line)
                lines.append('•    ' + line)
    lines.extend(['', 'This is a summary of selected clauses. Ask about a specific topic for details.' if english else 'นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ', f'Source: {selected[0].get("source_url", "")}' if english else f'แหล่งข้อมูล: {selected[0].get("source_url", "")}'])
    return CompetitionOverview('\n'.join(lines), [hit_from_curated(row) for row in used], tuple(row['id'] for row in used))
