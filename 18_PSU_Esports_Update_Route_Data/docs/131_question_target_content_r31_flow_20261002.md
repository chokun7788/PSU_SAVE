# Flow r31 ฉบับตรวจหลังลงมือ — เป้าหมายเกม สิ่งที่ถาม และข้อ source

ปรับ 3 ระยะ A → B → C จากผลจริง วันที่ 2 ตุลาคม 2026 เวลาไทย รุ่นเว็บ `2026.10.02-question-target-content-r31` แพ็กเกจ C

## 1. ขอบเขตที่ทำสำเร็จในรอบนี้

กู้ชื่อเกมยาวที่พิมพ์ผิดในบริบทกฎ แยกสถานที่/ระยะเวลารายการ CS2 กับคำถามตำแหน่งปุ่ม และแยก tactical timeout/technical pause/เงื่อนไข Freeze time ทั้งไทยและอังกฤษ ข้อมูลมาจากเอกสารที่มีอยู่ ไม่สร้างนโยบายใหม่

ตัวตรวจสิ่งที่ถามกับข้อ source อิสระมี **3 กลุ่มของ CS2**: technical pause, tactical timeout และ venue/duration ยังไม่ได้ครอบคลุมทุก proposition ทุกเกม คำว่า “source ถูก” หรือ “confidence สูง” ไม่รับรองว่าตอบครบทั้งคำถาม

## 2. Flow ที่ลงมือแล้ว

1. เก็บ Git status, snapshot app/tests 258 ไฟล์ และตรวจ hash ข้อมูลเจ้าของ/Gold 584 ไฟล์ ก่อนแก้ → ผ่านตรวจหลังทำ ไม่มี original test หรือข้อมูลเจ้าของเปลี่ยน
2. สร้างข้อทดสอบจาก source พร้อม raw answer/trace และ baseline → fixture20 เดิมผ่าน6 จากนั้น A19 และปรับก่อน full sweepเป็น20; แต่6เคสชื่อเกมตรวจ target/source ไม่รับรองเนื้อหาทุกหัวข้อ
3. กู้ชื่อเกมทั้งช่วงก่อน generic normalization → bounded optimal string alignment edit distance รองรับเพิ่ม/ขาด/สลับ/ผิด, แยก script/ขอบคำ/เลขภาค/รุ่น, รับเฉพาะชื่อยาวที่เลือกได้ชัด และเก็บ original span/alias/edits ใน trace ไม่แก้ CS3 ให้เป็น CS2
4. อ่าน proposition ที่ถามโดยผูกกับเกม → Freeze time ที่ต่อหลัง timeout เป็นเงื่อนไขของ timeout; การถาม round time แยกยังคงตอบ; technical qualifier ไม่กลายเป็น tactical quota
5. อ่านข้อ source และ English localization ที่ hashตรง → ตอบข้อเต็มพร้อมจำนวนครั้ง เวลา และเงื่อนไข ปีรายการไม่ตรงต้องไม่เอารายการ2026ไปยืนยัน2027
6. Validator เทียบข้อที่ถามจากโจทย์กับ source/คำตอบ → ตัด quota/time/condition ออกในการทดสอบแล้วต้องไม่ผ่าน; correct source ID อย่างเดียวไม่พอ
7. รัน full sweep A 20,327 inputs /55,583 grades → processหยุดหลัง18,894; รักษาไฟล์เดิมและรันเฉพาะ1,433ที่เหลือ ไม่อ้างผลที่ยังไม่ครบ
8. ทบทวนผล/คำตอบจริง → พบคำถาม “pause และ timeout” ตก pause แม้ old gateผ่าน จึงเพิ่ม contractทั้งสองเรื่องและ18เคสพร้อม negative controlsใน B
9. ทบทวน API B → พบภาษาไทย “เวลานอกทางเทคนิค” ยังเข้าหัวข้อรวม เพราะ rule gateไม่รู้วลีไทยและ tactical matcherจับคำว่าเวลานอกซ้ำ จึงแก้ gateที่ผูกCS2และ suppress tactical matchเฉพาะ technical qualifierใน C
10. ตรวจคะแนนคู่ clean/noisy → เพิ่มการจำแนก mode `competition_rule_detail_source` เป็น answer โดยยังตรวจ no_answer/clarificationก่อน และยังต้องตรวจ contentต่างหาก เทียบ G6/Cด้วย classifierและoverlayเดียวกัน ไม่เอาคะแนนที่เพิ่มเพราะ grader มาอ้างว่าโมเดลดีขึ้น
11. รัน unit441, full/extra affected replay, API gates, preservation/package hashes → สร้างแพ็กเกจ C เปิด8090 แล้วตรวจ post-release46, live-path/guard44 และ idle concurrent10; ปิดเฉพาะเว็บทดสอบ8091โดยเก็บlog
12. เก็บ failure inventory/paired remainingพร้อม trace/expected/คำตอบclean/noisy; แยกข้อผิดจริง ข้อคาดหวังเก่า source gap และ live dependency

