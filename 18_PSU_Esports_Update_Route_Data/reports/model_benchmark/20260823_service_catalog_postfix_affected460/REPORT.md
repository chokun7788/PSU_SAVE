# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T22:30:55
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 99.35% | 99.71 | 1.0445 | 5.9929 | 9.1671 | 0 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| availability_game | 166 | 100.0% | 100.0 | 0.3647 | 0.6769 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.4007 | 0.4687 |
| availability_service | 23 | 100.0% | 100.0 | 0.2506 | 0.38 |
| compound | 89 | 96.63% | 98.52 | 3.3144 | 8.8105 |
| games | 158 | 100.0% | 100.0 | 0.6298 | 0.9314 |
| reservation | 20 | 100.0% | 100.0 | 0.9053 | 2.7321 |

Top errors:
- `category_mismatch:no_answer`: 3
- `missing_any:จอง|เลือก|บริการ`: 3

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
