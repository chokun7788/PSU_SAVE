# ผลการทำ Answer Quality Pipeline

วันที่: 2026-07-01

เอกสารนี้สรุปสิ่งที่ทำเพิ่มจาก `docs/09_answer_quality_pipeline.md` โดยรอบนี้ไม่ได้เป็นแค่แผนแล้ว แต่ลงมือทำเป็นโค้ด pipeline จริงสำหรับให้คำตอบของ PSU Esports Chatbot เร็วขึ้น แม่นขึ้น และตอบให้ตรงคำถามก่อนค่อยอธิบายรายละเอียด

## เป้าหมาย

เป้าหมายของรอบนี้คือแก้ปัญหาที่เจอจากการทดลองก่อนหน้า:

- คำตอบบางข้อเริ่มด้วยข้อมูลกว้างเกินไป เช่น ถามวันจันทร์ แต่ตอบเรื่องเปิด 24 ชั่วโมงก่อน ทั้งที่ผู้ใช้ไม่ได้ถาม
- คำถามราคาที่มีคำว่า "จอง" เช่น "จอง PS5 ราคาเท่าไหร่" ถูก route ไปหมวดการจองแทนหมวดราคา
- คำถามเปรียบเทียบราคา เช่น "VR 30 นาที กับ 1 ชั่วโมงต่างกันเท่าไหร่" ควรตอบตัวเลขส่วนต่างก่อน ไม่ใช่บอกแค่ราคาอย่างใดอย่างหนึ่ง
- คำถามที่มีคำใกล้เคียง เช่น "ต่างมหาลัย", "นักศึกษาทั่วไป", "นักเรียนต่างสถาบัน" ควรเข้าใจว่าเป็นกลุ่ม `PSU Alumni and General Student`
- คำถามที่ไม่มีข้อมูลจริงควรตอบว่าไม่พบข้อมูลที่ยืนยันได้ ไม่ควรเดา
- ระบบควรเร็วกว่า LLM ล้วน โดยคำถาม FAQ/ราคา/เวลา/กฎหลักควรตอบได้แบบ fast path

## ไฟล์ที่เพิ่ม

- `app/pipeline/__init__.py`
- `app/pipeline/schemas.py`
- `app/pipeline/preprocess.py`
- `app/pipeline/guard.py`
- `app/pipeline/router.py`
- `app/pipeline/retrieval.py`
- `app/pipeline/formatter.py`
- `app/pipeline/validator.py`
- `app/pipeline/engine.py`
- `app/runtime/pipeline_answer.py`
- `tests/smoke_test_answer_pipeline.py`
- `tools/run_ground_truth_pipeline_eval.py`
- `docs/10_pipeline_implementation_result.md`

## ไฟล์ที่แก้

- `app/rules/matcher.py`
  - เพิ่ม `category` filter ให้ match rule เฉพาะหมวดได้
  - ทำให้ route เช่น `rules`, `reservation`, `games`, `equipment` ไม่ต้องสแกน rule ทุกก้อนเสมอ

- `app/pipeline/router.py`
  - ปรับ priority ของ intent ใหม่
  - ให้คำถามราคา/ค่าใช้จ่ายชนะคำว่า "จอง"
  - แยก penalty/checkin/payment/rules/schedule/games/contact/overview ให้ชัดขึ้น

- `app/pipeline/preprocess.py`
  - เพิ่มการจับคำว่า "ค่าใช้จ่าย" เป็น price intent
  - เก็บ entity สำคัญ เช่น day, service, user group, duration, price intent, comparison intent

- `app/pipeline/guard.py`
  - เพิ่ม no-answer guard สำหรับคำถามนอกขอบเขต เช่น คอร์สสอนเล่น/บริการที่ไม่มีข้อมูลยืนยัน

- `app/pipeline/formatter.py`
  - ปรับ short answer ให้ไม่ตัด keyword สำคัญออก
  - บังคับแนวคิด answer-first: ตอบประเด็นที่ถามก่อน แล้วค่อยให้รายละเอียด/แหล่งอ้างอิง

## Pipeline ที่ทำงานจริง

ลำดับการทำงานตอน user ส่งคำถามเข้ามา:

1. รับข้อความจากผู้ใช้
2. Normalize ข้อความ
3. Extract entity สำคัญ
4. Guard scope ว่าอยู่นอกขอบเขตหรือไม่
5. Route intent เข้า category ที่เหมาะสม
6. ลองตอบด้วย deterministic fast path
7. ถ้า fast path ไม่เจอ ให้ลอง category rule base
8. ถ้ายังไม่เจอ ให้ค้น curated RAG เฉพาะหมวด
9. Format คำตอบให้อ่านง่ายและตอบประเด็นก่อน
10. Validate คำตอบเบื้องต้น
11. ถ้าไม่มีข้อมูลยืนยันจริง ให้ตอบ no-answer แบบสุภาพ

