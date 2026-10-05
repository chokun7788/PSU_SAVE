# สรุปผล r26 — 2026-10-01

เปิดใช้รุ่นใหม่ที่ http://127.0.0.1:8090/ โดยใช้แพ็กเกจ `PSU_Esports_Chatbot_Local` ใน `owner_local_delivery_20261001_competition_content_speed_r26_ready`

## สิ่งที่แก้
- VALORANT ประเภทบทลงโทษไทยครบ 5 ประเภท พร้อมเงื่อนไขและ source s11–s15
- typo อังกฤษ tournament แบบเบิ้ล/ขาด/สลับ อาศัย edit distance ที่มีเกมใน registry เป็นบริบท
- รูปแบบแข่งขันเริ่มด้วย 1v1/FT2 ทั้งไทย/อังกฤษ รักษารอบ/เวลาไทยที่มีในส่วนเดียวกัน
- age/pause รายละเอียดที่ไม่มี source ต้อง no_answer; ไม่หยิบข้อใกล้เคียงมาตอบ
- game+facet กติกาชัดข้าม semantic route / LLM intent ซ้ำ แต่ยังตรวจแหล่งข้อมูล
- notice ไทย/อังกฤษสำหรับตัวอักษรซ้ำบอกว่าประมวลผลต่อแล้ว

## ทดสอบและข้อจำกัด
Unit 113/113; เนื้อหา HTTP ไทย/อังกฤษ 80/80; HTTP regression 36/36 เวลา 0.0609–3.4503s

GT รุ่นสุดท้าย ไทย 1000 อังกฤษ 1000 คะแนนดิบ 1953/2000; อีก 47 เป็นข้อจำกัด source-overlap grader (Tekken 30, VALORANT 17) พบ clause เต็มตรง source ใน review แยกครบ 47 จึงยืนยัน source presence 2000/2000 หลัง review แต่ไม่ใช่ semantic correctness ของทุกคำตอบหรือเจ้าของรับรอง

รอบ B เกิด timeout เคสหนึ่ง 719.2584s; replay ผ่าน 1.5759s และรอบสุดท้ายไม่พบ timeout นี้ ต้นเหตุยังยืนยันไม่ได้ เก็บผลเดิมและ trace ไว้ครบ

เวลาเทียบคำเกริ่นใหม่: RoV 7.2289 → 0.3664s, Tekken ประมาณ 2.8 → 0.3s ในชุด benchmark; cache/การเริ่มต้น/ประเภทคำถามมีผลต่อเวลา

## งานที่รอเจ้าของ
Tekken: s07 เป็นข้อยกเว้น s03 เรื่อง pause หรือไม่ ต้องอนุญาตกรรมการหรือไม่? แต่ละกรณีเสีย Round, Game หรือ FT2 Match? V2 104 รายการและคำแปลอังกฤษยังไม่ได้รับรองจากผู้จัด

## ไฟล์
Flow: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\docs\126_competition_content_speed_r26_flow_20261001.md`
วิเคราะห์ละเอียด: `CAUSE_ANALYSIS_TH.md`
ผลครบพร้อม hash: `FINAL_VERIFICATION.json`

รักษาโค้ดที่ยังไม่บันทึก Git, logs, Gold, policy sources, review queue, ตารางเจ้าของ และแพ็กเกจเก่าทั้งหมด มีสำเนาก่อนแก้/หลังแก้ ไม่มี reset/clean/commit
