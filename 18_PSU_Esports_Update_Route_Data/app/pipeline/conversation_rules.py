"""Detailed rulebook pages with source-versioned, acknowledged coverage.

The existing competition target/year/facet guards own interpretation. This
adapter only renders requested full sections and tracks what was displayed.
"""
from __future__ import annotations
import hashlib
import json
import re
from app.knowledge.localization import approved_localization
from app.pipeline.rulebook_source_fragments import fragment_translation, is_recorded_fragment
from app.pipeline.competition_targets import resolve_competition_targets
from app.pipeline.competition_conversation_signals import is_more_rule_request
from app.pipeline.competition_presentation import is_rule_clause
from app.pipeline.schemas import EntityBundle, PipelineRoute, PipelineTrace, ValidationResult


def wants_full_rules(query):
    return bool(re.search(r'ทั้งหมด|ทุก(?:ข้อ|หัวข้อ|ส่วน)|รายละเอียด(?:ครบ|ทั้งหมด)?|\b(?:all|full|complete|detailed)\b|\b(?:every|each)\s+(?:(?:single|documented)\s+)?(?:section|clause|rule|part|heading)s?\b', query, re.I))


def rulebook_manifest(target, rows=None):
    from app.pipeline.retrieval import load_curated_rows
    rows = load_curated_rows() if rows is None else rows
    candidates = [r for r in rows if r.get('category') == 'competition_rules'
                  and not r.get('_canonical_projection') and target.rulebook_id in r.get('source_ids', [])
                  and str(r.get('id','')).startswith(target.rulebook_id+'_s')]
    # Map names, headings and split table cells are real source sections.
    # Language and sentence classifiers cannot decide their completeness.
    meaningful = []
    for row in candidates:
        text = str(row.get('text','')).strip()
        if not text or re.match(r'(?i)^(?:update:|english below|กฎระเบียบและรูปแบบการแข่งขัน|รายการ\s+PSU)', text):
            continue
        meaningful.append(row)
    # Hash both source content and locale overlays. A changed translation must
    # not reuse a cursor based on a different displayed document.
    release = hashlib.sha256(json.dumps([(r['id'], r.get('text'), approved_localization(r,'text') or fragment_translation(r)) for r in meaningful],
                                         ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:16]
    return meaningful, release


def build_full_rule_answer(query, locale, *, recent_history=None):
    resolution = resolve_competition_targets(query)
    if resolution.status != 'exact':
        return None
    target = resolution.targets[0]
    history = recent_history if isinstance(recent_history,list) else []
    previous = []
    for item in history[-16:]:
        if isinstance(item,dict) and item.get('role') == 'assistant' and item.get('route_category') == 'competition_rules':
            coverage = item.get('rule_coverage')
            if isinstance(coverage,dict) and coverage.get('game_id') == target.game_id and coverage.get('detail_level') == 'full_sections':
                previous.append((item,coverage))
    more = is_more_rule_request(query)
    if not wants_full_rules(query) and not (more and previous):
        return None
    # Reuse edition guard. It must run before reading any default rulebook.
    from app.pipeline.competition_source_gaps import _recorded_year_guard
    if _recorded_year_guard(query,locale,target.rulebook_id) is not None:
        return None
    from app.pipeline.retrieval import hit_from_curated
    rows, release = rulebook_manifest(target)
    expected = [r['id'] for r in rows]
    seen = set()
    changed = bool(more and previous and previous[-1][1].get('source_release') != release)
    uncertain = False
    if more and not changed:
        for item, coverage in previous:
            if coverage.get('source_release') != release:
                continue
            if item.get('delivery_status') == 'client_acknowledged':
                seen.update(k for k in coverage.get('covered_ids',coverage.get('returned_ids',[])) if k in expected)
            else:
                uncertain = True
    units = {}
    locale_missing = []
    for row in rows:
        if row['id'] in seen:
            continue
        original = str(row.get('text',''))
        text = (approved_localization(row,'text') or fragment_translation(row) or (original if not re.search(r'[\u0e00-\u0e7f]',original) else None)) if locale == 'en' else original
        if not text or (locale == 'en' and re.search(r'[\u0e00-\u0e7f]',text)):
            locale_missing.append(row['id']); continue
        section = re.sub(r'_c\d+$','',row['id'])
        # The importer split the final penalty cell into a following section.
        # Preserve the source order and keep the cell with its table page.
        if original.strip() == 'แบนถาวร' and units:
            prior_key = next(reversed(units))
            if 'การละเมิด\nบทลงโทษ\n' in str(units[prior_key][0][0].get('text','')):
                section = prior_key
        units.setdefault(section,[]).append((row,text))
    selected = []; length = 0
    for group in units.values():
        size = sum(len(text) for _,text in group)
        if selected and (length+size > 12000 or len(selected)+len(group)>8):
            break
        selected.extend(group); length += size
    returned = [row['id'] for row,_ in selected]
    remaining = [k for k in expected if k not in seen and k not in returned and k not in locale_missing]
    covered = list(dict.fromkeys([*(k for k in expected if k in seen),*returned]))
    english = locale == 'en'
    lines = [(f'{target.label}: detailed sections from the recorded rulebook ({len(covered)}/{len(expected)} sections covered).' if english else
              f'กติกา {target.label}: รายละเอียดจากเอกสารที่บันทึกไว้ (แสดงแล้ว {len(covered)}/{len(expected)} ส่วน)')]
    if changed:
        lines.append('The source or translation changed. Coverage has restarted from the updated document.' if english else 'เอกสารหรือคำแปลเปลี่ยนไป จึงเริ่มแสดงรายละเอียดจากฉบับที่อัปเดตใหม่ครับ')
    elif uncertain:
        lines.append('Receipt of an earlier page was not confirmed; this page may repeat it rather than skip unseen rules.' if english else 'ยังไม่ยืนยันว่าได้รับหน้าก่อนครบ จึงอาจแสดงส่วนเดิมซ้ำเพื่อไม่ข้ามข้อกติกาครับ')
    previous_section = None
    for row,text in selected:
        # Keep complete source section text, including adjacent penalty cells.
        # No summarization model removes exceptions or reconstructs policy.
        section = re.sub(r'_c\d+$','',row['id'])
        if section == previous_section:
            heading = approved_localization(row,'section_title') if english else str(row.get('section_title',''))
            body = text.splitlines()
            if body and body[0].strip() == heading.strip():
                text = '\n'.join(body[1:])
            lines.append(text)
        else:
            lines.extend(['',text])
        previous_section = section
    if locale_missing:
        lines.append((f'{len(locale_missing)} source sections lack a verified English rendering: '+', '.join(locale_missing)) if english else 'บางส่วนยังแสดงไม่ได้จากแหล่งข้อมูลที่ตรวจ')
    if remaining:
        lines.append(f'\n{len(remaining)} sections remain. Type “continue” to see the next page.' if english else f'\nยังเหลือ {len(remaining)} ส่วน พิมพ์ “ต่อ” เพื่อดูหน้าถัดไปครับ')
    elif not locale_missing:
        lines.append('All readable recorded sections have been covered; this does not confirm rules for a new event.' if english else 'แสดงครบส่วนที่อ่านได้ของเอกสารที่บันทึกไว้แล้ว ไม่ได้ยืนยันกติกาของรายการใหม่ครับ')
    if target.game_id == 'tekken8':
        lines.append('The source has conflicting pause conditions; the organizer must confirm their application.' if english else 'เอกสารมีเงื่อนไขการหยุดเกมที่ขัดกัน ต้องให้ผู้จัดยืนยันการใช้เงื่อนไขครับ')
    source_gap_ids = [r['id'] for r in rows if is_recorded_fragment(r)]
    if source_gap_ids:
        lines.append('The recorded RoV source is incomplete at clauses 6.1.5 / 6.1.5.1. The fragment translation is prepared by the agent, not organizer approval; no missing penalty ending is inferred.' if english else 'ต้นฉบับ RoV ข้อ 6.1.5 / 6.1.5.1 มีข้อความกำกวมและถูกตัดท้าย ยังต้องให้ผู้จัดยืนยันข้อความและบทลงโทษส่วนที่ขาดครับ')
    if rows:
        lines.append(('Source: ' if english else 'แหล่งข้อมูล: ')+str(rows[0].get('source_url','')))
    outcome = 'answered_partial' if remaining or locale_missing or source_gap_ids else 'answered_complete' if expected else 'source_missing'
    coverage = {'game_id':target.game_id, 'rulebook_id':target.rulebook_id,'source_release':release,'detail_level':'full_sections',
                'expected_ids':expected,'returned_ids':returned,'covered_ids':covered,'remaining_ids':remaining,
                'missing_ids':locale_missing,'locale_gap_ids':locale_missing,'outcome':outcome,
                'source_gap_ids':source_gap_ids, 'known_source_fragment_gaps':bool(source_gap_ids), 'source_policy_complete':False if source_gap_ids else None, 'fragment_translation_basis':'agent_translation_readable_incomplete_source' if source_gap_ids and english else None,
                'source_changed':changed,'delivery_uncertain':uncertain,'owner_confirmed':False}
    route = PipelineRoute('competition_rules','competition_rules_full_sections',.98,'list','medium','source sections rendered in full with acknowledged coverage')
    hits = [hit_from_curated(row) for row,_ in selected] or ([hit_from_curated(rows[0])] if rows else [])
    return {'answer':'\n'.join(lines),'hits':hits,
            'mode':'pipeline:competition_rule_full_sections_source','route':route,'entities':EntityBundle(),
            'validation':ValidationResult(True, warnings=tuple((['english_localization_incomplete'] if locale_missing else [])+(['rulebook_source_incomplete'] if source_gap_ids else []))),
            'trace':[PipelineTrace('competition_full_coverage',outcome,1.0,'summary does not count as detailed coverage',coverage),
                     PipelineTrace('conversation_contract',outcome,1.0,'readable source coverage is separate from owner approval',coverage)]}
