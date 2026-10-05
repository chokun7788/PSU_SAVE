# วิเคราะห์ผลชุดใหญ่ r30

## สิ่งที่แก้แล้วและสาเหตุที่พิสูจน์ได้

1. ราคาแบบหลายระยะเวลา: parser เดิมเลือกตัวเลขชุดเดียว; เพิ่มรายการ duration พร้อมหน่วยและคำนวณแต่ละตัวเลือกตามตารางเดิม จำนวนรอบเดิมยังใช้เดิม
2. ปุ่มเฉพาะ: ชื่อปุ่มถูกชนกับคำในชื่อเกม/คำอธิบาย จึงได้รายการอื่น; เลือกชื่อปุ่มก่อนและรักษารหัสเลข ไม่เปลี่ยน R9 ให้เป็น R1
3. จองเพื่อเล่นเกม: booking steps ผ่านกฎทั่วไปก่อน game-to-service จึงขาดบริการที่ถาม; อ่าน catalog บริการตรงเกมแล้วแยกข้อความว่าไม่ได้ยืนยัน slot ว่าง
4. ไม่มีต้นฉบับนโยบาย: generic English fallback เหมารวมเป็น missing translation; ตรวจ source gap แยกและไม่แนบ homepage เป็นหลักฐานของกฎที่ไม่มี
5. การตรวจคำตอบปฏิเสธคำตอบที่ถูก: ชนิดงานคาด equipment/list หรือ generic fact แม้คำนวณราคาแล้ว และบังคับแหล่งราคา PC ในคำถามยืนยันกลุ่ม; เชื่อม operation ให้ถูก เพิ่มคำว่า ค่าเล่น และยกเว้น source-price gate เฉพาะ clarification ที่ไม่กล่าวราคา
6. ขอบที่พบเพิ่ม: สามตัวเลือกถูกตกหล่นตัวแรก กลุ่มที่ถูกปฏิเสธกลับถูกนับเป็น PSU นักศึกษา และรหัสปุ่ม Q9/Z9 หลุดไปแสดงทั้งหมด แก้และเพิ่ม negative controls แล้ว
7. กฎ implicit: ผู้เล่นหลัก/เปลี่ยนตัว/ปิดเลือดและศพหลุดไปเกมหรือหัวข้อหน้างาน; ผูก target และ proposition กับข้อ source เดียว พร้อม negative controls ไม่เปลี่ยนตัวละครเป็น roster
8. Web ingress: layout_direction เป็น candidate ทุกข้อความ แม้ score ต่ำและไม่มี mismatch flag; ให้เฉพาะ decision ที่จำแนกแล้วมีผลต่อภาษา หยุดภาษาไทยถูกโยนไป EN โดย candidate ที่ไม่ผ่าน

## หลักฐานก่อน/หลัง

ชุด 69 ข้อเดิม: baseline 15 → A 40 → B/C/F 69 ข้อผ่าน; ชุดเพิ่มขอบเป็น 79 ข้อ: D 75 → E 78 → F 79 ทั้ง guard profile แบบเว็บ และ API จริง 79/79 การเพิ่มขอบทำให้พบข้อผิดพลาดที่ชุดเดิมไม่ตรวจ ไม่ใช่หลักฐานว่าทุกประโยคใหม่จะถูก

## ผลแต่ละชุด — ไม่รวมเป็นความแม่นยำเดียว

