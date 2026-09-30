# Implementation Plan: Member / About Us Routing Correction

วันที่จัดทำ: 1 กันยายน 2026

สถานะ: **not_started**

Owner ที่แนะนำ: Pipeline Routing / Structured Data

อ้างอิงหลัก: [Master Plan 67](67_timeout_reliability_remediation_master_plan_20260901.md)

## 1. เป้าหมายและสถานะปัจจุบัน

เป้าหมายของงานนี้คือทำให้คำถามเกี่ยวกับบุคลากร สมาชิก ตำแหน่ง และผู้รับผิดชอบของ PSU Esports Studio เดินทางไปยัง **structured.members** โดยตรง ไม่ถูก Semantic Route Lock เปลี่ยนเป็นเส้นทางกว้าง และไม่แตะ Game Resolver, Equipment Resolver หรือ broad multi-domain handler โดยไม่จำเป็น

ขอบเขตที่ต้องรองรับ:

- ถามรายชื่อสมาชิกทั้งหมด
- ถามจำนวนสมาชิก
- ค้นหาบุคคลจากชื่อหรือ alias
- ถามบุคคลจากตำแหน่ง เช่น หัวหน้า ผู้ดูแล หรือประธาน
- ถามหลายบุคคลในคำถามเดียว
- ถามบุคคลที่ไม่มีในข้อมูล
- ชื่อหรือตำแหน่งที่ตรงได้มากกว่าหนึ่งคน
- ข้อมูลบุคลากรที่มี effective date หรือ version

สถานะปัจจุบันคือ Pipeline มี **structured.members** อยู่แล้ว แต่ลำดับการ Route ทำให้ Semantic evidence สามารถล็อก category เป็น **about_us** ก่อน Question Frame และ Universal Intent จะตัดสินว่าเป็น member lookup หลังจากนั้น Semantic Route Veto จะคืน route เดิม ทำให้เส้นทางสมาชิกสูญเสียสิทธิ์เลือก capability ที่เฉพาะเจาะจง

สิ่งที่งานนี้ไม่ทำ:

- ไม่สร้าง runtime route ชื่อ members หรือ about_us เพิ่ม
- ไม่สร้าง handler แยกตามชื่อบุคคล
- ไม่ให้ LLM ตัดสินรายชื่อ ตำแหน่ง หรือจำนวนสมาชิก
- ไม่เปลี่ยน schema ของข้อมูลบุคลากรในรอบเดียวกัน หาก schema เดิมให้ข้อมูลเพียงพอ

## 2. หลักฐานจาก Log/Code พร้อม Case ID

### 2.1 สิ่งที่ยืนยันจาก Log

- ชุดทดสอบ 2,116 ข้อมี FAQ เกิน 10 วินาที 10 ข้อ โดยกลุ่ม **MB-0499-M-010**, **MB-0500**, **MB-0501**, **MB-0503**, **MB-0507**, **MB-0518**, **MB-0519**, **MB-0618**, **MB-1229** และ **MB-1232** มีสัญญาณร่วมว่าเป็นคำถามบุคลากรหรือตำแหน่งแล้วไปใช้ขั้นค้นหาเกมหรือ broad deterministic handlers
- MB-0501 ใช้ Intent ประมาณ 7.777 วินาที, deterministic ประมาณ 7.400 วินาที และ vector ประมาณ 4.805 วินาที
- MB-0519 ใช้ Intent ประมาณ 7.810 วินาที, deterministic ประมาณ 11.605 วินาที และ vector ประมาณ 4.684 วินาที
- MB-0499 ถูกสรุปในรายงาน 66 ว่าเป็นคำถามบุคลากรที่ค้างใน game fuzzy lookup
- MB-1228-M-048 มีเนื้อหาคำตอบสอดคล้อง contract แต่ label เป็น about_us แทน members จึงยืนยันว่าปัญหาบางส่วนเป็น route/category mismatch ไม่ใช่ factual answer ผิด

Raw evidence:

