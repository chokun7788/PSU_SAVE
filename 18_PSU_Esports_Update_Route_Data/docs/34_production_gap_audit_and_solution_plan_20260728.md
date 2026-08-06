# PSU Esports Chatbot Production Gap Audit and Solution Plan - 2026-07-28

เอกสารนี้สรุปปัญหาที่ยังติดของ PSU Esports Chatbot ณ วันที่ 2026-07-28 โดยอ้างอิงจาก repo ปัจจุบัน:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

โฟกัสของเอกสารนี้คือ local chatbot / local LLM เท่านั้น ไม่รวม Vercel/deploy

## อ่านก่อน: คำอธิบายชื่อเฉพาะและไฟล์ในเอกสารนี้

ส่วนนี้ทำไว้เพื่อให้อ่านเอกสารนี้ง่ายขึ้น ถ้าเจอชื่อไฟล์ ชื่อเทคนิค หรือคำเฉพาะ ให้ดูความหมายจากหัวข้อนี้ก่อน

### คำที่เกี่ยวกับโครงสร้างโปรเจกต์

| คำ / ชื่อ | ความหมายแบบง่าย |
|---|---|
| repo | โฟลเดอร์โปรเจกต์หลักที่เก็บโค้ดและข้อมูลทั้งหมดของ chatbot |
| source หลัก | โฟลเดอร์ที่แก้ระบบจริงตอนนี้ คือ `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data` |
| daily log | ไฟล์บันทึกว่าวันนี้ทำอะไรไปแล้ว อยู่ที่ `C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs` |
| docs | โฟลเดอร์เอกสารอธิบายระบบ เช่น flow, audit, roadmap |
| app | โฟลเดอร์โค้ดหลักของ chatbot |
| data | โฟลเดอร์ข้อมูลจริง/ข้อมูล curated/eval/vector ที่ chatbot ใช้ตอบ |
| tests | โฟลเดอร์ test สำหรับเช็คว่าแก้แล้วระบบไม่พัง |
| notebooks | โฟลเดอร์ notebook สำหรับลองถาม chatbot/debug แบบ interactive |

### นามสกุลไฟล์ที่เจอบ่อย

| นามสกุล | คืออะไร |
|---|---|
| `.md` | Markdown file ใช้เขียนเอกสาร อ่านเป็นหัวข้อ/ตาราง/list ได้ง่าย |
| `.py` | ไฟล์ Python เป็นโค้ดที่ระบบรันจริง |
| `.json` | ไฟล์ข้อมูลแบบ JSON มักเป็น object ใหญ่หรือ config หนึ่งก้อน |
| `.jsonl` | JSON Lines คือ 1 บรรทัด = 1 record เหมาะกับข้อมูลหลายรายการ เช่น เกม 1 แถว, ปุ่ม 1 แถว, คำถาม eval 1 แถว |
| `.sqlite3` | ฐานข้อมูล SQLite แบบไฟล์เดียว ใช้เก็บ chat log/local history ได้ |
| `.png` / `.svg` | ไฟล์รูปภาพ `.png` เป็นภาพ bitmap, `.svg` เป็นภาพ vector |

ตัวอย่าง `.jsonl`:

```json
{"id":"game_detail_tekken_8","game":"TEKKEN 8","category":"games"}
{"id":"game_detail_valorant","game":"VALORANT","category":"games"}
```

แปลว่าไฟล์นี้มี 2 records แต่ละบรรทัดเป็นข้อมูล 1 ชุด

### ไฟล์ข้อมูลหลักที่พูดถึงในเอกสารนี้

| ไฟล์ | ใช้ทำอะไร |
|---|---|
| `data/curated/game_item_details.jsonl` | ข้อมูลรายละเอียดเกมที่จัดระเบียบแล้ว เช่น ชื่อเกม แนวเกม วิธีเล่นโดยสรุป โซนที่เล่นได้ |
| `data/curated/our_games_scraped_details.jsonl` | รายชื่อเกมที่ดึง/สรุปจากหน้า Our Games ของเว็บ แต่อาจยังขาด field บางอย่าง |
| `data/curated/game_title_aliases.jsonl` | รายการชื่อเรียก/ชื่อสะกดผิด/ชื่อย่อของเกม เช่น `valo` -> `VALORANT`, `tekken` -> `TEKKEN 8` |
| `data/curated/game_control_facts.jsonl` | ข้อมูลปุ่มควบคุมเกม เช่น TEKKEN 8 ปุ่ม Square คือหมัดซ้าย |
| `data/control_game_split/ps5/*.jsonl` | ไฟล์ปุ่มควบคุมแยกตามเกมฝั่ง PS5 |
| `data/control_game_split/nintendo/*.jsonl` | ไฟล์ปุ่มควบคุมแยกตามเกมฝั่ง Nintendo Switch |
| `data/curated/equipment_item_details.jsonl` | ข้อมูลอุปกรณ์ เช่น Gaming PC, monitor, keyboard, PS5, Nintendo Switch, cockpit, VR |
| `data/curated/curated_facts.jsonl` | facts ทั่วไปที่จัดไว้แล้ว เช่น วิธีจอง กฎการใช้งาน ช่องทางติดต่อ เงื่อนไขบางอย่าง |
| `data/curated/curated_facts_service_fee_2026_aliases.jsonl` | ข้อมูลเสริมเกี่ยวกับคำเรียก/alias ของราคาและ service fee |
| `data/curated/member_profiles.jsonl` | ข้อมูลสมาชิก/บุคลากร/ตำแหน่งที่ระบบใช้ตอบคำถามเกี่ยวกับสมาชิก |
| `data/competition_rules/competition_rule_fact_cards.jsonl` | fact cards กติกาการแข่งขันแบบสรุปเป็นข้อ ๆ |
| `data/competition_rules/competition_rule_fact_cards*.jsonl` | fact cards กติกาหลายรอบ/หลายชุดที่เคยเพิ่มหรือซ่อม |
| `data/curated/curated_competition_rules.jsonl` | chunks กติกาการแข่งขันที่ใช้ค้นหา/อ้างอิง |
| `data/vector/psu_hybrid_vector_index.json` | index สำหรับค้นหาข้อมูลแบบ vector/lexical hybrid |
| `data/eval/real_usage_golden_v1.jsonl` | ชุดคำถามใช้งานจริงที่คาดหวังคำตอบไว้ ใช้เป็น golden test |
| `data/eval/user_question_bank_400.jsonl` | ชุดคำถาม 400 เคสสำหรับวัดคุณภาพระบบ |
| `data/routing/routing_eval_real_usage.jsonl` | ชุดคำถามสำหรับเช็คว่า router ส่งคำถามไปหมวดถูกไหม |
| `data/eval/audits/.../summary.json` | สรุปผล audit/eval รอบเก่า เช่น score เฉลี่ยและ issue ที่เจอ |

### ไฟล์โค้ดหลักที่เกี่ยวข้อง

