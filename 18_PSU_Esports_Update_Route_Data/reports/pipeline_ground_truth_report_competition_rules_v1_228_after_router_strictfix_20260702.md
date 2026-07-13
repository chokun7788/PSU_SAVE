# Pipeline Ground Truth Evaluation

วันที่: 2026-07-02

## Summary

- Total: 228
- PASS: 203
- FAIL: 25
- ERROR: 0
- Pass rate: 89.04%
- Average latency: 0.0133s
- P95 latency: 0.0232s
- Keyword fail: 23
- Source fail: 15
- Quality fail: 1
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 208
- `pipeline:rag_direct_curated`: 12
- `pipeline:games_fast_path`: 5
- `pipeline:category_rule_fast_path`: 2
- `pipeline:schedule_fast_path`: 1

## Route Category Distribution

- `competition_rules`: 208
- `games`: 5
- `service_fee`: 5
- `general`: 5
- `penalty`: 2
- `schedule`: 1
- `contact`: 1
- `knowledge`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_v1_027 | competition_rules | `games` | Single Elimination; BO3; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_033 | competition_rules | `competition_rules` | Single Elimination; BO3 | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_v1_035 | competition_rules | `games` | Single Elimination; BO3; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_044 | competition_rules | `service_fee` | Technical Pause; 2 ครั้ง; 10 นาที; Tactical Timeout; 4 ครั้ง; 30 วินาที; competition_rules_cs2_psu_phuket_2026 | หากพบปัญหาการใช้งาน พฤติกรรมที่ไม่เหมาะสม หรือข้อกังวลใด ๆ ควรแจ้งเจ้าหน้าที่ทันที แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| competition_v1_046 | competition_rules | `competition_rules` | quality first sentence mismatch: ต่างกัน | คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tact... |
| competition_v1_048 | competition_rules | `schedule` | Technical Pause; 2 ครั้ง; 10 นาที; Tactical Timeout; 4 ครั้ง; 30 วินาที; competition_rules_cs2_psu_phuket_2026 | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| competition_v1_057 | competition_rules | `games` | 5 คน; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_058 | competition_rules | `service_fee` | VALORANT; 5 คน; competition_rules_valorant_psu_phuket_2026 | ค่าบริการ PlayStation 5 ต่อ 60 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 50 บาท, บุคคลทั่วไป 150 บาท แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Stud... |
| competition_v1_067 | competition_rules | `competition_rules` | Abyss; Ascent; Sunset | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
| competition_v1_077 | competition_rules | `service_fee` | Tactical Timeout; 2 ครั้ง; 60 วินาที; Overtime; competition_rules_valorant_psu_phuket_2026 | บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/upl... |
| competition_v1_088 | competition_rules | `service_fee` | Emergency; 1 ครั้ง; 10 นาที; competition_rules_valorant_psu_phuket_2026 | บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/upl... |
| competition_v1_093 | competition_rules | `competition_rules` | Emergency; 10 นาที | คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข... |
| competition_v1_094 | competition_rules | `competition_rules` | Emergency; 10 นาที | คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข... |
| competition_v1_095 | competition_rules | `competition_rules` | Emergency; 10 นาที | คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข... |
| competition_v1_105 | competition_rules | `competition_rules` | Agent; 2 สัปดาห์; 4 สัปดาห์ | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_v1_114 | competition_rules | `general` | ฝ่ายละ 5 คน; ยังไม่พบจำนวนสมาชิกทีม | คำตอบ: 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode) อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล่งข้อมูล: loca... |
| competition_v1_117 | competition_rules | `general` | ฝ่ายละ 5 คน; ยังไม่พบจำนวนสมาชิกทีม | คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน รายละเอียดที่เกี่ยวข้อง: - 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament... |
| competition_v1_137 | competition_rules | `penalty` | 15 นาที; ปรับแพ้; competition_rules_rov_blueket_2025_men | ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500 – 2,000 บาท แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| competition_v1_150 | competition_rules | `service_fee` | 5 ครั้ง; 1 นาที; competition_rules_rov_blueket_2025_men | คำถามที่ใช้คำว่า ศิษย์เก่า PSU, alumni, General Student, นักศึกษาทั่วไป, นักเรียนทั่วไป, นักศึกษาต่างมหาวิทยาลัย, นักเรียนต่างมหาวิทยาลัย, นักศึกษาต่างมหาลัย, นักเรียนต่างมหาลัย, เด็กต่างมหาลัย, ต่างมหาลัย, นักศึกษาจากมห... |
| competition_v1_175 | competition_rules | `contact` | โทรศัพท์มือถือ; ไม่อนุญาต; Tablet; iPad; competition_rules_rov_blueket_2025_men | เบอร์ติดต่อที่ปรากฏในระบบจองคือ +66 7627 6004 และ +66 7627 6045 แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| competition_v1_185 | competition_rules | `games` | 1v1; FT2; 60 วินาที; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_192 | competition_rules | `competition_rules` | 1v1; FT2; 60 วินาที | คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5 หลักฐานจากกติกา: - เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5 อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competit... |
| competition_v1_198 | competition_rules | `knowledge` | PlayStation 5; competition_rules_tekken8_psu_esports | อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge |
| competition_v1_203 | competition_rules | `games` | competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_221 | competition_rules | `penalty` | ไม่อนุญาต; Pause; แพ้ 1 Round; competition_rules_tekken8_psu_esports | ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100 – 500 บาท แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_rules_v1_228_after_router_strictfix_20260702.jsonl`
