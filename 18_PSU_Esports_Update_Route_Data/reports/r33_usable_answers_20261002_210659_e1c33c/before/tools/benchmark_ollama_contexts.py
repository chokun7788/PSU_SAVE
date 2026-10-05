from __future__ import annotations

import argparse
import json
import math
import statistics
import subprocess
import time
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = ROOT / "reports" / "model_runtime"


def _post(url: str, endpoint: str, payload: dict[str, Any], timeout_sec: float) -> dict[str, Any]:
    request = urllib.request.Request(
        f"{url.rstrip('/')}{endpoint}",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout_sec) as response:
        return json.loads(response.read().decode("utf-8"))


def _get(url: str, endpoint: str, timeout_sec: float = 10.0) -> dict[str, Any]:
    with urllib.request.urlopen(f"{url.rstrip('/')}{endpoint}", timeout=timeout_sec) as response:
        return json.loads(response.read().decode("utf-8"))


def _gpu_snapshot() -> dict[str, Any]:
    command = [
        "nvidia-smi",
        "--query-gpu=name,memory.total,memory.used,memory.free,utilization.gpu,power.draw",
        "--format=csv,noheader,nounits",
    ]
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=10, check=True)
        values = [value.strip() for value in completed.stdout.strip().split(",")]
        return {
            "name": values[0],
            "memory_total_mib": float(values[1]),
            "memory_used_mib": float(values[2]),
            "memory_free_mib": float(values[3]),
            "utilization_gpu_pct": float(values[4]),
            "power_draw_w": float(values[5]),
        }
    except Exception as exc:  # noqa: BLE001 - GPU telemetry is optional.
        return {"error": f"{type(exc).__name__}: {exc}"}


def _workloads() -> list[dict[str, Any]]:
    evidence = "\n".join(
        f"หลักฐาน {index}: ข้อมูลทดสอบสำหรับวัดการใช้ context เท่านั้น "
        "ห้ามนำไปใช้เป็นข้อเท็จจริงของ PSU Esports Studio"
        for index in range(1, 18)
    )
    return [
        {
            "name": "intent_json",
            "num_predict": 64,
            "prompt": (
                "จัดประเภทคำถามเป็น JSON เท่านั้น โดยมี keys domain, operation, confidence\n"
                "คำถาม: ผู้ใช้ต้องการทราบว่าข้อมูลใหม่ที่ผู้ดูแลเพิ่มไว้กล่าวถึงหัวข้อใด"
            ),
        },
        {
            "name": "general_thai",
            "num_predict": 96,
            "prompt": (
                "ตอบภาษาไทยแบบสั้นและตรงคำถาม อธิบายว่า semantic embedding "
                "ต่างจาก context length ของโมเดลสร้างข้อความอย่างไร"
            ),
        },
        {
            "name": "rag_grounded",
            "num_predict": 96,
            "prompt": (
                "สรุปคำตอบจาก EVIDENCE เท่านั้น ห้ามสร้างข้อเท็จจริงใหม่\n\n"
                f"EVIDENCE:\n{evidence}\n\n"
                "คำถาม: เอกสารนี้มีไว้ทำอะไร"
            ),
        },
    ]


def _unload(url: str, model: str) -> None:
    try:
        _post(url, "/api/generate", {"model": model, "keep_alive": 0}, 30.0)
    except Exception:
        return


def _running_model(url: str, model: str) -> dict[str, Any]:
    data = _get(url, "/api/ps")
    for row in data.get("models", []):
        if str(row.get("name") or row.get("model") or "").split(":")[0] == model.split(":")[0]:
            return row
    return {}


def _percentile(values: list[float], percentile: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, math.ceil(percentile / 100 * len(ordered)) - 1))
    return ordered[index]


def _summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    warm_rows = [row for row in rows if not row.get("cold") and not row.get("error")]
    wall = [float(row["wall_sec"]) for row in warm_rows]
    tokens_per_sec = [float(row["eval_tokens_per_sec"]) for row in warm_rows if row.get("eval_tokens_per_sec")]
    return {
        "request_count": len(rows),
        "error_count": sum(1 for row in rows if row.get("error")),
        "warm_avg_sec": round(statistics.mean(wall), 4) if wall else 0.0,
        "warm_p95_sec": round(_percentile(wall, 95), 4),
        "warm_max_sec": round(max(wall), 4) if wall else 0.0,
        "warm_avg_tokens_per_sec": round(statistics.mean(tokens_per_sec), 2) if tokens_per_sec else 0.0,
    }


