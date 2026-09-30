# Implementation Plan: Budgeted Target-Grounded RAG Retrieval

วันที่จัดทำ: 1 กันยายน 2026

สถานะ: **not_started**

Owner ที่แนะนำ: Retrieval / Answer Quality

อ้างอิงหลัก: [Master Plan 67](67_timeout_reliability_remediation_master_plan_20260901.md)

## 1. เป้าหมายและสถานะปัจจุบัน

เป้าหมายคือทำให้ Semantic RAG:

- ค้นเฉพาะเอกสารที่สอดคล้องกับ **QuestionFrame**
- ไม่เปลี่ยน game/member/zone target ที่ Frame ยืนยันแล้ว
- กรอง category, scope, target, facet, effective date และ trust level ก่อน similarity scoring
- ใช้เวลาไม่เกิน 1.5 วินาทีรวม embedding, search, rerank และ source guard
- ไม่เริ่ม retrieval หากเวลาที่เหลือไม่พอ
- คืน clarification/no-answer เมื่อ target ไม่รู้หรือหลักฐานขัดแย้ง

RAG มีหน้าที่ค้นหลักฐานและสร้าง verified draft ไม่ใช่สร้างข้อเท็จจริง PSU ขึ้นใหม่ และไม่ใช้ตอบข้อมูล real-time เช่น slot หรือ booking status

## 2. หลักฐานจาก Log/Code พร้อม Case ID

### 2.1 สิ่งที่ยืนยันจาก Log

- MB-0501 ใช้ vector/retrieval ประมาณ 4.805 วินาที
- MB-0519 ใช้ vector/retrieval ประมาณ 4.684 วินาที
- trace ล่าสุดมีกรณีคำนวณ semantic candidates แล้ว discard category mismatch จำนวนมากประมาณ 782 รายการในบางเส้นทาง
- ชุดทดสอบพบกรณี evidence หรือ route target ไม่ตรงคำถาม เช่น CS2/Overcooked ที่ต้องตรวจเป็น regression case
- Single-request ที่มี Intent LLM, deterministic และ vector ต่อกันสามารถเกิน 20–30 วินาที

### 2.2 สิ่งที่ยืนยันจาก Code

- app/pipeline/hybrid_retrieval.py เรียก curated, vector และ semantic retrieval ก่อนรวมคะแนนและ rerank
- app/pipeline/semantic_vector_retrieval.py สร้าง query embedding แล้ววน index documents เพื่อเช็ค category/trust และ score
- category mismatch ถูกนับหลังเข้ากระบวนการ retrieval แล้ว
- second_score ถูกตั้งเป็น 0 เมื่อมี candidate เดียว ทำให้ margin เท่ากับ top_score
- route discovery รองรับ knowledge, events_news และ about_us
- Answer Contract ตรวจ target บางชนิดแล้ว แต่ยังต้องล็อก source category, facet และ version เทียบ Frame เดิม
- semantic index มี model/dimension metadata และ lru cache แต่ cache identity ต้องรวม release/catalog/query normalization ให้ครบ

### 2.3 ข้อสันนิษฐานที่ต้องทดสอบ

- จำนวน 782 category mismatch เป็นตัวเลขจาก trace บาง case ไม่ใช่ค่าเฉลี่ยทั้งระบบ
- การ partition index ตาม metadata จะลด latencyเพียงใดขึ้นกับ backend และจำนวนเอกสารจริง
- absolute similarity threshold ต้อง calibrate ต่อ embedding model BGE-M3 และชนิดเอกสาร
- optional reranker อาจคุ้มเฉพาะ query บางแบบ ต้องวัดแยก

## 3. Root Cause และสิ่งที่ยังพิสูจน์ไม่ได้

### Root Cause ที่ยืนยันได้

1. **Late filtering**: metadata guard เกิดหลังเริ่ม retrieval/scoring ทำให้คำนวณเอกสารที่ไม่มีสิทธิ์ชนะ
2. **Route-centric แทน Frame-centric**: retrieval ใช้ route category แต่ไม่ได้บังคับ original target/facet ครบ
3. **Artificial margin**: candidate เดียวมี second_score 0 จึงดูมั่นใจเกินจริง
4. **No start gate ตาม remaining budget**: embedding/retrieval สามารถเริ่มใกล้ deadline
5. **Multiple retrieval backends**: curated/vector/semantic อาจทำงานต่อเนื่องโดยไม่มี total stage cap
6. **Weak version coupling**: cache/index identity ยังต้องล็อกกับ model, dimensions และ content version ชุดเดียว