| ไฟล์ | หน้าที่ |
|---|---|
| `app/pipeline/engine.py` | ตัวคุม flow หลักของ chatbot ตั้งแต่รับคำถามจนได้คำตอบสุดท้าย |
| `app/pipeline/preprocess.py` | ทำความสะอาดคำถาม เช่น normalize ภาษา/ช่องว่าง/รูปแบบคำ |
| `app/pipeline/router.py` | เดา route/หมวดหลักของคำถาม เช่น games, reservation, service_fee |
| `app/pipeline/universal_intent.py` | สรุป intent กลาง เช่น domain คืออะไร operation คืออะไร target คืออะไร |
| `app/pipeline/structured_tools.py` | tools ที่ตอบจากข้อมูล structured เช่น เกม ปุ่ม อุปกรณ์ สมาชิก ราคา |
| `app/pipeline/game_title_correction.py` | แก้ชื่อเกม/จับ alias/จับ typo เช่น `over cook` ให้หา Overcooked ได้ |
| `app/pipeline/tool_preconditions.py` | ด่านตรวจว่า tool นั้นควรถูกใช้ไหม เช่น ถามปุ่มห้ามไปใช้ game catalog tool |
| `app/pipeline/capability_registry.py` | รายชื่อ capability ที่ระบบเลือกได้ เช่น structured.games, fast.price_calculator |
| `app/pipeline/llm_tool_router.py` | ตัวช่วยเลือก tool ด้วย LLM เฉพาะเคสที่เปิดใช้และจำเป็น |
| `app/pipeline/facts_composer.py` | ให้ LLM ช่วยเรียบเรียงจาก facts ที่มีเท่านั้น ห้ามแต่งข้อมูลใหม่ |
| `app/pipeline/retrieval.py` | ค้นข้อมูล curated แบบพื้นฐาน |
| `app/pipeline/vector_retrieval.py` | ค้นข้อมูลจาก vector index |
| `app/pipeline/hybrid_retrieval.py` | รวมการค้นหลายแบบ เช่น lexical + vector |
| `app/pipeline/validator.py` | ตรวจคำตอบหลังสร้างเสร็จว่าตรงคำถามไหม หลุดหมวดไหม มี source พอไหม |
| `app/pipeline/formatter.py` | จัดรูปแบบคำตอบให้อ่านง่ายและคุม style |
| `app/pipeline/decision_artifact.py` | รวมหลักฐานการตัดสินใจของ pipeline เช่น route, candidate, source, validation |
| `app/pipeline/ambiguity_gate.py` | ด่านจับคำถามกำกวม ถ้าไม่ชัดให้ถามกลับหรือให้ preview |
| `app/pipeline/llm_health.py` | ตัวดูสุขภาพ LLM ถ้า timeout/ตอบว่างบ่อย จะเปิด circuit breaker |
| `app/calculator/service_fee.py` | คำนวณราคา service fee/PC/PS5/Nintendo/Cockpit/VR |
| `app/core/source_registry.py` | registry ของแหล่งข้อมูลที่ระบบเชื่อถือ ตอนนี้มีหลัก ๆ เรื่อง service fee/PC |
| `app/session/context_resolver.py` | จัดการคำถามต่อเนื่อง เช่น user ถามต่อว่า "แล้วราคาเท่าไหร่" ต้องรู้ว่าหมายถึงเรื่องก่อนหน้า |
| `app/session/chat_logger.py` | เขียน log การถามตอบลง JSONL/SQLite/Postgres |

### คำที่เกี่ยวกับ flow ของ chatbot

| คำ | ความหมายแบบง่าย |
|---|---|
| pipeline | ลำดับขั้นตอนทั้งหมดที่คำถามต้องผ่านก่อนออกเป็นคำตอบ |
| route | หมวดทางเดินของคำถาม เช่น `games`, `service_fee`, `reservation`, `equipment` |
| intent | เจตนาของคำถาม เช่น อยากรู้ราคา, อยากจอง, อยากดูปุ่ม, อยากดูรายชื่อเกม |
| domain | หมวดความรู้ เช่น games, equipment, members |
| operation | การกระทำที่ user ต้องการ เช่น lookup, calculate, compare, list, book |
| target | สิ่งที่ user ถามถึง เช่น `TEKKEN 8`, `PC`, `Nintendo Switch` |
| entity | ข้อมูลสำคัญที่ดึงจากคำถาม เช่น วัน เวลา ระยะเวลา กลุ่มผู้ใช้ ชื่อเกม |
| session context | บริบทจากบทสนทนาก่อนหน้า ใช้ตอบคำถามต่อเนื่อง |
| follow-up | คำถามต่อจากคำถามก่อน เช่น "แล้วจองยังไง" |
| mode | ชื่อ path ที่ตอบจริง เช่น `pipeline:structured_game_controls` |
| trace | log รายละเอียดว่าคำถามผ่าน step ไหน ตัดสินใจอะไร |
| confidence | คะแนนความมั่นใจของ route/intent/answer |

### คำที่เกี่ยวกับข้อมูลและแหล่งอ้างอิง

| คำ | ความหมายแบบง่าย |
|---|---|
| curated data | ข้อมูลที่คัด/จัดรูปแบบไว้ให้ chatbot ใช้ตอบ ไม่ใช่ raw text ล้วน |
| raw data | ข้อมูลดิบที่ยังไม่ได้จัดให้ใช้ง่าย |
| fact | ข้อเท็จจริง 1 เรื่อง เช่น PC สำหรับ PSU Student and Staff ราคา 0 บาท/ชั่วโมง |
| fact card | fact ที่เขียนเป็นการ์ดสั้น ๆ มักใช้กับกติกาการแข่งขัน |
| source_url | URL หรือ path ที่บอกว่าข้อมูลมาจากไหน |
| source_id | id ของแหล่งข้อมูล เช่น `service_fee_image_2026` ใช้ตรวจสอบซ้ำได้ |
| source_ids | list ของ source_id ที่คำตอบนั้นอ้างอิง |
| source registry | ทะเบียนกลางของแหล่งข้อมูลที่เชื่อถือได้ |
| Source Contract | กฎว่าคำตอบบางหมวดต้องมีแหล่งข้อมูลจริงและ source_id เสมอ |
| trust_level | ระดับความน่าเชื่อถือของ source เช่น official, user_confirmed, local_fact_update |
| last_verified_at | วันที่ตรวจแล้วว่าข้อมูลยังถูกต้อง |
| coverage_status | สถานะว่าข้อมูลครบไหม เช่น complete, partial, unknown |

### คำที่เกี่ยวกับ routing / guard / validator

| คำ | ความหมายแบบง่าย |
|---|---|
| heuristic | rule ที่เขียนไว้ตรง ๆ ไม่ใช้ LLM เช่น เจอคำว่า "ราคา" ให้ไปหมวด service_fee |
| heuristic router | router ที่ใช้ rule/keyword/score ในการเลือกหมวด |
| structured tools | ตัวตอบจากข้อมูลเป็นตาราง/record ชัดเจน เช่น ราคา ปุ่ม รายชื่อเกม |
| fast path | ทางลัดตอบเร็วสำหรับคำถามที่ deterministic เช่น คำนวณราคา |
| rule path / rulebase | คำตอบจากกฎที่เขียนไว้ ไม่ต้องใช้ LLM |
| candidate | ตัวเลือก route/tool ที่ระบบกำลังพิจารณา |
| Candidate Scoring | ให้คะแนนหลาย candidate ก่อนเลือก ไม่เลือกจาก keyword เดียวทันที |
| Margin Threshold | ถ้าคะแนนอันดับ 1 กับอันดับ 2 ใกล้กันเกินไป ให้ถือว่ายังไม่มั่นใจ |
| Negative Keyword Guard | กฎกันผิดทาง เช่น ถ้ามีคำว่า "ปุ่ม" ห้ามตอบเป็นรายชื่อเกม |
| Operation-First | ให้คำกริยา/ความต้องการหลักชนะหมวดกว้าง เช่น "ราคา" ต้องไปคำนวณราคา |
| Ambiguity Gate | ด่านจับคำถามกำกวม เช่น `PC มีอะไรบ้าง` อาจหมายถึงเกม/อุปกรณ์/ราคา/จอง |
| Clarification | การถามกลับเพื่อให้ user เลือกความหมายที่ต้องการ |
| Hybrid Clarification Preview | ถามกลับพร้อม preview สั้นจากข้อมูลจริง |
| Answer-Type Contract | กฎว่าคำถามแต่ละแบบต้องตอบเป็นรูปแบบไหน เช่น ถามราคาต้องมีตัวเลขราคา |
| Answer Validator | ตัวตรวจคำตอบหลังสร้างเสร็จว่าตรงคำถามและไม่หลุดหมวด |
| Safe No-answer Guard | ด่านกันไม่ให้ระบบเดาเมื่อไม่มีข้อมูลจริง |

