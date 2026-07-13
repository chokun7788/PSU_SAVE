# Experimental RAG Fallback Implementation - 2026-07-06

## สรุป

เพิ่มโหมดทดลองสำหรับคำถามที่เดิมจะถูกปฏิเสธด้วย no-answer/guard no-answer ให้ลองตอบด้วยข้อมูลที่เกี่ยวข้องจาก RAG หรือ LLM แทน โดยยังคุมไม่ให้ระบบเดาข้อมูลบริการที่ไม่มีหลักฐานยืนยัน

โหมดนี้เปิดผ่าน payload/API flag:

- `experimental_rag_fallback`
- `experimental_allow_llm`

หน้าเว็บถูกตั้งให้ส่ง flag ทดลองไปกับ `/api/chat` แล้ว เพื่อให้ลองพฤติกรรมใหม่จาก UI ได้ทันทีหลัง deploy จากโฟลเดอร์ 20

## ไฟล์ที่แก้

- `app/pipeline/experimental_fallback.py`
- `app/pipeline/engine.py`
- `app/pipeline/router.py`
- `app/web_api/server.py`
- `web_chat/app.js`
- `20_PSU_Esports_Vercel_Deploy/api/chat.py`
- `20_PSU_Esports_Vercel_Deploy/app.js`
- `20_PSU_Esports_Vercel_Deploy/web_chat/app.js`

## พฤติกรรมที่เพิ่ม

กรณีที่ strict mode เดิมจะตอบ no-answer ระบบทดลองจะพยายามตอบแบบเกี่ยวข้องแทน เช่น:

- `มีให้เช่าจอไปบ้านไหม`
  - strict: `pipeline:guard_no_answer`
  - experimental: บอกข้อมูลที่ยืนยันได้ว่าศูนย์มี Gaming Monitor สำหรับใช้งานใน PC Zone และบอกว่ายังไม่มีข้อมูลยืนยันเรื่องเช่า/ยืมออกนอกสถานที่
- `รับซ่อมคอมส่วนตัวไหม`
  - strict: `pipeline:guard_no_answer`
  - experimental: บอกข้อมูลที่ยืนยันได้ว่าศูนย์มี Gaming PC สำหรับใช้งานใน PC Zone และบอกว่ายังไม่มีข้อมูลยืนยันเรื่องรับซ่อมคอมส่วนตัว
- `อยากจัดวันเกิดที่ศูนย์ได้ไหม`
  - strict: `pipeline:no_answer`
  - experimental: บอกข้อมูลที่ยืนยันได้ว่าศูนย์มีระบบจองเข้าใช้บริการเป็นรอบเวลา และบอกว่ายังไม่มีข้อมูลยืนยันเรื่องจัดงานวันเกิด/ปาร์ตี้/อีเวนต์ส่วนตัว
- `มีคอร์สสอนเล่น Valorant ไหม`
  - strict: `pipeline:guard_no_answer`
  - experimental: บอกข้อมูลที่ยืนยันได้ว่า VALORANT มีให้เล่นใน PC Zone และยังไม่มีข้อมูลยืนยันเรื่องคอร์สสอนเล่น

## สิ่งที่ยังตั้งใจคงไว้

ไม่ได้ตัด no-answer ทิ้งทั้งหมด เพราะจากการทดสอบ ถ้าปล่อย RAG ตอบทุกอย่างจะมีโอกาสดึง context ที่ไม่เกี่ยวข้อง เช่นคำถามขาย/ซื้ออุปกรณ์ หรือเกมที่ไม่มีใน catalog

จึงคง fast path ที่ปลอดภัยไว้ เช่น:

- `อยากเล่น Pokemon` ยังตอบว่าไม่พบ Pokemon ในรายการเกมที่ยืนยันได้
- `อยากซื้อคีย์บอร์ดจากศูนย์` ยังตอบจาก category rule ว่าไม่มีข้อมูลขายคีย์บอร์ด แต่มีข้อมูลอุปกรณ์สำหรับใช้งานในศูนย์
- คำถามแนะนำเกม/โซนที่มีข้อมูลจริงยังใช้ related guidance fast path เหมือนเดิม

## LLM

รองรับ LLM ผ่าน Ollama แบบ optional:

- `OLLAMA_URL` ค่าเริ่มต้น `http://127.0.0.1:11434`
- `PSU_CHATBOT_OLLAMA_MODEL` ค่าเริ่มต้น `qwen2.5:3b`
- `PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC` ค่าเริ่มต้น `1.5`

ถ้าเปิด `experimental_allow_llm=true` แล้ว local มี Ollama ระบบสามารถลองเรียก LLM ใน fallback path ได้ แต่ถ้า fallback แบบ soft-related ตอบได้ก่อน จะไม่เรียก LLM เพราะคำตอบแบบมีกรอบข้อมูลจริงปลอดภัยกว่า

บน Vercel โดยปกติไม่มี Ollama local ให้เรียก ถ้ารู้สึกว่า API ช้าจาก timeout ให้เปลี่ยน `experimentalAllowLlm` ใน `app.js` เป็น `false` ก่อน deploy

## ผลทดสอบ

โฟลเดอร์ 18:

```powershell
python -m py_compile app\pipeline\engine.py app\pipeline\experimental_fallback.py app\pipeline\router.py
python tools\validate_update.py
python tests\smoke_test_answer_pipeline.py
python tests\smoke_test_fast_runtime.py
python tools\run_ground_truth_pipeline_eval.py --label experimental_rag_fallback_gt360_20260706
python tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl --label experimental_rag_fallback_comp_v2_20260706
```

ผล:

- compile: PASS
- validate: PASS
- smoke answer pipeline: PASS
- smoke fast runtime: PASS
- GT360: PASS 360/360
- Competition challenger v2: PASS 369/369

รายงาน ad hoc:

- `reports/ad_hoc_pipeline_results_experimental_rag_fallback_fix2_20260706.md`
- `reports/ad_hoc_pipeline_results_experimental_rag_fallback_fix2_20260706.jsonl`

โฟลเดอร์ 20:

```powershell
python -m py_compile app\pipeline\engine.py app\pipeline\experimental_fallback.py app\pipeline\router.py api\chat.py api\calendar.py api\health.py
```

ผล:

- compile: PASS
- `/api/chat` smoke experimental fallback: PASS
- `/api/chat` smoke strict no-answer: PASS

ตัวอย่างผล API ในโฟลเดอร์ 20:

```text
experimental_mode pipeline:experimental_soft_related_fallback
experimental_first_line โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้ตอนนี้คือศูนย์มี Gaming Monitor 10 Units สำหรับใช้งานใน PC Zone ภายในศูนย์
strict_mode pipeline:guard_no_answer
strict_first_line ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

## สถานะหลังจบงาน

- โค้ดหลักในโฟลเดอร์ 18 อัปเดตแล้ว
- ซิงก์ไปโฟลเดอร์ deploy 20 แล้ว
- ยังไม่ได้ deploy production ตามคำสั่งผู้ใช้
- หลังผู้ใช้กด deploy เอง ควรทดสอบ production API ด้วยคำถาม:
  - `มีให้เช่าจอไปบ้านไหม`
  - `รับซ่อมคอมส่วนตัวไหม`
  - `อยากจัดวันเกิดที่ศูนย์ได้ไหม`
  - `มีคอร์สสอนเล่น Valorant ไหม`
