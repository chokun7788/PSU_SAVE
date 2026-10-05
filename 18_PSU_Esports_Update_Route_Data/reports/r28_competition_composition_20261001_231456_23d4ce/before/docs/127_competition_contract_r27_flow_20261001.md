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
8. ทดสอบซ้ำ fixture, regression เดิม, negative controls ของ grader และ typo ที่รักษาชื่อ/ตัวเลข/negation เพิ่มคำถามใหม่แยกจาก Gold เดิม แล้วระบุให้ชัดว่าชุดที่นำมาแก้เป็น development/regression; unseen traffic ต้องเก็บแยกเมื่อพร้อม
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


## ทบทวน Flow จากผลจริงและปรับวิธีตรวจ

1. ตรวจ oracle ก่อนตีความ failure: เก็บ v1/v2 และ audit การแก้คำแปลเทียบเท่า/เลขหัวข้อ; ห้ามลด requirement เพราะ runtime ยังไม่ผ่าน
2. แยกการระบุ game/facet จาก proposition: อุปกรณ์ของเจ้าหน้าที่กับของผู้เล่น หรือเหตุหยุดกับเวลาอนุญาต ต้องไม่เลือกแทนกัน
3. แยก first line และ full body: ถูกอยู่ท้ายคำตอบไม่ได้แปลว่าประโยคแรกตรงคำถาม; ทุกหน่วย/ข้อยกเว้นต้องอยู่ครบ
4. ตรวจ integration mode กับ answer contract: route ใหม่ต้องผ่าน validator เดิม; อย่าข้าม guard เพื่อเพิ่มคะแนน
5. เพิ่ม real-word/negation tests: score/scope, ตัวเลข 1:55, ชื่อเกม และประโยคปฏิเสธต้องไม่ถูก typo recovery เปลี่ยน
6. เพิ่มคำถามใหม่และคำสำคัญพิมพ์ขาด: กู้ด้วย context + unique candidate + edit budget ไม่ใช้ whole-question alias; ถ้าเกินขอบเขตถามกลับ
7. ใช้ Gold 2,000 จับ broad-query และ multi-topic regression ก่อนขึ้นแพ็กเกจ; original grade และ source grade เป็นคนละคอลัมน์
8. ต้องข้าม worker recycle จริงบน HTTP: sequential ก็เกิด startup gap ได้; เตรียม worker ใหม่ขณะตัวเดิมยังตอบ และสลับเมื่อ ready
9. Unit doubles ต้องบังคับ signature ของ logger: Mock เปล่าไม่จับ missing request_id; ใช้ autospec และตรวจ spawn-failed branch
10. หลัง package acceptance จึงเปลี่ยน 8090 และตรวจ runtime/health/คำถามเดิมอีกครั้ง เก็บ package/PID/log เก่าและปิดเฉพาะตัวทดสอบที่สร้างเอง

ข้อข้างต้นเป็นสิ่งที่ทบทวนจากการตรวจและผลที่เกิดจริง ไม่ใช่การอ้างว่าทุกรอบรันทุกชุดเท่ากัน.

## ผลฉบับใช้งาน r27 verified

| Gate | ผล | ขอบเขต |
| --- | --- | --- |
| Unit/regression | 135/135 | รวม logging signature และ worker recycle race |
| Gold เดิม raw | 1,953/2,000 | เก็บ 47 legacy false failures |
| Gold source-grade | 2,000/2,000 | presence + gates เดิม; ไม่ใช่ completeness ทุกคำตอบ |
| Complete-clause contract TH/EN | 320/320 | 52 topics ×2 locales ×3 forms +8 controls |
| New question/typo | 128/128 | development/regression ไม่ใช่ blind traffic |
| Old propositions / web regression / clarification | 80/80 +36/36 +8/8 | ค่า หน่วย เงื่อนไข ตาราง / flow / missing-game |
| HTTP sequential | 573/573 HTTP200 | สลับ ready worker 2 ครั้ง, 572 cases +1 probe |
| Process recovery | ผ่าน | recycle 24 requests, crash และ timeout |
| หลังขึ้น 8090 | 36/36 +8/8 | health/version ถูกและ worker ready |

เวลา clarification หลังขึ้นเว็บ median 0.07035s/max 0.1094s สำหรับชุด 8 ครั้งนี้ ไม่ใช่คำรับประกันทุกคำถาม.

### Flow ถัดไปเมื่อมีเคสใหม่

เก็บ raw question + locale/history + answer/trace/เวลา → แยก transport/runtime/oracle/route/proposition/first-line/typo/source-gap → ตรวจต้นฉบับและคำแปล → freeze expected clauses พร้อม negative assertions → แก้ชั้นที่เป็นต้นเหตุ → rerun ชุดที่เกี่ยวข้องและ full regression เมื่อ routing เปลี่ยน → HTTP/package gate → บันทึกผลทั้งผ่าน/ไม่ผ่านและขอบเขต.

คำถามที่ policy ขัดกันส่งให้ผู้จัดตามรายการด้านบน; คำถามที่ source ไม่มีต้องตอบว่าข้อมูลยังไม่พบ; source-presence pass ไม่ใช้แทน completeness pass. งานเก็บ booking จริงยังเลื่อนตามคำขอเดิม.
