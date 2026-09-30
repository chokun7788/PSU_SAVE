# Master Ground Truth Full Run Analysis

วันที่รัน: 22 กันยายน 2026  
Corpus: `psu_esports_master_ground_truth_candidate_v1`  
โหมด: Local LLM enabled + RAG fallback enabled + 20-second case ceiling

## 1. ผลรวม

| Run | ผ่าน | ไม่ผ่าน | Strict pass rate |
|---|---:|---:|---:|
| Thai 5,000 | 4,289 | 711 | 85.78% |
| English 5,000 (Production localization gate) | 3,313 | 1,687 | 66.26% |
| English Competition Draft Preview 500 | 500 | 0 | 100.00% |

ไฟล์ผลรายข้อ:

- Thai: `reports/master_ground_truth_eval/master_gt_eval_20260922_211449.json`
- English Production: `reports/master_ground_truth_eval/master_gt_eval_20260922_212131.json`
- English Competition Draft Preview: `reports/master_ground_truth_eval/master_gt_eval_20260922_212621.json`

## 2. ผลแยกหมวด

| Domain | Thai | English Production |
|---|---:|---:|
| Service fee | 390/400 (97.50%) | 392/400 (98.00%) |
| Reservation policy | 281/450 (62.44%) | 267/450 (59.33%) |
| Live booking | 400/400 (100.00%) | 356/400 (89.00%) |
| Schedule/calendar | 288/350 (82.29%) | 308/350 (88.00%) |
| Games catalog/availability | 562/600 (93.67%) | 328/600 (54.67%) |
| Game detail | 422/450 (93.78%) | 33/450 (7.33%) |
| Game controls | 621/650 (95.54%) | 638/650 (98.15%) |
| Equipment | 275/350 (78.57%) | 288/350 (82.29%) |
| Studio rules/penalties | 209/350 (59.71%) | 320/350 (91.43%) |
| Competition rules | 492/500 (98.40%) | 66/500 (13.20%) |
| Members/overview/contact | 216/250 (86.40%) | 186/250 (74.40%) |
| Compound/context/boundary | 133/250 (53.20%) | 131/250 (52.40%) |

## 3. English Localization Gap

English Production มี 1,102 ข้อที่คาดหวังคำตอบ แต่ระบบคืน `localization_pending` อย่างปลอดภัย:

| Domain | จำนวนที่ถูก Localization Gate บล็อก |
|---|---:|
| Competition rules | 434 |
| Game detail | 414 |
| Games catalog/availability | 175 |
| Live booking | 44 |
| Equipment | 30 |
| Studio rules/penalties | 4 |
| Game controls | 1 |

หากแยก 1,102 ข้อนี้ออกเพื่อดูเฉพาะความสามารถที่มี English Localization พร้อม ระบบผ่าน 3,313 จาก 3,898 ข้อ หรือ **84.99%** ตัวเลขนี้เป็น Diagnostic Rate ไม่ใช่ Production Pass Rate

เมื่อนำ Competition Translation Draft ที่ซ่อมแล้วมา Preview แยก 500 ข้อ ผลเปลี่ยนจาก 66/500 เป็น **500/500** จึงยืนยันว่า Competition RAG, Target และ Claim Format ทำงานได้ แต่ Production ถูกบล็อกเพราะ `approved_localizations.jsonl` ยังว่าง การเปิด Draft Preview ไม่ถือเป็นการอนุมัติสำหรับใช้งานจริง

## 4. Failure Dimensions

หนึ่งข้ออาจผิดมากกว่าหนึ่ง Dimension จึงห้ามนำจำนวนในตารางมาบวกกัน

| Dimension | Thai | English |
|---|---:|---:|
| Route mismatch | 443 | 353 |
| Answer status mismatch | 448 | 1,417 |
| Content contract mismatch | 135 | 614 |
| Latency ceiling failure | 1 | 0 |

English Status mismatch ส่วนใหญ่เกิดจาก `localization_pending`; Thai Route mismatch เป็นปัญหา Routing จริงใน Reservation, Rules และ Equipment

## 5. Route Confusion หลัก

### Thai

- `reservation -> schedule`: 108 ข้อ
- `no_answer/overview/rules -> general`: 62 ข้อ
- `reservation -> no_answer`: 28 ข้อ
- `reservation -> clarification`: 26 ข้อ
- `rules -> clarification`: 24 ข้อ
- `games -> clarification`: 20 ข้อ
- `rules -> penalty`: 16 ข้อ
- `penalty -> no_answer`: 15 ข้อ
- `equipment -> games`: 15 ข้อ

### English

- `reservation -> schedule`: 60 ข้อ
- `games -> schedule`: 56 ข้อ โดยคำว่า `available` มักถูกตีความเป็น Live Slot
- `members/overview -> no_answer`: 52 ข้อ
- `reservation -> competition_rules`: 51 ข้อ
- `rules -> no_answer`: 15 ข้อ
- `reservation -> no_answer`: 11 ข้อ