### คำที่เกี่ยวกับ RAG / Vector / LLM

| คำ | ความหมายแบบง่าย |
|---|---|
| RAG | Retrieval-Augmented Generation คือค้นข้อมูลก่อน แล้วค่อยเอาข้อมูลนั้นไปตอบ |
| retrieval | การค้นข้อมูลจากฐานความรู้ |
| vector | วิธีแทนข้อความเป็นตัวเลขเพื่อค้นหาความใกล้เคียง |
| vector index | ฐานข้อมูล/ไฟล์ที่เก็บ vector ของเอกสารไว้ค้น |
| semantic embedding | vector ที่เข้าใจความหมายของประโยคมากกว่าแค่ตัวอักษร |
| lexical search | ค้นจากคำที่ตรงกันหรือใกล้กันแบบตัวอักษร |
| hybrid retrieval | ค้นแบบผสม เช่น lexical + vector + filter |
| reranker | ตัวจัดอันดับผลค้นอีกครั้งว่าอันไหนควรขึ้นก่อน |
| `local_hash_char_ngram_v1` | vector แบบ local ที่ใช้ hash จากตัวอักษร/คำ ไม่ใช่ semantic embedding จริง |
| LLM | โมเดลภาษา เช่น Qwen/Typhoon ใช้ช่วยบางจุด แต่ไม่ควรใช้ตอบข้อมูล PSU โดยเดาเอง |
| local LLM | LLM ที่รันในเครื่อง local ผ่าน Ollama หรือเครื่องผู้ใช้ ไม่ใช่ cloud API |
| facts composer | LLM ที่ใช้เรียบเรียงจาก facts ที่ระบบค้นเจอแล้วเท่านั้น |
| general fallback | ให้ LLM ตอบเฉพาะคำถามทั่วไปที่ไม่ใช่ข้อมูลเฉพาะ PSU |
| circuit breaker | ระบบพักการเรียก LLM ชั่วคราวเมื่อ timeout/ตอบว่างบ่อย |
| timeout | เวลาสูงสุดที่รอ model ตอบ |
| empty response | model ไม่ส่งคำตอบสุดท้ายกลับมา |

### คำที่เกี่ยวกับ eval / test / production

| คำ | ความหมายแบบง่าย |
|---|---|
| eval | การประเมินคุณภาพ chatbot ด้วยชุดคำถาม |
| golden eval | ชุดคำถามที่มีคำตอบ/route ที่คาดหวัง ใช้เป็นคำตอบมาตรฐาน |
| smoke test | test เล็ก ๆ ที่รันเร็วเพื่อเช็คว่า path สำคัญยังทำงาน |
| regression | bug เดิมที่เคยแก้แล้วต้องไม่กลับมาอีก |
| question bank | คลังคำถามจำนวนมากสำหรับทดสอบ |
| audit | การตรวจคุณภาพแบบละเอียดหลัง eval |
| production | สภาพที่พร้อมให้ user จริงใช้งาน ไม่ใช่แค่ demo |
| public-facing | user ภายนอกหรือคนทั่วไปใช้งานได้ |
| internal demo | ใช้โชว์/ลองภายใน ยังรับความเสี่ยงได้มากกว่า production |
| monitoring | การดูพฤติกรรมระบบหลังใช้งานจริง เช่น ตอบช้าไหม ผิด route ไหม |
| dashboard | หน้ารวมตัวเลข monitoring |
| review queue | คิวคำถามที่ควรให้คนมาช่วยตรวจ เช่น คำตอบไม่มั่นใจหรือ validator เตือน |
| p50 / p95 latency | เวลาในการตอบที่ 50% / 95% ของคำถามทำได้ภายในเวลานั้น |
| no-answer rate | สัดส่วนคำถามที่ระบบตอบว่าไม่มีข้อมูล |
| fallback rate | สัดส่วนที่ระบบต้องไหลไปทางสำรอง เช่น RAG/LLM/no-answer |
| P0 / P1 / P2 | ระดับความสำคัญของงาน P0 = ทำก่อนสุด, P1 = ถัดมา, P2 = polish/เสริม |

### คำที่เป็น field ในข้อมูล

| field | หมายถึงอะไร |
|---|---|
| `id` | รหัสของ record นั้น ๆ |
| `category` | หมวดข้อมูล เช่น games, equipment, reservation |
| `game` | ชื่อเกม |
| `title` | ชื่อหัวข้อหรือชื่อที่ใช้แสดง |
| `aliases` | ชื่อเรียกอื่น/ชื่อย่อ/ชื่อสะกดผิดที่ควรจับเป็นเรื่องเดียวกัน |
| `genre` | แนวเกม |
| `summary_th` | สรุปภาษาไทย |
| `how_to_play_th` | วิธีเล่น/ภาพรวมการเล่นภาษาไทย |
| `zones` | โซนที่เล่นได้ เช่น PC Zone, PlayStation 5 Zone |
| `platform` | แพลตฟอร์ม เช่น PS5, Nintendo Switch, PC |
| `platform_key` | key สั้น ๆ ของ platform เช่น `ps5`, `nintendo`, `pc` |
| `button` | ปุ่มบนจอย/คีย์บอร์ด |
| `action_th` | ความหมายของปุ่มภาษาไทย |
| `source_file` | ไฟล์ต้นทางที่ record นั้นมาจาก |
| `source_url` | ลิงก์/ที่มาของข้อมูล |
| `source_ids` | source id ที่อ้างอิง |
| `quantity` | จำนวนอุปกรณ์ |
| `affiliation` | หน่วยงาน/สังกัดของสมาชิก |
| `priority` | ค่าน้ำหนัก/ความสำคัญ ใช้ช่วยเรียงผล |

## สรุปสั้นก่อน

ถ้าจะเอาไปใช้งานจริงตอนนี้ ระบบไม่ได้ติดที่ "ไม่มี pipeline" แล้ว แต่ติดที่ "ข้อมูล, source contract, route edge cases, semantic retrieval, monitoring, และ UX ตอนถามกลับ" ยังไม่ครบพอสำหรับ production

คะแนนแบบไม่อวย:

- ใช้ demo / internal test: ประมาณ 75/100
- ใช้งานจริงแบบ public-facing production: ประมาณ 65/100

เหตุผลที่ยังไม่ควรให้สูงกว่านี้:

