# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-03T21:50:58
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 100.0% | 100.0 | 0.5443 | 1.0222 | 8.2799 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.4839 | 1.0259 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.2103 | 0.5265 |
| availability_game | 166 | 100.0% | 100.0 | 0.4987 | 0.7452 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3585 | 0.392 |
| availability_service | 23 | 100.0% | 100.0 | 1.2661 | 4.9297 |
| competition_rules | 75 | 100.0% | 100.0 | 0.4038 | 0.5531 |
| compound | 89 | 100.0% | 100.0 | 1.0061 | 1.7651 |
| equipment | 58 | 100.0% | 100.0 | 0.2586 | 0.3619 |
| game_controls | 345 | 100.0% | 100.0 | 0.4624 | 0.6549 |
| game_detail | 18 | 100.0% | 100.0 | 0.5737 | 0.8621 |
| games | 158 | 100.0% | 100.0 | 0.7042 | 1.1009 |
| members | 63 | 100.0% | 100.0 | 0.3422 | 0.4499 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.3321 | 1.1335 |
| reservation | 20 | 100.0% | 100.0 | 2.8276 | 7.9402 |
| schedule | 10 | 100.0% | 100.0 | 0.6653 | 1.7168 |
| service_fee | 258 | 100.0% | 100.0 | 0.3553 | 0.5579 |

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
