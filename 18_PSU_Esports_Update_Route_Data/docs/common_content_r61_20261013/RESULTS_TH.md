# ผลลงมือทำ Flow รอบ r61

วันที่ 2026-10-13 เวลาไทย. เป็นการลงมือระยะแรกและพัฒนาส่วนคิวต่อจากแผน 16 ข้อ ยังไม่ใช่การปิดทุกข้อของแผน

## ผลและข้อจำกัด

| ชุด | ผล | สิ่งที่พิสูจน์ |
|---|---:|---|
| actual local LLM development รอบแรก | 98/100 | news TH เลือก title แทน body 2 เคส |
| รอบสอง | 72/100 | มี 4s transport timeouts และ circuit cooldown; ไม่ใช่ semantic failuresทั้งหมด |
| หลังรักษา semantics TH/แก้ newsและ8s budget | 100/100 | ไทย50 อังกฤษ50; named synthetic seen regression |
| source หลัง identity guard/batch wrapper | 100/100 | actual LLM ใหม่ ไม่ใช่ replay |
| guard/projection replay | 100/100 | rawproposalsจากactualLLM;ไม่มีการเรียกโมเดลใหม่ |
| related regression รอบแรก | 5036/5056 | 20เคส policy conditionsต้องมีdetailsบริบท; projectionตัดมากเกิน |
| หลังแก้ contextของpolicy | 5056/5056 | TH2528 EN2528;ไม่ใช่20k fullsuite |
| parent game → child fields | 16/16 | read-only fixture;ไม่ครอบคลุมทุกgraphpath |
| pipelineจริง + actualLLM | 12/12 | 6หมวด×TH/EN;DEMO ไม่ใช่liveWordPress |
| owner preview HTTP + actualLLM | 12/12 | authenticatedloopback;epochไม่เปลี่ยน |
| guardsล่าสุด | 36/36 | รวม cross-process gate, batch, linkedpolicy, mutation, publication/HTTP |

มี HTTP guardหนึ่งรอบถูกWindowsabortด้วยWinError10053ที่requestoriginrejection ก่อนเรียกLLM;รันอีกครั้งผ่าน เก็บfailedlogไว้ ยังไม่ระบุสาเหตุเป็นโมเดลหรือปิดsecurityguardเพื่อคะแนน

## สิ่งที่แก้แล้ว

1. schema meaningsครบ155slotsใช้kind+key;แยกinstalledversionกับverifiedcontrolversion;รักษาคำอธิบายTHที่ช่วยสำนวนเดิม
2. typed read needs/artifactมีsource_span/field_refs/resolution/ambiguous_kind และ semantic_correctness_verified=False;ไม่เปลี่ยนschema-validเป็นintenttruth
3. response profilesแสดงexplicitfieldsกับnecessarycontext เลิกlistallfieldsสำหรับราคา/เหมา/childเสมอ;fullrequestsยังครบ
4. identity guardลดชื่อ/topic/FAQquestionที่โมเดลเติมเมื่อถามresponse/details ไม่ตัดidentityเมื่อuserถามจริง
5. knownemptyzone_idsเฉพาะschedule/closureแสดงทุกโซน และvalidatorยอมรับตามcatalog;ไม่เปลี่ยนemptyทุกชนิด
6. game→service→accountpolicyขยายdecision/detailsที่ถามตามFK มีedge+sourceของpolicy;unknownFKไม่เดา
7. typed game discoveryตามplayers_min/maxและstudio_supported ไม่ใช้roomseats;livequeriesยังไปadapterเดิม
8. “ทั้งหมด”ในhistoryของคำถามราคาใช้needsเดิม แสดงตัวเลือกของกลุ่มนั้น ไม่กลายเป็นข้อมูลทุกfieldของaudience
9. authority guardแยกno-release/unmanagedcompetition/live/ownedtarget/withdrawn;ownedmissที่คืนNoneไม่เปิดlegacyfallbackโดยเงียบ
10. ENschema typoเพิ่มunique adjacent transposition รักษาvalidwords/negation/digits
11. >6 clausesแบ่งได้2batch(สูงสุด12clauses) พร้อมwholecontext/globalbudget;หลายfieldsunionได้สูงสุด64ในallowedschema;เกินlimitยังdeclineอย่างชัด
12. planner8sปรับได้1–10sภายในglobaldeadline;boundedqueueรอสูงสุด12sและคำนวณเวลาที่เหลือใหม่หลังรอ
13. SharedModelGateใช้OSfilelockร่วมระหว่างprocess+threadsemaphore,ปลดเมื่อrelease/processexit;ไม่ได้เพิ่มOLLAMA_NUM_PARALLELหรือโหลดโมเดลเพิ่ม
14. health/statusมีfingerprintที่captureเมื่อmoduleload;candidatepackageversionr61.1;ไม่ได้restartprocessผู้ใช้
15. ownerreviewpacketอ่าน41draftsพร้อมfacts/source/status/blockersเป็นรายรายการ;ไม่แก้/approve/publishfacts

## ข้อมูลเกินยังต้องทำต่อ