- [ผลรายข้อ](../reports/current_flow_regression/20260901_full_model_enabled/analysis/per_case_analysis.jsonl)
- [Raw outputs และ Trace](../reports/current_flow_regression/20260901_full_model_enabled/results.jsonl)
- [Cases requiring review](../reports/current_flow_regression/20260901_full_model_enabled/analysis/cases_requiring_review.md)

### 2.2 สิ่งที่ยืนยันจาก Code

- app/pipeline/engine.py เรียก **refine_route_with_semantic_evidence** ก่อนสร้าง Universal Intent และ Question Frame ในช่วงหลักของ Pipeline
- app/pipeline/engine.py เก็บ semantic route ที่มี route_lock และสามารถ restore route นั้นภายหลัง Universal Intent refinement
- app/pipeline/engine.py ฟังก์ชัน **_handlers_for_route** รองรับ overview แต่ไม่รองรับ about_us; category ที่ไม่รู้จักตกไป default handler ซึ่งเรียก price, schedule, equipment, games และ static domain
- app/pipeline/capability_registry.py มี **structured.members** และให้ bonus แก่ operation member_lookup อยู่แล้ว
- app/pipeline/question_frame.py ยอมรับ about_us เป็น semantic category และสามารถสร้าง operation semantic_evidence_lookup ซึ่งบดบัง member_lookup
- app/pipeline/semantic_vector_retrieval.py สามารถสร้าง route lock สำหรับ about_us

### 2.3 ข้อสันนิษฐานที่ต้องทดสอบ

- ทั้ง 10 FAQ ช้าจาก root cause เดียวกันทั้งหมดหรือไม่ ต้องยืนยันด้วย stage event หลังเพิ่ม Observability ตามเอกสาร 76
- structured member store มี alias และ effective date ครบเพียงใด
- คำว่า “ทีม”, “สมาชิกทีม” หรือชื่อตำแหน่งบางคำอาจชนกับคำศัพท์ในเกม ต้องทดสอบ corpus จริง
- รายชื่อบุคลากรอาจมีชื่อซ้ำหรือ role เดียวกันหลายคน จึงห้ามออกแบบโดยสมมติว่า role เป็น unique key

## 3. Root Cause และสิ่งที่ยังพิสูจน์ไม่ได้

### Root Cause ที่ยืนยันได้

1. **Ordering defect**: Question Frame ซึ่งเป็นคำอธิบายความต้องการของผู้ใช้ถูกสร้างหลัง Semantic Route Refinement
2. **Semantic/runtime namespace collision**: about_us ถูกใช้ทั้งเป็น evidence category และเสมือน runtime route ทั้งที่ handler registry ไม่ได้รองรับแบบปิด
3. **Route lock precedence สูงเกินไป**: Semantic evidence สามารถ veto Universal Intent ที่เฉพาะกว่า
4. **Unsafe broad fallback**: unknown runtime category เรียกหลาย handler รวมถึงเกม ทำให้ latency และ false route ขยาย
5. **Exact structured query ยังเรียก LLM ได้**: member lookup บางข้อผ่าน Intent LLM ทั้งที่ deterministic signal เพียงพอ

### สิ่งที่ยังพิสูจน์ไม่ได้

- ยังห้ามสรุปว่า Game Resolver เป็นสาเหตุของ worker crash; มีเพียงความสัมพันธ์เชิงเวลาในบาง case
- ยังไม่ทราบ P50/P95 ของ member lookup หลังตัด LLM เพราะยังไม่มี focused benchmark
- ยังไม่ยืนยันว่าเอกสาร about_us ทุกชิ้น map สู่ member records ได้หนึ่งต่อหนึ่ง
- ยังไม่ยืนยันข้อมูลบุคลากร Production ว่ามีช่วงเวลามีผลย้อนหลังหรือไม่

## 4. Target Behavior และ Invariants

ส่วนนี้เป็น **การออกแบบที่เสนอ (Proposed Design)** ไม่ใช่คำอธิบาย behavior ที่ Source Code ปัจจุบันทำได้แล้ว

### Target Behavior

