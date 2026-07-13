# Ground Truth False-Pass Fix and Strict Audit

วันที่: 2026-07-02

## ปัญหาที่เจอ

ชุด Ground Truth 360 ข้อเคยดูเหมือนผ่านทั้งหมด แต่มีบางข้อที่คนอ่านเห็นว่าผิดหรือแปลก เช่น AI ตอบผิดราคา/ผิดหมวด แต่ตัวตรวจยังให้ผ่านได้

สาเหตุหลักคือ evaluator เดิมตรวจแบบค่อนข้างหลวม:

- ตรวจแค่ว่า expected keyword อยู่ในคำตอบรวม ไม่ได้ดูว่าบรรทัดแรกหรือคำตอบหลักตอบถูกไหม
- ตรวจ source แบบกว้าง ทำให้บางครั้งคำตอบมาจาก route ที่ไม่เหมาะสมแต่ยังผ่าน
- ไม่ได้บังคับ expected route/mode เช่น คำถามกติกาแข่งควรเข้า `competition_rules` แต่หลุดไป `games` หรือ `service_fee`
- คำตอบแบบผสม เช่น ถามเกมพร้อมถามวันนี้เปิดไหม ตัว route อาจเป็น `schedule` แต่ต้องยังตอบส่วนเกมด้วย
- no-answer บางเคส confidence ต่ำ ทำให้ระบบไหลต่อไป RAG และดึงคำตอบผิดจากข้อมูลที่คล้ายกัน

## สิ่งที่แก้ในรอบนี้

### 1. เพิ่ม strict audit

เพิ่มไฟล์:

`tools/strict_ground_truth_audit.py`

หน้าที่:

- อ่านผลลัพธ์จาก `pipeline_ground_truth_results_*.jsonl`
- เทียบกับ Ground Truth
- ตรวจซ้ำแบบเข้มกว่า evaluator เดิม
- แยกผลเป็น `pass`, `minor`, `major`
- สร้างรายงาน `.md` และ `.jsonl` ในโฟลเดอร์ `reports`

เช็คเพิ่มจาก evaluator เดิม:

- expected route กับ actual route
- expected mode prefix เช่น `pipeline:competition_fact_card`
- source จริงจาก retrieved/source ids และ source URL ที่อยู่ใน answer
- expected keyword ใน direct answer ไม่ใช่แค่ในรายละเอียดด้านล่าง
- no-answer ต้องตอบว่าไม่พบข้อมูลอย่างชัดเจน
- คำถามถามส่วนต่างควรตอบส่วนต่างก่อน
- คำถามราคา คำตอบหลักควรขึ้นราคาก่อน

### 2. ปรับ router ให้ไม่โดนคำกว้างลากผิดหมวด

ไฟล์ที่แก้:

`app/pipeline/router.py`

แก้หลักๆ:

- `facebook` เคยโดนคำว่า `book` ใน facebook ลากไปหมวด booking ตอนนี้ contact ชนะก่อน
- payment เช่น "หลังจองต้องจ่ายภายในกี่นาที" ชนะ price/service_fee
- damage/penalty เช่น "รอยขีดข่วน", "เบาะขาด" ชนะ service_fee
- เพิ่ม keyword กติกาแข่ง เช่น `single elimination`, `format`, `platform`, `round`, `tablet`, `ipad`, `customization`, `disconnect`

### 3. ปรับ retrieval ของ competition fact cards

ไฟล์ที่แก้:

`app/pipeline/retrieval.py`

เพิ่ม alias intent เช่น:

- team_size: `จำนวนคน`, `ทีม 5`, `5 คน`
- map_pool: ชื่อ map เช่น `Dust 2`, `Train`, `Ancient`, `Anubis`
- pause: `hardware`, `เครื่องมีปัญหา`, `ขอหยุด`
- format: `format`, `เล่นแบบไหน`, `วินาที`
- character/rematch: `customization`, `ฝ่ายตรงข้าม`, `ยินยอม`

### 4. ปรับ no-answer guard

ไฟล์ที่แก้:

- `app/pipeline/guard.py`
- `app/runtime/fast_answer.py`

แก้หลักๆ:

- เพิ่มคำ out-of-scope เช่น `แมว`, `ถ่ายรูปโปรไฟล์`, `สมาชิกรายปี`
- เพิ่ม confidence ของ no-answer fast answer จาก `0.55` เป็น `0.92`
- ทำให้เคสที่ควรตอบว่าไม่มีข้อมูลไม่ไหลไป RAG แล้วดึงคำตอบมั่ว

### 5. เพิ่ม mixed answer สำหรับเกม + วันที่

ไฟล์ที่แก้:

`app/runtime/fast_answer.py`

ตัวอย่าง:

คำถาม: `คอมมีวาโลไหม ถ้าจะไปวันนี้ต้องรู้ว่าไง`

ระบบควรตอบทั้ง:

