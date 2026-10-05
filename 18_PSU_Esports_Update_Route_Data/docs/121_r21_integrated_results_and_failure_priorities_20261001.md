# r21: ผลแก้ภาษาอังกฤษและความเข้าใจคำถาม พร้อมสาเหตุและลำดับงานต่อ

วันที่ 1 ตุลาคม 2026 — วิเคราะห์และลงมือจาก Flow 120; เก็บ r20, GT, source และ log เดิมไว้

## 1. สรุปที่ยืนยันได้

งานรอบนี้ทำทั้งการแปล การแก้ runtime การทดสอบซ้ำ การตรวจผลที่ถอย และการส่งแพ็กเกจใหม่ ไม่ใช่แผนอย่างเดียว

| เกณฑ์เดิมที่ตรึงไว้ | r20 | r21 | เปลี่ยน |
|---|---:|---:|---:|
| ไทย clean / 1,000 | 894 | 897 | +3 |
| ไทย noisy / 1,000 | 825 | 843 | +18 |
| อังกฤษ clean / 1,000 | 896 | 975 | +79 |
| อังกฤษ noisy / 1,000 | 830 | 920 | +90 |
| รวม clean / 2,000 | 1,790 | 1,872 | +82 |
| รวม noisy / 2,000 | 1,655 | 1,763 | +108 สุทธิ |

Noisy failures ลด 345 → 237 หรือลดลงประมาณ 31.3% ตามเกณฑ์นี้: 109 ข้อเดิมกลับมาผ่าน และมี 1 ข้อเดิมที่เคยผ่านกลับตก Clean ไม่มีข้อที่ผ่านเดิมแล้วตกใหม่ การผ่านเหล่านี้ยังไม่เท่ากับความถูกต้องทุกสาระ เพราะ 1,107/2,000 คู่ไม่มีเงื่อนไขเนื้อหาบวกใน GT เดิม

| การตรวจเพิ่ม | ผล | ขอบเขตที่ยืนยัน |
|---|---|---|
| Unit/regression หลัก | 54 test methods ผ่าน | มีหลาย semantic subcases รวมถึงหลายงาน/ตัวเลข/ชื่อ/คำกำกวม |
| Competition target/taxonomy/source facets | 37 test methods ผ่าน | เกมและ facet, source gap, translation gate; ตรวจเพิ่มหลังเผยแพร่คำแปล |
| Generated holdout | 196/196 ผ่าน | รูปคำผิดที่สร้างจากกรอบงานเดิม ไม่ใช่ข้อความจริง 196 คน |
| แพ็กเกจผ่าน HTTP + input guard | 28/28 ผ่าน | รับ input→pipeline→output ใน profile deterministic; รวม unavailable สองภาษา |
| Replay failures เดิม | 345/345 mode และ answer ตรง gate ใหม่ | ใช้ trace รุ่นใหม่อธิบายผลใหม่ได้ โดยยังเก็บ trace r20 เดิม |
| Exceptions / latency ceiling | 0 / 0 ใน 4,000 inputs | งบ 20 วินาทีของชุดทดสอบ; ไม่ใช่ SLA ของระบบจริง |
| Source/GT/fixture เดิม | 154/154 hashes ตรง | ไม่เปลี่ยนนโยบาย ราคา เวลา หรือข้อมูลเจ้าของ |
| Backup เริ่มรอบ | 20/20 hashes ตรง | สำรองสถานะที่มีการแก้อยู่ก่อนเริ่ม ไม่ย้อนกลับไปหา Git HEAD |
| Runtime + locales ในแพ็กเกจ | 124/124 ไฟล์ตรงโปรเจกต์ | รุ่น 2026.10.01-integrated-r21; ZIP ไม่มีชุดทดสอบและ log ผู้ใช้เดิม |

Full Thai gate รวมจากสองช่วงที่ไม่ทับกัน ช่วงละ 500 คู่ ตรวจ ID และลำดับกับ fixture เดิมครบ 1,000 คู่ รุ่น F หลังจากนั้นแก้เฉพาะเส้นทางการแข่งขันภาษาอังกฤษ ส่วน engine ภาษาไทยคงรุ่น E; replay และ HTTP ตรวจด้วยโค้ดแพ็กเกจสุดท้ายอีกครั้ง Full English gate ใช้รุ่น F ครบ 1,000 คู่

## 2. ทำไมคะแนนเดิมกับ V2 ไม่เท่ากัน

| Frozen V2 overlay เดิม | r20 | r21 |
|---|---:|---:|
| clean | 1,740 | 1,752 |
| noisy | 1,608 | 1,647 |

มี 116 noisy ที่ legacy ผ่านแต่ frozen V2 ตก:

