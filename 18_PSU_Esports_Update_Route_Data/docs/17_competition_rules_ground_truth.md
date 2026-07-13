# Competition Rules Ground Truth

วันที่สร้าง: 2026-07-02

เอกสารนี้สรุป Ground Truth ชุดแยกสำหรับคำถามกติกาการแข่งขัน/รายการแข่งขันของ PSU Esports Studio - Phuket

ชุดนี้แยกจาก Ground Truth v2 360 ข้อเดิม เพราะต้องการทดสอบเฉพาะหมวด:

```text
competition_rules
```

## ไฟล์ที่สร้าง

Ground Truth:

```text
data/ground_truth/ground_truth_competition_rules_v1_228.jsonl
```

Generator:

```text
tools/build_competition_ground_truth.py
```

Verbose evaluator สำหรับ notebook:

```text
tools/notebook_ground_truth_verbose.py
```

Notebook ที่ใส่ cell รันไว้แล้ว:

```text
notebooks/02_test_final_pipeline.ipynb
```

## จำนวนข้อ

ทั้งหมด 228 ข้อ

ครอบคลุม 4 เกม/รายการ:

- Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
- VALORANT / PSU Phuket VALORANT 2026 Tournament
- Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
- Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ

## หัวข้อที่ครอบคลุม

### CS2

- ทีมละกี่คน
- map pool
- Single Elimination / BO3
- Technical Pause / Tactical Timeout

### VALORANT

- ทีมละกี่คน
- map pool
- Tactical Timeout
- Emergency/Technical Pause
- Agent ใหม่ / map ใหม่

### RoV

- 5v5 / จำนวนคนที่ลงแข่งพร้อมกัน
- Default Skin
- เริ่มแข่งช้าเกิน 15 นาที
- Pause / Disconnect
- Rematch / First Blood / 2 นาที
- อุปกรณ์ที่ใช้แข่ง / มือถือ / ห้าม Tablet/iPad

### Tekken 8

- รูปแบบ 1v1 / FT2 / R3 / 60 วินาที
- Platform PlayStation 5
- DLC character / customization
- Pause penalty / แพ้ 1 Round

## Schema

ตัวอย่าง 1 แถว:

```json
{
  "id": "competition_v1_001",
  "category": "competition_rules",
  "game": "Counter-Strike 2",
  "intent": "team_size",
  "question": "CS2 แข่งทีมละกี่คน",
  "expected_keywords": ["CS2", "ผู้เล่น 5 คน"],
  "expected_source_keywords": ["competition_rules_cs2_psu_phuket_2026"],
  "answer_type": "fact",
  "difficulty": "medium",
  "variant_type": "competition_team_size",
  "source_fact_key": "cs2_team_size",
  "expected_mode_prefix": "pipeline:competition_fact_card"
}
```

## วิธีสร้างไฟล์ใหม่

ถ้าแก้ generator แล้วอยากสร้าง JSONL ใหม่:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\build_competition_ground_truth.py
```

## วิธีรันเช็คแบบปกติ

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\ground_truth_competition_rules_v1_228.jsonl --label competition_rules_v1_228
```

ผลลัพธ์จะอยู่ที่:

```text
reports/pipeline_ground_truth_report_competition_rules_v1_228.md
reports/pipeline_ground_truth_results_competition_rules_v1_228.jsonl
```

## วิธีรันใน Notebook แบบเรียงข้อ

เพิ่ม cell ไว้แล้วใน:

```text
notebooks/02_test_final_pipeline.ipynb
```

หัวข้อ:

```text
11. Ground Truth แยกสำหรับกติกาการแข่งขัน
```

โค้ดหลัก:

```python
competition_gt_path = PROJECT_ROOT / "data" / "ground_truth" / "ground_truth_competition_rules_v1_228.jsonl"

competition_gt_rows = run_ground_truth_verbose_display(
    competition_gt_path,
    label="competition_rules_v1_228_verbose",
    start=1,
    limit=None,
    show_pass=True,
    only_fail=False,
)
```

ถ้าต้องการดูเฉพาะข้อผิด:

```python
competition_gt_rows = run_ground_truth_verbose_display(
    competition_gt_path,
    label="competition_rules_v1_228_fail_only",
    only_fail=True,
)
```

