# Competition Source-Gap Negative Gold Report

วันที่ตรวจ: 2026-09-22

## เป้าหมาย

เพิ่มคำถามที่มนุษย์ใช้จริงสำหรับหัวข้อซึ่ง Active Rulebook ยังไม่มีข้อความพิสูจน์โดยตรง และบังคับให้ระบบตอบแบบ Safe No-answer แทนการยืมกฎจากหัวข้ออื่นหรือเกมอื่น

งานนี้ไม่ได้เพิ่มข้อเท็จจริงใหม่ลงฐานความรู้ และไม่ได้ใช้ LLM เติมช่องว่างของเอกสาร

## สิ่งที่ยืนยันจาก Source

- VALORANT มี Map Pool 7 แผนที่และคำสั่ง Ban maps until 3 maps remain อยู่ใน Source จริง จึงย้ายหัวข้อนี้เป็น Answerable และไม่จัดเป็น Source Gap
- RoV ยังไม่มีระยะเวลาที่ต้องมาถึงก่อนแข่งและไม่มีขั้นตอน Check-in หน้างานโดยตรง
- VALORANT ยังไม่มีจำนวนผู้เล่นตัวจริง, จำนวนตัวสำรอง, อายุขั้นต่ำ, กำหนดปิดรับรายชื่อ, กฎพฤติกรรม/น้ำใจนักกีฬา และขั้นตอนทั่วไปสำหรับเหตุระหว่างแมตช์
- ข้อความ Match Prep ที่อนุญาตไม่เกิน 6 คนในพื้นที่ ไม่ใช่หลักฐานว่าต้องส่งผู้เล่นตัวจริง 6 คน
- ตารางโทษจาก Exploit ไม่ใช่หลักฐานของโทษสำหรับคำหยาบหรือพฤติกรรมไม่เหมาะสม

## ชุดทดสอบใหม่

เพิ่ม `source_gap_safe_no_answer` 20 ข้อ:

- ภาษาไทย 10 ข้อ
- ภาษาอังกฤษ 10 ข้อ
- ทุกข้อ Lock เกม, Rulebook และ Facet
- ทุกข้อผูก `source_gap_manifest_key` และ `source_gap_reason`
- ทุกข้อต้องคืน No-answer โดยไม่มี Evidence ID หรือ Source Hit

หัวข้อที่ครอบคลุม:

1. RoV Arrival Lead Time
2. RoV On-site Check-in Procedure
3. VALORANT Starting Players
4. VALORANT Substitute Count
5. VALORANT Minimum Age
6. VALORANT Registration Deadline
7. VALORANT Conduct Penalty
8. VALORANT Sportsmanship/Fair Play
9. VALORANT General In-match Contact
10. VALORANT Unspecified Incident Procedure

## การแก้ Runtime

- เพิ่ม Natural-language signals ทั้งไทยและอังกฤษให้ Taxonomy กลาง
- แยก Registration ออกจาก On-site Check-in
- ให้ Conduct เป็น Facet หลักเมื่อคำถามถามโทษที่เกิดจากพฤติกรรม
- อ่าน Map Pool จาก Multi-topic Source Chunk ได้โดยตรง
- เพิ่ม English Hard Evidence Gate: Localization Overlay ไม่สามารถเอาชนะ Source Coverage ได้
- Evaluator ตรวจเพิ่มว่า Source-gap case ต้องไม่มี Evidence ติดกลับมา

## ผลทดสอบ

### Focused Source-gap

- Thai: 10/10 ผ่าน
- English: 10/10 ผ่าน
- Source-gap safety: ไม่มีการแนบหลักฐานจากหัวข้ออื่น

### Full Competition RAG Regression

| Locale | Passed | Evidence Contract | Answer | Safe No-answer | Clarification | Average | P95 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Thai | 274/274 | 274/274 | 230 | 42 | 2 | 0.2497s | 0.5098s | 2.3245s |
| English | 274/274 | 274/274 | 230 | 42 | 2 | 0.0828s | 0.1625s | 1.3705s |

Thai detail: `reports/competition_rules_rag_eval/competition_rules_rag_eval_20260922_182439.json`

English detail: `reports/competition_rules_rag_eval/competition_rules_rag_eval_20260922_182526.json`

English run ใช้ Draft Preview เฉพาะการประเมินข้อความแปลที่ยังรอ Human Approval ไม่ถือว่าเป็น Production-approved localization

## Acceptance

- [x] คำถาม Source Gap ใหม่ผ่าน 20/20
- [x] ไม่มี Source Gap case ยืม Evidence ผิดหัวข้อ
- [x] Full Thai ผ่าน 274/274
- [x] Full English ผ่าน 274/274
- [x] ไม่มี Case เกิน 20 วินาที
- [x] Map Pool ที่มี Source จริงตอบได้แทนการปฏิเสธ
- [x] Stored corpus และ manifest สร้างซ้ำได้

## วิธีเพิ่มข้อมูลภายหลัง

เมื่อได้รับเอกสารทางการสำหรับ Source Gap ใด:

1. เพิ่มข้อความลง Active Rulebook Source
2. ระบุ Content ID, Rulebook ID, Facet, Version และ Source URL
3. เปลี่ยน Coverage Manifest จาก `unsupported_in_active_source` เป็น `supported_in_active_source`
4. เปลี่ยน Negative Gold ของหัวข้อนั้นเป็น Answerable Gold พร้อม Allowed Evidence IDs
5. สร้าง corpus ใหม่และรัน Focused + Full Regression ทั้งสองภาษา
6. ห้ามแก้ Expected Result ให้ผ่านโดยที่ Source ยังไม่มีข้อความพิสูจน์
