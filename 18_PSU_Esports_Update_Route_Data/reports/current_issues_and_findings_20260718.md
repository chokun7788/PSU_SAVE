# PSU Esports Chatbot - Current Issues and Findings

วันที่อัปเดต: 2026-07-18

ไฟล์นี้สรุปปัญหาที่เจอระหว่างทดสอบ chatbot, สาเหตุที่พบ, สถานะการแก้ไข และสิ่งที่ควรทำต่อ

## สรุปสถานะรวม

ตอนนี้ระบบตอบได้ดีขึ้นในกลุ่มข้อมูลหลัก เช่น สมาชิก, เกม, ปุ่มควบคุม, อุปกรณ์, ตารางเวลา, การจอง และค่าบริการ แต่ยังมีปัญหาหลักอยู่ 4 กลุ่ม:

•    การตีความคำถามบางคำยังชนกัน เช่น `PS5` เป็นได้ทั้งเครื่อง/โซน/เกม  
•    follow-up memory ยังต้องระวังคำถามที่ใช้คำกว้าง เช่น `หมวด`, `อันนี้`, `มีอะไรบ้าง`  
•    Local LLM ยังใช้ได้บางจุด แต่ต้องคุมด้วย timeout/fallback เพราะบาง model ตอบช้าหรือว่าง  
•    ข้อมูลบางหมวดยังไม่ถูกทำเป็น structured tool ทำให้บางคำถามยังต้องพึ่ง RAG/rule มากเกินไป

## ปัญหาที่แก้แล้ว

### 1. ถาม `สมาชิก PSU Esport มีกี่หมวด` แล้วตอบรายชื่อคนทั้งหมด

อาการ:

•    ถามแบบนับหมวด แต่ระบบตอบเป็นรายชื่อสมาชิกทุกคน  
•    โดยเฉพาะหลังจากเคยถามเรื่องสมาชิกมาก่อนใน session เดียวกัน

สาเหตุ:

•    `context_resolver` เห็นคำว่า `หมวด` แล้ว rewrite เป็น `แต่ละหมวดมีใครบ้าง`  
•    priority ของ follow-up กว้างเกินไป ยังไม่แยก `กี่หมวด` กับ `มีใครบ้าง`

สิ่งที่แก้แล้ว:

•    ปรับ `app/session/context_resolver.py`  
•    ให้ `กี่หมวด / กี่กลุ่ม / มีกี่หมวด` ตอบจำนวนหมวดก่อน  
•    ให้ `มีใครบ้าง / รายชื่อ / แต่ละหมวดมีใคร` ค่อยตอบรายชื่อสมาชิก  
•    เพิ่ม regression test ใน `tests/smoke_test_session_context.py`

สถานะ: แก้แล้ว

### 2. ถาม `เกมใน PS5 มีอะไรมั่ง` แล้วตอบอุปกรณ์ PlayStation 5

อาการ:

•    ผู้ใช้ถามรายชื่อเกมใน PS5  
•    ระบบตอบว่า PlayStation 5 Zone มีเครื่อง PlayStation 5 Slim กี่เครื่อง

สาเหตุ:

•    route เห็น `PS5 + มีอะไร` แล้วเข้า `equipment` ก่อน  
•    universal intent ยังไม่รู้ว่า `มีอะไรมั่ง` เป็นคำกลุ่มเดียวกับ `มีอะไรบ้าง`

สิ่งที่แก้แล้ว:

•    ปรับ `app/pipeline/router.py` ให้ pattern `เกมใน/เกมบน/เกมของ + platform` เข้า `games/list` ก่อน  
•    ปรับ `app/pipeline/universal_intent.py` เพิ่มคำ `มีอะไรมั่ง`, `มีไรบ้าง`, `มีไรมั่ง` เป็น operation `list`  
•    เพิ่ม regression test ใน `tests/smoke_test_universal_intent.py`

สถานะ: แก้แล้ว

### 3. Notebook แสดง `...` เหมือนคำตอบถูกตัด

อาการ:

•    ใน notebook เห็น `...` ทำให้เหมือน chatbot ตอบไม่ครบ  
•    เจอบ่อยเวลา `ask()` return dict/debug object ยาวท้าย cell

สาเหตุ:

•    คำตอบจริงของ pipeline ไม่ได้ถูกตัด  
•    Jupyter/VS Code Notebook ย่อการแสดงผล object ยาว เช่น dict, DataFrame, trace

สิ่งที่แก้แล้ว:

•    ปรับ `notebooks/04_local_hybrid_chat_debug.ipynb`  
•    ให้ `ask()` และ `ask_with_composer()` ไม่ return dict เป็นค่า default  
•    เพิ่ม `ask_full(...)` สำหรับดูคำตอบเต็ม  
•    ถ้าต้องการ debug row ให้ใช้ `return_row=True`

สถานะ: แก้แล้วใน notebook 04

### 4. `ask_with_composer(...)` ทำให้เข้าใจผิดว่า composer เปลี่ยนคำตอบ

อาการ:

•    ถาม `สมาชิก PSU Esport มีกี่หมวด` ด้วย `ask_with_composer(...)` แล้วได้คำตอบรายชื่อคน  
•    ดูเหมือน Local LLM Composer ทำคำตอบผิด

สาเหตุ:

•    ปัญหาจริงเกิดก่อน composer คือ context resolver rewrite คำถามผิด  
•    composer แค่รับ draft answer ที่ผิดไปเรียบเรียงต่อ

สิ่งที่แก้แล้ว:

•    แก้ priority ใน context resolver  
•    เพิ่ม test กันไม่ให้คำถามนับหมวดกลายเป็นรายชื่อคน

สถานะ: แก้แล้ว

### 5. ถามปุ่มเกมแล้วตอบไม่ครบหรือตอบผิดเกม

อาการ:

•    ถามปุ่มเฉพาะ เช่น `Mario Kart Live ปุ่มเร่งเครื่องกดอะไร` แล้วมีโอกาสไปโดน Mario Kart 8  
•    ถามปุ่มเฉพาะแล้วบางทีตอบหลายปุ่มเกินไป

สาเหตุ:

•    ชื่อเกมคล้ายกัน  
•    alias ของเกมและปุ่มยังไม่แม่นพอ  
•    route/vector อาจดึงข้อมูลของเกมใกล้เคียงมา

สิ่งที่แก้แล้ว:

•    เพิ่ม cached alias index ใน `app/pipeline/structured_tools.py`  
•    ปรับ game controls ให้ตอบปุ่มเฉพาะก่อน ถ้าผู้ใช้ถาม action/button เฉพาะ  
•    เพิ่ม smoke test ใน `tests/smoke_test_game_controls.py`

สถานะ: แก้แล้วในเคสหลัก แต่ยังควรเพิ่ม test ตามเกมใหม่ ๆ เรื่อย ๆ

### 6. ถามราคาแบบช่วงเวลาแล้วไม่คำนวณ

อาการ:

•    เช่น `ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท`  
•    เคยตอบเป็น policy การจองแทน หรือบอกราคา 1 ชั่วโมงโดยไม่คำนวณ 2 ชั่วโมง

สาเหตุ:

•    route ระหว่าง reservation/service_fee ชนกัน  
•    structured service fee มีโอกาสแย่งคำถามที่ควรให้ deterministic calculator คำนวณ

สิ่งที่แก้แล้ว:

•    กันไม่ให้ structured service fee แย่ง time-range calculation  
•    ให้ deterministic calculator รับเคสช่วงเวลา เช่น 09:00-11:00, 09:00-12:00  
•    เพิ่ม regression test ใน `tests/smoke_test_booking_price_regression.py`

สถานะ: แก้แล้วในเคสที่ทดสอบ

## ปัญหาที่ยังต้องระวัง / ยังควรพัฒนาต่อ

### 1. คำถามกว้างมากยังมีโอกาสตีความผิด

ตัวอย่าง:

•    `มีอะไรบ้าง`  
•    `อันนี้คืออะไร`  
•    `เล่นยังไง`  
•    `แต่ละหมวดมีอะไร`  
•    `เกมนี้ปุ่มอะไร`

ความเสี่ยง:

•    ถ้าไม่มี session context จะไม่รู้ว่าผู้ใช้หมายถึงอะไร  
•    ถ้ามี session context แต่ context ล่าสุดไม่ใช่เรื่องที่ผู้ใช้ต้องการ อาจ inherit ผิดเรื่อง

แนวทางต่อ:

•    เพิ่ม context confidence  
•    ถ้า context ไม่ชัด ให้ถามกลับสั้น ๆ แทนการเดา  
•    เพิ่ม test สำหรับ topic shift เช่น จากเกมไปจอง จากสมาชิกไปอุปกรณ์

### 2. Structured tools ยังไม่ครอบคลุมทุก domain

ตอนนี้ structured tools ครอบคลุม:

•    members  
•    games  
•    game_controls  
•    equipment  
•    schedule  
•    reservation  
•    service_fee

ยังควรเพิ่ม:

•    contact  
•    knowledge  
•    competition_rules  
•    events/news  
•    how-to-use equipment แบบละเอียด  
•    policies/penalties แยกเป็น facts object

ผลกระทบ:

•    domain ที่ยังไม่ structured จะพึ่ง fast/rule/RAG มากกว่า  
•    ถ้า retrieval เลือก chunk ผิด คำตอบอาจผิดหรือไม่ตรงคำถาม

### 3. Local LLM ยังไม่ได้ใช้เต็มศักยภาพ

ตอนนี้ใช้ได้ใน 3 จุดหลัก:

•    Universal Intent LLM: ช่วยตี intent เป็น JSON เมื่อ heuristic ไม่มั่นใจ  
•    Facts-only Composer: ช่วยเรียบเรียงคำตอบจาก facts ที่ structured tools ดึงมา  
•    General/RAG LLM Fallback: ตอบคำถามทั่วไปหรือสรุปจาก retrieved context

ข้อจำกัด:

•    ถ้าใช้ `qwen3:4b` อาจเจอ thinking ยาวจน final answer ว่าง  
•    ถ้า timeout ต่ำเกินไป จะ fallback บ่อย  
•    ถ้า timeout สูงเกินไป ระบบจะช้า

แนวทางต่อ:

•    ใช้ `qwen2.5:3b` เป็น default สำหรับ local chat/debug  
•    ค่อยทดลอง model อื่นด้วย eval set เดียวกัน  
•    เก็บ log ว่า LLM ถูกใช้ตรงไหนและช่วยดีขึ้นจริงไหม

### 4. Composer ต้องคุมไม่ให้แต่ง facts

ความเสี่ยง:

•    LLM อาจเพิ่มชื่อเกม ราคา จำนวนคน หรือ source เอง  
•    อาจเปลี่ยนคำตอบจาก intent เดิม เช่นถาม count แต่ตอบ list

สิ่งที่มีแล้ว:

•    ใช้ FACTS_JSON + DRAFT_ANSWER  
•    reject ถ้า prompt leak, response ว่าง, source line หาย/เปลี่ยน  
•    fallback กลับ structured answer เดิม

สิ่งที่ควรเพิ่ม:

•    validator ตาม operation เช่น `group_count` ต้องมีจำนวนหมวด แต่ไม่ควรมีรายชื่อคนทั้งหมด  
•    validator สำหรับ `games/list` ต้องมี zone และรายชื่อเกม  
•    validator สำหรับ `price_calculate` ต้องมี session/hour/price

### 5. RAG/Vector ยังมีโอกาสเลือกข้อมูลใกล้เคียงแต่ไม่ตรง

อาการที่เคยเจอ:

•    ถามกติกาเรื่องหนึ่ง แต่ดึง fact card อีกเรื่อง  
•    ถามหลายเกม แล้วตอบบางเกมหรือเอาข้อมูลหมวดเดียวกันมาตอบแทน  
•    ถามเกมที่ไม่มีข้อมูล แล้วบางทีวนไปเกมอื่น

แนวทางต่อ:

•    เพิ่ม reranker หรือ strict intent filter ก่อนเลือก fact card  
•    ทำ structured competition rules แยกตาม game + intent  
•    เพิ่ม eval set สำหรับคำถามกฎ/การแข่งขัน  
•    ถ้า confidence ต่ำ ให้ตอบว่ายังไม่พบข้อมูลตรงคำถาม มากกว่าดึงข้อมูลใกล้เคียง

### 6. ข้อมูลบางเกม/บางปุ่มยังอาจไม่ครบ

ตัวอย่าง:

•    บางเกมมีข้อมูลว่าอยู่ในโซนไหน แต่ไม่มีปุ่ม  
•    บางเกมมีในกติกาแข่งขัน แต่ไม่มีใน catalog เกมให้เล่น  
•    บางเกม user ถามจากความรู้ทั่วไป เช่น Minecraft แต่ฐาน PSU อาจไม่มีข้อมูลให้เล่นจริง

แนวทางต่อ:

•    แยกสถานะเกมเป็น `available_in_studio`, `competition_only`, `general_known`, `no_verified_data`  
•    เวลาถามว่าเกมคืออะไร ถ้าไม่มีใน PSU แต่อยากให้ LLM อธิบายทั่วไป ต้องบอกแยกชัดว่าเป็นความรู้ทั่วไป ไม่ใช่ข้อมูลบริการของศูนย์  
•    เพิ่ม game metadata กลาง เช่น genre, platform, availability, controls_available

### 7. Vercel ไม่สามารถรัน Local Model ในตัวเอง

ข้อเท็จจริง:

•    Vercel deploy เว็บ/API ได้  
•    แต่ไม่ได้เอา Ollama/local model จากเครื่องเราไปรันบน Vercel ด้วย  
•    ถ้าจะให้คนอื่นใช้ model ได้โดยไม่เปิดเครื่อง ต้องใช้ hosted inference หรือ server/GPU/VPS แยก

ผลกระทบ:

•    โหมด Local LLM ใช้ได้ดีสำหรับ local notebook/CLI  
•    บน Vercel ควรใช้เฉพาะ rule/RAG/structured หรือเรียก API model ภายนอก

แนวทางต่อ:

•    แยก config `local` กับ `production`  
•    production ใช้ structured/RAG เป็นหลัก  
•    ถ้าจะใช้ LLM จริงบน production ให้เลือก hosted provider หรือ server ที่รัน Ollama ได้

### 8. Notebook / eval output อาจทำให้เข้าใจผิด

อาการ:

•    Jupyter ย่อ output เป็น `...`  
•    DataFrame แสดงแถวไม่ครบ  
•    dict/debug trace ยาวเกินแล้วถูกตัด

แนวทางต่อ:

•    ใช้ `ask_full(...)` สำหรับดูคำตอบเต็ม  
•    ถ้าจะดู row/debug ให้เซฟเป็น JSON/JSONL แล้วเปิดไฟล์  
•    อย่าใช้ output cell เป็นแหล่งตรวจคำตอบเดียวสำหรับเคสยาว


### 9. ยังเพิ่งเริ่มใช้ LLM ช่วยคัดกรอง route/tool

สถานะล่าสุด:

•    เพิ่ม `app/pipeline/llm_tool_router.py` เป็น LLM Tool Router แบบ optional แล้ว  
•    เปิดด้วย `PSU_LLM_TOOL_ROUTER=1`  
•    ใช้หลัง `universal_intent.py` และก่อน structured/fast/rule/RAG  
•    หน้าที่คือแนะนำ action เช่น `structured`, `fast_path`, `rulebase`, `retrieval`, `vector`, `general_llm`, `rag_llm`, `clarification`, `no_answer`

ข้อจำกัด/guard ที่ตั้งไว้:

•    ยังเป็น advisory เป็นหลัก ไม่ใช่ให้ model คุม pipeline ทั้งหมด  
•    ถ้า heuristic/structured มั่นใจสูง จะไม่เรียก LLM router เพื่อลด latency  
•    ไม่อนุญาตให้ LLM router โยนคำถาม PSU-specific ไป `general_llm` แบบมั่ว ๆ  
•    route ความเสี่ยงกลาง/สูงที่มั่นใจสูง เช่นราคา/จอง/กติกา จะไม่ถูก override ง่าย ๆ  
•    ตอนนี้ refine route จริงเฉพาะเคสปลอดภัย เช่น general/unknown -> retrieval domain เช่น `competition_rules`, `contact`, `knowledge`

สิ่งที่ควรทำต่อ:

•    เก็บ log เปรียบเทียบตอนเปิด/ปิด `PSU_LLM_TOOL_ROUTER`  
•    เพิ่ม eval set สำหรับคำถามกำกวมว่าควรเข้า RAG หรือ general  
•    เพิ่ม validator ว่าคำแนะนำของ tool router ทำให้คำตอบดีขึ้นจริง ไม่ใช่แค่เปลี่ยน route  

### 10. เพิ่ม Capability Registry และ Decision Artifact แล้ว

สถานะล่าสุด:

•    เพิ่ม `app/pipeline/capability_registry.py` เพื่อประกาศความสามารถของระบบเป็นรายการกลาง เช่น `structured.members`, `structured.games`, `fast.price_calculator`, `retrieval.hybrid_guarded`, `llm.general_answer`, `clarification.ask_user`  
•    เพิ่ม `Policy Filtering + Ranking` ให้ candidate แต่ละตัวมี score, status และ reason ว่าถูกเลือกหรือถูก reject เพราะอะไร  
•    เพิ่ม `app/pipeline/decision_artifact.py` เพื่อรวมผลตัดสินใจเป็น artifact เดียวใน `PipelineAnswer.decision_artifact`  
•    Decision Artifact ตอนนี้เก็บ intent, route, tool router trace, selected candidate, rejected candidates, policy, execution plan, final mode, evidence count และ source ids  
•    เพิ่ม artifact เข้า web debug response, chat log metadata, local notebook 04 และ mixed mode tester  

ข้อจำกัดที่ยังเหลือ:

•    Ranking ยังเป็น heuristic เป็นหลัก ยังไม่ได้ใช้ LLM ช่วย rerank evidence จริง ๆ  
•    Candidate ที่เลือกยังเป็นตัวอธิบาย/ตรวจสอบการตัดสินใจเป็นหลัก ส่วน execution order จริงยังใช้ pipeline เดิมเพื่อไม่ให้ระบบแกว่ง  
•    ต้องใช้ eval set วัดต่อว่า artifact ช่วย debug คำตอบผิดได้ดีแค่ไหน และควรให้ policy มีสิทธิ์ override execution เพิ่มตรงไหนบ้าง  

## สิ่งที่ควรทำต่อเป็นลำดับ

1. เพิ่ม structured tool สำหรับ `competition_rules` แบบแยก game + intent
2. เพิ่ม validator ตาม operation เพื่อกันตอบผิดชนิด เช่น count แต่ตอบ list
3. ทำ eval set แยกตาม domain: members, games, controls, equipment, reservation, service_fee, competition_rules, general
4. เพิ่ม alias/synonym จากคำถามจริงที่ user พิมพ์ผิดหรือใช้ภาษาพูด เช่น `มีอะไรมั่ง`, `เกมใน`, `เกมบน`, `โมบ้า`
5. เก็บ log ว่าแต่ละคำถามตอบจาก `structured`, `fast`, `rule`, `rag`, `vector`, `llm` เพื่อดูจุดที่ผิดบ่อย
6. ทดลอง Local LLM หลาย model ด้วยคำถามชุดเดียวกัน แล้วเทียบ latency/accuracy
7. แยก behavior ระหว่าง local กับ Vercel production ให้ชัด

## ไฟล์สำคัญที่เกี่ยวข้อง

•    `app/session/context_resolver.py` - memory/follow-up rewrite  
•    `app/pipeline/router.py` - route ชั้นแรก  
•    `app/pipeline/universal_intent.py` - domain/operation intent  
•    `app/pipeline/structured_tools.py` - structured facts answer  
•    `app/pipeline/facts_composer.py` - optional LLM composer  
•    `app/pipeline/engine.py` - main answer pipeline  
•    `notebooks/04_local_hybrid_chat_debug.ipynb` - local debug notebook  
•    `tests/smoke_test_session_context.py` - test memory/follow-up  
•    `tests/smoke_test_universal_intent.py` - test intent/route  
•    `tests/smoke_test_structured_tools.py` - test structured tools  
•    `tests/smoke_test_game_controls.py` - test game controls  
•    `tests/smoke_test_booking_price_regression.py` - test booking/price
