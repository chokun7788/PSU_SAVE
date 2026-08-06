# User Quality Audit Report

Source results: `data\eval\question_bank_runs\20260721_012559_20260721_tool_preconditions_v1_400\results.json`

## Summary

•    Total: 400
•    Average score: 8.716 / 10
•    Score levels: {'good': 248, 'needs_review': 58, 'usable': 91, 'bad': 3}
•    Cases below 7: 61
•    Cases below 5: 3

## Category Average

•    equipment_game_inside: 9.626 / 10
•    game_rules: 8.848 / 10
•    out_of_scope: 6.889 / 10
•    play_booking_controls: 9.502 / 10

## Top Issue Tags

•    no_major_issue_detected: 196
•    missing_source_id: 110
•    safe_decline_but_not_useful: 94
•    candidate_execution_mismatch: 46
•    no_answer_for_supported_question: 32
•    wrong_domain_or_source: 16
•    wrong_equipment_focus: 8
•    source_not_specific_enough: 6
•    missing_direct_number: 3
•    specific_question_answered_with_full_catalog: 2
•    number_answer_too_verbose: 1

## Main Problems As A Real User

1. บางคำถามเฉพาะเกมถูกตอบเป็น catalog/list ทั้งหมด ทำให้ไม่ได้คำตอบที่ถาม เช่น `ROV คือเกมอะไร` แต่ตอบรายชื่อเกม 44 เกม
2. คำถามเรื่องจองบางข้อถูกตอบเป็นข้อมูลอุปกรณ์ เช่น ถาม Nintendo Switch ต้องเลือกอะไรตอนจอง แต่ตอบรายละเอียดเครื่อง Nintendo Switch OLED
3. คำถามเจาะอุปกรณ์บางข้อจับ item ผิด เช่น ถามจอ/ทีวี/จำนวนชุด แต่คำตอบเริ่มจากอุปกรณ์คนละชิ้น
4. Out-of-scope 94 ข้อจบที่ `general_llm_disabled` เพราะรอบ baseline ปิด LLM จึงปลอดภัยแต่ไม่ค่อยมีประโยชน์กับผู้ใช้ทั่วไป
5. Decision Artifact ช่วยเห็นปัญหาใหม่ว่า selected candidate บางข้อไม่ตรงกับ execution จริง ทำให้ควรปรับ registry/ranking ให้สะท้อนทางที่ใช้จริงขึ้น

## Lowest Scoring Examples

### OOS-010 - 4.7/10
Question: ราคาทองวันนี้เท่าไหร่
Mode/route: `pipeline:general_llm_disabled` / `None`
Issues: missing_direct_number, safe_decline_but_not_useful, missing_source_id
User problem: คำถามต้องการตัวเลข/จำนวน แต่คำตอบไม่มีตัวเลขตรง ๆ; เป็นคำถามนอกเรื่องที่ควรให้ Local LLM ช่วยได้ แต่รอบนี้ปิด LLM จึงตอบไม่ได้; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ครับ ให้เปิด `experimental_allow_llm=True` หรือใช้ notebook local hybrid chat เพื่อให้โมเดลตอบคำถามทั่วไป

### OOS-060 - 4.7/10
Question: ค่าเงิน USD เป็น THB เท่าไหร่
Mode/route: `pipeline:general_llm_disabled` / `None`
Issues: missing_direct_number, safe_decline_but_not_useful, missing_source_id
User problem: คำถามต้องการตัวเลข/จำนวน แต่คำตอบไม่มีตัวเลขตรง ๆ; เป็นคำถามนอกเรื่องที่ควรให้ Local LLM ช่วยได้ แต่รอบนี้ปิด LLM จึงตอบไม่ได้; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ครับ ให้เปิด `experimental_allow_llm=True` หรือใช้ notebook local hybrid chat เพื่อให้โมเดลตอบคำถามทั่วไป

### OOS-061 - 4.7/10
Question: Bitcoin ราคาเท่าไหร่
Mode/route: `pipeline:general_llm_disabled` / `None`
Issues: missing_direct_number, safe_decline_but_not_useful, missing_source_id
User problem: คำถามต้องการตัวเลข/จำนวน แต่คำตอบไม่มีตัวเลขตรง ๆ; เป็นคำถามนอกเรื่องที่ควรให้ Local LLM ช่วยได้ แต่รอบนี้ปิด LLM จึงตอบไม่ได้; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ครับ ให้เปิด `experimental_allow_llm=True` หรือใช้ notebook local hybrid chat เพื่อให้โมเดลตอบคำถามทั่วไป