- **92** ข้อ: overlay เดิมยังคาด `localization_pending` แต่ runtime มีคำแปลที่เผยแพร่แล้วและตอบเป็นเนื้อหา ตัวเลขนี้คือสถานะที่ไม่ตรงวงจรคำแปล ไม่ใช่หลักฐานว่าคำตอบ 92 ข้อถูกสาระครบ และไม่ใช่ 92 ข้อผิดคำแปลทั้งหมด
- **14** ข้อ: V2 คาด live lookup แต่ได้คำตอบตาราง/ปฏิทิน ต้องตรวจว่าผู้ใช้ขอสถานะจองจริงหรือเวลาบริการตามปฏิทิน หากขอว่าง/ถูกจองจริง การตอบเวลาเปิดยังไม่พอ
- **10** ข้อ: V2 จัด verified negative หรือคำปฏิเสธเป็น no_answer แต่ fixture คาด answer_available มีทั้งเกมไม่อยู่ใน catalog และรุ่นอุปกรณ์ไม่ระบุ ต้องแยกคำตอบเชิงปฏิเสธที่มีหลักฐานจากการหา evidence ไม่ได้

ไม่แก้ overlay เดิมเพื่อทำให้คะแนนสวย เก็บรายการทั้งหมดใน `reports/r21_integrated_improvement_20261001/v2_frozen_overlay_disagreement.jsonl` งานถัดไปคือ overlay รุ่นใหม่ที่ระบุ release/hash ของคำแปล และตรวจเนื้อหาตาม task โดยยังรายงานคะแนนเทียบรุ่นเดิมคู่กัน

## 3. ภาษาอังกฤษ: ไม่ใช่แค่แปลคำแล้วเปิดใช้ทันที

ทะเบียนภาษาอังกฤษเดิมไม่มี records ที่ runtime ใช้ได้ แต่มี draft 615 fields ตรวจเทียบ source แล้วเผยแพร่ **590 fields** ใน release `en-20261001T093109+0700`; แก้ถ้อยคำ **266 fields**; กัก **25 fields** ได้แก่ชื่อไทย 23 ช่องที่ไม่มี spelling อังกฤษยืนยัน และข้อความ 2 ช่อง (ชื่อรายการ Tekken / clause RoV ที่ต้นฉบับขาด)

ตัวอย่างข้อแปลที่แก้:

| Source / ข้อเดิม | ทำไมผิด | คำแปลที่ใช้ |
|---|---|---|
| กรรมการ → Chairman | ทำให้หน้าที่เปลี่ยนเป็นประธาน | Committee member |
| เหรัญญิก → Priest | เป็นคนละตำแหน่ง | Treasurer |
| เลขานุการ → Assistant | หน้าที่เลขานุการหาย | Secretary |
| PSU → Chulalongkorn | ระบุองค์กรผิด | Prince of Songkla University |
| VALORANT: วัตถุที่ทำลายไม่ได้ | draft กลับความหมายเป็นทำลายได้ | indestructible พร้อมข้อยกเว้นเดิม |
| Tekken: ปรับแพ้ → disqualification | ปรับแพ้ไม่เท่ากับตัดสิทธิ์จากรายการ | forfeit ตาม clause นั้น |
| CS2: knife round | draft กลายเป็นดวลดาบ | knife round |
| Horizon: Call of the Mountain | draft เปลี่ยนเป็นอีกเกม | ใช้ชื่อเกมใน source |
| ตำแหน่ง ผู้ช่วย/รองอธิการบดี | ห้ามรวมเป็นตำแหน่งเดียวกัน | ใช้บทบาทที่ตรง source; แสดงบทบาทไทยกำกับ |

การตรวจ local model รอบแรกได้ audit ผ่าน 213/615 และมีผลที่คลาดเคลื่อน/ผิดรูปแบบหลายข้อ **ไม่ได้ใช้ชุด 213 นั้นเป็นตัวเผยแพร่** ผู้ช่วยกลับไปตรวจ source เทียบคำแปลและแก้รายการเป็นชุด 590 หลังจากนั้น Mechanical number flags 67 รายการมี resolution แยกไว้ ไม่ใช้จำนวนตัวเลขอย่างเดียวตัดสินความหมาย

Source hash ช่วยจับว่าต้นฉบับเปลี่ยนหลังแปล แต่ hash ไม่พิสูจน์ว่าคำแปลดี จึงมีทั้ง source comparison, semantic tests, stale-hash test และ held fields ผู้ใช้อนุญาตให้ผู้ช่วยแปล/review ได้แล้ว; metadata ยังคง `human_reviewed=false` และ `owner_policy_approval=false` ชื่อบุคคลไทยแสดง spelling เดิมจาก source ไม่แต่งชื่ออังกฤษขึ้นมา ทะเบียนและ draft เก่าทั้งแปดไฟล์ยังอยู่และ hash ตรง