| ชุด | ผ่านเกณฑ์ที่ระบุ / ตรวจ | ข้อจำกัด |
|---|---:|---|
| answer_quality_cases.jsonl | 22/26 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| routing_eval_cases.jsonl | 30/40 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| routing_eval_real_usage.jsonl | 88/115 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| broad_usage_eval_v1.json | 636/651 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| model_benchmark_1500.json | 1331/1600 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| thai_multi_error_from_verified49_20260929.jsonl | 110/110 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| thai_noisy_input_pairs_20260929.jsonl | 98/98 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| user_question_bank_400.json | 399/400 | observation/เกณฑ์สนับสนุนไม่พอพิสูจน์คำตอบถูก |
| thai_multi_error_holdout25_20260929.jsonl | 49/50 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| thai_noisy_input_holdout_20260929.jsonl | 50/50 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| real_usage_golden_v1.jsonl | 23/24 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| competition_composition_r28_280_20261001.json | 280/280 | complete clause และ first line; ไม่ใช่ผู้จัดรับรอง |
| competition_content_contract_r27_320_20261001.json | 320/320 | complete clause และ first line; ไม่ใช่ผู้จัดรับรอง |
| competition_new_questions_r27_128_20261001.json | 128/128 | complete clause และ first line; ไม่ใช่ผู้จัดรับรอง |
| competition_rules_rag_ground_truth_v1.jsonl | 548/548 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| competition_user_r24_2000_20261001.jsonl | 2000/2000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| master_ground_truth_bilingual_10000_v1.jsonl | 9347/10000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| master_ground_truth_bilingual_10000_v2.jsonl | 9591/10000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| master_ground_truth_th_5000_v1.jsonl | 4613/5000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| master_ground_truth_th_5000_v2.jsonl | 4703/5000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| master_gt_bilingual_multi_error_2000_20260929_r15.jsonl | 3673/4000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| competition_rules_rag_ground_truth_v2_expanded.jsonl | 178/282 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| english_gold_400_20260902.jsonl | 286/400 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| rag_robustness_ground_truth_v1.jsonl | 477/600 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| master_ground_truth_en_5000_v1.jsonl | 4734/5000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| master_ground_truth_en_5000_v2.jsonl | 4888/5000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| english_shadow_1600_machine_20260908.jsonl | 1229/1600 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| review_grounded_novel_20260925.jsonl | 41/41 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| english_shadow_1600_machine_sample_20260908_v4.jsonl | 6/6 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| english_shadow_1600_machine_sample_20260908_v2.jsonl | 6/6 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| english_shadow_1600_machine_sample_20260908_v3.jsonl | 3/3 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| english_shadow_1600_machine_sample_20260908.jsonl | 5/5 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| intent_trap_bilingual_1000_v1.jsonl | 876/1000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| intent_trap_bilingual_1000_v2.jsonl | 990/1000 | เกณฑ์เดิม/route หรือข้อความ; ดู evidence level |
| intent_trap_english_reference_200_20260926.jsonl | 200/200 | observation/เกณฑ์สนับสนุนไม่พอพิสูจน์คำตอบถูก |

## เปรียบเทียบคำตอบ clean/noisy 2,000 คู่

{"pairs": 2000, "legacy_clean_passed": 1892, "legacy_noisy_passed": 1781, "v2_clean_passed": 1740, "v2_noisy_passed": 1640, "v2_regressions": 117, "scope": "strict outcome and content overlay, not owner approved and not a booking oracle"}

## ประเภทของข้อที่เหลือและแนวทาง

### P1: งาน/ภาษา/เป้าหมายยังเสียความหมายในบางข้อความ

ตัวอย่าง Direct runner: `The Last of Us Part I / Part II ราคาเท่าไหร่` ตอบว่าแป้นอาจผิด แต่ API จริงในโหมด Auto ตอบราคา PS5 ภาษาไทยได้ถูกทาง ตรวจโค้ดแล้วพบว่า server ส่ง surface_language ให้ resolve_locale ขณะที่ engine โดยตรงไม่ส่งขั้นตอนนี้ จึงเป็นความต่างของทางเข้า ไม่ใช่หลักฐานว่าเว็บยังตอบกรณีนี้ผิด เก็บ auto/th/en probe และตรวจซ้ำ Auto ทุก input ด้วยการเลือกภาษาแบบ server โดยคงคะแนนเดิมแยกไว้ ควรรวม adapter ของการทดสอบให้ตรงกับทางเข้าใช้งาน

คำถามราคาที่มีเกมอยู่หลายบริการ เช่น TEKKEN 8 สามารถถามเลือก PC/PS5 ได้อย่างปลอดภัย แต่ Gold บางรุ่นคาด answer_available จึงไม่ควรตีความทุก clarification ว่าตอบผิด ส่วนเกมที่มีบริการเดียวแต่ยังถามเลือกบริการโดยไม่เสนอข้อมูลที่รู้ เป็นจุดที่พัฒนาได้ ใช้ game→services แล้วให้ตัวเลือกเฉพาะและราคาแต่ละกลุ่ม

