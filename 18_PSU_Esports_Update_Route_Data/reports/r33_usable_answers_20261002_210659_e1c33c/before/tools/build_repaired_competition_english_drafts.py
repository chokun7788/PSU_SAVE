"""Create a corrected, review-only English overlay for competition rules.

The output deliberately stays in ``draft`` status.  It is suitable for
preview and human review, never for automatic production publishing.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "locales" / "en" / "localization_review_drafts_machine_20260915_audited.jsonl"
OUTPUT = ROOT / "data" / "locales" / "en" / "localization_review_drafts_competition_20260921_repaired.jsonl"


REPAIRS: dict[tuple[str, str], str] = {
    (
        "competition_rules_cs2_psu_phuket_2026_s08_c01",
        "section_title",
    ): "One-day competition at PSU Esports Studio - Phuket, Prince of Songkla University, Phuket Campus",
    (
        "competition_rules_cs2_psu_phuket_2026_s08_c01",
        "text",
    ): "The competition will be held for one day at PSU Esports Studio - Phuket, Prince of Songkla University, Phuket Campus.",
    (
        "competition_rules_cs2_psu_phuket_2026_s08_c01",
        "title",
    ): "Counter-Strike 2: One-day competition at PSU Esports Studio - Phuket, Prince of Songkla University, Phuket Campus",
    (
        "competition_rules_cs2_psu_phuket_2026_s27_c01",
        "section_title",
    ): "Overtime: 3 rounds per side (6 rounds total); first to 4 rounds wins; starting money is $10,000; overtime may be played without limit",
    (
        "competition_rules_cs2_psu_phuket_2026_s27_c01",
        "text",
    ): "Overtime: 3 rounds per side (6 rounds total). The first team to win 4 of the 6 rounds wins. Starting money is $10,000, and overtime may be played without limit.",
    (
        "competition_rules_cs2_psu_phuket_2026_s27_c01",
        "title",
    ): "Counter-Strike 2: Overtime: 3 rounds per side (6 rounds total); first to 4 rounds wins; starting money is $10,000; overtime may be played without limit",
    (
        "competition_rules_cs2_psu_phuket_2026_s47_c01",
        "section_title",
    ): "Do not install your own software on the provided computers",
    (
        "competition_rules_cs2_psu_phuket_2026_s47_c01",
        "text",
    ): "4. Do not install your own software on the provided computers.",
    (
        "competition_rules_cs2_psu_phuket_2026_s47_c01",
        "title",
    ): "Counter-Strike 2: Do not install your own software on the provided computers",
    (
        "competition_rules_cs2_psu_phuket_2026_s53_c01",
        "section_title",
    ): "Only drinking water in sealed containers and chewing gum are permitted",
    (
        "competition_rules_cs2_psu_phuket_2026_s53_c01",
        "text",
    ): "4. Only drinking water in sealed containers and chewing gum are permitted.",
    (
        "competition_rules_cs2_psu_phuket_2026_s53_c01",
        "title",
    ): "Counter-Strike 2: Only drinking water in sealed containers and chewing gum are permitted",
    (
        "competition_rules_rov_blueket_2025_men_s04_c01",
        "text",
    ): "Competition Venue\n2.1. PSU Esports Studio - Phuket (Building 5, Floor 1)",
    (
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "text",
    ): "4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.\n4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game.\n4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate.\n4.3.5. If there is evidence that a competitor intentionally pauses the game, whether at a critical moment or to disrupt play, the offending team immediately forfeits the game in which the violation occurred and is immediately disqualified from the competition.\n4.4. Break Time\n4.4.1. The referee will inform competitors of the remaining time before the next game begins.\n4.4.2. If competitors do not return within the stated time, the referee may declare that team to have forfeited the competition.\n4.4.3. A 5-minute break follows every two games.\n4.5. Game Pauses During Competition\n4.5.1. General Game Pauses\n4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.",
    (
        "competition_rules_valorant_psu_phuket_2026_s02_c01",
        "text",
    ): "Competition Area and Regulations\n* Personnel: During Match Prep, no more than 6 players may be present.\n* Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends.\n* Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match.\n* Food and drinks: Only drinking water in sealed containers and chewing gum are permitted.\nCompetition Process",
    (
        "competition_rules_valorant_psu_phuket_2026_s08_c01",
        "text",
    ): "3. Player Emergency Pause\n* One request per map is allowed.\n* Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute.\nBug Rules\nA bug is an in-game error that produces an unintended result. It is classified to determine the appropriate response:\n* Play Through Bug: does not significantly affect fairness. The player must continue and may not request a Challenge.\n* Major Bug: significantly affects gameplay or game mechanics and has no immediate remedy. The team may request a Challenge for review.\n* Game Breaking Bug: destroys the fairness of that round so that the outcome cannot be determined.\nRound Rollback\n* If a bug occurs before either side deals damage, officials may roll back the round.\n* If damage has already been dealt, no rollback is allowed unless through the Challenge process.\n* For a Game Breaking Bug, officials will immediately roll back the round to its starting point.\nExploit Adjudication",
}


def main() -> None:
    rows = [json.loads(line) for line in INPUT.read_text(encoding="utf-8").splitlines() if line.strip()]
    output_rows: list[dict[str, object]] = []
    applied: set[tuple[str, str]] = set()

    for row in rows:
        content_id = str(row.get("content_id") or "")
        key = (content_id, str(row.get("field") or ""))
        repaired = REPAIRS.get(key)
        if repaired:
            row["text"] = repaired
            row["translation_method"] = "machine_draft_with_manual_correction"
            applied.add(key)
        output_rows.append(row)

    missing = set(REPAIRS) - applied
    if missing:
        raise SystemExit(f"Repair targets absent from source draft: {sorted(missing)}")

    OUTPUT.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in output_rows) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"output": str(OUTPUT), "rows": len(output_rows), "repairs": len(applied)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
