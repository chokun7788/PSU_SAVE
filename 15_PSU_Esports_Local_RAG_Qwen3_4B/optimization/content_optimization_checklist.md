# Content Optimization Checklist

ใช้ checklist นี้ก่อนสร้าง vector database

- [ ] มีข้อมูล raw จาก Webscraping
- [ ] copy `section_text.txt` เข้า `data/raw_sections`
- [ ] มี curated facts สำหรับกฎ/การจอง/contact/เกม
- [ ] รัน `scripts/optimize_content.py`
- [ ] ตรวจ `data/processed/optimization_manifest.json`
- [ ] ตรวจว่า category ไม่กระจุกอยู่หมวดเดียว
- [ ] ตรวจว่าภาษาไทยไม่เพี้ยนเป็น `à¸...`
- [ ] ตรวจว่า chunk สำคัญเรื่องกฎ/จองอยู่ใน category ที่ถูก
- [ ] ใช้ `optimized_chunks.jsonl` ใน notebook
- [ ] รัน ground truth อย่างน้อย 10-20 ข้อแรก

---

## สัญญาณว่าต้อง optimize เพิ่ม

- คำถามเรื่องจองแต่ค้นเจอข่าวหรือบทความ
- คำถามเรื่องเกมแต่ค้นเจอหน้า contact
- คำตอบมีข้อมูลมั่วทั้งที่ context ไม่มี
- source ที่แสดงไม่ตรงกับคำถาม
- no-answer ดึง chunk ที่ไม่เกี่ยวมาแล้วโมเดลเดา
- ภาษาไทยใน chunk เพี้ยน