- PC มี VALORANT
- วันนี้วันที่เท่าไหร่/วันอะไร
- วันนี้เปิดหรือปิดตามตาราง/วันหยุด

จึงเพิ่ม game context ลงใน calendar schedule answer

## ผลลัพธ์หลังแก้

### Ground Truth 360

ผล evaluator เดิม:

- Total: 360
- PASS: 360
- FAIL: 0

รายงาน:

`reports/pipeline_ground_truth_report_gt360_after_noanswer_mixed_20260702.md`

ผล strict audit ล่าสุด:

- Total: 360
- pass: 333
- minor: 27
- major: 0

รายงาน:

`reports/strict_ground_truth_audit_gt360_after_noanswer_mixed_audit_v2_20260702.md`

หมายเหตุ:

`minor 27` ส่วนใหญ่ไม่ใช่คำตอบผิดหนัก แต่เป็นคำตอบที่ keyword สำคัญ เช่น Monday/Friday อยู่ในรายละเอียดด้านล่าง ไม่ได้อยู่ใน direct answer จึงควรปรับ style ให้บรรทัดแรกครบขึ้น

### Competition Ground Truth 228

ผล evaluator เดิมหลังปรับ router/retrieval:

- Total: 228
- PASS: 203
- FAIL: 25

รายงาน:

`reports/pipeline_ground_truth_report_competition_rules_v1_228_after_noanswer_mixed_20260702.md`

ผล strict audit:

- Total: 228
- pass: 200
- major: 28

รายงาน:

`reports/strict_ground_truth_audit_competition_rules_v1_228_after_noanswer_mixed_20260702.md`

## สาเหตุที่ชุดกติกาแข่งยังผิด

กลุ่มปัญหาหลัก:

- บางคำถามกติกาแข่งยังหลุดไป `games`, `service_fee`, `general`, `penalty`, `schedule`
- บางคำถามเข้า `competition_rules` แล้ว แต่หยิบ fact card ผิดใบ เช่นถาม VALORANT emergency pause แต่ตอบ Tactical Timeout
- บางคำถามเป็น yes/no หรือถามส่วนต่าง แต่คำตอบ fact card ยังเป็นรูปแบบสรุปทั่วไป
- บางคำถามไม่ได้มีคำว่า "กติกา" ชัดเจน เช่น `Tekken 8 เป็น 1v1 ใช่ไหม` ทำให้ router มองเป็นเกมในศูนย์แทนการแข่งขัน

## แนวทางแก้ต่อ

1. เพิ่ม field ใน Ground Truth ให้ละเอียดขึ้น

- `expected_route_category`
- `expected_mode_prefix`
- `required_direct_keywords`
- `must_not_contain`
- `answer_focus`

2. แยก evaluator เป็น 2 ชั้นเสมอ

- ชั้นที่ 1: keyword/source evaluator เร็ว ใช้ดูภาพรวม
- ชั้นที่ 2: strict audit ใช้จับ false-pass และ route/mode ผิด

3. ปรับ competition fact card retrieval

- เพิ่ม exact question patterns ให้ 28 major ที่เหลือ
- เพิ่ม negative/positive intent เช่น Tactical Timeout vs Emergency Pause
- เพิ่ม answer template สำหรับ yes/no และ comparison
- เพิ่ม priority เมื่อ query มีคำว่า `emergency`, `technical`, `hardware`, `BO3`, `Best of 3`, `1v1`

4. ปรับ answer style ของ schedule

- ถ้าถาม service hours กว้างๆ ให้บรรทัดแรกใส่ `09:00-12:00`, `13:00-16:00`, Monday maintenance, Friday maintenance ให้ครบขึ้น
- รายละเอียดค่อยอยู่ด้านล่าง

## คำสั่งที่ใช้ตรวจซ้ำ

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --label gt360_after_noanswer_mixed_20260702
py -3 tools\strict_ground_truth_audit.py --results reports\pipeline_ground_truth_results_gt360_after_noanswer_mixed_20260702.jsonl --ground-truth C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl --label gt360_after_noanswer_mixed_audit_v2_20260702

py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\ground_truth_competition_rules_v1_228.jsonl --label competition_rules_v1_228_after_noanswer_mixed_20260702
py -3 tools\strict_ground_truth_audit.py --results reports\pipeline_ground_truth_results_competition_rules_v1_228_after_noanswer_mixed_20260702.jsonl --ground-truth data\ground_truth\ground_truth_competition_rules_v1_228.jsonl --label competition_rules_v1_228_after_noanswer_mixed_20260702
```

## สรุป

วิธีแก้ไม่ใช่ดูแค่ `PASS 360/360` แต่ต้องมี strict audit ซ้อนอีกชั้น เพราะ keyword evaluator สามารถ false-pass ได้

สถานะตอนนี้:

- 360 ข้อ: evaluator ผ่านหมด และ strict audit ไม่มี major แล้ว
- กติกาแข่ง 228 ข้อ: ยังเหลือ major 28 ต้องทำรอบถัดไปที่ competition router/fact-card
