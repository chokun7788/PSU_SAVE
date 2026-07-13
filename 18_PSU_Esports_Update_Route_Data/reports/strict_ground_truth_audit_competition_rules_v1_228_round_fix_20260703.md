# Strict Ground Truth Audit

Created: 2026-07-03T01:49:59
Results: `reports\pipeline_ground_truth_results_competition_rules_v1_228_round_fix_20260703.jsonl`
Ground truth: `data\ground_truth\ground_truth_competition_rules_v1_228.jsonl`
Audit JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\strict_ground_truth_audit_competition_rules_v1_228_round_fix_20260703.jsonl`

## Summary

- Total: 228
- pass: 223
- minor: 0
- major: 5

## By Category

| Category | pass | minor | major |
|---|---:|---:|---:|
| competition_rules | 223 | 0 | 5 |

## Items To Review

### competition_v1_009 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: CS2 แข่งแบบทีม 5 คนใช่ไหม
- Direct answer:

```text
คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - ไม่พบ expected keyword ในคำตอบรวม: ['ผู้เล่น 5 คน']

### competition_v1_011 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: CS2 ถ้าถามเรื่องจำนวนคนในทีมตอบว่าอะไร
- Direct answer:

```text
คำตอบ: CS2 Technical Pause ต่างจาก Tactical Timeout คือ Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - ไม่พบ expected keyword ในคำตอบรวม: ['ผู้เล่น 5 คน']

### competition_v1_046 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: CS2 technical กับ tactical timeout ต่างกันยังไงในกติกา
- Direct answer:

```text
คำตอบ: CS2 Technical Pause ต่างจาก Tactical Timeout คือ Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - คำถามถามส่วนต่าง แต่คำตอบหลักไม่ได้ขึ้นต้นด้วยส่วนต่าง

### competition_v1_188 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: PSU Esports Tekken 8 แข่งแบบ offline หรือเปล่า
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'FT2', '60 วินาที']

### competition_v1_222 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: Tekken 8 pause แล้วแพ้ 1 Round ใช่ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - ไม่พบ expected keyword ในคำตอบรวม: ['ไม่อนุญาต', 'Pause', 'แพ้ 1 Round']

