# ผลพัฒนาและชุดส่งต่อ r62 — 2026-10-13 เวลาไทย

## เป้าหมายที่ทำในรอบนี้

ส่งชุด Windows ที่รวมเว็บแชท หน้าผู้ดูแล ข้อมูลเดิม ตัวรัน และตัวเลือกโมเดล ให้เจ้าของเพิ่ม/แก้ข้อมูลตามหมวด บันทึก ทดสอบ อนุมัติ และเผยแพร่ แล้วแชทอ่านข้อมูลฉบับใหม่ โดยไม่เพิ่มเงื่อนไขชื่อเกมตามแต่ละคำถาม

**สถานะ: แพ็กเกจสำหรับใช้งานบน Windows ในเครื่องเดียว ยังไม่ใช่การเปิดเว็บไซต์สาธารณะบนอินเทอร์เน็ต และไม่ใช่คำรับรองทุกประโยคที่ผู้ใช้จะถามในอนาคต**

## การแก้ที่ตรวจจากหลักฐาน

| ปัญหา | สาเหตุ | การแก้ |
|---|---|---|
| เพิ่มรายการที่สองชนิดเดิมติดรหัสซ้ำ | แม่แบบใช้รหัสเริ่มต้นคงที่ | /api/template สร้างรหัสใหม่ให้แต่ละรายการ |
| ถามชื่อเดิมหลังแก้ชื่อแล้วไปข้อมูลเก่า | ค้นเฉพาะชื่อ release ปัจจุบัน | อ่านประวัติชื่อที่เคยเผยแพร่ โดยชื่อปัจจุบันมีลำดับเหนือชื่อเดิม |
| ข้อมูลใหม่มีแล้วแต่รายการเกมไม่รวมของเดิม | เส้นทางกลางแสดงเฉพาะ common release | รวมกับ verified legacy catalog และตัดซ้ำ/รายการถอน เฉพาะชนิดเกม |
| PC → กลุ่มผู้ใช้ → ทั้งหมด หลุดหัวข้อ | ประวัติเป็นข้อความลอย | เพิ่ม common_read_state ที่เซิร์ฟเวอร์บันทึกใน session |
| FAQ ใหม่ต้องถามชื่อใกล้ต้นฉบับ | ตัวอ่านเริ่มจากชื่ออย่างเดียว | คัด candidates จาก published facts แล้วให้ LLM เลือก indices ภายในรายการที่กำหนด ไม่สร้าง facts |
| ราคาเครื่อง/รุ่น/บริการที่เชื่อมไม่ถูกอ่าน | ไม่มี traversal ที่ครอบคลุม | ใช้ FK ของ schema อ่าน resource→model/zone, service→resource, rate→service/audience และ policy→procedure |
| ราคาเหมาถูกใช้แทนราคาปกติ | การถามราคาโซนเลือก rental เสมอ | แยก regular/rental intent; ส่วนที่ยังไม่ย้ายมา defer legacy; ราคาที่ถอนไม่ย้อนใช้เก่า |
| งบหลายคนใช้ราคาคนเดียว / งบเหมาไปเรตรายชั่วโมง | คำนวณจาก amount อย่างเดียว | จำกัดตาม service/group/zone/period; ไม่ขยาย fixed/free/unknown; จำนวนคนที่ยังยืนยันไม่ได้ตอบเป็น partial |
| เวลาเล่นปนกับระยะเวลาของราคา | เติม rate เข้า scope ทั่วไป | เติมราคาเฉพาะบริบทราคา และแยก session_minutes/occupancy_minutes/duration_minutes |
| แปล/ตอบช่องทางติดต่อแล้วไม่มี source ของ URL | เลือกแค่ชนิดช่องทาง | channel ต้องมี value เป็น necessary context |
| ขออุปกรณ์ที่รวมในราคาแต่ไม่ตอบอุปกรณ์ | จับคำว่า price แล้วคิดว่าครบ | เพิ่ม schema concept ของ included equipment และรักษาหัวข้อราคาเมื่อถามด้วย |
| ขอทั้งหมดแล้วตกนโยบายที่เชื่อม | full read ไม่เดิน policy edge | full game-service read รวม linked policy; รองรับ related fields ที่ประกาศใน schema |
| ค่าว่างที่ยืนยันแล้วดูเหมือนขาดข้อมูล | renderer แสดง [] เป็นข้อความว่าง | แสดงว่าไม่มีรายการในช่องนี้ และรักษา zone_ids=[] ของ schedule/closure ว่าทุกโซน |
| ต้องใช้ Ollama ของนักพัฒนา | launcher อาศัย PATH/11434 | รวม engine; ใช้ model store และ port ของแพ็กเกจ; ตรวจ manifest ของโมเดลที่ทดสอบ |
| โมเดลยังไม่พร้อมแล้วชุดทดสอบผิดจำนวนมาก | cold GPU execution หมดเวลา / circuit cooldown | warm chat model ก่อนรับคำถาม แยก startup time จากเวลาตอบ; parent startup wait รองรับ warmup |
| เปิดซ้ำแล้วเกิด model server เพิ่ม | PowerShell แปลง ISO timestamp เป็น DateTime | เทียบ creation ticks; PID/EXE/model store/port ต้องตรงก่อน reuse |
| เว็บแชทของแพ็กเกจตอบ common_unavailable | ฐานจริงรุ่นก่อนยังไม่มี cc_names | snapshot อ่านประวัติจาก release ได้โดยไม่ migrate/write ฐานจริง |
| แปลร่างใหม่ไม่ได้ | UI ส่ง note=null และยังไม่มี evidence ก่อน save | normalize note ตาม save; ผ่อนเฉพาะ cardinality evidence ใน schema ของ read-only translation |
| แปลเก็บไข่มุกเป็น Store pearls | แปลข้อความไม่มีบริบทหมวด/field | ให้ kind + field meaning กับโมเดล ทดสอบแล้วได้ Collect pearls and find an exit |
| คำที่กรอกระหว่าง request เสี่ยงถูกผลเก่าทับ | task ล็อกปุ่มแต่ไม่ล็อกช่อง | ล็อก inputs/selects/textarea ระหว่าง request และคืนสถานะ disabled เดิม |
| หน้าแก้ราคาเห็นแต่รหัส | rate ไม่มี name field | รายการผู้ดูแลแสดงชื่อบริการกับกลุ่มราคา; หัวแชทไม่ใช้ UUID เป็นคำอธิบาย |

