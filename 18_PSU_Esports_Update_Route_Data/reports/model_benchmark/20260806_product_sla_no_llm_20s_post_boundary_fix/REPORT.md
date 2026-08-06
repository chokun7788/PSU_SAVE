# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-06T15:58:34
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 86.12% | 97.39 | 0.4516 | 0.9152 | 7.3579 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.4131 | 0.9108 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.1568 | 0.3842 |
| availability_game | 166 | 100.0% | 100.0 | 0.4297 | 0.6586 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.2853 | 0.3167 |
| availability_service | 23 | 100.0% | 100.0 | 1.0497 | 4.187 |
| competition_rules | 75 | 100.0% | 100.0 | 0.3227 | 0.4454 |
| compound | 89 | 100.0% | 100.0 | 0.9558 | 1.747 |
| equipment | 58 | 100.0% | 100.0 | 0.2121 | 0.2856 |
| game_controls | 345 | 100.0% | 100.0 | 0.3829 | 0.549 |
| game_detail | 18 | 100.0% | 100.0 | 0.4638 | 0.7722 |
| games | 158 | 100.0% | 100.0 | 0.5402 | 0.8068 |
| general_llm | 275 | 19.27% | 84.79 | 0.4096 | 0.9625 |
| members | 63 | 100.0% | 100.0 | 0.3101 | 0.4155 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.3656 | 1.3005 |
| reservation | 20 | 100.0% | 100.0 | 2.4058 | 7.0084 |
| schedule | 10 | 100.0% | 100.0 | 0.5022 | 1.3956 |
| service_fee | 258 | 100.0% | 100.0 | 0.3081 | 0.4008 |

Top errors:
- `missing_any:latency|หน่วง`: 28
- `missing_any:เฟรม|ความละเอียด`: 28
- `missing_any:API|เชื่อมต่อ`: 28
- `missing_any:ขอบคุณ`: 28
- `missing_any:กิจกรรม`: 27
- `missing_any:คีย์บอร์ด|mechanical`: 27
- `missing_any:GPU|กราฟิก`: 27
- `missing_any:server|client`: 27

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