หลักฐาน: `english_final/source_review.jsonl`, `reviewed_candidate.jsonl`, `held.jsonl`, `summary.json`, `publication.json` และ `mechanical_flag_resolutions.jsonl` ในโฟลเดอร์รายงาน r21

## 4. ทำไมข้อมูลครบแต่คำตอบยังผิด

### 4.1 แต่ละจุดอ่านงานไม่ตรงกัน

ตัวอย่าง `บุคคลทั่วไป เล่น PC 30 นาที เสียกี่บบาท`: extractor เดิมอ่าน price_intent=true แต่ protected guard จับ “กี่บาท” แบบตรงตัวไม่ติด แล้วคำว่า “บุคคลทั่วไป”+“เล่น” ไปเลือกสิทธิ์เข้าใช้ Guard ตอบทันทีด้วย confidence 0.98 โดย calculator ไม่ได้แข่งขันคะแนนเลย

**ควรได้:** 70 บาท/1 session สำหรับกลุ่มที่ถาม ตามตาราง PC ที่เก็บอยู่ **แก้:** ส่ง price_intent ที่ยืนยันแล้วให้ guard และกู้คำถามราคาแบบมี anchor เพิ่ม negative “บุคคลทั่วไปเล่น PC ได้ไหม” ให้ยังตอบสิทธิ์ ผลทั้งคู่ผ่าน

### 4.2 รู้เกมแต่เสียรายละเอียดที่ต้องถาม

- `PUBG เล่นได้ทที่ไหน`: location cue เสีย เหลือ “เล่นได้” จึงถูกเลือกเป็น schedule ควรตอบ PC Zone
- `VR Zone รอบละกีน่าที`: duration cue หาย เหลือโซนอุปกรณ์ ควรมี 30/60 นาทีจากข้อมูล session; คนละเรื่องกับการใช้ VR 30 นาทีกินช่อง availability หนึ่งชั่วโมง
- `How many sessioons...`: จำนวน session หาย จึงตอบวิธีจองกว้าง ๆ ควรบอก maximum 3 sessions
- `afteronon ... Tuesday`: ยังอยู่ schedule แต่ period หาย ควรเฉพาะ 13:00–16:00; Friday afternoon ต้องยังเป็น Maintenance
- `CS2 คือเกมอะไน`: operation รายละเอียดเกมไม่ติดแม้ target ถูก ควรอธิบาย Tactical FPS และเป้าหมายการเล่นจาก source

**แก้:** operation/qualifier recovery มี anchor และงบ edit; ไม่แก้ตัวเลข วันที่ ชื่อเพื่อเดา เพิ่ม AND groups ของเนื้อหา จึงไม่ผ่านเพียงเพราะอยู่หมวดเดียวกัน การกู้ซ้ำต้องได้ข้อความเดิม (idempotence) พบและแก้กรณีรอบสองตี duration เป็นราคา/session singularization ใน pilot แล้ว

### 4.3 ตัวจับชื่อโซนสร้างเงื่อนไขเอง

คำสุภาพ “เลย” เดิม fuzzy เข้ากับ alias “เพลย์” เกิน threshold ทำให้เพิ่ม PS5 ในคำถาม CS2 ทั้งที่ผู้ใช้ไม่ได้ระบุ PS5 จากนั้น filter เกมด้วยโซนผิดและตอบว่าไม่มีเกมนั้น

**แก้:** exact alias ก่อน; fuzzy โซนเฉพาะ Latin token ทั้งคำที่ยาวพอ ระยะ edit หนึ่งและผลเดียว เช่น cockpik→Cockpit; ยกเลิก Thai sliding window ที่เทียบคำสุภาพกับชื่อบริการ Tests “เลย”, “เลยอยากทราบว่า” ไม่สร้าง PS5 และคำถาม CS2 กลับตอบ PC

### 4.4 Catalog ไม่ตอบทุกคำถามที่มีชื่ออุปกรณ์

`Do you offer vernight accommodation` เดิมคำ offer ถูกใช้เปิดรายการอุปกรณ์ ทั้งที่ object ไม่ใช่อุปกรณ์ **แก้:** offer/have ต้องมี object หรือโซนที่รองรับ จึงตอบว่าหาหลักฐานไม่ได้สำหรับ accommodation แต่ “offer headsets” ยังตอบอุปกรณ์

