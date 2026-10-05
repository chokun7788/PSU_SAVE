# ผลส่งมอบ r25: รูปแบบคำตอบกติกาการแข่งขัน

วันที่ 1 ตุลาคม 2026 — เว็บใช้งาน: http://127.0.0.1:8090/

## สิ่งที่แก้แล้ว

- เลือกข้อย่อยที่ตรงคำถามก่อนชื่อหัวเอกสาร ไทย/อังกฤษ
- แยก Technical/Tactical/Emergency และคำถามการสื่อสาร/โควตา ไม่ยืมค่าจากคนละประเภท
- CS2 penalty table ครบ 9 คู่ โดยรวม continuation s54/s55 พร้อมอ้างอิง
- Tekken การตั้งค่าเกม เข้าเส้นทางกติกาและตอบ 3 rounds / 60 seconds
- English RoV tablet/iPad ตอบข้อห้ามและผลตัดสิทธิ์ในบรรทัดแรก
- VALORANT penalties ครบ 5 ประเภทพร้อมเงื่อนไข ไม่ซ้ำ
- Overview ตรวจแต่ละ clause ก่อนจัดหมวด; เว็บแสดง heading/list/table จริง

## ผลทดสอบ

| รายการ | ผล |
| --- | --- |
| Unit + regression | 103/103 ผ่าน |
| HTTP บนเว็บ 8090 หลังสลับแพ็กเกจ | 30/30 ผ่าน เปิด LLM/semantic แบบเว็บ |
| Ground Truth เดิม 1000 ไทย + 1000 อังกฤษ ตัวตรวจ r24 | 1953/2000 ผ่าน, 47 ข้อตก source-content matcher |
| ตรวจ 47 ข้อที่ตกกลับจาก literal complete source clause | 47/47 มีข้อความต้นฉบับรองรับ |
| เกณฑ์มีข้อความ source รองรับหลัง review | 2000/2000; ไม่ใช่การตรวจความหมายครบทุก proposition โดยคน |
| DOM และภาพเว็บ | หัวข้อ/list จริง; ตารางไทย/อังกฤษ 9 แถว 2 คอลัมน์; user HTML เป็น text |
| Protected source/Gold/owner/release pointer hashes | 6/6 ตรงเดิม |

HTTP 8090 ใช้เวลาประมาณ 0.060–8.532 วินาทีในรอบนี้ ตัวอย่างคำถามพร้อมคำเกริ่นบางแบบยังใช้ LLM routing และปรับความเร็วได้อีก

## ทำไมตัวตรวจเดิมยังตก

30 ข้อเป็น exact short fact “PlayStation 5 console used” ภายในบรรทัด English ที่รวมหลาย bullet; ตัวตรวจเลือก fragment 7 tokens จึงตรวจข้อสั้นนี้ไม่พบ อีก 17 ข้อเป็นกฎโทษ VALORANT ซึ่งตัวกรองเลือกเฉพาะเลข/คำ modal บางคำและกรองบรรทัดโทษออกก่อนเทียบ ผลดิบและ Gold เดิมยังอยู่ครบ

## ผู้จัดยังต้องยืนยัน

1. Tekken s07 ให้หยุดได้เมื่อทุกคนเห็นพ้องและมีเหตุเหมาะสม เป็นข้อยกเว้นของ s03 ที่ห้ามหยุดหลังเริ่มเกมหรือไม่ ต้องให้กรรมการอนุญาตหรือไม่?
2. หยุดโดยเจตนา/ไม่จำเป็น เสีย Round, Game หรือ Match FT2 ในแต่ละกรณี? ข้อความ “1 รอบ” กับ “ปรับแพ้ทันที” ยังต้องให้ผู้จัดกำหนดขอบเขต

V2 review queue 104 records ยังรอตรวจและยังไม่ได้ activate canonical policy จากการแก้ format รอบนี้ คำตอบอังกฤษใช้ release ที่ระบบตรวจ hash แล้ว ไม่ถือเป็นหลักฐานการอนุมัติจากเจ้าของ

## เอกสารและหลักฐาน

- Flow ฉบับละเอียด: `docs/125_competition_format_r25_flow_20261001.md`
- Final verification: `final_verification.json`
- ตัวตรวจเดิม: `full_r25_B_summary.json`, `full_r25_B_details.jsonl`
- วิเคราะห์ข้อที่ตก: `full_r25_B_failure_groups.json`, `full_r25_B_source_presence_review.json`
- เว็บจริง: `http_ready_8090.json`; Browser evidence: `ui_verification.json`
- สำเนาโค้ดก่อน/หลัง: `before/`, `after/`; protected hashes: `protected_data_verification.json`

Package ใหม่อยู่ที่ `owner_local_delivery_20261001_competition_format_r25_final/PSU_Esports_Chatbot_Local`; package และ log เก่าคงอยู่ หยุดเฉพาะ launcher เว็บที่ตรวจว่า Codex เปิดเอง ไม่สั่งหยุด Dashboard ของเจ้าของหรือ Ollama
