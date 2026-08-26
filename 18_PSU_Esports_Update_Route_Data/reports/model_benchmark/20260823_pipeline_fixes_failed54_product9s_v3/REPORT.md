# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T18:13:40
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 2

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 92.59% | 98.78 | 2.0665 | 2.7081 | 2.9288 | 50 |
| 2 | no_llm | No-LLM | 12.96% | 86.04 | 0.4554 | 0.6409 | 1.0408 | 0 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 3 | 66.67% | 94.67 | 1.5478 | 2.5976 |
| competition_rules | 1 | 0.0% | 82.0 | 1.0013 | 1.0013 |
| games | 2 | 100.0% | 100.0 | 0.5855 | 0.9016 |
| general_llm | 48 | 95.83% | 99.33 | 2.1828 | 2.863 |

Top errors:
- `category_mismatch:no_answer`: 1
- `missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล`: 1
- `missing_any:ขอบคุณ`: 1
- `missing_any:กิจกรรม`: 1

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 3 | 100.0% | 100.0 | 0.3015 | 0.7035 |
| competition_rules | 1 | 0.0% | 82.0 | 1.0408 | 1.0408 |
| games | 2 | 100.0% | 100.0 | 0.5501 | 0.8518 |
| general_llm | 48 | 4.17% | 84.67 | 0.4489 | 0.5504 |

Top errors:
- `missing_any:คีย์บอร์ด|mechanical`: 27
- `missing_any:ขอบคุณ`: 9
- `missing_any:latency|หน่วง`: 5
- `category_mismatch:no_answer`: 1
- `missing_any:เฟรม|ความละเอียด`: 1
- `missing_any:API|เชื่อมต่อ`: 1
- `missing_any:กิจกรรม`: 1
- `missing_any:GPU|กราฟิก`: 1

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
