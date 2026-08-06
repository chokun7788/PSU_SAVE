# User Quality Audit Report

Source results: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\question_bank_runs\20260721_000537_decision_artifact_baseline_400\results_easy.json`

## Summary

•    Total: 400
•    Average score: 8.577 / 10
•    Score levels: {'bad': 14, 'good': 242, 'needs_review': 53, 'usable': 91}
•    Cases below 7: 67
•    Cases below 5: 14

## Category Average

•    equipment_game_inside: 9.626 / 10
•    game_rules: 8.527 / 10
•    out_of_scope: 6.889 / 10
•    play_booking_controls: 9.266 / 10

## Top Issue Tags

•    no_major_issue_detected: 190
•    missing_source_id: 110
•    safe_decline_but_not_useful: 94
•    candidate_execution_mismatch: 46
•    no_answer_for_supported_question: 29
•    wrong_domain_or_source: 17
•    source_not_specific_enough: 14
•    wrong_equipment_focus: 12
•    specific_question_answered_with_full_catalog: 10
•    number_answer_too_verbose: 5
•    reservation_question_answered_as_equipment: 3
•    missing_direct_number: 3

## Main Problems As A Real User

1. บางคำถามเฉพาะเกมถูกตอบเป็น catalog/list ทั้งหมด ทำให้ไม่ได้คำตอบที่ถาม เช่น `ROV คือเกมอะไร` แต่ตอบรายชื่อเกม 44 เกม
2. คำถามเรื่องจองบางข้อถูกตอบเป็นข้อมูลอุปกรณ์ เช่น ถาม Nintendo Switch ต้องเลือกอะไรตอนจอง แต่ตอบรายละเอียดเครื่อง Nintendo Switch OLED
3. คำถามเจาะอุปกรณ์บางข้อจับ item ผิด เช่น ถามจอ/ทีวี/จำนวนชุด แต่คำตอบเริ่มจากอุปกรณ์คนละชิ้น
4. Out-of-scope 94 ข้อจบที่ `general_llm_disabled` เพราะรอบ baseline ปิด LLM จึงปลอดภัยแต่ไม่ค่อยมีประโยชน์กับผู้ใช้ทั่วไป
5. Decision Artifact ช่วยเห็นปัญหาใหม่ว่า selected candidate บางข้อไม่ตรงกับ execution จริง ทำให้ควรปรับ registry/ranking ให้สะท้อนทางที่ใช้จริงขึ้น

## Lowest Scoring Examples

### GR-001 - 1.7/10
Question: ROV คือเกมอะไร
Mode/route: `pipeline:structured_games_catalog` / `games/game_availability_lookup`
Issues: wrong_domain_or_source, specific_question_answered_with_full_catalog, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (23 เกม) • Beat Saber • Call of Duty: Modern Warfare III • EA Sports FC 24 • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Gran T

### GR-026 - 1.7/10
Question: VALORANT คือเกมอะไร
Mode/route: `pipeline:structured_games_catalog` / `games/game_availability_lookup`
Issues: wrong_domain_or_source, specific_question_answered_with_full_catalog, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (23 เกม) • Beat Saber • Call of Duty: Modern Warfare III • EA Sports FC 24 • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Gran T

### GR-051 - 1.7/10
Question: CS2 คือเกมอะไร
Mode/route: `pipeline:structured_games_catalog` / `games/game_availability_lookup`
Issues: wrong_domain_or_source, specific_question_answered_with_full_catalog, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (23 เกม) • Beat Saber • Call of Duty: Modern Warfare III • EA Sports FC 24 • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Gran T

### GR-076 - 1.7/10
Question: TEKKEN 8 คือเกมอะไร
Mode/route: `pipeline:structured_games_catalog` / `games/game_availability_lookup`
Issues: wrong_domain_or_source, specific_question_answered_with_full_catalog, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (23 เกม) • Beat Saber • Call of Duty: Modern Warfare III • EA Sports FC 24 • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Gran T

### PBC-002 - 3.2/10
Question: จอง Nintendo Switch ต้องเลือกอะไรบ้าง
Mode/route: `pipeline:structured_equipment_item` / `reservation/booking_policy`
Issues: reservation_question_answered_as_equipment, wrong_equipment_focus
User problem: ผู้ใช้ถามวิธีจอง/เงื่อนไขจอง แต่ระบบตอบรายละเอียดอุปกรณ์แทน; คำถามเจาะอุปกรณ์ชิ้นหนึ่ง แต่ระบบโฟกัสอุปกรณ์อีกชิ้น
Answer preview: Nintendo Switch OLED: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว จำนวน: 1 Unit อยู่ที่: Nintendo Switch Zone ใช้สำหรับ: • เล่น Mario Kart 8 Deluxe • เล่น Overcooked 2 • เล่น Super Smash Bros Ultimate • เล่น Nintendo Switch Sports แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### PBC-019 - 3.2/10
Question: อยากเล่นพวงมาลัยต้องจองโซนอะไร
Mode/route: `pipeline:structured_equipment_catalog` / `reservation/booking_policy`
Issues: reservation_question_answered_as_equipment, wrong_equipment_focus
User problem: ผู้ใช้ถามวิธีจอง/เงื่อนไขจอง แต่ระบบตอบรายละเอียดอุปกรณ์แทน; คำถามเจาะอุปกรณ์ชิ้นหนึ่ง แต่ระบบโฟกัสอุปกรณ์อีกชิ้น
Answer preview: อุปกรณ์ใน Cockpit Zone: Cockpit Zone • Logitech G923 TRUEFORCE Racing Wheel (2 Units with Driving Force Shifter) • Driving Force Shifter (2 Units with Logitech G923) • Racezone Full Cockpit V3 (2 Units) • Pulse Elite Wireless Headset (2 Units) • TV 65 นิ้ว (2 Units) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### PBC-027 - 3.2/10
Question: จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม
Mode/route: `pipeline:structured_equipment_item` / `equipment/count`
Issues: reservation_question_answered_as_equipment, wrong_equipment_focus
User problem: ผู้ใช้ถามวิธีจอง/เงื่อนไขจอง แต่ระบบตอบรายละเอียดอุปกรณ์แทน; คำถามเจาะอุปกรณ์ชิ้นหนึ่ง แต่ระบบโฟกัสอุปกรณ์อีกชิ้น
Answer preview: Nintendo Switch OLED: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว จำนวน: 1 Unit อยู่ที่: Nintendo Switch Zone ใช้สำหรับ: • เล่น Mario Kart 8 Deluxe • เล่น Overcooked 2 • เล่น Super Smash Bros Ultimate • เล่น Nintendo Switch Sports แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### OOS-010 - 4.7/10
Question: ราคาทองวันนี้เท่าไหร่
Mode/route: `pipeline:general_llm_disabled` / `general/general_knowledge_query`
Issues: missing_direct_number, safe_decline_but_not_useful, missing_source_id
User problem: คำถามต้องการตัวเลข/จำนวน แต่คำตอบไม่มีตัวเลขตรง ๆ; เป็นคำถามนอกเรื่องที่ควรให้ Local LLM ช่วยได้ แต่รอบนี้ปิด LLM จึงตอบไม่ได้; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ครับ ให้เปิด `experimental_allow_llm=True` หรือใช้ notebook local hybrid chat เพื่อให้โมเดลตอบคำถามทั่วไป

### OOS-060 - 4.7/10
Question: ค่าเงิน USD เป็น THB เท่าไหร่
Mode/route: `pipeline:general_llm_disabled` / `general/general_knowledge_query`
Issues: missing_direct_number, safe_decline_but_not_useful, missing_source_id
User problem: คำถามต้องการตัวเลข/จำนวน แต่คำตอบไม่มีตัวเลขตรง ๆ; เป็นคำถามนอกเรื่องที่ควรให้ Local LLM ช่วยได้ แต่รอบนี้ปิด LLM จึงตอบไม่ได้; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ครับ ให้เปิด `experimental_allow_llm=True` หรือใช้ notebook local hybrid chat เพื่อให้โมเดลตอบคำถามทั่วไป

### OOS-061 - 4.7/10
Question: Bitcoin ราคาเท่าไหร่
Mode/route: `pipeline:general_llm_disabled` / `general/general_knowledge_query`
Issues: missing_direct_number, safe_decline_but_not_useful, missing_source_id
User problem: คำถามต้องการตัวเลข/จำนวน แต่คำตอบไม่มีตัวเลขตรง ๆ; เป็นคำถามนอกเรื่องที่ควรให้ Local LLM ช่วยได้ แต่รอบนี้ปิด LLM จึงตอบไม่ได้; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ครับ ให้เปิด `experimental_allow_llm=True` หรือใช้ notebook local hybrid chat เพื่อให้โมเดลตอบคำถามทั่วไป

### GR-013 - 4.8/10
Question: ROV รอบชิงเล่นกี่เกม
Mode/route: `pipeline:structured_games_catalog` / `competition_rules/competition_rules_lookup`
Issues: specific_question_answered_with_full_catalog, number_answer_too_verbose, source_not_specific_enough
User problem: ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; มีตัวเลขอยู่ แต่คำตอบยาวเกินและไม่ได้ตอบตัวเลขก่อน; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (23 เกม) • Beat Saber • Call of Duty: Modern Warfare III • EA Sports FC 24 • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Gran T

### GR-038 - 4.8/10
Question: VALORANT รอบชิงเล่นกี่เกม
Mode/route: `pipeline:structured_games_catalog` / `competition_rules/competition_rules_lookup`
Issues: specific_question_answered_with_full_catalog, number_answer_too_verbose, source_not_specific_enough
User problem: ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; มีตัวเลขอยู่ แต่คำตอบยาวเกินและไม่ได้ตอบตัวเลขก่อน; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (23 เกม) • Beat Saber • Call of Duty: Modern Warfare III • EA Sports FC 24 • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Gran T

### GR-063 - 4.8/10
Question: CS2 รอบชิงเล่นกี่เกม
Mode/route: `pipeline:structured_games_catalog` / `competition_rules/competition_rules_lookup`
Issues: specific_question_answered_with_full_catalog, number_answer_too_verbose, source_not_specific_enough
User problem: ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; มีตัวเลขอยู่ แต่คำตอบยาวเกินและไม่ได้ตอบตัวเลขก่อน; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (23 เกม) • Beat Saber • Call of Duty: Modern Warfare III • EA Sports FC 24 • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Gran T

### GR-088 - 4.8/10
Question: TEKKEN 8 รอบชิงเล่นกี่เกม
Mode/route: `pipeline:structured_games_catalog` / `competition_rules/competition_rules_lookup`
Issues: specific_question_answered_with_full_catalog, number_answer_too_verbose, source_not_specific_enough
User problem: ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; มีตัวเลขอยู่ แต่คำตอบยาวเกินและไม่ได้ตอบตัวเลขก่อน; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (23 เกม) • Beat Saber • Call of Duty: Modern Warfare III • EA Sports FC 24 • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Gran T

### EGI-093 - 5.5/10
Question: เกมไหนมีข้อมูลปุ่มครบ
Mode/route: `pipeline:game_control_missing_game_context` / `games/game_control_lookup`
Issues: wrong_domain_or_source, missing_source_id
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### EGI-100 - 5.5/10
Question: เกมที่ใช้จอย PS5 มีอะไร
Mode/route: `pipeline:game_control_missing_game_context` / `games/game_control_lookup`
Issues: wrong_domain_or_source, missing_source_id
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-062 - 5.6/10
Question: Overcooked 2 ปุ่มหยิบของคืออะไร
Mode/route: `pipeline:structured_game_controls_no_data` / `games/game_control_lookup`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ

### PBC-063 - 5.6/10
Question: Overcooked 2 ปุ่มหั่นของคืออะไร
Mode/route: `pipeline:structured_game_controls_no_data` / `games/game_control_lookup`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ

### PBC-066 - 5.6/10
Question: Nintendo Switch Sports ใช้จอยยังไง
Mode/route: `pipeline:structured_game_controls_no_data` / `games/game_control_lookup`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Nintendo Switch Sports ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ

### PBC-076 - 5.6/10
Question: Minecraft มีปุ่มอะไรบ้างในศูนย์
Mode/route: `pipeline:game_control_named_no_data` / `games/game_control_lookup`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Minecraft ที่ยืนยันได้ในฐานข้อมูลของศูนย์ตอนนี้ครับ ถ้าต้องการถามว่าเกมนี้มีให้เล่นในศูนย์ไหม หรือเป็นเกมแนวไหน สามารถถามต่อได้เลย

### PBC-077 - 5.6/10
Question: ROV มีปุ่มในเครื่องศูนย์ไหม
Mode/route: `pipeline:game_control_named_no_data` / `games/game_control_lookup`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ RoV / Arena of Valor ที่ยืนยันได้ในฐานข้อมูลของศูนย์ตอนนี้ครับ ถ้าต้องการถามว่าเกมนี้มีให้เล่นในศูนย์ไหม หรือเป็นเกมแนวไหน สามารถถามต่อได้เลย

### PBC-095 - 5.6/10
Question: Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง
Mode/route: `pipeline:structured_game_controls_no_data` / `games/game_control_lookup`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ

### GR-027 - 5.8/10
Question: VALORANT เป็นเกมแนวไหน
Mode/route: `pipeline:game_name_mention_detail_fast_path` / `games/game_detail_lookup`
Issues: wrong_domain_or_source, source_not_specific_enough, candidate_execution_mismatch
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง; ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน
Answer preview: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม เล่นได้ที่: PC Zone แหล่งข้อมูล

### GR-052 - 5.8/10
Question: CS2 เป็นเกมแนวไหน
Mode/route: `pipeline:game_name_mention_detail_fast_path` / `games/game_detail_lookup`
Issues: wrong_domain_or_source, source_not_specific_enough, candidate_execution_mismatch
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง; ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน
Answer preview: Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม แนวเกม: เกมยิง Tactical FPS วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ เล่นได้ที่: PC Zone แหล่งข้อมูล: ht

### GR-077 - 5.8/10
Question: TEKKEN 8 เป็นเกมแนวไหน
Mode/route: `pipeline:game_name_mention_detail_fast_path` / `games/game_detail_lookup`
Issues: wrong_domain_or_source, source_not_specific_enough, candidate_execution_mismatch
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง; ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน
Answer preview: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นได้ที่: PC Zone และ PlayStation 5 Zone แหล่งข้อมูล: https://e

### EGI-089 - 5.9/10
Question: Minecraft มีไหม
Mode/route: `pipeline:games_known_unsupported_fast_path` / `games/availability_lookup`
Issues: specific_question_answered_with_full_catalog, candidate_execution_mismatch
User problem: ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน
Answer preview: ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด 36 เกม: PC Zone (6 เกม) • VALORANT • Counter-Strike 2 • PUBG: BATTLEGROUNDS • Call of Duty: Warzone • TEKKEN 8 • League of Legends PlaySt

### EGI-091 - 5.9/10
Question: ROV มีให้เล่นในศูนย์ไหม
Mode/route: `pipeline:games_known_unsupported_fast_path` / `games/game_availability_lookup`
Issues: specific_question_answered_with_full_catalog, candidate_execution_mismatch
User problem: ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน
Answer preview: ยังไม่พบ RoV / Arena of Valor ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ในฐานข้อมูลมีข้อมูลกติกาการแข่งขันของเกมนี้ แต่ยังไม่พบว่าอยู่ในรายการเกมให้เล่นของศูนย์ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด 36 เกม: PC Zone (6 เกม) • VALORANT • 

### OOS-042 - 6.3/10
Question: ควรดื่มน้ำวันละเท่าไหร่
Mode/route: `pipeline:rag_direct_curated` / `service_fee/service_fee_query`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### OOS-043 - 6.3/10
Question: อาหารเช้าควรกินอะไร
Mode/route: `pipeline:rules_fast_path` / `rules/studio_rules`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-064 - 6.3/10
Question: วิธีจองตั๋วเครื่องบินราคาถูก
Mode/route: `pipeline:structured_service_fee` / `service_fee/service_fee_query`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: ราคา PC: ยังไม่พบราคาที่ตรวจยืนยันได้ใน Service Fee 2026 ครับ ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR ดังนั้นยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง ควรถามเจ้าหน้าที่หรืออัปเดตตารางราคา PC เพิ่มก่อน แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-ph

## Low Examples By Category

### equipment_game_inside
•    EGI-093 (5.5/10): เกมไหนมีข้อมูลปุ่มครบ -> wrong_domain_or_source, missing_source_id
•    EGI-100 (5.5/10): เกมที่ใช้จอย PS5 มีอะไร -> wrong_domain_or_source, missing_source_id
•    EGI-089 (5.9/10): Minecraft มีไหม -> specific_question_answered_with_full_catalog, candidate_execution_mismatch
•    EGI-091 (5.9/10): ROV มีให้เล่นในศูนย์ไหม -> specific_question_answered_with_full_catalog, candidate_execution_mismatch
•    EGI-092 (6.4/10): เกมไหนยังไม่มีข้อมูลบ้าง -> no_answer_for_supported_question, candidate_execution_mismatch
•    EGI-003 (6.8/10): PC Zone ใช้จออะไร -> wrong_equipment_focus
•    EGI-008 (6.8/10): Cockpit Zone มีทีวีกี่เครื่อง -> wrong_equipment_focus
•    EGI-028 (6.8/10): โซนไหนมีทีวีขนาด 86 นิ้ว -> wrong_equipment_focus

### game_rules
•    GR-001 (1.7/10): ROV คือเกมอะไร -> wrong_domain_or_source, specific_question_answered_with_full_catalog, source_not_specific_enough
•    GR-026 (1.7/10): VALORANT คือเกมอะไร -> wrong_domain_or_source, specific_question_answered_with_full_catalog, source_not_specific_enough
•    GR-051 (1.7/10): CS2 คือเกมอะไร -> wrong_domain_or_source, specific_question_answered_with_full_catalog, source_not_specific_enough
•    GR-076 (1.7/10): TEKKEN 8 คือเกมอะไร -> wrong_domain_or_source, specific_question_answered_with_full_catalog, source_not_specific_enough
•    GR-013 (4.8/10): ROV รอบชิงเล่นกี่เกม -> specific_question_answered_with_full_catalog, number_answer_too_verbose, source_not_specific_enough
•    GR-038 (4.8/10): VALORANT รอบชิงเล่นกี่เกม -> specific_question_answered_with_full_catalog, number_answer_too_verbose, source_not_specific_enough
•    GR-063 (4.8/10): CS2 รอบชิงเล่นกี่เกม -> specific_question_answered_with_full_catalog, number_answer_too_verbose, source_not_specific_enough
•    GR-088 (4.8/10): TEKKEN 8 รอบชิงเล่นกี่เกม -> specific_question_answered_with_full_catalog, number_answer_too_verbose, source_not_specific_enough

### out_of_scope
•    OOS-010 (4.7/10): ราคาทองวันนี้เท่าไหร่ -> missing_direct_number, safe_decline_but_not_useful, missing_source_id
•    OOS-060 (4.7/10): ค่าเงิน USD เป็น THB เท่าไหร่ -> missing_direct_number, safe_decline_but_not_useful, missing_source_id
•    OOS-061 (4.7/10): Bitcoin ราคาเท่าไหร่ -> missing_direct_number, safe_decline_but_not_useful, missing_source_id
•    OOS-042 (6.3/10): ควรดื่มน้ำวันละเท่าไหร่ -> wrong_domain_or_source
•    OOS-043 (6.3/10): อาหารเช้าควรกินอะไร -> wrong_domain_or_source
•    OOS-064 (6.3/10): วิธีจองตั๋วเครื่องบินราคาถูก -> wrong_domain_or_source
•    OOS-076 (6.3/10): ประวัติศาสตร์สงครามโลกครั้งที่สอง -> wrong_domain_or_source
•    OOS-085 (6.3/10): ทำไมคอมเปิดไม่ติด -> wrong_domain_or_source

### play_booking_controls
•    PBC-002 (3.2/10): จอง Nintendo Switch ต้องเลือกอะไรบ้าง -> reservation_question_answered_as_equipment, wrong_equipment_focus
•    PBC-019 (3.2/10): อยากเล่นพวงมาลัยต้องจองโซนอะไร -> reservation_question_answered_as_equipment, wrong_equipment_focus
•    PBC-027 (3.2/10): จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม -> reservation_question_answered_as_equipment, wrong_equipment_focus
•    PBC-062 (5.6/10): Overcooked 2 ปุ่มหยิบของคืออะไร -> no_answer_for_supported_question, missing_source_id
•    PBC-063 (5.6/10): Overcooked 2 ปุ่มหั่นของคืออะไร -> no_answer_for_supported_question, missing_source_id
•    PBC-066 (5.6/10): Nintendo Switch Sports ใช้จอยยังไง -> no_answer_for_supported_question, missing_source_id
•    PBC-076 (5.6/10): Minecraft มีปุ่มอะไรบ้างในศูนย์ -> no_answer_for_supported_question, missing_source_id
•    PBC-077 (5.6/10): ROV มีปุ่มในเครื่องศูนย์ไหม -> no_answer_for_supported_question, missing_source_id
