# วิเคราะห์สาเหตุ r29 — แยก guard, operation และความถูกต้องของเนื้อหา

## ขอบเขตผล

ชุดเดิมที่ถูก block 36 ข้อมี ordinary noisy 31 ข้อและ intentional keyboard-layout 5 ข้อ ไม่ใช่ false rejection 36 ข้อทั้งหมด. หลังแก้: guard31/31 ต่อได้ และ layout5/5ยังขอพิมพ์ใหม่. ชุด guard100/100; regression4,283ไม่มี newly blocked. 4,283 เป็นการทดสอบตัวกรอง ไม่ใช่การรันตอบครบทั้งหมด.

Pipeline62 responses (clean/noisy31คู่): legacy31/31 แต่เนื้อหา clean/noisyเหมือน29คู่. สองคู่ที่ต่างคือ conditional name suggestion และรูปแบบหัวข้อcontrolsที่ยังคงทุกปุ่ม/หมายเหตุ. จำนวนนี้ไม่รับรองว่าคำตอบ clean ครบทุกความหมายที่ผู้ใช้ตั้งใจ. ผล fixture booking แยกจาก live API จริง.

## ทำไมมีข้อมูลครบแล้วยังผิด

1. Guard ทำงานก่อนค้นข้อมูล: score layout สูงจาก ngram ของ candidate ที่ลบเลข/เครื่องหมายออกจนเหลืออักษรไม่กี่ตัว หรือคำอังกฤษ typo; จึงไม่ถึงฐานข้อมูลเลย.
2. ผ่าน guard แล้ว operation words ยังผิด: มีข้อมูลเกม/ราคาแต่เส้นทางเลือกตอบจาก cue ที่เหลือ เช่นชื่อเกม จึงตอบข้อมูลจริงคนละเรื่อง.
3. เครื่องคิดราคาใช้ group/duration ที่ parser ตรวจพบ: group หายทำให้คืนทุกกลุ่ม; duration หายทำให้คืนแพ็กเกจ 1 session. การตรวจว่า route เป็น service_fee ไม่พอ.
4. Formatter แต่ละเส้นทางรักษา provenance ไม่เหมือนกัน: มีคำตอบปุ่มตรงจากแหล่งรองแต่หมายเหตุ manual verification หาย.
5. เกณฑ์ legacy อ่อน: ยอมรับ domain/status/บางคำ ทำให้ 6 จาก8คำตอบที่ต่างได้ pass แม้เนื้อหาขาด. ต้องดู operation,group,duration,complete clauses,source statusแยก.

## หลักการคะแนน

คะแนน guard/capability/confidence เป็นค่าประเมินตามกฎของโค้ด ไม่ใช่เปอร์เซ็นต์ความถูกต้อง. Layout thresholdยังเป็น .39; scoreต่ำลงเมื่อ sourceอ่านได้แข็งแรงกว่า keyboard projection หรือ English typoมี 1-edit dictionary neighbor และ ≥3 known English words/สัดส่วน≥.55. การเป็น neighbor ไม่แก้ input. ชื่อบุคลากรเปรียบเทียบได้เฉพาะ full span/role frame, ≤2 edits, ratio≤.16 และ margin≥2; ตอบแบบเงื่อนไข ไม่ถือว่ารู้เจตนาผู้ใช้แน่นอน.

## รายกรณีที่ตอบต่างหลังปลด guard

### MASTER-GT-TH-04585 — P1 ชื่อเต็มผิดสองตำแหน่ง

คำถาม: `ผศ.ดร.ณัฐงศ์ ทอวเทพ ทำตำแหน่งอะไร`

สาเหตุ: resolver เดิมยอมรับชื่อเต็มตรงหรือส่วนชื่อที่ตรง; เมื่อทั้งชื่อและนามสกุลผิดจึงไม่พบคน แม้ capability structured.members ได้ .872 ก็ไม่ใช่หลักฐานยืนยันบุคคล

การแก้และสิ่งที่ควรตอบ: เทียบชื่อเต็มกับ directory เดิมได้ระยะ OSA=2 และห่างอันดับสองมากพอ; ตอบเงื่อนไข “หากหมายถึง…” ด้วยชื่อ/ตำแหน่งจากต้นฉบับ ไม่แก้ชื่อใน input

