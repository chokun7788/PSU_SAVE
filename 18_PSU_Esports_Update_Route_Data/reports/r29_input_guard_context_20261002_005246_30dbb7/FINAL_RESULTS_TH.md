# ผลรอบ r29 — input guard และคำถามพิมพ์ผิดหลายจุด

เว็บพร้อม: http://127.0.0.1:8090/ — รุ่น `2026.10.02-input-context-r29-verified`

## แก้แล้ว

- ordinary noisy31ข้อที่เคยถูกguardหยุด ผ่านไปตอบได้ทั้งหมด; 5 intentional layoutsยังขอพิมพ์ใหม่.
- คำถามอังกฤษ muc/xost/cot, stydent, Slumni และ bok/ook ในกรอบไวยากรณ์ที่ชัด ฟื้น operation/group/durationถูกจุด. ใช้ระยะedit/บริบท ไม่aliasทั้งคำถาม.
- ชื่อเต็มไทยผิดสองจุดเสนอชื่อจากdirectoryแบบ “หากหมายถึง…” ด้วยชื่อและตำแหน่งจริง; ไม่เขียนทับชื่อผู้ใช้.
- vector control pathรักษาหมายเหตุว่าข้อมูลจากแหล่งรองยังรอคนตรวจเครื่องจริง.

## ผ่านอัตโนมัติ (แยกขอบเขต)

- guard100/100; guard4,283ไม่มี newly blocked. ไม่ใช่ accuracyของคำตอบ4,283ข้อ.
- unit168/168; directclean/noisy31คู่ผ่านlegacy31/31และเหมือน29คู่. สองคู่ที่ต่างคือconditionalname/รูปแบบcontrolsพร้อมnote.
- actualHTTP684/684ตามชุดcontracts; หลังเปลี่ยน8090อีก72/72. รวม2live-noiseเคสทดสอบเฉพาะpath/transport ไม่มีreal booked/freeoracle.
- APIชุด684 median 0.112s, p95 0.315s, max 13.761s. เป็นsequential mixed workload ไม่ใช่ผลโหลดหลายคน.
- protected9filesไม่เปลี่ยน; snapshotก่อนแก้ตรวจhashผ่าน; appทุกไฟล์ตรงpackage; packageไม่มีeval.

## ยังพบปัญหา (ไม่ซ่อนในผลผ่าน)

1. ราคา1หรือ2ชั่วโมงยังตอบทางเลือกเดียว.
2. คำถามปุ่มเฉพาะบางข้อยังมีปุ่มอื่นปน/ตอบรายการกว้าง.
3. “ต้องจองอะไรเพื่อเล่นเกมนี้” อาจต้องการบริการที่เลือก แต่ตอนนี้ตอบขั้นตอน.
4. safe unknownอังกฤษบางเส้นทางบอกว่าไม่มีคำแปล ทั้งที่นโยบายต้นฉบับยังไม่มีหลักฐาน.

ประเด็นเหล่านี้พบทั้งclean input จึงไม่ใช่ false rejectionที่r29แก้ และยังไม่นับเป็นsemanticpass. ขั้นต่อไปตามFlowคือduration alternatives→focusedbuttons→bookingresource→source-gapexplanation.

## คน/เจ้าของยังไม่ได้ยืนยัน

กฎTekken pauseที่ขัดกัน, RoVท้ายข้อ6.1.5.1, version/scopeและ104reviewitems, ชื่ออังกฤษทางการ, PS5controllerรายละเอียด, photo/video/public/foodpolicy formalapproval, age/registrationfeesที่ไม่มีข้อมูล. การจองจริงยังพักไว้. ไม่มีการเปลี่ยนนโยบาย/ไฟล์ที่เจ้าของกรอกเพื่อให้testผ่าน.

## หลักฐาน

- `DETAILED_CAUSE_ANALYSIS_TH.md`: สาเหตุ/คำตอบเดิม/คำตอบใหม่/การเลือกrouteของ8เคสเนื้อหาต่าง
- `downstream_changed_cases_analysis.json`: traceก่อน/หลังเต็ม
- `pipeline31_A/B/C_details.jsonl`: ทุก62responseต่อรอบ
- `candidate_C_guard100.json`, `candidate_C_guard_regression4283.json`: guardspans/scores/profile
- `candidate_C_unit.json/log` เก็บผลที่ไม่ผ่านก่อนแก้; `candidate_D_unit.json/log`ผล168/168
- `http_noise36_details.jsonl`: graderครั้งแรกเข้าใจmodeผิด5controlsและพบsafeunknown1ต่างenvironment; `http_safe_unknown_clean_probe.json`พิสูจน์clean/noisyบนเว็บตรงกัน; `http_noise36_B_details.jsonl`ผลแก้graderโดยไม่เปลี่ยนexpected
- `release_preflight_verified.json`, `FINAL_VERIFICATION.json`, `change_audit.json`, `before/`, `changes/`, `git_status_before/after.txt`
- `flow_initial.md`, `flow_final.md`; เอกสารทำงาน `docs/129_input_guard_context_r29_flow_20261002.md`

แพ็กเกจเดิมr28และlogเดิมยังอยู่. ตัวทดสอบ8091หยุดแล้ว; เว็บ8090launcherPID34508พร้อมใช้. ไม่commit/reset/stashไฟล์เดิม.