## 3. หลักฐานและ gate สุดท้าย

| ชุด | ผล | การตีความ |
|---|---:|---|
| Fixtureเฉพาะจุด | 20/20 จาก6/20 | venue/timeout และtarget checksตามชนิดเคส |
| Compound + technical/tactical controls | 18/18 | ข้อ sourceเต็มทั้งไทย/อังกฤษ และเรื่องที่ไม่ถามต้องไม่ปน |
| Unitล่าสุด | 440/441 | เหลือGold English builder driftเดิม1ข้อ ไม่แก้frozenGoldให้เขียว |
| APIรวม | 941/941 | B941ครบ → Cรันซ้ำ482ที่ได้รับผล และเก็บB459ที่ไม่เปลี่ยน; ไม่ใช่Cรัน941ใหม่ |
| Strong competition clauses | 728/728 | รวม composition280/content320/new128 ใน APIรวม; ไม่ใช่เจ้าของรับรอง |
| หลังเปิดเว็บหลัก | 46/46 | 20new +18compound +8locale |
| Live-path/guard | 44/44 | live8เป็นทางดึงข้อมูล; guard36เป็นการบล็อก; ไม่มี occupancy oracle |
| 10พร้อมกัน รอบidle | 10/10 | locale/catalog count oracle; ไม่ใช่SLAของWordPressช้า |

Full Aครบ20327; Bรันซ้ำ4370กลุ่มcompetition/CS2/pause; Cรันซ้ำ355กลุ่มpause/timeout ข้อมูล inputและgradeยังครบเดิม ไม่อ้างว่าทุกรอบรัน20327ใหม่ ชุดเสริม A970inputs/981grades → Cรันซ้ำ321ที่เกี่ยวข้องและเก็บ649เดิม

เกณฑ์ rootเดิมมี inputsที่อย่างน้อย1gradeไม่ผ่านลด1905 →1898; newly failed grades=0 จำนวนนี้ไม่ได้แปลว่าคำตอบผิดจริง1898ข้อ เพราะมี historical/metadata/weak/no-content oracle

เมื่อใช้ **เกณฑ์เดียวกันทั้ง G6/C** คู่2000: clean1772ทั้งคู่, noisy1665 →1672, cleanผ่าน/noisyตก118 →111 (ไทย57/อังกฤษ54); ดีขึ้น7 ไม่มีคู่ผ่านเดิมตกใหม่ ใน111มีpositive content contract43 และไม่มี68 จึงไม่เรียก111คำตอบผิดเชิงเนื้อหาทั้งหมด

Smoke85ชุดแรกผ่าน71/85 ข้อที่failเหมือนG6เดิม; Bตรวจ16competitionที่เกี่ยวข้องผ่าน11/16โดยไม่มีข้อผ่านเดิมตก ทั้งชุดแรกและBมีขอบการเปลี่ยนไฟล์ระหว่างช่วงเวลา จึงอ้างfreeze Cได้จากunit/API/content gatesล่าสุด ไม่อ้างว่า85smokeรันบนCทั้งหมด

## 4. สิ่งที่ยังต้องแก้ — Flow ลำดับถัดไป

### P0 — ความหมายเรื่องสถานะสดต้องไม่หลุดไปตารางบริการ

ตัวอย่างจริง “พรุ่งนี้13:00 Nintendo Switch ... วางหรือเปล่า” หลุดจากliveไปcalendar ในcontrolled-offlineคู่ทดสอบ → เก็บคู่เป็นfixture, ตรวจavailable-intentจากบริบทอุปกรณ์+วันเวลา+คำกริยา, ตรวจfreshness requirementอีกชั้นก่อนrender ห้ามใช้ตารางเปิดบริการรับรองว่าง/ถูกจอง ควรเข้าlive fetchหรือบอกว่ายืนยันสดไม่ได้ การตรวจเลขเวลา/เครื่องต้องไม่แก้เอง Real occupancy oracleยังพักตามผู้ใช้

