# Master Ground Truth 10,000 Implementation Report

วันที่จัดทำ: 22 กันยายน 2026  
ชุดข้อมูล: `psu_esports_master_ground_truth_candidate_v1`

## 1. เป้าหมาย

สร้างชุด Ground Truth ครอบคลุมความสามารถปัจจุบันของ PSU Esports Chatbot จำนวน 10,000 คำถาม แบ่งเป็นภาษาไทย 5,000 ข้อและภาษาอังกฤษ 5,000 ข้อ โดยรวมทั้งคำถามข้อเท็จจริง คำถามที่ต้องอ่าน RAG คำถามสถานะสด คำถามกำกวม และคำถามที่ระบบต้องปฏิเสธอย่างปลอดภัย

ชุดนี้เป็น **Gold candidate** ไม่ใช่ Human-approved Gold ทั้งหมด เนื่องจากมีคำถามที่สร้างเป็น paraphrase จำนวนมาก รายการดังกล่าวถูกระบุด้วย `review_status=generated_paraphrase_pending_review` และต้องผ่านการตรวจคำตอบกับคนก่อนนำไปเป็น Release Gate แบบ strict

## 2. ไฟล์ผลลัพธ์

- `data/eval/master_ground_truth_th_5000_v1.jsonl` — ภาษาไทย 5,000 ข้อ
- `data/eval/master_ground_truth_en_5000_v1.jsonl` — ภาษาอังกฤษ 5,000 ข้อ
- `data/eval/master_ground_truth_bilingual_10000_v1.jsonl` — รวมสองภาษา 10,000 ข้อ
- `data/eval/master_ground_truth_bilingual_10000_v1_manifest.json` — จำนวน, SHA-256 และ Source Snapshot
- `data/eval/master_ground_truth_bilingual_10000_v1_report.md` — รายงานการกระจายข้อมูล
- `tools/build_master_ground_truth_10000.py` — ตัวสร้างข้อมูลแบบ deterministic
- `tools/run_master_ground_truth_eval.py` — ตัวรันและวิเคราะห์ Pipeline
- `tests/test_master_ground_truth_10000.py` — Structural Regression Tests

## 3. การกระจายข้อมูล

| Domain | ไทย | อังกฤษ | รวม |
|---|---:|---:|---:|
| Service fee | 400 | 400 | 800 |
| Reservation policy | 450 | 450 | 900 |
| Live booking/slot | 400 | 400 | 800 |
| Schedule/calendar | 350 | 350 | 700 |
| Game catalog/availability | 600 | 600 | 1,200 |
| Game detail | 450 | 450 | 900 |
| Game controls | 650 | 650 | 1,300 |
| Equipment/zones | 350 | 350 | 700 |
| Studio rules/penalties | 350 | 350 | 700 |
| Competition rules | 500 | 500 | 1,000 |
| Members/overview/contact | 250 | 250 | 500 |
| Compound/context/boundary | 250 | 250 | 500 |
| **รวม** | **5,000** | **5,000** | **10,000** |

## 4. แหล่งข้อมูล

ตัวสร้างรวมข้อมูลจาก Benchmark ภาษาไทย 1,600 ข้อ, English Shadow 1,600 ข้อ, English Gold 400 ข้อ, RAG Robustness 600 ข้อ, Competition RAG Ground Truth ปัจจุบัน, Rule Patterns, Game Details, Game Controls, Equipment, Members, Game Availability, Service Calendar และ Closure/Holiday Records

Manifest บันทึก SHA-256 ของทุก Source Snapshot และ Output ทั้งสามไฟล์ ทำให้ตรวจได้ว่าข้อมูลต้นทางเปลี่ยนหลังสร้างชุดทดสอบหรือไม่

## 5. Contract ของแต่ละข้อ

แต่ละ JSONL record มีข้อมูลหลักต่อไปนี้:

- `id`, `locale`, `question`, `domain`, `subdomain`
- `expected_routes`, `expected_status`, `target`, `facet`
- `answer_contract` สำหรับข้อความ/ข้อเท็จจริงที่ต้องพบหรือห้ามพบ
- `source_contract` สำหรับ Source ID, URL และข้อจำกัดของหลักฐาน
- `live_dependency` เพื่อแยกข้อมูลสดออกจาก Static Gold
- `review_status`, `origin`, `metadata`

สถานะคำตอบถูกแยกเป็น `answer_available`, `live_lookup_required`, `clarification_required`, `no_answer_expected`, `localization_pending`, `safe_clarification` และ `safe_no_answer` เพื่อไม่บังคับให้ระบบแต่งคำตอบเมื่อไม่มีหลักฐาน

## 6. Invariants ด้านความปลอดภัย

