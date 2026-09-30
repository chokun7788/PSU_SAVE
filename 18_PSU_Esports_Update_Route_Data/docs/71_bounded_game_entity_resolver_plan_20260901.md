# Implementation Plan: Bounded Game Entity Resolver

วันที่จัดทำ: 1 กันยายน 2026

สถานะ: **not_started**

Owner ที่แนะนำ: Entity Resolution / Runtime

อ้างอิงหลัก: [Master Plan 67](67_timeout_reliability_remediation_master_plan_20260901.md)

## 1. เป้าหมายและสถานะปัจจุบัน

เป้าหมายคือแทนที่การค้นชื่อเกมแบบ fuzzy ที่เปรียบเทียบ query กับ alias จำนวนมากและเลื่อนหน้าต่างตัวอักษรทุกตำแหน่ง ด้วย **GameResolver** กลางที่สร้าง index ตอน Startup, จำกัด candidate และจำนวน comparison, ตรวจ deadline ภายใน loop และคืนผลชนิดเดียวให้ทุก Pipeline component ใช้ร่วมกัน

ผลลัพธ์ที่ต้องได้:

- ชื่อเกมหรือ alias ที่ตรงชัดเจนตอบได้ทันที
- typo เล็กน้อยค้นได้โดยไม่สแกน alias ทั้งหมด
- ชื่อสั้นหรือชื่อ franchise ที่กำกวมไม่ถูกบังคับให้ match
- unknown English title จบเป็น unknown อย่างรวดเร็ว
- JSON, ข้อความหลายคำถาม และข้อความที่มี title ปะปนไม่ทำให้เวลาโตตามจำนวนตัวอักษรคูณจำนวน alias
- resolver มี P99 ต่ำกว่า 250 มิลลิวินาที

งานนี้ไม่สร้าง alias handler รายเกม และไม่เพิ่ม dependency ภายนอกในรอบแรก ใช้ Python standard library, character trigram inverted index และ difflib.SequenceMatcher เฉพาะ shortlist

## 2. หลักฐานจาก Log/Code พร้อม Case ID

### 2.1 สิ่งที่ยืนยันจาก Log

- **KIA-0460** ใช้ structured ประมาณ 2.027 วินาที และ deterministic ประมาณ 17.348 วินาที รวมประมาณ 19.927 วินาที โดยไม่เรียก LLM
- **KIA-0486** ใช้ structured ประมาณ 3.649 วินาที และ deterministic ประมาณ 23.875 วินาที รวมประมาณ 28.102 วินาที โดยไม่เรียก LLM
- MB-0499 มี trace/analysis ว่าคำถามบุคลากรเข้า game fuzzy lookup
- Slow cases ที่ไม่ใช้ LLM แสดงว่าปัญหานี้ไม่ใช่ model generation latency
- Worker log ก่อน KIA-0487 สิ้นสุดที่ KIA-0486 จึงห้ามผูก crash กับข้อความ Hollow Knight โดยไม่มี event ระดับ stage

หลักฐานอ่านได้จาก:

- [Raw results](../reports/current_flow_regression/20260901_full_model_enabled/results.jsonl)
- [Per-case analysis](../reports/current_flow_regression/20260901_full_model_enabled/analysis/per_case_analysis.jsonl)
- [รายงาน 66](66_current_flow_full_model_regression_20260901.md)

### 2.2 สิ่งที่ยืนยันจาก Code

- app/core/normalization.py ใช้ SequenceMatcher
- ฟังก์ชัน **_best_compact_window_ratio** สร้าง substring windows หลายขนาดและหลายตำแหน่ง
- **contains_alias** ทำ exact checks ก่อน แล้วใน fuzzy mode วน aliases, token windows และ compact windows
- app/runtime/fast_answer.py โหลด alias จาก game detail และ game_title_aliases.jsonl หลายแหล่ง
- Structured, target resolution และ fast answer มีโอกาสเรียก alias matching แยกกัน
- index ที่โหลดข้อมูลบางส่วนไม่ได้ทำหน้าที่เป็น resolver กลางที่มี comparison ceiling และ deadline contract

