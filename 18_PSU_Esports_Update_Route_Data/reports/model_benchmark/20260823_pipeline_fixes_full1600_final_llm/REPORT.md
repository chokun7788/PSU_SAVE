# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T21:04:55
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 99.94% | 99.99 | 0.5779 | 2.1365 | 7.8926 | 355 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 1.2275 | 5.8121 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.2747 | 1.1082 |
| availability_game | 166 | 100.0% | 100.0 | 0.2465 | 0.3768 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.1666 | 0.1873 |
| availability_service | 23 | 100.0% | 100.0 | 1.3664 | 3.3663 |
| competition_rules | 75 | 98.67% | 99.76 | 0.2038 | 0.3233 |
| compound | 89 | 100.0% | 100.0 | 0.6892 | 1.5316 |
| equipment | 58 | 100.0% | 100.0 | 0.7902 | 0.8584 |
| game_controls | 345 | 100.0% | 100.0 | 0.2644 | 0.3349 |
| game_detail | 18 | 100.0% | 100.0 | 0.2628 | 0.3886 |
| games | 158 | 100.0% | 100.0 | 0.3372 | 0.497 |
| general_llm | 275 | 100.0% | 100.0 | 1.7514 | 2.5099 |
| members | 63 | 100.0% | 100.0 | 0.1766 | 0.2453 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.5058 | 1.0519 |
| reservation | 20 | 100.0% | 100.0 | 0.1991 | 0.2852 |
| schedule | 10 | 100.0% | 100.0 | 0.317 | 0.8184 |
| service_fee | 258 | 100.0% | 100.0 | 0.1741 | 0.2366 |

Top errors:
- `category_mismatch:no_answer`: 1

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