### P1: ข้อมูลเก่าและข้อกำหนดของเกณฑ์ตรวจ

`What games are available?` ได้รายชื่อ 42 เกม แต่เกณฑ์ต้องมีหัวข้อ `Verified game catalog` จึง fail: เป็น assertion รูปแบบเก่าที่ไม่พิสูจน์ว่ารายชื่อผิด ต้องตรวจชื่อเกม/จำนวน/โซนจาก catalog แทน และเก็บคะแนนเดิมไว้

กฎแข่งขัน expanded v2 มีข้อ allowed evidence IDs ไม่ตรงกับข้อย่อยที่ตอบ ตัวอย่างการใช้อุปกรณ์ส่วนตัว CS2 ตอบรายการอุปกรณ์จาก rulebook เดียวกัน ต้องเทียบเนื้อหาข้อจริงก่อนเปลี่ยน Gold หรือสรุปว่า retrieval ผิด การมี source ID อย่างเดียวก็ยังไม่พิสูจน์ว่าตอบเงื่อนไขครบ

Gold builder ไม่ตรงไฟล์ frozen 6 แถวอังกฤษ เพราะ metadata reference_answer เรื่องค่าเสียหายฉบับใหม่เพิ่มเงื่อนไข/จำนวนเงิน ไม่ได้เกิดจากแก้ Gold ในรอบนี้ เก็บ drift แยก ไม่เขียนทับไฟล์เพื่อให้ test ผ่าน

### P1: แยก schedule policy ออกจาก live booking

บางคำถาม เช่น “วันศุกร์ช่วงบ่ายจองได้หรือเป็นเวลาปิดดูแลเครื่อง” เข้า live path แล้วเมื่อ fixture ถูกกำหนด unavailable จึงแจ้งดึงสดไม่ได้ ทั้งที่สามารถตอบนโยบาย Maintenance ทั่วไปได้บางส่วน ควรตอบส่วนตารางที่ยืนยันได้พร้อมแยกว่ารอบจริงยังต้องดึงสด ไม่แปลง offline fixture เป็นหลักฐานว่าจองจริงผิด

### P2: คำถามที่กำกวมและประสบการณ์ใช้งาน

Call of Duty ไม่ระบุภาค: ระบบใหม่ถามชื่อ/ภาคเพื่อไม่เลือกบริการผิด เกณฑ์เก่าที่บังคับ reservation ไม่ผ่าน เป็นการเปลี่ยนผลตอบแบบปลอดภัยตาม Flow ปัจจุบัน พัฒนาเพิ่มได้ด้วยรายการภาคที่มีและบริการแต่ละภาค แทนการถามแบบไม่มีตัวเลือก

สิบคำถามพร้อมกันมี HTTP 503 ทั้งกรณีทดสอบร่วมกับการดึง WordPress และรอบ G2 smoke ขณะ full sweep ใช้เครื่องหนัก worker เดียวมี queue wait 3 วินาที จึงต้องแยกผล under-load จาก idle เมื่อรันแยกโดยไม่มีงาน API อื่น รุ่น r29 และ r30-F ผ่าน 10/10 ทั้งคู่ ไม่มีภาษาข้ามกัน ไม่สรุปว่า r30 ทำให้ concurrency เสีย การรองรับคิวช่วงที่มีคำถามช้าหลายคนยังเป็นงานเสริม: แสดงสถานะรอ/ลองใหม่และวัด SLA แยกจาก correctness ก่อนปรับ worker/RAM

### P2: ภาษาอังกฤษและแหล่งข้อมูลที่ยังขาด

