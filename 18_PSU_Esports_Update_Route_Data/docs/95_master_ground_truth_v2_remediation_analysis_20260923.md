# Master Ground Truth v2: ผลรันและงานแก้ไขรอบ 23 กันยายน 2026

## ขอบเขตและสถานะของตัวเลข

Corpus เป็น candidate 5,000 คำถามไทย + 5,000 คำถามอังกฤษ ไม่ใช่ชุด Gold ที่มนุษย์ตรวจครบทุกข้อ ใช้ Local LLM และ RAG fallback ขณะรัน แต่คำตอบ Structured ที่มีหลักฐานชัดเจนไม่จำเป็นต้องเรียก LLM เพดานต่อข้อของ evaluator คือ 20 วินาที

| Run | Thai | English | หมายเหตุ |
|---|---:|---:|---|
| v1, 22 ก.ย. | 4,289/5,000 (85.78%) | 3,313/5,000 (66.26%) | Baseline ใน `94_master_ground_truth_full_run_analysis_20260922.md` |
| v2, 23 ก.ย. ก่อนแพตช์รอบนี้ | 4,386/5,000 (87.72%) | 4,046/5,000 (80.92%) | รันเต็มทั้งสองภาษา |
| v3, 23 ก.ย. หลังแพตช์ English member/equipment/game/machine | ไม่ได้รันเต็มซ้ำ | 4,414/5,000 (88.28%) | รัน English เต็มก่อนแก้ Schedule/Boundary |
| v4, 23 ก.ย. หลังแก้ Schedule/Boundary | ไม่ได้รันเต็มซ้ำ | 4,433/5,000 (88.66%) | English Full Run ล่าสุด; Thai ยังไม่รันเต็มหลังแพตช์ |
| v5, 24 ก.ย. หลังแพตช์ Thai equipment/rules | 4,467/5,000 (89.34%) | ไม่ได้รันเต็มซ้ำ | Thai Full Run ล่าสุด; เพิ่ม 81 ข้อจาก v2 |

Raw detail: `reports/master_ground_truth_eval/master_gt_eval_20260923_160630.json` (Thai v2), `master_gt_eval_20260923_145444.json` (English v2), `master_gt_eval_20260923_171356.json` (English v3), `master_gt_eval_20260923_202616.json` (English v4) และ `master_gt_eval_20260924_124559.json` (Thai v5) ในโฟลเดอร์เดียวกัน ไฟล์ `_summary.json` ชื่อเดียวกันคือผลแยกหมวด ห้ามเอาผลเฉพาะหมวดที่รันหลังจากนั้นมาอ้างว่าเป็น Full Run ใหม่

## สิ่งที่ยืนยันจากการทดสอบ

