# Strict Ground Truth Audit

Created: 2026-07-02T22:04:12
Results: `reports\pipeline_ground_truth_results_competition_rules_v1_228_smoke.jsonl`
Ground truth: `data\ground_truth\ground_truth_competition_rules_v1_228.jsonl`
Audit JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\strict_ground_truth_audit_competition_rules_v1_228_strict_20260702.jsonl`

## Summary

- Total: 228
- pass: 0
- minor: 0
- major: 228

## By Category

| Category | pass | minor | major |
|---|---:|---:|---:|
| competition_rules | 0 | 0 | 228 |

## Items To Review

### competition_v1_001 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 แข่งทีมละกี่คน
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_002 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Counter-Strike 2 ทีมละกี่คนตามกติกา
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_003 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา CS2 ต้องมีผู้เล่นกี่คนต่อทีม
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_004 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 สมาชิกทีมต้องมีกี่คน
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_005 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 ลงแข่งพร้อมกันกี่คน
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_006 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 roster ผู้เล่นหลักมีกี่คน
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_007 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: รายการ PSU Phuket CS2 2026 ทีมละกี่คน
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_008 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 ต้องส่งผู้เล่นกี่คนในทีม
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_009 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: CS2 แข่งแบบทีม 5 คนใช่ไหม
- Direct answer:

```text
คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['ผู้เล่น 5 คน']

### competition_v1_010 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Counter Strike 2 ในรายการนี้ผู้เล่นต่อทีมกี่คน
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_011 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: CS2 ถ้าถามเรื่องจำนวนคนในทีมตอบว่าอะไร
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['ผู้เล่น 5 คน']

### competition_v1_012 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 กติกาองค์ประกอบทีมกำหนดไว้กี่คน
- Direct answer:

```text
คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_013 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 ใช้ map อะไรบ้าง
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_014 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 map pool มีอะไรบ้าง
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_015 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 แผนที่ที่ใช้แข่งมีอะไรบ้าง
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_016 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา CS2 ระบุแผนที่อะไรบ้าง
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_017 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: PSU Phuket CS2 2026 ใช้แผนที่ไหน
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_018 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 มี Ancient กับ Anubis ใน map pool ไหม
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_019 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: CS2 รายการนี้ใช้ Dust 2 หรือ Train ไหม
- Direct answer:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Ancient', 'Anubis', 'Dust 2', 'Train']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_020 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: ขอรายชื่อ map ที่ใช้แข่ง CS2
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_021 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Counter-Strike 2 map pool ในกติกาคืออะไร
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_022 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 แข่งบนแผนที่อะไรได้บ้าง
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_023 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 ban map จาก pool ไหน
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_024 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 แผนที่ทั้งหมดตามกติกามีอะไร
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_025 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 แข่งรูปแบบอะไร
- Direct answer:

```text
คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_026 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: CS2 เป็น Single Elimination ไหม
- Direct answer:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Single Elimination', 'BO3']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_027 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: CS2 รอบรองกับรอบชิงเป็น BO อะไร
- Direct answer:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Single Elimination', 'BO3']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_028 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: กติกา CS2 format การแข่งขันเป็นยังไง
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Single Elimination', 'BO3']

### competition_v1_029 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: PSU Phuket CS2 2026 ใช้ระบบแข่งแบบไหน
- Direct answer:

```text
คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_030 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 รอบชิงใช้ BO3 ใช่ไหม
- Direct answer:

```text
คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_031 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 รอบรองชนะเลิศแข่งกี่เกม
- Direct answer:

```text
คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_032 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Counter-Strike 2 tournament format คืออะไร
- Direct answer:

```text
คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_033 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: CS2 แข่งแพ้คัดออกหรือเปล่า
- Direct answer:

```text
คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Single Elimination', 'BO3']

### competition_v1_034 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 รูปแบบทัวร์นาเมนต์ในเอกสารคืออะไร
- Direct answer:

```text
คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_035 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: CS2 รอบสำคัญเป็น Best of 3 ไหม
- Direct answer:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Single Elimination', 'BO3']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_036 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 กติกาบอกว่า single elimination หรือไม่
- Direct answer:

```text
คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3)
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_037 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 technical pause ได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_038 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 tactical timeout ได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_039 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 pause ได้กี่ครั้งตามกติกา
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_040 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 ขอหยุดเกม technical ได้กี่ครั้งและกี่นาที
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_041 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา CS2 tactical timeout ครั้งละกี่วินาที
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_042 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 Technical Pause รวมได้ไม่เกินกี่นาที
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_043 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 เวลานอก tactical timeout ได้ทีมละกี่ครั้ง
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_044 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `service_fee`
- Mode: `pipeline:category_rule_fast_path`
- Auto verdict: `FAIL`
- Question: CS2 ถ้าเครื่องมีปัญหาขอ pause ได้เท่าไหร่
- Direct answer:

```text
หากพบปัญหาการใช้งาน พฤติกรรมที่ไม่เหมาะสม หรือข้อกังวลใด ๆ ควรแจ้งเจ้าหน้าที่ทันที
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:category_rule_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Technical Pause', '2 ครั้ง', '10 นาที', 'Tactical Timeout', '4 ครั้ง', '30 วินาที']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_045 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Counter-Strike 2 pause policy เป็นยังไง
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_046 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: CS2 technical กับ tactical timeout ต่างกันยังไงในกติกา
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - คำถามถามส่วนต่าง แต่คำตอบหลักไม่ได้ขึ้นต้นด้วยส่วนต่าง

### competition_v1_047 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: CS2 ขอ Tactical Timeout 4 ครั้งใช่ไหม
- Direct answer:

```text
คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_048 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `FAIL`
- Question: CS2 หยุดเกมได้กี่ครั้งและใช้เวลากี่วินาที
- Direct answer:

```text
เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `schedule`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:schedule_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Technical Pause', '2 ครั้ง', '10 นาที', 'Tactical Timeout', '4 ครั้ง', '30 วินาที']
  - คำถามกติกาการแข่งขันหลุดไป route `schedule` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_049 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT แข่งทีมละกี่คน
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_050 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโลทีมละกี่คนตามกติกา
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_051 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT สมาชิกทีมกี่คน
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_052 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา VALORANT ต้องมีผู้เล่นกี่คน
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_053 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: PSU Phuket VALORANT 2026 แข่งทีมละกี่คน
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_054 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT ลงแข่งพร้อมกันกี่คน
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_055 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโลผู้เล่นตัวจริงกี่คน
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_056 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: VALORANT ทีม 5 คนใช่ไหม
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['5 คน']

### competition_v1_057 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: VALORANT roster ตัวจริงกี่คน
- Direct answer:

```text
PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['5 คน']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_058 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `service_fee`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: กฎแข่งวาโลจำนวนผู้เล่นต่อทีมคือเท่าไหร่
- Direct answer:

```text
ค่าบริการ PlayStation 5 ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 50 บาท, บุคคลทั่วไป 150 บาท
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['VALORANT', '5 คน']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_059 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT ในรายการนี้ใช้ทีมละกี่คน
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_060 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโลแข่งแบบกี่คนต่อทีม
- Direct answer:

```text
คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_061 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT แผนที่ที่ใช้แข่งมีอะไรบ้าง
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_062 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT map pool มีอะไรบ้าง
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_063 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโลใช้ map อะไรบ้าง
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_064 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา VALORANT ระบุแผนที่อะไรบ้าง
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_065 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: PSU Phuket VALORANT 2026 ใช้ map ไหน
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_066 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT มี Abyss กับ Ascent ใน map pool ไหม
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_067 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: วาโลแข่งบน Sunset ได้ไหม
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Abyss', 'Ascent', 'Sunset']

### competition_v1_068 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: ขอรายชื่อแผนที่แข่ง VALORANT
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_069 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT map pool ทั้งหมดมีอะไร
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_070 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโล ban map จากแผนที่ชุดไหน
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_071 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT แข่งแผนที่อะไรได้บ้าง
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_072 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎวาโลเรื่อง map pool คืออะไร
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_073 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT Tactical Timeout ขอได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_074 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโล timeout ได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_075 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT เวลานอกได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_076 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT tactical timeout ครั้งละกี่วินาที
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_077 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `service_fee`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: กติกา VALORANT timeout ต่อแผนที่ได้เท่าไหร่
- Direct answer:

```text
บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Tactical Timeout', '2 ครั้ง', '60 วินาที', 'Overtime']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_078 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT เข้า Overtime ได้ timeout เพิ่มไหม
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_079 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโล Tactical Timeout ได้ทีมละกี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_080 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT ขอเวลานอก 60 วินาทีใช่ไหม
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_081 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT timeout ในรอบปกติได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_082 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: PSU Phuket VALORANT 2026 tactical timeout rule คืออะไร
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_083 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโลเวลานอก tactical ต่อ map ได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_084 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT ถามเรื่อง tactical timeout ให้ตอบยังไง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_085 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT emergency pause ได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Emergency/Technical Pause ได้ทีมละ 1 ครั้งต่อแผนที่ โดยเวลาหยุดรวมสูงสุด 10 นาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_086 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT technical pause รวมได้กี่นาที
- Direct answer:

