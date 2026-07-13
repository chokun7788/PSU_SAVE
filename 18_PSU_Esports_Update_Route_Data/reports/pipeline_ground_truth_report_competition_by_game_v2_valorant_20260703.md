# Pipeline Ground Truth Evaluation

วันที่: 2026-07-03

## Summary

- Total: 48
- PASS: 10
- FAIL: 38
- ERROR: 0
- Pass rate: 20.83%
- Average latency: 0.0112s
- P95 latency: 0.0159s
- Keyword fail: 38
- Source fail: 14
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 34
- `pipeline:games_fast_path`: 12
- `pipeline:rules_fast_path`: 1
- `pipeline:no_answer`: 1

## Route Category Distribution

- `competition_rules`: 35
- `games`: 12
- `rules`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_valorant_v2_003 | competition_rules | `games` | ไม่เกิน 6; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_004 | competition_rules | `competition_rules` | ห้าม; โทรศัพท์มือถือ | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
| competition_valorant_v2_005 | competition_rules | `competition_rules` | หัวหน้าทีม; กรรมการ | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_006 | competition_rules | `rules` | น้ำดื่ม; ปิดสนิท; หมากฝรั่ง; competition_rules_valorant_psu_phuket_2026 | อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_007 | competition_rules | `competition_rules` | 30 นาที | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
| competition_valorant_v2_010 | competition_rules | `competition_rules` | เลือด; ศพ; OFF | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
| competition_valorant_v2_011 | competition_rules | `competition_rules` | ห้าม; FPS; Latency | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
| competition_valorant_v2_012 | competition_rules | `competition_rules` | 7 | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_014 | competition_rules | `competition_rules` | 3 แผนที่ | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_015 | competition_rules | `games` | โยนเหรียญ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_016 | competition_rules | `games` | เจ้าหน้าที่; บันทึกผล; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_017 | competition_rules | `competition_rules` | 13-0 | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_018 | competition_rules | `competition_rules` | 3; Tactical | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_022 | competition_rules | `competition_rules` | อุปกรณ์ขัดข้อง; หลุด; ซอฟต์แวร์ | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_023 | competition_rules | `competition_rules` | ห้าม; สื่อสาร; เว้นแต่ | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_026 | competition_rules | `competition_rules` | หมดสิทธิ์; ตัวสำรอง | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_027 | competition_rules | `competition_rules` | ไม่ส่งผลกระทบ; เล่นต่อ | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_028 | competition_rules | `competition_rules` | Major Bug; Challenge | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_029 | competition_rules | `competition_rules` | Game-Breaking; ย้อนรอบ | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_030 | competition_rules | `games` | ก่อน; ดาเมจ; ย้อนรอบ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_031 | competition_rules | `games` | damage; ไม่; Challenge; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_032 | competition_rules | `games` | ผิด; ได้เปรียบ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_033 | competition_rules | `games` | ห้าม; Cypher; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_034 | competition_rules | `competition_rules` | ห้าม; นอกขอบเขต | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_035 | competition_rules | `games` | KAY/O; ZERO/POINT; Texture; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_036 | competition_rules | `games` | ห้าม; กระโดด; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_037 | competition_rules | `games` | Warning; ตักเตือน; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_038 | competition_rules | `competition_rules` | Round Rollback; ช่องโหว่ | คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข... |
| competition_valorant_v2_039 | competition_rules | `competition_rules` | Round Loss; เจตนา; ช่องโหว่ | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_040 | competition_rules | `competition_rules` | Map Forfeit; ร้ายแรง; ซ้ำ | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_041 | competition_rules | `games` | Match Forfeit; Cheating; Match fixing; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_042 | competition_rules | `competition_rules` | Snap Tap; SOCD; permitted | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_043 | competition_rules | `games` | ห้าม; Macros; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_044 | competition_rules | `competition_rules` | ห้าม; ติดตั้งโปรแกรม | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
| competition_valorant_v2_045 | competition_rules | `competition_rules` | ห้าม; social media; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_valorant_v2_046 | competition_rules | `competition_rules` | Tactical | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026 |
| competition_valorant_v2_047 | competition_rules | `competition_rules` | Agent; 2 สัปดาห์; แผนที่ใหม่; 4 สัปดาห์ | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_048 | competition_rules | `competition_rules` | Warning; Round Rollback; Round Loss; Map Forfeit; Match Forfeit | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_valorant_20260703.jsonl`