1. สร้าง **QuestionFrame** จาก normalized query, deterministic intent signal และ preliminary route ก่อน Semantic Retrieval
2. หาก Frame operation เป็น member_lookup, member_list หรือ member_count ให้ runtime route เป็น **overview**
3. เก็บ **about_us** เป็น evidence_category ใน metadata เท่านั้น
4. Universal Intent members/role_lookup ต้อง map ไป **structured.members**
5. Candidate Scoring ต้องให้ structured.members ชนะ fast.domain_handlers อย่างชัดเจน
6. Tool Preconditions ต้อง veto games, equipment, price, schedule และ broad multi-domain handler
7. Exact member lookup ไม่เรียก Intent LLM และไม่เรียก Composer
8. ถ้าชื่อหรือตำแหน่งกำกวม ให้ถาม clarification จาก candidate จริง ไม่สร้างชื่อใหม่
9. ถ้าไม่พบข้อมูล ให้ Safe Outcome พร้อมระบุว่าไม่พบในข้อมูลที่เผยแพร่

### Invariants

- **runtime_route.category = overview** สำหรับ member operations
- **evidence_category = about_us** ใช้เพื่อกรองแหล่งข้อมูลเท่านั้น
- GameResolver call count ต้องเป็น 0
- LLM call count ต้องเป็น 0 สำหรับ exact/list/count
- structured.members เป็น capability เดียวที่ทำ factual member resolution
- ไม่ใช้ broad fallback เมื่อ operation ถูกระบุแล้ว
- คำตอบต้องอ้างอิง release/version เดียวกับ Structured Store
- ไม่แสดงข้อมูลส่วนบุคคลที่ไม่มีสถานะ public

## 5. Mermaid Flow/Sequence Diagram

### Current Flow ที่มีปัญหา

~~~mermaid
flowchart TD
    Q[Member question] --> R[Preliminary route: overview]
    R --> S[Semantic route refinement]
    S --> L[Route lock: about_us]
    L --> I[Universal intent: member lookup]
    I --> V[Semantic veto restores about_us]
    V --> H[Unknown broad handler fallback]
    H --> G[Price + Schedule + Equipment + Games + Static]
    G --> T[Slow or timeout]
~~~

### Target Flow

~~~mermaid
flowchart TD
    Q[Member question] --> N[Normalize + member/person signals]
    N --> F[Build QuestionFrame]
    F -->|member operation| U[Runtime route: overview]
    F --> E[Evidence category: about_us]
    U --> C[Candidate Scoring]
    E --> C
    C --> P[Tool Preconditions]
    P -->|allow only| M[structured.members]
    M --> X{Unique match?}
    X -->|yes| A[Verified factual answer]
    X -->|multiple| CL[Clarification from real candidates]
    X -->|none| NO[No-answer]
    A --> AC[Answer Contract]
    CL --> AC
    NO --> AC
~~~

### Route Selection Sequence

~~~mermaid
sequenceDiagram
    participant E as Pipeline Engine
    participant F as Question Frame Builder
    participant C as Capability Registry
    participant P as Tool Preconditions
    participant M as Structured Members
    E->>F: build before semantic route lock
    F-->>E: member_lookup + overview + about_us evidence
    E->>C: rank candidates with frame
    C-->>E: structured.members ranked first
    E->>P: validate candidate and invariants
    P-->>E: veto game/equipment/multi handlers
    E->>M: lookup name, role, list or count
    M-->>E: verified result + version + sources
~~~

## 6. Interface, Data Structure, Config และ pseudocode

### 6.1 QuestionFrame extension

เพิ่ม field แบบ backward-compatible ผ่าน metadata ก่อน หากต้องการ type ชัดเจนจึงค่อยย้ายเป็น field ใน release ถัดไป:

~~~python
QuestionFrame(
    operation="member_lookup",
    domain="overview",
    expected_answer_types=("member_profile",),
    targets=(...),
    metadata={
        "runtime_route": "overview",
        "evidence_category": "about_us",
        "member_signal": "role|person|list|count",
    },
)
~~~

ห้ามตั้ง domain เป็น about_us เพราะ domain ถูกใช้เลือก runtime capability

### 6.2 MemberResolution

~~~python
@dataclass(frozen=True)
class MemberResolution:
    status: Literal["matched", "ambiguous", "unknown"]
    member_ids: tuple[str, ...]
    match_method: str
    confidence: float
    candidates: tuple[MemberCandidate, ...]
    source_version: str
