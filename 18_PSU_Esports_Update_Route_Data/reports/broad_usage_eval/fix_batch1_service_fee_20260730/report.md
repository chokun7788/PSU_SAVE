# Broad Usage Eval v1

- Generated at: 2026-07-30T16:56:23
- Cases: 88
- Turn checks: 88
- Passed: 87
- Failed: 1
- Pass rate: 0.9886
- Total wall sec: 7.776
- Allow LLM: False
- RAG fallback: False

## By Group
- service_fee: 87/88 pass, 1 fail

## By Strategy
- fast/rule: 58
- structured: 30

## Common Problems
- missing 'Nintendo Switch Sports': 1

## Top Failures

### SF-083 service_fee
- Question: Nintendo Switch Sports ราคาเท่าไหร่
- Resolved: -
- Mode: `pipeline:deterministic_calculator_fast`
- Route: `service_fee/service_fee_query`
- Problems: missing 'Nintendo Switch Sports'
- Answer: Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง) •    PSU Student and Staff: 0 บาท •    PSU Alumni and General Student: 50 บาท •    General Adult: 140 บาท  Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง) •    PSU Student and Staff: 0 บาท •    PSU Alumni and General Stude...
