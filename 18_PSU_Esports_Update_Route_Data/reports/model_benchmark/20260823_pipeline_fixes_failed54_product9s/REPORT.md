# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T17:58:00
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 2

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 83.33% | 94.52 | 2.044 | 3.3568 | 7.4958 | 50 |
| 2 | no_llm | No-LLM | 12.96% | 86.04 | 0.4983 | 0.5071 | 6.1968 | 0 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 3 | 100.0% | 100.0 | 3.2563 | 7.4958 |
| competition_rules | 1 | 0.0% | 82.0 | 6.0494 | 6.0494 |
| games | 2 | 100.0% | 100.0 | 0.9453 | 1.6711 |
| general_llm | 48 | 83.33% | 94.21 | 1.9305 | 3.3543 |

Top errors:
- `missing_any:คีย์บอร์ด|mechanical`: 6
- `llm_required_but_unavailable`: 6
- `missing_any:ขอบคุณ`: 2
- `category_mismatch:no_answer`: 1

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 3 | 100.0% | 100.0 | 0.247 | 0.5651 |
| competition_rules | 1 | 0.0% | 82.0 | 6.1968 | 6.1968 |
| games | 2 | 100.0% | 100.0 | 0.9734 | 1.7197 |
| general_llm | 48 | 4.17% | 84.67 | 0.3755 | 0.4791 |

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