- English Game Detail: 228/450 -> 446/450 เพราะข้อความรอ Localization ระบุชื่อเกมเป้าหมาย และคำตอบว่าเกมอยู่โซนใดแสดงชื่อ Zone จากแหล่งข้อมูลเดียวกับ machine labels
- English Members: 158/250 -> 240/250; คำถามอังกฤษที่มีชื่อ/ตำแหน่งภาษาไทยทางการไม่ถูกตัดเป็น Keyboard Error อีก และค้นเฉพาะระเบียนบุคคล/ตำแหน่งที่ตรง
- English Equipment: 288/350 -> 312/350; คำถามรุ่น GPU และจอย PS5 ที่ไม่มีสเปกยืนยันตอบว่าไม่พบสเปกนั้น แทนการแสดงแคตตาล็อกทั้งโซน ส่วนคำถามหูฟังใช้รายการอุปกรณ์ที่มีจริง
- English machine-game availability: หมวดที่ชื่อ `live_booking` ใน corpus เพิ่ม 356/400 -> 400/400 หลังตรวจหมายเลข PC กับ `machine_numbers` ของระเบียนเกมแยกเครื่อง ระบบแยกชัดระหว่าง *catalog availability* กับสถานะติดตั้ง/ว่างแบบสด
- Thai Studio Rules แบบรันเฉพาะหมวดเพิ่ม 202/350 -> 266/350 หลัง safe RAG miss ถูกจัดเป็น route `no_answer` ตามผลลัพธ์จริง ไม่ใช่ `general`; ยังเหลือ 84 ข้อที่เกี่ยวกับ facet/route/หลักฐาน
- English Schedule แบบรันเฉพาะหมวดเพิ่ม 315/350 -> 334/350 หลังไม่ปล่อยชื่อวันสำคัญภาษาไทยที่ยังไม่แปลเข้า English prose, อ่าน closure รายสัปดาห์จาก local calendar และถามวันที่เมื่อถามวันหยุดราชการกว้าง ๆ
- เคส `MASTER-GT-TH-03608` (“มีเมาส์เกมมิ่งให้ไหม” พร้อมคำเกริ่น) เคยใช้ 25.22 วินาทีใน Full Run และ 35.18 วินาทีเมื่อรันเดี่ยว สาเหตุจาก trace คือ Structured 11.76 วินาที, Deterministic 12.73 วินาที, Hybrid Retrieval 7.07 วินาที โดย route ผิดเป็น Games ตอนนี้ใช้ระเบียนอุปกรณ์ที่ยืนยันแล้ว ตอบถูกใน 1.50 วินาทีเมื่อรันเดี่ยว
- English v4 Full Run: P50 0.060 วินาที, P95 0.449 วินาที, P99 0.775 วินาที, Max 11.819 วินาที, มี 2 ข้อเกิน 10 วินาทีและ 0 ข้อเกิน 20 วินาที ได้แก่ `MASTER-GT-EN-03346` (Equipment, 11.819 วินาที) และ `MASTER-GT-EN-04981` (คำถามทั่วไปผ่าน direct LLM, 10.226 วินาที) ทั้งสองข้อผ่าน answer contract แต่ไม่ผ่านเป้าหมาย 10 วินาที ส่วน Thai v2 Full Run ยังมี 32 ข้อเกิน 10 วินาทีและ 1 ข้อเกิน 20 วินาที; ยังอ้างไม่ได้ว่า Thai เวอร์ชันหลังแพตช์ผ่าน SLA ทั้งหมด
- English compound/boundary แบบรันเฉพาะหมวดได้ 250/250 หลังกันคำถาม weather ออกจาก Studio Schedule; Full Run v4 ยืนยัน 250/250 เช่นกัน
- Thai v5 Full Run เทียบ Thai v2: Studio Rules 202 -> 263/350 (+61), Equipment 275 -> 287/350 (+12), Compound/Boundary 155 -> 164/250 (+9), Members 216 -> 217/250 (+1), Reservation Policy 352 -> 350/450 (-2); หมวดอื่นคะแนนเท่าเดิม เคส `MASTER-GT-TH-03608` ผ่านใน 0.2775 วินาทีด้วย equipment fast path
- Thai v5: P50 0.419 วินาที, P95 2.209 วินาที, P99 7.757 วินาที, 28 ข้อเกิน 10 วินาที, 2 ข้อเกิน 20 วินาที สองข้อหลังมี elapsed ผิดปกติ 24,799.692 และ 29,766.957 วินาทีระหว่างรันข้ามวัน อาจสัมพันธ์กับเครื่องพัก/การเชื่อมต่อสะดุด แต่ยังพิสูจน์ไม่ได้; ต้อง rerun เคสเหล่านี้พร้อม monotonic stage trace ก่อนสรุปว่าเป็นเวลาประมวลผลจริง
- Focused rerun `master_gt_eval_20260924_124938.json`: `MASTER-GT-TH-04555` ใช้ 7.808 วินาทีและ `MASTER-GT-TH-04562` ใช้ 0.527 วินาที ไม่พบการค้างหลายชั่วโมงซ้ำ แต่ทั้งสองยังไม่ผ่านเพราะ `candidate_margin_clarification` แทนการตอบตัวตน/ผู้ดูแลศูนย์ ส่วน `MASTER-GT-TH-00411` และ `MASTER-GT-TH-00800` ยังถูก `answer_contract_no_answer` ใน rerun เดี่ยว 11.277 และ 12.707 วินาทีตามลำดับ (`master_gt_eval_20260924_125001.json`, `master_gt_eval_20260924_125025.json`)

## ตัวอย่างปัญหาที่แก้แล้ว

