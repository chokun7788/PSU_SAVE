# ผลพัฒนาและทดสอบ PSU Esports Chatbot — r32 final13

## ผลที่ได้

ทำ Flow และลงมือแก้ครบกลุ่มที่มีหลักฐานในรายการเดิม พร้อมตรวจซ้ำ 13 รอบของ candidate แต่ยังไม่ใช่ระบบที่ตอบทุกคำถามถูก 100% งาน source ที่ต้องให้ผู้จัดยืนยันและงานเก็บสถานะจองจริงยังมีข้อจำกัดเดิม

- กู้คำสถานะว่างจากบริบทอุปกรณ์/เวลา โดยไม่ใช้ตารางเปิดบริการแทนสถานะจอง
- กู้หัวข้อกฎด้วยศัพท์งานและ edit distance รักษาเกม เลขรุ่น ตัวเลข คำจริงและคำเชื่อม
- ตอบข้อกฎเต็มและทุกประเด็นที่มีหลักฐาน ตรวจข้อความจริง ไม่รับเพียง source ID หรือหัวข้อ
- ตอบส่วนที่มีหลักฐานพร้อมแจ้งส่วนอายุ/ค่าสมัครที่ยังขาด; ถ้าถามอายุอย่างเดียวไม่ใช้ eligibility แทน
- ปฏิเสธฉบับกฎผิดปี; ไม่นับปีเกิด/ยอดเงินเป็นปีฉบับ
- แก้ English builder metadata drift 6 แถวและทำ current-reference sidecar โดยคง frozen Gold
- เพิ่มข้อความรอและ bounded retry เฉพาะ 503 ที่ retryable; ปรับ TCP backlog 16 หลังทดลองบน Windows โดยไม่เพิ่ม worker
- เตรียม template/checker ของสถานะจองจริงที่ตรวจแยก transport และ occupancy

## หลักฐานทดสอบ

| ชุด | ผล | ขอบเขต |
|---|---|---|
| Unit final13 | 464/464 | tests เดิม + tests ใหม่; ไม่มี skip |
| Full corpus รวม affected replay | 51,983/55,583 grades; 20,327 inputs | ผล legacy ไม่ใช่ factual accuracy; provenance C6/C7/C10/C12/C13 |
| Bilingual typo pairs | clean 1772/2000; noisy 1676/2000 | scorer v2 เดียวกัน; ก่อน r32 noisy 1672, regression 111; ตอนนี้ 1676, regression 107 |
| Independent source clauses actual HTTP final13 | 30/30 | clause เต็ม + source + ภาษา |
| Independent partial/source-gap actual HTTP final13 | 8/8 | eligibility พร้อมบอกส่วน age/fee ที่ขาด; clean/noisy/age-only |
| Explicit source year HTTP | 24/24 ใน C9–C12 | TH/EN 3 เกม; หลัง deploy รุ่นสุดท้ายตรวจซ้ำและเก็บผลแยก |
| Existing actual HTTP regression | C9 937/937; C13 รันซ้ำเก็บผลแยก | 4 live occupancy questions defer; รุ่นล่าสุดมี frozen-status differences ที่อธิบายด้านล่าง |
| Synthetic known booking | 31/31 | approved/cancelled/no-show, boundary, lunch, Maintenance, special closure, VR; ไม่ใช่ oracle ของจริง |
| Session context | 12/12 sessions, 24/24 turns | offline original wording/contents; ไม่ยืนยันทุก session ภาษาอังกฤษ |
| Existing smoke scripts | 71/85 บน C7 | 14 ชื่อไฟล์ที่ตกเหมือน baseline; เก็บ log และสาเหตุด้านล่าง |
| Extra corpora | 970 requests / 981 grades | รุ่น C7, subset aliases แยก; human observations ไม่ใช่ accuracy |
| Native input guard | exact flags 471/500 | layout 500/500; repeat FN 27 / FP 2; ไม่ใช่คะแนนคำตอบ |
| Retry protocol | 9 scenarios + HTTP 503 TH/EN 2/2 | จำกัดรอบ/payload ไม่ซ้ำ ไม่ retry network/500/JSON เสีย |
| Windows pending TCP probe | backlog 5: 6/10; 16: 10/10 | delayed accept fixture; สนับสนุน intake fix ไม่ใช่ proof root cause ของ network failure ทุกครั้ง |
| Cold actual retry-helper C11 | 10/10, retry รวม 8 | 3.20–5.07 วินาทีบนเครื่องนี้; ไม่ใช่ WordPress SLA |

