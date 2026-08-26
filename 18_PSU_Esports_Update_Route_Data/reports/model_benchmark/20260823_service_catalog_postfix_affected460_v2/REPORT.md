# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T22:43:03
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 100.0% | 100.0 | 0.6152 | 1.0512 | 1.6804 | 0 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| availability_game | 166 | 100.0% | 100.0 | 0.5282 | 0.8335 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.4139 | 0.4578 |
| availability_service | 23 | 100.0% | 100.0 | 0.3147 | 0.4344 |
| compound | 89 | 100.0% | 100.0 | 0.8449 | 1.3794 |
| games | 158 | 100.0% | 100.0 | 0.6659 | 1.0201 |
| reservation | 20 | 100.0% | 100.0 | 0.2995 | 0.5044 |

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
