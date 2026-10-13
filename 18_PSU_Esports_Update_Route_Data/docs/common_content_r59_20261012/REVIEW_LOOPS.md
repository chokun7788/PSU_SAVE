# บันทึกลูปตรวจทานและแก้ r59

วันที่ 2026-10-12 — เก็บทุกผลรอบก่อน ไม่ลบหรือทับ log ที่ผิด

## ลูป 1: จาก root cause สู่ schema scope

**หลักฐาน:** r58 ผิด 2,403/5,056; 1,509 target ถูกแต่ field ว่าง, 763 target ถูกแต่ field ผิด/ขาด, 131 ไม่เข้า common route

**Flow ฉบับแรก:** ตัดชื่อออกก่อนเลือก field, ใช้ schema ของหมวด, quantity mapping, explicit continuation, guard broad/live และ grammar ของ planner

**ลงมือ:** query_contract.py + reader/planner; unique repetition correction ไม่ลด fuzzy margin; coverage ไม่เป็น constant True

**ผล:** sampled 840 ผ่าน 802 ผิด 38, มี pass→fail 6; focused ผ่าน 42/45

**วิเคราะห์:** schema ที่เพิ่ม rate/rental ให้ service กว้างเกินไป ทำให้ “กี่นาที” เลือก duration_minutes ของราคาโดยที่ถาม session; plural mapping(s) ไม่ตรง; fuzzy span ยังตัดเลข 88 เหลือ 8 ได้; รูปแบบ schema ยังไม่กันชื่อสั้นซ้อนชื่อยาว

## ลูป 2: กั้น scope และรักษาเลข

**ปรับ:** cues เลือกเฉพาะ primary/game children; numeric span boundaries; plural English; platform และ opening semantics สำหรับ compound; rule intent แยก age_rating จาก competition; exact substring prefilter ช่วยลดงาน regex โดยไม่เปลี่ยนผล matching

**ผล:** focused 45/45; core 5,056 ผ่าน 5,049 ผิด 7 ทั้งหมด name_repeat ของชื่อสั้นซ้อนชื่อยาว ไม่มี pass→fail; unit รอบแรกมี 2 duplicated rule assertions ล้มและ 2 local-socket permission errors จาก sandbox; แก้ rule scope และรัน unit ภายใต้สิทธิ์ local HTTP รอบใหม่ผ่าน 63/63

**ข้อวิเคราะห์:** correction channel ต้องใช้กฎเลือกชื่อยาวเช่นเดียวกับ exact matching ไม่ใช่ยอมรับชื่อทุกตัวที่ลบเบิ้ลแล้วพบ

## ลูป 3: การตอบครบยังไม่เท่ากับตอบพอดี

**ปรับ:** suppress nested shorter aliases หลังแก้เบิ้ล; runtime case-fold/normalization; platform scope จำกัด selected record/related game ไม่ใช้ทุก platform ทั้งฐาน

**ผล core:** 5,056/5,056; HTTP preview 224/224, actual pipeline 224/224; focused เพิ่ม scoped-list/nested repeat เป็น 49/49

**LLM รอบแรก:** 2 คำเรียกใช้เวลาถึง timeout ประมาณ 4 วินาที แล้ว cooldown ทำให้ 46 ถัดไปไม่เรียกจริง ไม่ใช่ “LLM ตอบผิด 48 ข้อ” เตรียม local model ที่ติดตั้งแล้ว ใช้ประมาณ 16.25 วินาที โดย load_duration ประมาณ 15.95 วินาที นี่เป็น prewarm call เฉพาะรอบ ไม่ใช่ค่า latency ทุก request

**LLM warm รอบ 2:** transport/schema 48/48; required-field recall 44/48; exact fields 29/48; 4 miss เลือก audience_id แทน proof/eligibility เพราะเพิ่ม related rate fields ทั้งชุดใน scope

**ปรับ Flow:** scope ต้องตรงกับ reader joins จริง ไม่ใช่รวม schema ทุกชนิดที่เกี่ยวข้องแบบเหมารวม เพิ่ม related price เฉพาะ amount_minor ที่ reader ตอบได้

**LLM warm รอบ 3:** transport/schema 48/48; required-field recall 48/48; exact fields 29/48; 19 เคสตอบเกิน เช่น proof ไปพ่วง name/eligibility, open/closed ไปพ่วงตาราง/นโยบายจัดการจอง, rule text ไปพ่วง metadata ทั้งข้อ

## ลูป 4: Semantic guard และการตรวจผลที่แยกชั้น

**ปรับ:** เมื่อทุก clause มี typed interpretation แล้ว จำกัด fields ใน model proposal ให้เท่าความต้องการนั้น ปฏิเสธ all_fields ที่ผู้ใช้ไม่ได้ขอและ plan ที่ตก known need ถ้ายังเป็น paraphrase ที่ resolver ไม่รู้ ให้ระบุว่า schema-only/unverified intent ไม่เรียกมันว่าพิสูจน์ semantic แล้ว

**actual LLM warm รอบ 4:** raw exact 29/48; หลัง guard exact 47/48 พบอีก 1 เคส “opening status” ถูกตีเป็น open_periods ทั้งที่ถาม state

**ปรับ:** แยก opening status ออกจาก opening hours/periods เป็น semantic scope ของ attribute เก็บข้อกำหนดเป็น regression guard ไม่เพิ่มชื่อ fixture/เกม/ราคาจริง

**ทวน captured proposals:** 48/48 ตรง fields หลัง guard เป็น replay ของ raw proposals จาก actual LLM รอบก่อน ไม่ใช่ 48 model calls ใหม่ และไม่เปลี่ยน raw exact 29/48

**ผลหลังปรับ:** focused 50/50; final core 5,056/5,056, regressions 0; conversation 160 บทสนทนา × 3 turns = 480/480 โดยใช้คำตอบ assistant จริงก่อนหน้า; final unit 12/12

## สิ่งที่ไม่ควรสรุปจากผลนี้

- ชุด core เป็น regression จาก templates ที่เคยวิเคราะห์แล้ว ไม่ใช่ holdout อิสระ 5,056 ประโยคจริง; fixtures 20 scenario sets ใช้ patterns ที่ซ้ำกันข้าม records
- 50 focused checks บางข้อสร้างก่อนแก้และนำมาเป็น regression guard จึงไม่ใช่ blind holdout ทั้งชุด
- semantic guard ให้ผลดีเมื่อ attribute resolver ชัดอยู่แล้ว; raw model ยังเลือกเกิน 19/48 ใน forced-planner suite การแก้ postprocessing ไม่ใช่การทำให้ raw LLM เก่งขึ้น 100%
- core scoring เน้น required-content recall/status/source pointer บาง reference gold ใช้ title helper ร่วมกัน; focused contact tests มี independent gold จาก value จริง แต่ยังไม่ควรสรุปว่าคุณภาพการแสดงผลทุกชนิดสมบูรณ์
- unit 63 มี imported base TestCase ที่ถูก discover ซ้ำ จึงไม่ใช่ 63 ความสามารถอิสระ
- HTTP 200 ไม่เท่ากับคำตอบถูก; ที่รายงาน 224/224 มี content/obligation checks เพิ่ม และแยกจาก transport count
- Snapshot/name-cache ใน core test ใช้เฉพาะ fixture immutable ไม่ใช่ performance benchmark หรือ cache ของ booking สด