### 2.3 ข้อสันนิษฐานที่ต้องทดสอบ

- native access violation เกิดจาก SequenceMatcher หรือ native library อื่นยังไม่ยืนยัน
- จำนวน alias จริงต่อ release และ distribution ของ alias length ต้องเก็บเป็น startup metric
- threshold 0.88 และ margin 0.08 เป็นค่าเริ่มต้นจากการออกแบบ ต้อง tune ด้วย regression corpus ไม่ใช่ถือเป็นค่าจริงถาวร
- character trigram อาจให้ recall ต่ำสำหรับ alias ไทยที่สั้นมาก จึงต้องมี exact/compact path และ policy สำหรับ short alias

## 3. Root Cause และสิ่งที่ยังพิสูจน์ไม่ได้

### Root Cause ที่ยืนยันได้

1. **Unbounded search surface**: fuzzy matching เดิมวน candidate aliases จำนวนมาก
2. **Nested comparison cost**: compact window ทำให้ cost ขึ้นกับ query length, alias length และจำนวน aliasพร้อมกัน
3. **No hard comparison ceiling**: ไม่มีขีดสูงสุดต่อ request ที่บังคับเสมอ
4. **No internal deadline checkpoint**: cooperative deadline ภายนอกไม่หยุด loop ที่กำลังทำงาน
5. **No canonical shared result**: หลาย stage สามารถ resolve เกมเดิมซ้ำ
6. **Unknown query worst case**: query ที่ไม่ตรงอะไรต้องตรวจ candidates จำนวนมากก่อนสรุป unknown

### สิ่งที่ยังพิสูจน์ไม่ได้

- ยังไม่ทราบว่า bottleneck ส่วนใดระหว่าง normalization, window generation และ SequenceMatcher มากที่สุดใน Production CPU
- ยังไม่ทราบ memory overhead ของ trigram index บน catalog รุ่นถัดไป
- ยังไม่ทราบ threshold ที่เหมาะกับภาษาไทยและอังกฤษทุก family
- ยังไม่พิสูจน์ว่า resolver ใหม่ลด crash; เป้าหมายตรงนี้คือจำกัดเวลาและแยกสาเหตุ

## 4. Target Behavior และ Invariants

ส่วนนี้เป็น **การออกแบบที่เสนอ (Proposed Design)** ค่า threshold และ limit ต้องยืนยันจาก corpus ก่อนเปิดใช้จริง

### Search Pipeline

1. Normalize query ครั้งเดียว
2. ตรวจ exact normalized map
3. ตรวจ exact compact map
4. Extract phrase candidates แบบ bounded
5. สร้าง trigrams และดึง alias IDs จาก inverted index
6. คำนวณ cheap overlap score แล้วเลือก top 8
7. ใช้ SequenceMatcher rerank เฉพาะ shortlist
8. ตัดสิน matched, ambiguous หรือ unknown จาก threshold และ margin
9. คืน GameResolution พร้อม method และ counters

### Invariants

- candidate_limit ไม่เกิน 8
- fuzzy comparison count ไม่เกิน 64 ต่อ resolution
- stage elapsed ceiling 0.25 วินาที
- deadline checkpoint ก่อนและหลัง candidate ทุกตัว
- ไม่มีการเรียก _best_compact_window_ratio บน catalog ทั้งชุด
- exact match ต้องไม่เข้าสู่ fuzzy path
- alias ที่สั้นกว่า policy ห้าม fuzzy match
- unknown target ไม่ถูกเปลี่ยนเป็นเกมที่คะแนนต่ำ
- catalog version และ index version ต้องตรงกัน
- resolver ไม่มี side effect และผลลัพธ์ immutable

