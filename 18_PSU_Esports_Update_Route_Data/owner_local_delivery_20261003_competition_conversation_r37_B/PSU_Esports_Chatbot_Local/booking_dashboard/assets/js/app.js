/* User dashboard logic - separated in v16 */
const BASE_CATEGORIES = [
  { key:'cockpit', title:'Cockpit', icon:'🏎️', match:[/cockpit/i] },
  { key:'switch', title:'Nintendo Switch', icon:'🎮', match:[/nintendo/i,/switch/i] },
  { key:'pc', title:'PC', icon:'🖥️', match:[/\bpc\b/i,/computer/i] },
  { key:'ps5', title:'PlayStation 5', icon:'🎯', match:[/playstation/i,/ps\s?5/i,/ps5/i] },
  { key:'vr', title:'VR Station', icon:'🥽', match:[/\bvr\b/i,/virtual/i] },
  { key:'other', title:'Other / ไม่เข้าหมวด', icon:'📦', match:[] }
];
const $ = id => document.getElementById(id);
const el = {
  refreshBtn:$('refreshBtn'), diagBtn:$('diagBtn'), rawBtn:$('rawBtn'), closeDiagBtn:$('closeDiagBtn'),
  dateInput:$('dateInput'), timeInput:$('timeInput'), inspectDateInput:$('inspectDateInput'), inspectTimeInput:$('inspectTimeInput'), inspectBtn:$('inspectBtn'),
  availabilityFilter:$('availabilityFilter'), categoryList:$('categoryList'), metrics:$('metrics'), message:$('message'), messageHint:$('messageHint'),
  connectionText:$('connectionText'), updated:$('updated'), sourceText:$('sourceText'), refreshText:$('refreshText'), clock:$('clock'),
  detailTitle:$('detailTitle'), detailDesc:$('detailDesc'), detailPill:$('detailPill'), categoryStats:$('categoryStats'), unitGrid:$('unitGrid'), inspectResult:$('inspectResult'), slotSummary:$('slotSummary'), timeline:$('timeline'),
  todayBookingList:$('todayBookingList'), centerStatusBox:$('centerStatusBox'), diagPanel:$('diagPanel'), diagOut:$('diagOut')
};
const state = {data:null, groups:[], selected:'all', diag:{}, timer:null};

