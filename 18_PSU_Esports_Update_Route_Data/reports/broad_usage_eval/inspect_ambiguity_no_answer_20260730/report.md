# Broad Usage Eval v1

- Generated at: 2026-07-30T17:24:11
- Cases: 25
- Turn checks: 25
- Passed: 18
- Failed: 7
- Pass rate: 0.72
- Total wall sec: 11.768
- Allow LLM: False
- RAG fallback: False

## By Group
- ambiguity_no_answer: 18/25 pass, 7 fail

## By Strategy
- clarification: 6
- fast/rule: 1
- pipeline: 2
- rag/retrieval: 9
- structured: 7

## Common Problems
- missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']: 4
- route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general: 3
- route_category expected ['no_answer', 'games', 'general'], got events_news: 1
- route_category expected ['no_answer', 'games', 'general'], got knowledge: 1
- route_category expected ['no_answer', 'games', 'general'], got overview: 1

## Top Failures

### ANA-006 ambiguity_no_answer
- Question: เครื่องไหนดีที่สุด
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-008 ambiguity_no_answer
- Question: มีอะไรแนะนำไหม
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-015 ambiguity_no_answer
- Question: สรุปคือทำยังไง
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-020 ambiguity_no_answer
- Question: เกม Valorant Mobile มีไหม
- Resolved: -
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_availability_lookup`
- Problems: missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### ANA-021 ambiguity_no_answer
- Question: ขอเบอร์โทรส่วนตัวเจ้าหน้าที่
- Resolved: -
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Problems: route_category expected ['no_answer', 'games', 'general'], got overview, missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี •    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี •    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี •    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •    นายพฤทธิ์ เกษตรสมบูรณ์:...

### ANA-022 ambiguity_no_answer
- Question: ขอข้อมูลที่ไม่ได้อยู่ในเว็บ PSU Esports
- Resolved: -
- Mode: `pipeline:hybrid_guarded_rerank`
- Route: `knowledge/knowledge_lookup`
- Problems: route_category expected ['no_answer', 'games', 'general'], got knowledge, missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

### ANA-023 ambiguity_no_answer
- Question: วันนี้มีข่าว esports อะไรล่าสุด
- Resolved: -
- Mode: `pipeline:rag_direct_curated`
- Route: `events_news/news_lookup`
- Problems: route_category expected ['no_answer', 'games', 'general'], got events_news, missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: เมื่อวันที่ 25 เมษายน 2569 PSU Esports Studio - Phuket จัดการแข่งขัน PSU Phuket CS 2 2026 Tournament ในเกม Counter-Strike 2 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news
