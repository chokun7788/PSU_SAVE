# Guarded Vector Retrieval 2026-07-08

## เป้าหมาย

ลดอาการ hallucination / ดึงข้อมูลคนละบริบท โดยเฉพาะคำถามเกมที่ผู้ใช้พิมพ์ชื่อไม่ครบหรือพิมพ์ผิด เช่น `Resident`, `residen`, `final fan`, และป้องกันเคสชื่อเกมมั่วอย่าง `abcxyz` ไม่ให้ไปดึงเกมอื่นมาตอบ

## สิ่งที่เพิ่ม

- เพิ่ม `app/pipeline/vector_retrieval.py`
  - ทำ local hybrid vector index แบบไม่เพิ่ม dependency หนัก
  - backend: `local_hash_char_ngram_v1`
  - ใช้ word token + char n-gram hashing เป็น sparse vector
  - มี guard ตาม category, route intent, entity score และ similarity score
- เพิ่ม `tools/build_vector_index.py`
  - generate index ไปที่ `data/vector/psu_hybrid_vector_index.json`
  - index ล่าสุดมี 247 documents
- ต่อ pipeline ใน `app/pipeline/engine.py`
  - deterministic/rulebase ยังมาก่อน
  - curated lexical ยังทำงานตามเดิม
  - ถ้า curated ไม่ผ่าน จึงใช้ `guarded_vector_direct`
  - ถ้า deterministic ตอบ unknown game เช่น `games_unknown_fast_path` จะลอง guarded vector override ก่อนตอบไม่พบ
- ปรับ `app/pipeline/experimental_fallback.py`
  - ใช้ guarded vector ก่อน
  - ยกเลิก broad retrieval สำหรับ `general/no_answer`
  - คำถามเกมแบบระบุชื่อ/วิธีเล่นใช้ vector-only หลัง guard ถ้าไม่ผ่านให้ no-context
- ปรับ `app/pipeline/retrieval.py`
  - เพิ่ม entity guard ให้ curated lexical สำหรับคำถาม `เกมคืออะไร/วิธีเล่น`
  - ถ้าไม่พบชื่อเกมหรือชื่อบางส่วนใน row เกม จะไม่ใช้ row นั้นตอบ
- ปรับ `app/runtime/fast_answer.py`
  - เพิ่ม `Resident` เป็น family alias ของ `Resident Evil`
  - ถ้าถาม detail ของ family จะสรุปข้อมูลเกมใน family แทนการตอบแค่มีเกมอะไร

## Guard สำคัญ

- ห้ามข้าม category เช่นคำถามเกมห้ามดึง knowledge/rules มาแทนโดยไม่มี route รองรับ
- คำถาม `game_detail` ต้องมี entity match กับชื่อเกม/title/aliases
- ถ้า vector score หรือ entity score ต่ำ จะ no-answer/no-context
- experimental RAG ไม่ fallback ไป broad lexical สำหรับคำถามทั่วไปหรือคำถามเกมแบบ entity route

## Smoke ที่ลอง

- `Resident คือเกมอะไร`
  - mode: `pipeline:games_family_availability_fast_path`
  - ตอบ Resident Evil 4 และ Resident Evil Village พร้อม summary
- `อยากเล่น residen`
  - mode: `pipeline:guarded_vector_override_unknown_game`
  - ดึง Resident Evil 4 ได้จาก guarded vector
- `เกม abcxyz คืออะไร`
  - mode: `pipeline:no_answer`
  - ไม่ดึง Super Smash/Valorant มั่ว
- `เกม abcxyz คืออะไร` พร้อม experimental RAG
  - mode: `pipeline:experimental_rag_no_context`
  - ไม่ fallback ไป scoped/broad lexical
- `วิธีเล่น little night`
  - mode: `pipeline:rag_direct_curated`
  - ยังดึง Little Nightmares II ได้
- `วิธีเล่น final fan`
  - mode: `pipeline:rag_direct_curated`
  - ยังดึง FINAL FANTASY XVI ได้
- `มีเกมอะไรให้เล่นบ้าง`
  - mode: `pipeline:games_catalog_fast_path`
  - fast path เดิมยังตอบถูก

## ผลตรวจ

- `py -3 -m py_compile ...` ผ่าน
- `py -3 tools\validate_update.py` ผ่าน
- ไม่ได้ run Ground Truth ชุดใหญ่ตามคำขอประหยัด token
- ยังไม่ได้ deploy production

## ข้อจำกัด

รอบนี้ยังไม่ใช้ neural embedding model เช่น `intfloat/multilingual-e5-small` เพราะต้องรักษาให้ Vercel deploy ได้เร็วและไม่เพิ่ม dependency/model ใหญ่ ถ้าจะยกระดับต่อ ควรทำ external/local backend สำหรับ embedding แล้วให้ Vercel เรียก index/result ที่ precomputed หรือ API ภายนอกแทน
