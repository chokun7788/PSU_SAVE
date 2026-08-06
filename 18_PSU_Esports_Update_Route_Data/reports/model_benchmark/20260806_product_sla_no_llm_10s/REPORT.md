# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-06T15:43:51
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 86.06% | 97.38 | 0.4517 | 0.8991 | 6.9153 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 95.83% | 99.33 | 0.4264 | 0.8646 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.1615 | 0.3953 |
| availability_game | 166 | 100.0% | 100.0 | 0.426 | 0.6636 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.2898 | 0.3138 |
| availability_service | 23 | 100.0% | 100.0 | 1.0642 | 3.9015 |
| competition_rules | 75 | 100.0% | 100.0 | 0.3407 | 0.4556 |
| compound | 89 | 100.0% | 100.0 | 0.9729 | 1.6378 |
| equipment | 58 | 100.0% | 100.0 | 0.1997 | 0.2578 |
| game_controls | 345 | 100.0% | 100.0 | 0.3911 | 0.5661 |
| game_detail | 18 | 100.0% | 100.0 | 0.4634 | 0.6789 |
| games | 158 | 100.0% | 100.0 | 0.535 | 0.7619 |
| general_llm | 275 | 19.27% | 84.79 | 0.3958 | 0.9703 |
| members | 63 | 100.0% | 100.0 | 0.2925 | 0.3946 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.3289 | 1.1347 |
| reservation | 20 | 100.0% | 100.0 | 2.3129 | 6.7195 |
| schedule | 10 | 100.0% | 100.0 | 0.4789 | 1.2827 |
| service_fee | 258 | 100.0% | 100.0 | 0.3204 | 0.4161 |

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