## 5. Mermaid Flow/Sequence Diagram

### Target Resolver Flow

~~~mermaid
flowchart TD
    Q[Raw query] --> N[Normalize once]
    N --> X{Exact normalized map}
    X -->|hit| M[Matched: exact]
    X -->|miss| C{Exact compact map}
    C -->|hit unique| MC[Matched: compact]
    C -->|ambiguous| A[Ambiguous]
    C -->|miss| P[Bounded phrase extraction]
    P --> T[Trigram lookup]
    T --> S[Cheap score + top 8]
    S --> B{Budget and comparison ceiling}
    B -->|insufficient| U[Unknown or deadline_exceeded]
    B -->|allowed| F[SequenceMatcher rerank]
    F --> D{score >= .88 and margin >= .08}
    D -->|yes| MF[Matched: fuzzy]
    D -->|low margin| A
    D -->|low score| U
~~~

### Startup and Request Sequence

~~~mermaid
sequenceDiagram
    participant S as Startup
    participant C as Canonical Catalog
    participant I as GameResolverIndex
    participant P as Pipeline Request
    participant B as RequestBudget
    S->>C: load one release/version
    C->>I: build exact, compact and trigram maps
    I-->>S: immutable index + metrics
    P->>B: allow game_resolution 0.25s
    P->>I: resolve query with deadline
    loop at most 8 shortlisted candidates
        I->>B: checkpoint
    end
    I-->>P: GameResolution + counters
~~~

## 6. Interface, Data Structure, Config และ pseudocode

### 6.1 GameResolution contract

~~~python
@dataclass(frozen=True)
class GameCandidate:
    canonical_id: str
    canonical_name: str
    matched_alias: str
    cheap_score: float
    fuzzy_score: float

@dataclass(frozen=True)
class GameResolution:
    status: Literal[
        "matched", "ambiguous", "unknown", "deadline_exceeded"
    ]
    canonical_id: str | None
    canonical_name: str | None
    score: float
    margin: float
    candidates: tuple[GameCandidate, ...]
    method: Literal[
        "exact", "compact", "trigram_fuzzy", "none", "budget"
    ]
    catalog_version: str
    candidate_count: int
    comparison_count: int
    elapsed_ms: float
~~~

Consumers ต้องอ่าน status ก่อน canonical_id เสมอ ห้ามถือว่า candidate แรกคือคำตอบ

### 6.2 Index contract

~~~python
@dataclass(frozen=True)
class GameResolverIndex:
    catalog_version: str
    exact_map: Mapping[str, tuple[AliasRecord, ...]]
    compact_map: Mapping[str, tuple[AliasRecord, ...]]
    trigram_postings: Mapping[str, tuple[int, ...]]
    alias_records: tuple[AliasRecord, ...]
~~~

Index สร้างครั้งเดียวต่อ catalog version แล้วเผยแพร่แบบ atomic; request ที่เริ่มก่อน reload ใช้ index เก่าจนจบ request

### 6.3 Normalization policy

- Unicode normalization ตาม utility เดิม
- lowercase สำหรับ Latin
- normalize whitespace และ punctuation ที่ไม่เปลี่ยนความหมาย
- compact form ตัดเฉพาะ separator ที่ policy อนุญาต
- ไม่ transliterate ไทยเป็นอังกฤษใน resolver รอบแรก
- จำกัด query สำหรับ entity extraction เช่น 512 normalized characters
- เก็บ phrase สูงสุด 16 ช่วง แต่ละช่วงมีความยาวสูงสุดตาม catalog alias

### 6.4 Trigram shortlist

~~~python
def make_trigrams(text):
    padded = "  " + text + "  "
    return unique(padded[i:i+3] for i in range(len(padded) - 2))

def cheap_score(query_grams, alias_grams):
    intersection = len(query_grams & alias_grams)
    union = len(query_grams | alias_grams)
    return intersection / union if union else 0.0
~~~

