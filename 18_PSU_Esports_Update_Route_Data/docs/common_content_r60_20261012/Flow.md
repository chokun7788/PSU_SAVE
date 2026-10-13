# Flow r60: ทดสอบสำนวนใหม่และลดการพึ่งคำถามที่ดักไว้

## ขอบเขต

เริ่มจาก r59 ที่ core 5,056 ผ่าน แต่เป็นชุดที่เห็นแล้ว รอบนี้สร้าง development 100 และ reserved 48 ใหม่ก่อนทดสอบ ครอบคลุม 24 หมวด ไทย/อังกฤษ และหลายส่วนในประโยค/พิมพ์ผิดสามจุด/ต่อเนื่อง/ปฏิเสธงานเดิม ใช้ DEMO 720 เดิมแบบ read-only ไม่เพิ่มข้อเท็จจริงใน production

reserved ถูก freeze ด้วย SHA256 ก่อนวัด แต่เป็น synthetic ที่ agent แต่งเอง ไม่ใช่ human blind holdout เมื่อเปิดดู failure แล้วต้องเรียกว่า regression ของรอบถัดไป

## ลำดับ

1. สำรอง source ทั้งสามชุด + DB logical hashes + Git status
2. Freeze questions/gold จากความต้องการเนื้อหา ไม่ส่ง expected_fields เข้า parser/planner
3. วัด development แบบ deterministic แล้วแบบ actual local LLM โดยแยก transport/schema/semantic/content
4. แยกปัญหา: field interpretation, incomplete clauses, rejected intent, history inheritance, typo correction, rendering/evidence และ uncertainty
5. แก้ structural causes ก่อน เช่น overview gate ที่ปิด planner, description อังกฤษที่เป็นแค่ชื่อ key, history ที่ inherit เมื่อ user ถามเรื่องใหม่
6. ใช้ bilingual schema descriptions/typed constraints เพื่อให้ LLM อ่าน attribute ใหม่ได้ ไม่เพิ่มชื่อ fixture หรือคำถามทั้งประโยคใน alias/CUES
7. เพิ่ม guard สำหรับ rejected task และ unknown clause: ตอบบางส่วนต้องประกาศว่าบางส่วน ไม่รายงาน validated complete โดยไม่รู้ need ทั้งหมด
8. วัด development ซ้ำและเปิด reserved ครั้งแรกหลังแก้จาก development เสร็จ
9. วิเคราะห์ reserved โดยไม่อ้าง 100% ถ้ายังผิด บันทึกข้อจำกัดและแก้ general rule ที่มีหลักฐาน แล้วทวนเป็น regression
10. ทวนชุด r59 ที่เกี่ยวข้อง/owner publication guards และคัดลอก logic เฉพาะที่ hash ยังตรงก่อนแก้ พร้อมเอกสาร/receipt ใหม่

## เกณฑ์

- requested content ต้องครบพร้อม status/source pointers
- forbidden fields จากงานที่ผู้ใช้ปฏิเสธต้องไม่ถูกตอบ
- ไม่สืบทอด fields ของคำถามเดิมเมื่อมีคำถามใหม่ชัดเจน
- correction ต้องรักษาเลข/คำปฏิเสธ และไม่ rewrite ข้อเท็จจริงเจ้าของ
- coverage ของ selected plan ไม่ใช่ semantic guarantee; unknown clauses ต้องยังมองเห็นใน artifact/คำตอบ
- policy/ราคาอาจแนบบริบทจำเป็น แต่แยก extra fields เพื่อวิเคราะห์ ไม่รวมกับ content recall


## Runtime flow ฉบับหลังแก้

### A. จากเจ้าของกรอกข้อมูลถึงคำตอบ

1. ฟอร์มรับtypedvalues/status/evidence → draft immutable revision; previewไม่publishdraftเอง
2. เจ้าของreviewfacts/การแปลที่ใช้ → approve exact revisionhash → publishrelease transaction
3. runtimeอ่านsnapshot releaseที่validated และ epoch; demoต้อง opt-inแยกจากproduction
4. คำถามรับ locale/history/config/deadline; common reader resolveexplicitrecordก่อนcontext และรักษาข้อความดิบ
5. stripselectedentitynamesเฉพาะการหาneeds; focusเฉพาะrejectedtaskที่ยืนยันรูปแบบได้; newquestionไม่inheritfieldsเดิม
6. resolvefieldsจากcatalog+schema metadata; scopekindsชัดเจน; broad=trueเฉพาะallจริง; overviewเฉพาะภาพรวมจริง
7. หากlexicalcomplete/reliableใช้fastpath; หากmissing/weak/multineedต้องreview และLLMenabled ให้ส่งschema meaning+clauses+enumโดยไม่ส่งgold
8. spellcandidateจากschemaใช้suggestionพร้อมoriginaltext ไม่มีsame-lengthrewriteโดยเดา; ไม่มีrewriteเลข/คำปฏิเสธ
9. >6clause→explicitplannerdecline;<=6clause→oneLLMcall;deadline4sec+modeladmission+healthgateเดิม
10. validateHTTP/outputsize/JSON/IDs/enum/types; outputerrorไม่ปะปนtransporterror; allfieldsถูกconstraintจากrequest
11. preserveclearneeds/removeweakmatchเมื่อมีvalidreview; tracksemanticsunverified; typedcoverageallocationrepairเฉพาะneedที่มีfieldแล้ว
12. selectrelatedrecordsโดยFK/catalogscope; ไม่ให้LLMสร้างSQL/เปลี่ยนfacts; ถ้ามีpresetหลายตัวถามเลือกก่อน
13. renderexactpublishedvalues,statusandlocator; unsupported/unknownต้องยังระบุ; unresolvedclauses→partialพร้อมบอกส่วนค้าง
14. verifyselectedobligations/evidence/epochอีกครั้งก่อนส่ง; ถ้าreleaseเปลี่ยนต้องไม่ส่งstalefacts; confidenceเป็นheuristic
15. ส่งanswer+decisionartifact+planner_audits; evaluatorนอกruntimeตรวจexpectedneedsที่เลือกไว้ก่อนวัด

