# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 369
- PASS: 368
- FAIL: 1
- ERROR: 0
- Pass rate: 99.73%
- Average latency: 0.0238s
- P95 latency: 0.0364s
- Keyword fail: 1
- Source fail: 1
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 236
- `pipeline:rag_direct_curated`: 132
- `pipeline:games_unknown_fast_path`: 1

## Route Category Distribution

- `competition_rules`: 368
- `games`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_v2_edge_044 | competition_rules | `games` | อาคาร; 5102A; competition_rules_rov_blueket_2025_men | ยังไม่พบ Aov ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ถ้าต้องการเล่นเกมนอกเหนือจากรายการนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ เกมที่มีข้อมูลยืนยันตอนนี้: - PC Zone: VALORANT, Counter-Str... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v2_game_zone_fix_20260704.jsonl`