สำหรับ alias ความยาวต่ำกว่า 4:

- exact normalized และ exact compact เท่านั้น
- fuzzy disabled เป็นค่าเริ่มต้น
- short alias เช่น CS2, ROV, GT7 ต้องอยู่ exact map อย่างชัดเจน

### 6.5 Resolve pseudocode

~~~python
def resolve(query, budget, index, config):
    started = monotonic()
    budget.checkpoint("game_resolution")
    normalized = normalize_once(query)

    exact = unique_target(index.exact_map.get(normalized))
    if exact:
        return matched(exact, "exact")

    compact = compact_once(normalized)
    exact_compact = unique_target(index.compact_map.get(compact))
    if exact_compact:
        return matched(exact_compact, "compact")

    phrases = extract_phrases_bounded(normalized, limit=16)
    ranked = trigram_shortlist(phrases, index, limit=8)

    scored = []
    comparisons = 0
    for candidate in ranked:
        budget.checkpoint("game_resolution")
        if comparisons >= 64:
            break
        score = sequence_ratio(best_phrase(candidate), candidate.alias)
        comparisons += 1
        scored.append((candidate, score))

    return decide(scored, threshold=0.88, margin=0.08)
~~~

หาก budget หมดระหว่าง fuzzy และยังไม่มี exact result ให้คืน deadline_exceeded; consumer ต้องใช้ clarification/no-answer ห้ามใช้ partial top candidate

### 6.6 Config defaults

| Config | Default | Hard bound |
|---|---:|---:|
| PSU_GAME_RESOLVER_STAGE_MS | 250 | 250 |
| PSU_GAME_RESOLVER_CANDIDATES | 8 | 16 |
| PSU_GAME_RESOLVER_COMPARISONS | 64 | 128 |
| PSU_GAME_FUZZY_THRESHOLD | 0.88 | 0.80–0.98 |
| PSU_GAME_FUZZY_MARGIN | 0.08 | 0.03–0.20 |
| PSU_GAME_QUERY_MAX_CHARS | 512 | 1024 |
| PSU_GAME_PHRASE_LIMIT | 16 | 32 |
| PSU_GAME_RESOLVER_SHADOW | true | boolean |

ค่า hard bound ต้อง enforce แม้ environment ตั้งสูงกว่านั้น

### 6.7 Index build validation

- canonical_id ทุกตัว unique
- normalized alias ว่างไม่ได้
- alias collision เก็บทุก target และทำให้ exact result ambiguous
- catalog version ต้องมีค่า
- trigram posting IDs อยู่ในช่วง
- index checksum log ตอน Startup
- build ล้มให้คง index release ก่อนหน้าและ mark stale; ห้ามเผยแพร่ index ครึ่งชุด

## 7. ขั้นตอน Implement ตามลำดับ

1. สร้าง resolver benchmark จาก known, typo, ambiguous และ unknown cases ในเอกสาร 68
2. Instrument resolver เดิมด้วย alias count, window count, comparison count และ elapsed โดยไม่เก็บ alias text
3. สร้าง GameResolution และ GameResolver protocol โดยยังไม่เปลี่ยน consumer
4. สร้าง catalog adapter ที่รวม alias ทุกแหล่งเป็น canonical records หนึ่งครั้ง
5. Implement exact normalized และ compact maps
6. Implement trigram posting index พร้อม build validation
7. Implement bounded phrase extraction และ top-k shortlist
8. Implement SequenceMatcher rerank เฉพาะ top 8
9. เพิ่ม threshold, margin, comparison ceiling และ RequestBudget checkpoint
10. เพิ่ม shadow mode เรียก resolver ใหม่ควบคู่เฉพาะ sample ที่มีงบ แต่ใช้ผลเก่าตอบ
11. วิเคราะห์ disagreement แยก matched/ambiguous/unknown
12. ปรับ threshold ด้วย corpus โดยให้ false cross-game match มีความสำคัญสูงกว่า recall
13. เชื่อม Question Frame, Structured และ Fast ผ่าน RequestExecutionContext ตามเอกสาร 72
14. ปิด full-scan path หลัง regression ผ่าน
15. ลบหรือ deprecate call site ของ _best_compact_window_ratio สำหรับ game entity โดยไม่ลบ utility ที่ domain อื่นอาจยังใช้

