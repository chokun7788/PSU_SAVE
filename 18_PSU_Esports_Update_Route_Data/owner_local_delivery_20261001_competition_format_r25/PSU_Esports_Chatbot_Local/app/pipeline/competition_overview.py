"""Render a bounded overview from substantive clauses of one locked rulebook."""
from __future__ import annotations

import re
from dataclasses import dataclass

from app.knowledge.localization import approved_localization
from app.pipeline.competition_targets import resolve_competition_targets
from app.pipeline.competition_source_facets import source_row_supports_facet
from app.pipeline.competition_presentation import clause_supports_facet, is_rule_clause, requested_pause_kind, source_clause_lines


@dataclass(frozen=True)
class CompetitionOverview:
    answer: str
    hits: list[dict]
    section_ids: tuple[str, ...]


_FACETS = (
    'competition_format', 'team_size', 'eligibility_registration',
    'equipment', 'match_settings', 'pre_match_on_site', 'pause_timeout',
    'conduct', 'penalty', 'dispute', 'schedule',
)
_LABELS = {
    'competition_format': ('รูปแบบการแข่งขัน', 'Competition format'),
    'team_size': ('ผู้เล่นและองค์ประกอบทีม', 'Players and team composition'),
    'eligibility_registration': ('คุณสมบัติและการลงทะเบียน', 'Eligibility and registration'),
    'equipment': ('อุปกรณ์การแข่งขัน', 'Competition equipment'),
    'match_settings': ('การตั้งค่าแมตช์', 'Match settings'),
    'pre_match_on_site': ('ก่อนแข่งและหน้างาน', 'Before the match'),
    'pause_timeout': ('การหยุดเกมและเวลานอก', 'Pauses and timeouts'),
    'conduct': ('ข้อห้ามและพฤติกรรม', 'Restrictions and conduct'),
    'penalty': ('บทลงโทษ', 'Penalties'),
    'dispute': ('ข้อพิพาท', 'Disputes'),
    'schedule': ('กำหนดการ', 'Schedule'),
    'other': ('ข้อกำหนดเพิ่มเติม', 'Additional rules'),
}
def substantive_lines(text: str) -> tuple[str, ...]:
    """Preserve complete source lines; headings and export metadata are not rules."""
    lines = []
    for raw in source_clause_lines(text):
        line = raw.strip().lstrip('*-•· ').strip()
        if len(line) < 12 or not is_rule_clause(line):
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
    selected_facets = {}
    selected_clauses = {}
    seen = set()
    for facet in _FACETS:
        def display_clauses(row):
            title = str(row.get('section_title') or '')
            pause_section = bool(re.search(r'(?i)technical pause|tactical timeout|emergency pause|หยุดเกมทางเทคนิค|เวลานอกทางยุทธวิธี|การหยุดกรณีฉุกเฉิน', title))
            if pause_section and facet != 'pause_timeout':
                return ()
            if facet == 'pause_timeout' and pause_section:
                return clauses[row['id']]
            return tuple(line for line in clauses[row['id']] if clause_supports_facet(line, facet))
        candidates = [row for row in rows if row['id'] in clauses and row['id'] not in seen and display_clauses(row)]
        candidates.sort(key=lambda row: (
            not bool(requested_pause_kind(str(row.get('section_title') or ''))) if facet == 'pause_timeout' else False,
            not any(re.search(r'ทีมละ\s*\d+\s*ครั้ง|\d+\s*(?:times|requests|timeouts)|five times', line, re.I) for line in display_clauses(row)) if facet == 'pause_timeout' else False,
            not source_row_supports_facet(row, facet),
        ))
        # Pause kinds remain separate. A technical clause cannot stand in for
        # a tactical timeout; Tekken's two source sections must both be shown.
        if facet == 'pause_timeout':
            kinds = set()
            unique = []
            for row in candidates:
                kind = requested_pause_kind(str(row.get('section_title') or ''))
                if kind and kind in kinds:
                    continue
                unique.append(row)
                if kind:
                    kinds.add(kind)
                if len(unique) == 3:
                    break
            candidates = unique
        for candidate in candidates[:3 if facet == 'pause_timeout' else 1]:
            selected.append(candidate)
            selected_facets[candidate['id']] = facet
            selected_clauses[candidate['id']] = display_clauses(candidate)
            seen.add(candidate['id'])
        if len(selected) >= 8:
            break
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
    groups = {}
    for row in selected:
        facet = selected_facets[row['id']]
        groups.setdefault(facet, []).append(row)
    selected = [row for facet in (*_FACETS, 'other') for row in groups.get(facet, [])]
    shown_groups = set()
    for row in selected:
        row_lines = [line for line in selected_clauses[row['id']][:2] if line not in emitted]
        if row_lines:
            used.append(row)
            facet = next(facet for facet, group in groups.items() if row in group)
            if facet not in shown_groups:
                lines.append('\n**' + _LABELS[facet][1 if english else 0] + '**')
                shown_groups.add(facet)
            label = approved_localization(row, 'section_title') if english else str(row.get('section_title', ''))
            if facet == 'pause_timeout' and label and re.search(r'(?i)technical pause|tactical timeout|emergency pause|หยุดเกมทางเทคนิค|เวลานอกทางยุทธวิธี', label) and len(label) <= 100 and not any(label.casefold() in line.casefold() for line in row_lines):
                lines.append('\n**' + label + '**')
            for line in row_lines:
                emitted.add(line)
                lines.append('•    ' + line)
    if target.game_id == 'tekken8' and 'pause_timeout' in shown_groups:
        lines.extend(['', 'The recorded rulebook contains both a no-pause clause and an emergency/agreement exception. Ask the organizer to confirm which conditions and penalties apply.' if english else 'เอกสารมีทั้งข้อห้ามหยุดเกมและข้อยกเว้นกรณีฉุกเฉิน/ผู้เล่นเห็นพ้อง ต้องให้ผู้จัดยืนยันขอบเขตและบทลงโทษที่ใช้ครับ'])
    lines.extend(['', 'This is a summary of selected clauses. Ask about a specific topic for details.' if english else 'นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ', f'Source: {selected[0].get("source_url", "")}' if english else f'แหล่งข้อมูล: {selected[0].get("source_url", "")}'])
    return CompetitionOverview('\n'.join(lines), [hit_from_curated(row) for row in used], tuple(row['id'] for row in used))