- ข้อมูลบางหมวดยังไม่ครบ โดยเฉพาะ game controls, booking edge cases, schedule exception, source id ของทุก fact
- route ดีขึ้นมาก แต่ยังมีโอกาสหลุดในคำถามสั้น กำกวม หรือชื่อเกมที่ชนกัน
- local LLM ยังไม่เสถียรพอเป็นตัวตัดสินหลักทุกเคส
- vector ตอนนี้เป็น local hash char n-gram ไม่ใช่ semantic embedding จริง
- log มีแล้ว แต่ยังไม่ถึงระดับ monitoring dashboard / review queue แบบ production

## ตัวเลขจาก repo ปัจจุบัน

ตัวเลขนี้เป็น snapshot จากไฟล์จริงใน repo วันที่ 2026-07-28

| ส่วน | ไฟล์หลัก | จำนวนที่พบ |
|---|---|---:|
| Game detail curated | `data/curated/game_item_details.jsonl` | 36 rows |
| Our games scraped | `data/curated/our_games_scraped_details.jsonl` | 31 rows |
| Game title aliases | `data/curated/game_title_aliases.jsonl` | 36 rows |
| Game control facts | `data/curated/game_control_facts.jsonl` | 357 rows |
| Equipment details | `data/curated/equipment_item_details.jsonl` | 16 rows |
| Curated facts | `data/curated/curated_facts.jsonl` | 42 rows |
| Service fee alias facts | `data/curated/curated_facts_service_fee_2026_aliases.jsonl` | 4 rows |
| Member profiles | `data/curated/member_profiles.jsonl` | 25 rows |
| Competition fact cards base | `data/competition_rules/competition_rule_fact_cards.jsonl` | 19 rows |
| Competition fact cards all round files | `data/competition_rules/competition_rule_fact_cards*.jsonl` | 166 rows |
| Vector index docs | `data/vector/psu_hybrid_vector_index.json` | 671 docs |
| Real usage golden eval | `data/eval/real_usage_golden_v1.jsonl` | 24 cases |
| User question bank | `data/eval/user_question_bank_400.jsonl` | 400 cases |
| Routing real usage eval | `data/routing/routing_eval_real_usage.jsonl` | 115 cases |

ผล audit เก่าที่สำคัญ:

- `data/eval/audits/20260721_tool_preconditions_v1_400_audit/summary.json`
- total 400 cases
- average score 8.716/10
- bad 3 cases
- needs_review 58 cases
- usable 91 cases
- good 248 cases
- issue ใหญ่:
  - `missing_source_id`: 110 cases
  - `safe_decline_but_not_useful`: 94 cases
  - `candidate_execution_mismatch`: 46 cases
  - `no_answer_for_supported_question`: 32 cases
  - `wrong_domain_or_source`: 16 cases

แปลแบบตรง ๆ:

ระบบตอบได้ค่อนข้างดีในชุดทดสอบเดิม แต่ production risk ยังอยู่ที่ source/evidence, no-answer quality, และ route/execution mismatch

## 1. ข้อมูลขาดอะไรบ้าง

### 1.1 Game Catalog

ไฟล์หลัก:

- `data/curated/game_item_details.jsonl`
- `data/curated/our_games_scraped_details.jsonl`
- `data/curated/game_title_aliases.jsonl`

มีอะไรแล้ว:

- มีชื่อเกม
- มี alias หลายเกม
- มี genre / summary / how_to_play สำหรับ `game_item_details`
- มี source_url
- มี zones ใน `game_item_details`

ยังขาด / ยังไม่ครบ:

- `our_games_scraped_details.jsonl` ขาด `how_to_play_th` ทุกแถว 31/31
- `our_games_scraped_details.jsonl` ขาด `zones` ทุกแถว 31/31
- ชื่อเกมมี variant เยอะ เช่น `TEKKEN 8` กับ `TEKKEN 8 Standard Edition`
- ยังไม่มี canonical service mapping ที่ชัดแบบหนึ่งเดียว เช่น เกมนี้อยู่ zone ไหนแน่, ใช้จอง service key ไหน, มีอุปกรณ์อะไรเกี่ยวข้อง
- ยังไม่มี field สถานะ availability เช่น `available`, `temporarily_unavailable`, `removed`, `unknown`
- ยังไม่มี source contract กลางต่อเกม เช่น `source_ids` ที่ link กับ source registry

สิ่งที่ควรเติม:

- `canonical_game_id`
- `canonical_title`
- `display_title`
- `aliases`
- `platforms`
- `zones`
- `service_keys`
- `genres`
- `summary_th`
- `how_to_play_th`
- `availability_status`
- `source_ids`
- `last_verified_at`
- `confidence_level`

### 1.2 Game Controls

ไฟล์หลัก:

- `data/curated/game_control_facts.jsonl`
- `data/control_game_split/ps5/*.jsonl`
- `data/control_game_split/nintendo/*.jsonl`

มีอะไรแล้ว:

- มี control facts 357 rows
- ครอบคลุมเกมประมาณ 26 ชื่อเกมหลักหลัง normalize จาก `game` field
- มี platform, platform_key, button, action_th/action_en หลายแถว
- มี source_file/source_url
- มี structured path สำหรับตอบปุ่ม

เกมที่มีข้อมูลปุ่มแล้วโดยประมาณ:

- Animal Crossing: New Horizons
- Call of Duty: Modern Warfare III
- EA Sports FC 24
- FINAL FANTASY XVI
- God of War Ragnarok
- Gran Turismo 7
- Hogwarts Legacy
- It Takes Two
- Little Nightmares II
- Luigi's Mansion 3
- Mario Kart 8 Deluxe
- Mario Kart Live: Home Circuit
- Marvel's Spider-Man 2
- Monster Hunter Rise
- Moving Out
- NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS
- Overcooked!
- Resident Evil 4 (Remake)
- Resident Evil Village
- Super Mario Odyssey
- Super Smash Bros. Ultimate
- TEKKEN 8
- The Last of Us Part I
- The Last of Us Part II
- The Legend of Zelda: Breath of the Wild
- Uncharted: Legacy of Thieves Collection

กลุ่มที่ยังเสี่ยงว่า mapping ไม่ครบ / ต้อง canonicalize เพิ่ม:

- Beat Saber
- Call of Duty: Warzone
- Counter-Strike 2
- Fortnite
- Horizon Call of the Mountain
- League of Legends
- Mario Party Superstars
- New Super Mario Bros. U Deluxe
- Nintendo Switch Sports
- PUBG: BATTLEGROUNDS
- Ring Fit Adventure
- VALORANT
- เกมที่เป็น edition/    เช่น `TEKKEN 8 Standard Edition`, `Gran Turismo 7: Standard Edition`, `The Last of Us Part I / Part II`

ข้อควรระวัง:

- บางเกมมี control facts แต่ชื่อไม่ตรง catalog จึงทำให้ lookup หลุดได้
- บางคำถามใช้คำว่า "เล่นยังไง" ซึ่งอาจหมายถึง "วิธีจองเพื่อเข้าเล่น" หรือ "ปุ่มควบคุม" ต้องใช้ operation-first + context ให้ดี
- PC games เช่น VALORANT/CS2/PUBG/LoL อาจไม่มีปุ่ม console เพราะเป็น keyboard/mouse ต้องมี schema แยกสำหรับ PC controls หรือ no-control-data ที่ชัด

สิ่งที่ควรเติม:

- `canonical_game_id`
- `platform`
- `controller_type`
- `control_context`
- `button`
- `action_th`
- `action_en`
- `short_answer_th`
- `source_ids`
- `last_verified_at`
- `coverage_status`: `complete`, `partial`, `not_available`, `unknown`

### 1.3 Equipment

ไฟล์หลัก:

- `data/curated/equipment_item_details.jsonl`

มีอะไรแล้ว:

- มี 16 rows
- มี item, zone, what_th, how_to_use_th, use_cases_th
- มี source_url ส่วนใหญ่

ยังขาด / ยังไม่ครบ:

- `quantity` ขาด 3 rows
- ยังไม่มี unique source id ต่อ item
- ยังไม่มี spec แบบ structured ลึก เช่น CPU/GPU/RAM/monitor Hz/จำนวน controller/รุ่น headset
- ยังไม่มีความสัมพันธ์ item -> service -> game -> booking
- ยังไม่มี policy เรื่องอุปกรณ์เสีย, การแจ้งปัญหา, การย้ายอุปกรณ์, การคืนอุปกรณ์ แบบ source contract

สิ่งที่ควรเติม:

- `equipment_id`
- `display_name`
- `zone`
- `service_key`
- `quantity`
- `specs`
- `included_with_booking`
- `user_can_adjust`
- `damage_policy`
- `source_ids`
- `last_verified_at`

### 1.4 Service Fee / Price

ไฟล์หลัก:

- `app/calculator/service_fee.py`
- `app/core/source_registry.py`
- `data/curated/curated_facts_service_fee_2026_aliases.jsonl`

มีอะไรแล้ว:

- ราคา service fee จากรูป official service fee 2026
- ราคา PC ที่ user ยืนยันแล้ว:
  - PSU Student and Staff: 0 บาท / 1 ชั่วโมง
  - PSU Alumni / General Student: 25 บาท / 1 ชั่วโมง
  - General Adult: 70 บาท / 1 ชั่วโมง
- มี source registry 2 entries:
  - `service_fee_image_2026`
  - `pc_service_fee_local_update_20260727`

ยังขาด / ยังไม่ครบ:

- source registry ครอบคลุมเฉพาะ service fee/PC ยังไม่ครอบคลุมทุก fact
- ต้องตรวจ group mapping ให้ครบ เช่น PSU Student, Staff, Alumni, General Student, General Adult, คนทั่วไป, นักศึกษา, บุคลากร
- ต้องมี calculation contract ชัดเจน เช่น 30 นาที/1 ชั่วโมง/session/หลายคน/หลายรอบ
- ต้องแยก service ที่ราคาเป็นคนละ model เช่น Nintendo 1-2 persons กับ 3-4 persons
- ต้องมี no-answer เมื่อถาม promotion/discount/เงื่อนไขพิเศษที่ไม่มีข้อมูล

สิ่งที่ควรเติม:

- `price_id`
- `service_key`
- `user_group_key`
- `duration_unit`
- `duration_min`
- `price_thb`
- `calculation_formula`
- `source_ids`
- `effective_from`
- `effective_to`
- `last_verified_at`

### 1.5 Booking / Reservation

ไฟล์หลัก:

- `data/curated/curated_facts.jsonl`
- `app/pipeline/structured_tools.py`
- `app/calculator/service_fee.py`

มีอะไรแล้ว:

- ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง
- จองได้สูงสุด 3 sessions
- ชำระเงินหลังจอง ถ้าไม่ชำระใน 10 นาทีจะถูกยกเลิก
- มีข้อมูลว่าหลังจองแล้วไม่สามารถยกเลิกได้จาก user context ก่อนหน้า
- มี structured booking selection ตอบวิธีจอง

ยังขาด / ยังไม่ครบ:

- ขั้นตอนจองแบบละเอียดทุก step ยังควรทำเป็น structured source แยก
- ข้อจำกัดการยกเลิก/เปลี่ยนเวลา/คืนเงิน ต้องมี source id และ wording ที่ตายตัว
- ยังไม่มี booking field contract เช่น service, date, time, duration, number of people, user group, payment slip
- ยังไม่มี edge cases เช่น จองผิดวัน, จองผิด zone, ลืมจ่าย, จ่ายแล้วแต่ระบบไม่ขึ้น, walk-in ได้ไหม, ไปช้ากี่นาทีได้ไหม
- ยังไม่มี policy สำหรับ fully booked / unavailable / maintenance

สิ่งที่ควรเติม:

- `booking_policy_id`
- `policy_type`
- `condition`
- `answer_th`
- `required_fields`
- `related_service_keys`
- `source_ids`
- `last_verified_at`

### 1.6 Schedule / Opening Hours

ไฟล์หลัก:

- `app/calendar/service_calendar.py`
- `data/curated/curated_facts.jsonl`

มีอะไรแล้ว:

- มี service calendar logic
- มี Thai holiday source URL ใน code
- มี structured schedule path

ยังขาด / ยังไม่ครบ:

- ต้องยืนยันเวลาเปิด-ปิดจริงของ PSU Esports Studio - Phuket แบบ source contract
- ต้องมีวันหยุดเฉพาะศูนย์, ปิดปรับปรุง, event day, exam period, special booking
- ต้องมี service-specific availability เช่น PC เปิดแต่ VR ไม่เปิด
- ต้องมีคำตอบแบบ "วันนี้/พรุ่งนี้" ที่อิง timezone Asia/Bangkok เสมอ

สิ่งที่ควรเติม:

- `schedule_rule_id`
- `day_of_week`
- `open_time`
- `close_time`
- `service_keys`
- `exception_dates`
- `source_ids`
- `last_verified_at`

### 1.7 Members

ไฟล์หลัก:

- `data/curated/member_profiles.jsonl`

มีอะไรแล้ว:

- มี 25 profiles
- มี group, name, role, source_url
- มี structured members สำหรับถามตำแหน่งแล้วตอบว่าใครทำตำแหน่งนั้น

ยังขาด / ยังไม่ครบ:

- `affiliation` ขาด 13 rows
- ยังไม่มี `source_ids`
- ยังไม่มี role canonicalization เช่น ประธาน/รองประธาน/ฝ่าย/ผู้ดูแล/เจ้าหน้าที่/นักวิชาการคอมพิวเตอร์
- ยังไม่มี policy ว่าถ้าถามเบอร์ติดต่อส่วนตัว/email ส่วนตัวต้องตอบยังไง
- ยังไม่มี relation กับ operation อื่น เช่น "ใครดูแลการจอง", "ใครดูแลอุปกรณ์", ถ้าไม่มีข้อมูลต้อง no-answer

สิ่งที่ควรเติม:

- `member_id`
- `name_th`
- `role_title`
- `role_key`
- `group`
- `affiliation`
- `responsibility_scope`
- `public_contact_allowed`
- `source_ids`
- `last_verified_at`

### 1.8 Competition Rules

ไฟล์หลัก:

- `data/competition_rules/competition_rule_fact_cards*.jsonl`
- `data/curated/curated_competition_rules.jsonl`
- `data/ground_truth/competition_by_game_v2/*.jsonl`

มีอะไรแล้ว:

- มี curated competition rules 104 chunks
- มี fact cards หลายรอบรวมประมาณ 166 cards
- มี ground truth หลายชุด เช่น 228, 184, challenger 369
- มี fast path / fact card retrieval สำหรับกติกา