## 8. Failure Modes และ Safe Fallback

| Failure | Detection | Safe Fallback |
|---|---|---|
| Alias collision | exact map มีหลาย canonical IDs | ambiguous และถามชื่อเต็ม/แพลตฟอร์ม |
| Fuzzy score ต่ำ | top score ต่ำกว่า 0.88 | unknown |
| Margin ต่ำ | top1-top2 ต่ำกว่า 0.08 | ambiguous พร้อมตัวเลือกสูงสุด 3 |
| Budget หมด | checkpoint exception | deadline_exceeded และ no-answer |
| Index build ล้ม | validation/build exception | ใช้ index release ก่อนหน้าแบบ stale พร้อม alert |
| Catalog version mismatch | context version ไม่ตรง index | ห้าม resolve; reload หรือ Safe Outcome |
| Query ยาวมาก | เกิน max chars | extract จาก bounded prefix/segments หรือ no-answer |
| JSON input | parser แยก user text ได้ | resolve เฉพาะ field ที่อนุญาต ไม่ scan serialized object ทั้งก้อน |
| Unknown English title | ไม่มี shortlist ที่ผ่าน | unknown ภายใน budget |

Safe Fallback ต้องไม่ตอบชื่อเกมจาก top candidate เมื่อ status ไม่ใช่ matched

## 9. Logging/Metrics ที่ต้องเพิ่ม

Events:

- game_resolver_started
- game_resolver_exact_hit
- game_resolver_shortlist_built
- game_resolver_candidate_progress
- game_resolver_finished
- game_resolver_budget_exceeded
- game_resolver_shadow_disagreement
- game_index_built
- game_index_build_failed

Fields:

- request_id, worker_id, index_version
- query_length และ script classes แต่ไม่เก็บ query เต็มใน performance log
- method, status, score bucket, margin bucket
- phrase_count, trigram_count, posting_count
- shortlisted_count, comparison_count
- elapsed_ms, remaining_ms
- cache_hit และ reused_request_resolution

Metrics:

- resolver latency P50/P95/P99/Max
- exact/compact/fuzzy/unknown/ambiguous rate
- comparisons P95/Max
- deadline_exceeded rate
- cross-game false match rate
- shadow disagreement rate
- index build time, alias count, collision count และ memory estimate

## 10. Unit, Integration, Regression และ Load Tests

### Unit Tests

- trigram generation deterministic
- exact map และ compact map resolve unique target
- alias collision คืน ambiguous
- short alias ไม่เข้าสู่ fuzzy
- top-k จำกัดไม่เกิน 8
- comparison counter ไม่เกิน 64
- threshold และ margin behavior
- deadline ก่อนเริ่มและระหว่าง loop
- catalog version mismatch
- immutable index ไม่ถูกแก้ระหว่าง request

### Dataset Coverage

- canonical names ไทย/อังกฤษ
- alias ทางการและคำเรียกทั่วไป
- typo เพิ่ม/หาย/สลับหนึ่งถึงสองตัว
- keyboard-layout text ต้องผ่าน Guard ก่อน ไม่ให้ resolverเดาเอง
- short titles เช่น ROV, CS2, GT7
- franchise เช่น Mario, Resident Evil, Call of Duty
- known game พร้อม platform qualifier
- unknown title อย่างน้อย 25 ข้อ
- non-game strings ที่คล้าย title อย่างน้อย 25 ข้อ
- long mixed text, multi-question และ JSON payload

### Integration Tests

