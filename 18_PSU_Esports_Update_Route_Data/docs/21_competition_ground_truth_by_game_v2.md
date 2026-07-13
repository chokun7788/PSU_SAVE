# Competition Ground Truth By Game V2

ชุดนี้สร้างเพื่อทดสอบคำถามกติกาการแข่งขันแบบแยกเกม โดยเน้นความหลากหลายของ intent มากกว่าการ paraphrase คำถามเดิมซ้ำหลายรอบ

## Files

- `Counter-Strike 2`: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_by_game_v2\ground_truth_competition_cs2_v2_diverse.jsonl` (48 ข้อ)
- `Arena of Valor (RoV)`: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_by_game_v2\ground_truth_competition_rov_v2_diverse.jsonl` (48 ข้อ)
- `VALORANT`: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_by_game_v2\ground_truth_competition_valorant_v2_diverse.jsonl` (48 ข้อ)
- `Tekken 8`: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_by_game_v2\ground_truth_competition_tekken8_v2_diverse.jsonl` (40 ข้อ)
- รวมทุกเกม: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_by_game_v2\ground_truth_competition_all_games_v2_diverse.jsonl` (184 ข้อ)

## Intent Distribution

### Counter-Strike 2
- `game_setting`: 8
- `equipment`: 5
- `eligibility`: 4
- `pause`: 4
- `area_rules`: 4
- `map_pool`: 3
- `penalty`: 3
- `team_size`: 2
- `game_version`: 2
- `language`: 2
- `schedule_location`: 2
- `communication`: 2
- `format`: 2
- `roster_change`: 1
- `registration`: 1
- `schedule`: 1
- `late_start`: 1
- `side_selection`: 1

### Arena of Valor (RoV)
- `schedule`: 9
- `penalty`: 8
- `pause`: 5
- `hero_rule`: 4
- `rematch`: 4
- `format`: 3
- `equipment`: 3
- `side_selection`: 2
- `late_start`: 2
- `break_time`: 2
- `team_size`: 2
- `schedule_location`: 1
- `match_process`: 1
- `skin`: 1
- `summary`: 1

### VALORANT
- `pause`: 10
- `penalty`: 8
- `character`: 5
- `bug_rule`: 5
- `area_rules`: 4
- `map_pool`: 4
- `equipment`: 4
- `team_size`: 2
- `game_setting`: 2
- `checkin`: 1
- `side_selection`: 1
- `post_match`: 1
- `summary`: 1

### Tekken 8
- `game_setting`: 7
- `format`: 6
- `pause`: 6
- `character`: 5
- `penalty`: 5
- `policy`: 4
- `summary`: 3
- `dispute`: 2
- `equipment`: 1
- `skin`: 1

## Design Notes

- คำถามที่มีความหมายใกล้กันมากถูกจำกัดไว้ประมาณ 2-3 ข้อต่อ fact สำคัญ
- เพิ่มคำถามแบบสรุปหลายประเด็น เพื่อทดสอบว่าระบบตอบรวมหลาย fact ได้หรือไม่
- เพิ่มคำถามเชิง policy เช่น `ได้ไหม`, `โดนอะไร`, `ควรตอบว่าอะไร` เพื่อทดสอบคำตอบที่ต้องไม่มั่ว
- ใช้ `expected_keywords` แบบพอเหมาะ ไม่ล็อกยาวเกินไป แต่ยังบังคับให้คำตอบต้องมีแก่นข้อมูลจริง
- ใช้ `expected_source_keywords` เป็น document id ของเกม เพื่อให้ตัวตรวจจับว่าดึงเอกสารเกมถูกหรือไม่

## Next Check

รันตรวจด้วย:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_by_game_v2\ground_truth_competition_all_games_v2_diverse.jsonl --label competition_by_game_v2_all
```
