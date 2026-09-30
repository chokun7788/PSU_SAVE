# Implementation Plan: Structured / Fast Resolution Deduplication

วันที่จัดทำ: 1 กันยายน 2026

สถานะ: **not_started**

Owner ที่แนะนำ: Pipeline Orchestration

อ้างอิงหลัก: [Master Plan 67](67_timeout_reliability_remediation_master_plan_20260901.md)

## 1. เป้าหมายและสถานะปัจจุบัน

เป้าหมายคือทำให้ทุก stage ภายใน request ใช้ผล entity resolution, retrieval และ capability attempt ชุดเดียวกันผ่าน **RequestExecutionContext** เพื่อตัดงานซ้ำระหว่าง Question Frame, Tool Preconditions, Structured, Fast และ Validation

ปัญหาที่ต้องแก้ไม่ใช่เพียง cache เพื่อให้เร็วขึ้น แต่เป็นการล็อก semantics ว่า:

- entity หนึ่งตัวถูก resolve ด้วย catalog/version เดียว
- unknown หรือ ambiguous ไม่ถูกลองใหม่ด้วย algorithm เดิมแล้วได้คำตอบต่างกัน
- candidate retry ทำได้อย่างมีขอบเขต
- side effect และ computation ไม่เกิดซ้ำ
- trace บอกได้ว่าผลถูกคำนวณใหม่หรือ reuse

Context นี้เป็น request-scoped เท่านั้น ไม่ข้าม session, user หรือ request และมีขนาดจำกัดแน่นอน

## 2. หลักฐานจาก Log/Code พร้อม Case ID

### 2.1 สิ่งที่ยืนยันจาก Log

- **KIA-0460** ใช้ structured ประมาณ 2.027 วินาที แล้ว deterministic ประมาณ 17.348 วินาที
- **KIA-0486** ใช้ structured ประมาณ 3.649 วินาที แล้ว deterministic ประมาณ 23.875 วินาที
- ทั้งสอง case ไม่เรียก LLM แต่รวมเวลาเกิน 10 วินาที จึงมีงาน CPU/deterministic ซ้ำหรือ unbounded อยู่ใน critical path
- MB-0501 และ MB-0519 มีหลาย stage แพงต่อเนื่องใน request เดียว แสดงว่า Pipeline ไม่มี budget-aware reuse ที่เข้มพอ

### 2.2 สิ่งที่ยืนยันจาก Code

- Question Frame เรียก target resolver
- Structured handlers และ app/runtime/fast_answer.py มี alias/game matching ของตนเอง
- Tool Preconditions สามารถตรวจ target/capability อีกครั้ง
- Engine สามารถลองหลาย handler ตาม route และ broad fallback
- ไม่มี object กลางที่บันทึกว่า capability ใดถูกพยายามด้วย input/version ใดแล้ว
- stage deadline เดิมตรวจเป็นช่วง แต่ไม่ได้ป้องกัน operation เดิมถูกเริ่มหลายครั้ง

### 2.3 ข้อสันนิษฐานที่ต้องทดสอบ

- จำนวน exact resolver calls ของ KIA-0460/KIA-0486 ยังไม่มี call counter จาก baseline จึงเรียกว่า “มีหลักฐานสอดคล้องกับ duplicate work” ไม่ใช่ยืนยันจำนวนครั้ง
- deterministic stage อาจรวม formatting หรือ handler อื่นด้วย ต้องแยก counter ตามเอกสาร 76
- cache retrieval ภายใน request อาจช่วยน้อยใน query ปกติ แต่ยังจำเป็นเพื่อป้องกัน semantic inconsistency

## 3. Root Cause และสิ่งที่ยังพิสูจน์ไม่ได้

### Root Cause ที่ยืนยันได้

1. **No request-scoped execution memory**: แต่ละ component รับ query แล้วคำนวณเอง
2. **Capability overlap**: Structured และ Fast รองรับ domain ใกล้กันและอาจใช้ resolver เดียวกันโดยไม่แชร์ผล
3. **Broad handler execution**: route fallback เรียกหลาย handler แม้ capability ก่อนหน้าพิสูจน์ unknown/ambiguous แล้ว
4. **Retry semantics ไม่ชัด**: validator rejection อาจทำให้ลองใหม่โดยไม่มี operation key
5. **Version identity ไม่ถูกส่งครบ**: cache/reuse ที่ไม่มี catalog version เสี่ยงผสม release

