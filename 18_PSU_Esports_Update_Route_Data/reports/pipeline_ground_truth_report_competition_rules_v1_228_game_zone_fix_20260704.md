# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 228
- PASS: 203
- FAIL: 25
- ERROR: 0
- Pass rate: 89.04%
- Average latency: 0.0200s
- P95 latency: 0.0332s
- Keyword fail: 25
- Source fail: 6
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_fact_card`: 195
- `pipeline:rag_direct_curated`: 33

## Route Category Distribution

- `competition_rules`: 228

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_v1_022 | competition_rules | `competition_rules` | Ancient; Anubis; Dust 2; Train | คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ รายละเอียดที่เกี่ยวข้อง: - 3. แผนที่ในการแข่งขัน - 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้... |
| competition_v1_029 | competition_rules | `competition_rules` | Single Elimination; BO3 | คำตอบ: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket รายละเอียดที่เกี่ยวข้อง: - 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระ... |
| competition_v1_031 | competition_rules | `competition_rules` | Single Elimination | คำตอบ: 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3) รายละเอียดที่เกี่ยวข้อง: - กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 - 3. รูปแบบการแข่งขัน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล... |
| competition_v1_034 | competition_rules | `competition_rules` | BO3 | คำตอบ: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง รายละเอียดที่เกี่ยวข้อง: - 1. รูปแบบทัวร์นาเมนต์ Single Elimination - กฎระเบียบและรูปแบบการแข่ง... |
| competition_v1_043 | competition_rules | `competition_rules` | Technical Pause; 2 ครั้ง; 10 นาที; Tactical Timeout | คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2... |
| competition_v1_078 | competition_rules | `competition_rules` | Tactical Timeout | คำตอบ: * เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ รายละเอียดที่เกี่ยวข้อง: - During Overtime, each team receives 1 additional timeout. Timeouts from regulation do... |
| competition_v1_079 | competition_rules | `competition_rules` | Tactical Timeout; 2 ครั้ง; 60 วินาที; Overtime | คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_202... |
| competition_v1_089 | competition_rules | `competition_rules` | Emergency; 1 ครั้ง; 10 นาที | คำตอบ: * จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_202... |
| competition_v1_094 | competition_rules | `competition_rules` | 10 นาที | คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause) รายละเอียดที่เกี่ยวข้อง: - 3. Player Emergency Pause - Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected pla... |
| competition_v1_116 | competition_rules | `competition_rules` | ฝ่ายละ 5 คน; ยังไม่พบจำนวนสมาชิกทีม | คำตอบ: 4. ระเบียบและกติกาการแข่งขัน รายละเอียดที่เกี่ยวข้อง: - 4.1. กติกาพื้นฐาน - 4.2. กติกาการแข่งขัน - 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง คร... |
| competition_v1_119 | competition_rules | `competition_rules` | 5v5; ฝ่ายละ 5 คน; ยังไม่พบจำนวนสมาชิกทีม; competition_rules_rov_blueket_2025_men | คำตอบ: * แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive รายละเอียดที่เกี่ยวข้อง: - เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive - New agents are restrict... |
| competition_v1_127 | competition_rules | `competition_rules` | Default Skin; competition_rules_rov_blueket_2025_men | คำตอบ: กฎระเบียบและรูปแบบการแข่งขัน VALORANT รายละเอียดที่เกี่ยวข้อง: - ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม - เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นา... |
| competition_v1_140 | competition_rules | `competition_rules` | 15 นาที; competition_rules_rov_blueket_2025_men | คำตอบ: * การบันทึกผล เจ้าหน้าที่จะยืนยัน และบันทึกผลการแข่งทันที รายละเอียดที่เกี่ยวข้อง: - การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0 - เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SO... |
| competition_v1_148 | competition_rules | `competition_rules` | 5 ครั้ง; 1 นาที | คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้ รายละเอียดที่เกี่ยวข้อง: - 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้... |
| competition_v1_152 | competition_rules | `competition_rules` | 5 ครั้ง; 1 นาที; competition_rules_rov_blueket_2025_men | คำตอบ: * เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ รายละเอียดที่เกี่ยวข้อง: - ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที - ขอได้ 1 ครั้งต่อแผนที... |
| competition_v1_163 | competition_rules | `competition_rules` | First Blood; 2 นาที; competition_rules_rov_blueket_2025_men | คำตอบ: * ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies) รายละเอียดที่เกี่ยวข้อง: - เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ - เอเจนท์ใหม่ จะถูกจำกัดห้... |
| competition_v1_166 | competition_rules | `competition_rules` | First Blood; 2 นาที | คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ... |
| competition_v1_175 | competition_rules | `competition_rules` | ไม่อนุญาต; Tablet; iPad; competition_rules_rov_blueket_2025_men | คำตอบ: * อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ รายละเอียดที่เกี่ยวข้อง: - เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้... |
| competition_v1_177 | competition_rules | `competition_rules` | โทรศัพท์มือถือ; ไม่อนุญาต; Tablet; iPad | คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)... |
| competition_v1_187 | competition_rules | `competition_rules` | 1v1; PlayStation 5; FT2 | คำตอบ: * ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ) รายละเอียดที่เกี่ยวข้อง: - หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน - เวลาแข่งขันต่อรอบ (Timer): 60 วินาที - การกดหยุดเกม (Pause) ทำไ... |
| competition_v1_191 | competition_rules | `competition_rules` | 1v1; PlayStation 5 | คำตอบ: * ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด รายละเอียดที่เกี่ยวข้อง: - FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน - กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะ... |
| competition_v1_212 | competition_rules | `competition_rules` | ยกเว้นตัวละคร DLC; Customization | คำตอบ: * ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ รายละเอียดที่เกี่ยวข้อง: - สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC) - อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ - เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด... |
| competition_v1_216 | competition_rules | `competition_rules` | ยกเว้นตัวละคร DLC; Customization | คำตอบ: * ต้องใช้ สกินมาตรฐาน เท่านั้น รายละเอียดที่เกี่ยวข้อง: - สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC) - ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ) - ใช้เครื่องเกม PlayStation... |
| competition_v1_222 | competition_rules | `competition_rules` | ไม่อนุญาต; Pause; แพ้ 1 Round | คำตอบ: * เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ รายละเอียดที่เกี่ยวข้อง: - กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ - FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน - หากมีการกดหยุดเกมโดยเจต... |
| competition_v1_227 | competition_rules | `competition_rules` | ไม่อนุญาต; แพ้ 1 Round | คำตอบ: * ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ รายละเอียดที่เกี่ยวข้อง: - หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที - ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไ... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_rules_v1_228_game_zone_fix_20260704.jsonl`
