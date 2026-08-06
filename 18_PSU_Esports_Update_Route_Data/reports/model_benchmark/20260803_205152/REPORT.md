# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-03T20:57:57
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 99.8% | 99.93 | 0.717 | 1.8809 | 10.1668 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.5071 | 0.9806 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.1948 | 0.4689 |
| availability_game | 166 | 100.0% | 100.0 | 0.4828 | 0.7588 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3406 | 0.3771 |
| availability_service | 21 | 100.0% | 100.0 | 1.2828 | 4.5437 |
| competition_rules | 75 | 100.0% | 100.0 | 0.4585 | 0.7217 |
| compound | 89 | 100.0% | 100.0 | 1.0608 | 1.8556 |
| game_detail | 18 | 100.0% | 100.0 | 0.5222 | 0.7873 |
| members | 63 | 100.0% | 100.0 | 0.3854 | 0.5674 |
| policy_schedule_rules | 8 | 87.5% | 95.75 | 0.4781 | 1.5373 |
| reservation | 20 | 100.0% | 100.0 | 3.363 | 9.7302 |
| schedule | 10 | 100.0% | 100.0 | 0.6008 | 1.7672 |

Top errors:
- `category_mismatch:no_answer`: 1
- `missing_any:เปิด|ปิด|จอง|ยกเลิก|นาที|อาหาร|ปรับ|กติกา`: 1

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
