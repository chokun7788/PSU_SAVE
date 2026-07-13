# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 369
- PASS: 367
- FAIL: 2
- ERROR: 0
- Pass rate: 99.46%
- Average latency: 0.0260s
- P95 latency: 0.0392s
- Keyword fail: 2
- Source fail: 2
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 235
- `pipeline:rag_direct_curated`: 132
- `pipeline:games_availability_fast_path`: 2

## Route Category Distribution

- `competition_rules`: 367
- `games`: 2

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_v2_edge_083 | competition_rules | `games` | 3 รอบ; competition_rules_tekken8_psu_esports | มีครับ TEKKEN 8 อยู่ในรายการเกมที่ยืนยันได้ของ PC Zone และ PlayStation 5 Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games |
| competition_challenger_v2_edge_102 | competition_rules | `games` | เกมตัดสิน; competition_rules_tekken8_psu_esports | มีครับ TEKKEN 8 อยู่ในรายการเกมที่ยืนยันได้ของ PC Zone และ PlayStation 5 Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v2_equipment_game_catalog_fix3_20260704.jsonl`
