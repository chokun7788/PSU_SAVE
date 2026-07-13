# Strict Ground Truth Audit

Created: 2026-07-02T22:09:23
Results: `reports\pipeline_ground_truth_results_competition_rules_v1_228_after_router_strictfix_20260702.jsonl`
Ground truth: `data\ground_truth\ground_truth_competition_rules_v1_228.jsonl`
Audit JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\strict_ground_truth_audit_competition_rules_v1_228_after_router_strictfix_20260702.jsonl`

## Summary

- Total: 228
- pass: 200
- minor: 0
- major: 28

## By Category

| Category | pass | minor | major |
|---|---:|---:|---:|
| competition_rules | 200 | 0 | 28 |

## Items To Review

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Single Elimination', 'BO3']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

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
  - ไม่พบ expected keyword ในคำตอบรวม: ['Single Elimination', 'BO3']

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Single Elimination', 'BO3']
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:category_rule_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_cs2_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Technical Pause', '2 ครั้ง', '10 นาที', 'Tactical Timeout', '4 ครั้ง', '30 วินาที']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

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
  - คำถามถามส่วนต่าง แต่คำตอบหลักไม่ได้ขึ้นต้นด้วยส่วนต่าง

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['VALORANT', '5 คน']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

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
  - ไม่พบ expected keyword ในคำตอบรวม: ['Abyss', 'Ascent', 'Sunset']

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Tactical Timeout', '2 ครั้ง', '60 วินาที', 'Overtime']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_valorant_psu_phuket_2026'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['Emergency', '1 ครั้ง', '10 นาที']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

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
  - ไม่พบ expected keyword ในคำตอบรวม: ['Emergency', '10 นาที']

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
  - ไม่พบ expected keyword ในคำตอบรวม: ['Agent', '2 สัปดาห์', '4 สัปดาห์']

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

### competition_v1_137 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `penalty`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: Blueket Games RoV ถ้ามาสายโดนปรับแพ้ไหม
- Direct answer:

```text
ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500 – 2,000 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `penalty`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['15 นาที', 'ปรับแพ้']

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `service_fee`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['5 ครั้ง', '1 นาที']
  - คำถามกติกาการแข่งขันหลุดไป route `service_fee` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_175 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `contact`
- Mode: `pipeline:category_rule_fast_path`
- Auto verdict: `FAIL`
- Question: Arena of Valor แข่งด้วยโทรศัพท์มือถือเท่านั้นไหม
- Direct answer:

```text
เบอร์ติดต่อที่ปรากฏในระบบจองคือ +66 7627 6004 และ +66 7627 6045
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `contact`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:category_rule_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_rov_blueket_2025_men'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['โทรศัพท์มือถือ', 'ไม่อนุญาต', 'Tablet', 'iPad']

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
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
  - ไม่พบ expected keyword ในคำตอบรวม: ['1v1', 'FT2', '60 วินาที']

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
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `knowledge`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['PlayStation 5']
  - คำถามกติกาการแข่งขันหลุดไป route `knowledge` ซึ่งเสี่ยงตอบคนละเรื่อง

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
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `games`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:games_fast_path`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - คำถามกติกาการแข่งขันหลุดไป route `games` ซึ่งเสี่ยงตอบคนละเรื่อง

### competition_v1_221 - major

- Category: `competition_rules`
- Expected route: `competition_rules`
- Actual route: `penalty`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: Tekken 8 ตั้งใจกดหยุดเกมโดนปรับแพ้ไหม
- Direct answer:

```text
ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100 – 500 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `competition_rules` แต่ได้ `penalty`
  - mode ผิด: ควรขึ้นต้น `pipeline:competition_fact_card` แต่ได้ `pipeline:rag_direct_curated`
  - source ไม่ตรงแบบ strict: ไม่พบ ['competition_rules_tekken8_psu_esports'] ใน retrieved/source ids
  - ไม่พบ expected keyword ในคำตอบรวม: ['ไม่อนุญาต', 'Pause', 'แพ้ 1 Round']