### EGI-093 - 5.5/10
Question: เกมไหนมีข้อมูลปุ่มครบ
Mode/route: `pipeline:game_control_missing_game_context` / `None`
Issues: wrong_domain_or_source, missing_source_id
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### EGI-100 - 5.5/10
Question: เกมที่ใช้จอย PS5 มีอะไร
Mode/route: `pipeline:game_control_missing_game_context` / `None`
Issues: wrong_domain_or_source, missing_source_id
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ

### PBC-062 - 5.6/10
Question: Overcooked 2 ปุ่มหยิบของคืออะไร
Mode/route: `pipeline:structured_game_controls_no_data` / `None`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ

### PBC-063 - 5.6/10
Question: Overcooked 2 ปุ่มหั่นของคืออะไร
Mode/route: `pipeline:structured_game_controls_no_data` / `None`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ

### PBC-066 - 5.6/10
Question: Nintendo Switch Sports ใช้จอยยังไง
Mode/route: `pipeline:structured_game_controls_no_data` / `None`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Nintendo Switch Sports ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ

### PBC-076 - 5.6/10
Question: Minecraft มีปุ่มอะไรบ้างในศูนย์
Mode/route: `pipeline:game_control_named_no_data` / `None`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Minecraft ที่ยืนยันได้ในฐานข้อมูลของศูนย์ตอนนี้ครับ ถ้าต้องการถามว่าเกมนี้มีให้เล่นในศูนย์ไหม หรือเป็นเกมแนวไหน สามารถถามต่อได้เลย

### PBC-077 - 5.6/10
Question: ROV มีปุ่มในเครื่องศูนย์ไหม
Mode/route: `pipeline:game_control_named_no_data` / `None`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ RoV / Arena of Valor ที่ยืนยันได้ในฐานข้อมูลของศูนย์ตอนนี้ครับ ถ้าต้องการถามว่าเกมนี้มีให้เล่นในศูนย์ไหม หรือเป็นเกมแนวไหน สามารถถามต่อได้เลย

### PBC-095 - 5.6/10
Question: Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง
Mode/route: `pipeline:structured_game_controls_no_data` / `None`
Issues: no_answer_for_supported_question, missing_source_id
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ไม่มี source id ให้ตรวจสอบย้อนกลับ
Answer preview: ยังไม่พบข้อมูลปุ่มควบคุมของ Overcooked 2 ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ

### GR-026 - 5.8/10
Question: VALORANT คือเกมอะไร
Mode/route: `pipeline:structured_game_detail` / `None`
Issues: wrong_domain_or_source, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม เล่นได้ที่: PC Zone แหล่งข้อมูล

### GR-027 - 5.8/10
Question: VALORANT เป็นเกมแนวไหน
Mode/route: `pipeline:structured_game_detail` / `None`
Issues: wrong_domain_or_source, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม เล่นได้ที่: PC Zone แหล่งข้อมูล

### GR-051 - 5.8/10
Question: CS2 คือเกมอะไร
Mode/route: `pipeline:structured_game_detail` / `None`
Issues: wrong_domain_or_source, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม แนวเกม: เกมยิง Tactical FPS วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ เล่นได้ที่: PC Zone แหล่งข้อมูล: ht

### GR-052 - 5.8/10
Question: CS2 เป็นเกมแนวไหน
Mode/route: `pipeline:structured_game_detail` / `None`
Issues: wrong_domain_or_source, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม แนวเกม: เกมยิง Tactical FPS วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ เล่นได้ที่: PC Zone แหล่งข้อมูล: ht

### GR-076 - 5.8/10
Question: TEKKEN 8 คือเกมอะไร
Mode/route: `pipeline:structured_game_detail` / `None`
Issues: wrong_domain_or_source, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นได้ที่: PC Zone และ PlayStation 5 Zone แหล่งข้อมูล: https://e

### GR-077 - 5.8/10
Question: TEKKEN 8 เป็นเกมแนวไหน
Mode/route: `pipeline:structured_game_detail` / `None`
Issues: wrong_domain_or_source, source_not_specific_enough
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ; แหล่งข้อมูลไม่ชี้ไปกติกาการแข่งขันโดยตรง
Answer preview: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นได้ที่: PC Zone และ PlayStation 5 Zone แหล่งข้อมูล: https://e

