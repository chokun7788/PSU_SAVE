# LLM Shadow Critic + Failure Analyst Report

- Generated: `2026-08-04T20:31:22`
- Input: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\real_usage_golden_v1.jsonl`
- Cases: `1`
- Chatbot LLM enabled: `False`
- Shadow Critic LLM enabled: `True`
- Shadow Critic model: `qwen2.5:3b`

## Summary

- Pass rate: **0.00%**
- Failure/review rate: **100.00%**
- Verdicts: `{"needs_review": 1}`
- Average latency: `1.4097s`
- P95 latency: `1.4097s`
- Max latency: `1.4097s`
- Pipeline LLM calls: `0`
- Cases reviewed by Critic LLM: `0`

## Failure Labels

- ไม่พบ failure label จากชุดตรวจนี้

## Failure Cases (สูงสุด 30 ข้อ)

### `RG-SF-001` - ราคา PC ต่อชั่วโมงเท่าไหร่
- Verdict: `needs_review` / Severity: `low`
- Labels: ``
- Route: `service_fee/service_fee_query` | Mode: `pipeline:deterministic_calculator_fast`
- Reason: shadow critic LLM unavailable; deterministic checks did not find a failure
- Suggested fix: -
- Answer: ราคา PC 1 ชั่วโมง (1 คน) •    PSU Student and Staff: 0 บาท •    PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท •    General Adult / บุคคลทั่วไป: 70 บาท หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27 แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