ยังขาด / ยังไม่ครบ:

- ต้อง consolidate fact cards หลายรอบให้เป็น source of truth เดียว ไม่ให้ rule ซ้ำ/ชนกัน
- ต้องมี version ต่อ tournament/game/rule document
- ต้องมี conflict resolution เช่น card เก่ากับ card ใหม่ตอบไม่ตรงกัน
- ต้องมี no-answer เมื่อถามกติกาที่ไม่มีในเอกสาร เช่น โปรแกรมช่วยเล่นบางแบบ ถ้าไม่มีข้อกำหนดจริงต้องไม่เดา

สิ่งที่ควรเติม:

- `rule_id`
- `game_key`
- `tournament_key`
- `rule_topic`
- `answer_th`
- `evidence_text`
- `source_doc_id`
- `version`
- `effective_date`
- `supersedes`
- `source_ids`

### 1.9 Source Contract / Source Registry

ไฟล์หลัก:

- `app/core/source_registry.py`

มีอะไรแล้ว:

- source registry มี 2 records:
  - `service_fee_image_2026`
  - `pc_service_fee_local_update_20260727`

ยังขาด / ยังไม่ครบ:

- ยังไม่ครอบคลุม games, controls, equipment, booking, schedule, members, competition rules
- eval ยังเจอ `missing_source_id` 110 cases
- หลาย hit มี `source_url` แต่ไม่มี `source_id` ที่ตรวจสอบแบบ registry ได้
- validator ยัง enforce source contract เข้มเฉพาะบางหมวด

สิ่งที่ควรเติม:

- source registry กลางแบบ data file เช่น `data/knowledge/source_registry.jsonl`
- ทุก fact ต้องอ้าง `source_ids`
- ทุก source ต้องมี trust level
- validator ต้อง reject/warn เมื่อ route เสี่ยงแต่ไม่มี source id

ตัวอย่าง schema:

```json
{
  "source_id": "game_catalog_our_games_page_20260728",
  "category": "games",
  "title": "Our Games Page",
  "source_url": "https://esports.phuket.psu.ac.th/Services/our-games",
  "source_type": "official_page",
  "trust_level": "official",
  "updated_at": "2026-07-28",
  "origin": "PSU Esports Studio - Phuket website",
  "description": "Game catalog source for current studio games."
}
```

### 1.10 Eval / Test Data

มีอะไรแล้ว:

- 400 question bank
- 24 real usage golden cases
- 115 routing real usage cases
- หลาย smoke tests ครอบคลุม pipeline สำคัญ

ยังขาด / ยังไม่ครบ:

- real usage golden ยังน้อยเกินไปสำหรับ production
- ยังไม่มี adversarial set สำหรับชื่อเกมคล้ายกัน / คำถามสั้น / typo หนัก / compound ข้ามหมวด
- ยังไม่มี per-domain acceptance threshold เช่น price ต้อง 99%, booking ต้อง 95%, games 90%
- ยังไม่มี test จาก log จริงหลัง user ใช้งาน

เป้าหมายที่ควรมี:

- real usage golden 100-200 cases
- adversarial routing 200 cases
- source contract eval 100 cases
- no-answer eval 100 cases
- latency eval p50/p95 แยก stage

## 2. ปัญหา route หลุด จะแก้ยังไง

ปัญหา:

- คำถามสั้นมาก เช่น `PC มีอะไรบ้าง`, `Mario เล่นยังไง`, `call of เล่นยังไง`
- คำว่า `เล่นยังไง` มี 2 ความหมาย คือ "วิธีเข้าใช้/วิธีจอง" หรือ "วิธีเล่นเกม/ปุ่มควบคุม"
- ชื่อเกมบางชื่อเป็น family หรือ partial เช่น `call of`, `mario`, `resident`
- คำถามบางอันมีหลาย intent ในประโยคเดียว เช่น ราคา + เกม + ปุ่ม

solution:

1. Route Confusion Matrix
   - เก็บผล route จริงทุกคำถาม
   - เทียบ expected route จาก human/golden eval
   - ดูว่า route ไหนชนกันบ่อย เช่น games vs controls, booking vs controls, equipment vs games

2. Candidate Scoring ต่อเนื่อง
   - ไม่เลือก route เดียวทันที
   - สร้าง candidates หลายอัน เช่น `structured.games`, `structured.game_controls`, `structured.reservation`
   - เลือกเมื่อ top score ชนะอันดับสองมากพอ

3. Margin Threshold
   - ถ้า top score กับ second score ใกล้กัน ให้เข้า ambiguity gate
   - ตัวอย่าง top 0.74, second 0.70 = ไม่ควรตอบทันที
   - ตัวอย่าง top 0.91, second 0.42 = ตอบได้

4. Operation-First Routing
   - คำกริยา/operation สำคัญกว่าหมวดกว้าง
   - `ราคา`, `กี่บาท`, `จอง`, `ปุ่ม`, `กดอะไร`, `เปิดกี่โมง` ต้องดันเข้าหมวดเฉพาะก่อน

5. Negative Keyword Guard
   - ถ้าถามปุ่ม ห้ามตอบ catalog เกม
   - ถ้าถามราคา ห้ามตอบรายชื่อเกม
   - ถ้าถามจอง ห้ามตอบยกเลิก เว้นแต่มีคำว่ายกเลิก
   - ถ้าถาม member ห้ามตอบ overview

6. Answer-Type Contract
   - route ต้องระบุ answer type เช่น `price`, `list`, `control`, `booking_step`, `schedule`, `person_lookup`
   - answer validator ตรวจว่า output มีรูปแบบตรง answer type

7. Cross-Check Route กับ Answer
   - หลังตอบแล้ว validator ดูว่า answer หลุดหมวดไหม
   - ถ้าผิด ให้ retry path อื่น 1 ครั้ง
   - ถ้ายังผิด ให้ safe no-answer หรือ clarification ไม่วนไม่รู้จบ

8. Ambiguity Gate v2
   - ถ้าคำถามกว้างหรือ target ไม่พอ ให้ถามกลับ
   - แต่ควรมี preview จากข้อมูลจริง ไม่ถามโล่ง ๆ

## 3. ปัญหา model ต่างกัน Qwen2.5 เร็วแต่ผิด / Typhoon ถูกแต่ช้า จะแก้ยังไง

แนวคิดหลัก:

ไม่ควรใช้ model เดียวทำทุกอย่าง ให้แยก model ตามหน้าที่

ควรใช้ LLM เฉพาะจุดนี้:

- intent review เฉพาะเคส heuristic ไม่มั่นใจ
- tool router เฉพาะเคส broad/mixed/ambiguous
- facts composer เฉพาะเอาข้อมูลจริงมาเรียบเรียง ห้ามแต่ง facts
- general fallback เฉพาะคำถามทั่วไปที่ไม่ใช่ PSU-specific

ไม่ควรใช้ LLM เป็นตัวหลักของ:

- ราคา
- จอง
- ตารางเวลา
- รายชื่อเกม
- ปุ่มควบคุมจากฐานข้อมูล
- member lookup
- competition rules ที่มี fact cards

วิธีแก้ model difference:

1. Model-by-role
   - Qwen2.5 3B: ใช้กับ intent JSON / tool routing เพราะเร็ว
   - Typhoon: ใช้เฉพาะ hard case หรือ offline eval เพราะช้า
   - ไม่ให้ Typhoon อยู่ใน critical path ทุกคำถาม