### สิ่งที่ยังพิสูจน์ไม่ได้

- operation ใดถูกเรียกซ้ำมากที่สุดจนกว่าจะมี call counters
- การลด duplicate เพียงอย่างเดียวจะทำให้ KIA ทั้งสองต่ำกว่า 1.5 วินาทีหรือยังต้องใช้ resolver ใหม่จากเอกสาร 71
- formatter หรือ validation มี hidden resolver call หรือไม่

## 4. Target Behavior และ Invariants

ส่วนนี้เป็น **การออกแบบที่เสนอ (Proposed Design)** และยังไม่ใช่ request behavior ใน Source Code ปัจจุบัน

### Target Behavior

1. API boundary สร้าง RequestExecutionContext หนึ่ง object ต่อ request
2. Context ถือ RequestBudget และ immutable release references
3. Question Frame เรียก GameResolver ผ่าน context
4. Tool Preconditions, Structured และ Fast ขอผลผ่าน context เดิม
5. Context คืน cached GameResolution เมื่อ operation key และ version ตรง
6. capability ที่ทำงานแล้วถูกบันทึกใน attempted_capabilities
7. candidate ถัดไปทำได้เมื่อเป็น capability/operation คนละตัวและ validator อนุญาต
8. retry หลัง validation failure ได้สูงสุดหนึ่ง candidate
9. Pipeline จบแล้ว context ถูกปล่อยทั้งหมด

### Invariants

- ไม่เก็บ context ใน global mutable dictionary ที่ไม่มี eviction
- ไม่ข้าม request แม้ session เดียวกัน
- game resolution ต่อ normalized query + operation + catalog version ไม่เกินหนึ่งครั้ง
- unknown และ ambiguous เป็น cacheable deterministic outcome
- exception ที่ retryable ต้องแยกจาก deterministic outcome
- capability side effect ห้าม retry โดยไม่มี idempotency key
- retrieval cache key ต้องรวม Frame fingerprint และ index version
- decision trace เป็น append-only sequence
- context size มี hard limits

## 5. Mermaid Flow/Sequence Diagram

### Current Duplication

~~~mermaid
flowchart TD
    Q[Query] --> F[Question Frame resolves game]
    F --> P[Tool Preconditions resolves game]
    P --> S[Structured resolves game]
    S --> V{Candidate valid?}
    V -->|no| FA[Fast resolves game again]
    FA --> R[Result]
~~~

### Target Shared Context

~~~mermaid
flowchart TD
    Q[Query] --> C[Create RequestExecutionContext]
    C --> F[Question Frame]
    F --> GR[context.resolve_game]
    GR -->|first call| IDX[GameResolver]
    IDX --> GC[Store GameResolution]
    GC --> P[Tool Preconditions]
    P -->|reuse| GC
    GC --> S[Structured]
    S --> V{Candidate accepted?}
    V -->|yes| A[Answer]
    V -->|no, retry allowed| N[Next distinct capability]
    N -->|reuse resolution| GC
    V -->|no retry| O[Safe Outcome]
~~~

### Candidate Attempt Sequence

~~~mermaid
sequenceDiagram
    participant E as Engine
    participant C as RequestExecutionContext
    participant G as GameResolver
    participant S as Structured
    participant F as Fast
    E->>C: resolve_game(key)
    C->>G: compute only if absent
    G-->>C: immutable GameResolution
    C-->>E: result
    E->>C: begin_attempt(structured.games)
    C-->>E: allowed
    E->>S: execute with same result
    S-->>E: candidate rejected by validator
    E->>C: allow_retry(fast.domain_handlers)
    C-->>E: allowed once, distinct operation
    E->>F: execute without resolving again
~~~

## 6. Interface, Data Structure, Config และ pseudocode

### 6.1 RequestExecutionContext

~~~python
@dataclass
class RequestExecutionContext:
    request_id: str
    budget: RequestBudget
    release_version: str
    catalog_version: str
    retrieval_index_version: str
    game_resolutions: dict[GameResolutionKey, GameResolution]
    attempted_capabilities: dict[CapabilityAttemptKey, AttemptRecord]
    retrieval_results: dict[RetrievalKey, RetrievalResult]
    trace_sequence: int
    retry_count: int
    counters: RequestCounters