บางกรณียังเหลือ: “คีย์บอร์ด mechanical คืออะไร” ไป inventory และคำถาม “ทำอุปกรณ์เสียหาย” ที่ cue เสียเหลือ equipment ไป catalog ต้องใช้ applicability ที่รวม operation+object มากขึ้น ไม่ใช่ keyword equipment อย่างเดียว

### 4.5 หลายงานและ noun phrase ใช้ and เหมือนกัน

`How many memberss are there, and who is the president` มี count + role scope สองงาน ต้องตอบจำนวนใน directory แล้วถามว่าประธานมหาวิทยาลัยหรือประธานชมรม แต่หัวข้อ “conduct and sportsmanship” หรือ “equipment and devices” อาจเป็นหนึ่งหัวข้อ

**แก้:** cue preflight ก่อนตัดสินใจ split; competition noun coordination อยู่กับ rulebook target เดียว; count-and-role แยกอย่างมีบริบท ไม่แยกทุก and

สำหรับ `PC ... ราคาเท่าไหร่ แล้วของยังไง` การแยกงานถูกแล้วแต่ preprocess เสนอ ของ→จองก่อน scope guard ทำให้ child ตอบขั้นตอนจอง **แก้เพิ่มรอบ E:** scope guard อ่านคำต้นฉบับ จึงตอบราคาในข้อหนึ่ง และถามตรงส่วน “หมายถึงวิธีจองใช่ไหม” ในอีกข้อ รักษาคำถามที่ชัดว่า “จองยังไง” ให้ตอบขั้นตอนตามเดิม

### 4.6 คำจริงที่กำกวมไม่ควรบังคับ correction

pay/play, rice/price, march/match มีความหมายได้อยู่แล้ว Keyboard distance ไม่บอกความตั้งใจแน่นอน

**แก้บางกรอบ:** ถามเฉพาะ pay/play เมื่อชื่อเกมชัดและไม่ใช่ pay for/to; `How to pay Ring Fit Adventure` จึงถามวิธีเล่นหรือค่าบริการ แทนการเดา `in-march procedure` ถาม phase แทนคืนหัวข้อเอกสารหรือเปลี่ยน march เป็น match ข้อขอจำนวน/ราคาแบบตรงตัวยังทำงาน

ยังเหลือ `... rice` และคำกำกวมหลายงาน ต้องใช้ task/target/บริบท session ร่วมกัน โดยรักษาคำที่ผู้ใช้ตั้งใจพูดจริง

### 4.7 แปลได้แล้วทำให้ข้อผิด facet ปรากฏ

`How do CS2 and VALORANT technical pause rules differ?` หลังเผยแพร่คำแปล เลือกถูกทั้งสองเกมแต่ VALORANT เคยตอบ Tactical Timeout เพราะ taxonomy รวม pause/timeout และ overlap ภาษาอังกฤษสูงพอ

**ควรได้:** CS2 technical pause ทีมละสองครั้ง ครั้งละไม่เกิน 10 นาที/แจ้งกรรมการ; VALORANT technical pause สำหรับ hardware/disconnection/software และห้ามสื่อสารเว้นแต่อนุญาต ไม่เอา quota tactical 60 วินาทีมาตอบ

**แก้รอบ F:** subtype ต้องมีหลักฐานจากหัวข้อ source จริงก่อนจัดอันดับภาษาอังกฤษ ทดสอบ comparison และ technical/tactical/emergency แยกกัน พร้อมห้ามปะปน 60 seconds กับ technical/emergency ผลผ่านใน engine และ HTTP

## 5. คะแนนเลือกคำตอบหมายถึงอะไร

### 5.1 Central capability score

จาก `app/pipeline/capability_registry.py`: เริ่ม base score ของ capability แล้วบวก domain match +0.12, answer type +0.06, tool action +0.10×tool confidence, tool domain +0.06, frame domain +0.20 และ operation priority ตามชนิดงาน เช่น game detail +0.28, price +0.32 ยังมี priority/precondition/veto จากนั้นหาร 1.80 และจำกัด 0–0.999

- top <0.45: execution_allowed=false / abstain_low_score
- margin <0.035, action ต่างกัน และ operation ไม่ชัด: review_required
- margin ต่ำแต่ operation/action ยังใช้ได้: selected_low_margin
- เงื่อนไขอื่น: selected

ดังนั้น score สูงไม่ได้หมายถึงถูก 99.9% สัญญาณ domain/frame/tool อาจมาจาก cue ที่เสียอันเดียวกัน คะแนนจึงเสริมกันได้แม้เข้าใจผิด

