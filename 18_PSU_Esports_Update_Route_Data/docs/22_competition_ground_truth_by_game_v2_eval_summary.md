# Competition Ground Truth By Game V2 - Evaluation Summary

วันที่: 2026-07-03

## สิ่งที่สร้าง

สร้าง Ground Truth ชุดใหม่สำหรับกติกาการแข่งขันแบบแยกเกม โดยเน้นคำถามที่หลากหลายกว่าเดิม ไม่ใช่การเปลี่ยนคำเล็กน้อยจากคำถามเดียว

ไฟล์ที่สร้าง:

- `data\ground_truth\competition_by_game_v2\ground_truth_competition_cs2_v2_diverse.jsonl`
- `data\ground_truth\competition_by_game_v2\ground_truth_competition_rov_v2_diverse.jsonl`
- `data\ground_truth\competition_by_game_v2\ground_truth_competition_valorant_v2_diverse.jsonl`
- `data\ground_truth\competition_by_game_v2\ground_truth_competition_tekken8_v2_diverse.jsonl`
- `data\ground_truth\competition_by_game_v2\ground_truth_competition_all_games_v2_diverse.jsonl`

จำนวนข้อ:

- Counter-Strike 2: 48 ข้อ
- Arena of Valor (RoV): 48 ข้อ
- VALORANT: 48 ข้อ
- Tekken 8: 40 ข้อ
- รวมทั้งหมด: 184 ข้อ

ไฟล์ generator:

- `tools\build_competition_ground_truth_by_game_v2.py`

เอกสารรายละเอียดชุดข้อมูล:

- `docs\21_competition_ground_truth_by_game_v2.md`

## แนวคิดการออกแบบคำถาม

ชุดนี้ตั้งใจให้ครอบคลุมหลาย intent ต่อเกม เช่น:

- team_size
- format
- schedule
- schedule_location
- map_pool
- game_setting
- pause
- timeout
- rematch
- equipment
- area_rules
- penalty
- character/skin
- bug_rule
- policy
- summary

หลักการสำคัญ:

- คำถามที่เป็น paraphrase ของ fact เดียวกันจำกัดไว้ประมาณ 2-3 ข้อ
- เพิ่มคำถามใหม่ที่ถามคนละมุม เช่น เวลาแข่ง, สถานที่, อุปกรณ์, การตั้งค่า, โทษ, ข้อห้าม, การสรุปหลายประเด็น
- ใช้ `expected_keywords` แบบไม่ยาวเกินไป แต่ยังบังคับให้คำตอบต้องมีแก่นข้อมูลจริง
- ใช้ `expected_source_keywords` เป็น document id ของเกม เพื่อจับว่าระบบดึงเอกสารถูกเกมหรือไม่

## ผลรัน Pipeline ปัจจุบัน