เส้นทางเดิม: `pipeline:experimental_rag_direct_fallback` → ใหม่: `pipeline:structured_members_person_lookup`

คำตอบเดิม:

ยังไม่พบหลักฐานที่ยืนยันคำตอบตรงคำถามนี้ครับ ข้อมูลที่ใกล้เคียงยังใช้ยืนยันข้อเท็จจริงที่ถามไม่ได้ กรุณาระบุเรื่องหรือบริการให้ชัดขึ้น หรือตรวจสอบกับศูนย์โดยตรงครับ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

คำตอบใหม่:

หากหมายถึง ผศ.ดร.ณัฐพงศ์ ทองเทพ ข้อมูลในแหล่งอ้างอิงระบุว่า:
ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ
หมวด: Members
สังกัด/รายละเอียด: มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### MASTER-GT-TH-03100 — P1 สถานะหลักฐานหายข้ามเส้นทาง

คำถาม: `ปุมควบคุมของ Super Mario Odyssey บน Nintendo Switch มีอะไรบ้่ง`

สาเหตุ: structured path มี coverage_status note แต่ vector path ไม่ใส่หมายเหตุ; legacy contract ไม่บังคับให้มีสถานะ manual verification

การแก้และสิ่งที่ควรตอบ: ใส่ note จาก source rows ก่อน metadata ถูกลดเหลือ hit; ทุกปุ่มเดิมคงอยู่ ไม่อ้างว่าคนตรวจเครื่องจริงแล้ว

เส้นทางเดิม: `pipeline:game_control_vector_first` → ใหม่: `pipeline:game_control_vector_first`

คำตอบเดิม:

Super Mario Odyssey บน Nintendo Switch มีปุ่มควบคุมดังนี้:
•    L (Left Stick): เคลื่อนที่ - บังคับทิศทางการเดินและวิ่งของมาริโอ
•    R (Right Stick): มุมกล้อง - หมุนและแพนมุมกล้องเพื่อดูสภาพแวดล้อม
•    R3 (Click Right Stick): มุมมองบุคคลที่หนึ่ง - กดเพื่อเปลี่ยนเป็นมุมมองบุคคลที่หนึ่งสำหรับส่องดูรายละเอียด
•    A / B: กระโดด - ใช้กระโดด สามารถใช้ปุ่ม A หรือ B ก็ได้
•    X / Y: ขว้างหมวก / วิ่งเร็ว - กดเพื่อขว้างหมวก Cappy หรือกดค้างไว้พร้อมบังคับทิศทางเพื่อวิ่งเร็ว
•    ZL: ย่อตัว - ย่อตัวลงเพื่อม้วนตัว หรือใช้ทำท่ากระแทกพื้น (Ground Pound)
•    R: รีเซ็ตกล้อง - รีเซ็ตมุมกล้องให้หันไปทางเดียวกับที่มาริโอกำลังมองอยู่
•    D-Pad Down: โหมดถ่ายภาพ - เข้าสู่โหมดถ่ายภาพเพื่อตกแต่งและบันทึกหน้าจอ
•    D-Pad Right: สแกนอะมีโบ - เปิดใช้งานระบบสแกนฟิกเกอร์ amiibo
•    - (Minus): แผนที่ - เปิดแผนที่เพื่อดูข้อมูลอาณาจักรหรือใช้วาร์ป
•    + (Plus): หยุดเกม - หยุดเกมชั่วคราวและเปิดเมนูตัวเลือก
แหล่งข้อมูล: https://gameinputdatabase.com/game/32

คำตอบใหม่:

Super Mario Odyssey บน Nintendo Switch มีปุ่มควบคุมดังนี้:
•    L (Left Stick): เคลื่อนที่ - บังคับทิศทางการเดินและวิ่งของมาริโอ
•    R (Right Stick): มุมกล้อง - หมุนและแพนมุมกล้องเพื่อดูสภาพแวดล้อม
•    R3 (Click Right Stick): มุมมองบุคคลที่หนึ่ง - กดเพื่อเปลี่ยนเป็นมุมมองบุคคลที่หนึ่งสำหรับส่องดูรายละเอียด
•    A / B: กระโดด - ใช้กระโดด สามารถใช้ปุ่ม A หรือ B ก็ได้
•    X / Y: ขว้างหมวก / วิ่งเร็ว - กดเพื่อขว้างหมวก Cappy หรือกดค้างไว้พร้อมบังคับทิศทางเพื่อวิ่งเร็ว
•    ZL: ย่อตัว - ย่อตัวลงเพื่อม้วนตัว หรือใช้ทำท่ากระแทกพื้น (Ground Pound)
•    R: รีเซ็ตกล้อง - รีเซ็ตมุมกล้องให้หันไปทางเดียวกับที่มาริโอกำลังมองอยู่
•    D-Pad Down: โหมดถ่ายภาพ - เข้าสู่โหมดถ่ายภาพเพื่อตกแต่งและบันทึกหน้าจอ
•    D-Pad Right: สแกนอะมีโบ - เปิดใช้งานระบบสแกนฟิกเกอร์ amiibo
•    - (Minus): แผนที่ - เปิดแผนที่เพื่อดูข้อมูลอาณาจักรหรือใช้วาร์ป
•    + (Plus): หยุดเกม - หยุดเกมชั่วคราวและเปิดเมนูตัวเลือก
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/32

### MASTER-GT-EN-00205 — P1 กลุ่มลูกค้าตกหล่น

คำถาม: `Slumni play Nintendo Switch for one hour. How much des it cost`

สาเหตุ: Slumni ไม่ตรง alumni จึงไม่เลือกกลุ่มและแสดงราคาทุกกลุ่ม; route/status ผ่านไม่พิสูจน์ eligibility ถูก

การแก้และสิ่งที่ควรตอบ: syntax/resource/price frame รองรับ alumni ระยะ 1; คืนราคา 50/100 THB เฉพาะกลุ่มตามตาราง

เส้นทางเดิม: `pipeline:structured_service_fee_en` → ใหม่: `pipeline:structured_service_fee_en`

คำตอบเดิม:

