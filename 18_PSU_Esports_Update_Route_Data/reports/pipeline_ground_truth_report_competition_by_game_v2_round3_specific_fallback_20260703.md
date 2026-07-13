# Pipeline Ground Truth Evaluation

วันที่: 2026-07-03

## Summary

- Total: 184
- PASS: 144
- FAIL: 40
- ERROR: 0
- Pass rate: 78.26%
- Average latency: 0.0158s
- P95 latency: 0.0253s
- Keyword fail: 40
- Source fail: 4
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:rag_direct_curated`: 123
- `pipeline:competition_fact_card`: 57
- `pipeline:no_answer`: 2
- `pipeline:games_fast_path`: 2

## Route Category Distribution

- `competition_rules`: 182
- `games`: 2

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_cs2_v2_035 | competition_rules | `competition_rules` | Freeze time | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| competition_cs2_v2_038 | competition_rules | `competition_rules` | ห้าม; เกลียดชัง; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_rov_v2_017 | competition_rules | `competition_rules` | ล่าช้า | คำตอบ: 4. ระเบียบและกติกาการแข่งขัน รายละเอียดที่เกี่ยวข้อง: - 4.1. กติกาพื้นฐาน - 4.2. กติกาการแข่งขัน - 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง คร... |
| competition_rov_v2_030 | competition_rules | `competition_rules` | ปรับ; แพ้ | คำตอบ: 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม รายละเอียดที่เกี่ยวข้อง: - 4.4. เวลาพัก - 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี... |
| competition_rov_v2_033 | competition_rules | `competition_rules` | ห้าม; สื่อสาร | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_034 | competition_rules | `competition_rules` | ครั้งที่ 1; ตักเตือน | คำตอบ: 6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที รายละเอียดที่เกี่ยวข้อง: - 6.1.3.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้... |
| competition_rov_v2_035 | competition_rules | `competition_rules` | ครั้งที่ 2; เพิ่มสิทธิการแบนฮีโร่; 1 ครั้ง | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_036 | competition_rules | `competition_rules` | ครั้งที่ 3; เพิ่มสิทธิการแบนฮีโร่; 2 ครั้ง | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_rov_v2_038 | competition_rules | `competition_rules` | ไม่อนุญาต; Tablet; iPad | คำตอบ: 6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น รายละเอียดที่เกี่ยวข้อง: - 6.2.4.1. บทลงโทษ: หากทางทีมงานตรวจสอบพบ หรือได้รั... |
| competition_rov_v2_040 | competition_rules | `competition_rules` | เกมที่พบ | คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น หลักฐานจากกติกา: - เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้ อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket G... |
| competition_rov_v2_042 | competition_rules | `competition_rules` | ไม่ตรงตามที่ลงทะเบียน; ปรับแพ้; ตัดสิทธิ์ | คำตอบ: · เวลา 8.00-8.30 ลงทะเบียน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men |
| competition_rov_v2_043 | competition_rules | `competition_rules` | เล่นแทน; ห้าม | คำตอบ: 6.2.4.1. บทลงโทษ: หากทางทีมงานตรวจสอบพบ หรือได้รับการร้องเรียนจากผู้อื่น ทีมงานจะมีมาตรการลงโทษผู้เข้าแข่งขันที่ฝ่าฝืนกติกา โดยตัดสิทธิ์การเข้าร่วมแข่งขัน รายละเอียดที่เกี่ยวข้อง: - 6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมท... |
| competition_rov_v2_044 | competition_rules | `competition_rules` | ออฟไลน์; BO3 | คำตอบ: 2.1. PSU Esports Studio – Phuket (อาคาร 5 ชั้น 1) แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men |
| competition_rov_v2_045 | competition_rules | `competition_rules` | ลงทะเบียน; รอบรอง; รอบชิง; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| competition_rov_v2_046 | competition_rules | `competition_rules` | pause; First Blood; 2 นาที | คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห... |
| competition_valorant_v2_007 | competition_rules | `competition_rules` | 30 นาที | คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก... |
| competition_valorant_v2_012 | competition_rules | `competition_rules` | 7 | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_014 | competition_rules | `competition_rules` | 3 แผนที่ | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_018 | competition_rules | `competition_rules` | 3; Tactical | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_022 | competition_rules | `competition_rules` | อุปกรณ์ขัดข้อง; หลุด; ซอฟต์แวร์ | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_023 | competition_rules | `competition_rules` | ห้าม; สื่อสาร; เว้นแต่ | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_026 | competition_rules | `competition_rules` | หมดสิทธิ์; ตัวสำรอง | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_029 | competition_rules | `competition_rules` | Game-Breaking | คำตอบ: * Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้ รายละเอียดที่เกี่ยวข้อง: - หากเป็น Game Breaking Bug เจ้าหน้าที่จะสั่งย้อนรอบไปยังจุดเริ่มต้นของรอบนั้นทันที - Play Through Bug บั... |
| competition_valorant_v2_030 | competition_rules | `games` | ก่อน; ดาเมจ; ย้อนรอบ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_031 | competition_rules | `competition_rules` | damage | คำตอบ: * Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้ รายละเอียดที่เกี่ยวข้อง: - หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้... |
| competition_valorant_v2_032 | competition_rules | `games` | ผิด; ได้เปรียบ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_034 | competition_rules | `competition_rules` | ห้าม; นอกขอบเขต | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_036 | competition_rules | `competition_rules` | ห้าม; กระโดด | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_037 | competition_rules | `competition_rules` | Warning; ตักเตือน | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา... |
| competition_valorant_v2_045 | competition_rules | `competition_rules` | social media | คำตอบ: * ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ รายละเอียดที่เกี่ยวข้อง: - ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์ - อุปกรณ์อิเล็ก... |
| competition_valorant_v2_046 | competition_rules | `competition_rules` | Tactical | คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026 |
| competition_valorant_v2_047 | competition_rules | `competition_rules` | Agent; 2 สัปดาห์; แผนที่ใหม่; 4 สัปดาห์ | คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /... |
| competition_valorant_v2_048 | competition_rules | `competition_rules` | Warning; Round Rollback; Round Loss; Map Forfeit; Match Forfeit | คำตอบ: ประเภทบทลงโทษในเกม รายละเอียดที่เกี่ยวข้อง: - บทลงโทษ - ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ - ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน - เจ้าหน้าที่จะ... |
| competition_tekken8_v2_006 | competition_rules | `competition_rules` | 3 รอบ | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| competition_tekken8_v2_009 | competition_rules | `competition_rules` | Random | คำตอบ: * สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC) รายละเอียดที่เกี่ยวข้อง: - ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ) - FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน - อนุญาตให้ใช้ ปุ่ม... |
| competition_tekken8_v2_012 | competition_rules | `competition_rules` | ปรับแต่ง | คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ... |
| competition_tekken8_v2_017 | competition_rules | `competition_rules` | ปรับแพ้ 1 รอบ | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_018 | competition_rules | `competition_rules` | อุปกรณ์ขัดข้อง; เหตุฉุกเฉิน | คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round... |
| competition_tekken8_v2_033 | competition_rules | `competition_rules` | ชนะครบ 2 เกม | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| competition_tekken8_v2_040 | competition_rules | `competition_rules` | PlayStation 5 | คำตอบ: * แข่งขันแบบ เดี่ยว (1v1) รายละเอียดที่เกี่ยวข้อง: - หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน - ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข - คำตัดสินของกรรมการถือเป็นที่สิ... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_round3_specific_fallback_20260703.jsonl`
