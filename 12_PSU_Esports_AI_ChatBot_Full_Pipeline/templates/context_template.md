# Context Template

ใช้รูปแบบนี้ในการส่ง context ให้ LLM

```text
<context>
[1]
title: {{title}}
category: {{category}}
subcategory: {{subcategory}}
url: {{url}}
text:
{{text}}

[2]
title: {{title}}
category: {{category}}
subcategory: {{subcategory}}
url: {{url}}
text:
{{text}}
</context>

คำถาม: {{question}}
```