รันด้วย:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_by_game_v2\ground_truth_competition_all_games_v2_diverse.jsonl --label competition_by_game_v2_all_20260703
```

ผลรวม:

- Total: 184
- PASS: 41
- FAIL: 143
- Pass rate: ประมาณ 22.28%

ผลแยกเกม:

| Game | Total | PASS | FAIL |
|---|---:|---:|---:|
| Counter-Strike 2 | 48 | 9 | 39 |
| RoV | 48 | 13 | 35 |
| VALORANT | 48 | 10 | 38 |
| Tekken 8 | 40 | 9 | 31 |

รายงานผลรัน:

- `reports\pipeline_ground_truth_report_competition_by_game_v2_all_20260703.md`
- `reports\pipeline_ground_truth_results_competition_by_game_v2_all_20260703.jsonl`
- `reports\pipeline_ground_truth_report_competition_by_game_v2_cs2_20260703.md`
- `reports\pipeline_ground_truth_report_competition_by_game_v2_rov_20260703.md`
- `reports\pipeline_ground_truth_report_competition_by_game_v2_valorant_20260703.md`
- `reports\pipeline_ground_truth_report_competition_by_game_v2_tekken8_20260703.md`

## สิ่งที่ผลรันบอกเรา

ผล fail เยอะไม่ได้แปลว่า Ground Truth ชุดนี้เสียเป็นหลัก แต่สะท้อนว่า pipeline ปัจจุบันยังถูกออกแบบมารองรับเฉพาะ fact card หลักๆ เช่น:

- จำนวนผู้เล่น
- map pool บางเกม
- format หลักบางเกม
- pause/timeout บางแบบ
- equipment หลักบางข้อ

แต่คำถามชุดใหม่เริ่มถามลึกขึ้น เช่น:

- CS2 ใช้ Steam/latest version หรือห้ามดัดแปลงเกมไหม
- CS2 round time, freeze time, start money, overtime
- RoV ตารางแข่งรายช่วงเวลา
- RoV Global Ban/Pick, hero 18 ตัว, break time, โทษ pause ผิดครั้งที่ 1-3
- VALORANT bug classification, rollback, Cypher camera, KAY/O exception
- VALORANT setting เลือด/ศพ/FPS graph
- Tekken 8 FT2, stage random, advantage, Assist, customization, dispute

คำถามพวกนี้มีข้อมูลจริงอยู่ใน `competition_rule_chunks.jsonl` แต่ยังไม่ได้ถูกยกเป็น fact card ที่ pipeline ด่วนเข้าใจได้ดีพอ

## สาเหตุหลักของการตอบผิด

### 1. Router หลุดหมวด

บางคำถามมีชื่อเกม แต่ router กลับส่งไปหมวดอื่น เช่น:

- `games`
- `schedule`
- `service_fee`
- `events_news`
- `rules`

ตัวอย่าง:

- `VALORANT Match Prep มีคนได้ไม่เกินกี่คน` หลุดไป `games_fast_path`
- `CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม` หลุดไป `games_fast_path`
- `PSU Phuket CS2 2026 รับเฉพาะนักศึกษาแบบไหน` หลุดไป `events_news`

สาเหตุคือ route เดิมเห็นคำว่าเกม/รายการ/PSU แล้วบางครั้งให้ route ทั่วไปชนะ route competition_rules

### 2. Fact Card ยังไม่พอ

ตอนนี้ fact card ของ competition rules ยังมีประมาณ 20 ใบ จึงครอบคลุมเฉพาะคำถามยอดนิยม ไม่พอสำหรับคำถามลึก 184 ข้อ

เมื่อไม่มี fact card ตรง ระบบมักหยิบ fact card ที่ใกล้ที่สุด เช่น:

- ถามเวลาแข่ง RoV แต่ตอบเรื่อง rematch/pause
- ถาม setting Tekken แต่ตอบ format หลัก
- ถาม penalty ย่อยของ VALORANT แต่ตอบ pause หรือ map pool

### 3. Competition fact card confidence สูงเกินแม้ intent ไม่ตรง

ระบบให้คะแนน fact card จากคำร่วม เช่น ชื่อเกม + แข่ง + กติกา ทำให้แม้ intent ไม่ตรงก็ยังได้ confidence สูงพอจะตอบ

ผลคือ LLM/RAG จาก chunk ไม่ค่อยได้มีโอกาสช่วย เพราะ pipeline หยุดที่ fact card ก่อน

### 4. RAG ยังเป็น lexical fallback ไม่ใช่ semantic retrieval ที่แข็งแรงพอ

ข้อมูล chunk มีอยู่ แต่ retrieval แบบ lexical ยังไม่สามารถดึง chunk ที่ตรงที่สุดได้สม่ำเสมอ โดยเฉพาะคำถามที่ถามแบบภาษาคนทั่วไป

ตัวอย่าง:

- `วาโล agent ใหม่ใช้ได้ทันทีไหม`
- `Tekken 8 ถ้าเสมอกัน 1-1 ต้องทำอะไร`
- `RoV เครื่องร้อนพักได้กี่นาที`

คำถามเหล่านี้ควรดึง chunk ที่มีคำตอบตรงๆ ได้ แต่ปัจจุบัน route/fact card อาจตัดสินก่อน

### 5. ตัวตรวจยังเป็น keyword แบบ AND ทั้งหมด

บางข้อ AI อาจตอบถูกในเชิงความหมาย แต่ fail เพราะ keyword ไม่ตรง phrasing

ตัวอย่าง:

- เฉลยคาด `ชนะครบ 2 เกม`
- AI ตอบ `First to 2 (FT2)`

กรณีนี้ถือว่าคำตอบพอใช้ได้ แต่ตัวตรวจ strict keyword ยัง fail ซึ่งดีสำหรับการจับความไม่ครบ แต่ควรเพิ่มระบบ synonym/acceptable keywords ในอนาคต

## สรุปคุณภาพชุด Ground Truth

ชุดนี้เหมาะสำหรับใช้เป็นชุดทดสอบรอบใหม่ เพราะ:

- แยกเกมชัดเจน
- มีคำถามหลากหลายกว่าเดิม
- มีคำถามที่ใช้ทดสอบ router, fact card, RAG และ answer formatting
- เปิดให้เห็นช่องว่างของระบบปัจจุบันชัดมาก

ชุดนี้ยังไม่ใช่ชุดที่ระบบควรผ่าน 100% ทันที แต่เป็นชุดที่ใช้ขับการพัฒนา pipeline รอบถัดไปได้ดี

## แผนแก้รอบต่อไป

### Step 1: เพิ่ม Competition Fact Cards จาก Ground Truth

ควรเพิ่ม fact cards เพิ่มเติมจาก source chunks สำหรับหัวข้อที่ถามบ่อยและต้องตอบเร็ว เช่น:

- CS2 game settings: round time, freeze time, start money, bomb timer, max round, overtime
- CS2 area rules: mobile, notes, sealed water, match prep 6 players
- RoV schedule: วันที่, เวลาแต่ละรอบ, สถานที่
- RoV hero rules: 18 heroes, Global Ban/Pick, Default Skin, duplicate hero
- RoV pause/rematch/penalty detail
- VALORANT match prep, content restriction, map ban, side selection
- VALORANT bug/rollback/penalty detail
- Tekken 8 FT2, R3, timer, stage random, advantage
- Tekken 8 character/customization/Assist/pause/dispute

### Step 2: ปรับ Router ให้ competition_rules ชนะเมื่อมีชื่อเกม + คำกติกา

ถ้าคำถามมีชื่อเกม เช่น CS2, RoV, VALORANT, Tekken และมีคำอย่าง:

- แข่ง
- กติกา
- ลงโทษ
- pause
- map
- รอบ
- อุปกรณ์
- ใช้ได้ไหม
- โดนอะไร
- ต้องทำยังไง

ควร route ไป `competition_rules` ก่อน ไม่ให้หลุดไป `games`, `schedule`, `service_fee`, `events_news`

### Step 3: เพิ่ม Intent Detection ภายใน competition_rules

ควรแยก intent ย่อยเพิ่ม เช่น:

- schedule
- game_setting
- area_rules
- bug_rule
- checkin
- post_match
- dispute
- hero_rule
- side_selection
- break_time

ตอนนี้ intent หลักมีไม่พอ ทำให้ fact card ที่คนละหมวดได้คะแนนสูงเกิน

### Step 4: ถ้า fact card ไม่ตรง intent ให้ fallback ไป RAG chunk

ควรเพิ่ม rule:

- ถ้า top fact card intent ไม่ตรง intent_hint
- หรือคะแนน top กับอันดับ 2 ใกล้กันมาก
- หรือคำตอบจาก fact card ไม่มี keyword สำคัญของ intent

ให้ไปดึง `competition_rule_chunks.jsonl` แทน แล้วค่อยสรุปด้วย LLM/RAG

### Step 5: เพิ่ม acceptable keyword groups ใน evaluator

เพื่อให้ตรวจคำตอบที่ถูกเชิงความหมายแต่ใช้คนละคำ เช่น:

- `First to 2` เทียบเท่า `ชนะครบ 2 เกม`
- `BO3` เทียบเท่า `Best of 3`
- `Round 3` เทียบเท่า `3 รอบ`
- `Map Forfeit` เทียบเท่า `ปรับแพ้ในแผนที่`

ยังควร strict อยู่ แต่ควร strict แบบมี synonym group ไม่ใช่ keyword เดียวตายตัว

## คำสั่งที่ใช้บ่อย

สร้าง Ground Truth ใหม่:

```powershell
py -3 tools\build_competition_ground_truth_by_game_v2.py
```

รันรวมทุกเกม:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_by_game_v2\ground_truth_competition_all_games_v2_diverse.jsonl --label competition_by_game_v2_all_20260703
```

รันแยกเกม:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_by_game_v2\ground_truth_competition_cs2_v2_diverse.jsonl --label competition_by_game_v2_cs2_20260703
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_by_game_v2\ground_truth_competition_rov_v2_diverse.jsonl --label competition_by_game_v2_rov_20260703
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_by_game_v2\ground_truth_competition_valorant_v2_diverse.jsonl --label competition_by_game_v2_valorant_20260703
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_by_game_v2\ground_truth_competition_tekken8_v2_diverse.jsonl --label competition_by_game_v2_tekken8_20260703
```