```text
คำตอบ: VALORANT ขอ Emergency/Technical Pause ได้ทีมละ 1 ครั้งต่อแผนที่ โดยเวลาหยุดรวมสูงสุด 10 นาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_087 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT pause ฉุกเฉินได้ไหม
- Direct answer:

```text
คำตอบ: VALORANT ขอ Emergency/Technical Pause ได้ทีมละ 1 ครั้งต่อแผนที่ โดยเวลาหยุดรวมสูงสุด 10 นาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_088 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `service_fee`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: วาโลหลุดเกมขอ emergency pause ได้เท่าไหร่
- Direct answer:

```text
บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Emergency', '1 ครั้ง', '10 นาที']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_089 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา VALORANT หยุดฉุกเฉินได้ทีมละกี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Emergency/Technical Pause ได้ทีมละ 1 ครั้งต่อแผนที่ โดยเวลาหยุดรวมสูงสุด 10 นาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_090 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT technical pause สูงสุดกี่นาที
- Direct answer:

```text
คำตอบ: VALORANT ขอ Emergency/Technical Pause ได้ทีมละ 1 ครั้งต่อแผนที่ โดยเวลาหยุดรวมสูงสุด 10 นาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_091 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT Emergency Pause ต่อแผนที่ได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Emergency/Technical Pause ได้ทีมละ 1 ครั้งต่อแผนที่ โดยเวลาหยุดรวมสูงสุด 10 นาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_092 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโลหยุดเกมฉุกเฉินรวมกี่นาที
- Direct answer:

```text
คำตอบ: VALORANT ขอ Emergency/Technical Pause ได้ทีมละ 1 ครั้งต่อแผนที่ โดยเวลาหยุดรวมสูงสุด 10 นาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_093 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: VALORANT ถ้า hardware มีปัญหาขอ pause ยังไง
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Emergency', '10 นาที']

### competition_v1_094 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: VALORANT emergency pause policy คืออะไร
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Emergency', '10 นาที']

### competition_v1_095 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: วาโล technical pause 10 นาทีใช่ไหม
- Direct answer:

```text
คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Emergency', '10 นาที']

### competition_v1_096 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT pause ฉุกเฉินตามกฎตอบว่าอะไร
- Direct answer:

```text
คำตอบ: VALORANT ขอ Emergency/Technical Pause ได้ทีมละ 1 ครั้งต่อแผนที่ โดยเวลาหยุดรวมสูงสุด 10 นาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_097 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT agent ใหม่ใช้ได้ไหม
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_098 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT map ใหม่ใช้ได้ไหม
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_099 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโลเอเจนท์ใหม่ใช้แข่งได้ไหม
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_100 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา VALORANT agent ใหม่ต้องรอกี่สัปดาห์
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_101 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT แผนที่ใหม่ต้องรอกี่สัปดาห์ก่อนแข่ง
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_102 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT ใช้เอเจนท์ที่เพิ่งออกใหม่ได้ทันทีไหม
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_103 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโล map ใหม่ใช้แข่งได้เลยหรือเปล่า
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_104 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT new agent restriction คืออะไร
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_105 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: VALORANT new map restriction ในกติกาคืออะไร
- Direct answer:

```text
คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Agent', '2 สัปดาห์', '4 สัปดาห์']

### competition_v1_106 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: วาโล agent ใหม่รอ 2 สัปดาห์ใช่ไหม
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_107 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: VALORANT map ใหม่รอ 4 สัปดาห์ไหม
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_108 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎวาโลเรื่อง content ใหม่เป็นยังไง
- Direct answer:

