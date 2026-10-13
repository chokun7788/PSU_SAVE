"""Source-hash-bound rendering of an incomplete rulebook fragment.

Agent translation is labelled as such; this does not publish an approved
localization, complete the policy, or modify the owner's source documents.
"""
import hashlib
ID = 'competition_rules_rov_blueket_2025_men_s08_c01'
SOURCE_SHA256 = '92ebcc6a88ca7486dda118de87f33f526c2a915384974575bf70f7daba4f3bd2'
ENGLISH_FRAGMENT = '6. Offences and penalties — translation of the readable source fragment; incomplete source\n6.1. Competitors must not commit any of the following acts.\n6.1.1. Using impolite speech or gestures, or making disparaging remarks about others, is prohibited.\n6.1.1.1. Penalty: immediate forfeiture of the game in which the offence is found.\n6.1.2. Submitting false or distorted competition results is prohibited.\n6.1.2.1. Penalty: immediate forfeiture of the game in which the offence is found and immediate disqualification of the offending team from the competition.\n6.1.3. Teams must not allow anyone who is absent from their registered team roster to compete. If a competitor does not match the registration, record photographic evidence and stop the match immediately. If the game has already been played to completion, both teams are deemed to have consented to the match; staff will not accept objections.\n6.1.3.1. Penalty: immediate forfeiture of the game in which the offence is found and immediate disqualification of the offending team from the competition.\n6.1.4. Competitors must not allow another person to play in their place during competition.\n6.1.4.1. Penalty: immediate forfeiture of the game in which the offence is found and immediate disqualification of the offending team from the competition.\n6.1.5. The readable text prohibits competitors from consuming, trading, or carrying out activities involving drugs, cigarettes, weapons, and other legally prohibited items. The source wording at the end of this clause is unclear.\n6.1.5.1. Readable penalty fragment: immediate forfeiture of the game in which the offence is found and immediate disqualification of the offending team from … [the source stops here; the missing ending and application of this clause require organizer confirmation].'

def is_recorded_fragment(row):
    return row.get('id') == ID and hashlib.sha256(str(row.get('text','')).encode()).hexdigest() == SOURCE_SHA256

def fragment_translation(row):
    return ENGLISH_FRAGMENT if is_recorded_fragment(row) else None