ตัวอย่างเดิมที่ trace ยืนยัน: PUBG location typo เลือก structured.schedule=0.926 เพราะ location cue หาย; VR duration typo เลือก structured.equipment=0.990; member operation typo เลือก hybrid=0.433 ต่ำกว่า 0.45 จึงถามกว้าง ๆ การแก้ควรคืน operation/qualifier และ evidence ไม่ลด threshold เพื่อผ่านทุกข้อ

### 5.2 Confidence ของ shortcut

protected branch, English shortcut และบาง fast path คืนก่อน central ranking ค่า 0.98/0.99 เป็นค่าประจำ branch ไม่ใช่ผลแข่ง candidate แยก `fixed_branch_confidence` กับ `selected_candidate.score` ในรายงานทุกข้อ ถ้า trace ไม่มี ranking จะระบุ N/A ไม่สร้างคะแนนอธิบายเอง

### 5.3 ทำไม validation ยังปล่อยคำตอบผิดได้

Warning ไม่ใช่ error; เช่น missing price source อาจเป็นแค่ warning และ validation.ok=true คำตอบมี source URL ถูกก็ยังตอบผิดงานได้ อีกข้อที่คงเหลือคือ finalizer บางจุดส่ง query ว่างเข้าตัวตรวจ ทำให้ contract ที่ต้องรู้ operation ตรวจได้ไม่ครบ

R21 เพิ่ม applicability/content checks ใน path ที่แก้แล้ว แต่ยังไม่ได้ย้ายทุก return ไปผ่าน semantic contract เดียวทั้งระบบ การเรียก Flow นี้ว่ามีขั้น N “ตรวจ required content” จึงเป็นแบบที่ต้องพัฒนาต่อด้วย ไม่ใช่การรับรองว่า global validator ทำครบแล้ว

## 6. “เนื้อหาต้องปรากฏ” คืออะไร

ถาม “PC ของบุคคลทั่วไป 2 ชั่วโมงเท่าไหร่” แล้วตอบ “PC เปิดวันจันทร์ถึงศุกร์” มีคำ PC และ source URL แต่ไม่ได้ตอบราคา

Contract ที่มีประโยชน์ต้องมี **จำนวนเงิน AND กลุ่มผู้ใช้ AND ระยะเวลา/session AND source ราคา** หากใช้ `must_contain_any=[PC, บาท, ราคา]` แค่มี PC ก็ผ่านได้ เช่นถามบุคคลหนึ่งแล้วส่ง directory 25 คน รายชื่อคนนั้นอยู่ในรายการจึงผ่าน แต่ยังไม่ใช่คำตอบที่เลือกบุคคลนั้นได้จริง

สำหรับการแข่งขัน technical pause ต้องมี subtype technical AND เงื่อนไขตาม source AND target เกมที่ถาม พร้อม forbidden tactical quota สำหรับ unavailable ต้องมีข้อความยืนยันไม่ได้ และห้ามแสดง free count ที่ไม่มีหลักฐาน Required content ต้องสัมพันธ์กับตัวเลข/หน่วย/คน/เครื่อง ไม่ใช่ถุงคำที่ปรากฏที่ใดก็ได้

## 7. ข้อเดียวที่ legacy ถอย: TH-04585

คำถาม: `ผศ.ดร.ณัฐงศ์ ทอวเทพ ทำตำแหน่งอะไร` ชื่อเสียทั้งชื่อและนามสกุล

- r20 ตอบ directory 25 คนทั้งชุด จึงผ่าน `must_contain_any=[ผู้ช่วยอธิการบดีฝ่ายวิชาการ, ผศ.ดร.ณัฐพงศ์]` แม้ไม่ได้แสดงว่าจับคนในคำถามได้
- r21 ไม่พบชื่อที่ยืนยันแล้วใน lookup จึง no_answer และคะแนนเดิมตก
- Source ของชื่อที่สะอาดระบุ ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ แต่ไม่บังคับ assign คนนี้จากชื่อผิดสองส่วนเพื่อรักษาคะแนน

งานต่อ: entity resolver สำหรับชื่อบุคคลแบบ candidate+margin และคำถาม “หมายถึง…หรือไม่” เมื่อไม่แน่นอน พร้อม negative ชื่อใกล้กัน/บุคคลที่ไม่มีจริง แยกจากการแก้ operation ตำแหน่งที่ทำแล้ว ไม่ใช้การส่งรายชื่อทั้งหมดเป็นการแก้ regression

## 8. ลำดับปัญหาที่ยังควรแก้ จากผลสุดท้าย

237 noisy ที่ตกไม่ใช่ 237 factual errors และหนึ่งคำถามอาจมีหลายสาเหตุ ตารางนี้เป็นจำนวนอาการตาม domain ไม่ใช่จำนวน root cause ที่เป็นอิสระ