1. `What is ผศ.ดร.นิวัติ แก้วประดับ's role` เคยถูกตอบว่าอาจพิมพ์ผิดคีย์บอร์ด ปัจจุบันค้นระเบียนชื่อทางการและตอบตำแหน่งจากต้นฉบับไทยพร้อมลิงก์
2. `What GPU model is inside the PCs` เคยตอบรายการอุปกรณ์ PC ทั้งโซน ปัจจุบันบอกตรง ๆ ว่าแหล่งข้อมูลอุปกรณ์ไม่ได้ระบุรุ่น GPU
3. `Which studio zone has Animal Crossing: New Horizons` เคยตอบแค่ชื่อ slot ของเครื่อง ปัจจุบันบอก `Nintendo Switch Zone` และ slot ที่มีรายการเกม
4. `Does PC #01 have Call of Duty: Warzone` เคยไป Game Detail และติด English Localization Gate ปัจจุบันตรวจเกมในกลุ่ม PC #01-#02 แล้วตอบว่าไม่อยู่ในรายการของเครื่องนี้ โดยไม่อ้างว่าเช็กการติดตั้งแบบสด
5. `Will the studio be open tomorrow` เคยถูก Hard Veto ทั้งคำตอบเมื่อปฏิทินมีชื่อวันสำคัญไทย ปัจจุบันยังแสดงเวลาที่เปิด/ปิดได้เป็นภาษาอังกฤษ และบอกว่ามีปฏิทินไทยที่ชื่ออยู่ในต้นฉบับ

## ส่วนที่ยังไม่ผ่านและสาเหตุ

| กลุ่ม | จำนวนอ้างอิง | สาเหตุ/ทางแก้ |
|---|---:|---|
| English Competition Rules | 436/500 ไม่ผ่านใน Full Run ล่าสุด | ส่วนใหญ่เป็น `missing_english_localization`; translation draft ที่ยังไม่ได้ Human Approval ห้าม Publish เพื่อดันคะแนน ต้องตรวจความหมายเทียบกฎไทยก่อนอนุมัติ |
| English Equipment | 38/350 ยังไม่ผ่าน | 30 ข้อถามคำอธิบายอุปกรณ์ที่ไม่มี Approved English overlay; ที่เหลือแยก unsupported specification กับคำตอบที่มีหลักฐานจริง ต้อง review รายข้อ |
| English Studio Rules | 30/350 ยังไม่ผ่าน | ขาดการจับ intent/facet กฎความรับผิดชอบ ของหาย และกฎทั่วไป บางคำถามไหลเข้าเกมจากคำว่า controller |
| English Service Fee | 21/400 ยังไม่ผ่าน | ส่วนหนึ่งถามราคาเกมโดยไม่ระบุ Zone/ระยะเวลา/กลุ่มลูกค้า เช่น TEKKEN 8 อยู่ได้หลายบริการ การถามกลับเป็นพฤติกรรมที่ถูกต้อง แต่ Gold เดิมคาด `answer_available`; ต้อง Human Adjudication ไม่ควรเดาราคา |
| Thai Reservation Policy | 100/450 ไม่ผ่านใน Thai Full v5 | Policy เช่นเช็กอิน คืนเงิน และจ่ายเงินหลุดไป Schedule/No-answer; สองข้อที่เคยผ่านกลับถูก `answer_contract_no_answer` และ rerun เดี่ยวยังล้ม ต้องไล่ retrieval/evidence validation โดยตรง |
| Thai Compound/Boundary | 86/250 ไม่ผ่านใน Thai Full v5 | คำถามหลายประเด็น/ข้อความกำกวมยังแบ่ง sub-question และรักษา target ไม่สม่ำเสมอ แม้ดีขึ้น 9 ข้อ |
| Thai Studio Rules | 87/350 ไม่ผ่านใน Thai Full v5 | รันเฉพาะหมวดก่อนหน้านี้ไม่ผ่าน 84 ข้อ ความต่าง 3 ข้อชี้ว่าผลยังไม่เสถียร; ต้องปรับ facet mapping/grounding แทนการเพิ่ม alias รายคำ |
| Thai Equipment | 63/350 ไม่ผ่านใน Thai Full v5 | ดีขึ้น 12 ข้อ แต่คำถามอุปกรณ์บางชนิดยัง route ผิดหรือไม่มีหลักฐานยืนยันสำหรับคุณสมบัติที่ถาม |
| Thai latency anomalies | 28/5,000 เกิน 10 วินาที; 2 ข้อเกิน 20 วินาที | สองข้อเป็น `MASTER-GT-TH-04555` และ `MASTER-GT-TH-04562` ที่มี elapsed หลายชั่วโมงระหว่างรันข้ามวัน; rerun ไม่เกิดเวลาหลายชั่วโมงซ้ำ แต่ยังต้องตรวจ host/worker trace ก่อนระบุ root cause ห้ามใช้ Max นี้เป็นตัวแทน production latency; อีก 26 ข้อเกิน 10 วินาทีโดยไม่รวมสอง anomaly |