~~~

Constructor ต้องสร้าง containers ใหม่ทุก request ห้ามใช้ mutable default ร่วมกัน

### 6.2 Keys

~~~python
@dataclass(frozen=True)
class GameResolutionKey:
    normalized_query_hash: str
    operation: str
    catalog_version: str
    resolver_version: str

@dataclass(frozen=True)
class CapabilityAttemptKey:
    capability_id: str
    operation: str
    target_ids: tuple[str, ...]
    release_version: str

@dataclass(frozen=True)
class RetrievalKey:
    normalized_query_hash: str
    frame_fingerprint: str
    index_version: str
    model_id: str
~~~

Hash ใช้เพื่อ lookup และ performance log ไม่ใช่ security token; ห้ามนำ query content ไป log จาก key

### 6.3 Size limits

| Item | Default limit |
|---|---:|
| game_resolutions | 4 |
| attempted_capabilities | 16 |
| retrieval_results | 4 |
| candidates ต่อ retrieval result | 8 |
| retry_count | 1 |
| trace events ต่อ request | 256 |

เมื่อถึง limit ให้ fail closed สำหรับ operation ใหม่ที่ไม่จำเป็น และ log context_limit_reached ห้ามปล่อย dictionary โตไม่จำกัด

### 6.4 Context methods

~~~python
def resolve_game(self, query, operation, resolver):
    key = make_game_key(query, operation, self.catalog_version)
    if key in self.game_resolutions:
        self.counters.game_resolution_cache_hits += 1
        self.trace("reused_request_resolution", key)
        return self.game_resolutions[key]

    self.budget.checkpoint("game_resolution")
    result = resolver.resolve(query, self.budget)
    self._bounded_store(self.game_resolutions, key, result)
    self.counters.game_resolution_calls += 1
    return result

def begin_capability(self, attempt_key):
    prior = self.attempted_capabilities.get(attempt_key)
    if prior and prior.status in TERMINAL_ATTEMPT_STATUSES:
        self.trace("skipped_duplicate_capability", attempt_key)
        return SKIP
    self.attempted_capabilities[attempt_key] = AttemptRecord.started()
    return ALLOW
~~~

### 6.5 Result caching policy

Cache ได้:

- matched, ambiguous และ unknown GameResolution
- retrieval result ที่ completed และผูก Frame/version ครบ
- capability output ที่ deterministic และไม่มี side effect
- controlled no-answer ที่เกิดจาก deterministic precondition

ไม่ cache เป็น reusable success:

- StageDeadlineExceeded
- worker crash
- provider/network transient error
- corrupted store result
- result ที่ version mismatch
- side effect ที่ไม่รู้สถานะ

### 6.6 Retry policy

Validator rejection แบ่งเป็น:

| Rejection | Retry |
|---|---|
| wrong answer shape แต่ evidence ถูก | repair ก่อน ไม่เปลี่ยน capability |
| target mismatch | ไม่ retry ด้วย target เดิม; Safe Outcome |
| unsupported claim | ลอง candidate ถัดไปได้ 1 ครั้งถ้ามี evidence คนละชุด |
| capability unavailable | ลอง deterministic fallback 1 ครั้ง |
| deadline insufficient | ไม่ retry |
| worker/provider transient failure | API-level retryable response ไม่ retryใน request เดิม |

Candidate retry ต้องตรวจว่า CapabilityAttemptKey ไม่ซ้ำและ remaining budget เพียงพอต่อ stage cap + finalizer reserve

### 6.7 Decision reasons

มาตรฐาน reason:

- computed_request_resolution
- reused_request_resolution
- cached_deterministic_unknown
- skipped_duplicate_capability
- skipped_duplicate_retrieval
- distinct_candidate_retry
- retry_limit_reached
- context_limit_reached
- version_key_mismatch

### 6.8 Configuration

| Config | Default |
|---|---:|
| PSU_REQUEST_CONTEXT_ENABLED | false ระหว่าง shadow |
| PSU_REQUEST_CONTEXT_SHADOW | true |
| PSU_REQUEST_CONTEXT_MAX_RESOLUTIONS | 4 |
| PSU_REQUEST_CONTEXT_MAX_ATTEMPTS | 16 |
| PSU_REQUEST_CONTEXT_MAX_RETRIEVALS | 4 |
| PSU_REQUEST_MAX_CANDIDATE_RETRY | 1 |

