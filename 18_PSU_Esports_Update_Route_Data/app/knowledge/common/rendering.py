"""Display enum/conditions without changing their truth values or logic."""
ENUMS={
 'decision':{'allowed':('อนุญาต','Allowed'),'prohibited':('ไม่อนุญาต','Prohibited'),'required':('จำเป็น','Required'),'conditional':('มีเงื่อนไข','Conditional')},
 'calculation_rule':{'fixed':('ราคาคงที่ตามรายการ','Fixed rate'),'linear':('คำนวณตามสัดส่วนที่ระบุ','Confirmed proportional calculation'),'no_extrapolation':('ห้ามขยายราคาจากรายการนี้เอง','Do not extrapolate this rate')},
 'state':{'closed':('ปิดบริการ','Closed'),'modified_hours':('เปลี่ยนเวลาบริการ','Modified hours'),'open_override':('เปิดเป็นกรณีพิเศษ','Special opening')},
 'gesture':{'press':('กด','Press'),'hold':('กดค้าง','Hold'),'simultaneous':('กดพร้อมกัน','Press together'),'sequence':('กดตามลำดับ','Press in sequence')},
 'channel':{'facebook':('Facebook','Facebook'),'email':('อีเมล','Email'),'phone':('โทรศัพท์','Phone'),'website':('เว็บไซต์','Website'),'onsite':('ติดต่อที่ศูนย์','At the venue')}
}
OPERATORS={'eq':('เท่ากับ','equals'),'ne':('ไม่เท่ากับ','does not equal'),'gte':('อย่างน้อย','at least'),'lte':('ไม่เกิน','at most'),'in':('อยู่ใน','is one of')}
def enum_text(field,value,lang):
    if not isinstance(value,str):return None
    pair=ENUMS.get(field,{}).get(value)
    return pair[lang=='en'] if pair else None
def conditions_text(conditions,lang,convert):
    if not conditions:return 'ไม่มีเงื่อนไขเพิ่มเติม (ยืนยันแล้ว)' if lang=='th' else 'No additional conditions (confirmed)'
    lines=[]
    for condition in conditions:
        name=condition['field'].replace('_',' ');op=OPERATORS.get(condition['operator'],(condition['operator'],condition['operator']))[lang=='en']
        lines.append('• '+name+' '+op+' '+convert(condition['value'],lang))
    return '\n'.join(lines)
