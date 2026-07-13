# Strict Ground Truth Audit

Created: 2026-07-02T22:09:23
Results: `reports\pipeline_ground_truth_results_gt360_after_router_strictfix_20260702.jsonl`
Ground truth: `C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl`
Audit JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\strict_ground_truth_audit_gt360_after_router_strictfix_20260702.jsonl`

## Summary

- Total: 360
- pass: 324
- minor: 25
- major: 11

## By Category

| Category | pass | minor | major |
|---|---:|---:|---:|
| about_us | 5 | 0 | 0 |
| contact | 10 | 0 | 0 |
| equipment | 9 | 0 | 1 |
| events_news | 5 | 0 | 0 |
| games | 25 | 0 | 1 |
| knowledge | 7 | 0 | 0 |
| no_answer | 22 | 0 | 3 |
| overview | 4 | 0 | 1 |
| penalty | 10 | 0 | 1 |
| reservation | 70 | 21 | 3 |
| rules | 22 | 0 | 1 |
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

### v2_028 - major

- Category: `reservation`
- Expected route: `reservation`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: morning session time?
- Direct answer:

```text
รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*
```
- Issues:
  - route ผิด: ควรเป็น `reservation` แต่ได้ `schedule`
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

### v2_035 - major

- Category: `reservation`
- Expected route: `reservation`
- Actual route: `schedule`
- Mode: `pipeline:schedule_fast_path`
- Auto verdict: `PASS`
- Question: afternoon session time?
- Direct answer:

```text
รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์
```
- Issues:
  - route ผิด: ควรเป็น `reservation` แต่ได้ `schedule`
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

### v2_192 - major

- Category: `reservation`
- Expected route: `reservation`
- Actual route: `reservation`
- Mode: `pipeline:category_rule_fast_path`
- Auto verdict: `PASS`
- Question: ถ้า check-in ไม่ทันจะโดนอะไร
- Direct answer:

```text
ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```
- Issues:
  - source ไม่ตรงแบบ strict: ไม่พบ ['Reservation'] ใน retrieved/source ids

### v2_223 - major

- Category: `equipment`
- Expected route: `equipment`
- Actual route: `games`
- Mode: `pipeline:equipment_fast_path`
- Auto verdict: `PASS`
- Question: เก้าอี้เกมมิ่งมีไหมใน PC zone
- Direct answer:

```text
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```
- Issues:
  - route ผิด: ควรเป็น `equipment` แต่ได้ `games`

### v2_252 - major

- Category: `penalty`
- Expected route: `penalty`
- Actual route: `knowledge`
- Mode: `pipeline:penalty_fast_path`
- Auto verdict: `PASS`
- Question: ศูนย์เก็บประวัติคนทำผิดไหม
- Direct answer:

```text
หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```
- Issues:
  - route ผิด: ควรเป็น `penalty` แต่ได้ `knowledge`

### v2_254 - major

- Category: `overview`
- Expected route: `overview`
- Actual route: `knowledge`
- Mode: `pipeline:overview_fast_path`
- Auto verdict: `PASS`
- Question: PSU Esports Studio Phuket คืออะไร
- Direct answer:

```text
PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/home
```
- Issues:
  - route ผิด: ควรเป็น `overview` แต่ได้ `knowledge`

### v2_282 - major

- Category: `no_answer`
- Expected route: `no_answer`
- Actual route: `general`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: เอาแมวเข้าได้ไหม
- Direct answer:

```text
คำตอบ: พื้นที่การแข่งขันและกฎระเบียบ
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `no_answer` แต่ได้ `general`
  - ไม่พบ expected keyword ในคำตอบรวม: ['ไม่พบข้อมูล']

### v2_283 - major

- Category: `no_answer`
- Expected route: `no_answer`
- Actual route: `service_fee`
- Mode: `pipeline:category_rule_fast_path`
- Auto verdict: `PASS`
- Question: สมัครสมาชิกรายปีราคาเท่าไหร่
- Direct answer:

```text
ยังไม่พบข้อมูลเรื่องค่าสมัครสมาชิกศูนย์รายปีในฐานข้อมูลที่มี ข้อมูลราคาที่มีตอนนี้เป็นค่าบริการตามประเภทอุปกรณ์และกลุ่มผู้ใช้ เช่น PSU Student and Staff, PSU Alumni and General Student และ General Adult
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```
- Issues:
  - route ผิด: ควรเป็น `no_answer` แต่ได้ `service_fee`

### v2_296 - major

- Category: `no_answer`
- Expected route: `no_answer`
- Actual route: `games`
- Mode: `pipeline:rag_direct_curated`
- Auto verdict: `FAIL`
- Question: มีบริการถ่ายรูปโปรไฟล์เกมเมอร์ไหม
- Direct answer:

```text
Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ โดยปรากฏในรายการบริการ Cockpit #1 (1 Person) 60 min ของระบบจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `no_answer` แต่ได้ `games`
  - ไม่พบ expected keyword ในคำตอบรวม: ['ไม่พบข้อมูล']

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

### v2_309 - major

- Category: `rules`
- Expected route: `rules`
- Actual route: `penalty`
- Mode: `pipeline:mixed_rules_fast`
- Auto verdict: `PASS`
- Question: ถ้ากินข้าวเสียงดังแล้วทำจอยพัง จะเกี่ยวกับกฎไหนบ้าง
- Direct answer:

```text
เกี่ยวกับกฎอาหารและเสียงดัง: อาหาร/เครื่องดื่มทำได้เฉพาะพื้นที่ที่กำหนด, กรุณางดส่งเสียงดัง และหากทำอุปกรณ์เสียหายต้องรับผิดชอบค่าปรับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```
- Issues:
  - route ผิด: ควรเป็น `rules` แต่ได้ `penalty`

### v2_354 - minor

- Category: `reservation`
- Expected route: `schedule`
- Actual route: `schedule`
- Mode: `pipeline:calendar_schedule_fast_path`
- Auto verdict: `PASS`
- Question: เปิดปิด วันจัน กีโมงอะ ถ้าจะไปวันนี้ต้องรู้ว่าไง
- Direct answer:

```text
วันนี้ 02/07/2026 (วันพฤหัสบดี): วันพฤหัสบดีเปิดให้เล่น 09:00-12:00 และ 13:00-16:00
วันที่อ้างอิงของระบบ: วันนี้คือ 02/07/2026 (วันพฤหัสบดี) ตามเวลาไทย
```
- Issues:
  - expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: ['Maintenance']

### v2_357 - major

- Category: `games`
- Expected route: `games`
- Actual route: `schedule`
- Mode: `pipeline:calendar_schedule_fast_path`
- Auto verdict: `FAIL`
- Question: คอมมีวาโลไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง
- Direct answer:

```text
วันนี้ 02/07/2026 (วันพฤหัสบดี): วันพฤหัสบดีเปิดให้เล่น 09:00-12:00 และ 13:00-16:00
วันที่อ้างอิงของระบบ: วันนี้คือ 02/07/2026 (วันพฤหัสบดี) ตามเวลาไทย
```
- Issues:
  - auto evaluator เดิมให้ FAIL
  - route ผิด: ควรเป็น `games` แต่ได้ `schedule`
  - ไม่พบ expected keyword ในคำตอบรวม: ['VALORANT']

