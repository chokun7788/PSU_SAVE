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
.\start_local_ai_chat.ps1 -Model qwen2.5:3b -Timeout 40 -NumPredict 256
```

ปิด Local LLM fallback แล้วใช้เฉพาะ rule/RAG:

```powershell
.\start_local_ai_chat.ps1 -NoLlm
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
- ถ้าใช้ `qwen3:4b` แล้วเจอ `thinking but no final response` ให้ลองเปลี่ยนเป็น `qwen2.5:3b` ก่อน เพราะ Qwen3 เป็น thinking model และอาจใช้ token ไปกับการคิดจนยังไม่ส่งคำตอบสุดท้าย
- ถ้า Ollama ไม่ตอบภายใน timeout ระบบจะไม่ดึงข้อมูลศูนย์มาตอบแทนสำหรับคำถามทั่วไป เพื่อเลี่ยงคำตอบมั่ว
