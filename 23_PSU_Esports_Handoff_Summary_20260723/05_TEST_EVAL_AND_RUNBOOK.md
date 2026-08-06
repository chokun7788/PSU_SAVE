# Test Eval And Runbook

ไฟล์นี้รวม command สำคัญสำหรับทดลอง local chatbot และตรวจระบบ

ให้ run จาก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

## เปิด Local Terminal Chat

```powershell
.\start_local_ai_chat.ps1
```

ระบุ model:

```powershell
.\start_local_ai_chat.ps1 -Model qwen2.5:3b
```

เปิด debug:

```powershell
.\start_local_ai_chat.ps1 -Debug
```

ถามครั้งเดียว:

```powershell
.\start_local_ai_chat.ps1 -Once "เกม คอลออฟดูตี้ มีข้อมูลไหม"
```

เปิด composer ให้ LLM เรียบเรียงจาก facts:

```powershell
.\start_local_ai_chat.ps1 -Composer
```

ปิด LLM ทั้งหมดเพื่อเช็ค deterministic path:

```powershell
.\start_local_ai_chat.ps1 -NoLlm
```

## คำสั่งใน Local Chat

```text
/help
/exit
/clear
/debug on
/debug off
/llm on
/llm off
/router on
/router off
/composer on
/composer off
/rag on
/rag off
/model qwen2.5:3b
/timeout 20
/predict 256
/check
/history
/session
/intent first
/intent normal
/intent-model qwen2.5:3b
/intent-timeout 8
/intent-predict 50
```

## Notebook Chat

เปิด:

```text
notebooks\04_local_hybrid_chat_debug.ipynb
```

ฟังก์ชันที่ใช้:

```python
ask("สมาชิก PSU Esport มีกี่หมวด", show_trace=True)
ask("แล้วแต่ละหมวดมีใครบ้าง", show_trace=True)
ask_with_composer("เกมใน PS5 มีอะไรมั่ง")
chat_loop(show_trace=True)
```

ความต่าง:

- `ask(...)`: ใช้ pipeline ปกติ
- `ask_with_composer(...)`: เปิด facts-only LLM composer เพื่อเรียบเรียงจาก facts อาจสวยขึ้นแต่ช้าขึ้น และเคยมีบางกรณีตอบยาว/ไม่ตรงเท่า structured ตรง

## Compile

รันเฉพาะไฟล์ที่แก้:

```powershell
python -m py_compile app\pipeline\game_title_correction.py app\pipeline\structured_tools.py
```

หรือเพิ่มไฟล์ตามงานที่แก้

## Smoke Tests สำคัญ

Game title typo:

```powershell
python tests\smoke_test_game_title_typo_correction.py
```

Game controls:

```powershell
python tests\smoke_test_game_controls.py
```

Universal/adaptive intent:

```powershell
python tests\smoke_test_universal_intent.py
python tests\smoke_test_adaptive_intent_gate.py
```

Booking/price regression:

```powershell
python tests\smoke_test_booking_price_regression.py
```

Structured tools:

```powershell
python tests\smoke_test_structured_tools.py
```

Members/session:

```powershell
python tests\smoke_test_members_and_game_knowledge.py
python tests\smoke_test_session_context.py
```

Formatting:

```powershell
python tests\smoke_test_answer_formatting.py
```

## Eval Scripts

Routing real usage:

```powershell
python tools\run_routing_eval.py --cases data\routing\routing_eval_real_usage.jsonl
```

Answer quality:

```powershell
python tools\run_answer_quality_eval.py
```

Adaptive intent:

```powershell
python tools\run_adaptive_intent_eval.py
```

Game title fuzzy all games:

```powershell
python tools\run_game_title_fuzzy_eval.py
```

Quick fuzzy eval:

```powershell
python tools\run_game_title_fuzzy_eval.py --limit 10
```

## Reports ล่าสุดที่ควรรู้

```text
reports\routing_eval\routing_eval_20260723_000249.json
reports\routing_eval\routing_eval_20260723_000249.csv
reports\answer_quality_eval\answer_quality_eval_20260722_235928.json
reports\answer_quality_eval\answer_quality_eval_20260722_235928.csv
reports\adaptive_intent_eval\adaptive_intent_eval_20260722_235853.json
reports\adaptive_intent_eval\adaptive_intent_eval_20260722_235853.csv
reports\game_title_fuzzy_eval\game_title_fuzzy_eval_20260723_134247.json
reports\game_title_fuzzy_eval\game_title_fuzzy_eval_20260723_134247.csv
```

## Debug Strategy

ถ้าคำตอบผิด:

1. ดู `mode`
2. ดู `route.category` / `route.intent`
3. ดู `universal_intent.domain` / `operation`
4. ดู `source_type`
5. ดู trace ว่า:
   - preprocess เปลี่ยนคำถามไหม
   - game_title_correction เกิดไหม
   - intent LLM ถูกเรียกไหม
   - structured tool ถูก allow/reject เพราะอะไร
   - fast path ตอบก่อนหรือไม่
   - retrieval ดึง source ไหน
6. แก้ที่สาเหตุ ไม่ใช่เพิ่ม rule ทับไปเรื่อย ๆ

## คำถาม smoke test ที่ควรลองมือ

```text
เกม คอลออฟดูตี้ มีข้อมูลไหม
คอลออฟดูตี้ มีเกมอะไรบ้าง
อยากเล่น tekkrn8 ต้องทำยังไง
tekkrn8 มีปุ่มอะไรบ้าง
เกม msrio มีข้อมูลไหม
เกม mqrio มีข้อมูลไหม
เกม ฟอทไน มีข้อมูลไหม
เกม วาโลแร้น มีข้อมูลไหม
สมาชิก PSU Esport มีกี่หมวด
แล้วแต่ละหมวดมีใครบ้าง
ใครเป็นผู้จัดการ
ตำแหน่ง Game and 3D Developer ใครทำ
เกมตอนนี้มีเกมอะไรบ้าง
PS5 มีเกมอะไรบ้าง
VR ราคาเท่าไหร่
วันจันทร์เล่น PS5 9 โมงถึง 12 โมงเสียกี่บาท
เมืองหลวงของประเทศไทยคืออะไร
```

