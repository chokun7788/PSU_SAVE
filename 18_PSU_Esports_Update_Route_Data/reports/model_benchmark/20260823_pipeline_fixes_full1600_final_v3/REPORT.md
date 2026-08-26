# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T22:06:23
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 99.94% | 99.99 | 0.773 | 2.3135 | 6.3254 | 349 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.7237 | 1.3061 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.4057 | 1.3784 |
| availability_game | 166 | 100.0% | 100.0 | 0.4609 | 0.7143 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.1889 | 0.2391 |
| availability_service | 23 | 100.0% | 100.0 | 2.4911 | 5.9847 |
| competition_rules | 75 | 98.67% | 99.76 | 0.3621 | 0.5647 |
| compound | 89 | 100.0% | 100.0 | 1.2148 | 2.6338 |
| equipment | 58 | 100.0% | 100.0 | 1.0866 | 1.2043 |
| game_controls | 345 | 100.0% | 100.0 | 0.4175 | 0.6109 |
| game_detail | 18 | 100.0% | 100.0 | 0.2732 | 0.3975 |
| games | 158 | 100.0% | 100.0 | 0.6352 | 0.947 |
| general_llm | 275 | 100.0% | 100.0 | 1.8534 | 2.6276 |
| members | 63 | 100.0% | 100.0 | 0.326 | 0.4498 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.7669 | 1.4121 |
| reservation | 20 | 100.0% | 100.0 | 0.3504 | 0.5125 |
| schedule | 10 | 100.0% | 100.0 | 0.5162 | 1.4281 |
| service_fee | 258 | 100.0% | 100.0 | 0.3342 | 0.4354 |

Top errors:
- `category_mismatch:no_answer`: 1

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
