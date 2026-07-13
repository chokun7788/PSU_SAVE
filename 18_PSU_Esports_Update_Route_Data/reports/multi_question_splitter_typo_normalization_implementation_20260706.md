# Multi-question Splitter and Typo Normalization Implementation

วันที่: 2026-07-06

## สรุปสั้น

ทำจริงแล้ว 2 ส่วน:

1. เพิ่ม typo normalization แบบจำกัดขอบเขต
2. เพิ่ม multi-question splitter สำหรับคำถามหลายเรื่องในข้อความเดียว

ยังไม่ได้ deploy และยังไม่ได้ sync ไปโฟลเดอร์ deploy ตามคำสั่งล่าสุดของผู้ใช้

## ไฟล์ที่แก้

```text
app/core/normalization.py
app/pipeline/engine.py
```

## 1. Typo normalization

เพิ่ม replacement ใน `normalize_text()` เพื่อแก้ typo ที่พบบ่อยและปลอดภัยต่อ intent:

```text
แข่งมเกม -> แข่งเกม
รายการแข่งมเกม -> รายการแข่งเกม
จัทนร์ -> จันทร์
จันทรื -> จันทร์
เพลห้า -> เพลย์ห้า
วีอา -> วีอาร์
คอกพิต -> คอกพิท
ค็อกพิต -> ค็อกพิท
```

ผลที่ต้องการ:

- ลด route หลุดจากคำสะกดผิดเล็ก ๆ
- ไม่ใช้ fuzzy กว้างกับข้อมูลสำคัญ เช่นราคา/กติกา/วันหยุด

## 2. Multi-question splitter

เพิ่ม logic ใน `AnswerQualityPipeline.answer()`:

- ถ้าคำถามเป็นคำถามเดียว ใช้ pipeline เดิมทั้งหมด
- ถ้าเป็นหลายคำถามที่มีสัญญาณชัด จะแยกเป็นไม่เกิน 3 ข้อ
- แต่ละข้อถูกส่งเข้า pipeline เดิมทีละข้อ
- รวมคำตอบกลับเป็นข้อ ๆ ด้วย mode:

```text
pipeline:multi_question_splitter
```

ตัวอย่างที่รองรับ:

```text
วันนี้เปิดไหม แล้ว VR ราคาเท่าไหร่
มีอุปกรณ์อะไรให้เล่นบ้าง และ VR มีเกมอะไรบ้าง
สอนจองได้ไหม แล้วเช็คอินล่วงหน้าได้กี่นาที
Minecraft เล่นได้ไหม และตอนนี้มีเกมแข่งอะไรบ้าง
```

ตัวอย่างที่ตั้งใจไม่แยก:

```text
Beat Saber คือเกมอะไรแล้วเล่นยังไง
VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่
```

เหตุผล:

- `Beat Saber คือเกมอะไรแล้วเล่นยังไง` เป็นคำถามเกมเดียวที่ fast path เดิมตอบทั้งคืออะไรและวิธีเล่นได้
- `VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่` เป็น comparison intent เดียว ไม่ควรถูกแยก

## Ad-hoc tests

Questions file:

```text
reports/ad_hoc_questions_multi_splitter_typo_normalization_20260706.txt
```

Latest ad-hoc report:

```text
reports/ad_hoc_pipeline_results_multi_splitter_typo_normalization_fix2_20260706.md
reports/ad_hoc_pipeline_results_multi_splitter_typo_normalization_fix2_20260706.jsonl
```

ผล ad-hoc:

```text
questions=8
routes:
- games/competition_game_list: 1
- games/game_availability_lookup: 1
- multi_question/multi_question_split: 4
- schedule/schedule_query: 1
- service_fee/service_fee_query: 1
```

ตัวอย่างผลที่สำคัญ:

- `วันนี้เปิดไหม แล้ว VR ราคาเท่าไหร่` แยกตอบ schedule + service fee
- `Minecraft เล่นได้ไหม และตอนนี้มีเกมแข่งอะไรบ้าง` แยกตอบ unknown game no-answer + competition game list
- `ตอนนี้รายการแข่งมเกมอะไรบ้าง` ยังตอบ 4 เกมจาก competition game list
- `Beat Saber คือเกมอะไรแล้วเล่นยังไง` ไม่ถูกแยกมั่ว และยังตอบ game detail ได้

## Regression

Compile:

```text
py_compile OK
```

Validate:

```text
VALIDATION OK
- rule files: 8
- rules: 77
- curated rows: 324
- service fee sanity: OK
```

GT360:

```text
Total: 360
PASS: 360
FAIL: 0
Pass rate: 100.00%
```

Report:

```text
reports/pipeline_ground_truth_report_multi_splitter_typo_normalization_gt360_20260706.md
reports/pipeline_ground_truth_results_multi_splitter_typo_normalization_gt360_20260706.jsonl
```

Competition challenger v2:

```text
Total: 369
PASS: 369
FAIL: 0
Pass rate: 100.00%
```

Report:

```text
reports/pipeline_ground_truth_report_multi_splitter_typo_normalization_comp_v2_20260706.md
reports/pipeline_ground_truth_results_multi_splitter_typo_normalization_comp_v2_20260706.jsonl
```

## ข้อจำกัดที่ยังเหลือ

- Splitter ตั้งใจจำกัดไม่เกิน 3 คำถามต่อ input
- ถ้าคำถามที่สองสั้นมากและไม่มี domain signal เช่น `แล้วอันนั้นล่ะ` ยังไม่รองรับ เพราะต้องใช้ session memory
- ยังไม่ได้ทำ memory ต่อบทสนทนา
- ยังไม่ได้ทำ booking action จริง
- ยังไม่ได้ cleanup source metadata บาง fast path
- ยังไม่ได้ deploy หรือ sync ไป deploy folder

## ขั้นต่อไปที่แนะนำ

1. ทดสอบผ่าน local API หรือหน้าเว็บใน dev server
2. ถ้าผู้ใช้พอใจ ให้ sync ไป deploy folder
3. ผู้ใช้กด deploy เองตามที่แจ้งไว้
4. หลัง deploy ให้ test production API อย่างน้อย:

```text
วันนี้เปิดไหม แล้ว VR ราคาเท่าไหร่
Minecraft เล่นได้ไหม และตอนนี้มีเกมแข่งอะไรบ้าง
ตอนนี้รายการแข่งมเกมอะไรบ้าง
```

