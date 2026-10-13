# ผล r60 — สำนวนใหม่และความครบของคำตอบตาม format กลาง

วันที่ 2026-10-12 (วันที่ตาม client); ใช้โมเดล local `scb10x/typhoon2.5-qwen3-4b` ที่มีอยู่ในเครื่อง ไม่ดาวน์โหลดหรือฝึกโมเดลใหม่

## ผลที่วัดได้จริง

| เส้นทาง / ชุด | ผล | ความหมาย |
|---|---:|---|
| ก่อนแก้, deterministic, development | 17/100 | อ่านชื่อรายการได้ แต่การเลือกเนื้อหาตามสำนวนใหม่อ่อน |
| ก่อนแก้, actual LLM, development | 79/100 | เชื่อมโมเดลได้ยังตอบไม่ครบ/ผิดช่อง |
| หลัง descriptions / gate / history รอบแรก | 87/100 | คำอธิบายอย่างเดียวไม่พอ |
| หลังแยก clause | 93/100 | ยังมี schema-valid แต่เลือกความหมายผิด |
| หลัง guard | 98/100 | มีส่วนที่สองตกหล่น |
| รอบถัดไป | 99/100 | มี false partial: เนื้อหาครบ แต่ why clause ถูกทำเป็น [] |
| หลัง typed coverage repair และใช้ context 3072 | 100/100 | ไทย 50/50 อังกฤษ 50/50; เป็น development ที่เห็นแล้ว |
| reserved ที่ freeze ก่อนเปิดผล ครั้งแรก | 43/48 | ไทย 22/24 อังกฤษ 21/24; synthetic ที่ agent แต่งเอง |
| reserved หลังแก้ | 48/48 | เป็น regression หลังเห็นปัญหาแล้ว |
| หลังแก้ แต่ปิด LLM, development | 18/100 | ยังไม่รองรับสำนวนใหม่กว้างเท่าเส้นทางเปิด LLM |
| actual pipeline + actual LLM | 12/12 | 6 หมวด × ไทย/อังกฤษ; มีแหล่งข้อมูล/เนื้อหาตาม fixture |
| actual authenticated owner preview HTTP + actual LLM | 12/12 | หลังแก้หน้าทดลองให้ใช้ planner; epoch ไม่เปลี่ยน |
| game → fields ของรายการลูกที่อ้าง game_id | 16/16 | catalog-driven projection; ไม่ได้ทดสอบ graph ทั้งหมด |
| related r59 regression | 5,056/5,056 | ไทย 2,528 อังกฤษ 2,528; seen synthetic, ไม่ใช่ชุดผู้ใช้จริง |
| owner/common unit ก่อนแก้ endpoint ล่าสุด | 81 tests ผ่าน | มี base tests ถูก discover ซ้ำ ไม่ใช่ 81 ความสามารถอิสระ |
| guards รุ่นสุดท้าย | 21 tests ผ่าน | r60 13 + r59 8; รวมการปิด LLM / default / clause overflow |
| นำเข้าโปรเจกต์จริงแล้ว, guards | 22 tests ผ่าน | actual project imports; mocked config guards + temporary owner HTTP |
| owner save/approve/publish/preview guard หลังแก้ | 1 test ผ่าน | ใช้ฐานข้อมูลชั่วคราว; auth/origin/draft guard ยังอยู่ |

ไม่รวมคะแนนเหล่านี้เป็น accuracy เดียว เพราะหน่วยวัด/เส้นทาง/การเห็นข้อมูลต่างกัน ไม่ใช่ latency หรือ concurrent benchmark ไม่ได้ทดสอบ WordPress รอบนี้

## สิ่งที่แก้

