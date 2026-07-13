# Debug Note - คำถาม "ศูนย์เปิดถึงกี่โมง"

วันที่: 2026-06-29

## อาการที่เจอ

หลังเพิ่ม rule แล้วผู้ใช้ restart kernel แต่คำตอบยังเหมือนเดิม หรือยังมีกรณีตอบว่า "ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี"

## ตรวจจาก shell แล้วพบอะไร

ข้อมูลไม่ได้หายจากฐานข้อมูล แต่ข้อมูลที่มีเป็น "ตารางรอบบริการอุปกรณ์" ไม่ใช่ประกาศเวลาเปิด-ปิดศูนย์อย่างเป็นทางการ

ข้อมูลที่พบ:

- `curated_schedule_morning`: ตารางบริการช่วง Morning คือ 09:00 - 12:00
- `curated_schedule_afternoon`: ตารางบริการช่วง Afternoon คือ 13:00 - 16:00
- ในข้อมูล web scraping มีข้อความตาราง `Gaming Equipment Schedule` ที่มี Morning และ Afternoon

ดังนั้นคำตอบที่ปลอดภัยควรเป็น:

> ข้อมูลที่มีในระบบเป็นตารางรอบบริการอุปกรณ์: Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยยังไม่พบข้อมูลเวลาเปิด-ปิดศูนย์อย่างเป็นทางการแยกต่างหาก

## สาเหตุหลัก

1. ถ้ารัน `answer_question("ศูนย์เปิดถึงกี่โมง", use_rules=False)` จะบังคับข้าม rule ทั้งหมด ทำให้ rule ใหม่ไม่ถูกใช้
2. ก่อนแก้ retrieval จัดอันดับเอกสารผิด โดยดึง `curated_time_change_policy` ขึ้นมาก่อน `curated_schedule_morning`
3. LLM-only มีโอกาสมองข้าม chunk ตารางบริการถ้า chunk นั้นอยู่ท้าย context
4. log ล่าสุดไม่พบคำถาม `ศูนย์เปิดถึงกี่โมง` ใน `chat_log.jsonl` ช่วงที่ตรวจ แปลว่าอาจไม่ได้รันผ่าน `answer_question()` ตัวล่าสุด หรือยังรัน cell เก่า

## สิ่งที่แก้แล้ว

ไฟล์ที่แก้:

- `C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\data\curated\rule_patterns.jsonl`
- `C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\notebooks\01_local_rag_qwen3_4b.ipynb`
- `C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\scripts\run_smoke_tests.py`

รายละเอียดการแก้:

- เพิ่ม `rule_service_schedule` สำหรับคำถามเวลาเปิด-ปิด/เวลาทำการ/ตารางบริการ
- เพิ่ม route keyword ให้คำถามกลุ่มนี้เข้า category `reservation`
- เพิ่ม `schedule_boost` ให้ retrieval ดัน `curated_schedule_morning` และ `curated_schedule_afternoon` ขึ้นก่อน
- เพิ่ม direct fallback ให้คำถามเวลาเปิด-ปิดหยิบ schedule facts จาก `records` โดยตรง
- เพิ่ม prompt guard ไม่ให้ LLM ตอบปนภาษาจีน/ภาษาอื่น
- เพิ่ม `sanitize_model_answer()` เพื่อตัดอักษรจีนที่โมเดลเล็กอาจเผลอปนในคำตอบภาษาไทย
- เพิ่ม progress log ใน `run_smoke_tests.py` เพื่อดูว่า test ค้างที่เคสไหน

## ผลทดสอบหลังแก้

รันทดสอบเฉพาะคำถาม `ศูนย์เปิดถึงกี่โมง`

| โหมด | เวลา | Retrieved IDs | ผล |
|---|---:|---|---|
| default, ใช้ rule | 0.008s | `rule_service_schedule` | ตอบ Morning 09:00-12:00 และ Afternoon 13:00-16:00 พร้อมเตือนว่ายังไม่พบเวลาเปิด-ปิดศูนย์ทางการ |
| `use_rules=False`, direct RAG | 0.039s | `curated_schedule_morning`, `curated_schedule_afternoon`, `curated_time_change_policy`, `curated_reservation_advance_time` | ตอบตารางบริการถูก และไม่หลุดไปตอบเรื่องเปลี่ยนเวลา |
| `use_rules=False`, `use_direct=False`, LLM-only | 4.66s | `curated_schedule_morning`, `curated_schedule_afternoon`, `curated_time_change_policy`, `curated_reservation_advance_time` | ตอบ 09:00-12:00 และ 13:00-16:00 ได้ ไม่ตอบว่าไม่พบข้อมูล |

## วิธีเช็คใน notebook

หลัง Restart Kernel ให้กด Run All หรืออย่างน้อยต้องรัน cell ที่โหลด config, records, Chroma, retriever, และ `answer_question()` ใหม่

```python
print(len(RULES))
```

ควรได้:

```text
27
```

ทดสอบ rule:

```python
match_rule("ศูนย์เปิดถึงกี่โมง", RULES)
```

ควรเจอ:

```text
rule_service_schedule
```

ทดสอบแบบใช้งานจริง:

```python
answer, hits, elapsed = answer_question("ศูนย์เปิดถึงกี่โมง")
print(elapsed)
print([h["id"] for h in hits])
print(answer)
```

ถ้าจะทดสอบ RAG โดยไม่ใช้ rule:

```python
answer, hits, elapsed = answer_question("ศูนย์เปิดถึงกี่โมง", use_rules=False)
print(elapsed)
print([h["id"] for h in hits])
print(answer)
```

ถ้าอยากทดสอบ LLM-only จริง ๆ:

```python
answer, hits, elapsed = answer_question("ศูนย์เปิดถึงกี่โมง", use_rules=False, use_direct=False)
print(elapsed)
print([h["id"] for h in hits])
print(answer)
```

## ถ้ายังตอบเหมือนเดิม

ให้เช็ค 4 จุดนี้ก่อน:

1. ใน cell ที่ถาม มี `use_rules=False` อยู่ไหม ถ้ามี แปลว่ากำลังปิด rule เอง
2. `print(len(RULES))` ได้ `27` หรือยัง ถ้าได้ `26` แปลว่ายังไม่ได้โหลด rule file ล่าสุด
3. เปิด notebook ถูกไฟล์ไหม ต้องเป็น `15_PSU_Esports_Local_RAG_Qwen3_4B\notebooks\01_local_rag_qwen3_4b.ipynb`
4. กด Restart Kernel อย่างเดียวไม่พอ ต้อง Run All หรือรัน cell โหลด rule/function ใหม่ด้วย
