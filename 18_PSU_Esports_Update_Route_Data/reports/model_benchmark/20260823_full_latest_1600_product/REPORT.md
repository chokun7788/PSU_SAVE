# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T02:35:55
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 2

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 96.62% | 98.94 | 1.3425 | 4.1369 | 18.282 | 278 |
| 2 | no_llm | No-LLM | 86.12% | 97.39 | 0.4719 | 0.8623 | 7.8775 | 0 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 87.5% | 94.5 | 1.9674 | 11.0166 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.7369 | 1.5998 |
| availability_game | 166 | 100.0% | 100.0 | 1.0438 | 1.6306 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.8571 | 1.4783 |
| availability_service | 23 | 100.0% | 100.0 | 1.4377 | 5.548 |
| competition_rules | 75 | 98.67% | 98.67 | 0.5608 | 1.2147 |
| compound | 89 | 100.0% | 100.0 | 1.1775 | 4.7661 |
| equipment | 58 | 100.0% | 100.0 | 0.1426 | 0.1842 |
| game_controls | 345 | 100.0% | 100.0 | 0.4314 | 0.6664 |
| game_detail | 18 | 100.0% | 100.0 | 1.4878 | 1.835 |
| games | 158 | 98.73% | 99.59 | 1.4042 | 1.9323 |
| general_llm | 275 | 82.55% | 94.92 | 4.3132 | 14.2934 |
| members | 63 | 100.0% | 100.0 | 0.2306 | 0.4136 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.8933 | 1.5383 |
| reservation | 20 | 100.0% | 100.0 | 1.4216 | 3.9974 |
| schedule | 10 | 100.0% | 100.0 | 0.2879 | 0.7788 |
| service_fee | 258 | 100.0% | 100.0 | 0.3677 | 0.5086 |

Top errors:
- `category_mismatch:equipment`: 27
- `missing_any:คีย์บอร์ด|mechanical`: 27
- `category_mismatch:clarification`: 10
- `missing_any:ขอบคุณ`: 9
- `missing_any:latency|หน่วง`: 5
- `exception:UnboundLocalError`: 2
- `missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล`: 2
- `missing:Animal Crossing`: 1

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.4636 | 1.0016 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.1824 | 0.452 |
| availability_game | 166 | 100.0% | 100.0 | 0.48 | 0.7097 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3357 | 0.3815 |
| availability_service | 23 | 100.0% | 100.0 | 1.1881 | 4.534 |
| competition_rules | 75 | 100.0% | 100.0 | 0.404 | 0.6289 |
| compound | 89 | 100.0% | 100.0 | 0.8235 | 1.9237 |
| equipment | 58 | 100.0% | 100.0 | 0.2472 | 0.3178 |
| game_controls | 345 | 100.0% | 100.0 | 0.43 | 0.6384 |
| game_detail | 18 | 100.0% | 100.0 | 0.5314 | 0.7619 |
| games | 158 | 100.0% | 100.0 | 0.629 | 0.9218 |
| general_llm | 275 | 19.27% | 84.79 | 0.3056 | 0.6427 |
| members | 63 | 100.0% | 100.0 | 0.3292 | 0.4503 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.3706 | 1.2834 |
| reservation | 20 | 100.0% | 100.0 | 2.6631 | 7.5563 |
| schedule | 10 | 100.0% | 100.0 | 0.563 | 1.5512 |
| service_fee | 258 | 100.0% | 100.0 | 0.3591 | 0.4621 |

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