การคัดงานจาก trace/ผลคู่คำถามแยกได้: 32 ข้อมีคำตอบออกมาแต่ scope/content/status ไม่ผ่าน, 105 ข้อ clean ผ่านแต่ noisy จบไม่ผ่านในกลุ่ม recovery/entity, 42 ข้อตกตั้งแต่ clean ที่ต้องตรวจ source/task/label, 29 ข้อต้องตรวจ scope/LLM profile, 17 ข้อ recording source-gap/route-label, 5 ข้อ specific ambiguity เทียบ label เดิม, 5 ข้อ localizationหรือเลือกงานผิด และ 2 ข้อ controller model source gap กลุ่มเหล่านี้รวมครบ237และเป็น **triage ที่มีหลักฐาน ไม่ใช่ primary cause ยืนยันแล้ว237ข้อ**

ควรเริ่มจาก 32 ข้อที่ยังปล่อยคำตอบไม่ตรงงาน/เกณฑ์และช่องliveก่อน แม้จำนวนจะน้อยกว่า105 typo symptoms เพราะการตอบข้อมูลที่ดูมั่นใจแต่ใช้ผิดงานมีผลต่อผู้ใช้มากกว่า no-answer ที่แสดงข้อจำกัดไว้แล้ว

| ลำดับ | งาน | หลักฐาน/จำนวนที่เกี่ยวข้อง | แนวทาง + gate |
|---|---|---|---|
| **P0.1** | ทุกเส้นทางต้องรักษา task+target+qualifier | ยังมี catalog/เวลา/ปุ่มแทนงานที่ถาม | ส่ง frame เดียวไป handler; hard applicability; final contract ใช้ query จริง; ไม่ให้ source URL กลบงานผิด |
| **P0.2** | ตารางปกติ vs live vsวันปิดต้องแยก | schedule 18, domain live 4; V2 disagreement 14 | ถ้า free/booked ต้อง live fixture; ถ้าเวลาเปิดต้อง calendar; closure exact date; unavailable ห้ามบอกว่าง |
| **P0.3** | Content contracts และ eval label/version | 1,107 pairs ไม่มี positive gate; 116 legacy/V2 conflicts | AND groups + relations + approved locale release/hash; outcome verified-negative; เก็บคะแนน frozen เทียบคู่กัน |
| **P1.1** | Operation cue ไทย/อังกฤษที่ยังหาย | rules/penalty 41, reservation 15, fees 15 | context + noisy-channel candidates จาก lexicon งาน/source; clear anchors; real-word veto; test untouched word negatives |
| **P1.2** | Object/scope/ชื่อบุคคล | members/contact 36, equipment 16 | ชื่อ/บทบาท/องค์กร/ประเภทงานแยก entity; role membershipไม่เหมือนตำแหน่งผู้บริหาร; candidate margin/clarify; ห้ามแต่ง romanization |
| **P1.3** | เกม: catalog/detail/control/location | catalog 11, detail 6, controls 3 | operation lock; explicit service restrictions; current catalog vs archival controls; negative unknownเกมไม่ตอบเวลา |
| **P1.4** | Compound/context/general boundary | compound domain 60 | ตรวจแต่ละ child task/status/content; อ้างถึงลอย ๆ ถามตรงส่วนที่ขาด; general knowledge แยก LLM-off gate กับ profileจริง |
| **P1.5** | Competition facets/source hierarchy | 12 + heading/subtype fixes ที่ทำแล้ว | parent-child section metadataใน projection; relation subtype; เมื่อไม่มีเนื้อหาห้ามตอบแต่ heading; source contradiction ถือไว้ |
| **P2** | Trace และ latencyใน owner assist profile | deterministic 4,000 inputs/HTTP28 ยังไม่ยืนยัน LLM profile | บันทึก cue edits/frame/evidence/child reasons/selection vs shortcut; ทดสอบ profileจริงแยกจาก determinism |

ตัวอย่างคงเหลือที่ต้องอ่านอย่างถูกประเภท:

