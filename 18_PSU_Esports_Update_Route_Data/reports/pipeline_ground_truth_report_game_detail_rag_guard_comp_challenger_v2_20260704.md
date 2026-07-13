# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 369
- PASS: 366
- FAIL: 3
- ERROR: 0
- Pass rate: 99.19%
- Average latency: 0.0260s
- P95 latency: 0.0395s
- Keyword fail: 3
- Source fail: 3
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 235
- `pipeline:rag_direct_curated`: 131
- `pipeline:competition_game_list_fast_path`: 2
- `pipeline:game_detail_fast_path`: 1

## Route Category Distribution

- `competition_rules`: 366
- `games`: 3

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_v2_derived_026 | competition_rules | `games` | ฝั่งละ 3 รอบ; 4 ใน 6; $10,000; competition_rules_cs2_psu_phuket_2026 | Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม แนวเกม: เกมยิง Tactical FPS วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาว... |
| competition_challenger_v2_derived_028 | competition_rules | `games` | Ancient; Anubis; Dust 2; Train; competition_rules_cs2_psu_phuket_2026 | เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้: - Counter-Strike 2: PSU Phuket CS2 2026 Tournament - VALORANT: PSU Phuket VALORANT 2026 Tournament - Arena of Valor (RoV): Blueket Games 2025 ประเภททีมชาย - TEKKEN 8: P... |
| competition_challenger_v2_derived_093 | competition_rules | `games` | ลงทะเบียน; รอบรอง; รอบชิง; competition_rules_rov_blueket_2025_men | เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้: - Counter-Strike 2: PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_game_detail_rag_guard_comp_challenger_v2_20260704.jsonl`