ต้นฉบับ shadow 1,600 แถวไม่มี question_en; ใช้ชุดแปลเครื่อง 1,600 แถวที่มีอยู่ตรวจแยก ไม่เรียกว่าคนตรวจแล้ว ชื่อบุคลากรภาษาไทยจาก source อาจเป็นการรักษาชื่อจริง ไม่ใช่ภาษาอังกฤษรั่วทุกกรณี แยก proper name จาก Thai prose และขอชื่ออังกฤษทางการตามแบบฟอร์มเดิม

นโยบายวิดีโอ/ภาพ อายุ ค่าสมัคร controller รายละเอียดที่ไม่มี และ Tekken/RoV ที่ขัดแย้ง/ถูกตัด ต้องได้เอกสารเจ้าของ ไม่ใช้โมเดลแต่งเติม; real booking oracle ยังพักตามคำขอ

### P2: ตัวตรวจการพิมพ์และความครอบคลุมของการทดสอบ

Native detector benchmark ตรวจ calibration 100/test 400 พร้อม disclosure ว่าไม่ใช่ untouched holdout; runtime profile ตรวจ 500 เคสด้วย published corpus/fixed thresholds บล็อกตาม policy ถูก 498/500 อีก 2 เคส mixed game title ไม่จับ layout และตอบข้อมูลเกมแทนคำถาม availability ตัวเลขนี้ไม่ใช่ answer accuracy; continued inputs 262 เคสตรวจ validation แต่ยังไม่มี content oracle ครบ

ชุดที่ตรวจแค่ route/outcome/validation ยังมีช่องว่างเรื่องเนื้อหา ต้องเติม oracle เนื้อหาจาก source เป็นรายกลุ่ม มีเลข/เงื่อนไข/ข้อห้าม/source scope และตรวจ clean/noisy ด้วย oracle เดียวกัน คู่ 2,000 มีการ rescore V2/overlay โดยไม่แก้ชุด frozen; native detector 500 เคสใช้ training corpus/threshold ต่างจาก runtime ให้ดู final_G_guard500/summary.json แยกจาก final_G_runtime_guard500_summary.json

## ตัวอย่าง trace ที่ไม่ผ่าน — หมวดเหล่านี้เป็นการคัดแยกเพื่อทบทวน

### safe_abstention_vs_gold_or_missing_data_review

คำถาม: Mario Kart Live ปุ่มเร่งกดอะไร

คำตอบจริง: ตอนนี้ยังไม่พบ Mario Kart Live: Home Circuit ในรายการเกมปัจจุบันของ PSU Esports Studio - Phuket ครับ
จึงไม่ดึงปุ่มของเกมอื่น เช่น Mario Kart 8 Deluxe มาตอบแทน
เกมตระกูล Mario ที่อยู่ในรายการปัจจุบันคือ: Mario Kart 8 Deluxe, Mario Party Superstars, New Super Mario Bros. U Deluxe, Super Mario Odyssey
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: `pipeline:structured_game_controls_no_current_game`; route: `{"category": "games", "intent": "game_control_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "low", "reason": "exact game target locked: Mario Kart 8 Deluxe"}`; confidence: 0.93

ไม่ผ่าน: ["quality_score_or_required_gate_failed", "เร่ง"]

Trace เต็มและ expected contract: FINAL_G3_FAILURE_EXAMPLES.json; ข้อมูล raw แถว 8 ใน final_G3_all_results.jsonl

### metadata_or_mode_assertion_review

คำถาม: มี TEKKEN 8 ไหม

คำตอบจริง: ได้ครับ TEKKEN 8 เล่นได้ที่ PC Zone - PC #01-#02, PlayStation 5 Zone - PlayStation 5 #01-#02
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: `pipeline:structured_service_game_availability`; route: `{"category": "games", "intent": "game_detail_lookup", "confidence": 0.95, "answer_type": "fact", "risk": "low", "reason": "exact game target locked: TEKKEN 8"}`; confidence: 0.97

ไม่ผ่าน: ["intent:game_detail_lookup expected:game_availability_lookup"]

Trace เต็มและ expected contract: FINAL_G3_FAILURE_EXAMPLES.json; ข้อมูล raw แถว 10 ใน final_G3_all_results.jsonl

### route_content_or_source_selection_review

