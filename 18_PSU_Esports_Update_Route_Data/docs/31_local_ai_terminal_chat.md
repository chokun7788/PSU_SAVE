# Local AI Terminal Chat

ใช้สำหรับทดลองถามตอบ chatbot จาก terminal โดยไม่ต้องเปิดเว็บ

## เปิดแชท

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
.\start_local_ai_chat.ps1
```

เลือกโมเดล:

```powershell
.\start_local_ai_chat.ps1 -Model qwen2.5:1.5b -Timeout 20
```

ถ้าต้องการปรับจำนวน token ที่ให้โมเดลสร้างคำตอบ:

```powershell
.\start_local_ai_chat.ps1 -Model scb10x/typhoon2.5-qwen3-4b -Timeout 20 -NumPredict 256
```

ปิด Local LLM fallback แล้วใช้เฉพาะ rule/RAG:

```powershell
.\start_local_ai_chat.ps1 -NoLlm
```

โหมด local ปัจจุบันจะเปิด Local LLM helper ให้ 3 ส่วนเมื่อไม่ใส่ `-NoLlm`:

- Universal Intent LLM: ช่วย classify intent เมื่อ heuristic ไม่มั่นใจ
- LLM Tool Router: ช่วยเลือกว่าจะไป structured / fast path / retrieval / general LLM
- Facts-only Composer: ช่วยเรียบเรียงคำตอบจาก facts โดยไม่เพิ่มข้อมูลใหม่

ถ้าต้องการเทียบกับ deterministic pipeline เดิม:

```powershell
.\start_local_ai_chat.ps1 -NoToolRouter -NoComposer
```

## คำสั่งในแชท

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
/model qwen2.5:1.5b
/timeout 30
/predict 256
/check
/history
```

## ทดสอบแบบถามครั้งเดียว

```powershell
python tools\local_ai_chat.py --once "PS5 มีเกมอะไรบ้าง" --no-llm
.\start_local_ai_chat.ps1 -NoLlm -NoLog -Once "PS5 มีเกมอะไรบ้าง"
```

## หมายเหตุ

- Memory อยู่ใน terminal session ปัจจุบัน และหายเมื่อออกจากโปรแกรม
- ถ้าใช้ Local LLM ต้องให้ Ollama/model ตอบได้ก่อน
- โมเดลหลักปัจจุบันคือ `scb10x/typhoon2.5-qwen3-4b` ซึ่งผ่านการเปรียบเทียบของโปรเจกต์แล้ว หากต้องการ override ให้ระบุ `-Model` ตอนเริ่มระบบ
- ถ้า Ollama ไม่ตอบภายใน timeout ระบบจะไม่ดึงข้อมูลศูนย์มาตอบแทนสำหรับคำถามทั่วไป เพื่อเลี่ยงคำตอบมั่ว
