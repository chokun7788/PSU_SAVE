# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-03T20:43:54
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 95.07% | 98.57 | 0.4492 | 0.6861 | 1.2687 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| game_controls | 345 | 95.07% | 98.57 | 0.4492 | 0.6861 |

Top errors:
- `category_mismatch:clarification`: 16
- `missing_any:L1|กระโดด / ปีนป่าย`: 1
- `missing_any:R3|เปลี่ยนท่า / สไลด์ / พุ่งหลบ`: 1
- `missing_any:Cross|ใช้อุปกรณ์ยุทธวิธี`: 1
- `missing_any:Circle|โจมตีประชิด`: 1
- `missing_any:Circle|ย่อตัว / หมอบ / สไลด์`: 1
- `missing_any:Square|โต้ตอบ / รีโหลด`: 1
- `missing_any:Triangle|สลับอาวุธ`: 1

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