### EGI-089 - 5.9/10
Question: Minecraft มีไหม
Mode/route: `pipeline:games_known_unsupported_fast_path` / `None`
Issues: specific_question_answered_with_full_catalog, candidate_execution_mismatch
User problem: ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน
Answer preview: ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด 36 เกม: PC Zone (6 เกม) • VALORANT • Counter-Strike 2 • PUBG: BATTLEGROUNDS • Call of Duty: Warzone • TEKKEN 8 • League of Legends PlaySt

### EGI-091 - 5.9/10
Question: ROV มีให้เล่นในศูนย์ไหม
Mode/route: `pipeline:games_known_unsupported_fast_path` / `None`
Issues: specific_question_answered_with_full_catalog, candidate_execution_mismatch
User problem: ผู้ใช้ถามเกมเฉพาะ แต่ระบบตอบ catalog เกมทั้งหมด ทำให้ไม่ตอบคำถาม; ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน
Answer preview: ยังไม่พบ RoV / Arena of Valor ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ในฐานข้อมูลมีข้อมูลกติกาการแข่งขันของเกมนี้ แต่ยังไม่พบว่าอยู่ในรายการเกมให้เล่นของศูนย์ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด 36 เกม: PC Zone (6 เกม) • VALORANT • 

### OOS-042 - 6.3/10
Question: ควรดื่มน้ำวันละเท่าไหร่
Mode/route: `pipeline:rag_direct_curated` / `None`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### OOS-043 - 6.3/10
Question: อาหารเช้าควรกินอะไร
Mode/route: `pipeline:rules_fast_path` / `None`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-064 - 6.3/10
Question: วิธีจองตั๋วเครื่องบินราคาถูก
Mode/route: `pipeline:category_rule_fast_path` / `None`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### OOS-076 - 6.3/10
Question: ประวัติศาสตร์สงครามโลกครั้งที่สอง
Mode/route: `pipeline:penalty_fast_path` / `None`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-085 - 6.3/10
Question: ทำไมคอมเปิดไม่ติด
Mode/route: `pipeline:structured_schedule` / `None`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open • วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open • วันพฤหัสบดี: Mor

### OOS-097 - 6.3/10
Question: เพลงฮิตตอนนี้มีอะไรบ้าง
Mode/route: `pipeline:experimental_rag_no_context` / `None`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: โหมดทดลอง RAG: ยังไม่มี context ที่โยงกับคำถามนี้ได้ชัดในฐานข้อมูลหมวด schedule ถ้าต้องการให้ตอบได้ ควรเพิ่ม fact/card หรือข้อมูลจริงของเรื่องนั้นเข้า knowledge base ก่อน

### PBC-067 - 6.3/10
Question: Beat Saber เล่นยังไง
Mode/route: `pipeline:structured_game_detail` / `None`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: Beat Saber: Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง แนวเกม: เกม VR Rhythm วิธีเล่นโดยสรุป: สวมแว่น VR ถือคอนโทรลเลอร์ แล้วฟันบล็อกตามทิศทาง หลบสิ่งกีดขวาง และพยายามทำคะแนนตามจังหวะเพลง เล่นได้ที่: PlayStation 5 Zone และ VR Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-

### PBC-068 - 6.3/10
Question: Gran Turismo 7 ใช้พวงมาลัยยังไง
Mode/route: `pipeline:structured_game_detail` / `None`
Issues: wrong_domain_or_source
User problem: คำตอบใช้ฐานข้อมูล/หมวดผิดจากสิ่งที่ควรตอบ
Answer preview: Gran Turismo 7: Gran Turismo 7 คือเกมแข่งรถที่เน้นการขับรถสมจริง การเลือกสนาม รถ และการควบคุมจังหวะเข้าโค้ง แนวเกม: เกมแข่งรถ / Driving Simulator วิธีเล่นโดยสรุป: ใน Cockpit Zone เล่นโดยใช้พวงมาลัย คันเร่ง เบรก และชุดเบาะจำลองการขับรถ เป้าหมายคือขับให้เร็วและควบคุมรถให้แม่นในแต่ละสนาม เล่นได้ที่: Cockpit Zone และ PlayS

