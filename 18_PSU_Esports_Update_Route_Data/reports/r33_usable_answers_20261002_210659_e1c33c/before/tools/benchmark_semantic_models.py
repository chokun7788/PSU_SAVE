from __future__ import annotations

import argparse
import json
import math
import os
import statistics
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.schemas import PipelineRoute
from app.pipeline.semantic_embeddings import clear_embedding_cache, embed_texts
from app.pipeline.semantic_vector_retrieval import build_semantic_index, retrieve_semantic_guarded


REPORT_ROOT = ROOT / "reports" / "semantic_rag"

CASES = [
    ("อีสปอร์ตหมายถึงอะไร", "knowledge", "curated_knowledge_esports_definition"),
    ("การแข่งขันอีสปอร์ตเริ่มต้นครั้งแรกเมื่อไหร่", "knowledge", "curated_knowledge_esports_origin"),
    ("เกมแนวไหนนิยมใช้แข่งขันอีสปอร์ต", "knowledge", "curated_knowledge_esports_categories"),
    ("มีอาชีพอะไรที่เกี่ยวข้องกับวงการอีสปอร์ต", "knowledge", "curated_knowledge_esports_careers"),
    ("Overcooked 2 ช่วยฝึกทักษะอะไรบ้าง", "knowledge", "curated_knowledge_overcooked2_skills"),
    ("บทความเกมนารูโตะพูดถึงทักษะอะไร", "knowledge", "curated_knowledge_naruto_connections_summary"),
    ("การแข่งขัน CS2 วันที่ 25 เมษายนเป็นรายการอะไร", "events_news", "curated_news_cs2_2026"),
    ("ทัวร์นาเมนต์ Valorant วันที่ 21 กุมภาพันธ์จัดที่ไหน", "events_news", "curated_news_valorant_2026"),
    ("ใครเข้าร่วม SURAT SMASH Tekken 8", "events_news", "curated_news_surat_smash_tekken8"),
    ("กิจกรรม game based learning มีนักศึกษาชาวจีนกี่คน", "events_news", "curated_news_chinese_students_game_based_learning"),
    ("GAME ON โรงเรียนท้ายเหมืองมีนักเรียนเข้าร่วมกี่คน", "events_news", "curated_news_game_on_thaimuang"),
]


def _safe_label(value: str) -> str:
    return "".join(char if char.isalnum() or char in "_.-" else "_" for char in value).strip("_")


def _post(url: str, endpoint: str, payload: dict[str, Any], timeout_sec: float = 30.0) -> dict[str, Any]:
    request = urllib.request.Request(
        f"{url.rstrip('/')}{endpoint}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout_sec) as response:
        return json.loads(response.read().decode("utf-8"))


def _unload(url: str, model: str) -> None:
    try:
        _post(url, "/api/embed", {"model": model, "input": "unload", "keep_alive": 0})
    except Exception:
        return


def _ps(url: str, model: str) -> dict[str, Any]:
    try:
        with urllib.request.urlopen(f"{url.rstrip('/')}/api/ps", timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
        base = model.split(":")[0]
        for row in payload.get("models", []):
            if str(row.get("name") or row.get("model") or "").split(":")[0] == base:
                return row
    except Exception:
        return {}
    return {}


def _cosine(left: list[float], right: list[float]) -> float:
    if len(left) != len(right) or not left:
        return 0.0
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm <= 0 or right_norm <= 0:
        return 0.0
    return sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, math.ceil(pct / 100 * len(ordered)) - 1))
    return ordered[index]


