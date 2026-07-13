#!/usr/bin/env python3
"""
Simple no-dependency retriever demo.

This does NOT call an LLM. It only searches prepared chunks so you can inspect
whether the data is ready before building the real RAG pipeline.

Usage:
  python src/simple_retriever_demo.py "จองได้สูงสุดกี่ session"
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHUNKS_PATH = ROOT / "data" / "processed" / "all_chunks.jsonl"
CURATED_PATH = ROOT / "data" / "curated" / "faq_facts.jsonl"
DEFAULT_CATEGORIES = {"reservation", "services", "competition", "knowledge", "contact"}


def normalize(text: str) -> str:
    return (text or "").lower()


def query_terms(query: str) -> list[str]:
    q = normalize(query)
    terms = re.findall(r"[a-z0-9+#.]+|[ก-๙]+", q)
    # Add short Thai character ngrams to help with Thai text without word segmentation.
    thai = "".join(re.findall(r"[ก-๙]+", q))
    for n in (3, 4, 5):
        terms.extend(thai[i:i+n] for i in range(max(0, len(thai) - n + 1)))
    return [t for t in terms if len(t) >= 2]


def load_chunks() -> list[dict]:
    chunks = []
    for path in [CURATED_PATH, CHUNKS_PATH]:
        if not path.exists():
            continue
        with path.open(encoding="utf-8") as f:
            for line in f:
                item = json.loads(line)
                if item.get("category") in DEFAULT_CATEGORIES:
                    chunks.append(item)
    return chunks


def preferred_categories(query: str) -> set[str]:
    q = normalize(query)
    rules = [
        ({"reservation"}, ["จอง", "session", "เช็คอิน", "check-in", "ยกเลิก", "ค่าปรับ", "ชำระ", "คืนเงิน"]),
        ({"services"}, ["ps5", "playstation", "pc", "switch", "nintendo", "vr", "cockpit", "เกมอะไร", "อุปกรณ์"]),
        ({"competition"}, ["แข่งขัน", "competition", "tournament", "challenge", "leaderboard", "rov", "valorant", "tekken", "cs2", "cs 2"]),
        ({"knowledge"}, ["esports คือ", "อีสปอร์ตคือ", "ประเภทเกม", "อาชีพ", "ความรู้", "ประวัติ"]),
        ({"contact"}, ["ติดต่อ", "เบอร์", "โทร", "email", "อีเมล", "facebook", "ที่อยู่"]),
    ]
    matched: set[str] = set()
    for categories, keywords in rules:
        if any(keyword in q for keyword in keywords):
            matched.update(categories)
    return matched


def score_chunk(query: str, chunk: dict) -> float:
    q = normalize(query)
    haystack = normalize(" ".join([
        chunk.get("title", ""),
        chunk.get("category", ""),
        chunk.get("subcategory", ""),
        " ".join(chunk.get("tags", [])),
        chunk.get("text", ""),
    ]))
    score = 0.0
    if chunk.get("record_type") == "curated_fact":
        score += 4.0
    device_boosts = [
        (["ps5", "playstation"], ["ps5", "playstation", "ps5_games"]),
        (["pc", "คอม"], ["pc_games", "pc #"]),
        (["switch", "nintendo"], ["switch_games", "nintendo"]),
        (["vr"], ["vr_games", "vr station"]),
        (["cockpit"], ["cockpit_games", "cockpit"]),
    ]
    for query_keys, chunk_keys in device_boosts:
        if any(key in q for key in query_keys) and any(key in haystack for key in chunk_keys):
            score += 20.0
    for term in query_terms(query):
        if term in haystack:
            score += 1.0 if len(term) < 5 else 1.5
    return score


def main() -> None:
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print('Usage: python src/simple_retriever_demo.py "คำถาม"')
        raise SystemExit(1)

    chunks = load_chunks()
    preferred = preferred_categories(query)
    if preferred:
        chunks = [chunk for chunk in chunks if chunk.get("category") in preferred]
    ranked = sorted(
        ((score_chunk(query, chunk), chunk) for chunk in chunks),
        key=lambda x: x[0],
        reverse=True,
    )
    top = [(score, chunk) for score, chunk in ranked[:8] if score > 0]

    print(f"Query: {query}")
    print(f"Loaded chunks: {len(chunks)}")
    if preferred:
        print(f"Preferred categories: {', '.join(sorted(preferred))}")
    print()
    if not top:
        print("No matching chunks found.")
        return

    for i, (score, chunk) in enumerate(top, 1):
        text = " ".join(chunk.get("text", "").split())
        preview = text[:450] + ("..." if len(text) > 450 else "")
        print(f"## {i}. score={score:.1f}")
        print(f"category: {chunk.get('category')} / {chunk.get('subcategory')}")
        print(f"title: {chunk.get('title')}")
        print(f"url: {chunk.get('url')}")
        print(preview)
        print()


if __name__ == "__main__":
    main()