1. แยกคำถามภาพรวมจริงออกจากการมีคำว่า “ข้อมูล/information” อยู่ในประโยค ทำให้คำถาม expiry ยังเข้าตัวตีความได้
2. เพิ่มคำอธิบายความหมายของ attribute ไทย/อังกฤษใน `schema_descriptions.json` ซึ่งเป็น metadata นักพัฒนา แยกจากข้อมูลเจ้าของและ gold
3. ให้โมเดลเลือก field ต่อ clause ในคำขอเดียว บังคับ enum/type/IDs จำนวน clause ไม่ให้ตอบ facts/SQL หรือเลือก record ใหม่
4. ทบทวนเมื่อ lexical match อาจเป็นแค่คำหัวข้อ เช่น eligibility/proof, provider/status mapping, rule text/rulebook edition, play/reserved time
5. ไม่คง field ที่เป็น weak match ไว้เพียงเพราะมันเลือกได้ก่อน; เก็บ strong needs และ rejected-task guard
6. ต่อบทสนทนาโดยสืบทอดรายการ แต่สืบทอด fields เฉพาะเมื่อข้อความเป็นตัวเลือกสั้นจริง ไม่สืบทอดทุก field เมื่อ user ถามเรื่องใหม่
7. spelling candidate จากศัพท์ schema เฉพาะ insertion/deletion ระยะ 1 และ candidate เดียว รักษาเลข/คำปฏิเสธ/คำที่เป็นคำจริง ไม่เพิ่ม alias ของคำถามทั้งประโยค
8. ตัวอ่าน game ใช้ metadata catalog เลือก fields ของรายการลูกโดย game_id พร้อม evidence เดิม
9. แยก transport / schema / semantic / content ใน trace; JSON ผิดแต่ HTTP สำเร็จไม่ทำให้ circuit มองว่าโมเดลล่ม
10. ถ้ารู้ว่าบาง clause ยังไม่ตีความ ให้ partial_answer พร้อมแจ้งส่วนที่ค้าง ไม่ validated complete; เกิน 6 clause ปฏิเสธ planner พร้อมเหตุผล ไม่ตัดข้อความเงียบ ๆ
11. context planner เปลี่ยน 4096 → 3072 ให้ตรง warmup ของแชท; วัด dev ใหม่ผ่านครบ แต่ยังไม่ได้วัดผลด้าน cold-start latency
12. owner preview เปิด planner ตาม `PSU_LOCAL_LLM_ASSIST_ENABLED` ค่าเริ่มต้นเปิด เหมือนเว็บแชท; `PSU_COMMON_PLAN_LLM=0` ยังปิดเฉพาะ planner ได้ มี deadline และ audit
13. pipeline ที่รับ `experimental_allow_llm=None` อ่าน `PSU_EXPERIMENTAL_ALLOW_LLM` ก่อน common route; explicit False ยังปิดได้เหมือนเดิม

## ข้อจำกัด

- คะแนนผ่านต้องมี expected fields/status/value leaves/evidence locator และไม่ตอบงานที่ปฏิเสธ แต่ไม่บังคับว่าห้ามมี field เสริมทุกชนิด
- คำถามใหม่ใช้ชื่อ/alias ของ fixture ที่ resolve ได้ก่อน; ยังไม่พิสูจน์ unnamed search, หลายรายการในข้อความเดียว หรือข้อความกำกวมทุกชนิด
- noise 48 เคสเป็นการเบิ้ล 2 จุดและลบ 1 จุดใน sentence รักษา entity names และตัวเลข; ไม่ใช่ 48 รูปแบบ keyboard substitution และไม่ใช่ human typo distribution
- context 2 เคสใน development เป็น previous user alias + all information; หลักฐานสนทนาหลาย turn ชุดใหญ่เป็นของ r59 ไม่ได้แต่งเติมว่าร60ทดสอบทั้งหมดใหม่
- schema-valid plan ยังเลือก field ผิดได้ ไม่ใช้ 100/100 เป็นหลักฐานว่า LLM เข้าใจทุกคำถามแล้ว
- ข้อมูลตัวอย่าง 720 รายการแยกจาก production และ opt-in demo; ฐานจริงยังมี draft ที่ไม่ได้ publish ข้อมูลใหม่ผ่าน format กลางต้อง owner review/approve/publish ก่อน
- การแปลความหมาย field โดย agent ไม่ใช่การยืนยันการแปลข้อเท็จจริงเจ้าของโดยมนุษย์
- process เว็บเดิมเก็บ Python modules รุ่นที่โหลดแล้ว ต้องปิด/เปิดใหม่เพื่อรับโค้ดนี้ ไม่ได้ restart session ของผู้ใช้ระหว่างทำงาน

รายละเอียดการเลือกผิดทุกเคส LLM และ reserved อยู่ใน [ANALYSIS_TH.md](ANALYSIS_TH.md); flow ฉบับปรับปรุงอยู่ใน [Flow.md](Flow.md)

## ความเกินของเนื้อหาใน development ที่ผ่าน

ตรง expected fields เป๊ะ 72/100; มี field เสริม 28/100. ตารางนี้แยก content recall จาก field precision: `{'device_type': 2, 'name': 6, 'usage': 2, 'channel': 4, 'purpose': 2, 'outcome': 2, 'preconditions': 2, 'topic': 4, 'deadline_minutes': 1, 'conditions_all': 4, 'consequence': 4, 'details': 4, 'subject': 1, 'audience_id': 8, 'calculation_rule': 4, 'currency': 8, 'duration_minutes': 8, 'persons_max': 4, 'persons_min': 4, 'service_id': 4, 'tax_note': 4, 'period_label': 4, 'room_seats': 4, 'terms': 4, 'zone_ids': 4, 'title': 2, 'public_scope': 1, 'team': 1, 'question': 4}`. Field เสริมจึงยังเป็นพื้นที่พัฒนา ไม่ปิดประเด็นด้วยคำว่า “ผ่านครบ”.
