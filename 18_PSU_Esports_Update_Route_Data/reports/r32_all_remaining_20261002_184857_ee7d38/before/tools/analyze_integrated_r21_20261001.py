"""Immutable per-case audit linking r20 causes, candidate outcomes and sources."""
from __future__ import annotations
import argparse
import json
import sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.eval_contract_v2 import rescore_pair

def read(p): return [json.loads(l) for l in Path(p).read_text(encoding='utf-8-sig').splitlines() if l.strip()]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--inputs',type=Path,nargs=2,required=True)
    ap.add_argument('--output-dir',type=Path,required=True)
    args=ap.parse_args();out=args.output_dir
    out.mkdir(parents=True,exist_ok=False)
    current=[r for p in args.inputs for r in read(p)]
    baseline=[r for lang in ('th','en') for r in read(ROOT/f'reports/reliability_flow_20261001/paired_{lang}_r20_gate.jsonl')]
    old={r['id']:r for r in baseline};new={r['id']:r for r in current}
    if len(new)!=len(current) or not set(new)<=set(old):raise ValueError('Invalid IDs')
    overlays={r['id']:r for r in read(ROOT/'data/eval/typo_r16_contract_overlay_20260930.jsonl')}
    fixture={r['id']:r for r in read(ROOT/'data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl')}
    new_traces={}
    for lang in ('th','en'):
        trace_path=ROOT/f'reports/r21_integrated_improvement_20261001/replay_{lang}_final.jsonl'
        if trace_path.exists() and trace_path.with_suffix('.summary.json').exists():
            new_traces.update({r['id']:r['replay'] for r in read(trace_path)})
    audit=read(ROOT/'reports/r20_deep_failure_analysis_20261001/residual_audit_345.jsonl')
    traces={r['id']:r for lang in ('th','en') for r in read(ROOT/f'reports/r20_deep_failure_analysis_20261001/traces_{lang}.jsonl') if r['variant']=='noisy'}
    summary={'count':len(current),'comparison':'same frozen GT and same scorer; assistant translation review, no owner sign-off or real booking oracle'}
    for kind in ('clean','noisy'):
        summary[kind]={'baseline_pass':sum(old[r['id']][kind]['passed'] for r in current),
                       'candidate_pass':sum(r[kind]['passed'] for r in current),
                       'improved_ids':[r['id'] for r in current if not old[r['id']][kind]['passed'] and r[kind]['passed']],
                       'worsened_ids':[r['id'] for r in current if old[r['id']][kind]['passed'] and not r[kind]['passed']]}
    summary['locales']={lang:{k:sum(r[k]['passed'] for r in current if r['locale']==lang) for k in ('clean','noisy')} for lang in ('th','en')}
    summary['v2']={}
    for kind in ('clean','noisy'):
        summary['v2'][kind]={phase:sum(rescore_pair(r,overlays.get(r['id']))['v2'][kind]['passed'] for r in rows) for phase,rows in [('baseline',[old[r['id']] for r in current]),('candidate',current)]}
    summary['remaining_domains']=dict(Counter(r['domain'] for r in current if not r['noisy']['passed']))
    summary['remaining_modes']=dict(Counter(r['noisy']['mode'] for r in current if not r['noisy']['passed']))
    summary['exceptions']=sum(r[k]['mode']=='pipeline_exception' for r in current for k in ('clean','noisy'))
    summary['latency_failures']=sum(not r[k]['latency_ok'] for r in current for k in ('clean','noisy'))
    summary['clean_pass_noisy_fail']=sum(r['clean']['passed'] and not r['noisy']['passed'] for r in current)
    all_audit=[];md=['# วิเคราะห์รายข้อ: r20 failures → r21','',
        'ครอบคลุม noisy failures เดิม 345 ข้อ โดยแยก trace-confirmed cause ออกจากสมมติฐานที่ยังต้องตรวจ source เพิ่ม คำตอบ clean เป็น reference output ของระบบเดิม ไม่ใช่ human gold โดยอัตโนมัติ', '',
        'คะแนน shortcut เป็นค่าของ branch; candidate score เป็นคะแนนจัดอันดับ ไม่ใช่ความน่าจะเป็นว่าคำตอบถูก เกณฑ์ legacy/v2 และ source semantics แยกกัน', '']
    for item in audit:
        cid=item['id'];b=old[cid];n=new.get(cid);t=traces[cid]['replay'];artifact=t.get('decision_artifact') or {}
        selected=artifact.get('selected_candidate') or {}; candidates=artifact.get('candidates') or []
        outcome=item['outcome_label'];clean_pass=b['clean']['passed']
        if item.get('cause_review_status')=='case_trace_and_code_inspected':
            cause=item['cause_note'];level='trace_code_source_inspected'
        elif outcome=='localization_pending':
            cause='English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.';level='branch_reason_confirmed_primary_cause_pending'
        elif selected and ((item.get('central_selection') or {}).get('selection') or {}).get('status')=='abstain_low_score':
            cause='The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.';level='selection_reason_confirmed_primary_cause_pending'
        elif clean_pass:
            cause='Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.';level='paired_regression_primary_cause_pending'
        else:
            cause='Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.';level='mixed_baseline_failure_primary_cause_pending'
        priority='P0 wrong task/target or omitted facet' if outcome=='answer' else 'P1 task/qualifier or English evidence'
        if outcome in ('no_answer','clarification') and not clean_pass:priority='P2 source/ambiguity/label review'
        row={**item,'priority':priority,'cause_evidence_level':level,'cause_analysis':cause,
             'old_answer':t['answer'],'clean_reference_answer':b['clean']['answer'],
             'clean_reference_certified_by_legacy':clean_pass,'expected_routes':b['expected_route_categories'],
             'expected_status':b['expected_answer_status'],'frozen_content_contract':b['answer_contract'],
             'score_explanation':{'fixed_branch_confidence':t['confidence'],'selected_candidate':selected,'candidates':candidates,'rejected':artifact.get('rejected',[])},
             'branch_reasons':[{'stage':x['stage'],'decision':x.get('decision'),'detail':x.get('detail'),'confidence':x.get('confidence'),'metadata':x.get('metadata')} for x in t['trace'] if x['stage'] in {'router','bilingual_route','protected_intent','candidate_selector','candidate_execution','validation','question_frame'}],
             'candidate_result':n['noisy'] if n else None,'candidate_clean':n['clean'] if n else None,
             'improved_under_frozen_contract':bool(n and n['noisy']['passed']),
             'trace_reference':f'reports/r20_deep_failure_analysis_20261001/traces_{item["locale"]}.jsonl'}
        gold=fixture[cid]
        current_trace=new_traces.get(cid)
        branch_selection=item.get('central_selection') or {}
        selection=branch_selection.get('selection') or {}
        frame=branch_selection.get('question_frame') or {}
        counterfactual=(
            'Answer the requested task with the verified target, qualifier, numbers and source; the clean output is only a candidate reference.'
            if gold['expected_answer_status']=='answer_available' else
            'Run the live adapter for the requested date/time/resource; unavailable is distinct from verified free/booked.'
            if gold['expected_answer_status']=='live_lookup_required' else
            'Clarify the missing target or operation; preserve real-word ambiguity instead of silently rewriting it.'
            if gold['expected_answer_status']=='clarification_required' else
            'State the exact evidence gap. Do not substitute inventory, opening hours or another game rule for the requested fact.'
        )
        chain=[]
        if selection:
            top=branch_selection.get('selected') or {}
            chain.append(f"Frame operation={frame.get('operation')}; domain={frame.get('domain')}; target={frame.get('target_status')}")
            chain.append(f"Selected {top.get('capability_id')} score={top.get('score')}; reasons={top.get('reason')}")
            chain.append(f"Execution={selection.get('execution_allowed')}; selection={selection.get('status')}; margin={selection.get('margin')}; runner-up={selection.get('second')}")
        else:
            chain.append('No central candidate selection was recorded before this return. Explain the shortcut using branch reason, not an invented ranking score.')
        chain.append(f"Final validation ok={t['validation']['ok']}; errors={t['validation']['errors']}; warnings={t['validation']['warnings']}")
        row.update(expected_target=gold.get('expected_target'),source_contract=gold.get('source_contract'),
                   scenario=gold.get('metadata'),counterfactual_behavior=counterfactual,selection_chain=chain,
                   missing_positive_content_gate=not any(gold['answer_contract'].get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')),
                   changed_spans=gold['edit_actions'],current_trace=current_trace,
                   current_replay_matches_gate=bool(n and current_trace and current_trace['mode']==n['noisy']['mode'] and current_trace['answer']==n['noisy']['answer']))
        all_audit.append(row)
        md += [f'## {cid} — {item["domain"]}', '',f'- Priority: {priority}',f'- Evidence: {level}',
               f'- คำถาม: {item["question"]}',f'- Legacy expected: {b["expected_route_categories"]}; {b["expected_answer_status"]}',
               f'- ก่อนแก้: {item["mode"]}; confidence={t["confidence"]}; source IDs={item["source_ids"]}',
               f'- Top candidate: {selected.get("capability_id","ไม่มี central ranking ใน trace ของผลนี้")}; score={selected.get("score","N/A")}; reason={selected.get("reason","ใช้ branch reason ใน JSON audit")}',
               f'- สาเหตุ/ขอบเขตการยืนยัน: {cause}',
               f'- หลังแก้: {n["noisy"]["mode"] if n else "not in this subset"}; frozen pass={n["noisy"]["passed"] if n else "N/A"}', '',
               '### คำตอบก่อนแก้', '',t['answer'],'','### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)', '',b['clean']['answer'],'']
        if n:md+=['### คำตอบหลังแก้','',n['noisy']['answer'],'']
        md+=['### ทำไมระบบเลือกผลนี้ / สิ่งที่ควรเกิดแทน','']
        md += [f'- {value}' for value in chain]
        md += [f'- พฤติกรรมที่ควรได้: {counterfactual}',f'- Target จาก fixture: {gold.get("expected_target")}',
               f'- Source contract (ยังไม่ใช่ owner approval): {gold.get("source_contract")}',
               f'- Scenario: {gold.get("metadata")}',f'- Positive content gate ขาด: {row["missing_positive_content_gate"]}',
               f'- Current replay ตรง gate: {row["current_replay_matches_gate"]}','']
        if current_trace:
            selected_current=(current_trace.get('decision_artifact') or {}).get('selected_candidate')
            md += [f'- หลังแก้ selected candidate: {selected_current or "shortcut ก่อน central ranking"}',
                   f'- หลังแก้ confidence ของ branch: {current_trace["confidence"]}',
                   f'- หลังแก้ validation: {current_trace["validation"]}','']
        md+=['### เงื่อนไขเนื้อหาของ GT เดิม','', '```json',json.dumps(b['answer_contract'],ensure_ascii=False,indent=2),'```','']
    summary['old_failure_outcomes_after']={'passed':sum(r['improved_under_frozen_contract'] for r in all_audit),'still_failed_or_not_run':sum(not r['improved_under_frozen_contract'] for r in all_audit)}
    summary['current_replay_count']=len(new_traces)
    summary['current_replay_matching_gates']=sum(r['current_replay_matches_gate'] for r in all_audit)
    summary['positive_content_gates']={"present":sum(any(r['answer_contract'].get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')) for r in current),"absent":sum(not any(r['answer_contract'].get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')) for r in current)}
    (out/'analysis.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    with (out/'per_case_audit_345.jsonl').open('x',encoding='utf-8') as f:
        for r in all_audit:f.write(json.dumps(r,ensure_ascii=False)+'\n')
    (out/'per_case_analysis_345.md').write_text('\n'.join(md),encoding='utf-8')
    remaining=[r for r in current if not r['noisy']['passed'] or not r['clean']['passed']]
    with (out/'remaining_pairs.jsonl').open('x',encoding='utf-8') as f:
        for r in remaining:f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k in ('count','locales','remaining_domains','exceptions','latency_failures')},ensure_ascii=False))

if __name__=='__main__':main()