- TH-04858 `Roblox เล่นได้ไม` ตอบเวลาบริการ: wrong operation/unknown game applicability; ต้องแสดงว่าไม่มีหลักฐานเกมนี้ ไม่เอา opening hours มาทดแทน
- TH-02613 `EA Sports FC 24 เล่นยังไงง` ตอบรายการปุ่ม: how-to กับ controls ยังปะปน ควรตอบวิธีเล่นจาก game detail
- TH-01260 `ตอนนี้ศูนย์์เปิดอยู่ไหม` ได้ข้อความวันปิดจาก curated: ต้องระบุ calendar/live/time evidence ที่ตรงวันจริง ไม่ถือข้อความทั่วไปว่าเป็นสถานะตอนนี้
- TH-03957 และ recording-policy variants: no_answer มีเหตุผลเพราะนโยบายไม่อยู่ในหลักฐาน แต่ตก route label; ต้องทบทวน label ไม่บังคับตอบว่าอนุญาต
- EN-03401 และอีก variant: source ไม่ระบุจอย PS5 รุ่นใด การตอบ unverified ถูกหลักฐาน แม้ GT คาด answer_available
- คำถาม latency/GPU/server-client/แปล reservation หลายข้อ: ชุดนี้ปิด LLM assist; local source ไม่มีข้ออธิบายที่ต้องการ เป็น capability/profile mismatch ที่ต้องทดสอบแยก ไม่ใช่ spell checker ล้มเหลวทุกข้อ
- `วันหยุดเปิดไหม`: ถ้ายังไม่บอกวัน การถามวันที่อาจถูกต้อง เพราะวันหยุดราชการไม่เท่ากับ special closure อัตโนมัติ
- Call of Duty family: เกมมากกว่าหนึ่งชื่อ/บริการ การถามรุ่นเกมเพื่อเลือกบริการเป็น clarification ที่มีเหตุผล ต้องตรวจ GT ว่าควรคาด list หรือ clarify

## 9. Flow สำหรับวงรอบต่อไปและวิธีใช้ร่วมกัน

1. **Freeze** source/runtime/locale/GT และสร้าง report ใหม่ ไม่ทับ log
2. **Parse** raw + recovered candidate เป็น task, target, qualifier, scope โดยเก็บ offset/reason และ protected literals
3. **Resolve** entity candidate จาก source; exact ก่อน, bounded edit/keyboard/noisy channel เมื่อ context รองรับ, ไม่เปลี่ยนคำจริงหรือ assign คนที่ margin ต่ำ
4. **Apply** operation/object preconditions ก่อน shortcut ทุกชนิด; ambiguity ต้องถามให้เฉพาะเจาะจง
5. **Retrieve/compute** source ที่ตรง target/facet; live API/fixture กับ calendar/ราคาเป็นคนละ evidence type
6. **Localize** เฉพาะ release source-hash-matched; translation unavailable กับ source unavailable เป็นคนละเหตุผล
7. **Validate** operation-specific required facts/relations/negation/units/subtype; ชื่อ source และ URL อย่างเดียวไม่พอ
8. **Return** ข้อเดียวหรือหลาย child พร้อม outcome/status/reasons; branch confidence ไม่เท่ากับ ranking probability
9. **Test** focused + negatives → frozen full set → semantic overlayรุ่นใหม่ → owner profile/API; owner oracle ตามช่วงที่ผู้ใช้พร้อม
10. **Analyze**ทุกข้อถอยและอันดับผลเสียจริง; แยก label mismatch/source gap/locale lifecycle แล้วปรับ Flow ก่อนรอบถัดไป

ใช้หลายวิธีตามหน้าที่: keyboard geometry ลดต้นทุน substitution; edit distance สร้าง candidate; context/operation anchorsคัดความหมาย; entity margin ป้องกันสลับเป้าหมาย; source facet ป้องกันสลับข้อกฎ; content contract กันคำตอบครบคำแต่ผิดเรื่อง ไม่มีวิธีเดียวแทนทุกขั้น

### งานที่ทำเองต่อได้ / งานที่ต้องมีข้อมูลจริง

ทำเองได้: P0 guards/contracts, structured projection hierarchy, cue recovery/negative controls, source-based translation update, outcome/versioned overlay, scoring trace และ API/profile tests

ข้อมูลที่ต้องถามเจ้าของเมื่อพร้อม (ยังไม่เปลี่ยน source):

1. Tekken: clause ห้ามหยุดเกมทุกกรณี กับ clause อนุญาตเมื่อคู่แข่งยินยอม/เกิดฉุกเฉิน ใช้ข้อใดเป็นหลักและในสถานการณ์ใด?
2. PS5 controller: รุ่นจริงที่ให้บริการแต่ละเครื่องคืออะไร และต้องการเก็บใน equipment source ใด?
3. การถ่ายภาพ/อัดวิดีโอ: อนุญาตหรือไม่, พื้นที่/เวลา/บุคคลอื่น/การขออนุญาตมีเงื่อนไขอะไร?
4. ชื่อไทย 23 ช่อง: มี spelling อังกฤษทางการหรือให้คงชื่อไทยในคำตอบอังกฤษ? (ปัจจุบันคง source ไทยแล้ว ไม่ต้องรอเพื่อถามบทบาททั่วไป)
5. Clause RoV ที่ขาดท้ายและชื่อรายการ Tekken: ขอ source ฉบับเต็ม/ชื่ออังกฤษยืนยัน ไม่เดาข้อความที่หาย
6. สถานะจองจริง: เมื่อเก็บได้ ขอเวลาบันทึก timezone, เครื่อง, slot และผล free/booked ที่เจ้าของรู้แน่ พร้อมสถานะ Maintenance/closed; API200อย่างเดียวใช้รับรองไม่ได้