### สิ่งที่ยังพิสูจน์ไม่ได้

- latency 4.7–4.8 วินาทีแบ่งเป็น embedding, scan, rerank และ I/O เท่าใดจนกว่าจะมี event จากเอกสาร 76
- reranker เป็น bottleneck หลักหรือไม่
- threshold ที่ดีที่สุดต่อภาษาไทย/อังกฤษ
- index partition strategy ที่เหมาะที่สุดระหว่าง in-memory metadata postings กับหลาย physical indexes

## 4. Target Behavior และ Invariants

ส่วนนี้เป็น **การออกแบบที่เสนอ (Proposed Design)** ค่า score gate ต้อง calibrate ก่อนถือเป็นค่าจริง

### Target Behavior

1. รับ original QuestionFrame และ release snapshot
2. สร้าง **RetrievalConstraint** จาก category/scope/target/facet/date/trust
3. ถ้า Frame ต้องการ target แต่ status unknown/ambiguous ให้หยุดก่อน embedding
4. ตรวจ RequestBudget: ต้องเหลืออย่างน้อย 1.75 วินาทีจึงเริ่ม
5. เลือก metadata partition ก่อน similarity scoring
6. สร้าง BGE query embeddingภายใน 0.75 วินาที
7. score candidate ไม่เกิน 8
8. optional rerank ภายในเวลาที่เหลือ
9. source guard และ target alignment
10. คืน evidence สูงสุด 4 ชิ้น
11. Answer Contract เทียบกับ Frame ต้นฉบับ ไม่ใช้ Frame ที่ RAG แก้เอง

### Invariants

- RAG ห้ามเปลี่ยน original target
- candidate limit 8 และ final evidence limit 4
- total retrieval budget 1.5 วินาที
- embedding budget 0.75 วินาที
- start gate ต้องการ remaining อย่างน้อย 1.75 วินาทีเพื่อรวม finalizer reserve
- unknown/ambiguous required target ไม่ค้นแบบเดาสุ่ม
- target mismatch ทุกชิ้นถูกตัดก่อน final evidence
- expired, future, low-trust หรือ stale document ไม่ผ่าน policy
- single candidate ต้องผ่าน absolute score และ alignment โดยไม่อาศัย margin
- Structured และ RAG อ่าน release/version เดียวกัน

## 5. Mermaid Flow/Sequence Diagram

### Retrieval Flow

~~~mermaid
flowchart TD
    F[Original QuestionFrame] --> T{Required target resolved?}
    T -->|no| C[Clarification or no-answer]
    T -->|yes/not required| B{Remaining >= 1.75s?}
    B -->|no| D[Verified deterministic draft or no-answer]
    B -->|yes| K[Build RetrievalConstraint]
    K --> P[Pre-filter metadata partition]
    P --> E[BGE query embedding <= 0.75s]
    E --> S[Similarity score <= 8 candidates]
    S --> R[Optional bounded rerank]
    R --> G[Source + target + facet guard]
    G --> L{Absolute score and alignment pass?}
    L -->|yes| O[Final evidence <= 4]
    L -->|no| C
~~~

### Evidence Contract Sequence

~~~mermaid
sequenceDiagram
    participant E as Engine
    participant F as QuestionFrame
    participant R as Retrieval
    participant G as Source Guard
    participant A as Answer Contract
    E->>F: freeze original frame
    E->>R: query + frame + budget + release
    R->>R: pre-filter before scoring
    R-->>G: max 8 scored candidates
    G-->>E: max 4 aligned evidence rows
    E->>A: draft + evidence + original frame
    A-->>E: pass or target/source/version errors
~~~

## 6. Interface, Data Structure, Config และ pseudocode

### 6.1 RetrievalConstraint

~~~python
@dataclass(frozen=True)
class RetrievalConstraint:
    allowed_categories: frozenset[str]
    scope: str
    target_ids: tuple[str, ...]
    target_required: bool
    facet: str
    effective_at: datetime
    minimum_trust_rank: int
    release_version: str
    index_version: str