## ผลที่ทดสอบอัตโนมัติ แยกกัน

| ชุด | ผล | ตรวจอะไร / ข้อจำกัด |
|---|---:|---|
| semantic_release_final | 148/148 | ไทย 74 อังกฤษ 74; clean/noise/negation/context/reserved; ใช้โมเดลจริงจากแพ็กเกจ กับ facts สมมุติ 720 รายการ |
| guards_final_delivery_round3 | 56/56 ก่อนเพิ่ม guard งบเหมา | schema, publication, stale/withdrawn, price, FK, context, old DB และ shared gate; ผล release ล่าสุดอยู่ใน FINAL_VERIFICATION.json |
| OWNER_HTTP_SUMMARY | 24 หมวด / 48/48 | เพิ่ม–อนุมัติ–เผยแพร่ผ่าน authenticated HTTP; canonical field questions; ไม่ใช่อัตราเข้าใจภาษาธรรมชาติ |
| WEB_FIXTURE_REVIEWED | 48/48 | /api/chat และ session จริง อ่าน facts ของ owner-created fixture; validation และ evidence pointers; ปิด worker supervisor ในชุด functional นี้ |
| UNNAMED_SUMMARY | 10/10 | 6 paraphrases FAQ ใหม่ + 4 เคสนอกเรื่อง/เลขเครื่อง/คำสั่งแทรก; ไม่มี alias ของประโยคทดสอบ |
| TRANSLATION_CHECK_REVIEWED | 3/3 | negation, booking identity, numbers/date/URL; ทดสอบร่าง ไม่ save/publish |
| TRANSLATION_CONTEXT_CHECK | 1/1 | gameplay verb collect/store; ไม่รับรองข้อความแปลใหม่ทั้งหมด |
| portable_launch_round2/3 | readiness ผ่าน | Python ของแพ็กเกจ, local LLM/embedding, workers และคำตอบ booking advance time ที่มี oracle; ไม่ใช่การยืนยันสถานะเครื่องว่างสด |
| DOWNLOAD_VARIANT_READINESS | empty-store gate ผ่าน | ไม่ยืมโมเดลของเครื่องพัฒนา; แจ้งให้ setup; ไม่ได้ดาวน์โหลด 3.6GB ซ้ำจากอินเทอร์เน็ตในรอบนี้ |
| MODEL_SERVICE_REUSE | PID/URL เดิม | ทดสอบเรียก helper สองครั้งข้ามรูปแบบ timestamp ของ PowerShell |

ดู final receipt สำหรับผล guard หลังแก้ล่าสุด, source hashes, logical DB hashes และ archive SHA/CRC

### รอบที่ล้มเหลวเก็บไว้

