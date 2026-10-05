from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.runtime.fast_answer import answer_question_fast  # noqa: E402


def check(question: str, expected_keywords: list[str], expected_mode_prefix: str | None = None) -> None:
    answer, hits, elapsed, mode = answer_question_fast(question)
    missing = [kw for kw in expected_keywords if kw.lower() not in answer.lower()]
    if missing:
        raise AssertionError(f"{question}: missing {missing}\n{answer}")
    if expected_mode_prefix and not mode.startswith(expected_mode_prefix):
        raise AssertionError(f"{question}: expected mode prefix {expected_mode_prefix}, got {mode}")
    print(f"OK {mode} {elapsed:.4f}s | {question}")


def main() -> int:
    check("วันจันทร์เปิดให้เล่นกี่โมง ปิดกี่โมง", ["13:00", "16:00", "Maintenance"], "schedule")
    check("ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่", ["VR", "30", "190", "บาท"], "deterministic")
    check("นักศึกษา สจล อยากเล่น PC เสียเท่าไหร่", ["General Student", "PC", "25 บาท"], "deterministic")
    check("เด็กจุฬา เล่น PC กี่บาท", ["ราคา PC", "General Student", "มหาลัยอื่น", "25 บาท"], "deterministic")
    check("เด็กลาดกระบังเล่น VR ครึ่งชั่วโมงราคาเท่าไหร่", ["General Student", "190", "VR"], "deterministic")
    check("เด็ก สจล เล่น VR พี่บาท", ["ราคา VR", "190", "375", "มหาลัยอื่น"], "deterministic")
    check("ราคา PC ต่อชั่วโมงเท่าไหร่", ["PC", "0 บาท", "25 บาท", "70 บาท"], "deterministic")
    check("คอมมีวาโลไหม", ["VALORANT"], "games")
    check("PC Zone มีอุปกรณ์อะไรบ้าง", ["Gaming PC", "Gaming Monitor", "Gaming Chair"], "equipment")
    check("มีให้เช่าจอไปบ้านไหม", ["ไม่พบข้อมูล"], "no_answer")
    print("FAST RUNTIME SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