## 10. หลักการจากงานวิจัยที่นำมาประกอบ

- [Brill & Moore (2000)](https://aclanthology.org/P00-1037/) เสนอ error model ที่ละเอียดกว่าการให้น้ำหนัก edit เท่ากัน ใช้เป็นหลักในการมอง keyboard/edit เป็น candidate cost ไม่ใช่ความหมายที่รับรองแล้ว
- [CRASpell](https://aclanthology.org/2022.findings-acl.237/) และ [RobustGEC](https://aclanthology.org/2023.emnlp-main.1043/) รองรับการศึกษาความทนต่อ noise/context perturbation แนวทดสอบคำผิดหลายส่วนและ negative controls ในระบบนี้เป็นการประยุกต์ ไม่ได้อ้างผลทดลองจีน/อังกฤษว่าเท่ากับความแม่นยำไทย
- [Tokenization Repair in the Presence of Spelling Errors](https://aclanthology.org/2021.conll-1.22/) เป็นหลักอ้างอิงว่าความผิด segmentation กับ spelling อาจพัวพันกัน การกู้ cue ไทยจึงต้องมี context ไม่ใช้ระยะตัวอักษรอย่างเดียว
- [RAGAs](https://aclanthology.org/2024.eacl-demo.16/) แยกการหา context ที่เกี่ยวข้อง การใช้ context อย่างซื่อตรง และคุณภาพคำตอบ ใช้สนับสนุนการแยก route/evidence/content gates ใน Flow นี้
- [RAGChecker](https://arxiv.org/abs/2408.08067) เสนอ diagnosis แยก retrieval และ generation ใช้เป็นแนวออกแบบตรวจ target/facet กับ factual claims โดยยังไม่ได้ติดตั้งหรือรายงานคะแนนจาก RAGChecker/RAGAs ในโปรเจกต์นี้

ข้อสรุปเชิงระบบมาจาก trace/source/test ของโปรเจกต์ ส่วน papers เป็นหลักออกแบบ ไม่ใช่หลักฐานรับรองคะแนนรอบนี้

## 11. ไฟล์ที่ใช้ติดตามและวิธีเปิดรุ่นใหม่

- Flow หลัก: `docs/120_integrated_reliability_and_english_flow_20261001.md`
- ทุก failure เดิม 345 ข้อ: `reports/r21_integrated_improvement_20261001/analysis_final/per_case_analysis_345.md` และ `.jsonl` มี old answer, clean candidate, new answer, source contract, trace reasons, selected/runner-up/margin/veto และการขาด positive gate
- ผลชุดใหญ่: `paired_th_final.jsonl` และ `paired_en_F.jsonl`; `analysis_final/analysis.json`
- ปัญหาที่ยังเหลือ: `analysis_final/remaining_pairs.jsonl`; รวมทั้ง 1 legacy regression ที่อยู่นอก 345 ข้อเดิม
- การจัดหมวดครบ237ข้อ: `analysis_final/remaining_classified_237.jsonl` และ `remaining_classified_summary.json`; traceของregressionใหม่แยกใน `legacy_regression_04585.json`
- คำแปล/เหตุผลกัก: `english_final/`; original audit ที่ไม่ได้เผยแพร่อยู่ `english_review/`
- HTTP และ integrity: `package_api_final.*`, `integrity_final.json`, `runtime_final_manifest.json`

แพ็กเกจใหม่อยู่ `owner_local_delivery_20261001_integrated_r21/PSU_Esports_Chatbot_Local` และ ZIP ข้างกัน เปิด `Open-PSU-Esports-Chatbot.cmd` จากโฟลเดอร์ใหม่นี้เมื่อต้องการใช้ r21 ตัวที่เปิดอยู่เดิมบน 8095 ไม่ได้ถูกเปลี่ยนโปรเซสหรือหยุดโดยงานนี้ Test server 8096 ที่สร้างขึ้นถูกปิดแล้ว

ยังไม่รับรอง production/LLM assist profile หรือสถานะ WordPress จริง ข้อที่ต้องเก็บข้อมูลจริงคงตามที่ผู้ใช้ให้พักไว้ ตัว launcher จริงยังมี profile LLM/semantic assist ตามเดิม; การผ่าน deterministic gate ไม่ได้ครอบคลุม path เหล่านั้นทั้งหมด