**เกณฑ์เดิมที่ผ่านแล้วตกเพิ่ม 2 grades:** สองคำถาม eligibility + minimum age เคยคาด no_answer ทั้งคำถาม แต่ source มี eligibility จึงตอบ partial พร้อมแจ้งอายุที่ขาด การตอบแบบใหม่ผ่าน oracle อิสระ 8/8 ไม่เปลี่ยน Gold เดิมเพื่อให้ผ่าน ดู FROZEN_STATUS_DIFFERENCES_REVIEW.json ส่วนก่อนเปลี่ยน partial (C10) ไม่มี new failed grades

## สิ่งที่ยังผิด/ยังพิสูจน์ไม่ได้

ยังมี 1898 unique inputs ที่ไม่ผ่านอย่างน้อยหนึ่ง legacy grade; จำนวนนี้รวม route/intent labels, ข้อความเก่า, source IDs, status, ข้อมูลขาด และคำตอบที่ต้องตรวจเนื้อหา ไม่ใช่ 1898 คำตอบที่ยืนยันว่าผิดข้อเท็จจริง

คู่ clean ผ่าน/noisy ตก 107 คู่: ไทย 54 อังกฤษ 53 มี positive content contract 42 อีก 65 คู่ยังไม่มีเงื่อนไขเนื้อหาบวก การแบ่งกลุ่มต่อไปนี้อิง trace และเป็นข้อสันนิษฐานเชิงวิเคราะห์ มิใช่การ adjudicate โดยเจ้าของ:

- คำจริงกำกวม ต้องถามกลับ: 1
- คำถามบุคคลและบทบาท: 19
- สถานะคำตอบหรือเกณฑ์อื่น: 9
- คำสำคัญหรือหัวข้อเปลี่ยนเส้นทาง: 71
- เนื้อหาไม่ครบตามสัญญา: 7

รายละเอียดทุกคู่มี input ปกติ/ผิด, output, expected route/status/content, recovery ที่ใช้, resolver score/margin, mode, validation errors และข้อจำกัดการสรุปที่ REMAINING_107_ANALYSIS_TH.md / JSONL คำตอบ clean เป็น baseline ไม่ใช่คำตอบจริงที่ยืนยันแล้ว ตัวอย่างชื่อบุคคลอังกฤษบางคำถามได้รายชื่อรวมที่ผ่าน route/status จึงยังใช้ยืนยันบทบาทบุคคลนั้นไม่ได้

Priority ต่อไป: ตรวจ 42 positive failures รายข้อ → เพิ่ม syntax/task cues และล็อกชื่อบุคคลจาก source → เพิ่ม positive oracle 65 เคสที่ยังขาด → ปรับ repeat guard พร้อม negative คำจริง → ทดสอบโหลดต่อเนื่องเมื่อจะเปิดหลายผู้ใช้ อย่าลด threshold หรือเพิ่ม alias ทั้งประโยคเพื่อให้ได้คะแนนสูง

## วิเคราะห์ smoke เดิม 14 รายการ

