# 12 — Full Pipeline: ทำ AI Chatbot สำหรับเว็บ PSU Esports Studio - Phuket

โฟลเดอร์นี้คือแผนละเอียดสำหรับทำ AI Chatbot ของเว็บ:

- https://esports.phuket.psu.ac.th/home
- https://esports.computing.psu.ac.th/

เป้าหมายคือทำบอทที่ตอบเรื่อง:

- กฎการจอง
- วิธีจอง
- เช็คอิน / ยกเลิก / ค่าปรับ
- รายชื่ออุปกรณ์และเกม
- ข้อมูลการแข่งขัน
- กิจกรรมและข่าว
- ความรู้เกี่ยวกับอีสปอร์ต
- ช่องทางติดต่อ

---

## อ่านไฟล์ตามลำดับนี้

1. `01_ต้องรู้อะไรบ้างก่อนทำ.md`
2. `02_Full_Pipeline_ภาพรวมทั้งหมด.md`
3. `03_Data_Pipeline_ดึงเว็บถึงข้อมูลพร้อมใช้.md`
4. `04_RAG_Pipeline_ค้นข้อมูลและให้_LLM_ตอบ.md`
5. `05_Chatbot_Behavior_ออกแบบพฤติกรรมบอท.md`
6. `06_Evaluation_Pipeline_วัดผลบอท.md`
7. `07_Production_Pipeline_ทำให้ใช้งานจริง.md`
8. `08_Roadmap_ลงมือทำทีละเฟส.md`
9. `09_ข้อควรระวังและปัญหาที่เจอบ่อย.md`
10. `10_เลือกโมเดล_LLM_Embedding_สำหรับโปรเจกต์นี้.md`
11. `11_กลยุทธ์ลด_Cost_Local_vs_API_ในเวลา_2เดือน.md`

---

## Pipeline สั้นที่สุด

```text
เว็บ PSU Esports
-> scrape ข้อมูล
-> clean / chunk / classify
-> curated facts
-> embedding
-> vector database
-> retrieve
-> rerank/filter
-> build prompt
-> LLM ตอบ
-> แสดง citation
-> log / evaluate / update
```

---

## โฟลเดอร์ที่เกี่ยวข้อง

โฟลเดอร์ข้อมูลและ starter kit เดิม:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\11_PSU_Esports_AI_ChatBot
```

โฟลเดอร์นี้:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\12_PSU_Esports_AI_ChatBot_Full_Pipeline
```

ใช้โฟลเดอร์ `11` เป็นข้อมูลและ starter code  
ใช้โฟลเดอร์ `12` เป็นแผนละเอียดและคู่มือการทำงาน

---

## สรุปว่าต้องทำอะไรบ้าง

1. เตรียมข้อมูลจากเว็บ
2. แยกข้อมูลเป็นหมวด
3. ทำ curated facts สำหรับข้อมูลสำคัญ
4. สร้าง vector index
5. ทำ retriever
6. ทำ prompt
7. ต่อ LLM
8. ทำ UI chatbot
9. ทำ evaluation
10. deploy
11. monitor
12. อัปเดตข้อมูลเป็นรอบ ๆ

---

## ถ้าจะเริ่มทันที

เริ่มจากอ่าน:

```text
08_Roadmap_ลงมือทำทีละเฟส.md
```

แล้วทำตาม Phase 1 ก่อน
