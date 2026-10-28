"""Price arithmetic over explicit typed rules, without built-in service prices."""
import re
from .registry import value
def calculate(rate,question):
    from app.calculator.service_fee import _detect_minutes
    minutes=_detect_minutes(question)
    if minutes is None or not 0<minutes<=1440:return None
    if len(re.findall(r'\d+(?:\.\d+)?\s*(?:นาที|ชั่วโมง|minutes?|mins?|hours?|hrs?)',question,re.I))>1:return None
    price=value(rate,'amount_minor');base=value(rate,'duration_minutes');rule=value(rate,'calculation_rule');unit=value(rate,'unit')
    if type(price) is not int or type(base) is not int or base<=0:return None
    party=re.search(r'(\d+)\s*(?:คน|people|persons|players)',question,re.I)
    if party and (value(rate,'persons_min') is None or value(rate,'persons_max') is None or not value(rate,'persons_min')<=int(party[1])<=value(rate,'persons_max')):return None
    if rule=='session_ceil' and unit=='per_session':
        units=(minutes+base-1)//base;total=units*price
    elif rule=='linear':
        # Do not round fractional minor currency units without a source rule.
        if minutes*price%base:return None
        units=minutes/base;total=minutes*price//base
    elif rule=='fixed' and minutes==base:units=1;total=price
    else:return None
    return {'record_id':rate['record_id'],'requested_minutes':minutes,'base_minutes':base,'units':units,'amount_minor':total,'currency':value(rate,'currency'),'calculation_rule':rule,'basis':'explicit source-bound rate rule; no availability claim','validity_state':rate['validity']['state']}
def render(calculation,lang):
    c=calculation;money=f"{c['amount_minor']//100:,}.{c['amount_minor']%100:02d} {c['currency']}"
    if lang=='en':return f"For {c['requested_minutes']} minutes: {c['units']:g} billing unit(s), total {money}."
    return f"ระยะเวลา {c['requested_minutes']} นาที: คิด {c['units']:g} รอบ รวม {money}"