function today(){const d=new Date();return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`}
function nowHM(){const d=new Date(); return `${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`;}
function esc(s){return String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]))}
function hmToMin(hm){const m=/^(\d{1,2}):(\d{2})$/.exec(String(hm||'')); if(!m) return null; return Number(m[1])*60+Number(m[2]);}
function minutesNow(){const n=new Date();return n.getHours()*60+n.getMinutes()}
function sameDay(a,b){return String(a||'')===String(b||'')}
function isPastSlot(date,start,end){const selected=String(date||''), todayStr=today(), endMin=hmToMin(end); if(selected<todayStr) return true; if(selected>todayStr) return false; return endMin!==null && minutesNow()>=endMin}
function isCurrentSlot(date,start,end){const startMin=hmToMin(start), endMin=hmToMin(end); return sameDay(date,today()) && startMin!==null && endMin!==null && minutesNow()>=startMin && minutesNow()<endMin}
function categoryOf(service){const name=(service.name||'').toLowerCase(); for(const c of BASE_CATEGORIES){ if(c.key==='other') continue; if(c.match.some(r=>r.test(name))) return c.key; } return 'other';}
function categoryDef(key){return key==='all' ? {key:'all',title:'All / ทั้งหมด',icon:'✨'} : BASE_CATEGORIES.find(c=>c.key===key) || BASE_CATEGORIES.at(-1)}
function statusClassFromAvailability(available,total,booked){ if(Number(available)<=0) return 'bad'; if(Number(booked)>0) return 'warn'; return 'ok'; }
function statusTextFromAvailability(available,total,booked){ if(Number(available)<=0) return 'เต็ม / ไม่ว่าง'; if(Number(booked)>0) return 'ว่างบางส่วน'; return 'ว่าง'; }
function slotVisual(slot, capacity, date){
  const booked = Number(slot?.booked_count||0);
  const noShow = Number(slot?.no_show_count||0);
  const total = Number(capacity||slot?.total_capacity||1);
  if(slot?.status === 'closed'){
    return {cls:'past', ratio:`0/${total}`, label:'ปิด / Maintenance', note:slot?.closed_reason || `ช่วง ${slot.start} - ${slot.end} ปิดให้บริการ`};
  }
  if(noShow > 0){
    return {cls:'noshow', ratio:`${booked}/${total}`, label:isCurrentSlot(date,slot.start,slot.end)?'No Show / กำลังล็อก':'No Show / จองไม่ได้', note:`ช่วง ${slot.start} - ${slot.end} ถูกตั้งเป็น No Show จึงยังไม่เปิดให้จองซ้ำ`};
  }
  if(booked > 0){
    return {cls:'bad', ratio:`${booked}/${total}`, label:isCurrentSlot(date,slot.start,slot.end)?'กำลังถูกจอง':'ถูกจองแล้ว', note:`ช่วง ${slot.start} - ${slot.end} มีการจองแล้ว`};
  }
  if(isPastSlot(date,slot?.start,slot?.end)){
    return {cls:'past', ratio:`0/${total}`, label:'ผ่านไปแล้ว', note:`ช่วง ${slot.start} - ${slot.end} ผ่านไปแล้วและไม่ได้ถูกจอง`};
  }
  return {cls:'ok', ratio:`0/${total}`, label:isCurrentSlot(date,slot.start,slot.end)?'ว่างตอนนี้':'ว่าง / จองได้', note:`ช่วง ${slot.start} - ${slot.end} ยังว่าง`};
}
function formatNow(){el.clock.textContent=new Date().toLocaleTimeString('th-TH',{hour12:false});}
function setMessage(html=''){el.message.innerHTML=html}

function makeGroups(services){
  const groups = [{key:'all',title:'All / ทั้งหมด',icon:'✨',services:[...(services||[])]}];
  for(const c of BASE_CATEGORIES) groups.push({...c, services:[]});
  const by = Object.fromEntries(groups.map(g=>[g.key,g]));
  (services||[]).forEach(s => by[categoryOf(s)].services.push(s));
  return groups.filter(g => g.key==='all' || g.services.length);
}
function aggregate(group){
  const services=group?.services||[];
  const total=services.reduce((a,s)=>a+Number(s.capacity||1),0);
  const available=services.reduce((a,s)=>a+Number(s.available_now||0),0);
  const bookedNow=services.reduce((a,s)=>a+Number(s.booked_now||0),0);
  const todayBookings=services.reduce((a,s)=>a+(s.today_bookings?.length||0),0);
  const next=services.map(s=>s.next_booking && {...s.next_booking, service_name:s.name, category:categoryDef(categoryOf(s)).title}).filter(Boolean).sort((a,b)=>a.start_full.localeCompare(b.start_full))[0]||null;
  const slotMap=new Map();
  services.forEach(s => (s.slots||[]).forEach(sl=>{
    const key=sl.start+'|'+sl.end;
    if(!slotMap.has(key)) slotMap.set(key,{start:sl.start,end:sl.end,booked_count:0,available_count:0,total_capacity:0});
    const row=slotMap.get(key);
    row.booked_count += Number(sl.booked_count||0);
    row.available_count += Number(sl.available_count||0);
    row.total_capacity += Number(s.capacity||1);
  }));
  const slots=[...slotMap.values()].sort((a,b)=>hmToMin(a.start)-hmToMin(b.start)||hmToMin(a.end)-hmToMin(b.end));
  return {services,total,available,busy:Math.max(0,total-available),bookedNow,todayBookings,next,slots};
}
function selectedGroup(){return state.groups.find(g=>g.key===state.selected) || state.groups[0] || {key:'all',title:'All / ทั้งหมด',services:[]}}
function centerClosed(){return state.data?.center?.open===false}
function renderCenterStatus(){
  const c=state.data?.center; if(!c){el.centerStatusBox.innerHTML=''; return;}
  if(c.open){
    el.centerStatusBox.className='center-status panel open';
    const periods=(c.open_periods||[]).map(p=>`${esc(p[0])}–${esc(p[1])}`).join(', '); el.centerStatusBox.innerHTML=`<div><h2>✅ วันที่ ${esc(c.date||state.data?.date||'')} ศูนย์เปิดให้บริการ</h2><p>ช่วงที่เปิด: ${periods || '09:00–16:00'} ${c.reason?'• '+esc(c.reason):''} • ${c.source==='date_override'?'ตั้งค่าเฉพาะวันนี้':'ตารางอัตโนมัติประจำสัปดาห์'}</p></div><span class="badge ok">OPEN</span>`;
  }else{
    el.centerStatusBox.className='center-status panel closed';
    el.centerStatusBox.innerHTML=`<div><h2>⛔ วันที่ ${esc(c.date||state.data?.date||'')} ศูนย์ปิดให้บริการ</h2><p>${c.reason?esc(c.reason):'วันหยุดตามตารางอัตโนมัติ'} • ทุกช่วงเวลาจะแสดงเป็นสีเทา และไม่ถือว่าเป็นการจอง</p></div><span class="badge past">CLOSED</span>`;
  }
}

function bookingStatusBadge(b){
  const key = String(b?.status_key || b?.status || '').replace(/[\s_-]+/g,'').toLowerCase();
  if(b?.is_no_show || key.includes('noshow')) return '<span class="badge noshow">No Show / จองไม่ได้</span>';
  return '<span class="badge bad">ถูกจองแล้ว</span>';
}
function allBookings(group){
  const rows=[];
  (group.services||[]).forEach(s=>{
    const c=categoryDef(categoryOf(s));
    (s.today_bookings||[]).forEach(b=>rows.push({...b, service_name:s.name, category_key:c.key, category_title:c.title, category_icon:c.icon}));
  });
  return rows.sort((a,b)=>String(a.start_full).localeCompare(String(b.start_full)));
}
function bookingsAtTime(group, hm){
  const minute=hmToMin(hm); if(minute===null) return null;
  const rows=(group.services||[]).map(s=>{
    const hit=(s.today_bookings||[]).find(b=>{
      const st=hmToMin(b.start), en=hmToMin(b.end); return st!==null && en!==null && minute>=st && minute<en;
    });
    return {service:s.name,busy:!!hit,booking:hit||null};
  });
  const busy=rows.filter(r=>r.busy).length;
  return {rows,busy,free:rows.length-busy,total:rows.length};
}

function filteredGroups(){
  const f=el.availabilityFilter.value;
  return state.groups.filter(g=>{
    const a=aggregate(g);
    if(f==='available') return a.available>0;
    if(f==='busy') return a.available<=0;
    if(f==='hasBooking') return a.todayBookings>0;
    return true;
  });
}
function renderMetrics(){
  const d=state.data; if(!d) return;
  const closed=centerClosed();
  const all=aggregate(state.groups.find(g=>g.key==='all')||{services:[]});
  el.metrics.innerHTML=`
    <article class="panel metric"><div class="k">สถานะศูนย์</div><div class="v">${closed?'ปิด':'เปิด'}</div><div class="s">${closed?'ปิดให้บริการวันนี้':'เปิดให้บริการวันนี้'}</div></article>
    <article class="panel metric"><div class="k">หมวดที่ถูกจอง</div><div class="v">${state.groups.filter(g=>g.key!=='all'&&aggregate(g).todayBookings>0).length}</div><div class="s">เลือกหมวดด้านซ้ายเพื่อดูรายละเอียด</div></article>
    <article class="panel metric"><div class="k">เครื่องทั้งหมด</div><div class="v">${all.total}</div><div class="s">รวมทุก service</div></article>
    <article class="panel metric"><div class="k">ว่างตอนนี้</div><div class="v">${all.available}/${all.total}</div><div class="s">ตามเวลาปัจจุบัน</div></article>`;
}
function renderCategories(){
  const groups=filteredGroups();
  if(!groups.some(g=>g.key===state.selected) && groups[0]) state.selected=groups[0].key;
  el.categoryList.innerHTML=groups.map(g=>{
    const a=aggregate(g);
    const cls=centerClosed()?'past':statusClassFromAvailability(a.available,a.total,a.bookedNow);
    const txt=centerClosed()?'ปิดให้บริการ':statusTextFromAvailability(a.available,a.total,a.bookedNow);
    return `<button class="cat-btn ${g.key===state.selected?'active':''}" data-cat="${esc(g.key)}">
      <div class="cat-left">
        <div class="cat-icon">${g.icon}</div>
        <div>
          <div class="cat-name">${esc(g.title)}</div>
          <div class="cat-meta">Booking วันนี้ ${a.todayBookings} • ว่าง ${a.available}/${a.total}</div>
        </div>
      </div>
      <span class="badge ${cls}">${txt}</span>
    </button>`;
  }).join('') || '<div class="empty">ไม่มีหมวดตาม filter นี้</div>';
  [...el.categoryList.querySelectorAll('.cat-btn')].forEach(btn=>btn.onclick=()=>{state.selected=btn.dataset.cat; renderAll();});
}
function renderDetail(){
  const group=selectedGroup(), a=aggregate(group), date=el.dateInput.value||today();
  const cls=centerClosed()?'past':statusClassFromAvailability(a.available,a.total,a.bookedNow);
  el.detailTitle.textContent=group.title;
  el.detailDesc.textContent=centerClosed()?'วันนี้ศูนย์ปิดให้บริการ ตารางจะแสดงสีเทาทั้งหมด':(group.key==='all'?'รวมทุกหมวด เพื่อดูว่า Booking วันนี้ทั้งหมดอยู่เครื่องไหน ช่วงเวลาใด':'ดูเฉพาะหมวด '+group.title);
  el.detailPill.className='pill '+cls;
  el.detailPill.textContent=centerClosed()?`ปิดให้บริการ • ${state.data.center?.reason||'ไม่ระบุเหตุผล'}`:`Booking วันนี้ ${a.todayBookings} • ว่างตอนนี้ ${a.available}/${a.total}`;
  el.categoryStats.innerHTML=`
    <div class="stat"><span class="muted mini">เครื่องในหมวด</span><b>${a.total}</b></div>
    <div class="stat"><span class="muted mini">ว่างตอนนี้</span><b>${a.available}</b></div>
    <div class="stat"><span class="muted mini">กำลังถูกจองตอนนี้</span><b>${a.bookedNow}</b></div>
    <div class="stat"><span class="muted mini">Booking วันนี้</span><b>${a.todayBookings}</b></div>`;
  el.unitGrid.innerHTML = (group.services||[]).map(s=>{
    const c=categoryDef(categoryOf(s));
    const busy=Number(s.booked_now||0)>0;
    return `<article class="unit">
      <span class="badge ${centerClosed()?'past':(busy?'bad':'ok')}">${centerClosed()?'ปิดให้บริการ':(busy?'กำลังถูกจอง':'ว่างตอนนี้')}</span>
      <h4>${esc(s.name)}</h4>
      <p>${group.key==='all'?esc(c.icon+' '+c.title):esc(s.description||'ไม่มีคำอธิบาย')}</p>
      <p style="margin-top:10px">วันนี้มี Booking: <b style="color:#fff">${s.today_bookings?.length||0}</b> รายการ</p>
      <p>คิวถัดไป: <b style="color:#fff">${s.next_booking ? esc(s.next_booking.start+' - '+s.next_booking.end) : 'ยังไม่มี'}</b></p>
    </article>`;
  }).join('') || '<div class="empty">ไม่มีอุปกรณ์ในหมวดนี้</div>';

  const inspectTime=el.inspectTimeInput.value || el.timeInput.value || nowHM();
  const inspected=bookingsAtTime(group, inspectTime);
  el.inspectResult.innerHTML = centerClosed() ? `<div class="empty">วันนี้ศูนย์ปิดให้บริการ จึงไม่มีเครื่องที่เปิดให้จองในเวลานี้</div>` : inspected ? `
    <div style="display:flex;justify-content:space-between;gap:12px;align-items:flex-start;flex-wrap:wrap">
      <div>
        <div class="muted mini">วันที่ ${esc(el.inspectDateInput.value||date)} เวลา ${esc(inspectTime)}</div>
        <div style="font-size:24px;font-weight:950;margin-top:6px">ว่าง ${inspected.free}/${inspected.total} เครื่อง</div>
      </div>
      <span class="badge ${inspected.free>0?'ok':'bad'}">${inspected.free>0?'มีเครื่องว่าง':'เต็มทั้งหมด'}</span>
    </div>
    <div style="display:grid;gap:8px;margin-top:12px">
      ${inspected.rows.map(r=>`<div class="pill ${r.busy?'bad':'ok'}">${esc(r.service)} — ${r.busy?'ถูกจอง '+esc(r.booking.start+' - '+r.booking.end):'ว่าง / จองได้'}</div>`).join('')}
    </div>` : 'เวลาไม่ถูกต้อง';

  const bookings=allBookings(group);
  el.todayBookingList.innerHTML = centerClosed() ? '<div class="empty">วันนี้ศูนย์ปิดให้บริการ จึงไม่แสดงรายการเป็นการจองของผู้ใช้</div>' : bookings.length ? bookings.map(b=>`
    <article class="booking-item">
      <div class="booking-time">${esc(b.start)} - ${esc(b.end)}</div>
      <div>
        <div class="booking-title">${esc(b.service_name)}</div>
        <div class="booking-sub">${esc(b.category_icon)} ${esc(b.category_title)} ${b.customer? '• '+esc(b.customer):''}</div>
      </div>
      ${bookingStatusBadge(b)}
    </article>`).join('') : '<div class="empty">วันนี้ยังไม่มี Booking ในหมวดนี้</div>';

  el.slotSummary.innerHTML = a.slots.length ? a.slots.map(sl=>{
    const v=slotVisual(sl, sl.total_capacity||a.total||1, date);
    return `<article class="slot">
      <div class="slot-top"><div class="slot-time">${esc(sl.start)} - ${esc(sl.end)}</div><span class="badge ${v.cls}">${esc(v.label)}</span></div>
      <div><b>${esc(v.ratio)}</b></div>
      <small>${esc(v.note)}</small>
    </article>`;
  }).join('') : '<div class="empty">ไม่มีช่วงเวลาให้แสดง</div>';

  renderTimeline(group, a.slots, date);
  el.messageHint.textContent=`กำลังดู: ${group.title}`;
}
function renderTimeline(group, slots, date){
  if(!slots.length || !(group.services||[]).length){el.timeline.innerHTML='<div class="empty">ไม่มีข้อมูลตาราง</div>'; return;}
  const head=slots.map(sl=>`<th>${esc(sl.start)}<br><span class="mini muted">${esc(sl.end)}</span></th>`).join('');
  const rows=group.services.map(s=>{
    const c=categoryDef(categoryOf(s));
    const cells=slots.map(groupSlot=>{
      const hit=(s.slots||[]).find(sl=>sl.start===groupSlot.start && sl.end===groupSlot.end) || {start:groupSlot.start,end:groupSlot.end,booked_count:0,available_count:Number(s.capacity||1)};
      const v=slotVisual(hit, Number(s.capacity||1), date);
      return `<td><div class="slot-cell"><span class="badge ${v.cls}">${esc(v.ratio)}</span><div class="slot-note">${esc(v.label)}</div></div></td>`;
    }).join('');
    return `<tr><td><b>${esc(s.name)}</b><div class="mini muted">${esc(c.icon+' '+c.title)}</div></td>${cells}</tr>`;
  }).join('');
  el.timeline.innerHTML=`<div class="tablewrap"><table><thead><tr><th>เครื่อง / Service</th>${head}</tr></thead><tbody>${rows}</tbody></table></div>`;
}
function renderAll(){renderCenterStatus();renderMetrics();renderCategories();renderDetail();}
function scheduleNextPoll(seconds){clearTimeout(state.timer);state.timer=setTimeout(()=>load(false),Math.max(3,Number(seconds)||10)*1000)}
async function load(showOk){
  try{
    const date=el.dateInput.value || today();
    const r=await fetch('/api/status?date='+encodeURIComponent(date)+'&_='+Date.now(),{cache:'no-store'});
    if(!r.ok) throw new Error('API HTTP '+r.status);
    const text=await r.text();
    let data; try{data=JSON.parse(text)}catch{throw new Error('API ไม่ได้ตอบ JSON: '+text.slice(0,160))}
    if(!data.ok) throw new Error(data.error||'API not ok');
    state.data=data; state.diag=data; state.groups=makeGroups(data.services||[]);

    if(!state.groups.some(g=>g.key===state.selected)) state.selected='all';
    const remote=data.source==='remote_csv_live';
    el.connectionText.textContent=remote?'เชื่อม CSV จริงแล้ว':'ใช้ sample/fallback อยู่';
    el.updated.textContent='อัปเดตล่าสุด: '+data.generated_at;
    el.sourceText.textContent='source: '+data.source;
    el.refreshText.textContent='Auto refresh ทุก '+(data.refresh_seconds||10)+' วินาที';
    if(showOk || !remote){
      setMessage(remote ? '<div class="alert">ดึงข้อมูลล่าสุดจาก CSV สำเร็จแล้ว ถ้า Booking วันนี้มีตัวเลข ให้กด <b>All / ทั้งหมด</b> เพื่อดูรายการทั้งหมด</div>' : '<div class="alert error">เว็บขึ้นแล้ว แต่ยังอ่าน CSV จริงไม่สำเร็จ จึงใช้ sample/fallback อยู่ กด “ดูการเชื่อมต่อ” เพื่อดู error</div>');
    }
    renderAll();
    scheduleNextPoll(data.refresh_seconds||10);
  }catch(err){
    state.diag={error:String(err)};
    setMessage('<div class="alert error"><b>เชื่อมข้อมูลไม่สำเร็จ</b><br>'+esc(err.message)+'</div>');
    scheduleNextPoll(10);
  }
}
function init(){
  const td=today(), tm=nowHM();
  el.dateInput.value=td; el.inspectDateInput.value=td; el.timeInput.value=tm; el.inspectTimeInput.value=tm;
  formatNow(); setInterval(formatNow,1000);
  el.refreshBtn.onclick=()=>load(true);
  el.diagBtn.onclick=()=>{el.diagPanel.classList.remove('hide');el.diagOut.textContent=JSON.stringify(state.diag,null,2)};
  el.closeDiagBtn.onclick=()=>el.diagPanel.classList.add('hide');
  el.rawBtn.onclick=()=>window.open('/api/raw-check?_='+Date.now(),'_blank');
  el.availabilityFilter.onchange=()=>renderAll();
  el.dateInput.onchange=()=>{el.inspectDateInput.value=el.dateInput.value;load(true)};
  el.timeInput.onchange=()=>{el.inspectTimeInput.value=el.timeInput.value;renderDetail()};
  el.inspectBtn.onclick=()=>renderDetail();
  el.inspectTimeInput.onchange=()=>renderDetail();
  if(location.protocol==='file:'){
    setMessage('<div class="alert error"><b>ห้ามเปิด index.html ตรง ๆ</b><br>ให้แตก ZIP แล้วกด <b>start-dashboard.bat</b> เพื่อเปิด server ก่อน</div>');
  }else{
    load(true);
  }
}
init();


/* v20 clean bilingual layer: re-render user page blocks instead of word-by-word mixing */
(function(){
  const I18N = {
    th: {
      current:'ไทย', next:'EN',
      title:'PSU Esports Booking Board v26',
      lead:'หน้าแสดงสถานะการจองสำหรับผู้ใช้งานจริง พร้อมตารางเปิด/ปิดอัตโนมัติ: จันทร์–ศุกร์เปิด, จันทร์เช้าและศุกร์บ่ายปิด Maintenance, เสาร์–อาทิตย์ปิด',
      refresh:'ดึง CSV ใหม่ตอนนี้', diag:'ดูการเชื่อมต่อ', raw:'เปิด raw-check',
      live:'เชื่อม CSV จริงแล้ว', fallback:'ใช้ sample/fallback อยู่',
      updated:'อัปเดตล่าสุด: ', source:'source: ', refreshEvery:'Auto refresh ทุก ', sec:' วินาที',
      filterAll:'ทุกสถานะ', filterAvailable:'มีเครื่องว่างอยู่ตอนนี้', filterBusy:'เต็ม / ไม่ว่างตอนนี้', filterHasBooking:'มี Booking วันนี้',
      hint:'เลือกหมวดทางซ้ายเพื่อดูรายละเอียด',
      centerStatus:'สถานะศูนย์', open:'เปิด', closed:'ปิด', openToday:'เปิดให้บริการวันนี้', closedToday:'ปิดให้บริการวันนี้',
      bookedCats:'หมวดที่ถูกจอง', selectLeft:'เลือกหมวดด้านซ้ายเพื่อดูรายละเอียด',
      totalDevices:'เครื่องทั้งหมด', allServices:'รวมทุก service', availableNow:'ว่างตอนนี้', atCurrent:'ตามเวลาปัจจุบัน',
      successMsg:'ดึงข้อมูลล่าสุดจาก CSV สำเร็จแล้ว ถ้า Booking วันนี้มีตัวเลข ให้กด All / ทั้งหมด เพื่อดูรายการทั้งหมด',
      centerOpen:'ศูนย์เปิดให้บริการ', centerClosed:'ศูนย์ปิดให้บริการ',
      openPeriods:'ช่วงที่เปิด', weekly:'ตารางอัตโนมัติประจำสัปดาห์', override:'ตั้งค่าเฉพาะวันนี้',
      closedNote:'ทุกช่วงเวลาจะแสดงเป็นสีเทา และไม่ถือว่าเป็นการจอง',
      noReason:'วันหยุดหรือช่วง Maintenance ตามตารางอัตโนมัติ',
      green:'ว่าง / จองได้', greenSub:'สีเขียว 0/1', red:'ถูกจองแล้ว', redSub:'สีแดง 1/1',
      purple:'No Show', purpleSub:'สีม่วง 1/1 จองไม่ได้', gray:'ผ่านเวลา / ปิด / Maintenance', graySub:'สีเทา 0/1',
      sideTitle:'หมวดอุปกรณ์', sideSub:'กด All เพื่อดูทุก booking ที่ทำให้เลข Booking วันนี้ขึ้น',
      all:'All / ทั้งหมด', bookingToday:'Booking วันนี้', freeShort:'ว่าง',
      allTitle:'All / ทั้งหมด', allDesc:'รวมทุกหมวด เพื่อดูว่า Booking วันนี้ทั้งหมดอยู่เครื่องไหน ช่วงเวลาใด',
      categoryDevices:'เครื่องในหมวด', categoryAvailable:'ว่างตอนนี้', categoryBusy:'กำลังถูกจองตอนนี้',
      devicesTitle:'อุปกรณ์ในหมวดนี้', devicesHelper:'แสดงสถานะปัจจุบันของแต่ละอุปกรณ์',
      inspectTitle:'ตรวจสอบช่วงเวลาที่ต้องการ', inspectHelper:'เลือกวันและเวลาเพื่อดูว่าอุปกรณ์ในหมวดนี้ว่างกี่เครื่อง',
      check:'ตรวจสอบ', notChecked:'ยังไม่ได้ตรวจสอบ',
      todayListTitle:'รายการจองวันนี้', todayListDesc:'ถ้า Booking วันนี้มีตัวเลข ให้กด All แล้วดูรายการตรงนี้ว่าอยู่เครื่องไหน เวลาไหน',
      noBookings:'วันนี้ไม่มี Booking ใน Category นี้',
      slotSummary:'สรุปสถานะตามเวลา', slotSummaryDesc:'สรุปเป็น Slot เวลา Red หมายถึง Slot นั้นมี booking อย่างน้อย 1 records',
      deviceTable:'ตารางเครื่องรายตัว 09:00–16:00', deviceTableDesc:'Red/ม่วงจะค้างไว้ถ้า Slot นั้นถูก Bookedหรือ No Show ส่วน Cancel จะ Openให้ Available',
      devicesService:'devices / Service',
      statusAvailable:'ว่าง / จองได้', statusBooked:'ถูกจองแล้ว', statusNoShow:'No Show / จองไม่ได้', statusClosed:'ปิด / Maintenance',
      statusPast:'ผ่านไปแล้ว', statusNowFree:'ว่างตอนนี้', statusCurrentBooked:'กำลังถูกจอง', statusCurrentNoShow:'No Show / กำลังล็อก',
      noBooking:'ยังไม่มี', currentBookings:'วันนี้มี Booking', nextQueue:'คิวถัดไป', records:'รายการ',
      availableBadge:'มีเครื่องว่าง',
      datePrefix:'วันที่'
    },
    en: {
      current:'English', next:'TH',
      title:'PSU Esports Booking Board v26',
      lead:'Live booking status for users with an automatic operating calendar: open Monday–Friday, Monday morning and Friday afternoon under maintenance, closed Saturday–Sunday.',
      refresh:'Refresh CSV now', diag:'Connection status', raw:'Open raw-check',
      live:'Connected to live CSV', fallback:'Using sample/fallback data',
      updated:'Last updated: ', source:'source: ', refreshEvery:'Auto refresh every ', sec:' seconds',
      filterAll:'All status', filterAvailable:'Available now', filterBusy:'Full / Busy now', filterHasBooking:'Has bookings today',
      hint:'Select a category on the left to view details',
      centerStatus:'Center status', open:'Open', closed:'Closed', openToday:'Open today', closedToday:'Closed today',
      bookedCats:'Booked categories', selectLeft:'Select a category on the left to view details',
      totalDevices:'Total devices', allServices:'All services', availableNow:'Available now', atCurrent:'At current time',
      successMsg:'Latest CSV data loaded successfully. If today has bookings, select All to see all records.',
      centerOpen:'center is open', centerClosed:'center is closed',
      openPeriods:'Open periods', weekly:'Weekly auto schedule', override:'Date override',
      closedNote:'All time slots are gray and are not counted as bookings',
      noReason:'Holiday or maintenance according to the auto schedule',
      green:'Available / Bookable', greenSub:'Green 0/1', red:'Booked', redSub:'Red 1/1',
      purple:'No Show', purpleSub:'Purple 1/1 not bookable', gray:'Past / Closed / Maintenance', graySub:'Gray 0/1',
      sideTitle:'Device categories', sideSub:'Use All to see every booking counted today',
      all:'All', bookingToday:'Bookings today', freeShort:'Available',
      allTitle:'All', allDesc:'All categories, showing which devices and time slots have bookings today',
      categoryDevices:'Devices in category', categoryAvailable:'Available now', categoryBusy:'Currently booked',
      devicesTitle:'Devices in this category', devicesHelper:'Current status for each device',
      inspectTitle:'Check a specific time', inspectHelper:'Choose a date and time to see how many devices are available',
      check:'Check', notChecked:'Not checked yet',
      todayListTitle:"Today's bookings", todayListDesc:'If today has bookings, select All and check here to see the device and time.',
      noBookings:'No bookings today in this category',
      slotSummary:'Time-slot status summary', slotSummaryDesc:'Summary by time slot. Red means at least one booking overlaps that slot.',
      deviceTable:'Device table 09:00–16:00', deviceTableDesc:'Red/Purple remain locked if the slot is booked or No Show. Cancel makes the slot available again.',
      devicesService:'Devices / Service',
      statusAvailable:'Available / Bookable', statusBooked:'Booked', statusNoShow:'No Show / Not bookable', statusClosed:'Closed / Maintenance',
      statusPast:'Past', statusNowFree:'Available now', statusCurrentBooked:'Currently booked', statusCurrentNoShow:'No Show / Locked',
      noBooking:'None', currentBookings:'Bookings today', nextQueue:'Next booking', records:'records',
      availableBadge:'Available',
      datePrefix:'Date'
    }
  };

  function lang(){return window.psuLang || document.body.getAttribute('data-lang') || 'th';}
  function t(k){return (I18N[lang()] && I18N[lang()][k]) || I18N.th[k] || k;}
  function esc2(s){return String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]));}
  function setText(sel, val){const el=document.querySelector(sel); if(el) el.textContent=val;}
  function setHTML(sel, val){const el=document.querySelector(sel); if(el) el.innerHTML=val;}

  function setLang(v){
    window.psuLang = v === 'en' ? 'en' : 'th';
    document.body.setAttribute('data-lang', window.psuLang);
    applyStatic();
    rerender();
  }
  window.psuSetLang=setLang;
  window.psuLangText=t;

  function applyStatic(){
    document.title=t('title');
    setText('h1',t('title'));
    const eyebrow=document.querySelector('.eyebrow'); if(eyebrow) eyebrow.innerHTML='<span class="pulse"></span> PSU ESPORTS BOOKING DASHBOARD';
    setHTML('.lead',t('lead'));
    setText('#refreshBtn',t('refresh')); setText('#diagBtn',t('diag')); setText('#rawBtn',t('raw')); setText('#messageHint',t('hint'));
    const btn=document.getElementById('langToggle'); if(btn) btn.innerHTML=`<span class="lang-current">${t('current')}</span><span class="lang-next">${t('next')}</span>`;
    const opts=document.querySelectorAll('#availabilityFilter option');
    if(opts[0]) opts[0].textContent=t('filterAll');
    if(opts[1]) opts[1].textContent=t('filterAvailable');
    if(opts[2]) opts[2].textContent=t('filterBusy');
    if(opts[3]) opts[3].textContent=t('filterHasBooking');

    const guides=document.querySelectorAll('.quick-guide .guide-item');
    [[t('green'),t('greenSub')],[t('red'),t('redSub')],[t('purple'),t('purpleSub')],[t('gray'),t('graySub')]].forEach((p,i)=>{
      const b=guides[i]?.querySelector('b'), s=guides[i]?.querySelector('span');
      if(b)b.textContent=p[0]; if(s)s.textContent=p[1];
    });
    setText('.side-title',t('sideTitle'));
    setText('.side-sub',t('sideSub'));
  }

  window.slotVisual = function(slot, capacity, date){
    const booked=Number(slot?.booked_count||0), noShow=Number(slot?.no_show_count||0), total=Number(capacity||slot?.total_capacity||1);
    if(slot?.status==='closed') return {cls:'past', ratio:`0/${total}`, label:t('statusClosed'), note:slot?.closed_reason||t('statusClosed')};
    if(noShow>0) return {cls:'noshow', ratio:`${booked}/${total}`, label:isCurrentSlot(date,slot.start,slot.end)?t('statusCurrentNoShow'):t('statusNoShow'), note:`${slot.start} - ${slot.end} ${t('statusNoShow')}`};
    if(booked>0) return {cls:'bad', ratio:`${booked}/${total}`, label:isCurrentSlot(date,slot.start,slot.end)?t('statusCurrentBooked'):t('statusBooked'), note:`${slot.start} - ${slot.end} ${t('statusBooked')}`};
    if(isPastSlot(date,slot?.start,slot?.end)) return {cls:'past', ratio:`0/${total}`, label:t('statusPast'), note:`${slot.start} - ${slot.end} ${t('statusPast')}`};
    return {cls:'ok', ratio:`0/${total}`, label:isCurrentSlot(date,slot.start,slot.end)?t('statusNowFree'):t('statusAvailable'), note:`${slot.start} - ${slot.end} ${t('statusAvailable')}`};
  };

  function renderMetricsClean(){
    const d=window.state?.data; if(!d) return;
    const el=document.getElementById('metrics'); if(!el) return;
    const closed=!!(d.center && !d.center.open);
    const services=d.services||[];
    const total=services.length;
    const available=services.reduce((a,s)=>a+Number(s.available_now||0),0);
    const bookedCats=services.filter(s=>(s.today_bookings||[]).length>0).length;
    el.innerHTML=`
      <article class="panel metric"><div class="k">${t('centerStatus')}</div><div class="v">${closed?t('closed'):t('open')}</div><div class="s">${closed?t('closedToday'):t('openToday')}</div></article>
      <article class="panel metric"><div class="k">${t('bookedCats')}</div><div class="v">${bookedCats}</div><div class="s">${t('selectLeft')}</div></article>
      <article class="panel metric"><div class="k">${t('totalDevices')}</div><div class="v">${total}</div><div class="s">${t('allServices')}</div></article>
      <article class="panel metric"><div class="k">${t('availableNow')}</div><div class="v">${available}/${total}</div><div class="s">${t('atCurrent')}</div></article>`;
  }

  function renderCenterClean(){
    const data=window.state?.data, c=data?.center, box=document.getElementById('centerStatusBox'); if(!c||!box)return;
    if(c.open){
      const periods=(c.open_periods||[]).map(p=>`${esc2(p[0])}–${esc2(p[1])}`).join(', ');
      box.className='center-status panel open';
      box.innerHTML=`<div><h2>✅ ${t('datePrefix')} ${esc2(c.date||data.date)} ${t('centerOpen')}</h2><p>${t('openPeriods')}: ${periods||'09:00–16:00'} ${c.reason?'• '+esc2(c.reason):''} • ${c.source==='date_override'?t('override'):t('weekly')}</p></div><span class="badge ok">OPEN</span>`;
    }else{
      box.className='center-status panel closed';
      box.innerHTML=`<div><h2>⛔ ${t('datePrefix')} ${esc2(c.date||data.date)} ${t('centerClosed')}</h2><p>${esc2(c.reason||t('noReason'))} • ${t('closedNote')}</p></div><span class="badge past">CLOSED</span>`;
    }
  }

  function renderGuidesClean(){ applyStatic(); }

  function categoryOfName(g){
    return g?.key==='all' ? t('all') : (g?.title || g?.name || '');
  }

  function patchCategoryList(){
    const list=document.getElementById('categoryList'); if(!list) return;
    list.querySelectorAll('.cat-btn').forEach(btn=>{
      btn.innerHTML=btn.innerHTML
        .replace(/All \/ ทั้งหมด/g,t('all'))
        .replace(/Booking วันนี้/g,t('bookingToday'))
        .replace(/ว่าง/g,t('freeShort'))
        .replace(/จอง/g,t('statusBooked'));
    });
  }

  function patchDetailHead(){
    const title=document.getElementById('detailTitle');
    const desc=document.getElementById('detailDesc');
    if(title && /All|ทั้งหมด/.test(title.textContent)) title.textContent=t('allTitle');
    if(desc && (/รวมทุกหมวด|All categories/.test(desc.textContent))) desc.textContent=t('allDesc');
    document.querySelectorAll('.stat .k').forEach(el=>{
      const raw=el.textContent.trim();
      if(raw.includes('เครื่องในหมวด')||raw.includes('Devices in category')) el.textContent=t('categoryDevices');
      if(raw.includes('ว่างตอนนี้')||raw.includes('Available now')) el.textContent=t('categoryAvailable');
      if(raw.includes('กำลังถูกจอง')||raw.includes('Currently booked')) el.textContent=t('categoryBusy');
      if(raw.includes('Booking วันนี้')||raw.includes('Bookings today')) el.textContent=t('bookingToday');
    });
  }

  function patchCards(){
    const cards=document.querySelectorAll('.card');
    if(cards[0]){ const h=cards[0].querySelector('h3'), hp=cards[0].querySelector('.helper'); if(h)h.textContent=t('devicesTitle'); if(hp)hp.textContent=t('devicesHelper'); }
    if(cards[1]){ const h=cards[1].querySelector('h3'), hp=cards[1].querySelector('.helper'); if(h)h.textContent=t('inspectTitle'); if(hp)hp.textContent=t('inspectHelper'); }
    setText('#inspectBtn',t('check'));
    const insp=document.getElementById('inspectResult'); if(insp && (/ยังไม่ได้ตรวจสอบ|Not checked/.test(insp.textContent))) insp.textContent=t('notChecked');
    document.querySelectorAll('.unit-card').forEach(card=>{
      card.innerHTML=card.innerHTML
        .replace(/วันนี้มี Booking:/g,t('currentBookings')+':')
        .replace(/คิวถัดไป:/g,t('nextQueue')+':')
        .replace(/ยังไม่มี/g,t('noBooking'))
        .replace(/รายการ/g,t('records'))
        .replace(/ว่างตอนนี้/g,t('statusNowFree'))
        .replace(/ว่าง \/ จองได้/g,t('statusAvailable'))
        .replace(/ถูกจองแล้ว/g,t('statusBooked'))
        .replace(/ปิด \/ Maintenance/g,t('statusClosed'));
    });
  }

  function patchBookingList(){
    document.querySelectorAll('.panel h2,.panel h3').forEach(h=>{
      const tx=h.textContent.trim();
      if(tx.includes('recordsBooked') || tx.includes('รายการจอง') || tx.includes("Today's bookings") || tx.includes('Booking วันนี้')){
        h.textContent=t('todayListTitle');
      }
      if(tx.includes('สรุปสถานะ') || tx.includes('Time-slot')) h.textContent=t('slotSummary');
      if(tx.includes('ตาราง') || tx.includes('Device table')) h.textContent=t('deviceTable');
    });
    document.querySelectorAll('.panel p,.helper').forEach(p=>{
      const tx=p.textContent;
      if(tx.includes('records') && tx.includes('devices')) p.textContent=t('todayListDesc');
      if(tx.includes('Slot') || tx.includes('booking อย่างน้อย')) p.textContent=t('slotSummaryDesc');
      if(tx.includes('Red/ม่วง') || tx.includes('Bookedหรือ')) p.textContent=t('deviceTableDesc');
    });
    document.querySelectorAll('.empty,.placeholder').forEach(e=>{
      if(e.textContent.includes('None') || e.textContent.includes('ไม่มี')) e.textContent=t('noBookings');
    });
  }

  function patchSlotSummary(){
    document.querySelectorAll('.slot,.slot-card,.timeline-card').forEach(el=>{
      el.innerHTML=el.innerHTML
        .replace(/Past/g,t('statusPast'))
        .replace(/Available now/g,t('statusNowFree'))
        .replace(/Available \/ Bookable/g,t('statusAvailable'))
        .replace(/Booked/g,t('statusBooked'))
        .replace(/No Show \/ Not bookable/g,t('statusNoShow'))
        .replace(/Closed \/ Maintenance/g,t('statusClosed'))
        .replace(/has passed and was not booked/g, lang()==='en'?'has passed and was not booked':'ผ่านไปแล้วและไม่ได้ถูกจอง')
        .replace(/is available/g, lang()==='en'?'is available':'ยังว่าง');
    });
    document.querySelectorAll('th').forEach(th=>{
      if(/devices|Service|เครื่อง|บริการ/i.test(th.textContent)) th.textContent=t('devicesService');
    });
  }

  function patchMessage(){
    const m=document.getElementById('message'); if(!m) return;
    if(m.textContent.includes('CSV') && m.textContent.includes('Booking')){
      m.innerHTML=`<div class="alert">${t('successMsg')}</div>`;
    }
  }

  function patchTopConnection(){
    const data=window.state?.data; if(!data) return;
    setText('#connectionText', data.source==='remote_csv_live'?t('live'):t('fallback'));
    const upd=document.getElementById('updated'); if(upd) upd.textContent=t('updated')+(data.generated_at||'');
    const src=document.getElementById('sourceText'); if(src) src.textContent=t('source')+(data.source||'');
    const rf=document.getElementById('refreshText'); if(rf) rf.textContent=t('refreshEvery')+(data.refresh_seconds||10)+t('sec');
  }

  function cleanMixedText(){
    if(lang()!=='en') return;
    document.querySelectorAll('*').forEach(el=>{
      if(el.children.length) return;
      let s=el.textContent;
      if(!s) return;
      const rep=[
        [/recordsBookedวันนี้/g,"Today's bookings"],
        [/วันนี้None Booking ในCategoryนี้/g,'No bookings today in this category'],
        [/วันนี้มี Booking/g,'Bookings today'],
        [/ในCategoryนี้/g,'in this category'],
        [/ตารางdevicesรายตัว/g,'Device table'],
        [/สรุปเป็นSlotเวลา/g,'Summary by time slot'],
        [/หมายถึงSlotนั้นมี booking อย่างน้อย/g,'means the slot has at least'],
        [/เครื่องในหมวด/g,'Devices in category'],
        [/กำลังถูกจองตอนนี้/g,'Currently booked'],
        [/ว่างตอนนี้/g,'Available now'],
        [/ปิดให้บริการวันนี้/g,'Closed today'],
        [/เปิดให้บริการวันนี้/g,'Open today'],
        [/รายการ/g,'records'],
        [/เครื่อง/g,'devices'],
        [/วันนี้/g,'today'],
        [/หมวด/g,'category']
      ];
      rep.forEach(([a,b])=>s=s.replace(a,b));
      if(s!==el.textContent) el.textContent=s;
    });
  }

  function rerender(){
    try{ if(typeof renderAll==='function') renderAll(); }catch(_){}
    setTimeout(applyAfterRender,0);
    setTimeout(applyAfterRender,80);
    setTimeout(applyAfterRender,250);
  }

  function applyAfterRender(){
    applyStatic();
    patchTopConnection();
    renderMetricsClean();
    renderCenterClean();
    renderGuidesClean();
    patchCategoryList();
    patchDetailHead();
    patchCards();
    patchBookingList();
    patchSlotSummary();
    patchMessage();
    cleanMixedText();
  }

  const oldRenderAll=window.renderAll;
  if(typeof oldRenderAll==='function' && !oldRenderAll.__v20){
    window.renderAll=function(){ const r=oldRenderAll.apply(this,arguments); setTimeout(applyAfterRender,0); setTimeout(applyAfterRender,100); return r; };
    window.renderAll.__v20=true;
  }

  document.addEventListener('click',e=>{
    const btn=e.target.closest && e.target.closest('#langToggle');
    if(btn){ e.preventDefault(); setLang(lang()==='th'?'en':'th'); }
  },true);
  ['change','input'].forEach(ev=>document.addEventListener(ev,e=>{
    if(e.target && ['availabilityFilter','dateInput','timeInput','inspectDateInput','inspectTimeInput'].includes(e.target.id)){
      setTimeout(applyAfterRender,120);
      setTimeout(applyAfterRender,500);
    }
  },true));

  new MutationObserver(()=>{ clearTimeout(window.__v20i18n); window.__v20i18n=setTimeout(applyAfterRender,50); }).observe(document.body,{childList:true,subtree:true});
  setLang('th');
  setInterval(applyAfterRender,1000);
})();




/* v21 final guard: remove all Thai text in English mode */
(function(){
  const TH_RE = /[\u0E00-\u0E7F]/;
  const thaiToEnglish = [
    ['เชื่อม CSV จริงแล้ว','Connected to live CSV'],
    ['อัปเดตล่าสุด','Last updated'],
    ['ตามเวลาปัจจุบัน','At current time'],
    ['รวมทุก service','All services'],
    ['เลือกcategoryด้านซ้ายเพื่อดูรายละเอียด','Select a category on the left to view details'],
    ['categoryที่ถูกจอง','Booked categories'],
    ['devicesทั้งหมด','Total devices'],
    ['เปิดให้บริการวันนี้','Open today'],
    ['ปิดให้บริการวันนี้','Closed today'],
    ['สถานะศูนย์','Center status'],
    ['เปิด','Open'],
    ['ปิด','Closed'],
    ['วันที่','Date'],
    ['ศูนย์เปิดให้บริการ','center is open'],
    ['ศูนย์ปิดให้บริการ','center is closed'],
    ['ช่วงที่เปิด','Open periods'],
    ['Maintenance ช่วงเช้า','Morning maintenance'],
    ['Maintenance ช่วงบ่าย','Afternoon maintenance'],
    ['ตารางอัตโนมัติประจำสัปดาห์','Weekly auto schedule'],
    ['วันหยุดหรือช่วง Maintenance ตามตารางอัตโนมัติ','Holiday or maintenance according to the auto schedule'],
    ['ทุกช่วงเวลาจะแสดงเป็นสีเทา และไม่ถือว่าเป็นการจอง','All time slots are gray and are not counted as bookings'],
    ['หมวดอุปกรณ์','Device categories'],
    ['กด All เพื่อดูทุก booking ที่ทำให้เลข Booking วันนี้ขึ้น','Use All to see every booking counted today'],
    ['ทั้งหมด','All'],
    ['ว่างตอนนี้','Available now'],
    ['ว่าง / จองได้','Available / Bookable'],
    ['ถูกจองแล้ว','Booked'],
    ['จองไม่ได้','Not bookable'],
    ['ผ่านเวลา / ปิด / Maintenance','Past / Closed / Maintenance'],
    ['ผ่านเวลา / ปิดบริการ','Past / Closed'],
    ['สีเขียว','Green'],
    ['สีแดง','Red'],
    ['สีม่วง','Purple'],
    ['สีเทา','Gray'],
    ['Booking วันนี้','Bookings today'],
    ['วันนี้มี Booking','Bookings today'],
    ['รายการจองวันนี้','Today’s bookings'],
    ['วันนี้ไม่มี Booking ใน Category นี้','No bookings today in this category'],
    ['ในCategoryนี้','in this category'],
    ['Category','Category'],
    ['อุปกรณ์ในหมวดนี้','Devices in this category'],
    ['แสดงสถานะปัจจุบันของแต่ละอุปกรณ์','Current status for each device'],
    ['ตรวจสอบช่วงเวลาที่ต้องการ','Check a specific time'],
    ['เลือกวันและเวลาเพื่อดูว่าอุปกรณ์ในหมวดนี้ว่างกี่เครื่อง','Choose a date and time to see how many devices are available'],
    ['ตรวจสอบ','Check'],
    ['ยังไม่ได้ตรวจสอบ','Not checked yet'],
    ['เครื่องในหมวด','Devices in category'],
    ['กำลังถูกจองตอนนี้','Currently booked'],
    ['คิวถัดไป','Next booking'],
    ['ยังไม่มี','None'],
    ['รายการ','records'],
    ['ตารางdevicesรายตัว','Device table'],
    ['ตารางเครื่องรายตัว','Device table'],
    ['สรุปสถานะตามเวลา','Time-slot status summary'],
    ['สรุปเป็นSlotเวลา','Summary by time slot'],
    ['หมายถึงSlotนั้นมี booking อย่างน้อย','means that slot has at least one booking'],
    ['ปิดให้บริการ','Closed'],
    ['ปิด / Maintenance','Closed / Maintenance'],
    ['ผ่านไปแล้ว','Past'],
    ['ไม่ถูกจอง','not booked'],
    ['เครื่อง','devices'],
    ['หมวด','category'],
    ['จอง','Booked'],
    ['ว่าง','Available'],
    ['วันนี้','today'],
    ['เวลา','time'],
    ['ช่วง','period'],
    ['รายตัว','table'],
    ['สถานะ','status']
  ];

  function isEnglish(){
    return (window.psuLang || document.body.getAttribute('data-lang')) === 'en';
  }

  function cleanThaiString(input, context){
    let s = String(input ?? '');
    if(!TH_RE.test(s)) return s;

    for(const [th,en] of thaiToEnglish){
      s = s.split(th).join(en);
    }

    // Fix common mixed outputs from previous layers.
    s = s
      .replace(/recordsBookedtoday/g, "Today's bookings")
      .replace(/recordsBooked/g, "Booked records")
      .replace(/Bookedวันนี้/g, 'Booked today')
      .replace(/todayมี Booked/g, 'Bookings today')
      .replace(/Date\s+/g, 'Date ')
      .replace(/categoryที่ถูกBooked/g, 'Booked categories')
      .replace(/devicesทั้งหมด/g, 'Total devices')
      .replace(/เลือกcategory/g, 'Select category')
      .replace(/ตารางdevices/g, 'Device table')
      .replace(/devicesรายตัว/g, 'Device table')
      .replace(/None Booking/g, 'No booking')
      .replace(/Booking ใน/g, 'Booking in')
      .replace(/สี/g, '')
      .replace(/\s+/g, ' ')
      .trim();

    if(TH_RE.test(s)){
      // Last-resort guard: remove Thai Unicode so English mode never shows Thai glyphs.
      s = s.replace(/[\u0E00-\u0E7F]+/g, '').replace(/\s+/g, ' ').trim();
    }

    if(!s || TH_RE.test(s)){
      const cls = context?.className || '';
      const tag = context?.tagName || '';
      if(String(cls).includes('badge')) return 'Status';
      if(/^H[1-6]$/.test(tag)) return 'Details';
      return 'Details';
    }
    return s;
  }

  function sanitizeEnglish(root=document.body){
    if(!isEnglish()) return;

    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node){
        const val = node.nodeValue || '';
        if(!val.trim() || !TH_RE.test(val)) return NodeFilter.FILTER_REJECT;
        const parent = node.parentElement;
        if(!parent || ['SCRIPT','STYLE','INPUT','TEXTAREA'].includes(parent.tagName)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    const nodes = [];
    while(walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node=>{
      node.nodeValue = cleanThaiString(node.nodeValue, node.parentElement);
    });

    document.querySelectorAll('option').forEach(opt=>{
      opt.textContent = cleanThaiString(opt.textContent, opt);
    });
    document.querySelectorAll('[placeholder],[title],[aria-label]').forEach(el=>{
      ['placeholder','title','aria-label'].forEach(attr=>{
        const v = el.getAttribute(attr);
        if(v && TH_RE.test(v)) el.setAttribute(attr, cleanThaiString(v, el));
      });
    });

    // Rebuild obvious blocks that still came out mixed.
    document.querySelectorAll('.panel h2, .panel h3').forEach(h=>{
      const txt = h.textContent || '';
      if(TH_RE.test(txt) || /recordsBooked|devicesราย|ตาราง|สรุป/.test(txt)){
        const lower = txt.toLowerCase();
        if(lower.includes('record') || lower.includes('booking')) h.textContent = "Today's bookings";
        else if(lower.includes('slot') || txt.includes('สรุป')) h.textContent = 'Time-slot status summary';
        else if(lower.includes('device') || txt.includes('ตาราง')) h.textContent = 'Device table 09:00–16:00';
        else h.textContent = cleanThaiString(txt, h);
      }
    });

    const btn = document.getElementById('langToggle');
    if(btn) btn.innerHTML = '<span class="lang-current">English</span><span class="lang-next">TH</span>';
  }

  function scanThaiCount(){
    const results = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode(node){
        const parent = node.parentElement;
        if(!parent || ['SCRIPT','STYLE'].includes(parent.tagName)) return NodeFilter.FILTER_REJECT;
        return TH_RE.test(node.nodeValue || '') ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    while(walker.nextNode()) results.push(walker.currentNode.nodeValue.trim());
    return results.filter(Boolean);
  }

  window.psuSanitizeEnglish = sanitizeEnglish;
  window.psuThaiTextLeftInEnglish = scanThaiCount;

  // Wrap renderAll again to sanitize after every render.
  const oldRenderAll = window.renderAll;
  if(typeof oldRenderAll === 'function' && !oldRenderAll.__v21Sanitized){
    window.renderAll = function(){
      const r = oldRenderAll.apply(this, arguments);
      setTimeout(sanitizeEnglish, 0);
      setTimeout(sanitizeEnglish, 100);
      setTimeout(sanitizeEnglish, 350);
      return r;
    };
    window.renderAll.__v21Sanitized = true;
  }

  document.addEventListener('click', e=>{
    if(e.target && (e.target.id === 'langToggle' || e.target.closest?.('#langToggle'))){
      setTimeout(sanitizeEnglish, 80);
      setTimeout(sanitizeEnglish, 240);
      setTimeout(sanitizeEnglish, 700);
    }
  }, true);

  document.addEventListener('change', e=>{
    if(e.target && ['availabilityFilter','dateInput','timeInput','inspectDateInput','inspectTimeInput'].includes(e.target.id)){
      setTimeout(sanitizeEnglish, 120);
      setTimeout(sanitizeEnglish, 500);
    }
  }, true);

  new MutationObserver(()=>{
    if(isEnglish()){
      clearTimeout(window.__v21NoThaiTimer);
      window.__v21NoThaiTimer = setTimeout(sanitizeEnglish, 40);
    }
  }).observe(document.body, {childList:true, subtree:true, characterData:true, attributes:true});

  setInterval(sanitizeEnglish, 500);
  setTimeout(sanitizeEnglish, 100);
  setTimeout(sanitizeEnglish, 1000);
})();

