# Docker Notes

สำหรับ MVP แนะนำให้รันแบบนี้ก่อน:

```text
Ollama: ติดตั้งบน Windows host
Backend/Notebook: รันบนเครื่องหรือ Docker
Vector DB: Chroma persistent folder
```

ถ้ารัน backend ใน Docker แล้วต้องเรียก Ollama บน Windows host ให้ใช้:

```text
http://host.docker.internal:11434
```

ถ้ารันบน Linux + NVIDIA GPU:

- ติดตั้ง NVIDIA driver
- ติดตั้ง NVIDIA Container Toolkit
- ค่อยเอา Ollama เข้า Docker Compose

ยังไม่แนะนำให้ทำ Docker เต็มชุดในวันแรก เพราะควรทำ core RAG ให้ตอบได้ก่อน

