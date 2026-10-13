# ผลวิจัยและการแก้ schema query r59

วันที่ 2026-10-12

## สรุปที่อ่านได้ก่อน

แก้ logic ที่ระบุสาเหตุได้จาก r58 แล้ว และนำไปใส่ทั้ง candidate, โปรเจกต์จริง และ ready_package มีสำเนาก่อนแก้ ไม่มีการ reset/clean/commit Git ไม่มีการแก้ policy/ราคา/เวลาเปิดที่เจ้าของกรอก และไม่มีการ approve/publish ข้อมูลจริงโดยอัตโนมัติ

สาเหตุใหญ่คือ **เลือก record ถูก แต่เลือกหัวข้อที่จะอ่านผิด/ไม่ครบ** ไม่ใช่เพราะฐานข้อมูลไม่มีเนื้อหา: 2,272 จาก 2,403 failed cases เดิมเป็นกลุ่มนี้ อีก 131 เคสไม่เข้า common route งานวิจัยที่คัดใช้ 12 งานและข้อจำกัดวิธีค้นอยู่ใน Research.md; Flow.md เป็นขั้นตอนการแก้และเส้นทางตอบ; REVIEW_LOOPS.md เก็บการตรวจทานจริง 4 ลูปพร้อมผลที่ผิดก่อนแก้

## ผลทดสอบอัตโนมัติ (แยกขอบเขต)

| ชุด | ก่อน | หลัง | สิ่งที่ยืนยัน |
|---|---:|---:|---|
| Common core 5,056 | 2,653 ผ่าน / 2,403 ผิด | **5,056 ผ่าน / 0 ผิด** | requested field/content/status/source ของ fixture เดิม |
| ภาษาไทยใน core | 1,141/2,528 | 2,528/2,528 | เป็น synthetic regression |
| อังกฤษใน core | 1,512/2,528 | 2,528/2,528 | ไม่ใช่การ review การแปลโดยมนุษย์ |
| name_repeat | 64/160 | 160/160 | single repeat + whitespace ที่ชุดนี้สร้างไว้ |
| HTTP preview | content 116/224; HTTP 200 224/224 | content 224/224; HTTP 200 224/224 | actual handler + content checks |
| Actual chat pipeline | 116/224 | 224/224 | common path ใน pipeline จริง โดยใช้ DEMO DB |
| สนทนา 3 รอบ | ครบบท 40/160 | 160/160, turns 480/480 | ใช้คำตอบ assistant ก่อนหน้าจริง ไม่มี old record leak ตอนเปลี่ยนชื่อ |
| Focused checks | 42/45 รอบแรก | 50/50 หลังปรับ | quantity/negation/platform/context/reference/coverage guards |
| Owner/common units | รอบแรกมี rule failures + socket permission errors | 63/63 ในรอบแก้ | approval/publication/withdrawal/edit/version/source guards; มี base tests discover ซ้ำ |
| Final targeted units | — | 12/12 | 8 tests ใหม่ + 4 integration guards เดิม |

หลังชุด core รอบสุดท้าย เพิ่ม fallback title จาก alias และแนบ planner audit เข้า pipeline artifact; ทั้งสองส่วนไม่เปลี่ยน requested-field matching ของชุด core และมี targeted assertions/semantic trace checks ส่วน guard ไทย “ระหว่าง” ที่เพิ่มท้ายรอบมี unit แยกเพื่อไม่ให้ถูกเข้าใจเป็น “ว่าง”

### ข้อจำกัดของตัวเลข 5,056/5,056

นี่เป็นชุด regression ที่วิเคราะห์มาแล้ว ใช้ 20 scenario sets และ question patterns ซ้ำข้าม records จึงไม่ใช่ 5,056 รูปแบบภาษาอิสระใหม่ ไม่มีการส่ง gold expected_fields ให้ resolver หรือโมเดล แต่การปรับระบบจาก failures ของชุดนี้ทำให้ต้องเรียกผลว่า regression accuracy ไม่ใช่ generalization guarantee

ตัว core scorer ตรวจเนื้อหาที่ต้องมีมากกว่าคุณภาพการตอบพอดี มี reference gold บางส่วนใช้ renderer helper ร่วมกัน จึงมี focused independent test ที่ตรวจ contact.value โดยตรงเพิ่ม แต่ยังไม่เท่ากับ audit rendering อิสระทุก field

## LLM: แยกการเชื่อมต่อออกจากคำตอบถูก

ทดสอบ Typhoon 4B ที่มีในเครื่องแล้ว ไม่ดาวน์โหลดโมเดลใหม่ ชุด forced planner 48 เคสไม่มี facts หรือ gold expected_fields ใน prompt

