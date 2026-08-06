# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-06T15:30:03
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 86.06% | 97.38 | 0.2628 | 0.5226 | 4.0222 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 95.83% | 99.33 | 0.2262 | 0.5049 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.0983 | 0.2239 |
| availability_game | 166 | 100.0% | 100.0 | 0.2425 | 0.3639 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.1691 | 0.1916 |
| availability_service | 23 | 100.0% | 100.0 | 0.5831 | 2.1868 |
| competition_rules | 75 | 100.0% | 100.0 | 0.186 | 0.2621 |
| compound | 89 | 100.0% | 100.0 | 0.5426 | 0.9404 |
| equipment | 58 | 100.0% | 100.0 | 0.1227 | 0.1614 |
| game_controls | 345 | 100.0% | 100.0 | 0.2173 | 0.309 |
| game_detail | 18 | 100.0% | 100.0 | 0.2576 | 0.3756 |
| games | 158 | 100.0% | 100.0 | 0.3098 | 0.4581 |
| general_llm | 275 | 19.27% | 84.79 | 0.2703 | 0.5427 |
| members | 63 | 100.0% | 100.0 | 0.1708 | 0.2479 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.1762 | 0.6313 |
| reservation | 20 | 100.0% | 100.0 | 1.3383 | 3.8336 |
| schedule | 10 | 100.0% | 100.0 | 0.2932 | 0.7946 |
| service_fee | 258 | 100.0% | 100.0 | 0.1784 | 0.2357 |

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
