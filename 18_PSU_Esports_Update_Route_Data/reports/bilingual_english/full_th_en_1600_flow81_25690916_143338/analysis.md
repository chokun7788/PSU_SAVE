# Supervised Thai-English 1,600 Evaluation Analysis

> English is a machine-translated Shadow corpus. These results measure current pipeline behavior and contract compliance, not human-approved translation quality.

## Summary

| Suite | Strict pass | Observed P95 | Observed >=10s | Watchdog escape | Raw max | Harness timeout | Worker crash |
|---|---:|---:|---:|---:|---:|---:|---:|
| Thai | 1519/1600 (94.94%) | 2.180s | 30 | 0 | 19.535s | 0 | 0 |
| English | 1425/1600 (89.06%) | 0.892s | 0 | 0 | 8.678s | 0 | 0 |

## Thai-English Parity

- Shared case IDs: 1600
- Route category mismatches: 219
- Large bullet-format gaps: 478
- One language passed while the other failed: 244

## Leading Failures

### Thai
- `category`: 64
- `missing`: 35
- `missing_any`: 19
- `mode`: 4

### English
- `category`: 120
- `thai_prose_leak`: 55

## Slowest Cases

### Thai

- `MB-1360-GL-035` 19.5349s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบเป็นภาษาไทย
- `MB-1540-GL-215` 19.4232s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบ bullet สั้น ๆ
- `MB-1460-GL-135` 19.185s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ช่วยยกตัวอย่างสั้น ๆ
- `MB-1450-GL-125` 19.0232s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายแบบใช้กับวงการเกม
- `MB-1380-GL-055` 19.0217s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอ 1 ย่อหน้า
- `MB-1410-GL-085` 16.1821s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบไม่ใช้ศัพท์ยาก
- `MB-1510-GL-185` 15.9751s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบไม่เป็นทางการมาก
- `MB-1470-GL-145` 15.667s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค เปรียบเทียบแบบสั้น
- `MB-1570-GL-245` 14.948s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ให้คำจำกัดความแบบสั้น
- `MB-1330-GL-005` 14.8189s | `pipeline:general_llm_after_rag_miss` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค
### English

- `EN-SHADOW-0739` 8.6779s | `pipeline:games_unknown_target_en` | Where is The Last of Us Part II located?
- `EN-SHADOW-1581` 8.4368s | `pipeline:english_no_answer` | What is the word 'reservation' in Thai? Explain it simply.
- `EN-SHADOW-1591` 8.3622s | `pipeline:english_no_answer` | What is the word 'reservation' in Thai?
- `EN-SHADOW-1443` 8.3371s | `pipeline:general_rag_miss_llm_unavailable` | What is a mechanical keyboard, briefly explained for use in a chatbot?
- `EN-SHADOW-0064` 8.1328s | `pipeline:price_service_clarification_en` | How much does TEKKEN 8 cost?
- `EN-SHADOW-0622` 8.1132s | `pipeline:multi_question_splitter` | What is the shooting button in Call of Duty? Where can I play it?
- `EN-SHADOW-0397` 8.1095s | `pipeline:english_no_answer` | How to play
- `EN-SHADOW-1483` 6.113s | `pipeline:general_llm_direct` | What is a mechanical keyboard, briefly?
- `EN-SHADOW-1401` 5.4877s | `pipeline:english_no_answer` | What is the word 'reservation' in Thai? Answer simply for a first grader to understand.
- `EN-SHADOW-1441` 5.1865s | `pipeline:english_no_answer` | What is the Thai word for reservation when used in a chatbot context?

## Watchdog-Control Observations

- `watchdog_escape_observed` means a row returned as `completed` after exceeding the evaluator's 25-second limit. It is a runner/pipeline cancellation defect, not normal latency.

## Limits

- A watchdog timeout is a runner observation, not a response delivered to a user.
- Direct Thai-English score comparison is limited because the English Shadow is machine-translated and has its own contract.
