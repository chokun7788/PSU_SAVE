# Supervised Thai-English 1,600 Evaluation Analysis

> English is a machine-translated Shadow corpus. These results measure current pipeline behavior and contract compliance, not human-approved translation quality.

## Summary

| Suite | Strict pass | Observed P95 | Observed >=10s | Watchdog escape | Raw max | Harness timeout | Worker crash |
|---|---:|---:|---:|---:|---:|---:|---:|
| Thai | 1385/1600 (86.56%) | 10.280s | 91 | 1 | 69546.688s | 1 | 0 |
| English | 1154/1600 (72.12%) | 2.913s | 1 | 0 | 10.689s | 0 | 0 |

## Thai-English Parity

- Shared case IDs: 1600
- Route category mismatches: 491
- Large bullet-format gaps: 486
- One language passed while the other failed: 295

## Leading Failures

### Thai
- `missing_any`: 173
- `category`: 50
- `mode`: 5
- `missing`: 2
- `validation`: 1
- `harness_timeout`: 1

### English
- `category`: 446

## Slowest Cases

### Thai

- `MB-1505-GL-180` 69546.6882s | `pipeline:no_answer` | server กับ client ต่างกันยังไง เขียนเป็นภาษาไทยธรรมชาติ
- `MB-1518-GL-193` 22.012s | `harness_timeout` | API คืออะไร ขอแบบเป็นทางการ
- `MB-1479-GL-154` 19.4199s | `pipeline:general_llm_after_rag_miss` | JSON คืออะไร ตอบแบบสุภาพ
- `MB-1519-GL-194` 19.0678s | `pipeline:no_answer` | JSON คืออะไร ขอแบบเป็นทางการ
- `MB-1517-GL-192` 19.0652s | `pipeline:no_answer` | เฟรมเรตกับความละเอียดต่างกันยังไง ขอแบบเป็นทางการ
- `MB-0064-SF-064` 19.0483s | `pipeline:no_answer` | TEKKEN 8 ราคาเท่าไหร่
- `MB-1414-GL-089` 19.0309s | `pipeline:no_answer` | GPU คืออะไรแบบเข้าใจง่าย ขอแบบไม่ใช้ศัพท์ยาก
- `MB-1358-GL-033` 19.0295s | `pipeline:no_answer` | API คืออะไร ตอบเป็นภาษาไทย
- `MB-1378-GL-053` 19.0292s | `pipeline:no_answer` | API คืออะไร ขอ 1 ย่อหน้า
- `MB-1589-GL-264` 19.0283s | `pipeline:no_answer` | JSON คืออะไร ตอบแบบไม่ต้องมีตัวอย่างยาว
### English

- `EN-SHADOW-0052` 10.6891s | `pipeline:structured_equipment_catalog_en` | Which is more expensive, PS5 or Nintendo?
- `EN-SHADOW-0589` 3.4561s | `pipeline:structured_competition_rules_en` | How many games are played in the TEKKEN 8 finals round?
- `EN-SHADOW-0582` 3.4521s | `pipeline:structured_competition_rules_en` | What are the rules of competition in TEKKEN 8?
- `EN-SHADOW-0474` 3.3969s | `pipeline:structured_competition_rules_en` | What happens if I arrive late?
- `EN-SHADOW-0588` 3.3836s | `pipeline:structured_competition_rules_en` | What is the match format for TEKKEN 8?
- `EN-SHADOW-0543` 3.3473s | `pipeline:structured_competition_rules_en` | What is VALORANT's match format?
- `EN-SHADOW-0563` 3.2114s | `pipeline:structured_competition_rules_en` | Do I need to check in before playing CS2?
- `EN-SHADOW-0552` 3.2044s | `pipeline:structured_competition_rules_en` | What are the CS2 competition rules?
- `EN-SHADOW-0565` 3.1628s | `pipeline:structured_competition_rules_en` | What maps are available in CS2?
- `EN-SHADOW-0554` 3.161s | `pipeline:structured_competition_rules_en` | What happens if I arrive late for CS2?

## Watchdog-Control Observations

- `watchdog_escape_observed` means a row returned as `completed` after exceeding the evaluator's 25-second limit. It is a runner/pipeline cancellation defect, not normal latency.
- Thai: `MB-1505-GL-180` 69546.6882s | `pipeline:no_answer`

## Limits

- A watchdog timeout is a runner observation, not a response delivered to a user.
- Direct Thai-English score comparison is limited because the English Shadow is machine-translated and has its own contract.
