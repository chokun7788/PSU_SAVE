# Pipeline Ground Truth Evaluation

วันที่: 2026-07-03

## Summary

- Total: 48
- PASS: 13
- FAIL: 35
- ERROR: 0
- Pass rate: 27.08%
- Average latency: 0.0138s
- P95 latency: 0.0291s
- Keyword fail: 35
- Source fail: 9
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 36
- `pipeline:rag_direct_curated`: 7
- `pipeline:no_answer`: 3
- `pipeline:schedule_fast_path`: 1
- `pipeline:rules_fast_path`: 1

## Route Category Distribution

- `competition_rules`: 38
- `general`: 4
- `games`: 3
- `rules`: 2
- `schedule`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_rov_v2_001 | competition_rules | `competition_rules` | 11 กันยายน 2568 | คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน หลักฐานจากกติกา: - เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน Fi... |
| competition_rov_v2_003 | competition_rules | `competition_rules` | 8.30; 8.40 | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)... |
| competition_rov_v2_004 | competition_rules | `competition_rules` | 8.40; 10.00; BO3 | คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น หลักฐานจากกติกา: - เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้ อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket G... |
| competition_rov_v2_005 | competition_rules | `competition_rules` | 10.00; 11.30 | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)... |
| competition_rov_v2_006 | competition_rules | `competition_rules` | 12.30; 14.00 | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)... |
| competition_rov_v2_007 | competition_rules | `competition_rules` | 14.00; 15.30 | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)... |
| competition_rov_v2_008 | competition_rules | `competition_rules` | 15.30; 17.00 | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)... |
| competition_rov_v2_009 | competition_rules | `competition_rules` | อาคาร 5; ชั้น 1 | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_013 | competition_rules | `games` | ด้านบน; สายการแข่งขัน; สีน้ำเงิน; competition_rules_rov_blueket_2025_men | เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home, https://esports.computing.psu.ac.th/ |
| competition_rov_v2_014 | competition_rules | `games` | ผู้ที่แพ้; เลือกฝั่ง; competition_rules_rov_blueket_2025_men | Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ โดยปรากฏในรายการบริการ Cockpit #1 (1 Person) 60 min ของระบบจอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/, https://esports.phuket.psu.ac.th/home |
| competition_rov_v2_015 | competition_rules | `competition_rules` | หมายเลขห้อง | คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad หลักฐานจากกติกา: - เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Game... |
| competition_rov_v2_018 | competition_rules | `competition_rules` | 18 ตัว | คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้ หลักฐานจากกติกา: - เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่... |
| competition_rov_v2_019 | competition_rules | `competition_rules` | Global Ban/Pick | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)... |
| competition_rov_v2_020 | competition_rules | `general` | รูน; พลังเสริม; ตามความต้องการ | คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพ... |
| competition_rov_v2_021 | competition_rules | `competition_rules` | ห้าม; ฮีโร่ซ้ำ | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_024 | competition_rules | `competition_rules` | Resume | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_025 | competition_rules | `general` | แจ้งทีมงาน; ดุลยพินิจ; กรรมการ; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| competition_rov_v2_026 | competition_rules | `competition_rules` | เริ่มเกมใหม่ | คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน หลักฐานจากกติกา: - เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน Fi... |
| competition_rov_v2_027 | competition_rules | `competition_rules` | อนุญาต; คู่แข่ง; กรรมการ | คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน หลักฐานจากกติกา: - เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน Fi... |
| competition_rov_v2_028 | competition_rules | `competition_rules` | ปรับแพ้; ตัดสิทธิ์ | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_029 | competition_rules | `games` | 5 นาที; competition_rules_rov_blueket_2025_men | เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home, https://esports.computing.psu.ac.th/ |
| competition_rov_v2_030 | competition_rules | `schedule` | ปรับ; แพ้; competition_rules_rov_blueket_2025_men | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| competition_rov_v2_031 | competition_rules | `competition_rules` | 10 นาที; เริ่มเกมใหม่ | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_033 | competition_rules | `competition_rules` | ห้าม; สื่อสาร | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_034 | competition_rules | `competition_rules` | ครั้งที่ 1; ตักเตือน | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_035 | competition_rules | `competition_rules` | ครั้งที่ 2; เพิ่มสิทธิการแบนฮีโร่; 1 ครั้ง | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_036 | competition_rules | `competition_rules` | ครั้งที่ 3; เพิ่มสิทธิการแบนฮีโร่; 2 ครั้ง | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_039 | competition_rules | `competition_rules` | ปลั๊กพ่วง; อุปกรณ์ชาร์จ | คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad หลักฐานจากกติกา: - เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Game... |
| competition_rov_v2_040 | competition_rules | `rules` | ปรับแพ้; เกมที่พบ; competition_rules_rov_blueket_2025_men | กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_rov_v2_041 | competition_rules | `competition_rules` | ปรับแพ้; ตัดสิทธิ์ | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)... |
| competition_rov_v2_042 | competition_rules | `competition_rules` | ไม่ตรงตามที่ลงทะเบียน; ปรับแพ้; ตัดสิทธิ์; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_rov_v2_043 | competition_rules | `rules` | เล่นแทน; competition_rules_rov_blueket_2025_men | ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| competition_rov_v2_044 | competition_rules | `competition_rules` | ออฟไลน์; PSU Esports Studio | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men |
| competition_rov_v2_045 | competition_rules | `competition_rules` | ลงทะเบียน; รอบรอง; รอบชิง; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_rov_v2_046 | competition_rules | `competition_rules` | pause; First Blood; 2 นาที | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_rov_20260703.jsonl`
