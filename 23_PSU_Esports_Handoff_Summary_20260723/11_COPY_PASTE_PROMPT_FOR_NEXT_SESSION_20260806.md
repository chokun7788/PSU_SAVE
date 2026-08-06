# Copy-Paste Prompt For Next Session

## ใช้ Prompt นี้เปิด session ใหม่

```text
คุณกำลังรับช่วงโปรเจกต์ PSU Esports Chatbot ต่อจาก session เดิม

โปรเจกต์นี้เป็น local-first chatbot สำหรับ PSU Esports Studio - Phuket และมีการพัฒนาต่อเนื่องถึงวันที่ 06/08/2026

ก่อนตอบหรือแก้โค้ด กรุณาอ่านไฟล์นี้ทั้งหมดก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\10_CURRENT_PROJECT_ALL_IN_ONE_20260806.md

จากนั้นอ่าน daily logs ล่าสุดตามลำดับ:
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs\2026-08-03.md
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs\2026-08-04.md
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs\2026-08-05.md
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs\2026-08-06.md

อ่านลำดับงานที่ควรทำต่อและรูปแบบ Daily Log ที่:
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\12_NEXT_WORK_AND_DAILY_LOG_GUIDE_20260806.md

ถ้าต้องการดู architecture/flow แบบละเอียด ให้อ่าน:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\docs\38_current_chatbot_full_process_flow_20260803.md

ภาพ Flow:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\docs\current_chatbot_full_process_flow_th_20260803.png

Source หลักที่ต้องแก้และทดสอบจริง:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

Daily logs:
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs

Handoff folder:
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723

Requirement ที่ต้องรักษา:
- ตอบเป็นภาษาไทย
- answer-first และไม่เวิ่นเว้อ
- ถ้าไม่มีข้อมูลจริงของ PSU Esports Studio - Phuket ห้ามเดา
- ถ้าคำตอบมาจาก rule/fast/structured/RAG ห้ามบอกว่าเป็น LLM
- ถ้ากำกวมและ evidence ไม่พอ ให้ถามกลับหรือ no-answer
- ไม่ใช้ git และไม่ยุ่ง Vercel/deploy ถ้าผู้ใช้ไม่ได้สั่ง
- อย่าแก้ test ให้ผ่านง่าย ต้องแก้ root cause
- ถ้าคำตอบผิด ให้ตรวจ mode/route/intent/target/source/trace ก่อนแก้
- งานที่มีสาระต้องอัปเดต daily log ของวันนั้น โดยเพิ่มสรุปล่าสุดไว้ด้านบน
- ไม่ต้องบอกผู้ใช้ทุกครั้งว่าเขียน daily log หรือรัน test ถ้าไม่ได้ถาม

สถานะสำคัญปัจจุบัน:
- Default Local LLM: scb10x/typhoon2.5-qwen3-4b
- Current game catalog: 42 unique games
- Per-request LLM max calls: 2
- LLM max concurrency: 1
- Compound max workers: 2
- Complex Query Planner timeout cap: 4 วินาที
- Global request timeout: 20 วินาที
- Structured/Fast path เป็นแกนหลัก
- Local LLM ใช้แบบ gated สำหรับ Query Planner, Intent review, optional Tool Router/Composer, General fallback และ Shadow Critic
- มี Boundary Guard, Ambiguity Gate, Candidate Scoring, Margin Threshold, Tool Preconditions, Answer Contract, Bounded Repair และ Final Hard Veto
- Complex compound ใช้ Complexity Gate + dependency plan; simple independent compound ใช้ bounded parallel
- Reference เช่น เกมนั้น/เครื่องนั้น/อันเดิม ต้อง resolve จาก evidence หรือถามกลับ ห้ามเดา

ปัญหาหลักที่ยังเหลือ:
1. ยังไม่ได้รัน full 1,500+/1,600 evaluation หลัง latest changes วันที่ 05/08
2. Concurrency guard ยังเป็น in-process ไม่ใช่ distributed queue
3. ยังต้องทำ multi-user load test และ session isolation
4. Ollama request ยัง hard-cancel ไม่ได้ทุกกรณี
5. Game controls บาง source ยังต้อง manual verify
6. Vector backend ยังไม่ใช่ semantic embedding เต็มรูปแบบ
7. Chatbot ยังบอกวิธีจอง ไม่ได้ทำ booking transaction จริง
8. ข่าว/กิจกรรมล่าสุดยังรอเพิ่ม

ลำดับงานที่ควรเสนอให้ทำต่อ:
1. รัน full evaluation 1,500+/1,600 cases หลังการแก้ล่าสุด โดยแยก No-LLM และ Typhoon
2. วิเคราะห์ failure จากคำตอบจริง แยก wrong route, wrong target, missing subanswer, unsupported claim, source mismatch, timeout และ unnecessary LLM call
3. แก้ correctness regression ที่พบจากผล eval โดยแก้ root cause และเพิ่ม regression test
4. ทำ multi-user load test อย่างน้อย 5 sessions พร้อมกัน วัด queue wait, latency และ session isolation
5. ออกแบบ shared queue/worker ถ้าต้องรองรับหลาย process
6. ตรวจ control sources ที่ยังเป็น secondary/manual verify
7. พิจารณา semantic embedding/retrieval หลัง structured correctness นิ่งแล้ว

เมื่อผู้ใช้สั่งให้ลงมือทำ:
- ตรวจ source code และ reproduce ปัญหาก่อนแก้
- แก้ logic/data จริง ไม่แก้ expected result ให้ผ่านง่าย
- รัน test ให้เหมาะกับความเสี่ยง
- เก็บผลที่วัดได้ เช่น pass rate, average, P95, max และ LLM calls
- อัปเดต Daily Log ของวันที่ทำงาน โดยเพิ่ม Latest Update ไว้ด้านบน
- ถ้ามี blocker ให้ระบุสิ่งที่ลองแล้วและข้อมูลที่ยังขาด ห้ามเดา

รูปแบบ Daily Log ต้องมีอย่างน้อย:
- สรุปสิ่งที่ทำ
- ปัญหาและ root cause
- สิ่งที่เพิ่มหรือแก้
- เทคนิค/วิธีที่ใช้
- ไฟล์หรือข้อมูลสำคัญที่เกี่ยวข้อง
- ผลทดสอบ/ผลวัด
- ข้อจำกัดและงานที่ยังเหลือ
- งานที่ควรทำต่อ

เมื่อตรวจไฟล์ครบแล้ว ให้ตอบฉันก่อนว่า:
1. เข้าใจโปรเจกต์และเป้าหมายว่าอย่างไร
2. Current flow ตั้งแต่ User Input ถึง Final Answer เป็นอย่างไร
3. Local LLM, RAG, rerank, structured และ fast path ถูกใช้ตรงไหน
4. ข้อมูลปัจจุบันและ test status เป็นอย่างไร
5. ปัญหาและ blocker ที่ยังเหลือเรียงตามความสำคัญคืออะไร
6. ถ้าจะทำงานต่อ ควรเริ่มจากอะไรและเพราะอะไร

อย่าเพิ่งแก้โค้ดจนกว่าจะอ่านไฟล์ข้างต้นและสรุปสถานะกลับมาก่อน
```

## ถ้ามีเวลาน้อยมาก

ให้ session ใหม่อ่านเพียงไฟล์นี้ก่อน:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\10_CURRENT_PROJECT_ALL_IN_ONE_20260806.md
```

แล้วค่อยอ่าน daily log วันที่ล่าสุดเมื่อจะลงมือแก้จริง

รายละเอียดลำดับงานและ Daily Log template:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723\12_NEXT_WORK_AND_DAILY_LOG_GUIDE_20260806.md
```