```text
คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids

### competition_v1_109 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: สมาชิกในทีม ROV ต้องมีกี่คน
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_110 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ทีมละกี่คน
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_111 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: ROV แข่งกี่คน
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_112 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: สมาชิกในทีม RoV กี่คนตามกติกา
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_113 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา RoV บอกว่าลงแข่งฝ่ายละกี่คน
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_114 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: RoV เป็น 5v5 ใช่ไหม
- Direct answer:

```text
คำตอบ: 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน
  - ไม่พบ expected keyword ในคำตอบรวม: ['ฝ่ายละ 5 คน', 'ยังไม่พบจำนวนสมาชิกทีม']

### competition_v1_115 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Blueket Games RoV ทีมละกี่คน
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_116 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV roster รวมมีกี่คนในไฟล์กติกา
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_117 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: ROV มีตัวสำรองกี่คนในเอกสาร
- Direct answer:

```text
คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน
  - ไม่พบ expected keyword ในคำตอบรวม: ['ฝ่ายละ 5 คน', 'ยังไม่พบจำนวนสมาชิกทีม']

### competition_v1_118 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ถามจำนวนสมาชิกทีมควรตอบยังไง
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_119 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Arena of Valor แข่งโหมดกี่ต่อกี่
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_120 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ยืนยันได้ไหมว่าลงแข่งฝ่ายละ 5 คน
- Direct answer:

```text
คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_121 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ใช้สกินได้ไหม
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_122 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: ROV ใช้ skin ได้ไหม
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_123 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ต้องใช้สกินอะไร
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_124 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา RoV อนุญาตให้ใช้สกินไหม
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_125 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Blueket Games RoV ใช้ Default Skin ใช่ไหม
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_126 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ห้ามใช้สกินอื่นไหม
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_127 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Arena of Valor แข่งต้องใช้ skin แบบไหน
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_128 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ใช้สกินพิเศษได้หรือเปล่า
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_129 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎ RoV เรื่องสกินคืออะไร
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_130 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: ROV default skin เท่านั้นไหม
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_131 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ถ้าใช้สกินนอก default ได้ไหม
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_132 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ในรายการนี้สกินต้องเป็นอะไร
- Direct answer:

```text
คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_133 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ถ้าเริ่มแข่งช้าเกิน 15 นาทีโดนอะไร
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_134 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `PASS`
- Question: RoV มาสายเกิน 15 นาทีเป็นอะไร
- Direct answer:

```text
คำตอบ: 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที
```
- Issues:
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน

### competition_v1_135 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `PASS`
- Question: ROV late start 15 นาที
- Direct answer:

```text
คำตอบ: 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที
```
- Issues:
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน

### competition_v1_136 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา RoV เริ่มแข่งล่าช้าเกิน 15 นาทีลงโทษยังไง
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_137 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Blueket Games RoV ถ้ามาสายโดนปรับแพ้ไหม
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_138 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ถ้าทีมทำให้เริ่มช้าจะโดนอะไร
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_139 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV เริ่มช้ากี่นาทีถึงปรับแพ้
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_140 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Arena of Valor ล่าช้า 15 นาทีตามกฎเป็นยังไง
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_141 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV แข่งช้าเกินเวลาที่กำหนดถูกปรับแพ้ไหม
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_142 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `PASS`
- Question: ROV ถ้าเริ่ม match ไม่ทัน 15 นาทีตอบว่าอะไร
- Direct answer:

```text
คำตอบ: 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที
```
- Issues:
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน

### competition_v1_143 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎ RoV เรื่องมาสายคืออะไร
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_144 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV late start rule ในเอกสารคืออะไร
- Direct answer:

```text
คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_145 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV pause ได้กี่ครั้ง
- Direct answer:

```text
คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_146 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `FAIL`
- Question: RoV หลุดเกมหยุดได้ไหม
- Direct answer:

```text
เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `schedule`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:schedule_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['5 ครั้ง', '1 นาที']
  - คำถามกติกาการแข่งขันหลุดไป route `schedule` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_147 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: RoV disconnect ทำยังไง
- Direct answer:

```text
คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน
  - ไม่พบ expected keyword ในคำตอบรวม: ['5 ครั้ง', '1 นาที']

### competition_v1_148 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา RoV หยุดเกมได้ทีมละกี่ครั้ง
- Direct answer:

```text
คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_149 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV pause ครั้งละกี่นาที
- Direct answer:

