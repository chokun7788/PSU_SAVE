# Fast Runtime Update

เอกสารนี้สรุป runtime รุ่นใหม่ที่เพิ่มเข้ามาเพื่อให้ Chatbot ตอบเร็วขึ้น แม่นขึ้น และใช้ทรัพยากรน้อยลง

## แนวคิด

Runtime นี้ไม่เรียก LLM และไม่โหลด Vector DB สำหรับคำถามที่ตอบได้แบบ deterministic เช่น ราคา เวลาเปิดปิด กฎการจอง เกม อุปกรณ์ ติดต่อ และข้อมูลพื้นฐาน

ลำดับ route ที่ใช้จริง:

1. `answer_static_domain` จับ no-answer, booking, check-in, payment, rules, knowledge, news, contact, overview
2. `answer_price` จับราคาและ Service Fee แบบ canonical table
3. `answer_schedule` จับเวลาเปิดปิดและ maintenance
4. `answer_equipment` จับอุปกรณ์/zone
5. `answer_games` จับรายชื่อเกม
6. `RuleMatcher` จาก `data/rules/*.jsonl`
7. `no_answer_fast`

## ไฟล์หลัก

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\runtime\fast_answer.py
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tools\run_ground_truth_fast_eval.py
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tests\smoke_test_fast_runtime.py
```

## วิธีรัน

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tests\smoke_test_fast_runtime.py
py -3 tools\run_ground_truth_fast_eval.py --label v2_fast_update_round4_20260701
```

## ผล Ground Truth ล่าสุด

Report:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\fast_ground_truth_report_v2_fast_update_round4_20260701.md
```

Results JSONL:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\fast_ground_truth_results_v2_fast_update_round4_20260701.jsonl
```

ผล:

- Total: 360
- PASS: 360
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.0001s
- P95 latency: 0.0002s
- Max latency จากการสรุป: ประมาณ 0.0007s

## สิ่งที่ช่วยลดทรัพยากร

- ไม่โหลด Qwen/Ollama สำหรับ FAQ ที่มีคำตอบแน่นอน
- ไม่โหลด Chroma/embedding ใน fast runtime
- ใช้ rule/deterministic answer ก่อน RAG
- ใช้ canonical answer สำหรับราคา ทำให้ไม่ต้องให้ LLM เรียบเรียงตัวเลข
- precompile regex ใน `RuleMatcher`
- cache normalization ด้วย `lru_cache`
- ลด fuzzy กว้าง ๆ และใช้ keyword/entity route เฉพาะจุด

## จุดที่แก้ระหว่างทดสอบ

- `จอ` เคย match ในคำว่า `จอง` ทำให้ booking ไปเข้า equipment
- `zone` เคย match ใน `Warzone` ทำให้คำถามเกมไปเข้า equipment
- `เสีย` เคย match ใน `เสียงดัง` ทำให้กฎเสียงดังไปเข้า price
- `GAME ON เปิดโลกอีสปอร์ต` เคยถูก schedule แย่ง route เพราะมีคำว่าเปิด
- `เช็คอินต้องใช้บัตรอะไร` เคยถูก route ไป check-in advance แทน check-in ID
- `service fee` แบบไม่ระบุบริการต้องตอบเป็น summary table

## สถานะข้อ 1-6

1. ผูก router/calculator กับ notebook แล้ว โดยเพิ่ม cell ท้าย notebook `01_local_rag_qwen3_4b.ipynb`
2. ราคาเข้า deterministic calculator/fast price route ก่อน LLM แล้ว
3. Rule loader อ่านจาก `data/rules/*.jsonl` แล้ว
4. สร้าง Human Review sample จากผล fast eval แล้วที่ `data/human_review/human_review_fast_round4_sample.jsonl`
5. ใช้ผล fail จาก eval รอบ 1-3 แก้ route/data logic แล้ว
6. รัน Ground Truth 360 ข้อแล้ว ผ่าน 360/360

## ข้อควรระวัง

คะแนน 360/360 นี้คือผ่านตาม Ground Truth ที่มีอยู่ ไม่ได้แปลว่าครอบคลุมทุกคำถามจริงของผู้ใช้แล้ว ดังนั้นถ้าเจอคำถามใหม่จาก Facebook หรือผู้ใช้จริง ควรเพิ่มเข้า Human Review และ Ground Truth ต่อ
