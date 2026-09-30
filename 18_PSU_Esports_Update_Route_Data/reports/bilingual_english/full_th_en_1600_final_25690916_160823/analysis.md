# Supervised Thai-English 1,600 Evaluation Analysis

> English is a machine-translated Shadow corpus. These results measure current pipeline behavior and contract compliance, not human-approved translation quality.

## Summary

| Suite | Strict pass | Observed P95 | Observed >=10s | Watchdog escape | Raw max | Harness timeout | Worker crash |
|---|---:|---:|---:|---:|---:|---:|---:|
| Thai | 1494/1600 (93.38%) | 3.992s | 31 | 0 | 19.104s | 0 | 0 |
| English | 1425/1600 (89.06%) | 0.924s | 16 | 0 | 12.042s | 0 | 0 |

## Thai-English Parity

- Shared case IDs: 1600
- Route category mismatches: 219
- Large bullet-format gaps: 478
- One language passed while the other failed: 223

## Leading Failures

### Thai
- `category`: 64
- `missing_any`: 43
- `missing`: 35
- `mode`: 4

### English
- `category`: 120
- `thai_prose_leak`: 55

## Slowest Cases

### Thai

- `MB-1440-GL-115` 19.1042s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายแบบใช้ในงาน chatbot
- `MB-1500-GL-175` 19.0895s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค เขียนเป็นภาษาไทยธรรมชาติ
- `MB-1380-GL-055` 19.0458s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอ 1 ย่อหน้า
- `MB-1480-GL-155` 19.0397s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบสุภาพ
- `MB-1510-GL-185` 19.032s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบไม่เป็นทางการมาก
- `MB-1530-GL-205` 19.0317s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ช่วยสรุปใจความสำคัญ
- `MB-1360-GL-035` 19.0255s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบเป็นภาษาไทย
- `MB-1600-GL-275` 19.0238s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบใช้พูดกับผู้ใช้บริการ
- `MB-1420-GL-095` 19.0237s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอสรุปเป็น 2 ข้อ
- `MB-1430-GL-105` 19.0231s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอคำตอบไม่เกิน 3 บรรทัด
### English

- `EN-SHADOW-1495` 12.0423s | `pipeline:missing_english_localization` | What's the difference between server and client? Answer appropriately for a PSU student
- `EN-SHADOW-1481` 11.257s | `pipeline:english_no_answer` | What is the word 'reservation' in Thai?
- `EN-SHADOW-1581` 11.1985s | `pipeline:english_no_answer` | What is the word 'reservation' in Thai? Explain it simply.
- `EN-SHADOW-1490` 11.1614s | `pipeline:english_no_answer` | Summarize a polite two-sentence way to say thank you, suitable for a PSU student
- `EN-SHADOW-1401` 11.0265s | `pipeline:english_no_answer` | What is the word 'reservation' in Thai? Answer simply for a first grader to understand.
- `EN-SHADOW-1591` 10.9719s | `pipeline:english_no_answer` | What is the word 'reservation' in Thai?
- `EN-SHADOW-1441` 10.7313s | `pipeline:english_no_answer` | What is the Thai word for reservation when used in a chatbot context?
- `EN-SHADOW-0622` 10.7247s | `pipeline:multi_question_splitter` | What is the shooting button in Call of Duty? Where can I play it?
- `EN-SHADOW-1501` 10.6964s | `pipeline:english_no_answer` | What is the Thai word for reservation?
- `EN-SHADOW-1451` 10.6831s | `pipeline:english_no_answer` | What is the term 'reservation' in the context of gaming?

## Watchdog-Control Observations

- `watchdog_escape_observed` means a row returned as `completed` after exceeding the evaluator's 25-second limit. It is a runner/pipeline cancellation defect, not normal latency.

## Limits

- A watchdog timeout is a runner observation, not a response delivered to a user.
- Direct Thai-English score comparison is limited because the English Shadow is machine-translated and has its own contract.
