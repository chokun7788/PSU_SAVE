# Supervised Thai-English 1,600 Evaluation Analysis

> English is a machine-translated Shadow corpus. These results measure current pipeline behavior and contract compliance, not human-approved translation quality.

## Summary

| Suite | Strict pass | Observed P95 | Observed >=10s | Watchdog escape | Raw max | Harness timeout | Worker crash |
|---|---:|---:|---:|---:|---:|---:|---:|
| Thai | 1388/1600 (86.75%) | 10.390s | 89 | 1 | 887.269s | 0 | 0 |
| English | 1061/1600 (66.31%) | 2.927s | 4 | 1 | 7902.739s | 0 | 0 |

## Thai-English Parity

- Shared case IDs: 1600
- Route category mismatches: 595
- Large bullet-format gaps: 480
- One language passed while the other failed: 387

## Leading Failures

### Thai
- `missing_any`: 170
- `category`: 50
- `mode`: 5
- `missing`: 2

### English
- `category`: 518
- `thai_prose_leak`: 23
- `latency`: 1
- `pipeline_timeout`: 1

## Slowest Cases

### Thai

- `MB-1099-SF-130` 887.2689s | `pipeline:request_timeout_no_answer` | General Student เล่น PS5 3 ชั่วโมง เสียกี่บาท
- `MB-1340-GL-015` 19.0551s | `pipeline:no_answer` | ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบสั้น ๆ
- `MB-1349-GL-024` 19.0516s | `pipeline:no_answer` | JSON คืออะไร ขอแบบเข้าใจง่าย
- `MB-1389-GL-064` 19.0338s | `pipeline:no_answer` | JSON คืออะไร อธิบายให้มือใหม่เข้าใจ
- `MB-1348-GL-023` 19.0325s | `pipeline:no_answer` | API คืออะไร ขอแบบเข้าใจง่าย
- `MB-1364-GL-039` 19.0313s | `pipeline:no_answer` | GPU คืออะไรแบบเข้าใจง่าย ตอบเป็นภาษาไทย
- `MB-1489-GL-164` 19.0313s | `pipeline:no_answer` | JSON คืออะไร ตอบให้เหมาะกับนักศึกษา
- `MB-1448-GL-123` 19.0291s | `pipeline:no_answer` | API คืออะไร อธิบายแบบใช้กับวงการเกม
- `MB-1329-GL-004` 19.0282s | `pipeline:no_answer` | JSON คืออะไร
- `MB-1484-GL-159` 19.025s | `pipeline:no_answer` | GPU คืออะไรแบบเข้าใจง่าย ตอบแบบสุภาพ
### English

- `EN-SHADOW-0608` 7902.7385s | `pipeline:request_timeout_no_answer` | Does ROV require check-in before a match?
- `EN-SHADOW-0609` 16.5494s | `pipeline:structured_games_catalog_en` | Which account does ROV use to compete
- `EN-SHADOW-0646` 14.3502s | `pipeline:structured_members_source_th` | What is the personal phone number of the staff member?
- `EN-SHADOW-0645` 13.8638s | `pipeline:experimental_rag_direct_fallback` | Is Valorant Mobile available?
- `EN-SHADOW-0647` 12.3777s | `pipeline:missing_english_localization` | Request information not available on the PSU Esports website
- `EN-SHADOW-0052` 9.2437s | `pipeline:structured_equipment_catalog_en` | Which is more expensive, PS5 or Nintendo?
- `EN-SHADOW-1586` 3.8212s | `pipeline:english_no_answer` | Explain the term latency in a computer system briefly without giving long examples
- `EN-SHADOW-0819` 3.8155s | `pipeline:english_no_answer` | How many players can join Cockpit #01-#02?
- `EN-SHADOW-0610` 3.756s | `pipeline:structured_competition_rules_en` | What maps are available in ROV?
- `EN-SHADOW-1556` 3.715s | `pipeline:english_no_answer` | Explain the term latency in a computer system briefly. Explain its pros and cons briefly.

## Watchdog-Control Observations

- `watchdog_escape_observed` means a row returned as `completed` after exceeding the evaluator's 25-second limit. It is a runner/pipeline cancellation defect, not normal latency.
- Thai: `MB-1099-SF-130` 887.2689s | `pipeline:request_timeout_no_answer`
- English: `EN-SHADOW-0608` 7902.7385s | `pipeline:request_timeout_no_answer`

## Limits

- A watchdog timeout is a runner observation, not a response delivered to a user.
- Direct Thai-English score comparison is limited because the English Shadow is machine-translated and has its own contract.