~~~

Candidate ต้องมีเฉพาะ public fields:

- member_id
- display_name
- public_role
- aliases ที่อนุญาตค้นหา
- effective_from และ valid_until
- public profile/source reference

### 6.3 Operation mapping

| Signal | Operation | Capability | LLM |
|---|---|---|---|
| ใครคือ, ชื่อบุคคล | member_lookup | structured.members | ไม่ใช้ |
| ตำแหน่ง, ผู้ดูแล, หัวหน้า | role_lookup หรือ member_lookup | structured.members | ไม่ใช้ |
| มีใครบ้าง, รายชื่อ | member_list | structured.members | ไม่ใช้ |
| กี่คน, จำนวนสมาชิก | member_count | structured.members | ไม่ใช้ |
| “เขา”, “คนนั้น” และ session มี antecedent | member_lookup | structured.members | ไม่ใช้ |
| “เขา” แต่ไม่มี antecedent | clarification | ไม่มี tool | ไม่ใช้ |

### 6.4 Candidate Scoring

ค่าเริ่มต้นที่เสนอ:

- structured.members base score ตาม registry เดิม
- member operation bonus อย่างน้อย +0.35
- exact person/role signal bonus +0.15
- fast.domain_handlers penalty -0.40
- retrieval.hybrid_guarded penalty -0.20 เมื่อ exact structured match พร้อม
- game/equipment candidate status เป็น veto ไม่ใช่แค่ลดคะแนน

คะแนนเป็นเพียง ranking; Tool Preconditions เป็นผู้บังคับ invariant ขั้นสุดท้าย

### 6.5 Tool Preconditions

~~~python
def check_member_preconditions(frame, candidate, context):
    if frame.operation not in MEMBER_OPERATIONS:
        return ordinary_preconditions(candidate)

    if candidate.id == "structured.members":
        return ALLOW

    if candidate.domain in {"games", "equipment", "service_fee", "schedule"}:
        return VETO("member_frame_domain_veto")

    if candidate.id in {"fast.domain_handlers", "rulebase.category_rules"}:
        return VETO("member_frame_broad_handler_veto")

    return VETO("member_frame_closed_route")
~~~

### 6.6 Closed handler map

~~~python
ROUTE_HANDLERS = {
    ("overview", "member_lookup"): ("structured.members",),
    ("overview", "member_list"): ("structured.members",),
    ("overview", "member_count"): ("structured.members",),
}
~~~

ห้าม fallback ไป tuple รวมเมื่อ Frame เป็น member operation หาก mapping หายให้ fail closed เป็น Safe Outcome

### 6.7 Feature flags

| Config | Default ตอน rollout | จุดประสงค์ |
|---|---:|---|
| PSU_MEMBER_FRAME_BEFORE_SEMANTIC | false แล้วค่อยเปิด | ย้าย Frame มาก่อน route lock |
| PSU_MEMBER_CLOSED_ROUTE | false แล้วค่อยเปิด | ปิด broad fallback |
| PSU_MEMBER_SKIP_INTENT_LLM | false แล้วค่อยเปิด | exact deterministic bypass |
| PSU_MEMBER_ROUTE_SHADOW | true ช่วงแรก | เปรียบเทียบ old/new route โดยไม่เปลี่ยนคำตอบ |

## 7. ขั้นตอน Implement ตามลำดับ