2. Strict JSON Contract
   - LLM intent ต้องตอบ JSON เท่านั้น
   - มี enum ของ domain/operation
   - ถ้า parse ไม่ได้ให้ทิ้งผล LLM แล้ว fallback heuristic

3. Timeout Budget ต่อ stage
   - intent LLM: 1.5-3 วินาที
   - tool router LLM: 1.5-3 วินาที
   - facts composer: 3-5 วินาที
   - general LLM: 8-12 วินาที เฉพาะ general

4. Circuit Breaker
   - ตอนนี้มี `app/pipeline/llm_health.py`
   - ถ้า timeout/empty response เกิน threshold ให้หยุดเรียก model ชั่วคราว
   - ต้องทำให้ข้อความ fallback เป็น user-friendly กว่านี้ ไม่โชว์ config technical ใน public

5. Cache
   - cache intent result ของคำถามซ้ำ
   - cache normalized entity/alias
   - cache vector retrieval

6. Shadow Eval
   - ให้ Qwen/Typhoon ตอบ intent แบบ offline
   - เทียบกับ golden labels
   - เอาเคสที่ Qwen ผิดมาปรับ rule หรือ prompt

7. Distill กลับเป็น rule
   - ถ้าเจอ pattern ซ้ำจาก log ให้แก้ deterministic rule
   - อย่าเพิ่ม LLM call ถ้าแก้ด้วย rule ได้

## 4. หลายส่วนยังไม่ใช่ vector ใช่ไหม

ใช่ หลายส่วนตั้งใจไม่ใช้ vector และไม่ควรบังคับให้เป็น vector ทั้งหมด

ส่วนที่ไม่ควรใช้ vector เป็นตัวหลัก:

- ราคา: ต้องคำนวณ deterministic
- booking policy: ต้องตอบจาก structured facts
- schedule: ต้องใช้ calendar/rule
- member lookup: ต้อง exact lookup
- game controls: ควร exact/structured ก่อน vector
- source contract: ต้อง exact
- validation: ต้อง rule/contract

ส่วน vector ตอนนี้:

- อยู่ที่ `data/vector/psu_hybrid_vector_index.json`
- backend คือ `local_hash_char_ngram_v1`
- doc_count 671
- ไม่ใช่ semantic embedding จริง

ข้อจำกัด:

- เหมาะกับ typo/คำใกล้/substring บางแบบ
- ไม่เข้าใจความหมายลึกเท่า embedding model
- ถ้าคำถาม semantic มาก เช่น "อยากเล่นแนวยิงกับเพื่อน 5 คน" อาจหาได้ไม่ดีเท่า embedding

solution:

1. เพิ่ม semantic embedding backend
   - ใช้ local embedding model เช่น bge-m3, multilingual-e5, หรือ nomic-embed-text
   - ต้อง benchmark ภาษาไทยก่อนเลือก

2. ทำ Hybrid Retrieval จริง
   - lexical score + semantic score + metadata filters
   - exact alias boost สำหรับชื่อเกม/service
   - source trust boost สำหรับ official/user-confirmed

3. Metadata Filter
   - ถ้า route = controls ให้ค้นเฉพาะ game_controls ก่อน
   - ถ้า route = service_fee ให้ค้นเฉพาะ service_fee
   - ถ้า route = competition_rules ให้ filter game/tournament/rule_topic

4. Reranker
   - ใช้ lightweight rerank heuristic ก่อน
   - ถ้ามี resource ค่อยใช้ reranker model

5. Retrieval Eval
   - ทำชุดคำถาม retrieval 200 cases
   - metric: top1 hit ถูกไหม, top3 มี source ถูกไหม, answer จาก hit ตรงไหม, no-answer เมื่อไม่มีข้อมูลทำได้ไหม

## 5. ขาดอะไรอีกสำหรับ production

### 5.1 Data Governance

ยังต้องมี:

- source registry กลาง
- schema validation ทุกไฟล์ data
- last verified date
- owner ของแต่ละข้อมูล
- policy ว่าข้อมูลเก่าเกินกี่วันต้องเตือน
- changelog ของข้อมูล

### 5.2 Admin Update Flow

ยังต้องมี:

- วิธีให้คนดูแลเติมข้อมูลแบบไม่แก้ code
- template สำหรับเพิ่มเกม, ปุ่ม, ราคา, อุปกรณ์, schedule
- validation ก่อน publish local knowledge
- preview ว่าข้อมูลใหม่จะตอบคำถามแบบไหน

### 5.3 Answer Quality Policy

ยังต้องมี:

- tone/style template ภาษาไทย
- direct answer first
- no-answer template แยกหมวด
- clarification template แยกหมวด
- source display policy
- ห้ามบอกว่าเป็น LLM เมื่อคำตอบมาจาก rule/structured/RAG

### 5.4 Security / Privacy

ยังต้องมี:

- ไม่ log ข้อมูลส่วนตัวเกินจำเป็น
- mask เบอร์โทร/email/รหัสนักศึกษา ถ้า user พิมพ์มา
- retention policy ว่าเก็บ log กี่วัน
- admin access control ถ้ามี dashboard

### 5.5 Regression and Release Gate

ยังต้องมี:

- minimum pass threshold ต่อหมวด
- run smoke tests + golden eval ก่อนส่งใช้งาน
- block release ถ้า price/booking/source contract fail
- report diff หลังเพิ่มข้อมูล

### 5.6 Observability

ยังต้องมี:

- latency per stage
- fallback rate
- LLM timeout rate
- no-answer rate
- clarification rate
- validator rejection rate
- top missing data
- top route confusion

## 6. Monitoring / Log จะเก็บยังไง

ตอนนี้มี:

- local JSONL log
- SQLite log
- Postgres log option
- `app/session/chat_logger.py`

แต่ production ควรเก็บเพิ่มให้เป็น quality monitoring ได้จริง

ควรเก็บ fields เหล่านี้ต่อ 1 turn:

```json
{
  "schema_version": "chat_turn_v2",
  "timestamp": "2026-07-28T00:00:00+07:00",
  "session_id": "anonymous-or-client-session",
  "channel": "local_chat",
  "user_question": "...",
  "resolved_question": "...",
  "normalized_question": "...",
  "answer": "...",
  "mode": "pipeline:structured_game_controls",
  "route_category": "games",
  "route_intent": "game_control_lookup",
  "ambiguity": {
    "triggered": false,
    "flags": [],
    "top_score": 0.91,
    "second_score": 0.42,
    "margin": 0.49
  },
  "selected_candidate": {
    "capability_id": "structured.game_controls",
    "score": 0.99,
    "reason": "operation_first_control_query"
  },
  "source_ids": ["game_controls_ps5_tekken8"],
  "validation": {
    "ok": true,
    "errors": [],
    "warnings": []
  },
  "llm_calls": [],
  "timing_ms": {
    "total": 220,
    "preprocess": 20,
    "routing": 18,
    "structured": 45,
    "retrieval": 0,
    "llm": 0,
    "validation": 10
  },
  "no_answer_reason": "",
  "user_feedback": null
}
```

Storage ที่แนะนำ:

- local/dev: JSONL + SQLite
- production: Postgres

table แนะนำ:

- `chat_sessions`
- `chat_turns`
- `pipeline_events`
- `retrieval_hits`
- `llm_calls`
- `validation_results`
- `user_feedback`
- `human_review_queue`
- `missing_data_reports`