- answer_pipeline / english_draft_preview / llm_health_circuit_breaker / pipeline_fixes_20260823 / game_catalog: บาง assertion บังคับชื่อ mode หรือ LLM path เก่า ทั้งที่มี source path/fast path ใหม่ ต้องแยกตรวจเนื้อหาก่อนปรับ oracle
- bilingual_pipeline: บังคับ clarification ราคาแบบเดิม; ต้องตรวจว่าคำถามขาดข้อมูลจริงหรือแสดงทางเลือกมีหลักฐานแล้ว
- availability_policy_regressions: bare Call of Duty ต้องแยก edition; ไม่ยืนยันเกมผิดฉบับเพื่อให้ผ่าน
- bilingual_web_api: เจอ 503 ขณะรันชุดอื่น; actual retry helper และ cold test แยกไว้ ผลนี้ไม่ได้เป็นหลักฐานตอบข้อเท็จจริงผิด
- boundary_guard: เกณฑ์คาด boundary mode แต่ระบบผ่าน freshness gate; ต้องตรวจไม่มีการอ้างสถานะสดเทียม
- correctness_control_flow_v1: บางเคสคาด no_controls ในขณะที่ source ปุ่มมีแล้ว
- english_format_parity_fixes: บังคับ literal label เดิม ขณะที่ระบุ official Thai source และแปล role แล้ว
- genre_alias_formatting: คาด Dota2/Mobile Legends ที่ไม่อยู่ใน verified catalog; ไม่เพิ่มเกมที่เจ้าของยังไม่ยืนยัน
- real_usage_golden: 23/24; Naruto how-to ต่าง mode/intent แต่มีคำตอบและ source PS5
- update: คาดคำ มหาลัยอื่น แต่ตอบ นักศึกษา-นักเรียนต่างสถาบัน และราคาเดิม; source/semantic check ต้องแยกจาก literal

ไม่เรียกว่า 14 ข้อนี้เป็นปัญหา oracle ทั้งหมดโดยอัตโนมัติ ต้องเก็บ assertion และหลักฐาน source ที่รองรับการจัดประเภทไว้

## เจ้าของยังต้องยืนยัน / สิ่งที่พักไว้

ดู OWNER_QUESTIONS_TH.md: ข้อยกเว้นและโทษ Tekken pause, ข้อ RoV 6.1.5.1 ฉบับเต็ม (แถว s08_c01), ฉบับปีของแต่ละรายการ, ค่าสมัคร/อายุ/รายชื่อรวมสำรอง, นโยบายถ่ายภาพ และการตรวจคำแปลเชิงนโยบาย Audit English hash 103/104 ไม่ใช่ owner approval

สถานะจองจริงยังไม่เก็บตามคำสั่งเดิม ไม่มีการสร้างการจองหรือยืนยัน occupancy จริง ใช้ REAL_BOOKING_ORACLE_PENDING_TEMPLATE_V2.json และ tools/check_saved_booking_oracle_r32.py เมื่อพร้อม

## การรักษางานและ provenance

- snapshot ก่อนแก้ 423 files; owner/Gold 584 hashes คงเดิม; tests เดิม 140 files คงเดิม; ไม่ reset/stash/commit
- เก็บ raw ทุก candidate; สร้างผลด้วย exclusive file mode; ไม่มี initial hash ของ historical logs ทั้งหมด จึงไม่อ้าง cryptographic verification ทุก log
- summary ของ HTTP runner ที่คัดจาก r31 บางไฟล์มี label runtime ค้าง แก้ provenance เป็น sidecar API_EXECUTION_PROVENANCE_CORRECTION.json โดยใช้ health/package/hash ของจริง ไม่เขียนทับผลเก่า; runner final13 ใช้ health version โดยตรงแล้ว
- C12 merge เขียน full results และ summary ครบก่อนชนชื่อ changes sidecar เดิม จึงยังเทียบครบ 20,327/55,583 ได้; เก็บความผิดพลาดและทำ execution sidecar ชื่อใหม่ ไม่เขียนทับ raw
- บาง retained provenance labels ของ replay ถูกคัดมาเป็น source-abstention แม้ C13 เป็น conjunction fix ให้ยึด FINAL_EXECUTION_SCOPE.json ที่บันทึก scope/keys/code hash แยกอย่างชัดเจน
- full offline runner ปิด LLM/semantic และใช้ controlled booking unavailable; legacy fast-answer alias บางข้อเรียก local 8091 แล้วได้ 404 ซึ่งไม่ใช่การเก็บ occupancy WordPress จริง ส่วน actual API ใช้ owner profile LLM/semantic เปิด

Flow ฉบับสุดท้าย: docs/133_all_remaining_r32_verified_flow_20261002.md

เว็บสำหรับลองใช้: http://127.0.0.1:8090/ — แพ็กเกจ final13; ตรวจผล postrelease ใน RELEASE_FINAL13_VERIFICATION.json
