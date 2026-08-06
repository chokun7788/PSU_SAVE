# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-03T19:36:59
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 86.01% | 97.52 | 1.6366 | 5.1583 | 30.5913 | 20 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 20 | 100.0% | 100.0 | 1.2413 | 6.005 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.2253 | 0.6343 |
| availability_game | 20 | 100.0% | 100.0 | 0.5265 | 0.7604 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3563 | 0.3951 |
| availability_service | 20 | 100.0% | 100.0 | 1.3121 | 5.5036 |
| competition_rules | 20 | 100.0% | 100.0 | 0.4057 | 0.5912 |
| compound | 20 | 100.0% | 100.0 | 1.4715 | 2.8615 |
| equipment | 20 | 80.0% | 95.2 | 6.8468 | 25.1557 |
| game_controls | 20 | 100.0% | 100.0 | 0.4693 | 0.6015 |
| game_detail | 18 | 61.11% | 93.56 | 0.8337 | 3.4807 |
| games | 20 | 80.0% | 97.0 | 0.747 | 1.053 |
| general_llm | 20 | 0.0% | 84.0 | 0.2973 | 0.4139 |
| members | 20 | 85.0% | 97.5 | 2.4893 | 3.878 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.8672 | 2.1094 |
| reservation | 20 | 95.0% | 98.3 | 2.4826 | 6.9956 |
| schedule | 10 | 90.0% | 96.6 | 1.3747 | 2.4649 |
| service_fee | 20 | 100.0% | 100.0 | 3.1913 | 4.5116 |

Top errors:
- `missing_any:Gaming|ใช้|Zone`: 3
- `category_mismatch:no_answer`: 3
- `category_mismatch:clarification`: 2
- `missing_any:latency|หน่วง`: 2
- `missing_any:เฟรม|ความละเอียด`: 2
- `missing_any:API|เชื่อมต่อ`: 2
- `missing_any:JSON|ข้อมูล`: 2
- `missing_any:ขอบคุณ`: 2

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
