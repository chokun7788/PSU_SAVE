# Broad Usage Eval v1

- Generated at: 2026-07-30T15:59:12
- Cases: 40
- Turn checks: 40
- Passed: 39
- Failed: 1
- Pass rate: 0.975
- Total wall sec: 0.941
- Allow LLM: False
- RAG fallback: False

## By Group
- service_fee: 39/40 pass, 1 fail

## By Strategy
- compound: 40

## Common Problems
- missing 'PS5': 1

## Top Failures

### SF-011 service_fee
- Question: PS5 ราคาเท่าไหร่
- Resolved: -
- Mode: `pipeline:deterministic_calculator_fast`
- Route: `service_fee/service_fee_query`
- Problems: missing 'PS5'
- Answer: PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน) •    PSU Student and Staff: 0 บาท •    PSU Alumni and General Student: 50 บาท •    General Adult: 150 บาท แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FE...
