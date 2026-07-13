# Handoff Context สำหรับแชทใหม่

ไฟล์นี้คือบริบทเต็มของงาน PSU Esports Chatbot ตั้งแต่แนวคิดจนถึงสถานะล่าสุด เพื่อให้ AI/Codex ตัวใหม่อ่านแล้วทำงานต่อได้โดยไม่ต้องไล่ conversation เก่า

## บทบาทของโปรเจกต์

โปรเจกต์นี้คือการทำ AI Chatbot สำหรับเว็บไซต์ PSU Esports Studio - Phuket โดยเริ่มจากข้อมูลในเว็บ:

```text
https://esports.phuket.psu.ac.th/
https://esports.phuket.psu.ac.th/home
https://esports.phuket.psu.ac.th/Services/our-games
https://esports.computing.psu.ac.th/reservation
```

เป้าหมายคือให้ผู้ใช้ทั่วไปหรือลูกค้าถามข้อมูลเกี่ยวกับศูนย์ได้ เช่น:

- ศูนย์คืออะไร
- เปิดปิดกี่โมง
- วันนี้เปิดไหม
- จองยังไง
- ต้องเช็คอินล่วงหน้ากี่นาที
- ราคา PS5/VR/Cockpit/Nintendo เท่าไหร่
- นักศึกษา PSU เล่นฟรีไหม
- นักศึกษาต่างมหาวิทยาลัยคิดราคาเท่าไหร่
- VR เล่นเกมอะไรได้บ้าง
- Cockpit คืออะไร
- เกม Minecraft/Roblox มีไหม
- กติกาแข่ง RoV/CS2/VALORANT/Tekken เป็นยังไง

## ข้อกำหนดจากผู้ใช้

ข้อกำหนดที่คุยกันไว้:

- ต้องการ local เป็นหลัก ฟรีเป็นหลัก
- ไม่อยากใช้ API LLM แบบเสียเงินถ้าไม่จำเป็น
- มีเวลาฝึกงานประมาณ 2 เดือน ตั้งแต่ 29 มิถุนายน 2026 ถึง 31 สิงหาคม 2026
- ต้องทำ MVP ก่อน
- ต้องทำ log รายวันว่าทำอะไรไปบ้าง
- ควรติดตั้งผ่าน Docker ได้ในอนาคต เพราะระบบของมหาวิทยาลัยมักใช้ Docker
- ตอน demo รัน local เครื่องตัวเองได้
- ถ้า deploy จริงอาจใช้ cloud ฟรี/นักศึกษา หรือ Vercel สำหรับ frontend/API เบา ๆ
- รองรับภาษาไทยและอังกฤษ
- เน้นตอบ FAQ ก่อน
- Phase 2 ค่อยทำ action เช่น จอง/ยกเลิก/เช็คสถานะ
- ข้อมูลเริ่มต้นมาจาก web scraping, PDF, txt, และข้อมูลที่เพิ่มเอง
- User input เริ่มจาก text ก่อน, image/PDF/voice เก็บไว้ phase ต่อไป

## สเปคเครื่องที่เคยให้มา

เครื่องศูนย์หรือเครื่องที่คาดว่าจะใช้:

- รุ่น: MSI MAG H610 Infinite S3 14
- CPU: Intel Core i5-14400
- RAM: 32 GB DDR5 จากภาพ CPU-Z ล่าสุด
- GPU: NVIDIA GeForce RTX 5060, VRAM ประมาณ 8 GB
- Mainboard: MSI PRO H610M-G

สรุปผลต่อโมเดล:

- สามารถรัน local LLM ขนาด 3B-4B quantized ได้
- ถ้าใช้ 7B อาจพอได้แต่ต้องระวัง RAM/VRAM/latency
- สำหรับ production บน Vercel ไม่ควรรัน local LLM เพราะ serverless ไม่เหมาะ
- ถ้าจะใช้ LLM จริง ควรแยก backend ไปเครื่องศูนย์/VPS/Cloud แล้วให้เว็บเรียก API

## Model ที่คุยกันไว้

ตอนแรกผู้ใช้เข้าใจว่าต้องโหลดโมเดลมา train แล้วโมเดลจะจำข้อมูลไปเลย แต่ได้อธิบายแล้วว่า:

- RAG ไม่ใช่การ train โมเดลให้จำถาวร
- โมเดลไม่จำความรู้ใหม่เองถ้าไม่ได้ fine-tune
- ความรู้ของระบบมาจากไฟล์ data/index/vector/rulebase ที่โหลดทุกครั้ง
- ถ้าปิดโปรแกรม โมเดลไม่ได้ลืม แต่ context ของ session หาย
- ฐานข้อมูล/ไฟล์ JSONL/Vector index ยังอยู่บนดิสก์และโหลดมาใช้ใหม่ได้

โมเดลที่คุยกัน:

- Qwen3 4B เป็นตัวที่ผู้ใช้สนใจ
- Qwen2.5:3b ถูกใช้ใน notebook บางช่วงเพื่อทดลองตอบ RAG/LLM
- มีโฟลเดอร์ทดลอง Qwen 3.5/4B hybrid RAG ที่ `19_PSU_Esports_Qwen35_Hybrid_RAG`

แนวทางแนะนำปัจจุบัน:

