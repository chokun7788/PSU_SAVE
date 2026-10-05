# ผลพัฒนาและทดสอบ PSU Esports Chatbot — r30 G6

วันที่ 2 ตุลาคม 2026 รุ่นเว็บ `2026.10.02-full-improvement-r30-G6`

## ใช้งาน

[เปิดเว็บแชท](http://127.0.0.1:8090/) — รีเฟรชหน้าก่อนลองรุ่นใหม่ มีแพ็กเกจใหม่แยกโฟลเดอร์และเก็บรุ่นเดิมไว้

## สรุปงานที่ทำจริง

- ทำ Flow, ตรวจหลักฐาน/trace, แก้ production เป็นจุด, เพิ่ม content/negative tests และรันวงจรตรวจซ้ำหลายรอบ F/G2/G3/G4/G5/G6 ไม่มีการอ้างว่ารันใหญ่สิบรอบ
- ราคาแบบหลายระยะเวลา/หน่วยร่วม, คำปฏิเสธกลุ่มผู้ใช้, รายการแพ็กเกจ, ปุ่ม exact/typo/เลขที่ไม่มี, บริการเพื่อเล่นเกม, นโยบายที่ยังไม่มี source, ภาษาไทยปนชื่อเกมอังกฤษ และ ingress layout direction แก้ในรอบนี้
- กฎ CS2 เรื่อง player roles/roster/action/client/version/language, VALORANT display settings, RoV late-start/skins และ Tekken rounds/edition scope ใช้ literal clauses จาก source เดิม
- G4→G5 แก้ regression ที่ตรวจเจอจริง: คำถามสามหัวข้อ eligibility/roster/registration และ available for generic booking periods; G6 เพิ่ม CS2 duration/venue ข้อ s08_c01 พร้อม qualifier ว่าข้อมูลในเอกสารกติกาที่มี
- Guard composition ตรวจ accidental repeat ที่มีหลักฐานก่อนประเมิน layout รอบ exact source game title; ไม่ส่งข้อความที่แก้ไปตอบและไม่ปรับ global threshold ลงเพื่อให้คะแนนผ่าน
- ตาราง Maintenance ทั่วไปแยกจากสถานะ PC1/วัน/เวลาจริง และ WordPress ดึงแบบ read-only ต่อคำถามสด; ไม่สร้างการจอง

## การรักษาไฟล์และหลักฐาน

- ข้อมูล/booking ที่ติดตาม hash 584 ไฟล์คงเดิม; snapshot ต้นฉบับ 248 ไฟล์ตรวจตรง; original tests ไม่ถูกแก้; package app ตรงกับ project freeze
- ผลทดสอบและรายงานเปิดเป็นไฟล์ใหม่ ไม่ reset/stash Git ไม่แทน frozen Gold; Git status ก่อน/หลังและ snapshot ทุกระยะอยู่ในรายงานนี้
- ไม่มีนโยบายใหม่ที่เจ้าของรับรอง และยังพัก oracle booked/free จริงตามคำขอ

## ผลทดสอบสำคัญและขอบเขต

| ชุด | ผล | สิ่งที่พิสูจน์/ข้อจำกัด |
|---|---:|---|
| Static corpus ทั้งหมด | 20,327 requests / 55,583 grades | G6 รันใหม่ครบจริง ตรวจ key/provenance; grade มีเวอร์ชันเก่า/ซ้ำ จึงไม่รวมเป็น answer accuracy |
| Actual API 8091 | 903/903 | โปรไฟล์จริงเปิด LLM/semantic ตาม gates; content/source/negative/locale ตาม oracle แต่ละชุด |
| Strong competition contracts | 728/728 | composition280 + content320 + novel128; ไม่แทนผู้จัดยืนยันความมีผลของกฎ |
| Source/regression/guard fixtures ล่าสุด | 45/45 | รวม 6 ประโยค duration/venue ไทย/อังกฤษและ negative boundaries |
| Unit tests | 424/425 | 1 failure เดิม: frozen EN metadata 6 แถวไม่ตรง builder; ไม่มี error/skip |
| Smoke files ทุกไฟล์ | 71/85 | ทุก failure เก็บ log; ตารางแยกด้านล่าง |
| Session context | 24/24 turns | 12 sessions; controlled offline booking |
| Runtime guard actions | 500/500 | block/continue policy; source synthetic corpus ไม่ใช่ independent holdout |
| Runtime guard exact flags | 471/500 | layout TP240/FN0/FP0; repeat TP173/FN27/FP2; ไม่ใช่ answer accuracy |
| Post-release API 8090 | 53/53 | ตรวจหลังสลับรุ่นจริง |
| Live path + guard 8090 | 44/44 | transport/path และ guard; ไม่รับรอง booked/free oracle |
| Idle concurrent API | 10/10 | locale/count ของเกม; ไม่แทน SLA คำถาม WordPress ช้าพร้อมกัน |

## ผลครบราย corpus — เก็บคะแนนเดิม

| Corpus | ผ่านเกณฑ์เดิม/ตรวจ |
|---|---:|
| answer_quality_cases.jsonl | 22/26 |
| routing_eval_cases.jsonl | 30/40 |
| routing_eval_real_usage.jsonl | 88/115 |
| broad_usage_eval_v1.json | 636/651 |
| model_benchmark_1500.json | 1331/1600 |
| thai_multi_error_from_verified49_20260929.jsonl | 110/110 |
| thai_noisy_input_pairs_20260929.jsonl | 98/98 |
| user_question_bank_400.json | 399/400 |
| thai_multi_error_holdout25_20260929.jsonl | 49/50 |
| thai_noisy_input_holdout_20260929.jsonl | 50/50 |
| real_usage_golden_v1.jsonl | 23/24 |
| competition_composition_r28_280_20261001.json | 280/280 |
| competition_content_contract_r27_320_20261001.json | 320/320 |
| competition_new_questions_r27_128_20261001.json | 128/128 |
| competition_rules_rag_ground_truth_v1.jsonl | 548/548 |
| competition_user_r24_2000_20261001.jsonl | 2000/2000 |
| master_ground_truth_bilingual_10000_v1.jsonl | 9348/10000 |
| master_ground_truth_bilingual_10000_v2.jsonl | 9592/10000 |
| master_ground_truth_th_5000_v1.jsonl | 4614/5000 |
| master_ground_truth_th_5000_v2.jsonl | 4704/5000 |
| master_gt_bilingual_multi_error_2000_20260929_r15.jsonl | 3673/4000 |
| competition_rules_rag_ground_truth_v2_expanded.jsonl | 178/282 |
| english_gold_400_20260902.jsonl | 286/400 |
| rag_robustness_ground_truth_v1.jsonl | 481/600 |
| master_ground_truth_en_5000_v1.jsonl | 4734/5000 |
| master_ground_truth_en_5000_v2.jsonl | 4888/5000 |
| english_shadow_1600_machine_20260908.jsonl | 1229/1600 |
| review_grounded_novel_20260925.jsonl | 41/41 |
| english_shadow_1600_machine_sample_20260908_v4.jsonl | 6/6 |
| english_shadow_1600_machine_sample_20260908_v2.jsonl | 6/6 |
| english_shadow_1600_machine_sample_20260908_v3.jsonl | 3/3 |
| english_shadow_1600_machine_sample_20260908.jsonl | 5/5 |
| intent_trap_bilingual_1000_v1.jsonl | 881/1000 |
| intent_trap_bilingual_1000_v2.jsonl | 995/1000 |
| intent_trap_english_reference_200_20260926.jsonl | 200/200 |

English reference200 และ user bank400 บางแถวไม่มี oracle เนื้อหา; human_review120 เป็น observation ไม่ใช่คำตอบคนตรวจแล้ว ชุด shadow ว่าง1,600แถวมี machine counterpart แยก ไม่แปลจำนวนนี้เป็นคนรับรองอังกฤษครบ

### Extra competition corpus 970 requests / 981 grades

| ชุด | เกณฑ์เดิม | Diagnostic ไม่บังคับ mode เก่า |
|---|---:|---:|
| ground_truth_competition_all_games_v2_diverse.jsonl | 97/184 | 97/184 |
| ground_truth_competition_rules_v1_228.jsonl | 0/228 | 66/228 |
| ground_truth_competition_challenger_v2_real_competitor_questions.jsonl | 192/369 | 192/369 |
| ground_truth_competition_challenger_v1_weird_user_questions.jsonl | 42/80 | 42/80 |

Diagnostic ที่เอา mode gate ออกยังตรวจ keyword/source จึงยังไม่พิสูจน์ semantic correctness ห้ามลบ fail ทั้งหมวด; v1 ที่ได้ 0/228 มี mode เก่าทุกแถวและยังมี keyword/content ปัญหาด้วย

### Clean/noisy 2,000 คู่

- Legacy clean 1892/2000; noisy 1781/2000
- V2 content overlay clean 1740/2000; noisy 1640/2000; clean-pass/noisy-fail 117 คู่
- เก็บคู่/expected/คำตอบ/trace และผล V2 แยก ไม่แก้ frozen Gold เพื่อขึ้นคะแนน

## ทำไมยังมีข้อไม่ผ่าน — แยกชนิดก่อนแก้

ใน root มี 1,905 unique requests ที่ไม่ผ่านเกณฑ์อย่างน้อยหนึ่งชุด ตัวเลขนี้รวม latency, mode/heading/source-ID เก่า, safe clarification, controlled unavailable และคำตอบผิดจริง ไม่ใช่จำนวนคำตอบผิดที่คนตรวจแล้ว

| ประเภท | สาเหตุและวิธีอ่าน trace | คำตอบที่ควรเป็น/แนวทาง |
|---|---|---|
| จับประเด็นไม่ครบ/ผิดงาน | คำถามมีหลาย proposition แต่ matcher/coverage/operation รับรู้แค่บางเรื่อง หรือ fallback แซงงานเดิม | แยก ledger ต่อประเด็น ผูก target/condition/source และตรวจ missing/forbidden clauses ก่อนตอบ |
| ชื่อเป้าหมายถูกเพิ่ม/เลือกผิด | normalization/variant เพิ่มชื่อแล้ว resolver ให้ exact score กับข้อความที่ขั้นก่อนสร้าง; คะแนนไม่ได้ยืนยันว่าผู้ใช้เอ่ยชื่อนั้น | รักษา raw-span provenance; ชื่อที่อนุมานต้องมี margin/clarification; G5 แก้ CS2 event-version gate แต่กรณีทั่วไปต้องตรวจต่อ |
| Thai repeat/multi-error ไม่ครบ | char n-gram ของไทยหลายคำติดกันให้ candidate_seen=False; บางคำที่ลบซ้ำถูกมีคะแนนต่ำกว่า .55; profile quality อาจลดแม้ correction ถูก | ใช้บริบท/operation/target และ segmentation ที่มี negative controls; แยก notice detection จากความถูกต้องของคำตอบ ไม่ลด threshold รวมโดยไม่วัด false positive |
| Source ขาด/ขัด/ตัด | ไม่ใช่ retrieval ต้องเลือกหัวข้ออื่นมาทดแทน; Tekken pause conflict และ RoV 6.1.5.1 ตัดประโยค | partial/no-answer/conflict พร้อมขอข้อความเต็มและขอบเขตจากผู้จัด |
| Gold/keyword/mode เก่า | เช่น “3 รอบ” เทียบ literal “จำนวนรอบต่อเกม (Round): 3”, “Default Skin” เทียบ “สกิน Default”, mode เก่าหรือ heading เก่า | เก็บคะแนนเดิม เทียบ source รายข้อ แล้วทำ overlay ที่มี reviewer/hash/scope; ห้ามประกาศทั้งหมดถูกเพราะคำพ้อง |
| ภาษาอังกฤษ/ชื่อจริง | proper names ไทยจาก source, localization hash ขาด/เก่า, ตัว Gold เองเป็น machine draft | แยก proper name / Thai prose / missing source / translation gap และใช้ source-bound localization |
| Dependency/เวลารอ | static booking ถูกกำหนด unavailable; loaded concurrency มี 503; แยก queue/restart/timeout จาก WordPress fetch errors | fixtures พิสูจน์ occupancy computation; live trace พิสูจน์ fetch; idle/load และ error body ตรวจแยก |
| Grader/คำอธิบาย metadata | F mode-prefix list bug, G2 layout status grade, summary template หรือ raw_gold_repeat label ไม่ตรง scope | เก็บ raw + correction audit แยก; metadata ไม่ใช้แทน row-level proof |

### ตัวอย่างที่แก้ พร้อมคำตอบและเหตุผลเลือกเดิม

1. CS2 platform/modification: เดิม splitter ส่วนหลังหลุดเป็นกฎเสียงดัง ตอนนี้ต้องมี Steam/latest CS2 และห้าม modification ที่ไม่ได้รับอนุญาตในข้อเดียว ไม่สรุปว่าห้ามทุก modification
2. Closed registration vs roster count: เดิมจับ roster noun จึงตอบ 5 คน ตอนนี้ action หลังปิดรับต้องตอบไม่อนุญาตลงทะเบียนเพิ่ม; คำถามสามหัวข้อยังต้องมี count จึงเพิ่ม enumeration ที่ไม่ชน action
3. RoV skins: implicit permission ไม่เข้ากฎ ตอนนี้ตอบเฉพาะ Default จาก 4.2.5 พร้อม rulebook
4. Tekken rounds: ชื่อ franchise/จำนวนรอบหลุดเป็นหัวข้อกว้าง ตอนนี้บอกตามเอกสาร Tekken 8 ที่มี 3 รอบ; explicit Tekken7/VII/v7 ไม่เดาเป็น8
5. Protest language: route มีคะแนน .97 และรู้ CS2 แต่ concept จับลำดับคำเดียว; “บังคับ” ทำให้ fallback ไปปุ่ม ตอนนี้ใช้ข้อภาษาทางการ/การประท้วงภาษาไทย
6. CS2 duration/venue: เดิม source coverage ไม่เห็นประเด็น แม้ s08_c01 มีทั้ง 1 วันและ PSU Esports Studio - Phuket; เว็บบางประโยคตอบข่าววันจัดซึ่งยังขาดระยะเวลา G6 ใช้ literal source เดียวและ qualifier ว่าเอกสารกติกาที่มี
7. Mixed name/repeat/layout: เดิมชื่อเกมอังกฤษ + wss, บดบัง mapping gain; G5 ตรวจ candidate หลังลบ duplicate ที่มี corpus evidence แล้วประเมิน residual คะแนน .86768 ผ่าน conservative gate ส่วนประโยคอังกฤษปกติยังให้ผ่าน ไม่ใช้ candidate เป็นคำถามใหม่

### คะแนนหมายถึงอะไร

Resolver 1.0 หมายถึง exact match ของข้อความที่เข้าขั้นนั้น; route .97 และ capability .999 มาจาก prior/domain/operation/type/precondition ตามโค้ด จึงอาจสูงกับข้อความที่ normalize ผิดได้ Trace ต้องใช้คู่กับ raw spans, target margin, source clauses และ content ledger การมี source ID หรือ confidence สูงไม่รับรองคำตอบครบ
ตัวอย่างข้อบังคับเนื้อหา: ถาม eligibility + roster + registration ต้องมีสิทธิ์สมัคร + 5 players + ห้ามลงทะเบียนหลังปิดรับครบทั้งสาม; ถามแค่หลังปิดรับเพิ่มเพื่อนได้ไหมต้องไม่ใช้ count มาแทน action

## งานที่ควรทำต่อ เรียงตามผลกระทบ

1. P1 — ขยาย proposition ledger/validator ให้เส้นทางทั่วไปและ typo ใช้ได้: แยก action/condition/negation/quantity/time/target และตรวจ content มากกว่า route หรือ keyword เดี่ยว เริ่มจากคู่ clean/noisy ที่เกิด regression และแถวที่ trace ยืนยันผิดงาน
2. P1 — สร้าง oracle overlay จาก source รายข้อและรักษา Gold เดิม: heading/mode/source-ID เก่าที่ผิดต้องทบทวนก่อนใช้คะแนนตัดสินการแก้ ไม่ลบ fail ทั้งหมวด คำตอบ partial/clarification ต้องมี expected ที่แยกจาก available
3. P1 — ขอข้อความ source ที่ขาดและความมีผลของแต่ละ rulebook: ใช้คำถามเฉพาะด้านล่าง; สิ่งที่คนยังไม่ยืนยันต้องไม่ใส่เป็น fact ใหม่
4. P2 — วิเคราะห์ repeat flag 27 FN/2 FP และ noisy content failures: segmentation/context ร่วมกับ bounded edits/keyboard evidence; ยืนยันกับ untouched held-out cases ก่อนปรับเกณฑ์ รวม true English, legitimate doubled letters, Roman edition, เลขเครื่อง/เวลา/คำปฏิเสธ
5. P2 — คิวภายใต้โหลด: วัด mixed fast/slow requests พร้อม error body/queue timing/cold vs warm; ออกแบบข้อความรอและ retry policy ตาม SLA ก่อนเพิ่ม workers/RAM ผล idle catalog10คำถามยังไม่แทนคำถาม WordPressช้าสิบคน
6. P2 — Platform ambiguity/หลายบริการ/ปฏิเสธหลายกลุ่ม: ขอบราคาและปุ่มยังต้องมี typed clarification และ tests ของ proposition ร่วม ไม่เดา platform หรือ affiliation ที่ขาด
7. พัก — เก็บ booked/free oracle จริงและ authentic unseen queries ตามคำขอผู้ใช้; ตอนนี้ทำ fixture/transport/source audits ต่อได้

## คำถามที่ต้องให้เจ้าของ/ผู้จัดตอบโดยตรง

- Tekken pause: ข้อห้ามหยุดกับข้อที่ทุกคนยินยอมใช้ร่วมกันอย่างไร กรณีไหนเป็นข้อยกเว้น โทษนับ round/game/match ใด?
- RoV 6.1.5.1: ขอประโยคเต็มหลัง “ออกจาก” พร้อมหัวข้อ/เวอร์ชัน/วันที่ของเอกสาร?
- Rulebook CS2/RoV/Tekken8/VALORANT: ใช้กับรายการชื่ออะไร ปี/รุ่นใด วันที่มีผลใด และเป็นกฎสำหรับรายการปัจจุบันหรือเอกสารเก็บย้อนหลัง?
- ถ่ายภาพ/วิดีโอ: อนุญาตหรือไม่ ต้องขอใคร/ความยินยอมใคร จำกัดพื้นที่ใด? ค่าสมัคร/อายุขั้นต่ำแต่ละรายการระบุเท่าไรและข้อยกเว้นใด?
- อุปกรณ์ controller รุ่น/จำนวนที่ศูนย์ใช้จริง และชื่ออังกฤษทางการของบุคลากรที่มีเฉพาะชื่อไทย?
- ยังไม่ขอให้เก็บ oracle จองจริงตอนนี้ เนื่องจากผู้ใช้ให้พักไว้

## รายงานและหลักฐานที่เปิดตรวจได้

- Flow: `docs/130_full_improvement_r30_flow_20261002.md`
- ทุกข้อไม่ผ่าน: `FINAL_G6_FAILURE_INVENTORY.jsonl` พร้อม raw row/expected/answer/trace; ตัวอย่างรายหมวด `FINAL_G6_FAILURE_EXAMPLES.json`
- วิเคราะห์ครบ corpus/paired/English: `FINAL_G6_DETAILED_CAUSE_ANALYSIS_TH.md`, `FINAL_G6_FULL_ANALYSIS_SUMMARY.json`, `FINAL_G6_PAIRED_TYPO_V2.jsonl`, `FINAL_G6_ENGLISH_REFERENCE_COMPARISONS.json`
- Root raw/coverage: `final_G6_all_results.jsonl`, `final_G6_all_summary.json`, `final_G6_verified_coverage.json`; scope template เก่าให้ใช้อธิบายจาก verified coverage แทน ไม่เปลี่ยน raw
- Extra: `FINAL_G6_EXTRA_CORPUS_RESULTS.jsonl`, `FINAL_G6_EXTRA_CORPUS_ANALYSIS.json`; human_review120 ต้องคนตรวจเพิ่ม
- Guard flags: `final_G5_runtime_guard500_interpretation.json`; guard code byte-identical G6/G5b และมี API guard rechecks
- Source before/after: `baseline_G3_source_source_G4_results.jsonl`, `PRODUCTION_EVENT_DETAILS_PROBE_G5.json`, `final_G6_source_G6_results.jsonl` และ actual HTTP903 rows
- Release: `release_preflight_G6.json`, post-release/API/live/concurrency logs, Git status และ snapshots

## Smoke failures — ไม่เรียกว่าผ่านทั้งหมด

| ไฟล์ | การตีความ |
|---|---|
| smoke_test_answer_pipeline.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_availability_policy_regressions.py | Call of Duty family clarification ปลอดภัยต่างจาก expectation เก่าที่ต้อง reservation; เก็บ fail เดิม |
| smoke_test_bilingual_web_api.py | loaded 10-concurrent HTTP503; idle resultแยก ดู error body/queue timing ไม่เหมารวมเป็น WordPress |
| smoke_test_bilingual_pipeline.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_boundary_guard.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_correctness_control_flow_v1.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_english_draft_preview.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_english_format_parity_fixes.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_game_catalog.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_genre_alias_formatting.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_llm_health_circuit_breaker.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_pipeline_fixes_20260823.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_real_usage_golden.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |
| smoke_test_update.py | ล้มซ้ำใน baseline r29/F ตาม log replay; บางข้อเป็น old heading/mode/control assumptions ต้องดูแถวจริง ไม่รับรองว่า content ทุกข้อถูก |

## การดึง WordPress สดหลังอัปเดต

ดึงสดสำเร็จ 8/8 ครั้ง; metadata source=remote_csv_live, transport=wordpress, cached=false, error_code ว่าง ใช้เวลาดึง 0.81–2.31 วินาที เป็นเวลาของการดึงข้อมูล ไม่ใช่ input-to-output SLA และไม่ใช่หลักฐาน booked/free ตรงจริง ดู http8090_G6_live_transport_audit.json

Smoke รายไฟล์มี error excerpts และข้อจำกัดแยกใน FINAL_G6_SMOKE_FAILURE_REVIEW_TH.md / JSON; ไม่ถือว่าคำถามหลัง assertion แรกที่หยุดนั้นได้ตรวจผ่านแล้ว

## ข้อผิดจริงที่ยังเปิดหลัง G6 — เริ่มแก้รอบถัดไป

- `สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน`: concept ยังไม่รู้จัก สถานที่จัด ก่อนชื่อรายการ จึงปฏิเสธ ทั้งที่เอกสารระบุ PSU Esports Studio - Phuket ม.อ. ภูเก็ต G6 รองรับบางสำนวน duration/venue แล้ว แต่ยังไม่ครบสำนวนนี้
- `CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง`: รู้จัก round_time เพราะ freeze time แต่ไม่รู้จัก bare timeout จึงตอบ 1:55/15 วินาทีแทนการขอเวลานอก ควรตอบทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ใน Freeze time ตาม source เดิม
- หลักฐาน source hash/trace/expected และ Flow แก้เฉพาะ proposition พร้อม negative controls อยู่ใน `CONFIRMED_REMAINING_G6_CASES.json` และ `REMAINING_G6_PRIORITY_AND_FLOW_TH.md` ข้อเหล่านี้เป็น P1 ที่ทำต่อได้โดยไม่ต้องขอเจ้าของเดานโยบาย

ไม่ใช้จำนวนข้อทดสอบที่ผ่าน route-only, observation, API transport หรือ guard policy มารับรองความถูกต้องของคำตอบทุกประโยคหรือ booked/free จริง

## เปิดรุ่นนี้อีกครั้งหลังปิดเครื่อง

เปิด `Open-PSU-Esports-Chatbot.cmd` ในแพ็กเกจ `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261002_full_improvement_r30_G6\PSU_Esports_Chatbot_Local` รุ่นก่อนและ logs ยังคงอยู่