## Route Priority ล่าสุด

แนวคิดคือ intent ที่เสี่ยงผิดสูงต้องมาก่อนคำกว้าง ๆ:

1. `penalty`
   - คอมพัง, จอแตก, เสียหาย, ค่าปรับ, ชดเชย, แบน

2. `reservation/checkin`
   - เช็คอิน, checkin, check in

3. `service_fee`
   - ราคา, ค่าบริการ, ค่าใช้จ่าย, กี่บาท, เท่าไหร่, ต้องจ่าย, ฟรีไหม
   - สำคัญ: ถ้ามีคำว่า "จอง" แต่ถามราคา ให้เข้า `service_fee`

4. `reservation/booking`
   - จองผิด, แก้เวลา, ยกเลิก, จองใหม่, booking, จอง

5. `reservation/payment`
   - ชำระ, โอนเงิน, สลิป, เลขบัญชี, ธนาคาร, ลืมจ่าย

6. `rules`
   - ของหาย, อุปกรณ์เปียก, ย้ายอุปกรณ์, แผ่นเกม, สูบบุหรี่, แอลกอฮอล์, อาวุธ, ขยะ

7. `events_news`
   - ข่าว, กิจกรรม, การแข่งขัน, แข่ง, GAME ON, VALORANT 2026, CS 2 2026

8. `knowledge`
   - อีสปอร์ตคืออะไร, MOBA, Spacewar, ประวัติ, อาชีพ, ฝึกทักษะ

9. `schedule`
   - เปิด, ปิด, เวลา, service hours, morning, afternoon, maintenance, จันทร์, ศุกร์

10. `games`
    - เกม, Valorant, CS2, PUBG, Warzone, Mario, Overcooked, Gran Turismo, Beat Saber, Tekken, เพลย์ห้า

11. `equipment`
    - อุปกรณ์, กี่เครื่อง, รุ่นอะไร, ทีวี, จอ, monitor, เก้าอี้, เมาส์, หูฟัง

12. `contact`
    - อีเมล, Facebook, เบอร์, โทร, ที่ตั้ง

13. `overview`
    - ศูนย์นี้คืออะไร, mission, ก่อตั้ง, หน่วยงาน

14. `general`
    - ยังอยู่ในโดเมน PSU Esports แต่ไม่เข้าหมวดชัดเจน

## การแก้ปัญหาใหญ่ที่เจอ

### ปัญหา: คำว่า "จอง" ทำให้ route ผิด

ตัวอย่าง:

```text
ถ้าเป็นนักศึกษาต่างมหาลัย จอง PS5 ราคาเท่าไหร่
```

ก่อนแก้:

- เข้า route `reservation`
- ระบบไปค้นข้อมูลกฎการจอง
- ไม่เจอ service fee
- ตอบว่าไม่พบข้อมูล

หลังแก้:

- ตรวจเจอ price intent ก่อน
- เข้า route `service_fee`
- ใช้ deterministic calculator
- ตอบราคา PS5 ได้ทันที

ตัวอย่างคำตอบล่าสุด:

```text
ราคา 50 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- PlayStation 5 60 นาที ราคา 50 บาท

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

### ปัญหา: คำถามเปรียบเทียบราคาไม่ตอบส่วนต่างก่อน

ตัวอย่าง:

```text
ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่
```

หลังแก้ คำตอบเริ่มด้วยผลลัพธ์ที่ผู้ใช้ถามก่อน:

```text
ต่างกัน 185 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
- VR 1 ชั่วโมง ราคา 375 บาท
ดังนั้น VR 1 ชั่วโมงแพงกว่า VR 30 นาที 185 บาท
```

### ปัญหา: schedule ตอบกว้างเกินไป

ตัวอย่าง:

```text
วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม
```

หลังแก้ คำตอบไม่พูดเรื่อง 24 ชั่วโมงแล้ว เพราะผู้ใช้ไม่ได้ถาม:

```text
วันจันทร์ Morning เล่นไม่ได้ เพราะ 09:00-12:00 เป็น Maintenance* ส่วน Afternoon เปิดให้เล่น 13:00-16:00
```

แล้วค่อยตามด้วยรายละเอียดจากตาราง

### ปัญหา: คำถามไม่มีข้อมูลจริง

ตัวอย่าง:

```text
มีบริการซ่อมคอมส่วนตัวไหม
```

คำตอบล่าสุด:

```text
ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