- Question Frame ใช้ GameResolution เดียวกับ Structured/Fast
- matched result เลือก structured game detail ถูก target
- ambiguous result ไป clarification
- unknown result ไป no-answer/RAG แบบ target-unknown policy
- RequestBudget เหลือน้อยไม่เริ่ม fuzzy
- index reload ระหว่าง request ไม่ทำให้ version ผสม

### Performance Tests

- cold index build แยกจาก request latency
- warm resolve 10,000 iterations โดย report P50/P95/P99/Max
- adversarial long unknown query
- all aliases share common trigram
- concurrent 30 usersอ่าน immutable index
- worker recycle และ reload

## 11. Acceptance Criteria แบบวัดค่าได้

- resolver P99 ต่ำกว่า 250 มิลลิวินาทีบน target server
- request ใดไม่มี comparison เกิน 64 และ shortlist เกิน 8
- exact match P99 ต่ำกว่า 20 มิลลิวินาที
- unknown title จบภายใน 250 มิลลิวินาที
- false match ข้ามเกมเป็น 0 ใน regression corpus
- known exact/alias recall ไม่ต่ำกว่า baseline
- ambiguous family ไม่ถูกบังคับเป็นเกมเดียว
- KIA-0460 และ KIA-0486 ไม่มี full catalog/window scan
- deadline_exceeded ไม่ส่ง partial candidate เป็น factual target
- resolver index version ตรง Structured/RAG release
- ไม่มี request เกิน Global SLA จาก resolver

## 12. Rollback และ Compatibility

- GameResolution เป็น interface ใหม่ แต่ adapter สามารถแปลงกลับ tuple เดิมระหว่าง migration
- เปิด **PSU_GAME_RESOLVER_SHADOW** ก่อนเปลี่ยนผลตอบ
- รักษา alias data format เดิม; index เป็น projection ที่สร้างจาก canonical release
- หาก known recall ลด ให้กลับไป old resolver เฉพาะ matched behavior แต่คง hard deadline/supervisor ไว้
- ห้าม rollback ไป unbounded fuzzy ใน Production โดยไม่มี worker isolation
- เก็บ old/new resolver metrics แยก version
- cache key ต้องมี resolver_version เพื่อไม่ใช้ผลข้าม implementation

Rollback triggers:

- cross-game false match มากกว่า 0
- known recall ลดเกิน 0.5 percentage point
- P99 เกิน 250 มิลลิวินาที
- index build failure ในสอง release ติดต่อกัน
- memory ของ index เกิน budget ที่กำหนดจาก target server

## 13. Dependencies และลิงก์ไปเอกสารอื่น

- [67 Master Plan](67_timeout_reliability_remediation_master_plan_20260901.md)
- [68 Baseline และ Regression Corpus](68_slow_case_baseline_and_regression_corpus_plan_20260901.md)
- [69 Hard Deadline](69_hard_deadline_and_pipeline_worker_supervision_plan_20260901.md)
- [70 Member Routing Correction](70_member_about_us_routing_correction_plan_20260901.md)
- [72 Structured/Fast Deduplication](72_structured_fast_resolution_deduplication_plan_20260901.md)
- [73 Target-grounded RAG](73_budgeted_target_grounded_rag_retrieval_plan_20260901.md)
- [75 Windows Worker Crash Diagnosis](75_windows_worker_crash_diagnosis_and_recovery_plan_20260901.md)
- [76 Observability](76_crash_resilient_stage_observability_plan_20260901.md)
- [77 SLA และ Rollout](77_end_to_end_sla_load_test_and_rollout_plan_20260901.md)
- [66 Current Flow Regression](66_current_flow_full_model_regression_20260901.md)

Implementation dependency: ต้องมี RequestBudget จาก 69 สำหรับ hard checkpoint, RequestExecutionContext จาก 72 สำหรับ reuse และ Parent Logger events จาก 76 ก่อนเปิด resolver ใหม่เต็มรูปแบบ
