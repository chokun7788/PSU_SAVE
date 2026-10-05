# ผลและวิเคราะห์ PSU Esports Chatbot r31

วันที่ 2 ตุลาคม 2026 เวลาไทย — Revision C

เว็บหลัก: [เปิดแชท](http://127.0.0.1:8090/) | รุ่น `2026.10.02-question-target-content-r31`

Flowฉบับตรวจหลังลงมือ: [Flow r31](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/docs/131_question_target_content_r31_flow_20261002.md>)

## แก้แล้วและทำไมเดิมจึงผิด

### 1. ชื่อเกมผิดถูกแบ่งแก้ทีละส่วน

ชื่อเคาน์เตอร์สไตรก์ที่เบิ้ล/ขาดบางตำแหน่งผ่านgeneric normalizationก่อนระบุtarget จึงได้ชื่อครึ่งไทยครึ่งอังกฤษหรือไม่มีtargetแม้คล้ายชื่อsourceมาก ระบบเลยถามเกมใหม่ แก้ให้เทียบชื่อยาวทั้งspanจากregistryก่อนการแทนทั่วไป ใช้optimal string alignment รองรับinsert/delete/substitute/transposition จำกัดedit budget2เมื่อยาว≥10อักษร/1เมื่อสั้นกว่า และfraction≤0.18 ต้องไม่มีคู่แข่งต่างเกมใกล้กันเกินmargin0.08; ชื่อสั้น<6ตัวเลขและภาคไม่ทำfuzzy recovery ตัวเลขเหล่านี้คือกติกาเลือกcandidate ไม่ใช่เปอร์เซ็นต์คำตอบถูก

Traceเก็บinput_text/offset/original/canonical/registered_alias/edit count; ไม่เพิ่มwhole-questionalias การทดสอบชื่อถูกต้อง/หลายเกม/CS3/Tekken7/unsupported/no-ruleยังอยู่ครบ แต่targetถูกอาจยังตอบfacetผิด ดูข้อที่เหลือด้านล่าง

### 2. Freeze time ถูกเลือกเป็นคำถามเวลารอบ

คำถาม “CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง” เดิมเลือกround_timeจากคำว่าfreeze timeก่อนquotaของtimeout จึงตอบ1:55/15วินาทีซึ่งเป็นคนละข้อแม้sourceCS2ถูก ตอนนี้ timeoutเป็นpropositionหลักและFreeze timeเป็นlimiting condition; คำตอบsourceคือทีมละ4ครั้ง ครั้งละ30วินาที ใช้ในช่วงFreeze time การถามround timeแยกยังตอบข้อนั้นได้

### 3. Venueมีข้อมูลแต่รูปประโยคไม่เข้าgate

คำถาม “สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน” มีtargetแต่ไม่เข้าpatternเดิมจึงตอบยังไม่พบด้วยconfidence0.92 เพิ่มtarget-boundvenue/location/แข่งที่ใด; อ่านs08_c01เดิมที่ระบุ1วัน ณ PSU Esports Studio - Phuket ไม่เอาตำแหน่งปุ่มหรือเวลาหยุดเกมไปเป็นสถานที่ และปี2027ไม่เอากติกา2026ไปยืนยัน

### 4. ทดสอบผ่านแต่ยังตกคำถามที่ขอหลายเรื่อง

Aตอบเฉพาะtimeoutใน “pause และ timeout” เกณฑ์เดิมหลายแถวตรวจroute/outcomeแต่ไม่มีpositivecontent จึงยังผ่าน ขยายrequest contractให้ทั้งtechnicalและtacticalครบ: technicalทีมละ2ครั้ง ครั้งละไม่เกิน10นาที พบปัญหาต้องแจ้งกรรมการทันที; tacticalทีมละ4ครั้ง ครั้งละ30วินาทีในFreeze time เพิ่ม18เคสและmutationที่ลบquota/เวลา/เงื่อนไขแล้วต้องfail

### 5. ภาษาไทยไม่มีคำว่าrulesและgenericเวลานอกชนqualifier

Bคำถาม “CS2 เวลานอกทางเทคนิคขอได้กี่ครั้ง” ไม่ผ่านlooks_like_competition_rule_query แม้routerจัดcompetition_rules เพราะrule signalsมีEnglishtimeoutแต่ไม่มีThaiequivalentที่ผูกtarget แล้วfallbackเลือกfacetpause_timeoutรวมทั้งสองข้อ `retrieval.competition_fact_cards` score0.939สูงกว่าhybrid0.506; sourcegroundingผ่านเพราะgame/sectionถูก แต่ตอบtacticalก่อนtechnicalผิดประเด็น นี่เป็นตัวอย่างว่าscoreสูงไม่ได้รับรองครบ

CเปิดCS2rulegateจากtechnical/tacticalrequestและให้technicalqualifierระงับtacticalmatchเฉพาะวลีนั้น APIเคสเดียวกันเหลือtechnical2ครั้ง/10นาที/แจ้งกรรมการครบ ไม่มี4ครั้ง/30วินาที; Bใช้15.042วินาที Cเคสนี้0.268วินาที เป็นผลรายเคส ไม่ใช่latencyทุกคำถาม

## ผลทดสอบและขอบของหลักฐาน

| ชุด | ผล | ขอบ |
|---|---:|---|
| Fixtureใหม่20 | 6→20ผ่าน | ชื่อ6ข้อเป็นtarget/source checks; venue/timeoutตรวจข้อความsource |
| Compound/control18 | 18/18 | ทั้งสองกฎ/กฎเดียว/เงื่อนไขที่ไม่ควรปน |
| Unitสุดท้าย | 440/441 | 1preexistingEnglishGoldbuilder drift; errors/skips0 |
| APIรวมจากB+C | 941/941 | B941ครบ/C482replayed; อีก459retainจากB |
| Strongcompetition | 728/728 | sourceclauses/firstline/conditionsตามfixture; รวมอยู่ใน941 |
| หลังเปิด8090 | 46/46 | 20new+18compound+8locale |
| Livepath/guard | 44/44 | ทางดึง8/guard36; ไม่มีoracle occupancy |
| Idle10พร้อมกัน | 10/10 | locale+42games; ไม่ใช่SLAWordPress |
| Smoke85 | 71/85 | fail14เหมือนG6เดิม; ไม่อ้างทั้งหมดCfreeze |
| Baffectedsmoke16 | 11/16 | ไม่มีข้อผ่านเดิมตก |

Rootinputsครบ20,327/55,583grades จากAเต็ม (preserved18,894 + resumed1,433), Baffectedreplay4,370 และClocalreplay355 ตัวเลขinput/gradeเท่าเดิม ข้อมูลที่retainมีprovenance ไม่อ้างทุกรอบรันใหม่หมด ส่วนextra970inputs/981gradesมีobservations120ที่ยังไม่มีhumanoracle; Crun321affected/retain649

Rootมีอย่างน้อย1gradefailลด1,905→1,898 และnewfailedgrades0 แต่ไม่นับเป็นansweraccuracyเดียวเพราะเกณฑ์ต่างรุ่นและข้อมูลซ้ำ/historical/route-only การเปรียบเทียบV2ด้วยclassifierและoverlayเดียวกัน: clean1,772→1,772; noisy1,665→1,672; cleanผ่าน/noisyตก118→111 ไม่เอาG6เดิม1740/1640มาเทียบตรงกับCเพราะเพิ่มrecognizedmodeในgrader

111คู่ที่เหลือ: ไทย57 อังกฤษ54; มีpositivecontent43 ไม่มี68; ทั้ง2000คู่มีpositivecontent894. Triageเป็นคำใบ้ไม่ใช่ยืนยันสาเหตุเดียวทุกข้อ:

- route_mismatch: 91
- abstention_or_dependency_vs_expected: 8
- other_status_mismatch: 3
- content_contract_failure: 8
- clarification_vs_expected_answer: 1

## ข้อที่ยังผิด/ไม่ครบที่ยืนยันจากคำตอบได้ และลำดับต่อไป

1. **P0 live-intentหายเมื่อคำผิด**: “วางหรือเปล่า” ของNintendoพร้อมวันเวลาไปcalendarแทนlive การดึงข้อมูลที่ถูกต้องต้องมีfreshness gateตั้งแต่intentจนrender; รายงานofflineนี้ไม่พิสูจน์bookingจริง

2. **P1 targetถูกแต่propositionผิด**: “อารีน่สออฟเวเลอร์ ... จำนวผู้เล่นต่อทีม” ตอบห้ามชื่อตัวละครหยาบคายแทนcount (confidence0.84). SourceRoVs06_c01ระบุโหมดการแข่งขัน5v5ใน4.2.1; การตอบจำนวนผู้เล่นในเกมต้องอ้าง5v5และแยกจากสมาชิกลงทะเบียน/สำรองที่ไม่ควรเดา ต้องกู้facetพร้อมบริบทและใส่source-derivedcontentoracle

3. **P1 หลายข้อขาดบางข้อ/หัวข้ออย่างเดียว**: “คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน” ตอบเพียงlate-registration และ “การตั้งค่าในเกม” ได้แค่ชื่อหัวข้อ กู้ชื่อสำเร็จไม่ได้แก้สองอย่างนี้ อิสระrequestcontractในr31มี3กลุ่มCS2เท่านั้น งานต่อไปต้องทำrequested-ledgerให้ครบfacetsเหล่านี้พร้อมoverviewvsdetails/negativecontrols

4. **P1 real-word errorsและภาษาทั่วไป**: “Wherw can you pay VALORANT” ไปservice_feeจากpay; ห้ามแก้pay→playเสมอ ต้องใช้location/zonecontextหรือถามเมื่อกำกวม ส่วน“โซซนไหน”ทำPokémon Championsได้no_answerทั้งที่cleanมีSwitch ให้ทดสอบboundedfacetrecoveryพร้อมcontent

5. **P2 eval/source/English**: FrozenEnglishbuilder1unitfailยังอยู่; extrahistorical228ยัง0/228เพราะmodeเก่า เป็นต้น ห้ามเติมoracleด้วยคำตอบที่ระบบสร้างเอง คำแปลเครื่อง/shadow1600ไม่ใช่humanapproved ดูFlowคำถามเจ้าของเรื่องฉบับกฎและส่วนที่ขาด

6. **P2 queue503**: concurrentwebsmokefailภายใต้โหลดเดิม ส่วนidle10ผ่าน การแก้UIรอ/ retryและวัดslowupstreamก่อนเพิ่มworkerเป็นงานแยกจากsemanticcorrectness

## Extra corpus — rawและdiagnosticแยก

| Corpus | ผ่านเกณฑ์เดิม | ไม่บังคับmodeเก่าเพื่อวิเคราะห์ |
|---|---:|---:|
| ground_truth_competition_all_games_v2_diverse.jsonl | 98/184 | 98/184 |
| ground_truth_competition_rules_v1_228.jsonl | 0/228 | 66/228 |
| ground_truth_competition_challenger_v2_real_competitor_questions.jsonl | 194/369 | 194/369 |
| ground_truth_competition_challenger_v1_weird_user_questions.jsonl | 43/80 | 43/80 |

การตัดmodegateในcolumnขวาเป็นdiagnostic ไม่ใช่ผลผ่านใหม่หรือsemanticvalidation; rawยังอยู่ครบ ไม่มีnewfailedgradeจากextraC

## คะแนนที่เลือกคำตอบหมายถึงอะไร

Route confidenceเช่น0.97, retrieval0.84 หรือcandidate0.939เป็นscoreจากกฎ/หลักฐานที่matcherมองเห็น ไม่ใช่โอกาส99%ว่าประโยคถูกครบ เมื่อmatcherไม่เห็นfacetที่หายไปก็ไม่มีcandidateนั้นให้เทียบ Validatorจึงต้องเริ่มจากโจทย์และมีpositiveoracleสำหรับสิ่งที่ต้องปรากฏ เช่นจำนวนครั้ง+เวลา+เงื่อนไข ทั้งหมดต้องตรงsource ห้ามรับคำตอบเพราะsourceIDถูกอย่างเดียว

## การรักษางานเดิม

ตรวจhash584owner/data/Goldไม่เปลี่ยน Snapshot258ไม่เปลี่ยน Originaltestsไม่เปลี่ยน Runtimeappในprojectตรงแพ็กเกจCทุกไฟล์ Oldlogs/rawresults/แพ็กเกจA,Bยังอยู่ ไม่มีGitreset/stash/commitหรือการลบไฟล์ เก็บflow_initialก่อนแก้Flowฉบับสุดท้าย

## ไฟล์หลักฐาน

- [release_preflight_C.json](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/release_preflight_C.json>)
- [preservation_package_C.json](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/preservation_package_C.json>)
- [API_FINAL_B_C_SUMMARY.json](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/API_FINAL_B_C_SUMMARY.json>)
- [R31_C_FULL_ANALYSIS_SUMMARY.json](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/R31_C_FULL_ANALYSIS_SUMMARY.json>)
- [R31_COMMON_SCORING_COMPARISON.json](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/R31_COMMON_SCORING_COMPARISON.json>)
- [R31_C_FAILURE_INVENTORY.jsonl](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/R31_C_FAILURE_INVENTORY.jsonl>)
- [R31_REMAINING_PAIRED_DETAILS.jsonl](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/R31_REMAINING_PAIRED_DETAILS.jsonl>)
- [R31_C_CHANGED_ANSWERS.jsonl](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/R31_C_CHANGED_ANSWERS.jsonl>)
- [R31_C_EXTRA_CORPUS_ANALYSIS.json](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/R31_C_EXTRA_CORPUS_ANALYSIS.json>)
- [B_THAI_TECHNICAL_FAILURE.json](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/B_THAI_TECHNICAL_FAILURE.json>)
- [REMAINING_ROV_5V5_SOURCE.json](<C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/reports/r31_question_target_content_20261002_160701_ce8b6e/REMAINING_ROV_5V5_SOURCE.json>)

## สิ่งที่ไม่ได้รับรอง

ไม่ได้รับรองทุกประโยคพิมพ์ผิด ไม่ได้ยืนยันsourceconflictsจากเจ้าของใหม่ และไม่ได้พิสูจน์ว่าง/ถูกจองของข้อมูลจริง การพักเก็บbookingoracleของผู้ใช้ยังมีผล การผ่านWordPress/HTTPเป็นหลักฐานการเชื่อมต่อเท่านั้น