- MVP/production บน Vercel ใช้ rulebase + calculator + RAG-lite + fact cards ก่อน
- Local demo ถ้าจะใช้ LLM ให้ใช้ Qwen ขนาด 3B-4B quantized ผ่าน Ollama
- LLM ควรเป็น fallback สำหรับเรียบเรียงหรือคำถามกว้าง ไม่ควรให้เดาข้อมูลสำคัญเอง

## โฟลเดอร์หลักของงาน

โฟลเดอร์ทั้งหมดอยู่ใต้:

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

โฟลเดอร์สำคัญ:

```text
15_PSU_Esports_Local_RAG_Qwen3_4B
17_PSU_Esports_Daily_Logs
18_PSU_Esports_Update_Route_Data
19_PSU_Esports_Qwen35_Hybrid_RAG
20_PSU_Esports_Vercel_Deploy
21_PSU_Esports_Handoff_Summary_20260705
```

ความหมาย:

- `15` คือ RAG local/Qwen notebook รุ่นแรกและ Ground Truth 360
- `17` คือ daily logs
- `18` คือ code/data/pipeline หลักที่แก้ล่าสุด
- `19` คือทดลอง hybrid RAG/LLM/Qwen 3.5-4B
- `20` คือ package สำหรับ deploy Vercel
- `21` คือ summary handoff ชุดนี้

## สถานะ runtime ปัจจุบัน

คำตอบจริงใน production ตอนนี้มาจาก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\runtime\fast_answer.py
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\engine.py
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\router.py
```

ไม่ใช่โมเดล LLM เป็นหลัก

ระบบเลือกตอบด้วย:

- deterministic calculator สำหรับราคา
- fast path สำหรับเวลา/กฎ/เกม/อุปกรณ์
- competition fact cards สำหรับกติกาแข่ง
- curated RAG-lite สำหรับข้อมูลที่มีใน curated JSONL
- guard/no-answer สำหรับคำถามที่ไม่มีข้อมูลจริง

## เหตุผลที่ระบบเร็วมาก

หลายคำถามตอบใน 0.004-0.04 วินาที เพราะ:

- ไม่เรียก LLM
- ไม่โหลดโมเดล
- ไม่ทำ vector search หนัก ๆ
- ใช้ normalize/entity/router แล้วตอบจาก data structure และ rule/fact card โดยตรง

นี่ไม่ใช่ข้อเสียถ้าคำถามเป็น FAQ/ข้อมูลตายตัว เพราะยิ่ง deterministic ยิ่งคุมคำตอบได้ดี

แต่ข้อเสียคือ:

- ถ้าคำถามหลุด pattern อาจไม่ตอบ
- ต้องคอยเพิ่ม synonym/alias/route guard
- ถ้าอยากตอบคำถามภาษาธรรมชาติยืดหยุ่นมากขึ้น ต้องเพิ่ม RAG/LLM fallback ที่คุม hallucination ดี ๆ

## ข้อมูลที่มีในระบบ

ข้อมูลหลัก:

- `data/curated/curated_facts.jsonl`: 42 แถว
- `data/curated/curated_competition_rules.jsonl`: 104 แถว
- `data/curated/equipment_item_details.jsonl`: 16 แถว
- `data/curated/game_item_details.jsonl`: 36 แถว
- `data/competition_rules/competition_rule_documents.jsonl`: 4 เอกสาร
- `data/competition_rules/competition_rule_chunks.jsonl`: 104 chunks
- `data/competition_rules/competition_rule_fact_cards.jsonl`: 19 fact cards หลัก
- `data/rules/*.jsonl`: rulebase หลายหมวด
- `data/calendar/service_closures.jsonl`: วันปิดพิเศษ

Ground Truth:

- GT360: `15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl`
- Competition v1 228: `18...\data\ground_truth\ground_truth_competition_rules_v1_228.jsonl`
- Competition challenger v2 369: `18...\data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl`

## Production deployment ล่าสุด

Production:

```text
https://psu-esports-chatbot.vercel.app
```

Deploy folder:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

Deploy log ล่าสุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\deploy_stdout_equipment_game_catalog_fix5_20260704.txt
```

Deploy inspect:

```text
https://vercel.com/chokuns-projects-908117b8/psu-esports-chatbot/3iHJehurdZdYCDS7ZtTH7cBbZ1E5
```

## สิ่งที่ควรระวังสำหรับ AI ตัวใหม่

อย่าเข้าใจผิดว่า:

- ระบบ production ใช้ Qwen ตอบทุกคำถาม
- ข้อมูลถูก train เข้าโมเดลแล้ว
- Vercel รัน local LLM ได้
- Ground Truth PASS 100% แปลว่าใช้งานจริงไม่มีปัญหา
- ตัวตรวจ keyword เพียงอย่างเดียวเพียงพอ

สิ่งที่ถูกต้องคือ:

- Production ตอนนี้เป็น rulebase/RAG-lite/fact-card เป็นหลัก
- LLM เป็น phase ทดลองและยังไม่ใช่ตัวหลักบนเว็บ deploy
- Data อยู่ใน JSONL และ Python code
- ต้องเพิ่ม data และ route guard ต่อเมื่อเจอคำถามใหม่
- ควรอ่านคำตอบจริงด้วยคนเสมอ โดยเฉพาะคำถามที่เสี่ยงทำให้ลูกค้าเข้าใจผิด

