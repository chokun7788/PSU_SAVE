"""Render a bounded overview from substantive clauses of one locked rulebook."""
from __future__ import annotations

import re
from dataclasses import dataclass

from app.knowledge.localization import approved_localization
from app.pipeline.competition_targets import resolve_competition_targets
from app.pipeline.competition_conversation_signals import is_more_rule_request, is_rulebook_catalog_request
from app.pipeline.competition_source_facets import source_row_supports_facet
from app.pipeline.competition_presentation import clause_supports_facet, is_rule_clause, requested_pause_kind, source_clause_lines


@dataclass(frozen=True)
class CompetitionOverview:
    answer: str
    hits: list[dict]
    section_ids: tuple[str, ...]
    history_answer_count: int = 0
    excluded_clause_count: int = 0
    no_further_clauses: bool = False


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


def build_rulebook_catalog(query: str, locale: str) -> CompetitionOverview | None:
    """List recorded rulebooks; this is not a claim about open registration."""
    from app.pipeline.competition_targets import target_for_game_id
    from app.pipeline.competition_taxonomy import COMPETITION_GAME_IDS
    from app.pipeline.retrieval import hit_from_curated, load_curated_rows

    if not is_rulebook_catalog_request(query):
        return None
    rows = load_curated_rows()
    selected = []
    english = locale == 'en'
    lines = ['Games/tournaments with recorded rulebooks:' if english else 'เกม/รายการแข่งขันที่มีเอกสารกติกาในระบบ:']
    for game_id in COMPETITION_GAME_IDS:
        target = target_for_game_id(game_id)
        candidates = [row for row in rows if row.get('category') == 'competition_rules'
                      and not row.get('_canonical_projection')
                      and str(row.get('id', '')).startswith(target.rulebook_id + '_s')
                      and row.get('tournament') and target.rulebook_id in row.get('source_ids', [])]
        if not candidates:
            return None
        row = candidates[0]
        selected.append(row)
        tournament = str(row['tournament'])
        if english:
            localized = approved_localization(row, 'tournament')
            if localized:
                tournament = localized
            elif re.search(r'[\u0e00-\u0e7f]', tournament):
                # Reuse the source-backed game/year identity when no English
                # event-title field exists. Never pass untranslated Thai prose
                # through an English-only answer or invent an approved title.
                years = re.findall(r'\b20\d{2}\b', tournament)
                tournament = target.label + (' / ' + ', '.join(dict.fromkeys(years)) if years else '')
        lines.append(f'• {target.label}: {tournament}')
    lines.extend(['', 'These are stored rulebooks; this does not confirm current registration or an upcoming event. Name a game to see its recorded rules.' if english else 'รายการนี้อ้างอิงเอกสารที่มี ไม่ได้ยืนยันว่ากำลังเปิดรับสมัครหรือเป็นรายการที่จะจัดครั้งถัดไปครับ พิมพ์ชื่อเกมเพื่อดูกติกาจากเอกสารได้'])
    return CompetitionOverview('\n'.join(lines), [hit_from_curated(row) for row in selected], tuple(row['id'] for row in selected))
def substantive_lines(text: str) -> tuple[str, ...]:
    """Preserve complete source lines; headings and export metadata are not rules."""
    lines = []
    for raw in source_clause_lines(text):
        line = raw.strip().lstrip('*-•· ').strip()
        if len(line) < 12 or not is_rule_clause(line):
            continue
        # A tournament year alone cannot turn an event title into a rule.
        body = re.sub(r'^\d+(?:\.\d+)*[.)]?\s+', '', line)
        if not is_rule_clause(re.sub(r'\b20\d{2}\b', '', body)):
            continue
        if re.match(r'(?i)^(?:update:|english below|กฎระเบียบและรูปแบบการแข่งขัน)', line):
            continue
        # A number inside a game name (CS2/Tekken 8) is not a rule quantity.
        if re.search(r'\b(?:tournament|championship|division)\s*$', line, re.I) and not re.search(
            r'\b(?:must|shall|may|cannot|allowed|permitted|prohibited|required|not)\b', line, re.I
        ):
            continue
        if line not in lines:
            lines.append(line)
    return tuple(lines)


