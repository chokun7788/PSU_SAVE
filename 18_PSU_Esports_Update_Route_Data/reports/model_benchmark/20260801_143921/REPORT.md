# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-01T14:56:23
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 81.81% | 96.87 | 0.631 | 3.1724 | 226.5192 | 215 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 97.0 | 0.4675 | 3.4775 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 2.8058 | 16.4996 |
| availability_game | 166 | 100.0% | 100.0 | 0.1415 | 0.1961 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.0176 | 0.0264 |
| availability_service | 21 | 61.9% | 93.14 | 0.4567 | 1.8979 |
| competition_rules | 75 | 100.0% | 100.0 | 0.1582 | 0.29 |
| compound | 89 | 100.0% | 100.0 | 2.3199 | 5.4846 |
| equipment | 58 | 100.0% | 100.0 | 1.6505 | 3.6051 |
| game_controls | 343 | 99.42% | 99.91 | 0.2379 | 0.2892 |
| game_detail | 18 | 100.0% | 100.0 | 0.5432 | 2.4641 |
| games | 158 | 100.0% | 100.0 | 0.1506 | 0.2409 |
| general_llm | 279 | 0.0% | 82.93 | 1.1081 | 0.2686 |
| members | 63 | 100.0% | 100.0 | 2.3464 | 3.6116 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.609 | 1.6671 |
| reservation | 20 | 100.0% | 100.0 | 1.7257 | 4.5539 |
| schedule | 10 | 100.0% | 100.0 | 1.0761 | 2.084 |
| service_fee | 258 | 100.0% | 100.0 | 0.0464 | 0.1508 |

Top errors:
- `missing_any:latency|หน่วง`: 28
- `missing_any:เฟรม|ความละเอียด`: 28
- `missing_any:API|เชื่อมต่อ`: 28
- `missing_any:JSON|ข้อมูล`: 28
- `missing_any:ขอบคุณ`: 28
- `missing_any:จอง`: 28
- `missing_any:กิจกรรม`: 28
- `missing_any:คีย์บอร์ด|mechanical`: 28

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