~~~

ห้ามสร้าง allowed_categories เป็น “ทุกหมวด” เมื่อ Frame มี domain ชัดเจน

### 6.2 EvidenceRecord

~~~python
@dataclass(frozen=True)
class EvidenceRecord:
    document_id: str
    chunk_id: str
    category: str
    scope: str
    target_ids: tuple[str, ...]
    facet: str
    source_url: str
    source_version: str
    effective_from: datetime | None
    valid_until: datetime | None
    trust_level: str
    semantic_score: float
    lexical_score: float
    rerank_score: float | None
~~~

### 6.3 RetrievalResult

~~~python
@dataclass(frozen=True)
class RetrievalResult:
    status: Literal[
        "completed", "no_candidates", "target_unresolved",
        "budget_skipped", "timeout", "version_mismatch"
    ]
    evidence: tuple[EvidenceRecord, ...]
    candidate_count: int
    filtered_counts: Mapping[str, int]
    top_score: float | None
    second_score: float | None
    margin: float | None
    index_version: str
    elapsed_ms: float
    timing: Mapping[str, float]
~~~

เมื่อมี candidate เดียว second_score และ margin ต้องเป็น None ไม่ใช่ 0/top_score

### 6.4 Frame to constraint mapping

| Frame | Allowed category | Target policy | Facet |
|---|---|---|---|
| overview/member_lookup | about_us | member ID/role | member_profile |
| games/game_how_to | games, knowledge ที่ target เดียวกัน | required game ID | how_to |
| games/game_detail | games | required game ID | detail |
| competition_rules | competition_rules | competition/event ถ้ามี | rule |
| events_news | events_news | optional event ID | current_news |
| service_fee | ไม่ใช้ RAG หาก exact | service/customer group | price |
| schedule/slot | ไม่ใช้ RAG real-time | resource/date | schedule |

### 6.5 Index partitions

สร้าง posting/filter maps ตอน index load:

- category_to_doc_ids
- scope_to_doc_ids
- target_to_doc_ids
- facet_to_doc_ids
- trust_rank_to_doc_ids
- active interval metadata

Candidate set เริ่มจาก intersection ของ filters แล้วจึงคำนวณ dot product/similarity เฉพาะ IDs นั้น หาก backend รองรับ metadata filter native ให้ adapter แปลง constraint โดยคง semantics เดียวกัน

### 6.6 Retrieval pseudocode

~~~python
def retrieve(query, frame, context):
    budget = context.budget
    if frame.target_required and frame.target_status != "matched":
        return result("target_unresolved")
    if budget.remaining() < 1.75:
        return result("budget_skipped")

    constraint = constraints_from(frame, context.release_snapshot)
    candidate_ids = index.prefilter(constraint)
    if not candidate_ids:
        return result("no_candidates")

    with budget.stage("retrieval", cap=1.5):
        vector = embed_query(
            query,
            timeout=min(0.75, budget.remaining_for_stage())
        )
        scored = index.score(vector, candidate_ids, limit=8)
        reranked = optional_rerank(scored, budget)
        aligned = source_and_target_guard(reranked, frame)
        return decide(aligned[:4], frame)
~~~

### 6.7 Score decision

ค่า threshold ต้องเก็บแยกตาม model/version และ calibrate จาก gold set:

- absolute semantic threshold สำหรับ route discovery
- absolute semantic threshold สำหรับ target-grounded lookup
- lexical support minimum เมื่อ alias/target text ควรปรากฏ
- target alignment เป็น hard boolean
- minimum source trust

Decision:

- 0 candidates → no_candidates
- 1 candidate → ต้องผ่าน absolute threshold + target/facet/source guard
- 2+ candidates → top ต้องผ่าน absolute threshold และ margin ที่กำหนด
- conflicting authoritative evidence → no-answer/manual content review ไม่เลือกตาม score อย่างเดียว

### 6.8 Cache key

~~~text
model_id
+ embedding_dimensions
+ normalized_query_hash
+ question_frame_fingerprint
+ release_version
+ catalog_version
+ index_version
+ retrieval_policy_version
~~~

Cache ต้อง bounded, มี TTL และ invalidated เมื่อ publish release ใหม่ ห้าม cacheผลจาก target_unresolved ข้าม request/session