def _run_model(model: str, output_dir: Path, ollama_url: str) -> dict[str, Any]:
    os.environ["PSU_EMBEDDING_MODEL"] = model
    os.environ["PSU_EMBEDDING_OLLAMA_URL"] = ollama_url
    os.environ["PSU_EMBEDDING_NUM_CTX"] = "1024"
    os.environ["PSU_EMBEDDING_KEEP_ALIVE"] = "10m"
    clear_embedding_cache()
    _unload(ollama_url, model)
    index_path = output_dir / "semantic_index.json"
    build = build_semantic_index(path=index_path, batch_size=16, timeout_sec=180.0)
    index = json.loads(index_path.read_text(encoding="utf-8"))

    rows: list[dict[str, Any]] = []
    for question, category, expected_id in CASES:
        started = time.perf_counter()
        embedded = embed_texts([question], timeout_sec=30.0, apply_request_deadline=False)
        route = PipelineRoute(category, "benchmark_lookup", 0.9, "fact", "low", "semantic benchmark")
        hits, trace = retrieve_semantic_guarded(
            question,
            route,
            limit=5,
            query_vector=embedded.vectors[0],
            index=index,
        )
        ids = [str(hit.get("id") or "") for hit in hits]
        rows.append({
            "question": question,
            "category": category,
            "expected_id": expected_id,
            "top_ids": ids,
            "top1_correct": bool(ids and ids[0] == expected_id),
            "top3_correct": expected_id in ids[:3],
            "elapsed_sec": round(time.perf_counter() - started, 4),
            "embedding": embedded.metadata(),
            "retrieval": {
                "decision": trace.decision,
                "confidence": trace.confidence,
                "detail": trace.detail,
                "metadata": trace.metadata,
            },
        })
    latencies = [float(row["elapsed_sec"]) for row in rows]
    summary = {
        "model": model,
        "case_count": len(rows),
        "top1_accuracy": round(sum(row["top1_correct"] for row in rows) / len(rows), 4),
        "top3_accuracy": round(sum(row["top3_correct"] for row in rows) / len(rows), 4),
        "avg_query_sec": round(statistics.mean(latencies), 4),
        "p95_query_sec": round(_percentile(latencies, 95), 4),
        "max_query_sec": round(max(latencies), 4),
        "build": build.as_dict(),
        "ollama_ps": _ps(ollama_url, model),
        "rows": rows,
        "index": index,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "results.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return summary


def _vector_drift(reference: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    ref_docs = {str(row.get("id")): row for row in reference["index"].get("docs", [])}
    candidate_docs = {str(row.get("id")): row for row in candidate["index"].get("docs", [])}
    similarities = [
        _cosine(ref_docs[row_id].get("vector") or [], candidate_docs[row_id].get("vector") or [])
        for row_id in sorted(set(ref_docs) & set(candidate_docs))
    ]
    return {
        "reference": reference["model"],
        "candidate": candidate["model"],
        "shared_docs": len(similarities),
        "avg_same_document_cosine": round(statistics.mean(similarities), 6) if similarities else 0.0,
        "min_same_document_cosine": round(min(similarities), 6) if similarities else 0.0,
        "top1_agreement": round(
            sum(
                left["top_ids"][:1] == right["top_ids"][:1]
                for left, right in zip(reference["rows"], candidate["rows"])
            ) / max(1, len(reference["rows"])),
            4,
        ),
    }


def _write_report(root: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Semantic Embedding Model Benchmark",
        "",
        f"- Generated: {payload['generated_at']}",
        f"- Cases: {len(CASES)}",
        "",
        "| Model | Quantization | Size MiB | Build sec | Top-1 | Top-3 | Avg query sec | P95 sec | Max sec |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for result in payload["models"]:
        process = result.get("ollama_ps") or {}
        details = process.get("details") or {}
        lines.append(
            f"| `{result['model']}` | {details.get('quantization_level') or '-'} | "
            f"{round(float(process.get('size') or 0) / 1048576, 1)} | "
            f"{result['build']['elapsed_sec']} | {result['top1_accuracy'] * 100:.2f}% | "
            f"{result['top3_accuracy'] * 100:.2f}% | {result['avg_query_sec']} | "
            f"{result['p95_query_sec']} | {result['max_query_sec']} |"
        )
    if payload.get("drift"):
        lines.extend(["", "## Quantization Drift", ""])
        for drift in payload["drift"]:
            lines.append(
                f"- `{drift['candidate']}` เทียบ `{drift['reference']}`: "
                f"average same-document cosine={drift['avg_same_document_cosine']}, "
                f"minimum={drift['min_same_document_cosine']}, "
                f"top-1 agreement={drift['top1_agreement'] * 100:.2f}%"
            )
    lines.extend([
        "",
        "หมายเหตุ: ชุดนี้วัด retrieval บนข้อมูลจริงที่มีในหมวด knowledge/events_news "
        "ยังไม่ใช่ human relevance benchmark ขนาดใหญ่",
        "",
    ])
    (root / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare F16/Q8/Q4 semantic embedding retrieval.")
    parser.add_argument("--models", default="bge-m3,psu-bge-m3:q8_0,psu-bge-m3:q4_k_m")
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434")
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    models = [value.strip() for value in args.models.split(",") if value.strip()]
    root = args.output_dir or REPORT_ROOT / datetime.now().strftime("%Y%m%d_bge_quant_%H%M%S")
    root.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []
    for model in models:
        result = _run_model(model, root / _safe_label(model), args.ollama_url)
        results.append(result)
        print(json.dumps({key: result[key] for key in ("model", "top1_accuracy", "top3_accuracy", "avg_query_sec", "p95_query_sec")}, ensure_ascii=False), flush=True)
    reference = results[0] if results else None
    payload = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "models": results,
        "drift": [_vector_drift(reference, candidate) for candidate in results[1:]] if reference else [],
    }
    (root / "results.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_report(root, payload)
    print(f"Saved: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