## 6. Latency

| Metric | Thai | English |
|---|---:|---:|
| P50 | 0.352 s | 0.028 s |
| P95 | 1.341 s | 0.377 s |
| P99 | 5.947 s | 0.569 s |
| Maximum | 24.121 s | 5.196 s |
| มากกว่า 10 s | 17 | 0 |
| มากกว่า 20 s | 1 | 0 |

Thai ยังไม่ผ่าน Hard SLA เพราะ `MASTER-GT-TH-03608` ใช้ 24.121 วินาทีจากคำถามอุปกรณ์ “มีเมาส์เกมมิ่งให้ไหม” และหลุดเข้า Games/No-answer path ก่อนจบ คำถามราคา PC, check-in, refund, cancellation และ inappropriate speech บางรูปแบบใช้ 10–17 วินาทีและมักจบด้วย No-answer แสดงว่า Unknown/Fallback Path ยังเรียกงานเกินจำเป็น

## 7. ปัญหาหลักที่ยืนยันได้

1. **English Localization ยังไม่ Publish**: เป็นต้นเหตุใหญ่ที่สุดของคะแนนอังกฤษต่ำ โดยเฉพาะ Game Detail และ Competition Rules
2. **Reservation กับ Schedule ปะปนกัน**: คำว่าเวลา, check-in, late และช่วงการจองทำให้ Route ไป Schedule แม้คำถามถาม Policy
3. **Studio Rules ไทยยังไม่เสถียร**: Intent กฎทั่วไปถูกส่งไป Penalty, Equipment, Clarification หรือ General
4. **Compound/Boundary ต่ำทั้งสองภาษา**: ระบบยังจัดการคำถามกำกวม หลายเจตนา และ Unsupported Claim ไม่สม่ำเสมอ
5. **English `available` มีสองความหมาย**: Game Catalog Availability กับ Live Booking Availability ยังไม่มี Target/Facet Gate ที่แข็งแรงพอ
6. **Member Resolver อังกฤษไม่ครอบคลุมชื่อทางการและชื่อไทยในประโยคอังกฤษ**
7. **Thai fallback มี Tail Latency**: คำถามสั้นที่ไม่ Match มักเสียเวลาใน General/LLM/RAG ก่อนตอบ No-answer
8. **Evaluator มี Semantic No-answer blind spot 21 ข้อในอังกฤษ**: Output เช่น “No information ... was found” เป็น Safe No-answer แต่ Mode เป็น `rule_en` ทำให้ถูกนับเป็น `answer` ต้องแก้ Status Contract โดยไม่เปลี่ยน Expected Fact

## 8. ลำดับแก้ไขที่แนะนำ

1. ตรวจ Human Review และ Publish English Competition Localization ที่ผ่าน Preview ก่อน ห้ามเปิด Draft ใน Production
2. สร้างและตรวจ English Localization สำหรับ Game Detail, Catalog, Live Booking และ Equipment ที่ยังขาด
3. เพิ่ม Facet Gate แยก `reservation_policy`, `schedule_calendar`, `game_catalog_availability` และ `live_booking_availability`
4. แก้ Thai Studio Rules taxonomy ให้ Rule Topic ชนะ Broad General/Equipment และใช้ RAG เมื่อ Structured ไม่มีหัวข้อ
5. ปรับ Member Resolver ให้รองรับ Official English Name, Thai name in English syntax และ possessive form
6. เพิ่ม Compound Planner ที่แยก Sub-question พร้อมคง Target/Locale เดิม และกำหนด Clarification Contract กลาง
7. ตัด General/LLM fallback เมื่อ Structured Candidate มี Target ชัดแต่ไม่มี Fact โดยตอบ Safe No-answer ภายใน Budget
8. แก้ Evaluator ให้รู้จัก Semantic Safe No-answer และรัน Rescore จาก Output เดิมก่อนรัน Pipeline ซ้ำ
9. หลังแก้แต่ละกลุ่ม ให้รันเฉพาะ Domain ก่อน แล้วจึงรัน Full 10,000 เพื่อป้องกัน Regression

## 9. ข้อสรุป

ระบบยังไม่พร้อมเรียกว่า “ผ่านดีมากทุกส่วน” แม้หมวด Live Booking, Game Controls และ Competition RAG ภาษาไทยจะแข็งแรงแล้ว คะแนนภาษาอังกฤษ 66.26% ไม่ได้หมายความว่าโมเดลเข้าใจอังกฤษไม่ได้ทั้งหมด แต่สะท้อน Localization Gate ที่ยังไม่ Publish 1,102 ข้อร่วมกับ Routing/Contract Gap อีกประมาณ 585 ข้อ ส่วนไทยยังมีปัญหาจริง 711 ข้อและมีหนึ่งคำขอเกินเพดาน 20 วินาที
