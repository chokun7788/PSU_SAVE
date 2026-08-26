# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T18:06:59
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 83.33% | 95.26 | 2.1426 | 2.6486 | 9.0498 | 50 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 3 | 100.0% | 100.0 | 1.546 | 2.5353 |
| competition_rules | 1 | 0.0% | 72.0 | 9.0498 | 9.0498 |
| games | 2 | 100.0% | 100.0 | 1.2572 | 2.1638 |
| general_llm | 48 | 83.33% | 95.25 | 2.0729 | 2.6486 |

Top errors:
- `missing_any:ขอบคุณ`: 6
- `llm_required_but_unavailable`: 4
- `category_mismatch:no_answer`: 1
- `missing_any:latency|หน่วง`: 1
- `missing_any:คีย์บอร์ด|mechanical`: 1

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