- semantic_llm: 37/148 มี transport timeouts และ circuit cooldown หลังเริ่มโมเดลเย็น ไม่ใช้ผลนี้เป็นการสรุปว่าไม่มีข้อมูล
- semantic_llm_warm: 145/148 เหลือ field/coverage defects 3 จุด
- semantic_llm_final: มี timeout/cooldown ระหว่างรันและเตรียมแพ็กเกจ เก็บแยกจากรอบที่ใช้ bundled service พร้อมแล้ว
- semantic_portable: 147/148; แก้ field ราคาที่ตกและตรวจด้วย gold เดิม ก่อนรัน final ได้ 148/148
- WEB_FIXTURE_SUMMARY ตัวแรกเขียน 0/48 เพราะ evaluator คาดชื่อ mode ผิด (common_content/common_published แทน common_answer); response ไม่ผิด เก็บ raw results และออก WEB_FIXTURE_REVIEWED เพิ่ม
- translation grader ตัวแรกไม่รู้จัก No เป็น negation; retained output ถูกในสาม fixture แต่ UI พบ collect/store อีกกรณี จึงแก้ prompt และตรวจเพิ่ม
- copy engine ใช้ path ยาวเกิน Windows API รุ่นเดิม; เปลี่ยนเป็น extended paths เก็บ failure logs เดิม
- unit fixtures บางรอบใช้ชนิด reference ผิดหรือชื่อที่ไม่ได้เผยแพร่ แก้ fixture ให้ตรง schema ไม่ผ่อน publication validator

## สิ่งที่เจ้าของ/คนจริงยังไม่ได้ยืนยันในรอบนี้

1. ฐานกลางที่ส่งต่อมี **41 ร่างเดิม / 0 common releases** ไม่อนุมัติแทนเจ้าของ ข้อมูลเดิมยังตอบผ่าน legacy จนกว่าจะมีรายการกลางที่เผยแพร่ ดู OWNER_REVIEW_PENDING.md และ .json สำหรับค่า/locators/ช่องที่ขาด
2. คำถามที่ยังไม่มีข้อเท็จจริง เช่น late arrival, refunds after special closure, game updates consuming booked time, extra installation/account policies และ billing basis สำหรับกลุ่ม ต้องกรอกตามคำตอบของศูนย์ ไม่ใช้ fixture เป็นนโยบาย
3. อังกฤษที่ผู้ใช้เคยบอกว่าผ่านยังคงเดิม สถานะ translation ของรายการกลาง/ข้อความใหม่เป็นอีกเรื่อง ไม่ขอให้เจ้าของยืนยันภาษาอังกฤษเดิมทั้งหมดซ้ำ
4. สถานะจริงที่ผู้ใช้เคยยืนยันว่าเช็คถูกแล้วบันทึกเป็น human-confirmed ก่อนรอบนี้ รอบนี้ไม่ได้ดึงรายการจองลูกค้าจริงมาเป็น fixture หรือรับรอง API ปัจจุบันจาก HTTP readiness

## ขอบเขตที่ยังไม่รับรองเป็น Production สาธารณะ

- ชุดนี้รัน local Windows/127.0.0.1; การใช้ URL เดียวจากมือถือ/อินเทอร์เน็ตต้องกำหนด host/domain/HTTPS/admin identity และทดสอบโหลดบน host จริง
- โปรแกรมอ่านข้อมูลกลางใหม่ได้ ไม่เขียนเปลี่ยนราคาหรือปฏิทินใน WordPress ไม่ยกเลิกการจอง การเปลี่ยนการให้บริการจริงต้องปรับต้นทางด้วย ยังไม่ได้รับรองการซิงก์ทุกตารางกลางเข้าหน้าจอง
- เพิ่มรายการใน 24 หมวดเดิมได้; เพิ่มหมวดใหม่/field ใหม่/API ใหม่ต้องทำ schema/adapter migration ไม่ใช่พิมพ์ JSON อิสระแล้วระบบจะรู้ทั้งหมด
- model candidates เป็น retrieval ที่มีขอบเขต และ confidence เป็น heuristic ที่ระบุว่าไม่ calibrated; ไม่ใช้ 148/148 เป็นโอกาสถูก 100% ของคนจริง
- functional tests และ R61 burst samples ไม่ใช่ sustained capacity certification; ยังต้องวัด concurrent traffic บนเครื่องปลายทาง
- คนละ OS/เครื่องที่ยังไม่ได้ลองจริงยังไม่ผ่าน clean-machine acceptance; รอบนี้ตรวจ bundled engine/store/Python ในเครื่องผู้ใช้พร้อม path แยกแล้ว
- Future replacement ยังต้องเก็บ draft และเผยแพร่เมื่อถึงเวลา ไม่มี scheduled publication อัตโนมัติ

## ใช้งาน

เลือกหนึ่งโฟลเดอร์ใน delivery: With Models หรือ Download Models (setup ก่อน) อ่าน START_HERE_TH.md → เปิด Open-PSU-Esports-Background.cmd → เปิด Open-Owner-Content.cmd เพื่อกรอกข้อมูล

ข้อมูลทดลอง, capability tokens และ log จากเครื่องพัฒนาไม่ได้รวมใน ZIP ใหม่ ข้อมูลจริงและ uncommitted files ใช้ hash ตรวจและมี backup/diffs ก่อนส่ง ไม่มี git reset/clean/commit และไม่เขียนทับ archive เก่า