### P1 — ชื่อถูกแต่หัวข้อ/หลายข้อยังไม่ครบ

ตัวอย่าง “อารีน่สออฟเวเลอร์ ... จำนวผู้เล่นต่อทีม” รู้RoVแล้วแต่ตอบข้อชื่อตัวละคร; “การตั้งค่าในเกม” ตอบแค่หัวข้อ; “คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน” ตอบเพียง late-registration → เพิ่ม source-derived positive oracleของแต่ละหัวข้อและรายข้อที่ผู้ใช้ขอ; กู้ facet spanด้วยขอบ/บริบท; แยก overview/ค่ารายละเอียด; ไม่ให้ headerหรือข้อข้างเคียงผ่านเพราะsourcegameตรง; หากเจาะข้อไม่ได้ให้ถามตรงประเด็น การกู้ชื่อ7ข้อที่ผ่านV2ยังไม่รับรองsemantic answerทั้งหมด

### P1 — คำผิดที่เป็นอีกคำจริง/คำถามทั่วไป

ตัวอย่าง “Where can you play...” → “Wherw can you pay...” ไปตอบราคา; Pokémon ... “โซซนไหน” ไปno_answer → ใช้บริบทquestionframeและservice/game entitiesแยก play/pay; ambiguityต้องถามเมื่อหลักฐานไม่พอ, ไม่บังคับแก้payเป็นplayหรือriceเป็นPriceเสมอ เติม real-word errorsและThai deletion/repeat fixturesพร้อม content oracleเดียวกับclean

### P2 — Evaluation และแหล่งข้อมูล

อย่าแก้frozen Gold/old logs: เพิ่มเวอร์ชันoracleแยกและบันทึกreview reason Mode/source keywordไม่ใช่semantic correctness; English shadow1600ที่ไม่มีคำแปลมนุษย์ไม่เรียกapproved เก็บsource gaps/conflictsและรายการถามเจ้าของชัดเจน

### P2 — Queue/503 เมื่อเครื่องหรือ upstreamช้า

Smoke10พร้อมกันยังมี503ขณะรันงานอื่น ส่วนidleผ่าน10/10 → เก็บHTTP body/queuewait/deadlineและแยกsource latency; วัดสถานการณ์หลายคำถามWordPressช้าก่อนปรับworker/RAM แสดงสถานะรอ/ลองใหม่เป็นงานเสริม ไม่ลดcorrectness gate

## 5. คำถามที่ต้องให้เจ้าของตัดสินใจ

1. ให้ใช้CS2/VALORANT2026, RoV Blueket2025ประเภททีมชาย และTekkenฉบับที่มีเป็นกติกาปัจจุบันของรายการใดบ้าง? แต่ละฉบับยังมีผลถึงวันใด และมีฉบับใหม่หรือไม่?
2. Tekken การpauseมีข้อยกเว้นใด และโทษกรณีpauseแต่ละกรณีให้ใช้ข้อความจากแหล่งใดเมื่อเอกสารขัดกัน?
3. RoVข้อ6.1.5.1ที่ถูกตัด ข้อความเต็มคืออะไรและเอกสารฉบับใดเป็นauthoritative?
4. มีนโยบายภาพ/วิดีโอ อายุผู้สมัคร ค่าสมัคร และcontrollerที่ต้องตอบหรือไม่? ขอข้อความ/แหล่งต้นฉบับ ไม่ให้ระบบสร้างเอง
5. เมื่อกลับมาทดสอบจองจริง ให้ส่งสถานะที่เจ้าของรู้แน่ของเครื่อง+วันที่+ช่วงเวลา และเวลาที่ตรวจ เพื่อเทียบว่าง/ถูกจอง การเข้าถึงWordPressสำเร็จอย่างเดียวไม่พอ

## 6. เกณฑ์สำหรับรอบต่อไป

สร้างsource oracle → เก็บbaseline/trace → แก้เฉพาะlogicมีหลักฐาน → positive/negative/mutation tests → clean/noisyเดียวกัน → root/APIaffected replay → เปรียบเทียบเนื้อหาผ่านเดิมตกใหม่ → แพ็กเกจ/hash → ผลหลังเปิดเว็บ และปรับFlowจากความผิดจริง ไม่เพิ่มaliasทุกประโยคหรือเปลี่ยนนโยบายโดยเดา
