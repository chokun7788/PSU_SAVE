# 01 - Docker Compose Examples

ไฟล์นี้เป็นตัวอย่างโครง docker compose สำหรับแนวคิด ไม่ใช่ไฟล์ที่ต้อง copy ไปรันตรง ๆ ทันที ต้องปรับ image, path, env และ secrets ตามโปรเจกต์จริง

---

## แบบ API

```yaml
services:
  backend:
    build: ./backend
    environment:
      APP_ENV: production
      LLM_PROVIDER: openai
      LLM_MODEL: latest-mini-model
      EMBEDDING_PROVIDER: openai
      VECTOR_DB: chroma
      CHROMA_HOST: chroma
      CHROMA_PORT: "8000"
      DATABASE_URL: postgresql://app:password@postgres:5432/app
    env_file:
      - .env
    depends_on:
      - chroma
      - postgres
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    environment:
      NEXT_PUBLIC_API_URL: https://your-domain.com/api
    ports:
      - "3000:3000"

  chroma:
    image: chromadb/chroma
    volumes:
      - chroma_data:/chroma/chroma

  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: password
      POSTGRES_DB: app
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  chroma_data:
  postgres_data:
```

---

## แบบ Local ด้วย Ollama

```yaml
services:
  backend:
    build: ./backend
    environment:
      APP_ENV: production
      LLM_PROVIDER: ollama
      OLLAMA_BASE_URL: http://ollama:11434
      LLM_MODEL: qwen-or-llama-model
      EMBEDDING_PROVIDER: local
      VECTOR_DB: chroma
      CHROMA_HOST: chroma
      DATABASE_URL: postgresql://app:password@postgres:5432/app
    depends_on:
      - ollama
      - chroma
      - postgres
    ports:
      - "8000:8000"

  ollama:
    image: ollama/ollama
    volumes:
      - ollama_data:/root/.ollama
    ports:
      - "11434:11434"
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  chroma:
    image: chromadb/chroma
    volumes:
      - chroma_data:/chroma/chroma

  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: password
      POSTGRES_DB: app
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  ollama_data:
  chroma_data:
  postgres_data:
```

---

## แบบ Local ด้วย vLLM

```yaml
services:
  backend:
    build: ./backend
    environment:
      APP_ENV: production
      LLM_PROVIDER: openai_compatible
      OPENAI_COMPATIBLE_BASE_URL: http://vllm:8000/v1
      LLM_MODEL: your-local-model-name
      VECTOR_DB: qdrant
      QDRANT_URL: http://qdrant:6333
    depends_on:
      - vllm
      - qdrant
    ports:
      - "8000:8000"

  vllm:
    image: vllm/vllm-openai:latest
    command:
      - --model
      - your-model
      - --host
      - 0.0.0.0
      - --port
      - "8000"
    volumes:
      - hf_cache:/root/.cache/huggingface
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  qdrant:
    image: qdrant/qdrant
    volumes:
      - qdrant_data:/qdrant/storage
    ports:
      - "6333:6333"

volumes:
  hf_cache:
  qdrant_data:
```

---

## สิ่งที่ต้องปรับก่อนใช้จริง

- ไม่ใช้ password ตรง ๆ ใน compose
- ใช้ `.env` หรือ secret manager
- ปิด port ภายในที่ไม่ควร expose
- วาง Nginx/Caddy หน้า backend
- เปิด HTTPS
- ตั้ง volume backup
- ตั้ง restart policy
- เพิ่ม healthcheck
- จำกัด resource

