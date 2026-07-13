# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 80
- PASS: 49
- FAIL: 31
- ERROR: 0
- Pass rate: 61.25%
- Average latency: 0.0209s
- P95 latency: 0.0362s
- Keyword fail: 30
- Source fail: 9
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:rag_direct_curated`: 50
- `pipeline:competition_fact_card`: 24
- `pipeline:games_fast_path`: 3
- `pipeline:no_answer`: 1
- `pipeline:equipment_fast_path`: 1
- `pipeline:schedule_fast_path`: 1

## Route Category Distribution

- `competition_rules`: 69
- `games`: 4
- `general`: 4
- `events_news`: 2
- `schedule`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_cs2_001 | competition_rules | `competition_rules` | ไม่มีการเปลี่ยนแปลงสมาชิก; ตลอดระยะเวลาการแข่งขัน | คำตอบ: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน รายละเอียดที่เกี่ยวข้อง: - 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง - 1. ผู้เล่น... |
| competition_challenger_cs2_010 | competition_rules | `competition_rules` | แมตช์ | คำตอบ: การใช้บัค รายละเอียดที่เกี่ยวข้อง: - 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ - 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ท... |
| competition_challenger_cs2_011 | competition_rules | `competition_rules` | ดูสตรีม; แมตช์ | คำตอบ: 8. ตารางบทลงโทษ (Penalties) รายละเอียดที่เกี่ยวข้อง: - การละเมิด - บทลงโทษ - การด่าทอ/ใช้ความรุนแรงทางวาจา - ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tourname... |
| competition_challenger_cs2_012 | competition_rules | `competition_rules` | ตักเตือน; ปรับแพ้; ตัดสิทธิ์ | คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3) หลักฐานจากกติกา: - เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3 อ้างอิงจากกติกา: Counter-Strike 2 / P... |
| competition_challenger_cs2_016 | competition_rules | `competition_rules` | Freeze time | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_challenger_cs2_017 | competition_rules | `games` | ห้าม; เกลียดชัง; ศาสนา; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_challenger_cs2_019 | competition_rules | `competition_rules` | ผู้เล่น 5 คน | คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น รายละเอียดที่เกี่ยวข้อง: - 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง - 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีส... |
| competition_challenger_rov_001 | competition_rules | `general` | 15 นาที | คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพ... |
| competition_challenger_rov_006 | competition_rules | `competition_rules` | Global Ban/Pick; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_challenger_rov_012 | competition_rules | `games` | แจ้งทีมงาน; ดุลยพินิจ; กรรมการ; competition_rules_rov_blueket_2025_men | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| competition_challenger_rov_014 | competition_rules | `competition_rules` | ปรับแพ้; ตัดสิทธิ์ | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_challenger_rov_016 | competition_rules | `competition_rules` | ปรับ; แพ้ | คำตอบ: 4.4. เวลาพัก รายละเอียดที่เกี่ยวข้อง: - 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม - 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม - 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขัน... |
| competition_challenger_rov_018 | competition_rules | `competition_rules` | PSU Esports Studio; อาคาร 5 | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_challenger_rov_020 | competition_rules | `competition_rules` | ห้าม; หยาบคาย; เสียดสี | คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad หลักฐานจากกติกา: - เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Game... |
| competition_challenger_valorant_005 | competition_rules | `competition_rules` | ติดตั้งโปรแกรม | คำตอบ: * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) รายละเอียดที่เกี่ยวข้อง: - เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้... |
| competition_challenger_valorant_006 | competition_rules | `competition_rules` | social media; เว็บไซต์สื่อสาร | คำตอบ: * เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น รายละเอียดที่เกี่ยวข้อง: - ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์ - อุปกร... |
| competition_challenger_valorant_011 | competition_rules | `competition_rules` | 30 นาที | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
| competition_challenger_valorant_014 | competition_rules | `schedule` | Blood; Bodies; competition_rules_valorant_psu_phuket_2026 | โดยทั่วไปเวลาสิ้นสุดช่วงบริการคือ 16:00 แต่วันศุกร์ช่วงบ่าย 13:00-16:00 เป็น Maintenance จึงควรดูวันประกอบ รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น... |
| competition_challenger_valorant_017 | competition_rules | `competition_rules` | 3 แผนที่ | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_challenger_valorant_019 | competition_rules | `competition_rules` | 24 รอบแรก | คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข... |
| competition_challenger_valorant_022 | competition_rules | `competition_rules` | หมดสิทธิ์; ตัวสำรอง | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_challenger_valorant_024 | competition_rules | `competition_rules` | Cypher | คำตอบ: * ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง รายละเอียดที่เกี่ยวข้อง: - Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุต... |
| competition_challenger_valorant_025 | competition_rules | `competition_rules` | Match Forfeit; Cheating; Match fixing | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_challenger_tekken8_001 | competition_rules | `events_news` | 1v1; competition_rules_tekken8_psu_esports | PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news |
| competition_challenger_tekken8_003 | competition_rules | `events_news` | 3 รอบ; R3; competition_rules_tekken8_psu_esports | เมื่อวันที่ 25 เมษายน 2569 PSU Esports Studio - Phuket จัดการแข่งขัน PSU Phuket CS 2 2026 Tournament ในเกม Counter-Strike 2 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news |
| competition_challenger_tekken8_005 | competition_rules | `general` | competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_challenger_tekken8_006 | competition_rules | `general` | Random | คำตอบ: * สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC) รายละเอียดที่เกี่ยวข้อง: - อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ - การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่ - 4.2.2.ใช้การแบนและเ... |
| competition_challenger_tekken8_008 | competition_rules | `general` | Customization | คำตอบ: * สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC) รายละเอียดที่เกี่ยวข้อง: - ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ) - 4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเส... |
| competition_challenger_tekken8_009 | competition_rules | `games` | ปรับแพ้; 1 รอบ; competition_rules_tekken8_psu_esports | Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ โดยปรากฏในรายการบริการ Cockpit #1 (1 Person) 60 min ของระบบจอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/, https://esports.phuket.psu.ac.th/home |
| competition_challenger_tekken8_010 | competition_rules | `competition_rules` | อุปกรณ์ขัดข้อง; เหตุฉุกเฉิน | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_challenger_tekken8_014 | competition_rules | `games` | เกมตัดสิน; competition_rules_tekken8_psu_esports | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v1_20260704_014048.jsonl`
