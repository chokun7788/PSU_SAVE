# Competition Challenger Ground Truth V2

ชุดนี้สร้างเพื่อกดดัน pipeline ด้วยคำถามภาษาคนจริงมากขึ้น โดยยังใช้เฉลย/keyword ที่ตรวจได้จากกติกาเดิม

## Files

- Ground truth: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl`

## Summary

- Total: 369
- Derived from stable/previous GT: 264
- New edge-style questions: 105

## Game Distribution

- VALORANT: 100
- Arena of Valor (RoV): 95
- Counter-Strike 2: 89
- Tekken 8: 85

## Top Intent Distribution

- pause: 61
- penalty: 48
- format: 30
- game_setting: 30
- equipment: 29
- character: 17
- schedule: 15
- map_pool: 12
- area_rules: 12
- team_size: 11
- hero_rule: 11
- bug_rule: 10
- schedule_location: 9
- policy: 9
- late_start: 7
- side_selection: 7
- break_time: 7
- roster_change: 6
- rematch: 6
- registration: 5

## Final Evaluation Reference

หลังจากรันและแก้ pipeline หลายรอบ ผล final วันที่ 2026-07-04 ผ่านครบ:

- Challenger V2: 369/369
- Challenger V1 regression: 80/80
- Competition by-game V2 regression: 184/184

ดูรายละเอียดสาเหตุ/สิ่งที่แก้/ข้อควรระวังได้ที่:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\docs\28_competition_challenger_v2_eval_audit_20260704.md`
