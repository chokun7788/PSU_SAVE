"""Compare explicit audiences on a shared, current source billing basis."""
import re
from .registry import value
from .query_contract import normalize
from .relations import related_rates
ROOT_KINDS={'service','resource','zone','game'}
BASIS=('currency','unit','duration_minutes','persons_min','persons_max','calculation_rule')
def requested(question):return bool(re.search(r'เท่ากัน|เหมือนกัน|ต่างกัน|เปรียบเทียบ|\b(?:same|different|compare|comparison|versus)\b|\bvs\.?\b',normalize(question)))
def groups_for_roots(records,roots):return sorted({value(r,'audience_id') for rid in roots for r in related_rates(records,records[rid]) if value(r,'audience_id') in records})
def summaries(records,roots,audiences,at,axis='audience'):
    from .answer import effective
    rates={r['record_id']:r for rid in roots for r in related_rates(records,records[rid],audiences=audiences)};services=sorted({value(r,'service_id') for r in rates.values()});out=[]
    for target in (services if axis=='audience' else audiences):
        side='audience_id' if axis=='audience' else 'service_id';anchor='service_id' if axis=='audience' else 'audience_id';operands=audiences if axis=='audience' else services
        current=[r for r in rates.values() if value(r,anchor)==target and r['validity']['state']=='known' and effective(r,at,records)]
        selected=[]
        for operand in operands:
            matches=[r for r in current if value(r,side)==operand]
            if len(matches)!=1:break
            selected.append(matches[0])
        row={'service_id':target if axis=='audience' else None,'audience_id':target if axis=='service' else None,'axis':axis,'operand_ids':list(operands),'audience_ids':list(audiences),'rate_ids':[r['record_id'] for r in selected],'status':'not_confirmed','reason':'current_comparable_rates_missing_or_ambiguous'}
        if len(operands)>=2 and len(selected)==len(operands):
            if all(all(r['fields'][key]['status']=='known' for key in BASIS) and type(value(r,'amount_minor')) is int for r in selected):
                bases={tuple(value(r,key) for key in BASIS) for r in selected}
                if len(bases)==1:row.update(status='equal' if len({value(r,'amount_minor') for r in selected})==1 else 'different',reason='same_declared_billing_basis',amounts_minor=[value(r,'amount_minor') for r in selected],basis=dict(zip(BASIS,next(iter(bases)))))
                else:row['reason']='different_billing_basis'
            else:row['reason']='billing_basis_not_confirmed'
        out.append(row)
    return out or [{'service_id':None,'audience_ids':list(audiences),'rate_ids':[],'status':'not_confirmed','reason':'no_rates_in_declared_scope'}]
