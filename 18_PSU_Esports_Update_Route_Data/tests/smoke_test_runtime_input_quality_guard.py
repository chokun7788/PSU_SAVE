from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard  # noqa: E402


def main() -> int:
    guard = RuntimeInputQualityGuard.from_environment()
    guard.mode = "enforce"

    layout = guard.inspect("g]jo")
    if not layout.should_short_circuit or "keyboard_layout_mismatch" not in layout.flags:
        raise AssertionError(f"expected keyboard-layout retry, got {layout}")
    if layout.detected_action != "request_retype" or layout.applied_action != "request_retype":
        raise AssertionError(f"expected applied layout retry, got {layout}")
    if layout.elapsed_ms < 0 or not layout.profile_version.startswith("keyboard-profile-v1:"):
        raise AssertionError(f"expected timing and profile metadata, got {layout}")

    repeated = guard.inspect("จอองแล้วแก้ไขได้ไหม")
    if not repeated.should_short_circuit or "repeated_character_typo" not in repeated.flags:
        raise AssertionError(f"expected repeated-character retry, got {repeated}")

    normal = guard.inspect("PS5 ราคาเท่าไหร่")
    if normal.should_short_circuit or normal.flags:
        raise AssertionError(f"expected normal input to continue, got {normal}")

    for question in ("วันนี้ตอน10โมง PC1 ว่างไหม", "พรุ่งนี้ตอน10โมง PC1 ว่างไหม"):
        booking = guard.inspect(question)
        if booking.should_short_circuit or "keyboard_layout_mismatch" in booking.flags:
            raise AssertionError(f"valid Thai booking question was rejected: {question!r}, {booking}")

    expressive = guard.inspect("เล่นได้ไหมมม")
    if expressive.should_short_circuit or expressive.flags:
        raise AssertionError(f"expected expressive repetition to continue, got {expressive}")

    shadow = RuntimeInputQualityGuard.from_environment()
    shadow_layout = shadow.inspect("g]jo")
    if shadow_layout.should_short_circuit or shadow_layout.applied_action != "continue":
        raise AssertionError(f"expected shadow layout to continue, got {shadow_layout}")

    soft_guard = RuntimeInputQualityGuard.from_environment()
    soft_guard.mode = "enforce"
    soft_guard.repeat_policy = "warn_and_continue"
    soft_repeat = soft_guard.inspect("จอองแล้วแก้ไขได้ไหม")
    if soft_repeat.should_short_circuit or soft_repeat.applied_action != "warn_and_continue":
        raise AssertionError(f"expected enforced soft warning, got {soft_repeat}")

    print("RUNTIME INPUT QUALITY GUARD SMOKE TEST OK")
    print(guard.startup_status())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