1. Freeze slow member cases ตามเอกสาร 68 และยืนยัน expected operation/capability
2. เพิ่ม deterministic member/person/role signals ใน Question Frame โดยใช้ข้อมูล alias จาก release เดียวกัน
3. แยก runtime route กับ evidence category ให้ชัดใน QuestionFrame metadata
4. ย้ายการสร้าง Frame ให้เกิดก่อน Semantic Route Lock
5. ปรับ Semantic Route Refinement ให้ about_us ทำหน้าที่กรอง evidence เท่านั้นเมื่อ Frame ระบุ member operation
6. ปรับ Universal Intent mapping ให้ members/role_lookup กลับเป็น overview/member_lookup
7. ปรับ Candidate Scoring ให้ structured.members ชนะอย่างมี margin
8. เพิ่ม member-specific Tool Preconditions แบบ closed route
9. เพิ่ม handler map แบบปิดและลบการตกไป broad default เฉพาะ member frame
10. เพิ่ม exact/list/count bypass สำหรับ Intent LLM และ Composer
11. เชื่อม RequestExecutionContext จากเอกสาร 72 เพื่อบันทึก attempted capability
12. เพิ่ม Answer Contract ตรวจ operation, source version และ public field
13. เปิด shadow flag และเก็บ route disagreement
14. รัน Unit, 10 slow FAQ และ focused member corpus
15. เปิด route correction ก่อน hard rollout เฉพาะเมื่อไม่มี accuracy regression

## 8. Failure Modes และ Safe Fallback

| Failure | Detection | Safe Fallback |
|---|---|---|
| ไม่พบชื่อ | MemberResolution unknown | แจ้งว่าไม่พบในข้อมูลที่เผยแพร่ ไม่เดาชื่อ |
| ชื่อตรงหลายคน | ambiguous และ margin ต่ำ | แสดงตัวเลือกชื่อ/ตำแหน่งที่มีจริงเพื่อถามเพิ่ม |
| role มีหลายคน | มากกว่า 1 active record | ตอบเป็นรายการหรือขอช่วงเวลาเพิ่มเติม |
| Structured Store โหลดไม่ได้ | store unavailable | Safe Outcome และ retryable ตามประเภทระบบผิดพลาด |
| release version ไม่ตรง RAG | version mismatch | ใช้ Structured เท่านั้นและ log mismatch |
| Semantic route พยายาม override | invariant check | คง overview/member operation และบันทึก veto |
| ไม่มี handler mapping | closed route miss | No-answer ห้าม broad fallback |
| Deadline เหลือน้อย | RequestBudget gate | ข้าม retrieval/LLM และใช้ structured draft |

ข้อความ fallback ต้องไม่กล่าวว่าบุคคล “ไม่มีอยู่จริง”; ให้กล่าวเพียงว่า “ไม่พบในข้อมูลที่ระบบเผยแพร่ในขณะนี้”

## 9. Logging/Metrics ที่ต้องเพิ่ม

Event ขั้นต่ำ:

- member_signal_detected
- question_frame_created
- semantic_route_override_blocked
- member_candidate_ranked
- member_precondition_veto
- structured_member_lookup_started/finished
- member_resolution_matched/ambiguous/unknown
- member_exact_llm_bypassed
- answer_contract_member_passed/failed

Fields:

- request_id, worker_id, sequence
- operation, runtime_route, evidence_category
- member_signal ชนิดสัญญาณ ไม่เก็บ query เต็มใน performance log
- candidate_count, top_margin, match_method
- executed_capability
- game_resolver_calls, llm_calls
- source_version
- stage elapsed และ remaining budget

Metrics:

- member_route_accuracy
- member_game_resolver_call_rate เป้าหมาย 0
- member_llm_call_rate สำหรับ exact/list/count เป้าหมาย 0
- member_latency P50/P95/P99/Max
- member_clarification_precision
- member_unknown_rate
- route_shadow_disagreement_rate

## 10. Unit, Integration, Regression และ Load Tests

### Unit Tests

- Question Frame แยก overview runtime route จาก about_us evidence category
- คำว่าใคร, รายชื่อ, กี่คน และตำแหน่ง map สู่ operation ถูกต้อง
- Candidate Scoring ให้ structured.members เป็นอันดับหนึ่ง
- Tool Preconditions veto games/equipment/fast.domain_handlers
- Closed handler ไม่มี broad default
- ambiguous role สร้าง candidates จากข้อมูลจริง
- expired member record ไม่ถูกตอบเป็น active

### Integration Tests

- Exact name → structured.members → Answer Contract โดย game resolver และ LLM call count เป็น 0
- Role lookup ที่มีคนเดียว → factual answer พร้อม source/version
- Role lookup หลายคน → clarification/list ตาม contract
- Multi-person question → list จาก structured records
- Session reference “เขาคนนั้น” มี antecedent → resolve ได้
- ไม่มี antecedent → clarification

