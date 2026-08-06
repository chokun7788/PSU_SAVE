# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-03T21:18:45
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 99.77% | 99.96 | 0.5179 | 0.993 | 8.267 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.4377 | 0.8476 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.1995 | 0.5248 |
| availability_game | 166 | 98.19% | 99.71 | 0.4705 | 0.7167 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3016 | 0.3439 |
| availability_service | 21 | 100.0% | 100.0 | 1.2245 | 4.6948 |
| competition_rules | 75 | 100.0% | 100.0 | 0.3682 | 0.5406 |
| compound | 89 | 100.0% | 100.0 | 1.0207 | 1.6103 |
| equipment | 58 | 100.0% | 100.0 | 0.29 | 0.3662 |
| game_controls | 345 | 100.0% | 100.0 | 0.4255 | 0.6119 |
| game_detail | 18 | 100.0% | 100.0 | 0.4874 | 0.7923 |
| games | 158 | 100.0% | 100.0 | 0.5786 | 0.8468 |
| members | 63 | 100.0% | 100.0 | 0.3426 | 0.518 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.3701 | 1.2798 |
| reservation | 20 | 100.0% | 100.0 | 2.7511 | 7.7053 |
| schedule | 10 | 100.0% | 100.0 | 0.5656 | 1.6086 |
| service_fee | 258 | 100.0% | 100.0 | 0.3911 | 0.5206 |

Top errors:
- `missing_any:Nintendo Switch (1-2 Persons)|Nintendo Switch|Overcooked!`: 1
- `missing_any:Overcooked!|Nintendo Switch (1-2 Persons)|Nintendo Switch`: 1
- `missing_any:Nintendo Switch|Nintendo Switch (1-2 Persons)`: 1

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