def _write_report(output_dir: Path, payload: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "results.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    lines = [
        "# Ollama Context Benchmark",
        "",
        f"- Generated: {payload['generated_at']}",
        f"- Model: `{payload['model']}`",
        f"- Contexts: {', '.join(str(value) for value in payload['contexts'])}",
        f"- Repeats per workload: {payload['repeats']}",
        "",
        "| num_ctx | Warm avg sec | P95 sec | Max sec | tok/s | Ollama size MiB | VRAM size MiB |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for context in payload["contexts"]:
        section = payload["by_context"][str(context)]
        summary = section["summary"]
        process = section.get("ollama_ps") or {}
        lines.append(
            f"| {context} | {summary['warm_avg_sec']} | {summary['warm_p95_sec']} | "
            f"{summary['warm_max_sec']} | {summary['warm_avg_tokens_per_sec']} | "
            f"{round(float(process.get('size') or 0) / 1048576, 1)} | "
            f"{round(float(process.get('size_vram') or 0) / 1048576, 1)} |"
        )
    lines.extend([
        "",
        "หมายเหตุ: context length คือเพดาน token ต่อ request และมีผลต่อ KV cache; "
        "ไม่ได้หมายความว่า prompt ทุกข้อใช้ token เต็มเพดาน",
        "",
    ])
    (output_dir / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure Ollama latency and memory across num_ctx values.")
    parser.add_argument("--model", default="scb10x/typhoon2.5-qwen3-4b")
    parser.add_argument("--contexts", default="1024,2048,3072,4096")
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434")
    parser.add_argument("--timeout-sec", type=float, default=30.0)
    parser.add_argument("--keep-alive", default="10m")
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    contexts = [int(value.strip()) for value in args.contexts.split(",") if value.strip()]
    output_dir = args.output_dir or REPORT_ROOT / datetime.now().strftime("%Y%m%d_context_%H%M%S")
    payload: dict[str, Any] = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "model": args.model,
        "contexts": contexts,
        "repeats": args.repeats,
        "gpu_before": _gpu_snapshot(),
        "by_context": {},
    }
    workloads = _workloads()
    for context in contexts:
        _unload(args.ollama_url, args.model)
        time.sleep(0.5)
        rows: list[dict[str, Any]] = []
        for workload in workloads:
            for repeat in range(args.repeats + 1):
                started = time.perf_counter()
                row: dict[str, Any] = {
                    "context": context,
                    "workload": workload["name"],
                    "repeat": repeat,
                    "cold": repeat == 0 and workload is workloads[0],
                }
                try:
                    response = _post(
                        args.ollama_url,
                        "/api/generate",
                        {
                            "model": args.model,
                            "prompt": workload["prompt"],
                            "stream": False,
                            "think": False,
                            "keep_alive": args.keep_alive,
                            "options": {
                                "temperature": 0,
                                "num_predict": workload["num_predict"],
                                "num_ctx": context,
                            },
                        },
                        args.timeout_sec,
                    )
                    eval_count = int(response.get("eval_count") or 0)
                    eval_duration = float(response.get("eval_duration") or 0) / 1_000_000_000
                    row.update({
                        "wall_sec": round(time.perf_counter() - started, 4),
                        "load_duration_ms": round(float(response.get("load_duration") or 0) / 1_000_000, 2),
                        "prompt_eval_count": int(response.get("prompt_eval_count") or 0),
                        "prompt_eval_duration_ms": round(float(response.get("prompt_eval_duration") or 0) / 1_000_000, 2),
                        "eval_count": eval_count,
                        "eval_duration_ms": round(eval_duration * 1000, 2),
                        "eval_tokens_per_sec": round(eval_count / eval_duration, 2) if eval_duration > 0 else 0.0,
                        "done_reason": response.get("done_reason"),
                        "response": str(response.get("response") or ""),
                    })
                except Exception as exc:  # noqa: BLE001 - benchmark records failures.
                    row.update({
                        "wall_sec": round(time.perf_counter() - started, 4),
                        "error": f"{type(exc).__name__}: {exc}",
                    })
                rows.append(row)
        payload["by_context"][str(context)] = {
            "summary": _summary(rows),
            "ollama_ps": _running_model(args.ollama_url, args.model),
            "gpu": _gpu_snapshot(),
            "rows": rows,
        }
        print(json.dumps({"num_ctx": context, **payload["by_context"][str(context)]["summary"]}, ensure_ascii=False), flush=True)

    payload["gpu_after"] = _gpu_snapshot()
    _write_report(output_dir, payload)
    print(f"Saved: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
