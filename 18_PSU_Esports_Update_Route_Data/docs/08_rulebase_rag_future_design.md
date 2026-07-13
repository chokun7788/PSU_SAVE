# Rule Base / Calculator / RAG Design

แนวทางนี้เน้นให้ Chatbot ตอบเร็ว แม่น และยังแก้ข้อมูลในอนาคตได้ง่าย โดยไม่เอาทุกอย่างไปไว้ใน LLM

## หลักใหญ่

คำตอบควรเป็นแบบ answer-first:

1. ตอบสิ่งที่ผู้ใช้ถามก่อน เช่น ราคา เวลา ส่วนต่าง หรือกฎสรุป
2. ค่อยใส่รายละเอียด เงื่อนไข และข้อยกเว้น
3. ปิดท้ายด้วยแหล่งข้อมูลเมื่อมี

ตัวอย่าง:

```text
วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียด:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning เป็น Maintenance*
แหล่งข้อมูล: ...
```

## Route ที่แนะนำ

ลำดับควรเป็น:

1. `guard/no_answer`
2. `direct_faq_rule`
3. `calculator`
4. `structured_lookup`
5. `rag_retrieval`
6. `llm_rewrite`
7. `clarify_or_no_answer`

เหตุผล:

- คำถามที่ห้ามตอบ/ไม่มีข้อมูลควรออกเร็ว เพื่อกัน AI มั่ว
- FAQ ที่เป็นข้อเท็จจริงตายตัวควรตอบจาก rule/template
- ราคา เวลา ค่าปรับ และจำนวน session ควรใช้ calculator หรือ structured lookup
- RAG ใช้กับข้อมูลยาว/เอกสาร/รายละเอียดที่ไม่ได้เป็นสูตรตายตัว
- LLM ใช้เรียบเรียง ไม่ควรใช้เป็นแหล่งความจริงหลัก

## Rule Base ตอนนี้

ในโฟลเดอร์ `data/rules` มี 8 กลุ่มหลัก:

- `reservation_rules.jsonl` กฎการจอง เช็คอิน ชำระเงิน ยกเลิก booking
- `penalty_rules.jsonl` ค่าปรับและความเสียหาย
- `misc_rules.jsonl` กฎทั่วไป เช่น อาหาร เครื่องดื่ม เสียงดัง การพนัน อาวุธ
- `games_rules.jsonl` เกมของ PC, PS5, Switch, VR, Cockpit
- `equipment_rules.jsonl` อุปกรณ์/PC Zone
- `contact_rules.jsonl` email, Facebook, ที่ตั้ง, เบอร์ติดต่อ
- `overview_rules.jsonl` ภาพรวมศูนย์/พันธกิจ
- `no_answer_rules.jsonl` สิ่งที่ไม่มีข้อมูลหรือไม่ใช่บริการของศูนย์

## สิ่งที่ควรแยกออกจาก Rule Base

ไม่ควรใส่ทุกอย่างเป็น if/else เดียวกัน เพราะจะดูแลยาก

ควรแยกเป็น:

- `rules`: กฎที่เป็นข้อความแน่นอน
- `service_fee`: ตารางราคาและ calculator
- `schedule`: เวลาเปิดปิดและ maintenance timeline
- `reservation_policy`: เงื่อนไขจอง/ยกเลิก/เช็คอิน/ชำระเงิน
- `games_catalog`: รายการเกมตาม platform
- `equipment_catalog`: รายการเครื่องและอุปกรณ์
- `no_answer_policy`: คำถามที่ควรปฏิเสธหรือบอกว่าไม่มีข้อมูล
- `rag_documents`: เนื้อหายาวจากเว็บ, PDF, Facebook

## โครงสร้างข้อมูลที่แนะนำ

Rule หนึ่งข้อควรมี:

```json
{
  "id": "rule_checkin_advance",
  "category": "reservation",
  "intent": "checkin_advance_time",
  "patterns": ["เช็คอินล่วงหน้า", "check in how early"],
  "aliases": ["เชคอิน", "check-in"],
  "answer_first_th": "เช็คอินได้ล่วงหน้าสูงสุด 30 นาที",
  "details_th": ["ต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง"],
  "source_url": "https://...",
  "priority": 100,
  "needs_calculation": false
}
```

จุดสำคัญคือแยก `answer_first_th` กับ `details_th` เพื่อบังคับให้ตอบตรงคำถามก่อน

## ควรใช้ Rule Base แบบไหน

แนะนำเป็น hybrid rule:

- Exact keyword/regex สำหรับ intent สำคัญ เช่น `จองล่วงหน้า`, `เช็คอิน`, `ยกเลิก`
- Alias normalization สำหรับคำเหมือน เช่น `นักเรียน มอ`, `นักศึกษา PSU`, `เด็ก มอ`
- Fuzzy เฉพาะ entity ที่ควบคุมได้ เช่น `Nintendo`, `PlayStation`, `Cockpit`, `VR`
- ไม่ใช้ cosine similarity ทั่วทั้ง rule โดยตรง เพราะอาจ match ผิดหมวดได้ง่าย

ถ้าจะใช้ similarity ให้ใช้หลังจาก router แยกหมวดแล้ว เช่น query ถูกจัดเป็น `service_fee` ก่อน แล้วค่อยหา service ที่ใกล้ที่สุด

## Template ที่ควรมี

แต่ละหมวดควรมี response template ต่างกัน:

- ราคา: `ราคา/ผลคำนวณก่อน -> ตารางรายละเอียด -> source`
- เวลา: `ช่วงเวลาที่ถามก่อน -> maintenance/ข้อยกเว้น -> source`
- กฎ: `ทำได้/ทำไม่ได้ก่อน -> เงื่อนไข -> source`
- เกม: `มี/ไม่มีเกมก่อน -> รายชื่อ/แพลตฟอร์ม -> source`
- ไม่พบข้อมูล: `ยังไม่พบข้อมูลที่ยืนยันได้ -> แนะนำติดต่อศูนย์/ขอข้อมูลเพิ่ม`

## ข้อแนะนำสำหรับ MVP

ตอนนี้ควรทำให้ 4 กลุ่มนี้แน่นก่อน:

1. เวลาเปิดปิด/maintenance
2. ราคา/คำนวณค่าบริการ
3. กฎการจอง/ยกเลิก/เช็คอิน/ชำระเงิน
4. เกมและอุปกรณ์ที่มี

หลังจากนั้นค่อยเพิ่ม RAG สำหรับ Facebook/PDF/ข่าว/รายละเอียดกิจกรรม

## ข้อแนะนำสำหรับอนาคต

- เก็บ chat log จริง แล้วเอาคำถามซ้ำไปเพิ่ม rule
- เพิ่ม field `answer_style` เช่น `direct`, `comparison`, `calculation`, `list`, `clarify`
- เพิ่ม test ที่เช็ค “ประโยคแรก” ไม่ใช่แค่ keyword ทั้งคำตอบ
- ให้ admin เพิ่มข้อมูลผ่าน JSON/CSV ง่าย ๆ แล้ว validate ก่อน deploy
- ใช้ RAG เป็น fallback พร้อม threshold ถ้า score ต่ำให้ตอบไม่พบข้อมูลแทน
