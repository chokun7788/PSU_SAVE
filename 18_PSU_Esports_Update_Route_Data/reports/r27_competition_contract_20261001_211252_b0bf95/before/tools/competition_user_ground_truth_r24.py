"""Source-preserving bilingual competition cases and end-to-end guard evaluation.

Generated variants are synthetic assistant-reviewed candidates, not owner Gold.
The runtime never reads this corpus. Original Gold and rulebooks are immutable.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, sys, time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.knowledge.localization import approved_localization
from app.pipeline.engine import answer_question_pipeline_debug
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from tools.run_competition_rules_rag_ground_truth import actual_status, hit_identifiers

GOLD = ROOT / 'data/eval/competition_user_r24_2000_20261001.jsonl'
SOURCE = ROOT / 'data/eval/competition_rules_rag_ground_truth_v1.jsonl'
CHUNKS = ROOT / 'data/competition_rules/competition_rule_chunks.jsonl'
GAMES = {
    'cs2': ('cs2', 'competition_rules_cs2_psu_phuket_2026'),
    'rov': ('rov', 'competition_rules_rov_blueket_2025_men'),
    'tekken8': ('tekken 8', 'competition_rules_tekken8_psu_esports'),
    'valorant': ('วาโล', 'competition_rules_valorant_psu_phuket_2026'),
}

def read(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]

def normalized(text):
    return re.sub(r'\s+', ' ', text.casefold().replace('เเ', 'แ')).strip()

def variant(q, locale, index):
    # Change task vocabulary only, preserving game names, dates and numbers.
    if index == 0:
        return q, 'clean'
    replacements = (
        [('การแข่งขัน', 'การเเข่งขัน'), ('กติกา', 'กติกกา'), ('แข่งขัน', 'แข่่งขัน'), ('อะไรบ้าง', 'อะไรมั่ง'), ('กฎ', 'กฏ'), ('การแข่ง', 'การแข่')]
        if locale == 'th' else
        [('rules', 'ruls'), ('competition', 'compettition'), ('tournament', 'tournamet'), ('rules', 'ruules'), ('competition', 'competiton'), ('rules', 'rulse')]
    )
    old, new = replacements[(index - 1) % len(replacements)]
    edited = q.replace(old, new, 1)
    prefix = ('ช่วยดูหน่อย ', 'อยากทราบว่า ', 'สอบถามหน่อยครับ ', 'ขอข้อมูล ', 'ช่วยอธิบาย ', '') if locale == 'th' else ('Please check: ', 'Could you explain: ', 'I would like to know: ', 'Please tell me: ', 'Quick question: ', '')
    suffix = (' ครับ', ' หน่อย', ' ได้ไหม', '', ' คะ', ' นะครับ') if locale == 'th' else (' please.', '', ' Thanks.', ' please', '.', '?')
    return prefix[(index - 1) % 6] + edited + suffix[((index - 1) // 6) % 6], ('task_typo' if edited != q else 'natural_wrapper')

def build():
    originals = read(SOURCE)
    rows = []
    seen = set()
    for locale in ('th', 'en'):
        for game, (label, rulebook) in GAMES.items():
            seeds = [dict(row, parent_gold_id=row['id'], oracle='existing_source_evidence') for row in originals if row['locale'] == locale and row.get('expected_game_id') == game]
            title = label if locale == 'th' else ('VALORANT' if game == 'valorant' else label)
            broad = [f'กฏตอนเเข่ง {title} มีอะไรมั่ง', f'กติกา {title} มีอะไรบ้าง', f'สรุปกฎการแข่งขัน {title} ทั้งหมด', f'กฎตอนแข่ง {title} มีไรบ้าง'] if locale == 'th' else [f'What are the {title} tournament rules?', f'What rules apply to the {title} competition?', f'Summarize the {title} competition rules.', f'{title} rules overview please.']
            seeds = [dict(id=f'overview-{locale}-{game}-{n}', question=q, locale=locale, case_type='broad_substantive_overview', expected_game_id=game, expected_answer_status='answer_available', expected_route_categories=['competition_rules'], expected_rulebook_ids=[rulebook], expected_facet=None, rag_required=True, oracle='multiple_substantive_source_clauses') for n,q in enumerate(broad)] + seeds
            added = 0
            for index in range(36):
                for seed in seeds:
                    q, style = variant(seed['question'], locale, index)
                    key=(locale, q)
                    if key in seen:
                        continue
                    seen.add(key)
                    rows.append(dict(seed, id=f'R24-{locale.upper()}-{game}-{added+1:03d}', question=q, clean_question=seed['question'], mutation=style, review_status='assistant_source_reviewed_candidate', latency_ceiling_sec=20, generation_index=index))
                    added += 1
                    if added == 240:
                        break
                if added == 240:
                    break
            assert added == 240, (locale, game, added)
        safe = [row for row in originals if row['locale']==locale and row.get('expected_game_id') not in GAMES]
        added=0
        for index in range(36):
            for seed in safe:
                q,style=variant(seed['question'],locale,index)
                if (locale,q) in seen:
                    continue
                seen.add((locale,q))
                rows.append(dict(seed,id=f'R24-{locale.upper()}-SAFE-{added+1:03d}',clean_question=seed['question'],question=q,mutation=style,oracle='existing_control_outcome',review_status='assistant_source_reviewed_candidate'))
                added+=1
                if added==40:break
            if added==40:break
        assert added==40, (locale,added)
    assert len(rows)==2000
    with GOLD.open('x',encoding='utf-8') as handle:
        for row in rows:handle.write(json.dumps(row,ensure_ascii=False)+'\n')
    manifest={'total':len(rows),'locales':dict(Counter(row['locale'] for row in rows)), 'mutations':dict(Counter(row['mutation'] for row in rows)), 'source_gold_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(), 'source_chunks_sha256':hashlib.sha256(CHUNKS.read_bytes()).hexdigest(), 'review':'synthetic assistant-reviewed candidates; no owner approval; original Gold preserved', 'original_seed_questions':len({row['clean_question'] for row in rows}), 'runtime_training_use':False}
    GOLD.with_suffix('.manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(manifest,ensure_ascii=False),flush=True)

def substantive_overlap(answer, texts, locale):
    # Content check independent of the runtime overview selector. A citation,
    # game title or heading alone cannot satisfy this check.
    answer=normalized(answer.split('แหล่งข้อมูล:')[0].split('Source:')[0])
    clauses=[]
    for text in texts:
        for line in text.splitlines():
            line=normalized(line.strip().lstrip('*-•· '))
            if len(line)<32 or not re.search(r'ต้อง|ห้าม|อนุญาต|ปรับแพ้|ผู้เล่น|\d|must|shall|allowed|prohibited|players|winner',line):continue
            if re.match(r'update:|english below|รายการ |กฎระเบียบ|กติกาการแข่งขัน',line):continue
            if locale=='en':
                tokens=re.findall(r'[a-z0-9]+',line)
                fragments=[' '.join(tokens[i:i+7]) for i in range(max(0,len(tokens)-6))]
                body=' '.join(re.findall(r'[a-z0-9]+',answer))
            else:
                body=re.sub(r'\s+','',answer)
                source=re.sub(r'\s+','',line)
                fragments=[source[i:i+24] for i in range(max(0,len(source)-23))]
            if any(fragment in body for fragment in fragments):clauses.append(line)
    return len(set(clauses))

def evaluate(report, run, limit, only_failed=None):
    os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce'
    os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
    os.environ['PSU_BILINGUAL_EN_ENABLED']='1'
    os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
    guard=RuntimeInputQualityGuard.from_environment()
    source_rows={row['id']:row for row in read(CHUNKS)}
    source_texts={}
    for locale in ('th','en'):
        source_texts[locale]={id:(approved_localization(row,'text') if locale=='en' else row['text']) or '' for id,row in source_rows.items()}
    cases=read(GOLD)
    if only_failed:
        ids={row['id'] for row in read(only_failed) if not row['passed']}
        cases=[case for case in cases if case['id'] in ids]
    if limit:cases=cases[:limit]
    stats=Counter(); by_group={}; started=time.perf_counter()
    with (report/f'{run}_details.jsonl').open('x',encoding='utf-8') as output:
        for n,case in enumerate(cases,1):
            q=case['question']; failures=[]; quality=guard.inspect(q)
            if quality.should_short_circuit:
                answer=quality.message; mode=quality.mode; category='input_quality'; ids=set(); refs=set(); elapsed=0; trace=[]; valid=True
                failures.append('false_keyboard_rejection')
            else:
                result=answer_question_pipeline_debug(q,locale=case['locale'],experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
                answer=result.answer or ''; mode=result.mode; category=result.route.category; elapsed=result.elapsed; trace=[{'stage':t.stage,'decision':t.decision,'detail':t.detail,'metadata':t.metadata} for t in result.trace]; valid=result.validation.ok
                ids,refs=hit_identifiers(result.hits)
            status=actual_status(answer,mode)
            expected=case['expected_answer_status']
            expected_status='answer' if expected=='answer_available' else 'clarification' if expected=='clarification_required' else 'no_answer'
            if status!=expected_status:failures.append('outcome_mismatch')
            if category not in case['expected_route_categories']:failures.append('route_mismatch')
            substantive=0
            if expected_status=='answer':
                rulebooks=case.get('expected_rulebook_ids',[])
                if not all(any(rulebook in ref for ref in refs) for rulebook in rulebooks):failures.append('missing_target_evidence')
                if any('competition_rules_' in ref and not any(rulebook in ref for rulebook in rulebooks) for ref in refs):failures.append('foreign_game_evidence')
                allowed=set(case.get('allowed_evidence_rule_ids',[])) | set(case.get('allowed_evidence_fact_ids',[]))
                if allowed and not ids.intersection(allowed):failures.append('wrong_facet_evidence')
                selected_ids={id.removeprefix('canonical::') for id in ids if id.removeprefix('canonical::') in source_rows}
                texts=[source_texts[case['locale']][id] for id in selected_ids]
                substantive=substantive_overlap(answer,texts,case['locale'])
                if case['case_type']=='broad_substantive_overview':
                    if len(selected_ids)<3 or substantive<3:failures.append('overview_without_multiple_rule_clauses')
                elif case.get('expected_facet')!='rulebook_identity' and not substantive:
                    # Some short exact facts are legitimately under 32 chars.
                    short=[normalized(line.strip().lstrip('*-•· ')) for text in texts for line in text.splitlines() if 8<=len(line.strip())<120 and (any(ch.isdigit() for ch in line) or re.search(r'\b(?:uses?|must|may|prohibited|allowed)\b',line,re.I))]
                    if not any(text in normalized(answer) for text in short):failures.append('answer_without_substantive_source_content')
            if not valid:failures.append('validation_failure')
            if elapsed>20:failures.append('latency_failure')
            record={'id':case['id'],'locale':case['locale'],'game':case.get('expected_game_id'),'case_type':case['case_type'],'mutation':case['mutation'],'question':q,'expected_facet':case.get('expected_facet'),'expected_status':expected_status,'actual_status':status,'mode':mode,'category':category,'answer':answer,'elapsed_sec':round(elapsed,4),'input_quality':quality.to_log_dict(),'source_ids':sorted(ids),'substantive_source_lines':substantive,'failures':failures,'passed':not failures,'trace':trace}
            output.write(json.dumps(record,ensure_ascii=False)+'\n'); output.flush()
            stats['passed' if not failures else 'failed']+=1
            for failure in failures:stats[failure]+=1
            group=case['locale']+'/'+str(case.get('expected_game_id') or 'safe')
            by_group.setdefault(group,Counter())['passed' if not failures else 'failed']+=1
            if n%100==0:print(json.dumps({'completed':n,'total':len(cases),'elapsed_sec':round(time.perf_counter()-started,1),'stats':dict(stats)},ensure_ascii=False),flush=True)
    summary={'run':run,'total':len(cases),'stats':dict(stats),'by_group':by_group,'wall_sec':round(time.perf_counter()-started,2),'guard':'enforce','llm':False,'semantic_retrieval':False,'oracle_note':'source evidence plus literal substantive overlap; no independent owner confirmation; overlap is not full semantic grading'}
    with (report/f'{run}_summary.json').open('x',encoding='utf-8') as handle:json.dump(summary,handle,ensure_ascii=False,indent=2)
    print(json.dumps(summary,ensure_ascii=False),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--build',action='store_true'); parser.add_argument('--report',type=Path); parser.add_argument('--run',default='full_A'); parser.add_argument('--limit',type=int,default=0); parser.add_argument('--only-failed',type=Path)
    args=parser.parse_args()
    if args.build:build()
    if args.report:evaluate(args.report,args.run,args.limit,args.only_failed)