## 7. ขั้นตอน Implement ตามลำดับ

1. เพิ่ม call counters รอบ resolver, retrieval และ capability ใน baseline โดยยังไม่เปลี่ยน behavior
2. นิยาม keys และ RequestExecutionContext ใน module ที่ไม่มี import cycle
3. สร้าง context ที่ API/pipeline entry และส่งเป็น explicit parameter
4. ส่ง RequestBudget, release version และ index versions เข้า context
5. เปลี่ยน Question Frame ให้เรียก context.resolve_game
6. เปลี่ยน Tool Preconditions ให้รับ GameResolution จาก context แทน resolve เอง
7. เปลี่ยน structured game handlers ให้รับ resolved target
8. เปลี่ยน fast handlers ให้ reuse resolved target
9. เพิ่ม attempted_capabilities และ closed duplicate skip
10. เพิ่ม retrieval request cache หลัง Target-grounded key จากเอกสาร 73 พร้อม
11. เพิ่ม bounded candidate retry และ reason codes
12. เพิ่ม context limits และ cleanup ใน finally
13. เปิด shadow counters เปรียบเทียบ expected call count กับ behavior เดิม
14. รัน KIA-0460, KIA-0486 และ focused corpus
15. เปิด context behavior ก่อนลบ duplicate resolver call sites

## 8. Failure Modes และ Safe Fallback

| Failure | Detection | Safe Fallback |
|---|---|---|
| Context ไม่ถูกส่ง | assertion ที่ pipeline boundary | สร้างใหม่หนึ่งครั้งและ log integration defect |
| Key version ไม่ตรง | version comparison | คำนวณใหม่ด้วย current versionถ้ามี budget มิฉะนั้น no-answer |
| Context เต็ม | bounded store guard | ข้าม optional operation; Safe Outcome |
| Cached exception | type/status check | ห้าม reuse เป็น deterministic answer |
| Duplicate side effect | attempt/idempotency record | ห้าม execute ซ้ำ; ส่ง manual/retryable outcome |
| Retry loop | retry_count > 1 | หยุดและ Safe Outcome |
| Mutable cached object ถูกแก้ | frozen result/type test | reject mutation ใน test และ copy only when formatting |
| cleanup ไม่ทำงาน | finally/supervisor event | parent ปลด resource และ context ตายพร้อม worker |

ถ้า context subsystem เองล้ม ต้องไม่ตกกลับไป unbounded duplicate pathภายใต้ deadline; ให้ตอบ Safe Outcome และ mark internal_error

## 9. Logging/Metrics ที่ต้องเพิ่ม

Events:

- request_context_created
- request_resolution_computed
- request_resolution_reused
- capability_attempt_started/finished
- duplicate_capability_skipped
- retrieval_result_reused
- candidate_retry_allowed/blocked
- context_limit_reached
- request_context_released

Counters:

- game_resolution_calls
- game_resolution_cache_hits
- retrieval_calls
- retrieval_cache_hits
- capability_attempts
- duplicate_capabilities_skipped
- candidate_retries
- context_peak_entries

Metrics:

- duplicate resolver call rate เป้าหมาย 0
- duplicate capability skip rate
- request cache hit rate แยก operation
- latency saved estimate จาก shadow timing
- context size P95/Max
- retry success rate
- context cleanup success rate

Trace ต้องมี sequence จาก Parent Logger ตามเอกสาร 76 และไม่เก็บ query/PII

## 10. Unit, Integration, Regression และ Load Tests

### Unit Tests

- mutable defaults ไม่แชร์ข้าม context
- key เปลี่ยนเมื่อ catalog/index/resolver version เปลี่ยน
- matched/ambiguous/unknown ถูก cache
- transient exception ไม่ถูก cache เป็น success
- limit ทุก dictionary ถูกบังคับ
- duplicate capability ถูก skip
- distinct candidate retry ได้ครั้งเดียว
- timeout ไม่อนุญาต retry
- frozen result แก้ไขไม่ได้

### Integration Tests