```text
คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_150 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `service_fee`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: Blueket Games RoV ถ้าเกมหลุดขอหยุดได้เท่าไหร่
- Direct answer:

```text
คำถามที่ใช้คำว่า ศิษย์เก่า PSU, alumni, General Student, นักศึกษาทั่วไป, นักเรียนทั่วไป, นักศึกษาต่างมหาวิทยาลัย, นักเรียนต่างมหาวิทยาลัย, นักศึกษาต่างมหาลัย, นักเรียนต่างมหาลัย, เด็กต่างมหาลัย, ต่างมหาลัย, นักศึกษาจากมหาวิทยาลัยอื่น, นักศึกษาจากต่างสถาบัน ให้ตีความเป็นกลุ่ม PSU Alumni and General Student ในตาราง Service Fee 2026
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['5 ครั้ง', '1 นาที']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_151 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV แต่ละทีมมีสิทธิ์หยุดเกมกี่ครั้ง
- Direct answer:

```text
คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_152 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Arena of Valor pause ได้สูงสุดกี่ครั้ง
- Direct answer:

```text
คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_153 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV หยุดเกมได้ 5 ครั้งใช่ไหม
- Direct answer:

```text
คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_154 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: ROV pause 1 นาทีต่อครั้งใช่หรือเปล่า
- Direct answer:

```text
คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_155 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: RoV disconnect แล้วกลับมาเล่นต่อเมื่อไหร่
- Direct answer:

```text
คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน
  - ไม่พบ expected keyword ในคำตอบรวม: ['5 ครั้ง', '1 นาที']

### competition_v1_156 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎ RoV เรื่อง pause/disconnect คืออะไร
- Direct answer:

```text
คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_157 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `PASS`
- Question: RoV ขอเริ่มใหม่ได้ไหม
- Direct answer:

```text
คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่
```
- Issues:
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['First Blood', '2 นาที']

### competition_v1_158 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ก่อน first blood remake ได้ไหม
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_159 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV แข่งใหม่ได้ตอนไหน
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_160 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา RoV rematch ทำได้เมื่อไหร่
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_161 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ขอแข่งใหม่ก่อน 2 นาทีได้ไหม
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_162 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Blueket Games RoV ถ้าเกิด First Blood แล้ว remake ได้ไหม
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_163 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Arena of Valor เริ่มใหม่ได้ก่อน First Blood ใช่ไหม
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_164 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ถ้าเกิน 2 นาทีแล้วขอแข่งใหม่ได้ไหม
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_165 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: RoV ต้องให้ฝ่ายตรงข้ามยินยอมเมื่อไหร่
- Direct answer:

```text
คำตอบ: 6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน
  - ไม่พบ expected keyword ในคำตอบรวม: ['First Blood', '2 นาที']

### competition_v1_166 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: ROV rematch rule ตามเอกสารคืออะไร
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_167 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV remake ก่อน First Blood และก่อน 2 นาทีใช่ไหม
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_168 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎ RoV เรื่องขอแข่งใหม่ตอบยังไง
- Direct answer:

```text
คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_169 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ใช้อุปกรณ์อะไรแข่ง
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_170 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ใช้ iPad แข่งได้ไหม
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_171 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: RoV ใช้ tablet ได้ไหม
- Direct answer:

```text
คำตอบ: 4. ระเบียบและกติกาการแข่งขัน
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน
  - ไม่พบ expected keyword ในคำตอบรวม: ['โทรศัพท์มือถือ', 'ไม่อนุญาต', 'Tablet', 'iPad']

### competition_v1_172 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV แข่งด้วยเครื่องอะไร
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_173 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา RoV ต้องใช้มือถือไหม
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_174 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: Blueket Games RoV อนุญาต iPad หรือเปล่า
- Direct answer:

```text
คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `general`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน
  - ไม่พบ expected keyword ในคำตอบรวม: ['โทรศัพท์มือถือ', 'ไม่อนุญาต', 'Tablet', 'iPad']

### competition_v1_175 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Arena of Valor แข่งด้วยโทรศัพท์มือถือเท่านั้นไหม
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_176 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ใช้ Tablet ในการแข่งขันได้หรือไม่
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_177 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: ROV device rule คืออะไร
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_178 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV อุปกรณ์ที่ใช้แข่งกำหนดยังไง
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_179 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: RoV ถ้าจะใช้ iPad ต้องได้ไหมตามกฎ
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_180 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎ RoV เรื่องอุปกรณ์แข่งคืออะไร
- Direct answer:

