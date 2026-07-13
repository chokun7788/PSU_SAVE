# Ground Truth Evaluation - PSU Esports Local RAG

วันที่: 2026-06-29

## Summary

- Total: 105
- PASS: 105
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.220s
- Keyword fail: 0
- Source fail: 0
- Answers containing `ไม่พบข้อมูล`: 6
- Chinese character leakage: 0

## Mode Distribution

- `rule_fast_path`: 52
- `rag_direct_curated`: 48
- `rag_llm`: 5

## Answer Type Distribution

- `fact`: 73
- `list`: 14
- `summary`: 8
- `no_answer`: 6
- `procedure`: 3
- `definition`: 1

## By Category

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| about_us | 5 | 5 | 100.00% |
| contact | 5 | 5 | 100.00% |
| equipment | 8 | 8 | 100.00% |
| events_news | 5 | 5 | 100.00% |
| games | 8 | 8 | 100.00% |
| knowledge | 8 | 8 | 100.00% |
| no_answer | 6 | 6 | 100.00% |
| overview | 5 | 5 | 100.00% |
| penalty | 5 | 5 | 100.00% |
| reservation | 29 | 29 | 100.00% |
| rules | 18 | 18 | 100.00% |
| services | 3 | 3 | 100.00% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| definition | 1 | 1 | 100.00% |
| fact | 73 | 73 | 100.00% |
| list | 14 | 14 | 100.00% |
| no_answer | 6 | 6 | 100.00% |
| procedure | 3 | 3 | 100.00% |
| summary | 8 | 8 | 100.00% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| easy | 64 | 64 | 100.00% |
| medium | 41 | 41 | 100.00% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| rag_direct_curated | 48 | 48 | 100.00% |
| rag_llm | 5 | 5 | 100.00% |
| rule_fast_path | 52 | 52 | 100.00% |

## Failed Cases

No failed cases.

## Answer Characteristics

- `rule_fast_path` คือคำตอบ FAQ ที่เร็วและนิ่งที่สุด
- `rag_direct_curated` คือคำตอบจาก curated facts ที่ไม่ต้องเรียก LLM จึงเร็วและลด hallucination
- `rag_llm` คือคำตอบที่ต้องให้โมเดลสรุปจาก context จึงช้ากว่าและเสี่ยง keyword หายมากกว่า
- การวัดนี้เป็น keyword/source match แบบเข้ม ถ้าคำตอบถูกความหมายแต่ใช้คำคนละรูป อาจถูกนับเป็น FAIL ได้

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_2026-06-29.jsonl`
- Chat log JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_chat_log_2026-06-29.jsonl`