## ผลรันล่าสุด

คำสั่งที่รัน:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\ground_truth_competition_rules_v1_228.jsonl --label competition_rules_v1_228_smoke
```

ผล:

```text
Total: 228
PASS: 186
FAIL: 42
```

ไฟล์ report:

```text
reports/pipeline_ground_truth_report_competition_rules_v1_228_smoke.md
reports/pipeline_ground_truth_results_competition_rules_v1_228_smoke.jsonl
```

Verbose report:

```text
reports/pipeline_ground_truth_verbose_report_competition_rules_v1_228_verbose.md
reports/pipeline_ground_truth_verbose_results_competition_rules_v1_228_verbose.jsonl
```

## วิเคราะห์ข้อที่ Fail

Fail 42 ข้อส่วนใหญ่เป็นประโยชน์ต่อการพัฒนาต่อ ไม่ใช่ Ground Truth ผิดทั้งหมด

กลุ่มปัญหาหลัก:

1. Router ไปหมวด `games` แทน `competition_rules`

ตัวอย่าง:

```text
Tekken 8 platform อะไร
CS2 เป็น Single Elimination ไหม
```

สาเหตุคือคำถามมีชื่อเกม แต่บางคำยังดูเหมือนถามรายการเกม/เครื่องเล่นมากกว่ากติกา

แนวทางแก้:

- เพิ่ม route terms เช่น `platform`, `Single Elimination`, `BO`, `FT2`, `roster`
- ถ้ามีชื่อเกมการแข่งขัน + คำพวก format/platform/pause/map ให้ bias ไป `competition_rules`

2. Router ไปหมวด `service_fee` เพราะมีคำว่า `เท่าไหร่`

ตัวอย่าง:

```text
CS2 ถ้าเครื่องมีปัญหาขอ pause ได้เท่าไหร่
VALORANT timeout ต่อแผนที่ได้เท่าไหร่
```

สาเหตุคือ `เท่าไหร่` ถูกมองเป็นราคา แม้บริบทคือจำนวนครั้ง/เวลาในกติกา

แนวทางแก้:

- ถ้ามีชื่อเกมแข่งขัน + pause/timeout/กติกา ให้ route กติกามาก่อนราคา

3. Fact card retrieval เลือก fact card ใกล้เคียงผิด

ตัวอย่าง:

```text
VALORANT ถ้า hardware มีปัญหาขอ pause ยังไง
```

ควรไป Emergency/Technical Pause แต่บางครั้งไป Tactical Timeout

แนวทางแก้:

- เพิ่ม intent ย่อย `technical_pause` แยกจาก `tactical_timeout`
- ให้ keyword `hardware`, `ฉุกเฉิน`, `emergency`, `technical` boost ไป card emergency

4. RoV บางคำถามไม่มี route signal พอ

ตัวอย่าง:

```text
RoV ใช้ tablet ได้ไหม
RoV disconnect ทำยังไง
```

แนวทางแก้:

- เพิ่ม `tablet`, `ipad`, `disconnect`, `หลุดเกม` เป็น rule terms สำหรับ competition route

## ใช้ชุดนี้ยังไง

ชุดนี้ควรใช้เป็น regression/challenge set หลังปรับ router หรือ fact card ทุกครั้ง

เป้าหมายระยะต่อไป:

- ให้ PASS เพิ่มจาก 186/228 เป็น 210+/228
- ลดเคสที่ route ไป `games`, `service_fee`, `schedule`, `general`
- แยก pause intent ให้ละเอียดขึ้น
- เพิ่ม fact card ใหม่สำหรับหัวข้อที่ยังไม่มี

## หมายเหตุ

Ground Truth ชุดนี้ตั้งใจมีคำถามแบบภาษาคนทั่วไปและคำถามก้ำกึ่ง เพื่อจับปัญหาในระบบจริง

ดังนั้นไม่ควรลบข้อ fail ทิ้งทันที แต่ควรดูว่า fail เพราะ:

- Ground Truth เขียนแคบเกินไป
- Router เข้า route ผิด
- Fact card scoring เลือกผิด
- Data ยังไม่มีจริง
- คำถามคลุมเครือและควรถามกลับ