## ข้อจำกัดของ Ground Truth และ Evaluator

1. `generated_paraphrase_pending_review` ยังไม่ใช่ Gold ที่รับรองแล้ว คำเกริ่นหลายแบบทำให้ case เดิมถูกนับซ้ำหลายสิบครั้ง คะแนนจึงไม่เท่ากับความครอบคลุมเชิงเจตนา 10,000 แบบอิสระ
2. Evaluator ตรวจ route, status, latency และ substring `must_contain`/`must_contain_any` เป็นหลัก ยังไม่ได้ตรวจความหมาย, `expected_target`, `expected_facet`, `source_contract`, เวอร์ชันข้อมูล หรือข้อความ unsupported claim แบบครบถ้วน คะแนนผ่านจึงไม่รับรองว่าคำตอบทุกข้อถูกต้อง
3. Gold บางข้อขัดกันเอง: `Is the studio open on public holidays` ถูกคาดทั้ง `answer_available` และ `clarification_required`; ต้องระบุวันที่ก่อนจึงตรวจ exception ได้อย่างปลอดภัย อีกตัวอย่างคือถามรุ่นจอย PS5 ทั้งที่ curated equipment source ไม่ได้ระบุรุ่น
4. `localization_pending` เป็น safe outcome แต่ยังไม่ใช่คำตอบครบสำหรับผู้ใช้ หากต้องการ English เต็ม ต้องมีการแปลและอนุมัติเนื้อหาต้นทาง โดยเฉพาะ Competition Rules
5. การจำกัดเวลารวมของ Local LLM stream ได้เพิ่มการตรวจ elapsed ระหว่าง token แล้ว แต่ socket timeout และ Python Pipeline แบบ in-process ยังไม่ใช่ Hard Deadline ที่รับประกัน 20 วินาทีในทุกกรณี ต้องทดสอบ HTTP/Worker Supervisor แยกต่างหาก

## ลำดับงานถัดไป

1. Human review/approve English Competition Rule claims ทีละ source/facet/version แล้วรัน 500 competition cases และ 5,000 English อีกครั้ง ห้ามเปิด draft preview ใน Production
2. Adjudicate Gold ที่ขัดกันและเพิ่ม semantic/source/target assertions สำหรับเคสสำคัญ โดยไม่เปลี่ยน expected เพียงเพื่อเพิ่มคะแนน
3. แก้ Thai Reservation/Rules/Compound ตาม failure cluster พร้อม focused regression และกันคำถามอุปกรณ์ไม่ให้เข้า Game Resolver
4. ทำ Hard Deadline ที่ระดับ HTTP + Worker พร้อมทดสอบ concurrent users จริง; ตรวจว่า timeout/stream/cancel ไม่ทิ้งงานค้าง
5. เก็บ stage trace ของเคส identity/manager และ Reservation ที่ rerun แล้วยังไม่ผ่าน, แก้ route/grounding โดยไม่เดาข้อเท็จจริง จากนั้นรัน Full Thai/English 5,000 หลังงาน localization และรายงานทั้ง pass rate กับ P95/P99/Max โดยแยก source-language fallback

## จุดอ้างอิงสำหรับการรันซ้ำ

- Full corpus: `data/eval/master_ground_truth_bilingual_10000_v2.jsonl`
- Runner: `tools/run_master_ground_truth_eval.py --locale th|en --allow-llm --rag-fallback`
- English Full ล่าสุด: `reports/master_ground_truth_eval/master_gt_eval_20260923_202616.json`
- Thai Full ล่าสุด: `reports/master_ground_truth_eval/master_gt_eval_20260924_124559.json`
- Focused: `master_gt_eval_20260923_163730.json` (Thai rules), `master_gt_eval_20260923_170320.json` (English machine-game), `master_gt_eval_20260923_195916.json` (English schedule) ใน `reports/master_ground_truth_eval/`
- Regression tests: `tests/test_master_ground_truth_route_regressions.py` และ `tests/test_experimental_fallback_deadline_stream.py`