```text
คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids

### competition_v1_181 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 เล่นแบบไหน
- Direct answer:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'FT2', '60 วินาที']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_182 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 รูปแบบการแข่งขัน
- Direct answer:

```text
คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_183 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 แข่งกี่ต่อกี่
- Direct answer:

```text
คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_184 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: กติกา Tekken 8 ใช้ format อะไร
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'FT2', '60 วินาที']

### competition_v1_185 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 เป็น 1v1 ใช่ไหม
- Direct answer:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'FT2', '60 วินาที']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_186 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 FT2 คือรูปแบบแข่งใช่ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_187 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 แข่งบน PS5 และเวลา 60 วินาทีไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_188 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: PSU Esports Tekken 8 แข่งแบบ offline หรือเปล่า
- Direct answer:

```text
คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_189 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 รอบหนึ่งตั้งเวลากี่วินาที
- Direct answer:

```text
เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `schedule`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:schedule_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'PlayStation 5', 'FT2', '60 วินาที']
  - คำถามกติกาการแข่งขันหลุดไป route `schedule` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_190 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 ใช้ Round 3 ไหม
- Direct answer:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'FT2', '60 วินาที']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_191 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 format ในเอกสารคืออะไร
- Direct answer:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'FT2', '60 วินาที']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_192 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `FAIL`
- Question: Tekken 8 กติกาการแข่งขันสรุปยังไง
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'FT2', '60 วินาที']

### competition_v1_193 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ใช้เครื่องอะไรแข่ง
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_194 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 แข่งบนอะไร
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_195 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 platform อะไร
- Direct answer:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_196 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา Tekken 8 ระบุเครื่องแข่งว่าอะไร
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_197 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ใช้ PS5 แข่งใช่ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_198 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `knowledge`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: PSU Esports Tekken 8 ใช้ PlayStation 5 หรือเปล่า
- Direct answer:

```text
อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `knowledge`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['PlayStation 5']
  - คำถามกติกาการแข่งขันหลุดไป route `knowledge` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_199 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 อุปกรณ์หลักที่ใช้แข่งคืออะไร
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_200 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 แข่งด้วยเครื่องเกมอะไร
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_201 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 platform ตามเอกสารคืออะไร
- Direct answer:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_202 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ใช้ console อะไรในการแข่ง
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_203 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 ต้องเล่นบน PlayStation 5 ไหม
- Direct answer:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_204 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎ Tekken 8 เรื่อง platform คืออะไร
- Direct answer:

```text
คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_205 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ใช้ DLC character ได้ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_206 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ใช้ตัวละคร DLC ได้ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_207 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 เลือกตัวละครอะไรได้บ้าง
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_208 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา Tekken 8 ห้าม DLC ใช่ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_209 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `games`
- Mode: `pipeline:games_fast_path`
- Auto verdict: `FAIL`
- Question: Tekken 8 ใช้ customization ได้ไหม
- Direct answer:

```text
PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['ยกเว้นตัวละคร DLC', 'Customization']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_210 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ใช้ชุดแต่งตัวละครได้หรือเปล่า
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_211 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: PSU Esports Tekken 8 ตัวละคร DLC แข่งได้ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_212 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ใช้ skin custom ได้ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_213 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 character rule คืออะไร
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_214 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 เลือกได้ทุกตัวยกเว้น DLC ใช่ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_215 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ห้าม customization ตามกฎหรือไม่
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_216 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎ Tekken 8 เรื่องตัวละครและสกินคืออะไร
- Direct answer:

```text
คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_217 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 pause ได้ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_218 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 หยุดเกมได้ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_219 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 กด pause โดนอะไร
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_220 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กติกา Tekken 8 ถ้ากด pause หลังเริ่มเกมเป็นยังไง
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_221 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ตั้งใจกดหยุดเกมโดนปรับแพ้ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_222 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 pause แล้วแพ้ 1 Round ใช่ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_223 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: PSU Esports Tekken 8 ห้าม pause หรือเปล่า
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_224 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 หยุดเกมได้เฉพาะกรณีไหน
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_225 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 ถ้าทั้งสองฝ่ายยินยอม pause ได้ไหม
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_226 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 pause penalty คืออะไร
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_227 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: Tekken 8 กด pause ระหว่างแข่งลงโทษยังไง
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

### competition_v1_228 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `competition_rules`
- Mode: `pipeline:competition_fact_card`
- Auto verdict: `PASS`
- Question: กฎ Tekken 8 เรื่อง pause ตอบว่าอะไร
- Direct answer:

```text
คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids

