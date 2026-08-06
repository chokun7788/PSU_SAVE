# Universal Intent Pipeline Roadmap - 2026-07-18

## เป้าหมาย

เพิ่มชั้นกลางให้ chatbot เข้าใจคำถามเป็น `domain + operation` เพื่อไม่ต้องเขียนคำถาม/คำตอบทีละประโยค และเปิดทางให้ Local LLM ช่วยตีความคำถามได้มากขึ้นโดยยังคุมความถูกต้องจากข้อมูลจริง

## Flow ปัจจุบันหลังอัปเดต

1. User question
2. ส่ง `recent_history` ของ session ปัจจุบันเข้ามาพร้อมคำถาม
3. Session Context Resolver เช็กว่าคำถามเป็น follow-up หรือเปลี่ยนเรื่อง
4. ถ้าเป็น follow-up จะ rewrite คำถามให้ชัดขึ้น เช่น `แล้วแต่ละหมวดมีใครบ้าง` -> `สมาชิกใน PSU Esports แต่ละหมวดมีใครบ้าง`
5. Preprocess / normalize
6. Router เดิมเลือก route หลัก
7. Universal Intent Parser ตีความเป็น `domain/operation`
8. Universal route refine ช่วยปรับ route เมื่อมั่นใจพอ
9. Fast/Rule/Structured/RAG ทำงานตาม route
10. Formatter / validator
11. Final answer + trace + universal_intent + context_resolution

## Universal Intent Schema

```json
{
  "domain": "members",
  "operation": "group_count",
  "target": "",
  "filters": {},
  "needs": ["count_groups", "list_group_names", "count_items_per_group"],
  "answer_style": "summary_bullets",
  "confidence": 0.82,
  "method": "heuristic",
  "reason": "..."
}
```

## Domains

- `members`
- `games`
- `game_controls`
- `equipment`
- `reservation`
- `service_fee`
- `schedule`
- `competition_rules`
- `contact`
- `knowledge`
- `general`

## Operations

- `count`
- `list`
- `group_count`
- `group_list`
- `detail`
- `how_to`
- `control`
- `price_calculate`
- `schedule_lookup`
- `rule_lookup`
- `compare`
- `source_lookup`
- `availability`
- `recommendation`
- `general_answer`
- `unknown`

## สิ่งที่ทำแล้ว

- เพิ่ม `UniversalIntent` dataclass ใน `app/pipeline/schemas.py`
- เพิ่ม `app/pipeline/universal_intent.py`
- ต่อ universal intent เข้า `app/pipeline/engine.py`
- ให้ API ส่ง `universal_intent` กลับไปที่ frontend/debug
- ให้ notebook แสดง `universal_intent` ตอนใช้ `ask(...)`
- เพิ่ม `tests/smoke_test_universal_intent.py`
- ขยาย `app/session/context_resolver.py` ให้จำบริบทจาก `universal_intent`, route และข้อความคำตอบล่าสุด
- รองรับ follow-up ข้ามคำถามสำหรับสมาชิก, หมวดเกม/โซนเกม และปุ่มเกม
- ให้ web/local CLI/notebook ส่ง history ที่มี `universal_intent`, route และ `resolved_text` กลับเข้า resolver
- เพิ่ม metadata ใน log: `context_domain`, `context_operation`, `context_topic`, `context_resolution`, `universal_intent`
- เพิ่ม `app/pipeline/structured_tools.py` เป็นชั้น Structured Tool Registry + Evidence Builder รอบแรก
- ต่อ structured tool เข้า pipeline หลัง universal intent เพื่อให้คำถามที่มี facts ชัดเจนตอบจาก object กลางก่อน deterministic/RAG
- Structured tool รอบแรกครอบคลุม `members`, `games`, `game_controls`
- Structured tool รอบสองครอบคลุมเพิ่ม `equipment`, `schedule`, `reservation`, `service_fee`
- เพิ่มการ dedupe ชื่อเกมที่ต่างกันเพราะ `™`, `®`, accent และ `Standard Edition`
- ปรับ game control matcher ให้คำถามปุ่มเฉพาะตอบเฉพาะปุ่มนั้นก่อน เช่น `TEKKEN 8 ปุ่มเตะขวา`, `Mario Kart Live ปุ่มเร่งเครื่อง`
- เพิ่ม `tests/smoke_test_structured_tools.py`
- เพิ่ม cached alias index สำหรับชื่อเกม/ปุ่ม ทำให้คำถาม game controls ลดเวลาและลดโอกาสจับเกมผิด
- เพิ่ม structured equipment จาก `equipment_item_details.jsonl` เช่น `PC Zone มีอุปกรณ์อะไรบ้าง`, `Logitech G923 คืออะไร ใช้ยังไง`
- เพิ่ม structured schedule สำหรับตารางประจำ เช่น `วันจันทร์เปิดกี่โมง`, `เปิด 24 ชั่วโมงไหม`
- เพิ่ม structured reservation facts สำหรับคำถามจองหลัก เช่น วิธีจอง, เช็คอิน, payment timeout, refund, max sessions
- เพิ่ม structured service fee สำหรับคำถามราคาที่ไม่ใช่ time-range calculation และปล่อยคำถามคำนวณช่วงเวลาให้ deterministic calculator เดิม

## ตัวอย่างที่รองรับแล้ว

- `สมาชิกใน PSU Esport มีกี่หมวด` -> `members/group_count`
- `สมาชิกมีหมวดอะไรบ้าง` -> `members/group_count`
- `Nintendo มีเกมอะไรบ้าง` -> `games/list`
- `PS5 มีเกมกี่เกม` -> `games/count`
- `TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง` -> `game_controls/control`
- `ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท` -> `service_fee/price_calculate`

