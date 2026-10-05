# Flow r32 — แก้รายการที่เหลือทั้งหมด

## ขอบเขตและข้อจำกัดที่ยังมีผล

แก้รายการ1–9ที่มีหลักฐานในระบบและจัดการงานที่ต้องยืนยันอย่างเป็นรูปธรรม ข้อมูลเจ้าของ/Goldเดิม584ไฟล์รักษาhash เก็บsnapshotโค้ด/เครื่องมือ/tests/UIและGitก่อนแก้ เก็บผลแต่ละรอบแยก ไม่เปลี่ยนนโยบายเอง งานเก็บoracleการจองจริงข้อ10ยังพักตามผู้ใช้; เตรียมfixtureและวิธีตรวจที่ไม่ต้องเขียนการจองจริงไว้ให้ครบ

## รายการงานและผลที่ต้องส่ง

| ลำดับ | งาน | การลงมือ | หลักฐานตรวจ |
|---|---|---|---|
| 1 P0 | availability intentหาย | กู้คำกริยาด้วยอุปกรณ์/เวลา/รูปคำถาม และfreshness guardก่อนตอบ | คำปกติ/ผิด/เบิ้ล/ขาด TH/EN + schedule/วางอุปกรณ์negative |
| 2 P1 | เกมถูกหัวข้อผิด | กู้facet spanจากlexiconงานเดิมในบริบทcompetition; source clauseต้องตรงfacet | RoVplayercount/settingsและunsupported topicnegative |
| 3 P1 | หลายเรื่องตอบขาด | สร้างรายการrequestedpropositionsและsource requirementsร่วมกันกับrenderer/validatorแต่แยกการตรวจ | eligibility/roster/registrationและmutationลบข้อหนึ่ง |
| 4 P1 | มีแต่header | อ่านรายละเอียดข้อย่อยจริงตามsourceและแยกoverview/detail | setupค่าตั้งต้น + title-onlymutantsต้องfail |
| 5 P1 | play/payและคำทั่วไป | syntax/context-anchored recovery; ambiguityแยกจากราคา/การชำระจริง | locationvsprice/validwordnegative/Thaizoneเบิ้ลขาด |
| 6 P1 | oracleไม่ตรวจเนื้อหา | เพิ่มsource-derivedpositivecontractsเวอร์ชันใหม่ไม่แก้frozenGold | clean/noisyใช้oracleเดียวกัน; รายงานold/newscoringแยก |
| 7 P2 | Englishbuilderdrift/translation | เปรียบเทียบแถวต่าง/sourceและแก้ตัวสร้างให้reproduceชุดเวอร์ชันเดิม หรือแยกเวอร์ชันเมื่อsemanticต่าง | frozenhashไม่เปลี่ยน + originalunittest |
| 8 P2 | sourcegap/conflict/ปี | งานtechnicalให้source-awareabstentionและeditiondisclosure; ownerquestionsพร้อมfieldsหลักฐาน | ไม่มีsourceห้ามclaim; ambiguous/conflictnegative |
| 9 P2 | คิว503 | ตรวจqueue/deadlineจากfixture; เพิ่มboundedretry/Retry-Afterและข้อความรอTH/ENตามหลักฐาน ไม่เพิ่มworkerเดา | mockslowworker/upstream + idle/loadedAPIแยก |
| 10 พัก | realbookingoracle | ทำoracletemplate/runnerread-onlyพร้อมแยกtransportและoccupancycorrectness | knownfixtureผ่าน; templateจริงยังpendingไม่เรียกverified |

## รอบการทำและปรับFlow

1. Baselineเก็บraw/trace/contentsource → วิเคราะห์cause/score → เปลี่ยนเฉพาะจุด → unit/positive/negative/mutation tests
2. รวมแต่ละกลุ่มเข้าด้วยกันและตรวจผลถอย โดยsource/goldchecksเป็นoracleอิสระ ไม่ใช้คำตอบระบบสร้างคำตอบคาดหวัง
3. รันชุดใหญ่เดิม20327inputs/55583grades พร้อมpair2000/extra970/strong728 และAPIจริงตามส่วนที่แก้; ถ้าหยุดเก็บผลเดิมแล้วresumeเฉพาะขาด
4. แก้ข้อที่พบจากการรันตามหลักฐาน เก็บผลเดิม/affectedreplayและprovenanceทุกระยะ
5. ตรวจhash/preservation/package/runtime → เปิด8090รุ่นใหม่เฉพาะเว็บของงานนี้ → postrelease/content/guard/queuechecks
6. เขียนรายงานสาเหตุ/actual/expected/score/remaining แยกผ่านอัตโนมัติจากเจ้าของยังไม่ยืนยัน และปรับFlowฉบับสุดท้าย

## การตรวจแผนก่อนลงมือ

- availabilityต้องไม่เอาตารางเปิดบริการแทนoccupied/free และห้ามเปลี่ยนเลขเครื่อง/วันที่/เวลา
- realwordเช่นpay/riceเป็นคำจริง ต้องมีcontextขัดกันชัดหรือถาม; ไม่ทำglobalreplace
- sourcepolicy/ปี/ข้อความขัดกันไม่แก้ownerdataเพื่อให้testผ่าน
- บังคับrequestedclausesเฉพาะมีsourceตรวจได้; sourceขาด/qualifierไม่ตรงให้honestpartial/clarificationตามที่อธิบาย ไม่เลือกข้อข้างเคียง
- คิวretryต้องboundedและเฉพาะserverบอกretryable; ไม่ทำคำถามซ้ำไม่จำกัดหรือสร้างbooking
- ไม่เรียกทุกgradefailว่าsemanticผิด และไม่รวมhistorical/observationเป็นaccuracyเดียว

## ผลหลังลงมือ

เติมเมื่อมีผลจริง แต่ละข้อมีสถานะเสร็จ/ข้อจำกัด/sourceเจ้าของpending พร้อมการปรับFlowจากข้อที่พบ
