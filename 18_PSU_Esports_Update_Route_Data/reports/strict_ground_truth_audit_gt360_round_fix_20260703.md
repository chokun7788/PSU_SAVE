# Strict Ground Truth Audit

Created: 2026-07-03T01:49:59
Results: `reports\pipeline_ground_truth_results_gt360_round_fix_20260703.jsonl`
Ground truth: `C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl`
Audit JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\strict_ground_truth_audit_gt360_round_fix_20260703.jsonl`

## Summary

- Total: 360
- pass: 334
- minor: 26
- major: 0

## By Category

| Category | pass | minor | major |
|---|---:|---:|---:|
| about_us | 5 | 0 | 0 |
| contact | 10 | 0 | 0 |
| equipment | 10 | 0 | 0 |
| events_news | 5 | 0 | 0 |
| games | 26 | 0 | 0 |
| knowledge | 7 | 0 | 0 |
| no_answer | 25 | 0 | 0 |
| overview | 5 | 0 | 0 |
| penalty | 11 | 0 | 0 |
| reservation | 72 | 22 | 0 |
| rules | 23 | 0 | 0 |
| service_fee | 135 | 4 | 0 |

## Items To Review

### v2_016 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: ศูนย์เปิดกีโมงปิดกี่โมง
- Direct answer:

```text
เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_017 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: เปิดปิดกี่โมงนะ
- Direct answer:

```text
เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_018 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: เวลาเปิดให้บริการคืออะไร
- Direct answer:

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_019 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: service hours คืออะไร
- Direct answer:

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_020 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: เปิดถึง 16:00 ใช่ไหม
- Direct answer:

```text
เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_021 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: เปิด 24 ชม ไหม
- Direct answer:

```text
ไม่เปิด 24 ชั่วโมง ตามข้อมูลที่มี ศูนย์ใช้ช่วงเวลา Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยต้องดูวัน Maintenance ประกอบ
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_022 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: ช่วงเช้าของตารางคือเวลาไหน
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_023 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: Morning คือกี่โมงถึงกี่โมง
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_024 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: รอบเช้า 09 ถึง 12 ใช่ไหม
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_025 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: ช่วงเช้าเปิดตั้งแต่กี่โมงถึงเที่ยงไหม
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_026 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: ตอนเช้าเปิดกี่โมง
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_027 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: รอบเช้าเริ่มตอนไหน
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_028 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: morning session time?
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_029 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: morning slot time
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_030 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: ช่วงบ่ายของตารางคือเวลาไหน
- Direct answer:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_031 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: Afternoon คือกี่โมงถึงกี่โมง
- Direct answer:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_032 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: รอบบ่าย 13 ถึง 16 ใช่ไหม
- Direct answer:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_033 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: ช่วงบ่ายเปิดกี่โมงปิดกี่โมง
- Direct answer:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_034 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: รอบบ่ายปิดกี่โมง
- Direct answer:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_035 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: afternoon session time?
- Direct answer:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_036 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: afternoon slot time
- Direct answer:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Monday', 'Friday']

### v2_039 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: maintenance weekly hardware inspection คืออะไร
- Direct answer:

```text
เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Weekly hardware inspection', 'cleaning']

### v2_158 - minor

- Category: `service_fee`
- Expected route: `service_fee`
- Actual route: `service_fee`
- Mode: `pipeline:deterministic_calculator_fast`
- Auto verdict: `PASS`
- Question: ราคาค่าบริการทั้งหมดมีอะไรบ้าง
- Direct answer:

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```
- Issues:
  - คำถามราคา แต่บรรทัดแรกยังไม่ขึ้นราคาหรือบอกไม่พบราคา

### v2_160 - minor

- Category: `service_fee`
- Expected route: `service_fee`
- Actual route: `service_fee`
- Mode: `pipeline:deterministic_calculator_fast`
- Auto verdict: `PASS`
- Question: ตารางราคา 2026 มีอะไร
- Direct answer:

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```
- Issues:
  - คำถามราคา แต่บรรทัดแรกยังไม่ขึ้นราคาหรือบอกไม่พบราคา

### v2_161 - minor

- Category: `service_fee`
- Expected route: `service_fee`
- Actual route: `service_fee`
- Mode: `pipeline:deterministic_calculator_fast`
- Auto verdict: `PASS`
- Question: ค่าเล่นแต่ละเครื่องเท่าไหร่
- Direct answer:

```text
ตาราง Service Fee 2026:
- PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
- Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท
- Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง): PSU Student and Staff 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท
- Cockpit 60 นาที (1 ชั่วโมง, 1 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท
- VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
- VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
หมายเหตุ: ใน Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```
- Issues:
  - คำถามราคา แต่บรรทัดแรกยังไม่ขึ้นราคาหรือบอกไม่พบราคา

### v2_306 - minor

- Category: `service_fee`
- Expected route: `service_fee`
- Actual route: `service_fee`
- Mode: `pipeline:deterministic_calculator_fast`
- Auto verdict: `PASS`
- Question: General Student เล่น PS5 กับ Nintendo 1-2 ราคาเท่ากันไหม
- Direct answer:

```text
เท่ากัน สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 ราคา 50 บาท
- Nintendo Switch 1-2 คน ราคา 50 บาท
```
- Issues:
  - คำถามราคา แต่บรรทัดแรกยังไม่ขึ้นราคาหรือบอกไม่พบราคา

