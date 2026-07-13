# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 360
- PASS: 340
- FAIL: 20
- ERROR: 0
- Pass rate: 94.44%
- Average latency: 0.0135s
- P95 latency: 0.0375s
- Keyword fail: 8
- Source fail: 12
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:deterministic_calculator_fast`: 139
- `pipeline:schedule_fast_path`: 46
- `pipeline:guard_no_answer`: 25
- `pipeline:rules_fast_path`: 21
- `pipeline:booking_fast_path`: 20
- `pipeline:games_fast_path`: 14
- `pipeline:checkin_fast_path`: 12
- `pipeline:penalty_fast_path`: 11
- `pipeline:payment_fast_path`: 10
- `pipeline:contact_fast_path`: 10
- `pipeline:equipment_zone_fast_path`: 8
- `pipeline:knowledge_fast_path`: 7
- `pipeline:overview_fast_path`: 5
- `pipeline:members_fast_path`: 5
- `pipeline:news_fast_path`: 4
- `pipeline:mixed_reservation_fast`: 4
- `pipeline:games_availability_fast_path`: 3
- `pipeline:equipment_game_catalog_fast_path`: 3
- `pipeline:equipment_item_fast_path`: 3
- `pipeline:mixed_rules_fast`: 2
- `pipeline:rag_direct_curated`: 2
- `pipeline:calendar_schedule_fast_path`: 2
- `pipeline:category_rule_fast_path`: 1
- `pipeline:competition_fact_card`: 1
- `pipeline:equipment_fast_path`: 1
- `pipeline:competition_game_list_fast_path`: 1

## Route Category Distribution

- `service_fee`: 139
- `schedule`: 48
- `reservation`: 47
- `no_answer`: 25
- `rules`: 22
- `games`: 19
- `equipment`: 14
- `penalty`: 11
- `contact`: 10
- `knowledge`: 9
- `overview`: 9
- `events_news`: 4
- `competition_rules`: 3

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| v2_201 | games | `competition_rules` | Reservation | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| v2_202 | games | `equipment` | Reservation | PlayStation 5 Zone คือโซนเล่นเกมคอนโซล PS5 สำหรับ 1-2 คนต่อรอบตามบริการที่มีในระบบ วิธีใช้งานโดยสรุป: จอง PlayStation 5 Zone แล้วเล่นเกมผ่านเครื่อง PS5 และจอ/อุปกรณ์ที่ศูนย์จัดไว้ เลือกเกมตามรายการที่มีให้บริการ อุปกรณ์ห... |
| v2_203 | games | `games` | Reservation | มีครับ Fortnite อยู่ในรายการเกมที่ยืนยันได้ของ PlayStation 5 Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games |
| v2_208 | games | `games` | Reservation | มีครับ Super Smash Bros Ultimate อยู่ในรายการเกมที่ยืนยันได้ของ Nintendo Switch Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games |
| v2_211 | games | `games` | Reservation | มีครับ Counter-Strike 2 อยู่ในรายการเกมที่ยืนยันได้ของ PC Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games |
| v2_212 | games | `equipment` | Reservation | สรุปเกมที่เล่นได้ในโซนที่ถาม: - PC Zone: VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8 และ League of Legends อุปกรณ์หลัก: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 เครื่อง, Gaming Moni... |
| v2_214 | games | `equipment` | Reservation | PC Zone คือโซนคอมพิวเตอร์เกมมิ่งสำหรับเล่นเกมบน PC และใช้ฝึกซ้อม/เรียนรู้ด้านอีสปอร์ต วิธีใช้งานโดยสรุป: จอง PC Zone ตามรอบบริการ เข้าใช้งานเครื่องที่ศูนย์จัดไว้ แล้วเปิดเกมหรือโปรแกรมที่ต้องการตามรายการที่มี อุปกรณ์หลัก... |
| v2_215 | games | `equipment` | Reservation | สรุปเกมที่เล่นได้ในโซนที่ถาม: - VR Zone: Beat Saber และ Horizon Call of the Mountain อุปกรณ์หลัก: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 เครื่อง และ Sony PlayStation VR2 1 ชุด วิธีใช้งานโดยสรุป: จอง VR Zon... |
| v2_218 | games | `equipment` | Reservation | สรุปเกมที่เล่นได้ในโซนที่ถาม: - Cockpit Zone: Gran Turismo 7 (Single Player) อุปกรณ์หลัก: TV 65 นิ้ว 2 เครื่อง, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 ชุด, Racezone Full Cockpit V3 2 ชุด และ Pulse... |
| v2_221 | equipment | `equipment` | 10 Units | PC Zone คือโซนคอมพิวเตอร์เกมมิ่งสำหรับเล่นเกมบน PC และใช้ฝึกซ้อม/เรียนรู้ด้านอีสปอร์ต วิธีใช้งานโดยสรุป: จอง PC Zone ตามรอบบริการ เข้าใช้งานเครื่องที่ศูนย์จัดไว้ แล้วเปิดเกมหรือโปรแกรมที่ต้องการตามรายการที่มี อุปกรณ์หลัก... |
| v2_222 | equipment | `equipment` | 10 Units | Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต ใช้ทำอะไร/เล่นอะไรได้: เล่น VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKE... |
| v2_223 | equipment | `games` | 10 Units | PC Zone คือโซนคอมพิวเตอร์เกมมิ่งสำหรับเล่นเกมบน PC และใช้ฝึกซ้อม/เรียนรู้ด้านอีสปอร์ต วิธีใช้งานโดยสรุป: จอง PC Zone ตามรอบบริการ เข้าใช้งานเครื่องที่ศูนย์จัดไว้ แล้วเปิดเกมหรือโปรแกรมที่ต้องการตามรายการที่มี อุปกรณ์หลัก... |
| v2_225 | equipment | `equipment` | Units | Cockpit Zone คือโซนจำลองการขับรถ/เกมแข่งรถ ใช้เล่น Gran Turismo 7 ด้วยชุดพวงมาลัยและเบาะขับ วิธีใช้งานโดยสรุป: จอง Cockpit Zone แล้วนั่งในชุด Cockpit ใช้พวงมาลัย Logitech G923 พร้อมคันเร่ง/เบรก/คันเกียร์เพื่อควบคุมรถในเก... |
| v2_226 | equipment | `equipment` | Units | Logitech G923 TRUEFORCE Racing Wheel: ชุดพวงมาลัยแข่งรถสำหรับเล่นเกมขับรถใน Cockpit Zone ใช้ทำอะไร/เล่นอะไรได้: ใช้เล่น Gran Turismo 7 ร่วมกับชุด Cockpit และ TV 65 นิ้ว วิธีใช้งานโดยสรุป: จอง Cockpit Zone แล้วใช้พวงมาลัย... |
| v2_227 | equipment | `equipment` | Units | Nintendo Switch Zone คือโซนเล่นเกม Nintendo Switch สำหรับเล่นเป็นกลุ่ม/ครอบครัว/กิจกรรมสนุก ๆ วิธีใช้งานโดยสรุป: จอง Nintendo Switch Zone แล้วเล่นผ่าน Nintendo Switch OLED กับ TV 86 นิ้ว ใช้จอย Joy-Con/Controller ตามเกมท... |
| v2_228 | equipment | `equipment` | Units | PlayStation 5 Zone คือโซนเล่นเกมคอนโซล PS5 สำหรับ 1-2 คนต่อรอบตามบริการที่มีในระบบ วิธีใช้งานโดยสรุป: จอง PlayStation 5 Zone แล้วเล่นเกมผ่านเครื่อง PS5 และจอ/อุปกรณ์ที่ศูนย์จัดไว้ เลือกเกมตามรายการที่มีให้บริการ อุปกรณ์ห... |
| v2_229 | equipment | `equipment` | Units | Sony PlayStation VR2: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone ใช้ทำอะไร/เล่นอะไรได้: เล่น Beat Saber และ Horizon Call of the Mountain วิธีใช้งานโดยสรุป: จอง VR Zone แล้วสวมแว่น PlayStation VR2 และใช้คอนโทรลเลอร์ตามค... |
| v2_270 | events_news | `games` | News | เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้: - Counter-Strike 2: PSU Phuket CS2 2026 Tournament - VALORANT: PSU Phuket VALORANT 2026 Tournament - Arena of Valor (RoV): Blueket Games 2025 ประเภททีมชาย - TEKKEN 8: P... |
| v2_333 | games | `competition_rules` | Reservation | คำตอบ: * รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน รายละเอียดที่เกี่ยวข้อง: - บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม่ตั้งใจ โดยแบ่งประเภทเพื่อกำ... |
| v2_341 | games | `competition_rules` | Reservation | คำตอบ: * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) รายละเอียดที่เกี่ยวข้อง: - กฎระเบียบและรูปแบบการแข่งขัน VA... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_gt360_equipment_game_catalog_fix_20260704.jsonl`