| รอบ | Transport | Schema accepted | มี fields ที่ต้องการครบ | ตรง fields ไม่มีส่วนเกิน |
|---|---:|---:|---:|---:|
| Cold run | 2 attempted timeout, อีก 46 ถูก cooldown gate | 0 | 0 | 0 |
| Warm ก่อนตัด unrelated rate scope | 48/48 | 48/48 | 44/48 | 29/48 |
| Warm หลังจำกัด scope | 48/48 | 48/48 | 48/48 | 29/48 |
| Warm actual calls + semantic guard | 48/48 | 48/48 | 48/48 | 47/48 หลัง guard; raw ยัง 29/48 |
| Replay 48 raw proposals หลังแยก opening status | ไม่เรียกโมเดลใหม่ | raw เดิมผ่าน 48/48 | 48/48 | **48/48 หลัง guard replay**, raw ยัง 29/48 |

การ guard ให้ผลดีเพราะคำถามทั้ง 48 ในชุดนี้มี typed attributes ที่ resolver อ่านได้แล้ว ไม่ใช่ raw LLM ตอบถูก 100% สำหรับ paraphrase ที่ไม่รู้จัก ยังมี semantic uncertainty ต้องมี holdout ต่อและควรถามส่วนที่ไม่ชัดแทนเดานโยบาย

Prewarm call ใช้ประมาณ 16.25 วินาที ส่วนใหญ่เป็น model load ประมาณ 15.95 วินาที ตัวเลขนี้ไม่ใช่เวลาเฉลี่ยทุกคำถามของ chatbot ยังรักษา planner timeout 4 วินาทีและ request budget เดิม

## โค้ดที่เปลี่ยน

1. `app/knowledge/common/query_contract.py` — attribute resolver ตาม schema/kind, minimum/maximum, duration, broad request, negation, price vs live, bounded English tokens/plurals, canonical keys/labels dynamic
2. `app/knowledge/common/answer.py` — ตัดชื่อก่อนอ่าน intent; continuation/history; unique single-repeat correction + nested title; ปกป้องเลข; game mode joins; แยก rulebook release จาก rule text; source/coverage check; render contact/procedure/alias fallback; pipeline planner audit
3. `app/knowledge/common/planner.py` — field/platform enum ตาม scope, null ชัดเจน, abstention, validator ไม่ crash จาก malformed list, scope สอดคล้อง joins, semantic guard, แยก gate/timeout/schema/semantic diagnostics
4. `tests/test_common_query_contract_r59.py` — guards ที่ไม่ต้องใช้ LLM หรือแก้ owner DB

ไม่ได้แก้ `catalog.json`, owner forms/server, registry/store, engine, owner data หรือ booking API adapters เพื่อทำให้ fixtures ผ่าน

## ตัวอย่างเหตุและการแก้

### กี่คนผิดเป็น players_min

เดิม field resolver มองคำว่า “กี่คน” แล้วใส่ players_min ทุกหมวด จึงไปหา players_min ใน resource ที่มี capacity_persons การตอบว่าไม่มีข้อมูลในกรณีนี้เกิดจากเลือก schema field ผิด

ใหม่ใช้ kind: zone→room_seats, resource→capacity_persons, service→capacity_min/max, game_mode→players_min/max; คำว่า “ขั้นต่ำ/สูงสุด” กำหนดด้านของช่วง ไม่มีการอนุมานว่าจำนวนที่นั่งห้องเท่ากับผู้เล่น

### ข้อมูลครบแต่ถามต่อแล้วไม่เข้าใจ

เดิม And ไม่ได้เป็น continuation marker ที่ใช้ได้ทุกกรณี และไม่ทราบ fields ของคำถามใหม่หลายหมวด จึงไม่ได้ inherit record หรือมี record แล้ว fields ว่าง ใหม่อ่าน user turn ล่าสุดที่ระบุชื่อและให้ explicit ชื่อใหม่ชนะ history เป็นเสมอ ข้อมูล state นี้ยังมาจาก history ที่ request ส่งมา ไม่ได้สร้าง session persistence ใหม่ในรอบนี้

### ถามราคา แต่ชื่อ/alias ทำให้ตีความผิด

เดิมอ่าน keywords ก่อนลบชื่อ ชื่อที่มี rate/about/rules จึงกลายเป็น intent ใหม่ strip entity span ก่อน resolve fields และ scope related price เฉพาะ attribute ที่ reader join ได้ ไม่รวมทุก column ของ rate/rental มาให้โมเดลเลือก

### LLM ส่ง platform เป็น record ID

เดิม format เป็น string/null อิสระและ prompt ไม่มี allowed platforms โมเดลจึงส่ง demo20_* หรือ unknown แล้ว validator ปฏิเสธ แม้ HTTP/Ollama สำเร็จ ใหม่ enum เป็น null + platforms ของ selected scope และ audit บอก invalid_platform แยกจาก transport success ไม่ผ่อน validator เพื่อให้ดูผ่าน

### ตอบทั้ง record ทั้งที่ถามแค่ข้อเดียว

เดิม ครบ/all เป็น broad trigger ตาม substring และโมเดลเลือก fields ทั้งชุดง่าย ใหม่ broad ไม่ติด football/install/small/all seats/ข้อมูลครบไหม; rule text ยังคงทั้งข้อความของข้อและ dependencies แต่ metadata ทั้ง record ไม่ถูกดึงเพียงเพราะมีคำว่า “ครบ” สำหรับ raw LLM ใช้ semantic guard ลด fields เกินเมื่อ known clauses ชัดแล้ว

