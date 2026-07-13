# Pipeline Ground Truth Evaluation

วันที่: 2026-07-02

## Summary

- Total: 228
- PASS: 186
- FAIL: 42
- ERROR: 0
- Pass rate: 81.58%
- Average latency: 0.0129s
- P95 latency: 0.0230s
- Keyword fail: 38
- Source fail: 22
- Quality fail: 1
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 195
- `pipeline:rag_direct_curated`: 16
- `pipeline:games_fast_path`: 13
- `pipeline:schedule_fast_path`: 3
- `pipeline:category_rule_fast_path`: 1

## Route Category Distribution

- `competition_rules`: 195
- `games`: 13
- `general`: 11
- `service_fee`: 5
- `schedule`: 3
- `knowledge`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_v1_009 | competition_rules | `competition_rules` | ผู้เล่น 5 คน | คำตอบ: CS2 ใช้รูปแบบ Single Elimination โดยรอบรองชนะเลิศและรอบชิงชนะเลิศเป็น Best of 3 (BO3) หลักฐานจากกติกา: - เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3 อ้างอิงจากกติกา: Counter-Strik... |
| competition_v1_011 | competition_rules | `competition_rules` | ผู้เล่น 5 คน | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_v1_019 | competition_rules | `games` | Ancient; Anubis; Dust 2; Train; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_026 | competition_rules | `games` | Single Elimination; BO3; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_027 | competition_rules | `games` | Single Elimination; BO3; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_028 | competition_rules | `competition_rules` | Single Elimination; BO3 | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_v1_033 | competition_rules | `competition_rules` | Single Elimination; BO3 | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_v1_035 | competition_rules | `games` | Single Elimination; BO3; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_044 | competition_rules | `service_fee` | Technical Pause; 2 ครั้ง; 10 นาที; Tactical Timeout; 4 ครั้ง; 30 วินาที; competition_rules_cs2_psu_phuket_2026 | หากพบปัญหาการใช้งาน พฤติกรรมที่ไม่เหมาะสม หรือข้อกังวลใด ๆ ควรแจ้งเจ้าหน้าที่ทันที แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| competition_v1_046 | competition_rules | `competition_rules` | quality first sentence mismatch: ต่างกัน | คำตอบ: CS2 ขอ Technical Pause ได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที และ Tactical Timeout ได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10 นาที และ Tact... |
| competition_v1_048 | competition_rules | `schedule` | Technical Pause; 2 ครั้ง; 10 นาที; Tactical Timeout; 4 ครั้ง; 30 วินาที; competition_rules_cs2_psu_phuket_2026 | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| competition_v1_056 | competition_rules | `competition_rules` | 5 คน | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
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
| competition_v1_146 | competition_rules | `schedule` | 5 ครั้ง; 1 นาที; competition_rules_rov_blueket_2025_men | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| competition_v1_147 | competition_rules | `general` | 5 ครั้ง; 1 นาที | คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพ... |
| competition_v1_150 | competition_rules | `service_fee` | 5 ครั้ง; 1 นาที; competition_rules_rov_blueket_2025_men | คำถามที่ใช้คำว่า ศิษย์เก่า PSU, alumni, General Student, นักศึกษาทั่วไป, นักเรียนทั่วไป, นักศึกษาต่างมหาวิทยาลัย, นักเรียนต่างมหาวิทยาลัย, นักศึกษาต่างมหาลัย, นักเรียนต่างมหาลัย, เด็กต่างมหาลัย, ต่างมหาลัย, นักศึกษาจากมห... |
| competition_v1_155 | competition_rules | `general` | 5 ครั้ง; 1 นาที | คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause) รายละเอียดที่เกี่ยวข้อง: - ขอได้ 1 ครั้งต่อแผนที่ - รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน - กฎ... |
| competition_v1_165 | competition_rules | `general` | First Blood; 2 นาที | คำตอบ: 6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น รายละเอียดที่เกี่ยวข้อง: - 6.2.1.ห้ามผู้เข้าแข่งขันทุกคนใช้โปรแกรมช่วยหรือใน... |
| competition_v1_171 | competition_rules | `general` | โทรศัพท์มือถือ; ไม่อนุญาต; Tablet; iPad | คำตอบ: 4. ระเบียบและกติกาการแข่งขัน รายละเอียดที่เกี่ยวข้อง: - 4.1. กติกาพื้นฐาน - 4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น - 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสี... |
| competition_v1_174 | competition_rules | `general` | โทรศัพท์มือถือ; ไม่อนุญาต; Tablet; iPad | คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพ... |
| competition_v1_181 | competition_rules | `games` | 1v1; FT2; 60 วินาที; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_184 | competition_rules | `competition_rules` | 1v1; FT2; 60 วินาที | คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5 หลักฐานจากกติกา: - เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5 อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competit... |
| competition_v1_185 | competition_rules | `games` | 1v1; FT2; 60 วินาที; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_189 | competition_rules | `schedule` | 1v1; PlayStation 5; FT2; 60 วินาที; competition_rules_tekken8_psu_esports | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| competition_v1_190 | competition_rules | `games` | 1v1; FT2; 60 วินาที; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_191 | competition_rules | `games` | 1v1; FT2; 60 วินาที; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_192 | competition_rules | `competition_rules` | 1v1; FT2; 60 วินาที | คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5 หลักฐานจากกติกา: - เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5 อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competit... |
| competition_v1_195 | competition_rules | `games` | competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_198 | competition_rules | `knowledge` | PlayStation 5; competition_rules_tekken8_psu_esports | อีสปอร์ต (Esports) หรือกีฬาอิเล็กทรอนิกส์ (Electronic Sports) เป็นการแข่งขันกีฬาที่ใช้ทักษะและความสามารถในการเล่นวิดีโอเกมในรูปแบบต่าง ๆ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge |
| competition_v1_201 | competition_rules | `games` | competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_203 | competition_rules | `games` | competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_v1_209 | competition_rules | `games` | ยกเว้นตัวละคร DLC; Customization; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_rules_v1_228_smoke.jsonl`