- Question Frame, Preconditions, Structured และ Fast ได้ object identity/result เดียวกัน
- call counter ของ game resolver เท่ากับ 1
- validator reject candidate แรกแล้ว candidate ที่สอง reuse resolution
- target mismatch หยุด ไม่ลอง capability อื่นเพื่อเปลี่ยน target
- index reload สร้าง key ใหม่โดย request เดิมยังใช้ version snapshot
- context cleanup ทำงานเมื่อ success, exception, timeout และ worker cancellation

### Regression Tests

- KIA-0460 game resolution ไม่เกิน 1 call
- KIA-0486 game resolution ไม่เกิน 1 call
- member cases game resolution 0 call
- known game answersไม่เปลี่ยน target
- unknown game ไม่ถูกลอง fuzzy ซ้ำใน Structured/Fast
- previously-passing FAQ ไม่ลด

### Load Tests

- 30 concurrent requests มี context แยกกัน
- session เดียวหลาย sequential requests ไม่ reuse context
- memory หลัง 10,000 requests กลับใกล้ warm baseline
- kill worker กลาง request แล้ว parent ไม่มี global context leak

## 11. Acceptance Criteria แบบวัดค่าได้

- game resolution ต่อ key ไม่เกินหนึ่งครั้งทุก request
- KIA-0460 และ KIA-0486 ไม่มี duplicate lookup ใน trace
- KIA-0460 และ KIA-0486 total pipeline time ไม่เกิน 1.5 วินาทีเมื่อ resolver 71 เปิด
- candidate retry ไม่เกิน 1
- context limits ไม่เคยเกิน hard bound
- target/version ของ reused result ตรง original Question Frame
- ไม่มี result ข้าม request หรือ session
- ไม่มี context memory growth ต่อเนื่องหลัง load test
- strict FAQ scoreไม่ต่ำกว่า 91.00% และไม่มี previously-passing case ตกจาก dedup
- controlled timeout และ worker crash คืน resource/context ครบ

## 12. Rollback และ Compatibility

- เพิ่ม context เป็น optional argument ชั่วคราวได้ แต่ production path ต้องสร้างเสมอหลัง rollout
- consumers รุ่นเก่าสามารถเรียก adapter ที่สร้าง context เฉพาะ request ได้
- response API ไม่เปลี่ยน
- เปิด shadow counters ก่อนใช้ cached result เปลี่ยน behavior
- หาก accuracy ลด ให้ปิด reuse ของ capability outputก่อน แต่คง reuse ของ immutable GameResolution ที่ผ่าน tests
- หาก memory สูง ให้ลด limits ไม่เปลี่ยนเป็น global cache
- rollback ห้ามลบ reason/counters เพราะต้องใช้วิเคราะห์

Rollback triggers:

- target mismatch เพิ่มแม้แต่หนึ่ง known case
- cross-request contamination
- context P99 memory สูงกว่าค่าที่กำหนด
- latency P95 แย่ลงเกิน 10%
- previously-passing regression

## 13. Dependencies และลิงก์ไปเอกสารอื่น

- [67 Master Plan](67_timeout_reliability_remediation_master_plan_20260901.md)
- [68 Baseline และ Regression Corpus](68_slow_case_baseline_and_regression_corpus_plan_20260901.md)
- [69 RequestBudget และ Worker Supervisor](69_hard_deadline_and_pipeline_worker_supervision_plan_20260901.md)
- [70 Member Routing](70_member_about_us_routing_correction_plan_20260901.md)
- [71 Bounded Game Resolver](71_bounded_game_entity_resolver_plan_20260901.md)
- [73 Target-grounded RAG](73_budgeted_target_grounded_rag_retrieval_plan_20260901.md)
- [74 Local LLM Budget](74_local_llm_budget_health_and_fallback_plan_20260901.md)
- [76 Observability](76_crash_resilient_stage_observability_plan_20260901.md)
- [77 End-to-end Verification](77_end_to_end_sla_load_test_and_rollout_plan_20260901.md)
- [66 Current Flow Regression](66_current_flow_full_model_regression_20260901.md)

Implementation dependency: Context ใช้ RequestBudget จาก 69, GameResolution จาก 71 และ Frame/retrieval fingerprints จาก 70/73; Observability 76 ต้องพร้อมเพื่อพิสูจน์ว่า operation ไม่เกิดซ้ำจริง