## สิ่งที่ยังทำต่อเองได้

| ลำดับ | งานต่อ | เหตุผล/ขอบเขต |
|---|---|---|
| 1 | Blind holdout ที่ไม่ใช้ question templates เดิม และ natural typo หลายตำแหน่ง | ผลนี้เห็น regression แล้ว; single repeat ไม่แทน missing/substitution/multi-error ทั้งประโยค |
| 2 | Dynamic schema descriptions ที่ละเอียดทั้งไทย/อังกฤษ + developer example bank แยกจาก evaluation | fast path ยังมี semantic cues ของ attributes; field ใหม่ไม่ได้รู้ทุก paraphrase อัตโนมัติ |
| 3 | ตรวจ accepted LLM plan ของ unknown clauses กับ independent semantic gold | enum กันค่าประหลาด แต่ยังเลือก valid field ผิด/เกินได้ |
| 4 | เปรียบเทียบ intent ของ common path กับ request_plan/preprocess/state ของ legacy | common ถูกเรียกก่อน full legacy preprocessing; รอบนี้ปรับ normalization ของ common เฉพาะ NFC/เเ/เบิ้ล ไม่ได้รวมทุกระบบ state ใหม่ |
| 5 | Rendering gold ที่ไม่ใช้ title/text helper เดียวกับ implementation และวัด over-answering แยกตาม kind | ราคา/policy ต้องมีบริบท แต่บางส่วนอื่นอาจยาวเกินจำเป็น |
| 6 | ออกแบบ human-facing field labels แยกจาก owner schema instructions | ตอนนี้บางคำอธิบาย schema ยาว/technical และ enum/condition objects ยังอ่านได้ไม่เป็นธรรมชาติทุกชนิด |
| 7 | Calibrate confidence จาก holdout และวัด clarification/answer trade-off | ค่า .8 ใน reader เป็น heuristic ที่ติดป้าย uncalibrated ไม่ใช่โอกาสถูก 80% |
| 8 | วัด warm/cold/multi-user latency ของเส้นทางที่ใช้งานจริง | core test มี immutable snapshot/name-cache ไม่ใช่ performance benchmark |
| 9 | ขยาย joins ตาม relation contracts ที่มีหลักฐาน เช่น game→installed service→ราคา | ไม่เพิ่ม graph traversals แบบเหมารวม เพราะจะสลับราคา/โซน/กลุ่มผู้ใช้ |

## สิ่งที่ผลอัตโนมัติยังแทนเจ้าของไม่ได้

- ผู้ใช้ยืนยันความถูกต้องของสถานะสดและภาษาอังกฤษไว้ก่อนหน้านี้แล้ว ยังคงบันทึกเป็น user confirmation ของการตรวจครั้งนั้น
- ข้อมูล DEMO 720 records ใหม่ยัง synthetic และ en_status=agent_translated ไม่ใช่ข้อมูล PSU จริง
- production common DB ตอนตรวจมี 41 heads/41 revisions และไม่มี cc_release ที่เผยแพร่ การนำ logic ไปใส่ไม่ได้เผยแพร่ 41 drafts นี้หรือยืนยัน facts แทนเจ้าของ เส้นทาง legacy ยังเป็นทางใช้งานของข้อมูลจริงที่ไม่ได้ migrate/publish
- หากจะใช้ข้อมูลกลางจริง ต้อง review records/sources/version/validity แล้ว approve/publish ผ่านเครื่องมือเดิม ส่วน logic ของการอ่านได้แก้แล้ว
- โปรเซส Python ที่เปิดอยู่ยังถือ module ที่โหลดก่อนแก้ ต้องเปิดระบบใหม่เพื่อใช้ source รุ่นนี้ ไม่ได้หยุด server ที่ผู้ใช้เปิดค้างในรอบนี้

## หลักฐานและการย้อนกลับ

- BEFORE_RECEIPT.json และ `before/` เป็น source/hash/DB logical hash ก่อนแก้
- PROPAGATION_RECEIPT.json และ THAI_GUARD_PROPAGATION.json แสดงไฟล์ที่นำไปใส่และสำเนาก่อนปรับท้ายรอบ
- `GIT_STATUS_BEFORE.txt`, `GIT_STATUS_AFTER.txt` ยืนยันว่าตรวจไฟล์ที่ยังไม่บันทึกไว้ก่อนแก้ ไม่มีคำสั่งล้างงานเดิม
- SOURCE_DIFF.patch เป็น diff รอบส่งหลัก; FINAL_SOURCE_DIFF.patch จะเก็บ source ล่าสุดหลังตรวจ preservation
- `final_verified/`, `http_round1/`, `pipeline_round1/`, `conversations_final/`, `focused_final/`, `llm_round*/` เก็บคำถาม/คำตอบ/plan/rejection และผลก่อนแก้ที่ไม่ผ่านด้วย
- Hash ฐาน owner จริง/แพ็กเกจ/DEMO ทั้งสองชุดตรงก่อนแก้ ไม่มีการลบ old logs หรือทับ analysis r58