1. คำถาม Live Booking และ Date-aware Schedule ไม่บันทึกผลว่าง/ไม่ว่าง ณ เวลาสร้างเป็นคำตอบถาวร
2. คำถามที่ Source ไม่มีข้อมูลวัดการ abstain หรือ clarification ไม่สร้างคำตอบสมมติ
3. English Contract ไม่อนุญาตให้ Runtime แปลข้อเท็จจริงสดเอง
4. Competition Rules ใช้ Ground Truth รุ่นปัจจุบันเป็นหลัก และไม่สืบทอด Label เก่าที่ขัดกับ Source Contract
5. Game Controls ที่มีคำถามซ้ำรวม Source ID ทุกแหล่งไว้ โดยไม่เพิ่ม Duplicate Question เพื่อหลอกจำนวน
6. Generated paraphrase ทุกข้อยังคงสถานะรอตรวจจากคน

## 7. ผลตรวจโครงสร้าง

- จำนวนรวม: 10,000 ข้อ
- ภาษาไทย: 5,000 ข้อ
- ภาษาอังกฤษ: 5,000 ข้อ
- ID ซ้ำ: 0
- Allocation ผิดจากเป้าหมาย: 0
- Source coverage ที่กำหนดใน Test: ผ่าน
- Builder reproducibility/check: ผ่าน
- Unit tests: 4/4 ผ่าน

## 8. ผล Pipeline Smoke Test

รันแบบ stratified จำนวน 3 ข้อต่อ Domain รวมภาษาละ 36 ข้อ เพื่อเช็กว่า Schema และ Evaluator ใช้งานกับ Pipeline ปัจจุบันได้จริง

| ภาษา | ผ่าน | ไม่ผ่าน | อัตราผ่าน |
|---|---:|---:|---:|
| ไทย | 36 | 0 | 100.00% |
| อังกฤษ | 29 | 7 | 80.56% |

ผลนี้เป็น Smoke Test ไม่ใช่คะแนน Full 5,000 ข้อ และรอบอังกฤษเปิด Draft Preview เพื่อวัดข้อมูลที่ยังไม่ Publish เท่านั้น

### จุดผิดภาษาอังกฤษที่พบ

1. `membership annual` ถูกคำว่า membership ดึงเข้า Member List แทน Safe No-answer
2. `Are you open` ตอบตารางปกติทันที แทนการขอวัน/เวลาหรือใช้เวลาปัจจุบัน ต้องตัดสิน Product Contract ให้ชัด
3. `Which game is available in the Cockpit Zone` ถูกคำว่า available ดึงเข้า Live Schedule แทน Game Catalog
4. คำถามอังกฤษที่มีชื่อบุคลากรภาษาไทยหา Member Record ไม่เจอ
5. `Mr. Amine Abidellaoui's role` หา Member Record ไม่เจอ
6. `How many sessions can one booking include` ตอบขั้นตอนจอง แทนข้อจำกัด 3 sessions
7. `damage responsibility` เข้า No-answer แทน Studio Penalty/Responsibility Rule

ข้อผิดเหล่านี้ถูกเก็บเป็น Regression Finding โดยไม่แก้ Expected Answer ให้ตาม Output ที่ผิด

## 9. วิธีรัน

สร้างใหม่และตรวจความคงที่:

```powershell
python -X utf8 tools/build_master_ground_truth_10000.py --write
python -X utf8 tools/build_master_ground_truth_10000.py --check
python -X utf8 -m unittest tests.test_master_ground_truth_10000
```

รันภาษาไทยเต็ม 5,000 ข้อ:

```powershell
python -X utf8 tools/run_master_ground_truth_eval.py --locale th --rag-fallback
```

รันภาษาอังกฤษเต็ม 5,000 ข้อโดยเปิด Bilingual Pipeline:

```powershell
$env:PSU_BILINGUAL_EN_ENABLED='1'
python -X utf8 tools/run_master_ground_truth_eval.py --locale en --rag-fallback
```

รันตัวอย่างแบบ stratified เพื่อตรวจเร็ว:

```powershell
python -X utf8 tools/run_master_ground_truth_eval.py --locale th --sample-per-domain 3 --rag-fallback
```

## 10. ขั้นตอนก่อนเรียกว่า Human-approved Ground Truth

1. ตรวจ `generated_paraphrase_pending_review` โดยสุ่มตาม Domain และ Template Family ไม่สุ่มรวมแบบทั่วไป
2. ตรวจทุก `localization_pending` และห้ามนำไปคิด strict English answer score จนกว่าจะอนุมัติคำแปล
3. Adjudicate คำถามกำกวม โดยเฉพาะ `Are you open`, `available`, `can I`, และคำถามหลายเจตนา
4. รัน Full 5,000 ต่อภาษาและแยก Error ตาม Route, Status, Target, Fact, Source และ Latency
5. Freeze รุ่นที่ผ่านแล้วด้วย Manifest ใหม่ และเปลี่ยน `review_status` เฉพาะข้อที่คนตรวจจริง

## 11. สถานะปัจจุบัน

ชุดข้อมูลและเครื่องมือพร้อมสำหรับ Full Evaluation แล้ว แต่ยังไม่ได้อ้างว่ารัน Pipeline ครบ 10,000 ข้อในรอบนี้ การรับรอง Production Gate ต้องรอ Full Run และ Human Review ตามข้อ 10