## ตัวอย่าง follow-up ที่รองรับแล้ว

### สมาชิก

1. User: `สมาชิกใน PSU Esport มีกี่หมวด`
2. Bot: ตอบว่าแบ่งเป็น 3 หมวด พร้อมจำนวนคน
3. User: `แล้วแต่ละหมวดมีใครบ้าง`
4. Resolver rewrite เป็น `สมาชิกใน PSU Esports แต่ละหมวดมีใครบ้าง`
5. Bot: ตอบรายชื่อสมาชิกแยกตามหมวด

### เกมในโซน

1. User: `PS5 มีเกมกี่เกม`
2. Bot: ตอบจำนวนเกมใน PlayStation 5 Zone
3. User: `แล้วมีเกมอะไรบ้าง`
4. Resolver rewrite เป็น `PlayStation 5 มีเกมอะไรบ้าง`
5. Bot: ตอบรายชื่อเกมของ PlayStation 5 Zone

### เกมเดิม

1. User: `Mario Kart Live คือเกมอะไร`
2. Bot: ตอบรายละเอียดเกม
3. User: `ปุ่มเร่งเครื่องกดอะไร`
4. Resolver rewrite เป็น `Mario Kart Live: Home Circuit ปุ่มเร่งเครื่องกดอะไร`
5. Bot: ตอบจากข้อมูลปุ่มของเกมนั้น

## Structured Tool / Evidence Builder

ชั้นนี้เป็นฐานสำหรับให้ Local LLM ใช้งานข้อมูลจริงมากขึ้นในอนาคต โดยแยกข้อมูลออกมาเป็น evidence object ก่อน เช่น:

```json
{
  "tool": "get_game_controls",
  "game": "TEKKEN 8",
  "control_count": 11,
  "returned_control_count": 1,
  "platforms": {"PlayStation / PS5": 1}
}
```

ตอนนี้ pipeline ใช้ evidence นี้เพื่อตอบแบบ deterministic ก่อน และมี Facts-only LLM Composer แบบ optional แล้ว ถ้าเปิด `PSU_FACTS_LLM_COMPOSER=1` ระบบจะส่ง evidence object เข้าโมเดลเพื่อช่วยเรียบเรียงคำตอบ แต่ยังบังคับให้ใช้เฉพาะ facts ที่ส่งเข้าไปและ fallback กลับคำตอบ structured เดิมทันทีหากโมเดล timeout หรือทำคำตอบไม่ปลอดภัย

Structured tools ที่มีตอนนี้:

- `get_member_groups`
- `get_games_by_zone`
- `get_game_detail`
- `get_game_controls`
- `get_equipment_by_zone`
- `get_equipment_item`
- `get_service_schedule`
- `get_reservation_fact`
- `calculate_service_fee`

## Session ID และ Memory

- Web: ใช้ memory เฉพาะในหน้าเว็บปัจจุบันตามที่ต้องการ ถ้า Refresh จะเริ่ม session ใหม่
- Local CLI: เปิดโปรแกรมหนึ่งครั้งจะได้ `local-cli-...` หนึ่ง session ถามกี่ครั้งก็ใช้ id เดิมจนกว่าจะ `/exit`
- Notebook: รัน cell ตั้งค่าหนึ่งครั้งจะได้ `local-ipynb-...` หนึ่ง session ถามผ่าน `ask(...)` กี่ครั้งก็ใช้ id เดิมจนกว่าจะ `new_session()` หรือ restart kernel
- Log เก่าจะถูก append เก็บไว้ตาม session id ไม่โดนลบทิ้งตอนเริ่ม session ใหม่

## ใช้ LLM ยังไง

ตอนนี้ parser ใช้ heuristic ก่อนเพื่อความเร็วและความเสถียร ถ้า confidence ต่ำและ `experimental_allow_llm=True` จะเรียก Ollama เพื่อให้ LLM ตีความ JSON intent

ตัวแปรที่เกี่ยวข้อง:

- `PSU_UNIVERSAL_INTENT_LLM=1`
- `PSU_INTENT_LLM_MODEL=qwen2.5:3b`
- `PSU_INTENT_LLM_TIMEOUT_SEC=1.2`
- `PSU_INTENT_LLM_NUM_PREDICT=180`
- `PSU_INTENT_HEURISTIC_SKIP_LLM_CONFIDENCE=0.88`

Facts-only LLM Composer:

- `PSU_FACTS_LLM_COMPOSER=1`
- `PSU_FACTS_LLM_MODEL=qwen2.5:3b`
- `PSU_FACTS_LLM_TIMEOUT_SEC=2.5`
- `PSU_FACTS_LLM_NUM_PREDICT=360`
- `PSU_OLLAMA_THINK=false`

## รอบถัดไปที่ควรทำ

1. ขยาย structured tool สำหรับ `contact`, `knowledge`, `competition_rules` แบบ facts object กลาง
2. ทำ Validator ตาม operation เช่น `group_count` ต้องมีจำนวนหมวด, `price_calculate` ต้องมีราคาและ session
3. เพิ่ม eval set สำหรับ operation ทุก domain
4. ทดลองเปิด Facts-only LLM Composer เฉพาะ local notebook/CLI ก่อน แล้วเก็บ log เปรียบเทียบว่าเรียบเรียงดีขึ้นหรือหลุด facts ไหม
5. ทำ caching/index เพิ่มสำหรับ equipment aliases และ reservation facts หาก latency เริ่มสูง
