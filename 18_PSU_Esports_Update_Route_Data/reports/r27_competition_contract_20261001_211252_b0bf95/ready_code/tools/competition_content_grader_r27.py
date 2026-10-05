"""Literal atomic-source grading separate from legacy grades and Gold.

This proves source presence. Proposition completeness uses separate frozen
contracts; a matching fragment alone is never labelled semantic correctness.
"""
from __future__ import annotations
import argparse
import json
import re
from collections import Counter
from pathlib import Path

def atomic_clauses(text: str) -> list[str]:
    # Independent evaluator implementation: no runtime selection/render imports.
    lines = re.split(r'\n|\s+\*\s+|\s+(?=\d+(?:\.\d+)+\.?\s*[^\W\d_])', text)
    result = []
    for line in lines:
        line = re.sub(r'^(?:\d+(?:\.\d+)+[.)]?|\d+[.)])\s*', '', line.strip().lstrip('*-•· '))
        if len(line) < 10 or re.match(r'(?i)^(?:update:|english below|competition rules(?: and| for|$)|กฎระเบียบ|กติกาการแข่งขัน)', line):
            continue
        if re.search(r'\d|ต้อง|ห้าม|อนุญาต|ปรับแพ้|ตัดสิทธิ์|เท่านั้น|\b(?:must|may|shall|used|uses?|not|only|allowed|prohibited|permitted|winner|warning|rollback|loss|forfeit|disqualified)\b', line, re.I):
            result.append(line)
    return list(dict.fromkeys(result))

def normalized(text: str) -> str:
    return re.sub(r'\s+', ' ', text.casefold()).strip()

def literal_source_matches(answer: str, source_texts: dict[str, str]) -> list[dict[str, str]]:
    body = normalized(answer.split('แหล่งข้อมูล:')[0].split('Source:')[0])
    return [{'source_id': source_id, 'complete_clause': clause} for source_id, text in source_texts.items() for clause in atomic_clauses(text) if normalized(clause) in body]

def rescore(rows: list[dict], source: dict[str, dict], translate) -> tuple[list[dict], dict]:
    records = []
    for row in rows:
        texts = {origin: ((translate(source[origin], 'text') or '') if row['locale'] == 'en' else source[origin]['text']) for raw in row.get('source_ids', []) if (origin := raw.removeprefix('canonical::')) in source}
        matches = literal_source_matches(row['answer'], texts)
        failures = list(row['failures'])
        # Only replace the defective legacy presence check. Route, status,
        # game/facet evidence, timeout and validation remain hard failures.
        if matches and 'answer_without_substantive_source_content' in failures:
            failures.remove('answer_without_substantive_source_content')
        records.append({'id': row['id'], 'legacy_passed': row['passed'], 'legacy_failures': row['failures'], 'atomic_source_presence': bool(matches), 'complete_clause_matches': matches, 'source_grade_passed': not failures, 'remaining_failures': failures, 'completeness_grade': 'not_assessed_by_presence_grader'})
    summary = {'total': len(records), 'legacy_passed': sum(r['legacy_passed'] for r in records), 'source_grade_passed': sum(r['source_grade_passed'] for r in records), 'presence_false_failures_resolved': sum(not r['legacy_passed'] and r['source_grade_passed'] for r in records), 'remaining_failures': dict(Counter(f for r in records for f in r['remaining_failures'])), 'scope': 'literal complete-clause presence plus retained legacy gates; completeness evaluated only by separate proposition fixture; not organizer confirmation'}
    return records, summary

if __name__ == '__main__':
    import sys
    root = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(root))
    from app.knowledge.localization import approved_localization
    parser = argparse.ArgumentParser(); parser.add_argument('--input', type=Path, required=True); parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rows = [json.loads(x) for x in args.input.read_text(encoding='utf-8').splitlines() if x.strip()]
    source = {r['id']: r for r in (json.loads(x) for x in (root/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines())}
    records, summary = rescore(rows, source, approved_localization)
    with args.output.open('x', encoding='utf-8') as f: json.dump({'summary': summary, 'records': records}, f, ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False))