The question does not specify the number of players, so both verified packages are shown.
Nintendo Switch - 1 hour (1-2 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 50 THB
- General adults: 140 THB
- Requested duration: 60 minutes, charged as 1 session(s).
Nintendo Switch - 1 hour (3-4 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 100 THB
- General adults: 280 THB
- Requested duration: 60 minutes, charged as 1 session(s).
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

คำตอบใหม่:

The question does not specify the number of players, so both verified packages are shown.
Nintendo Switch - 1 hour (1-2 people)
- PSU alumni and students from other institutions: 50 THB
- Requested duration: 60 minutes, charged as 1 session(s).
Nintendo Switch - 1 hour (3-4 people)
- PSU alumni and students from other institutions: 100 THB
- Requested duration: 60 minutes, charged as 1 session(s).
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### MASTER-GT-EN-01933 — P1 คำบอกการจองตกหล่น

คำถาม: `What do you need to ook to play Beat Saber`

สาเหตุ: ook ไม่ตรง book ทำให้ game_detail ชนะ; เกมถูกชื่อแต่ operation ผิด; legacy contract ยังให้ผ่าน

การแก้และสิ่งที่ควรตอบ: recover book เฉพาะกรอบ what do you need to ... to play; ได้ขั้นตอนจองเหมือน clean; ความหมาย “ต้องจองอุปกรณ์อะไร” ยังต้องเสริม

เส้นทางเดิม: `pipeline:structured_game_detail_en` → ใหม่: `pipeline:rule_en`

คำตอบเดิม:

Verified English information:
Beat Saber
Genre: VR Rhythm Game
Overview: Beat Saber is a VR rhythm game in which players use light swords to slash blocks in time with the music.
How to play: Put on VR glasses, hold the controller, and smash blocks in the direction indicated. Dodge obstacles and try to score points according to the rhythm of the music.
Available at: VR Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

คำตอบใหม่:

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### MASTER-GT-EN-00110 — P1 คำราคาหายสองจุด

คำถาม: `How muc does it xost for a PSU student to play VR for 1 hour`

สาเหตุ: muc/xost ไม่ถูกคืนเป็น much/cost; entity price_intent=False; ตัวเลือก no_answer จึงชนะ ไม่ใช่เพราะไม่มีราคาต้นฉบับ

การแก้และสิ่งที่ควรตอบ: คืนคำราคาแต่ละ span ใน frame how ... does it ... for + resource; 1 edit/คำ; PSU student, VR, 1 hour ไม่เปลี่ยน; ตอบ 0 THB/60 นาที

เส้นทางเดิม: `pipeline:english_no_answer` → ใหม่: `pipeline:structured_service_fee_en`

คำตอบเดิม:

I could not find verified PSU Esports Studio - Phuket information for this question.

คำตอบใหม่:

VR - 1 hour (1-5 people)
- PSU students and staff: 0 THB
- Requested duration: 60 minutes, charged as 1 session(s).
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### MASTER-GT-EN-04950 — P1 ราคา/กลุ่ม/ระยะเวลาในคำถามหลายหัวข้อ

คำถาม: `How much does it cot for a PSU stydent to play Nintendo Switch for 2 hours, and how do I book`

สาเหตุ: cot + stydent ทำให้หัวข้อราคากลับเป็นทุกกลุ่มและแสดงราคา 1 session ทั้งที่ถาม 2 hours; legacy route multi_question ผ่านจึงซ่อน defect

การแก้และสิ่งที่ควรตอบ: คืน cost จากไวยากรณ์ราคาและ student หลัง PSU; ก่อน splitter/calculator; คง 2 hours และหัวข้อ booking; ได้ 120 นาที/2 sessions/PSU 0 THB

เส้นทางเดิม: `pipeline:multi_question_splitter` → ใหม่: `pipeline:multi_question_splitter`

คำตอบเดิม:

This question contains several topics. Here are the answers separately:

Question 1: How much does it cot for a PSU stydent to play Nintendo Switch for 2 hours
The question does not specify the number of players, so both verified packages are shown.
Nintendo Switch - 1 hour (1-2 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 50 THB
- General adults: 140 THB
Nintendo Switch - 1 hour (3-4 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 100 THB
- General adults: 280 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

Question 2: how do I book
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

คำตอบใหม่:

This question contains several topics. Here are the answers separately:

Question 1: How much does it cost for a PSU student to play Nintendo Switch for 2 hours
The question does not specify the number of players, so both verified packages are shown.
Nintendo Switch - 1 hour (1-2 people)
- PSU students and staff: 0 THB (0 THB x 2 sessions)
- Requested duration: 120 minutes, charged as 2 session(s).
Nintendo Switch - 1 hour (3-4 people)
- PSU students and staff: 0 THB (0 THB x 2 sessions)
- Requested duration: 120 minutes, charged as 2 session(s).
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

Question 2: how do I book
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### MASTER-GT-EN-01849 — P1 คำบอกการจองตกหล่น

คำถาม: `What do you need to bok to play Uncharted`

สาเหตุ: bok ไม่ตรง book จึงตอบรายละเอียด Uncharted แทนขั้นตอนจอง; legacy ตรวจเพียง domain กว้าง

การแก้และสิ่งที่ควรตอบ: recover operation ใน syntax frame เดียวกัน ไม่เพิ่ม alias ของทั้งคำถามหรือชื่อเกม

เส้นทางเดิม: `pipeline:structured_game_detail_en` → ใหม่: `pipeline:rule_en`

คำตอบเดิม:

Verified English information:
Uncharted: Legacy of Thieves Collection
Genre: Action-Adventure
Overview: Uncharted is a treasure-hunting adventure game focused on climbing, exploration, puzzle solving and action scenes.
How to play: Explore locations, climb, solve puzzles, fight with firearms and progress through missions.
Available at: PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

คำตอบใหม่:

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### MASTER-GT-EN-01841 — P1 คำบอกการจองตกหล่น

คำถาม: `What do you need to ook to play The Last of Us Part I`

สาเหตุ: ook ไม่ตรง book จึงตอบว่ามีเกมบน PS5 แทนขั้นตอนจอง; legacy ตรวจเกม/หมวดจึงให้ผ่าน

การแก้และสิ่งที่ควรตอบ: recover book แบบ bounded 1 edit; ชื่อ The Last of Us Part I ไม่เปลี่ยน

เส้นทางเดิม: `pipeline:structured_game_availability_en` → ใหม่: `pipeline:rule_en`

คำตอบเดิม:

The Last of Us Part I is available on: PlayStation 5 #01-#02. Studio zone(s): PlayStation 5 Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

คำตอบใหม่:

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

## ปัญหาที่พบในการทดลองแต่ไม่ใช่ defect runtime ใหม่

- Unit candidate_C เคยใส่ fallback ชื่อผิดฟังก์ชัน (game resolver); testsพบและย้ายให้ถูกฟังก์ชันแล้ว. เก็บไฟล์ intermediateไว้ ไม่เคยใช้เป็นเว็บให้ผู้ใช้.
- หมายเหตุ control ตอนแรกใช้ reduced hits ซึ่งไม่มี coverage_status; ย้ายไป source rows ก่อน reductionแล้ว. Unit candidate_D168/168ผ่าน.
- HTTPครั้งแรก graderไม่รู้จัก mode input_guard_layout_retype ทั้งที่ expected5ข้อควรblock; แก้ grader ไม่แก้ expectation/runtime และเก็บ rawผลไว้.
- HTTP English video-policy ต่างจาก directเพราะ liveเปิดLLM/semantic. ตรวจ cleanคู่ผ่านเว็บได้ข้อความเดียวกับ noisy: เป็น safe unknown แต่เหตุผลว่าไม่มีคำแปลยังไม่ตรงช่องว่างข้อมูลนโยบาย. เก็บเป็นงานแก้คำอธิบาย ไม่อ้างว่าต้นฉบับมีนโยบายหรือเจ้าของอนุมัติ.

## ลำดับงานที่ยังพบจาก clean answers (ยังไม่รวมเป็นผลผ่านเชิงความหมาย)

1. P1 คำถามราคา “1 hour or 2 hours” ตอบเพียง60นาที. ต้องคำนวณ/แสดงแต่ละทางเลือกและตรวจ contract ทุก duration; ไม่เปลี่ยนราคา/สิทธิ์ลูกค้า.
2. P1 คำถามปุ่มเฉพาะ: Little Nightmares II OptionsมีCircleปน และอังกฤษ D-Padคืนทุกปุ่ม. ให้ explicit button identifier ชนะคำอธิบายกว้างและตรวจก่อน render. Source controlsยังรอคนเทียบเครื่องจริง.
3. P1 “What do you need to book to play [game]” อาจหมายถึงอุปกรณ์/บริการที่ต้องเลือก; ปัจจุบันทั้งclean/noisyตอบขั้นตอน. ต้องเติมgame→service mappingจากข้อมูลเดิม แล้วให้ตอบบริการพร้อมขั้นตอน หรือถามแยกเมื่อกำกวม.
4. P2 safe unknown อังกฤษเมื่อไม่มี policy ต้องระบุ missing evidence ไม่ใช่ missing translation โดยอ้างhomepageที่ไม่รองรับกฎ. ไม่เดาว่าถ่ายรูป/วิดีโอได้หรือไม่ได้.
5. P2 short/mixed layout และ valid-word collisionsยังมี tradeoff. ไม่ลด thresholdจากเคสเดียวหรือแก้คำจริง/ชื่อ/เลขทั่วทั้ง input.

## ยังรอเจ้าของ/ข้อมูลจริง

Tekken pause s03/s07ขัดกัน, RoV6.1.5.1ขาด, rulebook/version/scopeและ104หัวข้อ, official English names, PS5 controller counts/models, photo/video policy, public/food policy formal signoff, minimum age/registration fee ที่ไม่มีข้อมูล. Oracleการจองจริงยังพักตามผู้ใช้. การผ่าน testไม่ใช่การอนุมัติเหล่านี้. แบบฟอร์มคำถามเจ้าของอยู่ชุด outputs/owner_information_request_20261001_225453_48f6a2 เดิม.