แนวนี้ดีกว่าการให้ LLM เดา เพราะเป็น chatbot ของศูนย์ ถ้าตอบบริการที่ไม่มีจริงจะเสี่ยงมาก

### ปัญหา: คำว่า "แบบภาษาคนทั่วไป" ทำให้จับกลุ่มผิด

ตัวอย่าง:

```text
เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท แบบภาษาคนทั่วไป
```

ก่อนแก้ ระบบเห็นคำว่า "คนทั่วไป" ในวลี "แบบภาษาคนทั่วไป" แล้วตีความเป็นกลุ่ม General Adult จึงตอบ 150 บาท ทั้งที่ "เด็ก มอ" ควรเป็นกลุ่ม PSU Student and Staff และราคา 0 บาท

สิ่งที่แก้:

- ให้กลุ่มที่ระบุชัด เช่น `เด็ก มอ`, `นักศึกษา มอ`, `ต่างมหาลัย` ชนะคำสร้อยอย่าง `แบบภาษาคนทั่วไป`
- เพิ่ม smoke test กัน regression สำหรับเคสนี้
- เพิ่ม quality check ของ Ground Truth หมวด `service_fee` ให้ keyword เฉลยต้องอยู่ในคำตอบหลักก่อน `รายละเอียดจากตาราง`
- ป้องกัน false pass ที่เกิดจากเลขถูกไปโผล่อยู่ในรายละเอียดตาราง แต่คำตอบหลักผิด

คำตอบล่าสุด:

```text
ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff
- PlayStation 5 60 นาที ราคา 0 บาท
```

## ผล Ground Truth ล่าสุด

ไฟล์ผล:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_quality_pipeline_round4_group_fix_20260701.md
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_quality_pipeline_round4_group_fix_20260701.jsonl
```

ไฟล์สำหรับ human review จากผล pipeline ล่าสุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\human_review\human_review_pipeline_quality_round4_group_fix_full_360.md
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\human_review\human_review_pipeline_quality_round4_group_fix_full_360.jsonl
```

หน้าเว็บรีวิว:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\review_ui\index.html
```

ตอนนี้ `review_ui/review_data.js` ถูก regenerate จากผล pipeline ล่าสุดแล้ว

ผลรวม:

- Total: 360
- PASS: 360
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.0002s
- P95 latency: 0.0004s
- Keyword fail: 0
- Source fail: 0
- Quality fail: 0
- Validation fail: 0

Mode distribution สำคัญ:

- `pipeline:deterministic_calculator_fast`: 139
- `pipeline:schedule_fast_path`: 47
- `pipeline:games_fast_path`: 26
- `pipeline:guard_no_answer`: 22
- `pipeline:rules_fast_path`: 21
- `pipeline:booking_fast_path`: 20
- `pipeline:checkin_fast_path`: 12

## วิธีรัน

เปิด PowerShell:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tests\smoke_test_answer_pipeline.py
py -3 tools\run_ground_truth_pipeline_eval.py --label quality_pipeline_round4_group_fix_20260701
```

ถ้าต้องการเรียกถามเองจาก Python:

```python
from app.runtime.pipeline_answer import answer_question_pipeline_debug

result = answer_question_pipeline_debug("ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ ในเว็บบอกว่าไง")
print(result.route.category)
print(result.mode)
print(result.answer)
```

## ข้อจำกัดที่ยังต้องรู้

ผล 360/360 เป็นผลตาม Ground Truth ชุด v2 ไม่ได้แปลว่าคำถามจริงทุกแบบบนโลกจะถูกทั้งหมด

สิ่งที่ยังควรทำต่อ:

- ให้คนรีวิวคำตอบจริงอีกชั้น โดยเฉพาะคำถามยาว/คำถามกำกวม
- เพิ่มข้อมูลจริงจากศูนย์ เช่น กฎฉบับล่าสุด, policy จ่ายเงิน, policy ยกเลิก, service fee หลัง 31 มีนาคม 2026
- เพิ่ม admin update flow เพื่อให้ผู้ดูแลเพิ่มกฎใหม่ได้แบบ NotebookLM style
- ทำ retrieval แบบ hybrid สำหรับข้อมูลยาว เช่น PDF กฎ, โพสต์ Facebook, ข่าวกิจกรรม
- แยก test ชุด production ออกจาก test ชุด experiment
- เพิ่ม logging ว่า user ถามอะไร route ไปไหน และตอบด้วย source ไหน
- ทำ confidence threshold จริงสำหรับคำถามที่ข้อมูลไม่พอ

## สรุป

รอบนี้ pipeline ใช้งานได้เป็นฐาน MVP ที่ดีกว่าเอาทุกอย่างยัด rule base ก้อนเดียว เพราะแยกหน้าที่ชัดเจน:

- Rule/fast path ใช้กับคำถามที่ต้องแม่นและเร็ว
- Calculator ใช้กับราคาและการเปรียบเทียบราคา
- Guard ใช้กันคำถามนอกขอบเขต
- RAG ใช้เป็นชั้นค้นข้อมูลยืนยันเมื่อ fast path ไม่พอ
- Validator ใช้เช็คไม่ให้คำตอบหลุดประเด็นง่าย ๆ

ผลตอนนี้ตอบ Ground Truth 360 ข้อผ่านทั้งหมด และเร็วมากพอสำหรับเอาไปต่อยอดเป็น chatbot local MVP ได้

## อัปเดตเพิ่มเติม - Final Audit รอบแก้ False Pass

หลังจากตรวจผ่านหน้า review พบว่า auto evaluator แบบ keyword/source ยังมีโอกาสให้ PASS ทั้งที่คำตอบหลักผิดได้ เช่นคำถามราคาที่เฉลยต้องเป็น 0 บาท แต่คำตอบหลักตอบ 150 บาท แล้วเลข 0 ไปปรากฏในรายละเอียดตารางด้านล่าง จึงเพิ่มการตรวจแบบ answer audit อีกชั้น

สิ่งที่ปรับเพิ่มในรอบนี้:

- ปรับตัวตรวจ Ground Truth ให้หมวด `service_fee` เช็ค keyword ในคำตอบหลักก่อน `รายละเอียดจากตาราง`
- เพิ่ม `tools/audit_pipeline_answers.py` สำหรับอ่านผลลัพธ์ทีละข้อแล้วให้ `audit_decision`, `audit_score_0_4`, ปัญหาที่พบ และคำแนะนำแก้
- เพิ่ม audit เฉพาะหมวดราคาให้เช็คกลุ่มผู้ใช้กับราคาที่ควรตอบในบรรทัดแรก
- เพิ่ม audit เฉพาะหมวด schedule เพื่อกันคำตอบพูดเรื่อง 24 ชั่วโมงทั้งที่ผู้ใช้ไม่ได้ถาม
- เพิ่ม audit เฉพาะหมวด `about_us` เพื่อให้คำถาม “คือใคร” ต้องตอบชื่อจริง ไม่ใช่ตอบกว้าง ๆ ว่าเป็นหน้าสมาชิก
- เพิ่ม audit เฉพาะหมวด `events_news` เพื่อให้คำถามข่าวเฉพาะเรื่องตอบเรื่องนั้นก่อน เช่น SURAT SMASH ต้องตอบว่า 4 คน
- ปรับ fast runtime ให้คำถามข่าวและสมาชิกตอบแบบ answer-first
- ปรับ router ให้คำถามสมาชิก/Gallery เข้า route ที่เหมาะขึ้น ไม่ไปชน `knowledge` เพราะคำว่า esports

ตัวอย่างคำตอบหลังแก้:

```text
v2_339
คำถาม: เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท แบบภาษาคนทั่วไป
คำตอบหลัก: ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff

v2_272
คำถาม: SURAT SMASH ส่งตัวแทนกี่คน
คำตอบหลัก: SURAT SMASH ส่งตัวแทน 4 คน

v2_275
คำถาม: อธิการบดีในหน้าสมาชิกคือใคร
คำตอบหลัก: ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์ (PSU)
```

ผลรอบ final:

```text
Ground Truth: 360/360 PASS
Answer Audit: pass 360, minor_fix 0, major_fix 0, needs_data 0, needs_policy 0
Average latency: 0.000281s
P95 latency: 0.0004s
Max latency: 0.011s
```

ไฟล์ผลลัพธ์รอบ final:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_quality_pipeline_round6_finalaudit_20260701.md
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_quality_pipeline_round6_finalaudit_20260701.jsonl
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\answer_audit_report_round6_finalaudit_20260701.md
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\answer_audit_results_round6_finalaudit_20260701.jsonl
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\human_review\human_review_pipeline_quality_round6_finalaudit_full_360.md
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\human_review\human_review_pipeline_quality_round6_finalaudit_full_360.jsonl
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\review_ui\review_data.js
```

หมายเหตุ: ผล 360/360 ยังเป็นผลบนชุด Ground Truth v2 และ audit heuristic ที่เขียนไว้ ไม่ได้แทนการทดสอบจากคำถามผู้ใช้จริงทั้งหมด ขั้นต่อไปควรเก็บคำถามจริงจาก Facebook/ผู้ใช้ แล้วเพิ่มเข้า test set ต่อเนื่อง