def build_competition_overview(query: str, locale: str, *, recent_history=None) -> CompetitionOverview | None:
    # Import lazily: retrieval itself uses competition target resolution.
    from app.pipeline.retrieval import hit_from_curated, load_curated_rows

    resolution = resolve_competition_targets(query)
    if resolution.status != 'exact':
        return None
    target = resolution.targets[0]
    more = is_more_rule_request(query)
    def comparison_text(text):
        import unicodedata
        return re.sub(r"\s+", "", unicodedata.normalize("NFC", text).casefold())
    seen_answers = []
    if more and isinstance(recent_history, list):
        for item in recent_history[-10:]:
            if not isinstance(item, dict) or item.get('role') != 'assistant' or item.get('route_category') != 'competition_rules':
                continue
            if item.get('contextEligible') is False or item.get('context_eligible') is False:
                continue
            previous = resolve_competition_targets(str(item.get('resolved_text') or ''))
            if previous.status == 'exact' and previous.targets[0].game_id == target.game_id:
                # History only excludes already displayed clauses. It is not
                # a source of facts and cannot add a new policy or target.
                seen_answers.append(comparison_text(str(item.get('text') or '')))
    rows = [
        row for row in load_curated_rows()
        if row.get('category') == 'competition_rules'
        and not row.get('_canonical_projection')
        and str(row.get('id', '')).startswith(target.rulebook_id + '_s')
        and target.rulebook_id in row.get('source_ids', [])
    ]
    # Bilingual documents may include a second set of English source sections
    # after the Thai rulebook. Use one primary set for both locales, translating
    # it through the existing localization registry for English. Parallel source
    # versions are not new rules when the user asks for additional clauses.
    primary_rows = [row for row in rows if any(re.search(r'[\u0e00-\u0e7f]', line)
                    for line in substantive_lines(str(row.get('text') or '')))]
    if primary_rows:
        rows = primary_rows
    clauses = {}
    primary_pause_clauses = {}
    excluded_count = 0
    for row in rows:
        # Alternating violation/penalty cells are not independent prose rules.
        # The dedicated table renderer keeps their relationship intact.
        if 'การละเมิด\nบทลงโทษ\n' in str(row.get('text') or ''):
            continue
        text = approved_localization(row, 'text') if locale == 'en' else str(row.get('text', ''))
        if text:
            lines = substantive_lines(text)
            if locale != 'en' and primary_rows:
                lines = tuple(line for line in lines if re.search(r'[\u0e00-\u0e7f]', line))
            identities = {comparison_text(str(value)) for value in (
                row.get('section_title'), row.get('tournament'),
                approved_localization(row, 'section_title') if locale == 'en' else '',
                approved_localization(row, 'tournament') if locale == 'en' else '',
            ) if value}
            # Some source sections consist of a complete numbered rule in
            # their title field. Retain a title that contains an actual rule;
            # remove only heading labels without substantive policy evidence.
            lines = tuple(line for line in lines if comparison_text(line) not in identities
                          or is_rule_clause(re.sub(r'^\d+(?:\.\d+)*[.)]?\s+', '', line)))
            section_title = str(row.get('section_title') or '')
            if requested_pause_kind(section_title):
                # Chunks can contain a second heading after the pause rules.
                # Bind the primary pause label only to clauses before that
                # heading; remaining bug/rollback rules may appear as extras.
                scoped = []
                raw_lines = source_clause_lines(text)
                # A one-line source section may itself be the complete rule.
                # Do not drop its first line merely because it has a title.
                first_is_heading = bool(raw_lines and comparison_text(raw_lines[0]) in identities
                                        and not is_rule_clause(re.sub(r'^\d+(?:\.\d+)*[.)]?\s+', '', raw_lines[0])))
                for line in raw_lines[1:] if first_is_heading else raw_lines:
                    if not is_rule_clause(line):
                        if scoped:
                            break
                        continue
                    scoped.append(line)
                primary_pause_clauses[str(row['id'])] = substantive_lines('\n'.join(scoped))
            if more:
                previous_count = len(lines)
                lines = tuple(line for line in lines if not any(comparison_text(line) in answer for answer in seen_answers))
                excluded_count += previous_count - len(lines)
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
                return tuple(line for line in clauses[row['id']] if line in primary_pause_clauses.get(row['id'], clauses[row['id']]))
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
    if more:
        # Include remaining source sections that do not map to a broad facet.
        for row in rows:
            if len(selected) >= 8:
                break
            if row['id'] in clauses and row['id'] not in seen:
                selected.append(row)
                selected_facets[row['id']] = 'other'
                selected_clauses[row['id']] = clauses[row['id']]
                seen.add(row['id'])
        if not selected:
            english = locale == 'en'
            answer = (f"I could not find further {target.label} clauses to show from the source sections this summary can read. This does not mean the rulebook contains no other rules. Ask about a specific topic for details."
                      if english else f"ยังไม่พบข้อกติกา {target.label} เพิ่มเติมจากส่วนเอกสารที่สรุปนี้อ่านได้ครับ ไม่ได้หมายความว่าเอกสารไม่มีกฎอื่น หากต้องการรายละเอียด ระบุหัวข้อ เช่น บทลงโทษ อุปกรณ์ หรือการหยุดเกมได้ครับ")
            hits = [hit_from_curated(rows[0])] if rows else []
            return CompetitionOverview(answer, hits, (), len(seen_answers), excluded_count, True)
    elif len(selected) < 3:
        return None
    english = locale == 'en'
    tournament = str(selected[0].get('tournament', ''))
    if english:
        localized_tournament = approved_localization(selected[0], 'tournament')
        years = re.findall(r'\b20\d{2}\b', tournament)
        tournament = localized_tournament or (target.label + (' / ' + years[0] if years else ''))
    title = f'Selected {target.label} competition rules from the recorded rulebook:' if english else f'สรุปกติกา {target.label} บางประเด็นจากเอกสารที่มี:'
    if more:
        title = f'Additional {target.label} competition rules from the recorded rulebook:' if english else f'กติกา {target.label} เพิ่มเติมจากเอกสารที่มี:'
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
    return CompetitionOverview('\n'.join(lines), [hit_from_curated(row) for row in used], tuple(row['id'] for row in used), len(seen_answers), excluded_count)
