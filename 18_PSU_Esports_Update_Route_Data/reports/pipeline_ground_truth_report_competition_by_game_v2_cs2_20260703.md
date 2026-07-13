# Pipeline Ground Truth Evaluation

วันที่: 2026-07-03

## Summary

- Total: 48
- PASS: 9
- FAIL: 39
- ERROR: 0
- Pass rate: 18.75%
- Average latency: 0.0113s
- P95 latency: 0.0159s
- Keyword fail: 38
- Source fail: 18
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 28
- `pipeline:games_fast_path`: 12
- `pipeline:rag_direct_curated`: 5
- `pipeline:category_rule_fast_path`: 1
- `pipeline:schedule_fast_path`: 1
- `pipeline:no_answer`: 1

## Route Category Distribution

- `competition_rules`: 31
- `games`: 12
- `events_news`: 2
- `service_fee`: 2
- `schedule`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_cs2_v2_001 | competition_rules | `events_news` | มหาวิทยาลัยสงขลานครินทร์; ภูเก็ต; competition_rules_cs2_psu_phuket_2026 | เมื่อวันที่ 27 กุมภาพันธ์ 2569 นักศึกษาชาวจีนระดับปริญญาโท คณะการบริการและการท่องเที่ยว จำนวน 11 คน เข้าร่วมกิจกรรมการเรียนรู้โดยใช้เกมเป็นฐาน (Game-based Learning) ณ PSU Esports Studio - Phuket แหล่งข้อมูล: https://espo... |
| competition_cs2_v2_002 | competition_rules | `competition_rules` | เฉพาะ; นักศึกษา; ภูเก็ต | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_005 | competition_rules | `games` | Steam; ห้าม; ดัดแปลง; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_006 | competition_rules | `games` | ล่าสุด; CS2; Steam; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_007 | competition_rules | `competition_rules` | ภาษาไทย | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_cs2_v2_008 | competition_rules | `games` | ภาษาไทย; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_009 | competition_rules | `competition_rules` | 1 วัน; PSU Esports Studio | คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru... |
| competition_cs2_v2_010 | competition_rules | `events_news` | competition_rules_cs2_psu_phuket_2026 | PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us |
| competition_cs2_v2_011 | competition_rules | `games` | Discord; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_012 | competition_rules | `competition_rules` | Discord; ศูนย์ | คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru... |
| competition_cs2_v2_013 | competition_rules | `competition_rules` | ไม่มีการเปลี่ยนแปลง; สมาชิก | คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru... |
| competition_cs2_v2_014 | competition_rules | `competition_rules` | ไม่อนุญาต; ปิดรับสมัคร | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_015 | competition_rules | `competition_rules` | ถอนตัว; ตัดสิทธิ์ | คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru... |
| competition_cs2_v2_016 | competition_rules | `competition_rules` | ทีมเดียว | คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru... |
| competition_cs2_v2_017 | competition_rules | `competition_rules` | ล่วงหน้า; 1 วัน | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_cs2_v2_021 | competition_rules | `games` | Competitive; 5v5; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_022 | competition_rules | `service_fee` | 1:55; 15 วินาที; competition_rules_cs2_psu_phuket_2026 | บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/upl... |
| competition_cs2_v2_023 | competition_rules | `service_fee` | $800; 40 วินาที; competition_rules_cs2_psu_phuket_2026 | บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/upl... |
| competition_cs2_v2_024 | competition_rules | `competition_rules` | 13 รอบ | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_cs2_v2_025 | competition_rules | `games` | 24 รอบ; 12 รอบ; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_026 | competition_rules | `games` | ฝั่งละ 3 รอบ; 4 ใน 6; $10,000; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_027 | competition_rules | `schedule` | ไม่จำกัด; competition_rules_cs2_psu_phuket_2026 | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| competition_cs2_v2_030 | competition_rules | `competition_rules` | MAPBAN.GG | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_cs2_v2_031 | competition_rules | `games` | ดวลมีด; เลือกฝั่ง; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_033 | competition_rules | `competition_rules` | กรรมการ; ทันที | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_035 | competition_rules | `competition_rules` | Freeze time | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_036 | competition_rules | `competition_rules` | ห้าม; บัค; ปรับแพ้ | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_cs2_v2_037 | competition_rules | `competition_rules` | ห้าม; สตรีม | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_038 | competition_rules | `competition_rules` | ห้าม; เกลียดชัง; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_cs2_v2_039 | competition_rules | `games` | คีย์บอร์ด; เมาส์; มาเองได้; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_040 | competition_rules | `competition_rules` | PC; จอภาพ; โต๊ะ; เก้าอี้ | คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C... |
| competition_cs2_v2_041 | competition_rules | `games` | Crosshair; Resolution; Brightness; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_042 | competition_rules | `games` | ห้าม; สคริปต์; มาโคร; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_043 | competition_rules | `competition_rules` | ห้าม; ติดตั้งโปรแกรม | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_044 | competition_rules | `competition_rules` | ห้าม; โซเชียลมีเดีย | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_045 | competition_rules | `games` | ไม่เกิน 6 คน; competition_rules_cs2_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_cs2_v2_046 | competition_rules | `competition_rules` | ห้าม; โทรศัพท์มือถือ; สมาร์ทวอทช์ | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_047 | competition_rules | `competition_rules` | หัวหน้าทีม; กรรมการ | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_048 | competition_rules | `competition_rules` | น้ำดื่ม; ปิดสนิท; หมากฝรั่ง | คำตอบ: 6. อุปกรณ์และการตั้งค่าเกม รายละเอียดที่เกี่ยวข้อง: - 1. อุปกรณ์ที่อนุญาต - 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_cs2_20260703.jsonl`
