# ผล r28 — กติกาหลายประเด็นและ input guard

เสร็จวันที่ 2026-10-02T00:27:10.243372+07:00. เริ่มงาน/ชื่อ report ใช้วันที่ 1 ตุลาคม ระหว่างงานข้ามเป็น 2 ตุลาคม

## เว็บพร้อมลอง

[เปิดแชท](http://127.0.0.1:8090/) รุ่น `2026.10.02-competition-composition-r28-guard-verified`

แพ็กเกจใหม่: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261002_competition_composition_r28_guard_verified\PSU_Esports_Chatbot_Local`. Launcher PID 2976; เว็บทดสอบ 8091 หยุดแล้ว. ต้องให้โปรแกรมเว็บรันอยู่ขณะใช้; โหมดจองดึง WordPress ต่อคำถาม ไม่ต้องมี Dashboard แยกสำหรับแพ็กเกจนี้. ไม่เปลี่ยนหรือหยุด Dashboard ต้นฉบับ/Ollama

## เปลี่ยนอะไรและเหตุผล

- เพิ่มการเลือก clause ของ 24 แนวคิดทั่วไปสองภาษา ครอบคลุมคำถามแคบเรื่อง bugs, streams, macros, install, equipment responsibility, prep, drinks, technical reasons, abilities, customization และอื่น ๆ จากต้นฉบับเดิม
- แก้เงื่อนไขที่ตัดหัวข้อจากคำทั้งประโยค: normal money/overtime, language/protest, map pool/map tool, equipment permission/quality. ชุดทดสอบตรวจ 16 คู่ประเด็นต่อภาษา
- แยก final decision จาก final match และ dispute resolution จาก screen resolution. ข้อผิดจริง 12 ข้อจากชุดใหญ่แก้และตรวจผ่านเว็บอีกครั้ง
- ค่าสมัครที่ไม่มีหลักฐานไม่ใช้ข้อ late registration แทน. คำถาม scripts+fee เก็บข้อ scripts และแจ้งว่า fee ไม่พบ; validation ของ partial ยังบังคับแหล่งเกมถูก
- เลขข้อที่ถามต้องตรง; RoV 6.1.5.1 ที่ต้นฉบับขาดไม่ใช้โทษข้อใกล้เคียงเติม. Tekken pause แจ้งเอกสารขัดกันตั้งแต่บรรทัดแรกและแสดงทั้งสองข้อ ไม่เลือกนโยบายแทนผู้จัด
- เพิ่ม pronouns/คำหน้าที่จริงใน English language prior เพราะ its ถูกตีเป็นแป้นผิด. ไม่ปิด guard ไม่ลด threshold และไม่สร้าง alias ทั้งประโยค. Profile hash รวม prior แล้ว
- Freeze เวลาเฉพาะ fixture tests วันที่ 1 ตุลาคม เพื่อให้ “วันนี้” ตรง CSV หลังข้ามวัน. Runtime ยังตรวจวันที่จริง

## ผลอัตโนมัติ

| ชุดตรวจ | ผล | ความหมาย |
|---|---:|---|
| ชุดใหม่ 280 ข้อ | ก่อน 63/280 → หลัง 280/280 | 28 ประเด็นเดี่ยว + 16 คู่ + 8 controls ต่อภาษา; clean/polite/task typo |
| ชุดเดิม 320 / 128 / 80 | 320 / 128 / 80 ผ่านครบ | Regression ใน pipeline; ไม่ใช่ owner Gold |
| Unit | 154/154 | รวม routing, source gaps/conflicts, negation, source target, booking fixtures และ worker behavior |
| Ground Truth 2,000 รอบแรก | legacy 1,941/2,000 | ผิดประเด็นจริง 12 + ตัวตรวจ source presence พลาด 47 |
| หลังทดสอบ 59 ข้อที่ผิดซ้ำ | legacy รวม 1,953/2,000; source-grade 2,000/2,000 | ผลรวมจากรอบแรก 1,941 ข้อ + retest 59; ไม่ใช่รันเต็มรอบสองหรือ semantic correctness ทั้งชุด |
| เว็บแพ็กเกจจริง | 280 + 12 + 320 + 36 = 648/648 | รันทีละชุด; เนื้อหาตาม contracts/route smoke; ไม่มี 500/503 |
| หลังเปลี่ยน 8090 | 36/36 | Health/runtime รุ่นตรงและ mixed-route smoke |
| Guard ก่อน/หลัง | 4,283 ข้อ; newly blocked 0; ปลด false rejection 3 | Guard-only; ยังมี 36 ข้อชุด multi-error เก่าที่ต้องวิเคราะห์ พร้อม negative controls 2 ข้อที่ถูกหยุดตามเดิม |

เว็บ verified median 0.1333 s, p95 0.3304 s, max 11.2188 s. ไม่ใช่ benchmark ทุกคำถาม. ข้อช้าที่สุดคือ unsupported-game clarification/no-answer ยังผ่านเส้นทาง LLM บางส่วนราว 10–11 s. Worker recycle เปลี่ยนตัวสำเร็จ 2 ครั้งในชุดเว็บ โดยไม่มี transport error

รอบเว็บก่อนแก้ guard 275/280: ข้อผิด guard 3 + HTTP 503 จากการรันสอง clients พร้อมกัน 2. เก็บ logs/คำตอบ/trace เดิมทั้งหมดและรันทดสอบใหม่ทีละชุด ไม่ปรับเกณฑ์ให้คำตอบผิดผ่าน

## สิ่งที่คนหรือเจ้าของยังไม่ได้ยืนยัน

1. Tekken pause s03/s07: ข้อห้ามทั่วไปกับยินยอมทุกคนใช้เงื่อนไขใด กรรมการต้องอนุญาตหรือไม่ และปรับแพ้ Round/Game/Match ระดับใด
2. RoV 6.1.5–6.1.5.1: ขอข้อความต้นฉบับฉบับเต็ม เพราะท้ายข้อจบที่ “ออกจาก”
3. รายการ/ฉบับ/วันที่ใช้จริงของ rulebook และ V2 104 ข้อ. Translation approval ในระบบไม่ใช่ owner policy signoff
4. รุ่น/จำนวนจอย PS5, นโยบายภาพและวิดีโอ, ชื่ออังกฤษทางการ 23 คน/ชื่อรายการ Tekken
5. การเข้าใช้ของบุคคลทั่วไป และการนำอาหารเข้า/พื้นที่รับประทาน: ปัจจุบันมี user review+site context; ยังไม่มี owner signoff ในไฟล์
6. อายุขั้นต่ำ/ค่าสมัครแต่ละรายการ ถ้าต้องการให้ตอบได้: ต้องส่งประกาศพร้อมหน่วย/วันนับอายุ/ข้อยกเว้น. ห้ามใช้ราคาจองเครื่องเป็นค่าสมัครแข่ง
7. Oracle จองจริงกับเจ้าของยังเลื่อนไว้ตามคำสั่งผู้ใช้. API เชื่อมได้/HTTP 200 ไม่ยืนยัน booked/free ถูกต้องของข้อมูลจริง. ผล booked/free ที่ยืนยันอัตโนมัติเป็น fixture เท่านั้น

## งานต่อที่จัดลำดับได้

1. ตรวจ 36 noisy inputs ที่ guard ยังหยุดจากชุดเก่า ตาม span และบริบท; ยังไม่ใช่ผลตอบผิดทั้งหมด ต้องตรวจความหมายก่อน
2. เสริมการวัดความครบของคำถามที่มีมากกว่า 2 ประเด็น, หลายเกม, หลายเลขข้อ และ missing age+eligibility. ปัจจุบัน missing-age guard อาจตอบ no-answer ทั้งคำถาม; ไม่อ้างว่ารวมทุกประเด็นได้
3. ลดเวลาตอบกรณีเกมไม่รองรับ/ถามกลับที่ไม่ต้องใช้ LLM และตรวจผู้ใช้พร้อมกันหลายคน. การรันทีละคำถามผ่านไม่ได้พิสูจน์ concurrency
4. นำข้อมูลเจ้าของกลับมาทบทวนเฉพาะข้อที่ยืนยันแล้ว พร้อม source/version/hash และ regression; ไม่เติมนโยบายหรือข้อความ source ที่ขาดเอง

## หลักฐานและการรักษาไฟล์

Protected source/Gold/V2 queue/English CURRENT/owner schedule/service policies/r27 Flow 9 ไฟล์ hash ตรงเดิม. Snapshot ก่อนเปลี่ยนทุกไฟล์เดิมที่แก้เก็บใน before พร้อม manifest. ไม่ reset/checkout/stash Git ไม่ลบไฟล์ที่ยังไม่ commit. แพ็กเกจและ logs เก่าทั้งหมดเก็บไว้; แพ็กเกจใหม่ไม่มี eval corpus

รายงานละเอียด: CAUSE_ANALYSIS_TH.md, FULL_GROUND_TRUTH_ANALYSIS_TH.md, INPUT_GUARD_ANALYSIS_TH.md. ผลดิบ/trace อยู่ใน *_details.jsonl; สรุปตรวจสุดท้าย FINAL_VERIFICATION.json

แบบฟอร์มข้อมูลเจ้าของ: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\owner_information_request_20261001_225453_48f6a2` มีแบบเดิม 3 ไฟล์ พร้อม addendum 04/05 ที่เพิ่มใหม่โดยไม่ทับแบบเดิม