### B. Loopพัฒนาที่ทำจริงรอบนี้

| รอบ | พบอะไร | เปลี่ยนอะไร | หลักฐาน |
|---|---|---|---|
| baseline | deterministic17,LLM79 | freeze100/48และสำรอง | BEFORE,manifest,rawlogs |
| 1 | schemaอังกฤษเป็นkey/overviewgate/history | descriptions+gate+focus | 87/100 |
| 2 | flattenedplanตกneed | per-clauseJSON+descriptionsTH | 93/100 |
| 3 | wrongweakcue/falsewholeoverview | strongneeds,wholeoverview,semanticreview | 98/100 |
| 4 | แล้วclauseไม่ตรวจ | splitแล้ว+FAQscope | 99/100 |
| 5 | whyallocationfalsepartial | typedcoverage repair | 100/100 |
| 6 | reserved5failure | conceptmetadata+comparativegate | first43/48→regression48/48 |
| 7 | relatedoldpatternfail20 | sharedmodifierobject | 5056/5056 |
| 8 | context4096vswarmup3072,ownerpreviewnoplan,Nonefalse | contextalignment+entrysettings+audit | dev100,actualpipeline12,previewHTTP12,guards21+1 |

ตารางนี้เป็นรอบที่มีการเปลี่ยนและวัดจริง ไม่เรียกการอ่านเอกสารซ้ำว่าexperimentใหม่ ไม่เพิ่มผลของชุดที่ยังไม่ได้ทดสอบ

### C. Flowรอบถัดไปตามความเสี่ยง

1. ทำmeaning/exclusionแยกkindเมื่อkeyซ้ำ; freezeชุดใหม่ก่อนเห็นผล; goldต้องแยกexplicitneed vs optionalcontextและทวนhumanambiguityภายหลัง
2. เพิ่มqueryentityvariants/unnamed/multitargetพร้อมhardnegatives; isolateddemoพร้อมepoch/withdrawal; เลือกrecordผิดต้องclarifyก่อนfacts
3. เพิ่มlegacyfallbackafterwithdraw/publishregression; ป้องกันข้อมูลownerใหม่ถูกข้อมูลเก่าตอบทับ
4. เพิ่มtypedrelationshipneedสำหรับlinkedpolicy/rateที่ชัดเจน; ambiguityถามเลือก; ตรวจrenderallzonesจากcatalog
5. วัดcoverage+fieldprecision+partialqualityพร้อมtimeouts/busy/unavailable; ทดสอบพ่วงendpointจริงไม่ใช่readerอย่างเดียว
6. ค่อยทำblindhumancheckของfacts/policy/translationหลังautomatedlogicคงที่; userเคยยืนยันlivebookingถูกแยกจากfixtureของcommonรอบนี้

### D. วิธีใช้และการนำเข้า

- เว็บแชท `PSU_LOCAL_LLM_ASSIST_ENABLED` ค่าเริ่มต้นเปิด; owner previewใช้ค่าเดียวกันหลังr60
- directpipeline `experimental_allow_llm=None` อ่าน `PSU_EXPERIMENTAL_ALLOW_LLM`; explicitTrue/Falseoverrideได้
- `PSU_COMMON_PLAN_LLM=0`ปิดเฉพาะcommonplanner; ปิดแล้วสำนวนใหม่ชุดนี้ผ่าน18/100 จึงต้องไม่แสดงว่าเป็นโหมดความสามารถเท่ากัน
- เปิดOllama/modelที่แพ็กมีตามlauncherเดิม; ไม่แก้launcherหรือดาวน์โหลดmodelในรอบนี้; หากmodelcold/busyไม่รับรองlatency
- การอัปเดตโค้ดไม่reloadprocessเดิมอัตโนมัติ: เปิดใหม่จากlauncherหลังปิดprocessของชุดนั้นอย่างปกติ
- สำรอง/ตรวจhashก่อนcopyเฉพาะlogic+test+metadata+docs; ห้ามcopyDEMO.sqliteลงproduction/h้ามpublishdraftแทนเจ้าของ