ไม่ได้อ้างว่ากระชับขึ้นทุกกรณี: r60 มี106extrafieldsรวม, r61ก่อนidentityguardมี133, replayหลังguard121 และactualrunล่าสุด122. เพิ่มส่วนใหญ่จากการแสดงวัน/โซน/แพลตฟอร์ม/เงื่อนไขราคาเพื่อรักษาscope ส่วนextrasที่โมเดลเลือกเกินยังมี

ต้องใช้goldที่แยกmust_include/allowed_context/must_excludeจึงวัดfieldprecisionจริงได้;เลขextraทั้งหมดไม่ใช่เลขคำตอบผิด. ไม่ลดบริบทจนราคา/กฎผิดเพื่อให้ตัวเลขเล็กลง

## ทดลองพร้อมกัน — sampleเล็กจากเครื่องจริง

| คำขอพร้อมกัน | ถูก/ทั้งหมด | medianต่อคำขอ | มากสุด |
|---:|---:|---:|---:|
| 1 | 1/1 | 4.20s | 4.20s |
| 2 | 2/2 | 4.17s | 4.98s |
| 4 | 4/4 | 5.89s | 8.01s |
| 8,queue10s | 7/8 | 10.00s | 12.82s |
| 8,queue12s | 8/8 | 8.75s | 14.66s |

เป็นthreadsเรียกactualpipeline+localLLMด้วยsyntheticfixture ไม่ใช่browser/multiworkerlong-runcapacity ไม่มีการยืนยันwarm/coldแยก sample1/2/4/8ยังน้อยจึงไม่ใช้p95นี้รับรองSLOทั่วไป ชุด8หลังปรับเป็นseenworkload retest

## งานที่ยังเหลือตาม16ข้อ

| ID | สถานะในรอบนี้ | ยังต้องทำ |
|---|---|---|
| S01 | projection+identityguardแล้ว | independentcontextgold/over-answeringที่เหลือ |
| S02 | gamechildren+linkedaccountpolicyแล้ว | resource→service→rate/multipleplatform/fullgraphscope |
| S03 | kind-qualified155slotsแล้ว | semanticexamples/exclusionsที่ละเอียดกว่าและnewholdout |
| S04 | ENtransposeเพิ่มแล้ว | Thai keyboard/grapheme/multipleentityerror+candidatecontext |
| S05 | bounded2batchesแล้ว | actualLLMlong-querymatrix/nouncoordinationที่กว้างขึ้น |
| S06 | labelsสำคัญ/allzonesแก้แล้ว | enum/structuredconditions/labelsทุกfieldให้เป็นภาษาผู้ใช้ |
| S07 | timeout/queue/degradationเฉพาะrecordแล้ว | cancellation/recoveryและbusycontextmatrixมากขึ้น |
| S08 | needs+guardinstrumentationแล้ว | independentsemanticvalidation/calibratedmeaningconfidence |
| S09 | playercountgamefilterแล้ว | budget/compare/generalunnamedentityranking |
| S10 | ownedtargetfallthroughguardและmutationแล้ว | field-levellegacybridge/withdrawalacrossalloldaliases/filtersก่อนretrieval |
| S11 | allchoicespricehistoryแก้แล้ว | sharedtypedstateข้ามcommon/legacyและ24flows |
| S12 | uncalibratedflagยังชัด | separatecalibration/holdoutlabels;ยังไม่fitcalibrator |
| S13 | cross-processgate+1/2/4/8sampleแล้ว | sustainedbrowser/workerload/coldrun;ไม่claim8usersproduction |
| S14 | read-only41-recordpacketแล้ว | 41รายการมีpublicationblockers;ownerfactsapprovalยังต้องรอ |
| S15 | healthsourcefingerprint/versionแล้ว | controlledrestartและUIตรวจstaleprocess |
| S16 | sourcefoldersyncแล้ว | zipสองvariantsใหม่/clean-machineproofยังไม่ทำ |

ไม่ระบุว่าall16complete. ลำดับต่อ: annotatecontextgold+fieldauthoritybridge → entitydiscovery/compare/sharedstate → Thaierror/cancellation → calibratedholdout/productionload → ownerapproval/activation/packagebuild

## หลักฐาน

BEFORE/EXTRA_BEFOREและbeforeสำรองcode;failedrunsเก็บแยกทุกครั้ง;OWNER_REVIEW_PACKETอ่านอย่างเดียว;GUARD_REPLAYแยกจากactualLLM;LOAD_RESULTSเดิมและQUEUE12ใหม่;sourcehash/DBhash/Gitstatusตรวจแล้วในDELIVERY_RECEIPTก่อนนำเข้า

### การจัดประเภท extra ของ actualrunล่าสุด

{"explicit": 25, "necessary_context": 97}

## ตรวจหลังนำเข้าโปรเจกต์จริง

installed_project_guards.log:36/36ผ่าน;sourcehashทั้ง3ชุดตรงกัน;DBlogicalhashทั้ง4เท่าเดิม;Gitentriesก่อนเริ่ม325รายการยังอยู่ครบ;ไม่restartผู้ใช้/ไม่publishownerfacts/ไม่rebuildZIP. ทดสอบล่าสุดsharedgateได้8/8ในsample ไม่ใช่productioncapacityguarantee
