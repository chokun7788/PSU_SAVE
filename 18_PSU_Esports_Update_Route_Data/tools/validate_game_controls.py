from __future__ import annotations

import subprocess
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "control_game" / "nintendo"


def run_step(label: str, args: list[str]) -> None:
    print(f"\n== {label} ==")
    completed = subprocess.run(args, cwd=ROOT)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> int:
    python = sys.executable
    run_step(
        "compile",
        [
            python,
            "-m",
            "py_compile",
            "app/pipeline/vector_retrieval.py",
            "app/pipeline/engine.py",
            "tools/build_game_control_facts.py",
            "tools/audit_game_control_data.py",
            "tests/smoke_test_game_controls.py",
        ],
    )
    if SOURCE_DIR.exists() and any(SOURCE_DIR.glob("*.json")):
        run_step("build game control facts", [python, "tools/build_game_control_facts.py"])
        run_step("build vector index", [python, "tools/build_vector_index.py"])
    else:
        print(f"\n== build skipped ==")
        print(f"raw source not available: {SOURCE_DIR}")
    run_step("audit game control data", [python, "tools/audit_game_control_data.py"])
    run_step("smoke test game controls", [python, "tests/smoke_test_game_controls.py"])
    print("\nGAME CONTROL VALIDATION OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
