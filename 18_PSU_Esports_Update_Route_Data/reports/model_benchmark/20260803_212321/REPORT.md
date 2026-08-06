# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-03T21:35:28
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 100.0% | 100.0 | 0.5442 | 1.013 | 7.8011 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.5616 | 1.3607 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.1923 | 0.4542 |
| availability_game | 166 | 100.0% | 100.0 | 0.5827 | 0.9364 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3416 | 0.4003 |
| availability_service | 21 | 100.0% | 100.0 | 1.4942 | 5.256 |
| competition_rules | 75 | 100.0% | 100.0 | 0.3675 | 0.4867 |
| compound | 89 | 100.0% | 100.0 | 1.0858 | 1.9443 |
| equipment | 58 | 100.0% | 100.0 | 0.2575 | 0.3152 |
| game_controls | 345 | 100.0% | 100.0 | 0.4378 | 0.652 |
| game_detail | 18 | 100.0% | 100.0 | 0.5551 | 0.7921 |
| games | 158 | 100.0% | 100.0 | 0.6272 | 0.9034 |
| members | 63 | 100.0% | 100.0 | 0.3405 | 0.4723 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.3456 | 1.2501 |
| reservation | 20 | 100.0% | 100.0 | 2.6287 | 7.4611 |
| schedule | 10 | 100.0% | 100.0 | 0.6118 | 1.9592 |
| service_fee | 258 | 100.0% | 100.0 | 0.363 | 0.4813 |

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