Dashboard ที่ควรมี:

- total questions/day
- p50/p95 latency
- no-answer rate
- clarification rate
- LLM attempted rate
- LLM timeout/empty response rate
- validator error/warning rate
- top unanswered questions
- top route confusion pairs
- top missing source ids
- top game names not found
- top control questions with no data

ควรส่งเข้า human review queue เมื่อ:

- validator error
- answer confidence ต่ำ
- route margin ต่ำ
- no-answer แต่ question มี PSU-specific signal
- user กด negative feedback
- LLM ถูกใช้ในคำถาม PSU-specific
- source_ids ว่างใน route ที่ต้องมี source

## 7. UX ตอนถามกลับ ควรทำยังไง

ปัญหา:

- ถ้าถามกลับเยอะไป user จะรู้สึก bot ไม่ตอบ
- ถ้าตอบเดาไปเลยจะผิดง่าย
- คำถามสั้นอย่าง `PC มีอะไรบ้าง` ถามได้หลายความหมาย

solution ที่เหมาะกับโปรเจคนี้คือ Hybrid Clarification Preview

หลักการ:

- ถ้าไม่มั่นใจ ให้ถามกลับ
- แต่ต้องให้ preview สั้นจากข้อมูลจริง
- ไม่ให้ LLM แต่งข้อมูล
- ให้ user ตอบสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา`, `จอง`

ตัวอย่าง:

```text
คำว่า PC อาจหมายถึงหลายเรื่องครับ

ถ้าหมายถึงเกมใน PC: มี VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8, League of Legends
ถ้าหมายถึงราคา PC: PSU Student and Staff 0 บาท/ชั่วโมง, PSU Alumni/General Student 25 บาท/ชั่วโมง, General Adult 70 บาท/ชั่วโมง

อยากดูเรื่องไหน: เกม / อุปกรณ์ / ราคา / จอง
```

ข้อควรระวัง:

- preview ต้องมาจาก structured facts/source จริงเท่านั้น
- อย่า preview ยาวเกิน
- pending clarification ต้องหมดอายุหลัง turn ถัดไป
- ถ้า user พิมพ์ target ใหม่ชัด เช่น `Tekken 8 ปุ่ม` ต้องชนะ context เดิม
- ถ้า user ไม่เลือกและถามใหม่ ให้เข้า pipeline ปกติ

## Roadmap ที่เสนอ

### P0: ควรทำก่อนสุด

1. Data Coverage Report อัตโนมัติ
   - สร้าง script ตรวจทุก domain
   - รายงานว่าเกมไหนไม่มี controls, item ไหนไม่มี quantity, fact ไหนไม่มี source_id

2. Canonical Knowledge Schema
   - ทำ canonical id สำหรับ game/service/equipment/member/rule/source
   - ลดปัญหา edition/variant/ชื่อสะกดไม่ตรง

3. Source Registry v2
   - ย้าย source registry เป็น data file
   - ครอบคลุมทุกหมวด
   - validator ต้องเตือน/กันเมื่อ source_id หาย

4. Game Controls Coverage Fix
   - map controls กับ catalog ด้วย canonical_game_id
   - แยก `no-control-data` จาก `game-not-found`
   - เพิ่ม PC controls policy สำหรับ keyboard/mouse games

5. Route Regression เพิ่มจากเคสจริง
   - เพิ่มเคสที่ user เจอจริง เช่น `call of เล่นยังไง`, `mario kart liveเล่นยังไง`, `อุปกรณ์ไหนเกมเยอะสุด`
   - เพิ่ม compound cross-domain cases

### P1: ทำหลัง P0

1. Semantic Vector Backend
   - เพิ่ม embedding model local
   - ทำ hybrid lexical + semantic + metadata filter
   - benchmark ภาษาไทย

2. Monitoring v1
   - เพิ่ม chat_turn schema
   - ทำ summary report รายวัน
   - top missing data / route confusion / validator failures

3. No-answer Quality v2
   - no-answer ต้องบอกว่าขาดข้อมูลอะไร
   - เสนอคำถามที่ระบบตอบได้แทน
   - ไม่โชว์ technical LLM timeout ใน public answer

4. Model Routing Policy
   - Qwen สำหรับ intent/tool routing เฉพาะ ambiguous
   - Typhoon สำหรับ offline eval/hard case เท่านั้น
   - timeout/circuit breaker ต่อ model

### P2: Production polish

1. Admin update tool
   - เพิ่ม/แก้ข้อมูลผ่าน template
   - validate แล้ว build index ใหม่

2. Human feedback UI
   - ให้ user กด ถูก/ผิด/ไม่ครบ
   - ส่งเข้า review queue

3. Release gate
   - smoke tests
   - golden eval
   - source coverage threshold
   - latency threshold

4. Dashboard
   - quality
   - latency
   - missing data
   - route confusion

## เป้าหมายคะแนน

### จาก 65 ไป 75

ต้องทำ:

- canonicalize game/control mapping
- source contract ให้ครอบคลุม core domains
- เพิ่ม real usage eval เป็น 100+ cases
- no-answer ไม่ technical และ helpful ขึ้น

### จาก 75 ไป 85

ต้องทำ:

- semantic vector/hybrid retrieval จริง
- monitoring/report รายวัน
- admin update + schema validation
- route confusion matrix + regression จาก log จริง

### จาก 85 ไป 90+

ต้องทำ:

- source coverage ใกล้ 100% ในหมวดสำคัญ
- latency p95 อยู่ใน budget
- human review loop
- production dashboard
- policy/security/privacy พร้อม

## ข้อเสนอรูปแบบไฟล์ข้อมูลใหม่

แนะนำทำ knowledge layer ใหม่ใต้:

```text
data/knowledge/
```

ไฟล์ที่ควรมี:

- `source_registry.jsonl`
- `services.jsonl`
- `service_fees.jsonl`
- `game_catalog.jsonl`
- `game_controls.jsonl`
- `equipment.jsonl`
- `booking_policies.jsonl`
- `schedule_rules.jsonl`
- `members.jsonl`
- `competition_rules.jsonl`
- `no_answer_policies.jsonl`
- `clarification_templates.jsonl`

หลักสำคัญ:

- ทุก record ต้องมี `id`
- ทุก record ต้องมี `source_ids`
- ทุก record ต้องมี `last_verified_at`
- ทุก record ต้องมี `confidence_level`
- ถ้าไม่มีข้อมูลจริง ให้ระบุเป็น `coverage_status: unknown` หรือ `not_available` อย่าให้ระบบเดา

## สรุปสุดท้าย

สิ่งที่ควรทำต่อทันทีคือ P0:

1. ทำ Data Coverage Report อัตโนมัติ
2. ทำ canonical id/mapping ระหว่าง game catalog กับ controls
3. ขยาย Source Registry ให้ครบทุกหมวด
4. เพิ่ม regression cases จากคำถามจริง
5. ปรับ no-answer ให้บอกว่าขาดอะไรและถามต่อได้ดีขึ้น

หลังจากนั้นค่อยทำ semantic vector และ monitoring dashboard เพราะถ้าข้อมูล/source ยังไม่เป็นระเบียบ ต่อให้ vector ดีขึ้นก็ยังมีโอกาสดึงข้อมูลผิดหรืออธิบายผิดอยู่ดี
