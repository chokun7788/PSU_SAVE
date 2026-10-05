# Flow r27 — ตรวจเนื้อหากติกาและการให้คะแนน

## ขอบเขตและหลักฐาน
รักษา source, Gold 2,000 ข้อ, owner schedule, English release, V2 review และ log เก่า เก็บ snapshot ก่อนแก้ แปลอังกฤษใช้ overlay ที่ hash ตรงกับต้นฉบับเท่านั้น ข้อที่ต้นฉบับขัดกันไม่ตัดสินนโยบายแทนผู้จัด

## ลำดับทำงาน
1. ตรวจแหล่ง 104 chunks พร้อมคำแปล จัดข้อกำหนดที่ทดสอบตาม game → facet → proposition
2. ตรึง fixture รายละเอียดใหม่ 320 ข้อ: 104 ประเด็นสองภาษา × 3 รูปคำถาม และ 8 safe controls ข้อคาดหวังเป็น clause ต้นฉบับเต็ม ไม่ดึงจาก runtime selector
3. วัด baseline r26 ก่อนแก้ แยก outcome/route, หลักฐานต่างเกม, missing clause และ first line ไม่ตรงคำถาม
4. แก้ grader ที่ปฏิเสธคำอังกฤษสั้นและ penalty: ตรวจ atomic clause เต็ม แยกผล source presence จาก completeness ไม่เปลี่ยนคะแนนดิบหรือ Gold
5. ตรวจความผิดของ fixture กับ source ก่อนแก้โค้ด แก้เฉพาะการเลือก/จัดแสดง clause ที่มีหลักฐาน ค่า หน่วย ข้อห้าม เงื่อนไข และข้อยกเว้นต้องคงครบ
6. ข้อมูลย่อยไม่พบ → no_answer; เกมไม่ระบุ → clarification; เกมไม่รองรับ → no_answer; ต้นฉบับขัดกัน → แจ้งข้อมูลขัดกัน ไม่สร้างข้อสรุปใหม่
7. เพิ่ม timing ตั้งแต่ locale, cue recovery, canonical preflight พร้อม elapsed ของช่วงก่อน split เพื่อหาตำแหน่ง wall gap การวัดไม่ใช่ข้อพิสูจน์สาเหตุ timeout ครั้งเก่า
8. ทดสอบซ้ำ fixture, regression เดิม, negative controls ของ grader และ typo ที่รักษาชื่อ/ตัวเลข/negation เพิ่มคำถาม holdout ที่ไม่ใช้ในการแก้
9. รัน Gold เดิม 2,000 ข้อ เก็บคะแนนเดิมและ atomic-source grade แยก อีกตารางเป็นผล completeness fixture
10. สร้าง package ใหม่ ทดสอบ HTTP ใน package จริง แล้วจึงเปลี่ยนเฉพาะเว็บที่เราเปิด 8090 เก็บ launcher/log เก่า

## เกณฑ์ตรวจคำตอบ
- Route/status/source เป้าหมายถูก ไม่เท่ากับเนื้อหาถูก
- Presence: clause เต็มจาก source อย่างน้อยหนึ่งข้อ คำอ้างอิงหรือ heading ไม่นับ
- Completeness: fixture ต้องมีทุก clause ที่ระบุ; การตัด unless/เว้นแต่ หรือหน่วยนาทีเป็นวินาทีต้องไม่ผ่าน
- First line: ตอบ proposition ที่ถามก่อนรายละเอียด ข้อมูลถูกอยู่ท้ายคำตอบยังไม่พอ
- ภาษาอังกฤษตรวจจาก hash overlay และคู่ข้อกำหนดไทย ไม่ใช่การรับรองการแปลอย่างเป็นทางการ
- ชุด typo นี้เป็น synthetic bounded cases ไม่ใช่ความแม่นยำกับทุกการพิมพ์ผิด

## สิ่งที่รอผู้จัด
1. Tekken s03 ห้าม pause ทุกเหตุผล แต่ s07 อนุญาตบางกรณี: s07 เป็นข้อยกเว้นหรือไม่? กรณีใดต้องขอกรรมการก่อน? แต่ละโทษเสีย Round/Game/FT2 Match อะไร?
2. V2 review 104 รายการยังไม่เผยแพร่ คำแปลอังกฤษที่ตรวจ source แล้วไม่ได้แปลว่าผู้จัดรับรอง

## รายงานผล
เติมผลจริงหลังแต่ละรอบ พร้อมแยก oracle error, runtime error, unresolved/source gap และข้อจำกัด ไม่มีการนับการแก้ flow ที่ไม่ได้ตรวจจริงเป็นรอบทดสอบ