### Regression Tests

- 10 FAQ ที่เคยช้าต้องไม่แตะ Game Resolver
- MB-1228 ต้องไม่ตกเพียงเพราะ evidence label about_us
- previously-passing member cases ต้องคงข้อความสำคัญและ source
- non-member about-us เช่น ประวัติองค์กร ยังใช้ evidence about_us ได้
- คำถามเกมที่มีคำว่า “ทีม” ต้องไม่ถูกดึงเป็น member โดยอัตโนมัติ

### Load Tests

- member-only 30 concurrent users
- mixed member/game 30 concurrent users
- ตรวจว่า member exact ไม่รอ LLM semaphore
- ตรวจ session isolation เมื่อหลายคำถามใช้คำสรรพนามพร้อมกัน

## 11. Acceptance Criteria แบบวัดค่าได้

- slow member cases ที่ระบุทั้งหมดมี elapsed ไม่เกิน 1.5 วินาทีใน single-request test
- P99 ของ focused member corpus ไม่เกิน 1.5 วินาทีบน target server
- GameResolver call count เท่ากับ 0 ทุก member case
- Intent LLM และ Composer call count เท่ากับ 0 สำหรับ exact/list/count
- executed_capability เป็น structured.members ทุก matched case
- ไม่มี broad multi-domain handler ใน trace
- runtime route เป็น overview และ evidence category เป็น about_us ตาม invariant
- ambiguous case ไม่ตอบบุคคลผิดและใช้ candidate จริงเท่านั้น
- unknown case ไม่สร้างชื่อ ตำแหน่ง หรือข้อมูลใหม่
- strict FAQ score รวมไม่ต่ำกว่า baseline 91.00% และ previously-passing member case ห้ามตก
- ไม่มี request เกิน Global SLA 10 วินาที

## 12. Rollback และ Compatibility

- ทุกการเปลี่ยน behavior อยู่หลัง feature flags แยกกัน
- response schema เดิมไม่เปลี่ยน; metadata ใหม่เป็น optional
- about_us ใน stored documents ยังใช้ได้ในฐานะ evidence category
- overview route เดิมยังรองรับ static overview question
- หาก shadow disagreement สูงกว่า 1% หรือ member accuracy ลด ให้ปิด MEMBER_FRAME_BEFORE_SEMANTIC ก่อน
- หาก closed route ทำให้ valid about-us question no-answer เพิ่ม ให้ rollback เฉพาะ MEMBER_CLOSED_ROUTE และแก้ Frame classifier
- Rollback ห้ามคืน broad handler ให้ member frameแบบถาวร; ใช้เพื่อเก็บหลักฐานและแก้ mapping เท่านั้น

## 13. Dependencies และลิงก์ไปเอกสารอื่น

- [67 Master Plan](67_timeout_reliability_remediation_master_plan_20260901.md)
- [68 Baseline และ Regression Corpus](68_slow_case_baseline_and_regression_corpus_plan_20260901.md)
- [69 Hard Deadline และ Worker Supervisor](69_hard_deadline_and_pipeline_worker_supervision_plan_20260901.md)
- [71 Bounded Game Resolver](71_bounded_game_entity_resolver_plan_20260901.md)
- [72 Request-scoped Deduplication](72_structured_fast_resolution_deduplication_plan_20260901.md)
- [73 Target-grounded RAG](73_budgeted_target_grounded_rag_retrieval_plan_20260901.md)
- [76 Crash-resilient Observability](76_crash_resilient_stage_observability_plan_20260901.md)
- [77 SLA, Load Test และ Rollout](77_end_to_end_sla_load_test_and_rollout_plan_20260901.md)
- [66 Current Flow Regression](66_current_flow_full_model_regression_20260901.md)

Implementation dependency: ต้องมี baseline IDs จาก 68 และ stage logging ขั้นต่ำจาก 76 ก่อนเปิด production flag ส่วน hard deadline จาก 69 ต้องครอบ lookup ทุกแบบแม้ member path จะเร็วแล้ว
