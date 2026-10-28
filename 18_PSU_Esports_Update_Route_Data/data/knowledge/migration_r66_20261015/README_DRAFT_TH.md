# ร่าง Format กลาง R66 — ยังไม่เผยแพร่

candidate.sqlite เป็นร่างข้อมูลจริง 588 รายการ: เก็บ 582 รายการเดิม และ PC rates จาก source เดิม 6 รายการ ไม่มี synthetic fixtures ไม่มี approvals และ active release ว่าง ไม่ได้แทนฐานข้อมูลที่ Chatbot ใช้งานอยู่

การแก้คำแปล/ฟิลด์เป็น revision ใหม่พร้อม source lineage เก็บต้นฉบับเดิม วันมีผลหรือกฎที่ไม่ทราบยังเป็น unknown ต้องจัดการ release gates ก่อนเผยแพร่ ไม่เปิด evaluation draft override ใน production

เปิดร่างนี้ด้วยตัวเปิดแยก โดยใช้ runtime ของโปรเจกต์:

```powershell
.\data\knowledge\migration_r66_20261015\Open-R66-Draft.ps1
```

หากเครื่องเลือก Python ไม่ตรง ให้ส่ง -PythonPath เป็น Python 3.12 ตัวเดียวกับที่ใช้เปิด Chatbot ตัวเปิดจะส่งฐานข้อมูลร่างเฉพาะไปยัง Owner editor และคืนค่า environment เดิมเมื่อเปิดเสร็จ ไม่เปลี่ยน default DB ของ launcher หลัก

ถ้าต้องการเปิดร่างนี้ใน Owner editor ให้รันจากโฟลเดอร์โปรเจกต์ด้วย Python environment ของโปรเจกต์:

```powershell
python -m app.knowledge.common.owner_server --db "data/knowledge/migration_r66_20261015/candidate.sqlite" --port 8099
```

เลือกทดสอบร่างเพื่อดูข้อมูลในไฟล์นี้ การทดสอบร่างไม่ใช่การเผยแพร่ ห้ามอ้างว่าไฟล์ชื่อ candidate ได้รับอนุมัติแล้ว

รายงาน Flow และคำถามที่ต้องใช้ข้อมูลจริงเพิ่มเติมอยู่ในโฟลเดอร์งาน R66 ตาม delivery manifest ด้านล่าง โค้ดมี before backups แยกต่างหาก ไม่ได้อัปเดต portable packages หรือ restart Chatbot ที่เปิดค้างโดยอัตโนมัติ