คำถาม: เอาอาหารเข้าได้ไหม

คำตอบจริง: นำอาหารหรือเครื่องดื่มเข้ามาได้ครับ แต่รับประทานหรือดื่มได้เฉพาะพื้นที่ที่ศูนย์กำหนด ไม่ใช่ทุกจุดในห้องเล่นเกม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Mode: `pipeline:protected_food_bring_permission`; route: `{"category": "rules", "intent": "food_bring_permission", "confidence": 0.98, "answer_type": "answer", "risk": "low", "reason": "requested answer facet protected from unrelated catalog and booking handlers"}`; confidence: 0.98

ไม่ผ่าน: ["quality_score_or_required_gate_failed", "พื้นที่ที่กำหนด"]

Trace เต็มและ expected contract: FINAL_G3_FAILURE_EXAMPLES.json; ข้อมูล raw แถว 18 ใน final_G3_all_results.jsonl

### allowed_evidence_ids_need_source_review

คำถาม: May players use their own equipment in Counter-Strike 2?

คำตอบจริง: Answer: Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Mode: `pipeline:competition_rule_detail_source`; route: `{"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}`; confidence: 0.97

ไม่ผ่าน: ["retrieval evidence did not match the allowed canonical fact/rule IDs"]

Trace เต็มและ expected contract: FINAL_G3_FAILURE_EXAMPLES.json; ข้อมูล raw แถว 1952 ใน final_G3_all_results.jsonl

### legacy_heading_assertion

คำถาม: What games are available?

คำตอบจริง: There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 games)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Mode: `pipeline:structured_games_catalog_en`; route: `{"category": "games", "intent": "games_lookup", "confidence": 0.98, "answer_type": "fact", "risk": "low", "reason": "shared game availability records rendered by English template"}`; confidence: 0.98

ไม่ผ่าน: ["missing required: Verified game catalog"]

Trace เต็มและ expected contract: FINAL_G3_FAILURE_EXAMPLES.json; ข้อมูล raw แถว 3771 ใน final_G3_all_results.jsonl

### controlled_live_dependency_unavailable

คำถาม: Which PC is available now?

คำตอบจริง: For 2026-10-02 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

Mode: `pipeline:live_booking_status_unavailable`; route: `{"category": "schedule", "intent": "live_booking_status", "confidence": 0.94, "answer_type": "no_answer", "risk": "medium", "reason": "aggregate-only live booking dashboard"}`; confidence: 0.94

ไม่ผ่าน: ["route:schedule expected:['no_answer']", "missing required: not connected"]

Trace เต็มและ expected contract: FINAL_G3_FAILURE_EXAMPLES.json; ข้อมูล raw แถว 3887 ใน final_G3_all_results.jsonl

### proper_names_or_language_leak_review

คำถาม: Who are the studio members?

