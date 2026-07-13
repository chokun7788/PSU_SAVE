# Pipeline Ground Truth Evaluation

วันที่: 2026-07-06

## Summary

- Total: 369
- PASS: 366
- FAIL: 3
- ERROR: 0
- Pass rate: 99.19%
- Average latency: 0.0245s
- P95 latency: 0.0382s
- Keyword fail: 3
- Source fail: 3
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 233
- `pipeline:rag_direct_curated`: 130
- `pipeline:multi_question_splitter`: 3
- `pipeline:no_answer`: 2
- `pipeline:related_guidance_fast_path`: 1

## Route Category Distribution

- `competition_rules`: 363
- `multi_question`: 3
- `equipment`: 3

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_v2_derived_018 | competition_rules | `equipment` | มาสาย; ตัดสิทธิ์; competition_rules_cs2_psu_phuket_2026 | ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น: - เล่นเป็นกลุ่ม/ครอบครัวหน้าจอเดียว: Nintendo Switch Zone เพราะมีเกม Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Nintendo Switc... |
| competition_challenger_v2_derived_051 | competition_rules | `equipment` | 8.30; 8.40; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ |
| competition_challenger_v2_edge_027 | competition_rules | `equipment` | 15 นาที; ปรับแพ้; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_safe_related_guidance_comp_v2_20260706.jsonl`
