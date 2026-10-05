# Flow r30 — วิเคราะห์ ปรับแก้ และทดสอบชุดทั้งหมด

## จุดตั้งต้นและลำดับความสำคัญ

1. P1 ราคาแบบหลายระยะเวลา: parserใช้durationเดียวทำให้ตัวเลือกที่เหลือหาย. เพิ่ม typed alternatives, ไม่เปลี่ยนราคา/สิทธิ์/VRbooking roundingpolicy.
2. P1 ปุ่มที่ถามเฉพาะ: lexicaldescriptionชนกับชื่อปุ่มหรือgame title; ให้ explicitbutton targetชนะและตรวจสิ่งที่ไม่ควรปน พร้อมsecondary-source note.
3. P1 จองเพื่อเล่นเกม: แยกบริการที่ต้องเลือกจากขั้นตอนจอง ใช้game→serviceจากcatalogเดิม; ไม่ส่งคำสั่งจอง/สร้างbooking.
4. P2 source gapกับmissingtranslation: route/rendererต้องไม่บอกว่าไม่มีคำแปลเมื่อจริงๆไม่มีpolicy. แสดงnoAnswerพร้อมคำถามเจ้าของที่ตรง ไม่เดาอนุญาต/ห้าม.
5. P1 evaluation: ต้องตรวจcontentครบ/ห้ามผิดเรื่อง/เลข/กลุ่ม/เงื่อนไข/แหล่งข้อมูล ไม่ถือrouteผ่านเป็นคำตอบถูก. เกณฑ์เก่าที่ขัดกับsourceแยกเป็นgraderissue ไม่แก้Goldต้นฉบับให้ผ่าน.
6. P2 failuretaxonomy/trace: inputguard→recovery→entity/intent→selectionscore→retrieval→render→validation→API. ทุกfailureต้องมีคำถาม/คำตอบจริง/expectedsource/เหตุผลที่เลือก/การแก้.

## ขั้นตอนทำงาน

1. สำรองapp/testsเดิมและhashruntime/eval/ownerdata; เก็บGitstatus. Inventorydatasetsและtestscriptsทั้งหมดก่อนเริ่ม.
2. ตรวจFlowหาจุดเสี่ยง: ตัวเลขช่วงเวลาvsduration, alternativesvscomparisons, negatedgroups, ปุ่มที่มีหลายชื่อ, gamefamilyambiguous, sourcegapvslocalization, ownerapproval.
3. สร้างsource-backed fixturesใหม่TH/ENพร้อมclean/noisy/negativecontrols. ทดสอบbaselineก่อนแก้และเก็บtrace. Expectationsต้องมาจากdata/confirmedpolicy ไม่ใช่คำตอบruntime.
4. แก้เฉพาะหลักฐานชัดทีละส่วน; retestและตรวจFlowหลังพบปัญหา. ไม่เพิ่มaliasทั้งประโยคเพื่อไล่จำชุดทดสอบ.
5. รันtest_*.pyทุกmodule, smoke_test_*.pyแยกprocessพร้อมtimeout/outputใหม่. Testที่ต้องบริการภายนอก/เขียนข้อมูลจริงใช้safe fixtureหรือระบุblockedพร้อมเหตุผล.
6. รันcorporaทั้งหมดที่มีquestion/expectation; JSON/JSONLซ้ำกันหรือTH/ENsplitsที่ตรงกับbilingualparentบันทึกaliascoverage. Historicalversionsยังgradeตามcontractของแต่ละรุ่น; ไม่รวมผ่านทับกัน. Guard-only/route-only/answer/contentreviewต้องแยก.
7. Bookingcorrectnessใช้knownfixtureพร้อมtestclockอย่างชัดเจน; real APIตรวจpath/transportเท่านั้นเพราะuserพักrealoracle. เก็บsource-conflicts/missing-owner-policyเป็นpendingไม่guess.
8. วิเคราะห์ทุกfailureแยกconfirmeddefect, unsupported/missingdata, staleGold/weakgrader, environment/dependency, timeout และambiguousinput. จัดอันดับตามseverity/count/blastradiusและลิสต์วิธีแก้.
9. แก้confirmeddefectsที่ทำได้จากข้อมูลในรอบนี้ แล้วรันrelevantcases+finalfullsweepหลังfreeze; optionaltestไม่วนซ้ำเมื่อไม่มีriskใหม่.
10. Buildpackageใหม่ → actualHTTPregressionไทย/อังกฤษ+newfixtures → hashprotection → เปลี่ยน8090เฉพาะownedlauncher → smoke → รายงานผลและข้อจำกัด. เก็บแพ็กเกจ/logsเก่า.

## เกณฑ์รับผลและสิ่งที่ห้ามสรุปเกินหลักฐาน

ต้องมีinventoryระบุทุกdataset/scriptว่ารัน/alias/notexecutable/blockedเพราะอะไร. ต้องแยกunit,smoke,guard,legacyGT,strongcontentcontracts,liveHTTPและhuman/ownerapproval. Synthetic/translatedGoldไม่ใช่เจ้าของรับรอง. หากมีfailureต้องรายงานจำนวน/หมวด/ตัวอย่าง/trace/expectedfact ไม่แปลงเป็นpassโดยแก้ต้นฉบับ. 8090เปลี่ยนได้เมื่อrelevantreleasegatesไม่มีnewwronganswerและknownlimitationsแสดงครบ.

## รายการที่ต้องเจ้าของให้ข้อมูล

Tekkenpauseconflict,RoV6.1.5.1ขาด,rulebookversion/scope,officialENnames,controllercounts/models,photo/video/public/foodpolicy,age/registrationfeeที่ไม่มีในsource. ใช้แบบฟอร์มเดิมและเพิ่มเฉพาะคำถามที่พบใหม่. Realbookingoracleยังพัก.
