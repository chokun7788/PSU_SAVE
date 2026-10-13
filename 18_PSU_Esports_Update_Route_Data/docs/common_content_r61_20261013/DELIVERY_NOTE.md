# การใช้ r61 ที่ส่งเข้าแล้ว

sourceในโปรเจกต์จริงและโฟลเดอร์ready_packageอัปเดตแล้ว 11ไฟล์เดิม+9ไฟล์ใหม่ มีbefore/diffsและreceipt. LLMยังเปิดตามlauncherปกติ

ปิดแล้วเปิดระบบชุดนั้นใหม่ตามปกติเพื่อโหลดโค้ด; processที่ค้างยังไม่เปลี่ยนตามไฟล์ ไม่ได้หยุดserver/โมเดลของผู้ใช้ระหว่างทำงาน. `/health` รุ่นใหม่มีcommon_loaded_build เพื่อดูโค้ดที่โหลด;owner `/api/status` มีbuildแยกactive/epoch

planner8s queue12sยังถูกจำกัดด้วยglobaldeadlineจริง;preview10sอาจมีเวลารอน้อยกว่าweb19s. ไม่ใช้sample8requestsเพื่อโฆษณาว่ารองรับ8usersต่อเนื่องทุกคำถาม

อ่าน RESULTS_TH.md เพื่อดูรายการS01–S16:ยังไม่ครบทั้งหมดของFlow. ข้อมูลจริง41draftsไม่มีapproval/release;OWNER_REVIEW_PACKETอยู่workspaceสำหรับreview ไม่คัดลอกrawpacketเข้าdistributionและไม่publishเอง

ZIPเดิมยังไม่ใช่buildนี้ ส่วนที่อัปเดตคือsourcefolders. งานต่อหลัก:field-levellegacybridge/independentcontextgold →budget/compare/sharedstate →Thaierror →calibration/long-runload →ownerapproval/activation/rebuildสองvariants