### EGI-092 - 6.4/10
Question: เกมไหนยังไม่มีข้อมูลบ้าง
Mode/route: `pipeline:games_missing_data_fast_path` / `None`
Issues: no_answer_for_supported_question, candidate_execution_mismatch
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล; ระบบเลือก candidate แบบหนึ่ง แต่ execution จริงไปอีกทางหนึ่ง ทำให้ debug สับสน
Answer preview: ตอนนี้ระบบยังไม่สามารถสรุปรายชื่อเกมที่ไม่มีข้อมูลทั้งหมดได้แบบครบถ้วนครับ เพราะฐานข้อมูลยืนยันได้เฉพาะเกม/รายการที่มีข้อมูลอยู่แล้ว ไม่ได้มี master list ของทุกเกมที่ควรมีแต่ยังขาดข้อมูล สิ่งที่ยืนยันได้ตอนนี้คือรายการเกมที่มีข้อมูลแล้ว: PC Zone (6 เกม) • VALORANT • Counter-Strike 2 • PUBG: BATTLEGROUNDS • Call of Duty

### GR-005 - 6.4/10
Question: ROV มีตัวสำรองได้ไหม
Mode/route: `pipeline:competition_generic_fast_path` / `None`
Issues: no_answer_for_supported_question
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล
Answer preview: RoV ยังไม่พบข้อมูลตัวสำรองที่ระบุชัดเจนครับ • ข้อมูลที่ยืนยันได้คือแข่งแบบ 5v5 • ถ้าจะใช้ตัวสำรองควรยึดประกาศผู้จัดหรือสอบถามกรรมการก่อนแข่ง แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

### GR-010 - 6.4/10
Question: ROV ใช้โปรแกรมช่วยเล่นได้ไหม
Mode/route: `pipeline:competition_generic_fast_path` / `None`
Issues: no_answer_for_supported_question
User problem: คำถามควรมีข้อมูลรองรับ แต่ระบบตอบว่าไม่มีข้อมูล
Answer preview: RoV ยังไม่พบข้อมูลชัดเจนเรื่องโปรแกรมช่วยเล่นในไฟล์กติกาที่มีครับ • ข้อมูลอุปกรณ์ที่ยืนยันได้: ใช้โทรศัพท์มือถือในการแข่งขัน และไม่อนุญาต Tablet/iPad • ถ้าเป็นโปรแกรมช่วยเล่นควรถือว่าเสี่ยงผิดกติกาและถามกรรมการก่อนแข่ง แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

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
•    GR-026 (5.8/10): VALORANT คือเกมอะไร -> wrong_domain_or_source, source_not_specific_enough
•    GR-027 (5.8/10): VALORANT เป็นเกมแนวไหน -> wrong_domain_or_source, source_not_specific_enough
•    GR-051 (5.8/10): CS2 คือเกมอะไร -> wrong_domain_or_source, source_not_specific_enough
•    GR-052 (5.8/10): CS2 เป็นเกมแนวไหน -> wrong_domain_or_source, source_not_specific_enough
•    GR-076 (5.8/10): TEKKEN 8 คือเกมอะไร -> wrong_domain_or_source, source_not_specific_enough
•    GR-077 (5.8/10): TEKKEN 8 เป็นเกมแนวไหน -> wrong_domain_or_source, source_not_specific_enough
•    GR-005 (6.4/10): ROV มีตัวสำรองได้ไหม -> no_answer_for_supported_question
•    GR-010 (6.4/10): ROV ใช้โปรแกรมช่วยเล่นได้ไหม -> no_answer_for_supported_question

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
•    PBC-062 (5.6/10): Overcooked 2 ปุ่มหยิบของคืออะไร -> no_answer_for_supported_question, missing_source_id
•    PBC-063 (5.6/10): Overcooked 2 ปุ่มหั่นของคืออะไร -> no_answer_for_supported_question, missing_source_id
•    PBC-066 (5.6/10): Nintendo Switch Sports ใช้จอยยังไง -> no_answer_for_supported_question, missing_source_id
•    PBC-076 (5.6/10): Minecraft มีปุ่มอะไรบ้างในศูนย์ -> no_answer_for_supported_question, missing_source_id
•    PBC-077 (5.6/10): ROV มีปุ่มในเครื่องศูนย์ไหม -> no_answer_for_supported_question, missing_source_id
•    PBC-095 (5.6/10): Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง -> no_answer_for_supported_question, missing_source_id
•    PBC-067 (6.3/10): Beat Saber เล่นยังไง -> wrong_domain_or_source
•    PBC-068 (6.3/10): Gran Turismo 7 ใช้พวงมาลัยยังไง -> wrong_domain_or_source
