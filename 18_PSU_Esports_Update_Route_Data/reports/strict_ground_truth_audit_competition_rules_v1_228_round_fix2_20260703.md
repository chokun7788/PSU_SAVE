# Strict Ground Truth Audit

Created: 2026-07-03T01:51:53
Results: `reports\pipeline_ground_truth_results_competition_rules_v1_228_round_fix2_20260703.jsonl`
Ground truth: `data\ground_truth\ground_truth_competition_rules_v1_228.jsonl`
Audit JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\strict_ground_truth_audit_competition_rules_v1_228_round_fix2_20260703.jsonl`

## Summary

- Total: 228
- pass: 227
- minor: 0
- major: 1

## By Category

| Category | pass | minor | major |
|---|---:|---:|---:|
| competition_rules | 227 | 0 | 1 |

## Items To Review

### competition_v1_046 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: CS2 technical กับ tactical timeout ต่างกันยังไงในกติกา
- Direct answer:

```text
คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - คำถามถามส่วนต่าง แต่คำตอบหลักไม่ได้ขึ้นต้นด้วยส่วนต่าง