คำตอบจริง: Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- ผศ.ดร.นิวัติ แก้วประดับ: University President (อธิการบดี) - Prince of Songkla University
- รศ.ดร.พันธ์ ทองชุมนุม: Vice President (รองอธิการบดี) - Prince of Songkla University, Phuket Campus
- รศ.ดร.อซีส นันทอมรพงศ์: Dean (คณบดี) - College of Computing, Prince of Songkla University, Phuket Campus
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: Assistant to the President for Academic Affairs (ผู้ช่วยอธิการบดีฝ่ายวิชาการ) - Prince of Songkla University, Phuket Campus
- นายพฤทธิ์ เกษตรสมบูรณ์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายณัฐวัฒน์ นิธิคุณานนต์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายชนะชัย สิริพันธ์วราภรณ์: Manager (ผู้จัดการ) - PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus
- นายณภัทร เชื้อเหล่าวานิช: Cooperative education student — Game and 3D Developer (นักศึกษาสหกิจ Game and 3D Developer) - College of Computing, Prince of Songkla University, Phuket Campus
- Mr. Amine Abidellaoui: Internship Student - High School Bristol Cannes, France
- นายสุพศิน อะนะฝรั่ง: Cooperative education student — Web & AI Developer (นักศึกษาสหกิจ Web & AI Developer) - College of Computing, Prince of Songkla University, Phuket Campus
- Mr. Yanis Igoudjil: Internship Student - Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France
- นายภาสวุฒิ ชูติประชากิจ: Super AI SS6 project intern — AI Chat Bot Developer (นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer) - IoT System and Information Engineering, King Mongkut's Institute of Technology Ladkrabang
- นายษุภากรณ์ จิราจินดากุล: Chairperson (ประธาน)
- นายนพัทธ์ ฝอยทอง: Vice Chairperson (รองประธาน)
- นายปัณณวิชญ์ หนูเรือง: Secretary (เลขานุการ)
- นายภูจิตร จิรวิริยาภรณ์: Treasurer (เหรัญญิก)
- นายธนชาติ เอ่งฉ้วน: Public relations officer (ประชาสัมพันธ์)
- นางสาวกมลวรรณ นวลสาย: Committee member (กรรมการ)
- นางสาวชญาภา จันทร์เอิบ: Committee member (กรรมการ)
- นางสาวณัฐธิดา คำทะเนตร์: Committee member (กรรมการ)
- นางสาวสุภาสินี ธนภพ: Committee member (กรรมการ)
- นางสาวอาทิตยา แดงประดับ: Committee member (กรรมการ)
- นายณัฐพนธ์ อินทรสังขนาวิน: Committee member (กรรมการ)
- นายอภิวิชญ์ เลิศกมลรักษ์: Committee member (กรรมการ)
- นายอรรถนนท์ สุขแก้ว: Committee member (กรรมการ)
Source: https://esports.phuket.psu.ac.th/about-us/Members (original source in Thai)

Mode: `pipeline:structured_members_source_th`; route: `{"category": "overview", "intent": "members_lookup", "confidence": 0.98, "answer_type": "fact", "risk": "low", "reason": "English member localization overlay matched current Thai source hashes"}`; confidence: 0.98

ไม่ผ่าน: ["missing required: English localization", "legacy_english_thai_prose_flag"]

Trace เต็มและ expected contract: FINAL_G3_FAILURE_EXAMPLES.json; ข้อมูล raw แถว 4012 ใน final_G3_all_results.jsonl

### deadline_or_loaded_machine_latency

คำถาม: ขอสอบถามหน่อยครับ ขอข้อมูลที่ยืนยันได้หน่อยครับ: ที่ศูนย์มี Minecraft ไหม

คำตอบจริง: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

Mode: `pipeline:no_answer`; route: `{"category": "games", "intent": "game_availability_lookup", "confidence": 0.95, "answer_type": "fact", "risk": "low", "reason": "game availability terms found before schedule"}`; confidence: 0.56

ไม่ผ่าน: ["latency_ceiling"]

Trace เต็มและ expected contract: FINAL_G3_FAILURE_EXAMPLES.json; ข้อมูล raw แถว 8679 ใน final_G3_all_results.jsonl

## วิธีอ่านคะแนนและเหตุผลเลือก

Trace แสดง input recovery, route candidates, top score/margin, target lock, hits, validation errors และ fallback ตามที่แต่ละเส้นทางบันทึก การผ่าน confidence threshold แปลว่าเลือก candidate ตามกติกาคะแนนได้ ไม่ใช่พิสูจน์ว่าคำตอบครบหรือ source ยังใช้งานจริง ทุกข้อไม่ผ่านเก็บ result เต็มใน FINAL_G3_FAILURE_INVENTORY.jsonl แล้วเชื่อมกลับ raw line ได้ หมวด triage อัตโนมัติเป็นเพียงคำใบ้ในการทบทวน ไม่ใช่ยืนยันสาเหตุเดียวให้ทุกข้อ

## สิ่งที่ยังไม่สรุป

ไม่มีการยืนยัน booked/free ของข้อมูลจริง ไม่มีการรับรองนโยบายจากเจ้าของใหม่ ไม่รวม historical versions/splits/aliases เป็นเปอร์เซ็นต์เดียว และไม่เรียก reference ที่ไม่มี content oracle ว่าคำตอบถูกแล้วทั้งหมด
