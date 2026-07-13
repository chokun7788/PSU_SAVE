# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 184
- PASS: 157
- FAIL: 27
- ERROR: 0
- Pass rate: 85.33%
- Average latency: 0.0164s
- P95 latency: 0.0240s
- Keyword fail: 27
- Source fail: 2
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:rag_direct_curated`: 100
- `pipeline:competition_fact_card`: 82
- `pipeline:games_fast_path`: 2

## Route Category Distribution

- `competition_rules`: 182
- `games`: 2

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_rov_v2_001 | competition_rules | `competition_rules` | 11 กันยายน 2568 | คำตอบ: ควรตอบตารางทั้งวันของ RoV ได้แก่ ลงทะเบียน, แบ่งสาย, รอบ 5 ทีม, รอบรองชนะเลิศ, รอบชิงอันดับที่ 3 และรอบชิงชนะเลิศ หลักฐานจากกติกา: - เอกสารกำหนดการแข่งขันระบุเวลา 8.00-17.00 ครอบคลุมลงทะเบียน รอบรอง และรอบชิง อ้าง... |
| competition_rov_v2_002 | competition_rules | `competition_rules` | 8.30 | คำตอบ: ควรตอบตารางทั้งวันของ RoV ได้แก่ ลงทะเบียน, แบ่งสาย, รอบ 5 ทีม, รอบรองชนะเลิศ, รอบชิงอันดับที่ 3 และรอบชิงชนะเลิศ หลักฐานจากกติกา: - เอกสารกำหนดการแข่งขันระบุเวลา 8.00-17.00 ครอบคลุมลงทะเบียน รอบรอง และรอบชิง อ้าง... |
| competition_rov_v2_003 | competition_rules | `competition_rules` | 8.30; 8.40 | คำตอบ: ควรตอบตารางทั้งวันของ RoV ได้แก่ ลงทะเบียน, แบ่งสาย, รอบ 5 ทีม, รอบรองชนะเลิศ, รอบชิงอันดับที่ 3 และรอบชิงชนะเลิศ หลักฐานจากกติกา: - เอกสารกำหนดการแข่งขันระบุเวลา 8.00-17.00 ครอบคลุมลงทะเบียน รอบรอง และรอบชิง อ้าง... |
| competition_rov_v2_004 | competition_rules | `competition_rules` | 8.40; 10.00; BO3 | คำตอบ: ควรตอบตารางทั้งวันของ RoV ได้แก่ ลงทะเบียน, แบ่งสาย, รอบ 5 ทีม, รอบรองชนะเลิศ, รอบชิงอันดับที่ 3 และรอบชิงชนะเลิศ หลักฐานจากกติกา: - เอกสารกำหนดการแข่งขันระบุเวลา 8.00-17.00 ครอบคลุมลงทะเบียน รอบรอง และรอบชิง อ้าง... |
| competition_rov_v2_005 | competition_rules | `competition_rules` | 10.00; 11.30 | คำตอบ: ควรตอบตารางทั้งวันของ RoV ได้แก่ ลงทะเบียน, แบ่งสาย, รอบ 5 ทีม, รอบรองชนะเลิศ, รอบชิงอันดับที่ 3 และรอบชิงชนะเลิศ หลักฐานจากกติกา: - เอกสารกำหนดการแข่งขันระบุเวลา 8.00-17.00 ครอบคลุมลงทะเบียน รอบรอง และรอบชิง อ้าง... |
| competition_rov_v2_007 | competition_rules | `competition_rules` | 14.00; 15.30 | คำตอบ: ควรตอบตารางทั้งวันของ RoV ได้แก่ ลงทะเบียน, แบ่งสาย, รอบ 5 ทีม, รอบรองชนะเลิศ, รอบชิงอันดับที่ 3 และรอบชิงชนะเลิศ หลักฐานจากกติกา: - เอกสารกำหนดการแข่งขันระบุเวลา 8.00-17.00 ครอบคลุมลงทะเบียน รอบรอง และรอบชิง อ้าง... |
| competition_rov_v2_008 | competition_rules | `competition_rules` | 15.30 | คำตอบ: ควรตอบตารางทั้งวันของ RoV ได้แก่ ลงทะเบียน, แบ่งสาย, รอบ 5 ทีม, รอบรองชนะเลิศ, รอบชิงอันดับที่ 3 และรอบชิงชนะเลิศ หลักฐานจากกติกา: - เอกสารกำหนดการแข่งขันระบุเวลา 8.00-17.00 ครอบคลุมลงทะเบียน รอบรอง และรอบชิง อ้าง... |
| competition_rov_v2_017 | competition_rules | `competition_rules` | ล่าช้า | คำตอบ: 4. ระเบียบและกติกาการแข่งขัน รายละเอียดที่เกี่ยวข้อง: - 4.1. กติกาพื้นฐาน - 4.2. กติกาการแข่งขัน - 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง คร... |
| competition_rov_v2_019 | competition_rules | `competition_rules` | Global Ban/Pick | คำตอบ: RoV Pause ผิดครั้งที่ 2 จะเพิ่มสิทธิการแบนฮีโร่ให้ฝ่ายตรงข้าม 1 ครั้ง หลักฐานจากกติกา: - เอกสารบทลงโทษการ Pause ผิดระบุครั้งที่ 2 เพิ่มสิทธิการแบนฮีโร่ 1 ครั้ง อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games... |
| competition_rov_v2_029 | competition_rules | `competition_rules` | 5 นาที | คำตอบ: RoV หากไม่กลับมาภายในเวลาพักที่กำหนด ผู้ตัดสินอาจปรับให้ทีมดังกล่าวแพ้จากการแข่งขัน หลักฐานจากกติกา: - เอกสารข้อ 4.4.2 ระบุว่าหากผู้เข้าแข่งขันไม่กลับมาภายในเวลาที่กำหนด ผู้ตัดสินอาจปรับให้ทีมดังกล่าวแพ้จากการแข่ง... |
| competition_rov_v2_035 | competition_rules | `competition_rules` | ครั้งที่ 2; เพิ่มสิทธิการแบนฮีโร่; 1 ครั้ง | คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ... |
| competition_rov_v2_036 | competition_rules | `competition_rules` | ครั้งที่ 3; เพิ่มสิทธิการแบนฮีโร่; 2 ครั้ง | คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ... |
| competition_rov_v2_038 | competition_rules | `competition_rules` | ไม่อนุญาต; Tablet; iPad | คำตอบ: 6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น รายละเอียดที่เกี่ยวข้อง: - 6.2.4.1. บทลงโทษ: หากทางทีมงานตรวจสอบพบ หรือได้รั... |
| competition_rov_v2_042 | competition_rules | `competition_rules` | ไม่ตรงตามที่ลงทะเบียน; ปรับแพ้; ตัดสิทธิ์ | คำตอบ: · เวลา 8.00-8.30 ลงทะเบียน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men |
| competition_rov_v2_044 | competition_rules | `competition_rules` | ออฟไลน์; BO3 | คำตอบ: 2.1. PSU Esports Studio – Phuket (อาคาร 5 ชั้น 1) แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men |
| competition_valorant_v2_027 | competition_rules | `competition_rules` | ไม่ส่งผลกระทบ; เล่นต่อ | คำตอบ: ถ้า VALORANT เกิดบั๊กก่อนมี damage เจ้าหน้าที่อาจย้อนรอบ (Round Rollback) ได้ หลักฐานจากกติกา: - เอกสาร Round Rollback ระบุหากบั๊กเกิดก่อนมีการทำดาเมจ เจ้าหน้าที่อาจย้อนรอบได้ อ้างอิงจากกติกา: VALORANT / PSU Phuke... |
| competition_valorant_v2_028 | competition_rules | `competition_rules` | Major Bug | คำตอบ: ถ้าทำ damage ไปแล้ว โดยปกติ VALORANT จะไม่ rollback ยกเว้นได้รับอนุมัติผ่านกระบวนการ Challenge หลักฐานจากกติกา: - เอกสาร Round Rollback ระบุหากมีการทำ damage ไปแล้ว จะไม่มีการย้อนรอบ ยกเว้นผ่านกระบวนการ Challenge... |
| competition_valorant_v2_029 | competition_rules | `competition_rules` | Game-Breaking | คำตอบ: ถ้าทำ damage ไปแล้ว โดยปกติ VALORANT จะไม่ rollback ยกเว้นได้รับอนุมัติผ่านกระบวนการ Challenge หลักฐานจากกติกา: - เอกสาร Round Rollback ระบุหากมีการทำ damage ไปแล้ว จะไม่มีการย้อนรอบ ยกเว้นผ่านกระบวนการ Challenge... |
| competition_valorant_v2_030 | competition_rules | `games` | ก่อน; ดาเมจ; ย้อนรอบ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_032 | competition_rules | `games` | ผิด; ได้เปรียบ; competition_rules_valorant_psu_phuket_2026 | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| competition_valorant_v2_033 | competition_rules | `competition_rules` | ห้าม; Cypher | คำตอบ: ถ้าทำ damage ไปแล้ว โดยปกติ VALORANT จะไม่ rollback ยกเว้นได้รับอนุมัติผ่านกระบวนการ Challenge หลักฐานจากกติกา: - เอกสาร Round Rollback ระบุหากมีการทำ damage ไปแล้ว จะไม่มีการย้อนรอบ ยกเว้นผ่านกระบวนการ Challenge... |
| competition_valorant_v2_035 | competition_rules | `competition_rules` | KAY/O; ZERO/POINT; Texture | คำตอบ: ถ้าทำ damage ไปแล้ว โดยปกติ VALORANT จะไม่ rollback ยกเว้นได้รับอนุมัติผ่านกระบวนการ Challenge หลักฐานจากกติกา: - เอกสาร Round Rollback ระบุหากมีการทำ damage ไปแล้ว จะไม่มีการย้อนรอบ ยกเว้นผ่านกระบวนการ Challenge... |
| competition_valorant_v2_038 | competition_rules | `competition_rules` | Round Rollback; ช่องโหว่ | คำตอบ: ผิด กติกา VALORANT ถือว่าการใช้บั๊กเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจเป็นความผิด หลักฐานจากกติกา: - เอกสาร Exploit Adjudication ระบุการใช้บั๊กหรือ unintended mechanics เพื่อสร้างความได้เปรียบถือเป็นความผิด อ้า... |
| competition_valorant_v2_039 | competition_rules | `competition_rules` | เจตนา; ช่องโหว่ | คำตอบ: บทลงโทษในเกมของ VALORANT ได้แก่ Warning, Round Rollback, Round Loss, Map Forfeit และ Match Forfeit หลักฐานจากกติกา: - เอกสาร In-Game Penalty Types ระบุ Warning, Round Rollback, Round Loss, Map Forfeit และ Match Fo... |
| competition_valorant_v2_047 | competition_rules | `competition_rules` | Agent; Abyss | คำตอบ: * การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่ รายละเอียดที่เกี่ยวข้อง: - แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive - เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2... |
| competition_tekken8_v2_008 | competition_rules | `competition_rules` | No advantage | คำตอบ: Tekken 8 ให้เลือก Stage แบบ Random หลักฐานจากกติกา: - เอกสารการตั้งค่าเกมระบุ Stage: Random อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competition_rules_tekken... |
| competition_tekken8_v2_030 | competition_rules | `competition_rules` | ปรับแพ้ | คำตอบ: Tekken 8 กดหยุดเกมได้เฉพาะกรณีอุปกรณ์ขัดข้องหรือเหตุฉุกเฉินที่สมควร และต้องได้รับการยินยอมหรืออนุญาตตามกติกา หลักฐานจากกติกา: - เอกสารระบุ Pause ได้เฉพาะกรณีมีเหตุผลสมควร เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน และต้อง... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_round4_curated_factcards_20260703.jsonl`
