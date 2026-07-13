from __future__ import annotations

import json
import math
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.rag.ollama_client import ollama_generate
from app.rag.text import compact_text, normalize_text, token_counts


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CORPUS_PATH = PROJECT_ROOT / "data" / "unified" / "unified_knowledge.jsonl"
LEXICAL_INDEX_PATH = PROJECT_ROOT / "data" / "index" / "lexical_index.json"
VECTOR_INDEX_PATH = PROJECT_ROOT / "data" / "index" / "vector_index_ollama.json"


@dataclass(frozen=True)
class SearchHit:
    id: str
    score: float
    lexical_score: float
    vector_score: float
    row: dict[str, Any]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def cosine(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


class HybridRagEngine:
    def __init__(
        self,
        *,
        corpus_path: Path = CORPUS_PATH,
        lexical_index_path: Path = LEXICAL_INDEX_PATH,
        vector_index_path: Path = VECTOR_INDEX_PATH,
    ) -> None:
        self.corpus_path = corpus_path
        self.lexical_index_path = lexical_index_path
        self.vector_index_path = vector_index_path
        self.rows = load_jsonl(corpus_path)
        self.row_by_id = {str(row["id"]): row for row in self.rows}
        self.lexical_index = self._load_json(lexical_index_path)
        self.vector_index = self._load_json(vector_index_path)

    @staticmethod
    def _load_json(path: Path) -> dict[str, Any]:
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))

    def search(
        self,
        query: str,
        *,
        top_k: int = 6,
        category: str | None = None,
        query_embedding: list[float] | None = None,
    ) -> list[SearchHit]:
        lexical_scores = self._lexical_scores(query)
        vector_scores = self._vector_scores(query_embedding) if query_embedding else {}
        all_ids = set(lexical_scores) | set(vector_scores)
        hits: list[SearchHit] = []
        normalized_query = normalize_text(query)
        game_hint = self._game_hint(normalized_query)
        intent_hints = self._intent_hints(normalized_query)
        category_hints = self._category_hints(normalized_query)

        for row_id in all_ids:
            row = self.row_by_id.get(row_id)
            if not row:
                continue
            if category and row.get("category") != category:
                continue
            lexical = lexical_scores.get(row_id, 0.0)
            vector = vector_scores.get(row_id, 0.0)
            priority = float(row.get("priority", 0)) / 100.0
            exact_bonus = self._exact_bonus(normalized_query, row)
            category_bonus = self._category_bonus(category_hints, row)
            service_bonus = self._service_fee_bonus(normalized_query, row)
            game_bonus = self._game_bonus(game_hint, row)
            intent_bonus = self._intent_bonus(intent_hints, row)
            source_bonus = 0.15 if row.get("source_kind") in {"competition_fact_card", "rulebase", "curated_fact"} else 0.0
            score = (0.58 * lexical) + (0.32 * vector) + priority + exact_bonus + category_bonus + service_bonus + game_bonus + intent_bonus + source_bonus
            hits.append(SearchHit(str(row_id), round(score, 5), round(lexical, 5), round(vector, 5), row))

        hits.sort(key=lambda hit: hit.score, reverse=True)
        return hits[:top_k]

    def _lexical_scores(self, query: str) -> dict[str, float]:
        if not self.lexical_index:
            return {}
        query_counts = token_counts(query)
        if not query_counts:
            return {}
        idf = self.lexical_index.get("idf", {})
        documents = self.lexical_index.get("documents", [])
        scores: dict[str, float] = {}
        query_norm = math.sqrt(sum((count * float(idf.get(tok, 1.0))) ** 2 for tok, count in query_counts.items()))
        if query_norm == 0:
            query_norm = 1.0

        for doc in documents:
            doc_counts = doc.get("tokens", {})
            dot = 0.0
            doc_norm = 0.0
            for tok, tf in doc_counts.items():
                weight = float(tf) * float(idf.get(tok, 1.0))
                doc_norm += weight * weight
                if tok in query_counts:
                    dot += weight * float(query_counts[tok]) * float(idf.get(tok, 1.0))
            if dot <= 0:
                continue
            denom = query_norm * math.sqrt(doc_norm or 1.0)
            scores[str(doc["id"])] = dot / denom
        return scores

    def _vector_scores(self, query_embedding: list[float] | None) -> dict[str, float]:
        if not query_embedding or not self.vector_index:
            return {}
        scores: dict[str, float] = {}
        for item in self.vector_index.get("vectors", []):
            scores[str(item["id"])] = cosine(query_embedding, item.get("embedding", []))
        return scores

    @staticmethod
    def _category_hints(normalized_query: str) -> set[str]:
        hints: set[str] = set()
        if any(term in normalized_query for term in ("ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "บาท", "เสียเงิน", "fee", "price", "cost")):
            hints.add("service_fee")
        if any(term in normalized_query for term in ("เปิด", "ปิด", "วันหยุด", "หยุด", "เดือนนี้", "วันนี้", "พรุ่งนี้", "กี่โมง", "เวลา", "calendar", "holiday")):
            hints.add("schedule")
        if any(term in normalized_query for term in ("พัง", "เสียหาย", "ค่าปรับ", "ชดเชย", "ซ่อม", "ปรับ", "ban", "แบน", "penalty")):
            hints.add("penalty")
            hints.add("rules")
        if any(term in normalized_query for term in ("จอง", "เช็คอิน", "checkin", "booking", "reserve", "ยกเลิก", "ชำระ", "จ่าย")):
            hints.add("reservation")
        if any(term in normalized_query for term in ("อุปกรณ์", "สเปค", "spec", "เมาส์", "คีย์บอร์ด", "จอ", "gpu", "cpu", "ram")) and "penalty" not in hints:
            hints.add("equipment")
        if any(term in normalized_query for term in ("cs2", "counter-strike", "counter strike", "rov", "arena of valor", "valorant", "วาโล", "tekken")) and any(term in normalized_query for term in ("กติกา", "แข่ง", "ทีม", "pause", "timeout", "map", "รูปแบบ", "มาสาย", "รอบ", "ผู้เล่น")):
            hints.add("competition_rules")
        return hints

    @staticmethod
    def _category_bonus(category_hints: set[str], row: dict[str, Any]) -> float:
        if not category_hints:
            return 0.0
        category = str(row.get("category", "")).strip()
        if "penalty" in category_hints:
            if category == "penalty":
                return 1.75
            if category == "rules":
                return 0.65
        if "service_fee" in category_hints and category == "service_fee":
            return 1.55
        if "schedule" in category_hints and category == "schedule":
            return 1.55
        if category in category_hints:
            return 1.25
        if category == "competition_rules" and "competition_rules" not in category_hints:
            return -1.35
        if "competition_rules" in category_hints and category != "competition_rules":
            return -0.35
        return -0.15

    @staticmethod
    def _service_fee_bonus(normalized_query: str, row: dict[str, Any]) -> float:
        if row.get("category") != "service_fee":
            return 0.0
        row_text = normalize_text(" ".join(str(row.get(key, "")) for key in ("id", "title", "text", "search_text")))
        score = 0.0
        service_requested = False
        service_aliases = [
            ("vr", ("vr", "virtual reality")),
            ("playstation", ("playstation", "ps5")),
            ("nintendo", ("nintendo", "switch")),
            ("cockpit", ("cockpit", "พวงมาลัย")),
        ]
        for _, aliases in service_aliases:
            if any(alias in normalized_query for alias in aliases):
                service_requested = True
                if any(alias in row_text for alias in aliases):
                    score += 1.2
                else:
                    score -= 0.35
        if any(term in normalized_query for term in ("30 นาที", "ครึ่ง", "ครึ่งชม", "ครึ่งชั่วโมง")):
            score += 0.8 if "30" in row_text else -0.25
        if any(term in normalized_query for term in ("1 ชั่วโมง", "60 นาที", "1 ชม", "หนึ่งชั่วโมง")):
            score += 0.8 if ("60" in row_text or "1 ชั่วโมง" in row_text) else -0.25
        if service_requested and "alias" in str(row.get("id", "")):
            score -= 0.75
        return score

    @staticmethod
    def _intent_hints(normalized_query: str) -> set[str]:
        hints: set[str] = set()
        if any(term in normalized_query for term in ("pause", "timeout", "technical", "emergency", "หยุดเกม", "ขอหยุด", "หลุดเกม", "เกมหลุด", "disconnect")):
            hints.add("pause")
        if any(term in normalized_query for term in ("มาสาย", "ล่าช้า", "late", "late start", "15 นาที", "เริ่มแข่งช้า", "เริ่ม match ช้า")):
            hints.add("late_start")
        if any(term in normalized_query for term in ("กี่คน", "ทีมละ", "สมาชิก", "ผู้เล่น", "team size", "players", "roster", "ตัวสำรอง", "ตัวจริง")):
            hints.add("team_size")
        if any(term in normalized_query for term in ("map", "แผนที่", "map pool", "ban map", "mapban")):
            hints.add("map_pool")
        if any(term in normalized_query for term in ("รูปแบบ", "format", "bo3", "bo5", "single elimination", "1v1", "5v5", "ft2", "round")):
            hints.add("format")
        if any(term in normalized_query for term in ("อุปกรณ์", "เครื่อง", "มือถือ", "tablet", "ipad", "playstation", "ps5", "platform")):
            hints.add("equipment")
        if any(term in normalized_query for term in ("สกิน", "skin", "default skin")):
            hints.add("skin")
        if any(term in normalized_query for term in ("dlc", "ตัวละคร", "character", "agent", "เอเจนท์", "ฮีโร่")):
            hints.add("character")
        return hints

    @staticmethod
    def _intent_bonus(intent_hints: set[str], row: dict[str, Any]) -> float:
        if not intent_hints:
            return 0.0
        row_intent = str(row.get("metadata", {}).get("intent", "") or row.get("intent", "")).strip()
        if not row_intent:
            return 0.0
        if row_intent in intent_hints:
            return 0.85
        if row.get("source_kind") == "competition_fact_card":
            return -0.45
        return -0.15

    @staticmethod
    def _game_hint(normalized_query: str) -> str | None:
        if any(term in normalized_query for term in ("rov", "arena of valor", "aov", "blueket")):
            return "Arena of Valor (RoV)"
        if any(term in normalized_query for term in ("cs2", "counter-strike", "counter strike")):
            return "Counter-Strike 2"
        if any(term in normalized_query for term in ("valorant", "วาโล")):
            return "VALORANT"
        if "tekken" in normalized_query:
            return "Tekken 8"
        return None

    @staticmethod
    def _game_bonus(game_hint: str | None, row: dict[str, Any]) -> float:
        if not game_hint:
            return 0.0
        row_game = str(row.get("metadata", {}).get("game", "") or row.get("game", "")).strip()
        if not row_game:
            haystack = " ".join(
                str(row.get(key, ""))
                for key in ("id", "title", "text", "search_text")
            ).lower()
            if "rov" in haystack or "arena of valor" in haystack:
                row_game = "Arena of Valor (RoV)"
            elif "cs2" in haystack or "counter-strike" in haystack or "counter strike" in haystack:
                row_game = "Counter-Strike 2"
            elif "valorant" in haystack or "วาโล" in haystack:
                row_game = "VALORANT"
            elif "tekken" in haystack:
                row_game = "Tekken 8"
        if not row_game:
            return 0.0
        if row_game == game_hint:
            return 0.95
        known_games = {"Arena of Valor (RoV)", "Counter-Strike 2", "VALORANT", "Tekken 8"}
        if row_game in known_games:
            return -0.85
        return 0.0

    @staticmethod
    def _exact_bonus(normalized_query: str, row: dict[str, Any]) -> float:
        bonus = 0.0
        for pattern in row.get("question_patterns", [])[:8]:
            pattern_norm = normalize_text(str(pattern))
            if pattern_norm and (pattern_norm in normalized_query or normalized_query in pattern_norm):
                bonus += 0.75
                break
        tags = " ".join(str(tag) for tag in row.get("tags", []))
        for tag in tags.split():
            if tag and normalize_text(tag) in normalized_query:
                bonus += 0.03
        return min(bonus, 1.0)

    def answer(
        self,
        query: str,
        *,
        model: str = "qwen3.5:4b",
        top_k: int = 5,
        query_embedding: list[float] | None = None,
        use_llm: bool = True,
        timeout_sec: float = 10.0,
    ) -> dict[str, Any]:
        started = time.perf_counter()
        hits = self.search(query, top_k=top_k, query_embedding=query_embedding)
        deterministic = self._deterministic_answer(query, hits)
        if deterministic:
            return {
                "question": query,
                "mode": deterministic["mode"],
                "model": None,
                "answer": deterministic["answer"],
                "elapsed_sec": round(time.perf_counter() - started, 4),
                "hits": [self._public_hit(hit) for hit in hits],
                "used_llm": False,
            }

        direct = self._direct_answer_if_confident(query, hits)
        if direct:
            return {
                "question": query,
                "mode": "direct_fact",
                "model": None,
                "answer": direct,
                "elapsed_sec": round(time.perf_counter() - started, 4),
                "hits": [self._public_hit(hit) for hit in hits],
                "used_llm": False,
            }

        if not hits:
            return {
                "question": query,
                "mode": "no_context",
                "model": None,
                "answer": "ยังไม่พบข้อมูลที่ยืนยันได้จากฐานข้อมูลที่มีครับ",
                "elapsed_sec": round(time.perf_counter() - started, 4),
                "hits": [],
                "used_llm": False,
            }

        intent_hints = self._intent_hints(normalize_text(query))
        fact_synthesis = self._fact_card_synthesis(hits[:top_k], intent_hints=intent_hints)
        if fact_synthesis:
            return {
                "question": query,
                "mode": "fact_card_synthesis",
                "model": None,
                "answer": self._append_sources(fact_synthesis, hits[:3]),
                "elapsed_sec": round(time.perf_counter() - started, 4),
                "hits": [self._public_hit(hit) for hit in hits],
                "used_llm": False,
            }

        if not use_llm:
            return {
                "question": query,
                "mode": "retrieval_preview",
                "model": None,
                "answer": self._retrieval_preview(hits),
                "elapsed_sec": round(time.perf_counter() - started, 4),
                "hits": [self._public_hit(hit) for hit in hits],
                "used_llm": False,
            }

        prompt = self._build_prompt(query, hits[:top_k])
        try:
            raw = ollama_generate(prompt, model=model, timeout_sec=timeout_sec, num_predict=96, temperature=0.1)
            answer = str(raw.get("response", "")).strip()
            if not answer:
                answer = "ยังไม่พบข้อมูลที่ยืนยันได้จากฐานข้อมูลที่มีครับ"
            if self._is_no_answer(answer):
                synthesized = self._fact_card_synthesis(hits[:top_k], intent_hints=intent_hints)
                if synthesized:
                    answer = synthesized
            answer = self._append_sources(answer, hits[:3])
            mode = "rag_llm"
            error = ""
        except Exception as exc:  # noqa: BLE001 - notebook/test helper should explain failures.
            answer = self._retrieval_preview(hits)
            mode = "rag_llm_failed_fallback_preview"
            error = f"{type(exc).__name__}: {exc}"

        return {
            "question": query,
            "mode": mode,
            "model": model,
            "answer": answer,
            "elapsed_sec": round(time.perf_counter() - started, 4),
            "hits": [self._public_hit(hit) for hit in hits],
            "used_llm": mode == "rag_llm",
            "error": error,
        }

    @staticmethod
    def _direct_answer_if_confident(query: str, hits: list[SearchHit]) -> str | None:
        if not hits:
            return None
        best = hits[0]
        row = best.row
        if best.score < 0.78:
            return None
        if row.get("source_kind") not in {"competition_fact_card", "rulebase", "curated_fact"}:
            return None
        answer = str(row.get("answer") or row.get("text") or "").strip()
        if not answer:
            return None
        if len(query) > 24 and any(term in normalize_text(query) for term in ("สรุป", "อธิบาย", "ขั้นตอน", "เปรียบเทียบ", "ต่างกัน")):
            return None
        source = str(row.get("source_url", "")).strip()
        if source:
            answer += f"\nแหล่งข้อมูล: {source}"
        return answer

    @staticmethod
    def _deterministic_answer(query: str, hits: list[SearchHit]) -> dict[str, str] | None:
        normalized_query = normalize_text(query)
        calendar_hits = [hit for hit in hits if hit.row.get("source_kind") == "calendar_closure"]
        if calendar_hits and any(term in normalized_query for term in ("วันหยุด", "หยุด", "เดือนนี้", "ปิดวันไหน")):
            lines = ["เดือนนี้มีวันปิด/วันหยุดที่อยู่ในข้อมูลดังนี้:"]
            for hit in calendar_hits[:6]:
                text = str(hit.row.get("text", "")).strip()
                if text:
                    lines.append(f"- {text}")
            return {"mode": "calendar_synthesis", "answer": "\n".join(lines)}

        service_hits = [hit for hit in hits if hit.row.get("category") == "service_fee"]
        if service_hits and any(term in normalized_query for term in ("ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "บาท", "price", "cost")):
            answer = HybridRagEngine._service_fee_answer(query, service_hits)
            if answer:
                return {"mode": "service_fee_synthesis", "answer": answer}
        return None

    @staticmethod
    def _service_fee_answer(query: str, hits: list[SearchHit]) -> str | None:
        normalized_query = normalize_text(query)
        group_patterns: list[tuple[str, tuple[str, ...]]] = []
        if any(term in normalized_query for term in ("มอ", "psu", "student and staff", "บุคลากร")):
            group_patterns.append(("นักศึกษา/บุคลากร PSU", ("PSU Student and Staff", "นักศึกษา/บุคลากร PSU")))
        if any(term in normalized_query for term in ("ต่างมหาลัย", "ต่างมหาวิทยาลัย", "ต่างสถาบัน", "general student", "ศิษย์เก่า", "alumni", "สจล", "จุฬา")):
            group_patterns.append(("ศิษย์เก่า PSU / General Student / นักศึกษาต่างสถาบัน", ("General Student", "ศิษย์เก่า PSU หรือ General Student")))
        if any(term in normalized_query for term in ("บุคคลทั่วไป", "คนทั่วไป", "general adult", "adult")):
            group_patterns.append(("บุคคลทั่วไป", ("General Adult", "บุคคลทั่วไป")))

        best = hits[0].row
        text = str(best.get("text", "") or best.get("answer", "")).strip()
        if not text:
            return None

        source = str(best.get("source_url", "")).strip()
        if not group_patterns:
            answer = text
        else:
            label, patterns = group_patterns[0]
            amount = ""
            for pattern in patterns:
                match = re.search(rf"{re.escape(pattern)}[^0-9]{{0,40}}(\d+)\s*บาท", text)
                if match:
                    amount = match.group(1)
                    break
            if not amount:
                match = re.search(r"General Student[^0-9]{0,40}(\d+)\s*บาท", text)
                amount = match.group(1) if match else ""
            if amount:
                service_label = str(best.get("title", best.get("id", "ค่าบริการ"))).replace("ค่าบริการ ", "")
                answer = f"{amount} บาท สำหรับ {service_label}\nกลุ่มผู้ใช้: {label}"
            else:
                answer = text
        if source:
            answer += f"\nแหล่งข้อมูล: {source}"
        return answer

    @staticmethod
    def _retrieval_preview(hits: list[SearchHit]) -> str:
        lines = ["พบข้อมูลใกล้เคียงจาก RAG แต่ยังไม่ได้ให้ LLM เรียบเรียง:"]
        for index, hit in enumerate(hits[:5], start=1):
            row = hit.row
            lines.append(f"{index}. {row.get('title') or row.get('id')} | score={hit.score}")
            lines.append(f"   {compact_text(str(row.get('text') or row.get('answer') or ''), 220)}")
        return "\n".join(lines)

    @staticmethod
    def _is_no_answer(answer: str) -> bool:
        lowered = normalize_text(answer)
        return "ไม่พบข้อมูล" in lowered or "ไม่มีข้อมูล" in lowered or "no verified" in lowered

    @staticmethod
    def _fact_card_synthesis(hits: list[SearchHit], *, intent_hints: set[str] | None = None) -> str | None:
        fact_hits = [hit for hit in hits if hit.row.get("source_kind") == "competition_fact_card"]
        if not fact_hits:
            return None
        intent_hints = intent_hints or set()
        if intent_hints:
            fact_hits = [
                hit for hit in fact_hits
                if str(hit.row.get("metadata", {}).get("intent", "") or hit.row.get("intent", "")) in intent_hints
            ]
            if not fact_hits:
                return None
        else:
            best_score = fact_hits[0].score
            fact_hits = [hit for hit in fact_hits if hit.score >= best_score - 0.75]
        if not fact_hits:
            return None
        lines: list[str] = []
        seen: set[str] = set()
        for hit in fact_hits[:4]:
            answer = str(hit.row.get("answer", "")).strip()
            if not answer or answer in seen:
                continue
            seen.add(answer)
            lines.append(f"- {answer}")
        if not lines:
            return None
        return "สรุปจากกติกาที่พบ:\n" + "\n".join(lines)

    @staticmethod
    def _build_prompt(query: str, hits: list[SearchHit]) -> str:
        context_blocks: list[str] = []
        for index, hit in enumerate(hits, start=1):
            row = hit.row
            text = compact_text(str(row.get("text") or row.get("answer") or ""), 900)
            source = row.get("source_url", "")
            context_blocks.append(
                f"[{index}] id={row.get('id')} | category={row.get('category')} | kind={row.get('source_kind')} | source={source}\n{text}"
            )
        context = "\n\n---\n\n".join(context_blocks)
        return f"""คุณคือผู้ช่วยของ PSU Esports Studio - Phuket
ตอบเป็นภาษาไทย สุภาพ กระชับ และตอบประเด็นหลักก่อน
ใช้เฉพาะข้อมูลใน CONTEXT เท่านั้น ห้ามเดาราคา กฎ เวลา หรือเงื่อนไขเพิ่มเอง
CONTEXT ด้านล่างคือข้อมูลที่ retrieval พบว่าเกี่ยวข้องแล้ว ให้พยายามตอบจากข้อมูลนี้ก่อน
ถ้า CONTEXT ไม่พอจริง ๆ ให้ตอบว่า "ยังไม่พบข้อมูลที่ยืนยันได้จากข้อมูลที่มี"
ถ้าคำถามถามราคา/เวลา/จำนวน ให้ขึ้นต้นด้วยตัวเลขหรือคำตอบหลักทันที
ตอบไม่เกิน 7 บรรทัด ยกเว้นผู้ใช้ขอรายละเอียด

QUESTION: {query}

CONTEXT:
{context}

ANSWER:"""

    @staticmethod
    def _append_sources(answer: str, hits: list[SearchHit]) -> str:
        if "แหล่งข้อมูล" in answer:
            return answer
        used_hits = [
            hit for hit in hits
            if str(hit.row.get("answer", "")).strip()
            and str(hit.row.get("answer", "")).strip() in answer
        ]
        if used_hits:
            hits = used_hits
        sources: list[str] = []
        for hit in hits:
            source = str(hit.row.get("source_url", "")).strip()
            row_id = str(hit.row.get("id", "")).strip()
            label = f"{row_id} ({source})" if source else row_id
            if label and label not in sources:
                sources.append(label)
        if sources:
            return answer.rstrip() + "\nแหล่งข้อมูล: " + "; ".join(sources[:3])
        return answer

    @staticmethod
    def _public_hit(hit: SearchHit) -> dict[str, Any]:
        row = hit.row
        return {
            "id": hit.id,
            "score": hit.score,
            "lexical_score": hit.lexical_score,
            "vector_score": hit.vector_score,
            "category": row.get("category"),
            "source_kind": row.get("source_kind"),
            "title": row.get("title"),
            "source_url": row.get("source_url"),
            "text_preview": compact_text(str(row.get("text") or row.get("answer") or ""), 260),
        }