### 6.9 Configuration

| Config | Default |
|---|---:|
| PSU_RETRIEVAL_TOTAL_TIMEOUT_SEC | 1.5 |
| PSU_RETRIEVAL_EMBED_TIMEOUT_SEC | 0.75 |
| PSU_RETRIEVAL_MIN_REMAINING_SEC | 1.75 |
| PSU_RETRIEVAL_CANDIDATE_LIMIT | 8 |
| PSU_RETRIEVAL_EVIDENCE_LIMIT | 4 |
| PSU_RETRIEVAL_RERANK_ENABLED | true แต่ budget-gated |
| PSU_RETRIEVAL_TARGET_GROUNDING | shadow ก่อน |
| PSU_RETRIEVAL_POLICY_VERSION | target_grounded_v1 |

## 7. ขั้นตอน Implement ตามลำดับ

1. Freeze mismatch/slow retrieval casesใน corpus 68
2. เพิ่ม timing breakdown embedding, prefilter, scoring, rerank และ guard
3. นิยาม RetrievalConstraint/EvidenceRecord/RetrievalResult
4. ทำ Frame fingerprint จาก immutable original QuestionFrame
5. สร้าง metadata posting maps ตอน index load
6. ย้าย category/scope/target/facet/date/trust filteringก่อน score
7. เพิ่ม required-target short circuit ก่อน embedding
8. เพิ่ม remaining budget start gate และ stage cap
9. จำกัด candidates 8/evidence 4
10. แก้ single-candidate margin เป็น None และใช้ absolute gate
11. เพิ่ม target/source/version checks ใน Answer Contract
12. ผูก cache key กับ model/dimensions/versions/policy
13. เชื่อม RequestExecutionContext เพื่อ reuse retrieval result
14. เปิด shadow เปรียบเทียบ old/new evidence IDs และ latency
15. รัน mismatch, focused RAG, full 2,116 และ load test

## 8. Failure Modes และ Safe Fallback

| Failure | Detection | Safe Fallback |
|---|---|---|
| target unknown/ambiguous | Frame status | clarification/no-answer ก่อน embedding |
| remaining ต่ำ | start gate | verified draft จาก Structured/Fast หรือ no-answer |
| embedding timeout | StageDeadlineExceeded | no-answer; ไม่ใช้ stale query vector |
| index/model mismatch | metadata validation | disable retrieval และ alert |
| no candidate after filter | empty intersection | no-answer |
| single weak candidate | absolute score fail | no-answer |
| target mismatch | source guard | discard และ log |
| expired/stale document | effective date guard | discard |
| conflicting trusted sources | conflict detector | no-answer + content review event |
| reranker ไม่ทัน | budget checkpoint | ใช้ pre-rerank orderที่ผ่าน guard หาก policy อนุญาต |

RAG fallback ต้องไม่ขยาย category หรือถอด target constraintเพื่อพยายามให้ “ได้คำตอบ”

## 9. Logging/Metrics ที่ต้องเพิ่ม

Events:

- retrieval_gate_evaluated
- retrieval_prefilter_started/finished
- embedding_started/finished/failed
- similarity_scoring_started/finished
- rerank_started/finished/skipped
- source_guard_finished
- retrieval_finished
- retrieval_target_mismatch
- retrieval_version_mismatch

Fields:

- original frame fingerprint
- allowed category count, target count, facet
- index/model/policy versions
- total_docs, prefiltered_docs, scored_docs, final_docs
- filtered_counts แยก category/scope/target/date/trust/conflict
- embedding/scoring/rerank/guard elapsed
- top_score, second_score nullable, margin nullable
- budget remaining before/after
- selected evidence IDs โดยไม่ log document body

Metrics:

- retrieval P50/P95/P99/Max
- embedding P95
- prefilter reduction ratio
- target mismatch rate
- no-candidate rate
- weak single-candidate rejection rate
- stale/conflict rejection rate
- retrieval start-after-budget rate เป้าหมาย 0
- evidence target accuracy เป้าหมาย 100%

## 10. Unit, Integration, Regression และ Load Tests

### Unit Tests

- Frame maps เป็น constraintถูกต้อง
- category/scope/target/facet/date/trust intersection
- single candidateมี margin None
- target mismatch ถูก discard
- effective date boundary
- trust threshold
- cache keyเปลี่ยนเมื่อ model/dimensions/version เปลี่ยน
- budgetต่ำกว่า 1.75 ไม่เรียก embedder
- candidate/evidence limits

### Integration Tests

- CS2 query ไม่ได้ Overcooked evidence
- Overcooked query ไม่ได้ CS2 evidence
- member query prefilter about_us ก่อน scoring
- unknown game ไม่ค้นแบบ broad
- stale document ไม่ชนะ current source
- conflicting sources ไป Safe Outcome
- Structured/RAG release versionตรงกัน
- Answer Contractใช้ original Frame

### Regression Tests

- retrieval slow cases MB-0501 และ MB-0519
- known/new game RAG cases
- member role cases
- news/effective-date cases
- category discovery ที่ valid ยังคงทำงาน
- exact Structured casesไม่ถูกบังคับผ่าน RAG

### Load Tests

- 30 concurrent mixed queries
- cold embedding model แยกจาก warm SLA
- cache hit/miss mix
- index reload ระหว่าง requests
- all-RAG-attempt scenario โดยยังรักษา admission control

## 11. Acceptance Criteria แบบวัดค่าได้

- total retrieval elapsed ไม่เกิน 1.5 วินาทีทุก request
- embedding elapsed ไม่เกิน 0.75 วินาที
- ไม่มี retrieval เริ่มเมื่อ remaining budgetต่ำกว่า 1.75 วินาที
- scored candidatesไม่เกิน 8 และ final evidenceไม่เกิน 4
- ไม่มี evidence ข้าม target ใน corpus
- CS2/Overcooked mismatch เป็น 0
- about_us filterเกิดก่อน scoring
- single candidateไม่ผ่านจาก marginเทียม
- expired/stale/conflicting evidenceไม่ถูกใช้เป็น factual answer
- Structured/RAG version mismatch rateเป็น 0
- strict FAQ scoreไม่ต่ำกว่า 91.00% และ RAG-focused accuracyไม่ต่ำกว่า baseline
- ไม่มี request เกิน 10 วินาทีจาก retrieval

## 12. Rollback และ Compatibility

- RetrievalResult adapter แปลงเป็น hit dictionaries เดิมได้ช่วง migration
- API responseเดิมไม่เปลี่ยน; trace fieldsใหม่เป็น optional
- เปิด target grounding และ prefilterใน shadow modeก่อน
- รักษา old index loaderไว้หนึ่ง releaseเพื่อ rollback
- หาก recallลด ให้ tune partition mapping/threshold ไม่ถอด target invariant
- rerankerสามารถปิดแยกโดยไม่ปิด source guard
- cacheสามารถปิดทันทีเมื่อสงสัย version contamination

Rollback triggers:

- known target recallลดเกิน 1 percentage point
- cross-target evidenceแม้หนึ่ง case
- P99 retrievalเกิน 1.5 วินาที
- index/version mismatch
- current authoritative documentถูก stale filterผิด

## 13. Dependencies และลิงก์ไปเอกสารอื่น

- [67 Master Plan](67_timeout_reliability_remediation_master_plan_20260901.md)
- [68 Baseline และ Corpus](68_slow_case_baseline_and_regression_corpus_plan_20260901.md)
- [69 RequestBudget](69_hard_deadline_and_pipeline_worker_supervision_plan_20260901.md)
- [70 Member Routing](70_member_about_us_routing_correction_plan_20260901.md)
- [71 Game Resolver](71_bounded_game_entity_resolver_plan_20260901.md)
- [72 RequestExecutionContext](72_structured_fast_resolution_deduplication_plan_20260901.md)
- [74 Local LLM Budget](74_local_llm_budget_health_and_fallback_plan_20260901.md)
- [76 Observability](76_crash_resilient_stage_observability_plan_20260901.md)
- [77 SLA และ Rollout](77_end_to_end_sla_load_test_and_rollout_plan_20260901.md)
- [66 Current Flow Regression](66_current_flow_full_model_regression_20260901.md)

Implementation dependency: ต้องมี original Frame จาก 70, RequestBudget จาก 69, request cache จาก 72 และ stage timingจาก 76 ก่อนเปิด target-grounded retrievalเป็น production behavior
