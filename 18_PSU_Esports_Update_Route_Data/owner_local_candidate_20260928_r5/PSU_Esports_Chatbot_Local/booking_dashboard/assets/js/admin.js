/* Admin calendar logic - separated in v16 */
const $=id=>document.getElementById(id);let schedule={default_open:false,default_hours:{start:'09:00',end:'16:00'},dates:{}};
function today(){const d=new Date();return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`}
function esc(s){return String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]))}
function msg(html,err=false){$('message').className='msg'+(err?' err':'');$('message').innerHTML=html}
function fillForm(date){$('date').value=date;const cfg=schedule.dates?.[date]||{};$('open').value=String(cfg.open ?? schedule.default_open ?? false);$('start').value=cfg.hours?.start || schedule.default_hours?.start || '09:00';$('end').value=cfg.hours?.end || schedule.default_hours?.end || '16:00';$('reason').value=cfg.reason||''}
function renderDates(){const entries=Object.entries(schedule.dates||{}).sort(([a],[b])=>a.localeCompare(b));$('dates').innerHTML=entries.length?entries.map(([d,c])=>`<div class="date-item"><div><b>${esc(d)}</b><small>${c.open?'เปิด':'ปิด'} ${esc(c.hours?.start||'09:00')}–${esc(c.hours?.end||'16:00')} ${c.reason?'• '+esc(c.reason):''}</small></div><div class="row" style="flex:0 0 auto"><span class="badge ${c.open?'ok':'past'}">${c.open?'OPEN':'CLOSED'}</span><button class="btn" type="button" data-edit="${esc(d)}">แก้</button></div></div>`).join(''):'<div class="msg">ยังไม่มีวันที่ตั้งค่าเฉพาะ ระบบจะใช้ตารางอัตโนมัติประจำสัปดาห์</div>';document.querySelectorAll('[data-edit]').forEach(b=>b.addEventListener('click',()=>fillForm(b.dataset.edit)))}
async function load(){try{const r=await fetch('/api/center-schedule?_='+Date.now(),{cache:'no-store'});const j=await r.json();if(!j.ok)throw new Error(j.error||'โหลดไม่สำเร็จ');schedule=j.schedule||schedule;fillForm($('date').value||today());renderDates();msg('โหลดปฏิทินสำเร็จแล้ว');}catch(e){msg('โหลดข้อมูลไม่สำเร็จ: '+esc(e.message),true)}}
async function save(){try{const d=$('date').value;if(!d)throw new Error('กรุณาเลือกวันที่');schedule.dates=schedule.dates||{};schedule.dates[d]={open:$('open').value==='true',hours:{start:$('start').value||'09:00',end:$('end').value||'16:00'},reason:$('reason').value.trim()};const r=await fetch('/api/center-schedule',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({pin:$('pin').value,schedule})});const j=await r.json();if(!j.ok)throw new Error(j.error||'บันทึกไม่สำเร็จ');schedule=j.schedule;renderDates();msg('บันทึกเรียบร้อยแล้ว หน้า User จะอัปเดตในการ refresh รอบถัดไป');}catch(e){msg('บันทึกไม่สำเร็จ: '+esc(e.message),true)}}
async function clearDay(){try{const d=$('date').value;if(!d)throw new Error('กรุณาเลือกวันที่');delete schedule.dates[d];const r=await fetch('/api/center-schedule',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({pin:$('pin').value,schedule})});const j=await r.json();if(!j.ok)throw new Error(j.error||'บันทึกไม่สำเร็จ');schedule=j.schedule;fillForm(d);renderDates();msg('ลบ override ของวันนี้แล้ว');}catch(e){msg('ลบไม่สำเร็จ: '+esc(e.message),true)}}
$('dayForm').addEventListener('submit',e=>{e.preventDefault();save()});$('clearDay').addEventListener('click',clearDay);$('refreshBtn').addEventListener('click',load);$('date').addEventListener('change',e=>fillForm(e.target.value));$('date').value=today();load();


/* v20 clean bilingual admin layer */
(function(){
  const D={
    th:{current:'ไทย',next:'EN',title:'Admin Calendar v26',sub:'ตั้งค่าวันพิเศษสำหรับเปิด/ปิด PSU eSports โดยค่า default ใช้ตารางอัตโนมัติประจำสัปดาห์',back:'กลับหน้า User',reload:'โหลดข้อมูลใหม่',form:'ตั้งค่ารายวัน',pin:'Admin PIN',date:'วันที่',status:'สถานะศูนย์',open:'เปิดให้บริการ',closed:'ปิดให้บริการทั้งวัน',start:'เวลาเริ่ม',end:'เวลาปิด',reason:'เหตุผล/หมายเหตุ',save:'บันทึก',clear:'ลบ override วันนี้',saved:'วันที่ที่ตั้งค่าไว้',hint:'ถ้าไม่ได้ตั้งค่าวันพิเศษ ระบบจะใช้ weekly auto schedule',none:'ยังไม่มีวันที่ตั้งค่าเฉพาะ ระบบจะใช้ตารางอัตโนมัติประจำสัปดาห์',edit:'แก้'},
    en:{current:'English',next:'TH',title:'Admin Calendar v26',sub:'Set special open/closed dates for PSU eSports. By default, the weekly auto schedule is used.',back:'Back to User page',reload:'Reload data',form:'Daily override',pin:'Admin PIN',date:'Date',status:'Center status',open:'Open',closed:'Closed all day',start:'Start time',end:'End time',reason:'Reason / note',save:'Save',clear:'Clear today override',saved:'Saved override dates',hint:'If no special date is set, the weekly auto schedule will be used.',none:'No date overrides. The weekly auto schedule will be used.',edit:'Edit'}
  };
  function lang(){return window.psuAdminLang||document.body.getAttribute('data-lang')||'th'}
  function t(k){return (D[lang()]&&D[lang()][k])||D.th[k]||k}
  function setLang(v){window.psuAdminLang=v==='en'?'en':'th';document.body.setAttribute('data-lang',window.psuAdminLang);apply();try{if(typeof renderDates==='function')renderDates()}catch(_){}setTimeout(apply,80)}
  function txt(sel,val){const el=document.querySelector(sel);if(el)el.textContent=val}
  function apply(){
    document.title=t('title')+' - PSU Esports';
    txt('h1',t('title')); const p=document.querySelector('.hero p'); if(p)p.textContent=t('sub');
    const b=document.getElementById('langToggle'); if(b)b.innerHTML=`<span class="lang-current">${t('current')}</span><span class="lang-next">${t('next')}</span>`;
    document.querySelectorAll('.hero .btn').forEach(btn=>{const s=btn.textContent;if(/กลับ|Back/.test(s))btn.textContent=t('back');if(/โหลด|Reload/.test(s))btn.textContent=t('reload')});
    const h=document.querySelectorAll('.card h2'); if(h[0])h[0].textContent=t('form'); if(h[1])h[1].textContent=t('saved');
    const labels=document.querySelectorAll('.label b'); [t('pin'),t('date'),t('status'),t('start'),t('end'),t('reason')].forEach((v,i)=>{if(labels[i])labels[i].textContent=v});
    const op=document.querySelector('#open option[value="true"]'); if(op)op.textContent=t('open');
    const cl=document.querySelector('#open option[value="false"]'); if(cl)cl.textContent=t('closed');
    const reason=document.getElementById('reason'); if(reason)reason.placeholder=t('reason');
    const save=document.querySelector('#dayForm button.primary'); if(save)save.textContent=t('save');
    const clear=document.getElementById('clearDay'); if(clear)clear.textContent=t('clear');
    const hint=document.querySelector('.hint'); if(hint)hint.textContent=t('hint');
    document.querySelectorAll('[data-edit], .date-item button').forEach(x=>{if(/แก้|Edit/.test(x.textContent))x.textContent=t('edit')});
    document.querySelectorAll('.msg').forEach(x=>{if(x.textContent.includes('ยังไม่มี')||x.textContent.includes('No date'))x.textContent=t('none')});
  }
  document.addEventListener('click',e=>{const b=e.target.closest&&e.target.closest('#langToggle');if(b){e.preventDefault();setLang(lang()==='th'?'en':'th')}},true);
  new MutationObserver(()=>{clearTimeout(window.__v20admin);window.__v20admin=setTimeout(apply,60)}).observe(document.body,{childList:true,subtree:true});
  setLang('th'); setInterval(apply,1000);
})();




/* v21 final guard: remove all Thai text in English admin mode */
(function(){
  const TH_RE=/[\u0E00-\u0E7F]/;
  const MAP=[
    ['ตั้งค่าวันพิเศษสำหรับเปิด/ปิด PSU eSports โดยค่า default ใช้ตารางอัตโนมัติประจำสัปดาห์','Set special open/closed dates for PSU eSports. By default, the weekly auto schedule is used.'],
    ['กลับหน้า User','Back to User page'],['โหลดข้อมูลใหม่','Reload data'],['ตั้งค่ารายวัน','Daily override'],
    ['วันที่ที่ตั้งค่าไว้','Saved override dates'],['วันที่','Date'],['สถานะศูนย์','Center status'],
    ['เปิดให้บริการ','Open'],['ปิดให้บริการทั้งวัน','Closed all day'],['เวลาเริ่ม','Start time'],['เวลาปิด','End time'],
    ['เหตุผล/หมายเหตุ','Reason / note'],['บันทึก','Save'],['ลบ override วันนี้','Clear today override'],
    ['ถ้าไม่ได้ตั้งค่าวันพิเศษ ระบบจะใช้ weekly auto schedule','If no special date is set, the weekly auto schedule will be used.'],
    ['ยังไม่มีวันที่ตั้งค่าเฉพาะ ระบบจะใช้ตารางอัตโนมัติประจำสัปดาห์','No date overrides. The weekly auto schedule will be used.'],
    ['แก้','Edit'],['เปิด','Open'],['ปิด','Closed']
  ];
  function en(){return (window.psuAdminLang||document.body.getAttribute('data-lang'))==='en'}
  function clean(s){
    s=String(s??'');
    if(!en()||!TH_RE.test(s)) return s;
    for(const [a,b] of MAP) s=s.split(a).join(b);
    if(TH_RE.test(s)) s=s.replace(/[\u0E00-\u0E7F]+/g,'').replace(/\s+/g,' ').trim();
    return s||'Details';
  }
  function run(){
    if(!en()) return;
    const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,{acceptNode(n){
      const p=n.parentElement;if(!p||['SCRIPT','STYLE','INPUT','TEXTAREA'].includes(p.tagName)||!TH_RE.test(n.nodeValue||''))return NodeFilter.FILTER_REJECT;return NodeFilter.FILTER_ACCEPT;
    }});
    const ns=[];while(w.nextNode())ns.push(w.currentNode);ns.forEach(n=>n.nodeValue=clean(n.nodeValue));
    document.querySelectorAll('option').forEach(o=>o.textContent=clean(o.textContent));
    const b=document.getElementById('langToggle'); if(b)b.innerHTML='<span class="lang-current">English</span><span class="lang-next">TH</span>';
  }
  window.psuAdminSanitizeEnglish=run;
  new MutationObserver(()=>{if(en()){clearTimeout(window.__v21AdminNoThai);window.__v21AdminNoThai=setTimeout(run,40)}}).observe(document.body,{childList:true,subtree:true,characterData:true});
  document.addEventListener('click',e=>{if(e.target&&(e.target.id==='langToggle'||e.target.closest?.('#langToggle')))setTimeout(run,80)},true);
  setInterval(run,500);
})();




/* v22 robust Admin Edit button + language fix */
(function(){
  const TH = {
    current:'ไทย', next:'EN',
    title:'Admin Calendar v26',
    sub:'ตั้งค่าวันพิเศษสำหรับเปิด/ปิด PSU eSports โดยค่า default ใช้ตารางอัตโนมัติประจำสัปดาห์',
    back:'กลับหน้า User', reload:'โหลดข้อมูลใหม่',
    form:'ตั้งค่ารายวัน', saved:'วันที่ที่ตั้งค่าไว้',
    pin:'Admin PIN', date:'วันที่', status:'สถานะศูนย์', open:'เปิดให้บริการ', closed:'ปิดให้บริการทั้งวัน',
    start:'เวลาเริ่ม', end:'เวลาปิด', reason:'เหตุผล/หมายเหตุ',
    save:'บันทึก', clear:'ลบ override วันนี้', edit:'แก้',
    loaded:'โหลดปฏิทินสำเร็จแล้ว',
    editLoaded:'โหลดวันที่นี้มาแก้ไขแล้ว',
    noDates:'ยังไม่มีวันที่ตั้งค่าเฉพาะ ระบบจะใช้ตารางอัตโนมัติประจำสัปดาห์',
    hint:'ถ้าไม่ได้ตั้งค่าวันพิเศษ ระบบจะใช้ weekly auto schedule',
    savedMsg:'บันทึกเรียบร้อยแล้ว หน้า User จะอัปเดตในการ refresh รอบถัดไป',
    deleted:'ลบ override ของวันนี้แล้ว'
  };
  const EN = {
    current:'English', next:'TH',
    title:'Admin Calendar v26',
    sub:'Set special open/closed dates for PSU eSports. By default, the weekly auto schedule is used.',
    back:'Back to User page', reload:'Reload data',
    form:'Daily override', saved:'Saved override dates',
    pin:'Admin PIN', date:'Date', status:'Center status', open:'Open', closed:'Closed all day',
    start:'Start time', end:'End time', reason:'Reason / note',
    save:'Save', clear:'Clear today override', edit:'Edit',
    loaded:'Calendar loaded successfully',
    editLoaded:'Loaded this date into the form',
    noDates:'No date overrides. The weekly auto schedule will be used.',
    hint:'If no special date is set, the weekly auto schedule will be used.',
    savedMsg:'Saved. The User page will update on the next refresh.',
    deleted:'Today override has been removed'
  };
  function lang(){ return window.psuAdminLang || document.body.getAttribute('data-lang') || 'th'; }
  function dict(){ return lang()==='en' ? EN : TH; }
  function t(k){ return dict()[k] || TH[k] || k; }
  function $(id){ return document.getElementById(id); }

  function translateAdmin(){
    const d = dict();
    document.title = d.title + ' - PSU Esports';
    const h1 = document.querySelector('h1'); if(h1) h1.textContent = d.title;
    const heroP = document.querySelector('.hero p'); if(heroP) heroP.textContent = d.sub;

    const langBtn = $('langToggle');
    if(langBtn) langBtn.innerHTML = `<span class="lang-current">${d.current}</span><span class="lang-next">${d.next}</span>`;

    document.querySelectorAll('.hero .btn').forEach(btn=>{
      const text = btn.textContent.trim();
      if(/กลับ|Back/.test(text)) btn.textContent = d.back;
      if(/โหลด|Reload/.test(text)) btn.textContent = d.reload;
    });

    const h2s = document.querySelectorAll('.card h2');
    if(h2s[0]) h2s[0].textContent = d.form;
    if(h2s[1]) h2s[1].textContent = d.saved;

    const labels = document.querySelectorAll('.label b');
    [d.pin,d.date,d.status,d.start,d.end,d.reason].forEach((v,i)=>{ if(labels[i]) labels[i].textContent = v; });

    const op = document.querySelector('#open option[value="true"]'); if(op) op.textContent = d.open;
    const cl = document.querySelector('#open option[value="false"]'); if(cl) cl.textContent = d.closed;
    const reason = $('reason'); if(reason) reason.placeholder = d.reason;
    const saveBtn = document.querySelector('#dayForm button.primary'); if(saveBtn) saveBtn.textContent = d.save;
    const clearBtn = $('clearDay'); if(clearBtn) clearBtn.textContent = d.clear;
    const hint = document.querySelector('.hint'); if(hint) hint.textContent = d.hint;

    document.querySelectorAll('[data-edit]').forEach(btn=>btn.textContent = d.edit);
    document.querySelectorAll('.msg').forEach(m=>{
      const raw = m.textContent.trim();
      if(/โหลดปฏิทินสำเร็จ|Calendar loaded/.test(raw)) m.textContent = d.loaded;
      if(/ลบ override|removed/.test(raw)) m.textContent = d.deleted;
      if(/ยังไม่มีวันที่|No date overrides/.test(raw)) m.textContent = d.noDates;
    });
  }

  function setAdminLang(next){
    window.psuAdminLang = next === 'en' ? 'en' : 'th';
    document.body.setAttribute('data-lang', window.psuAdminLang);
    translateAdmin();
    setTimeout(translateAdmin, 80);
    setTimeout(translateAdmin, 300);
  }

  function getSchedule(){
    try{
      if(typeof schedule !== 'undefined') return schedule;
    }catch(_){}
    return window.schedule || null;
  }

  function safeFillForm(date){
    if(!date) return;
    const dateInput = $('date');
    if(dateInput) dateInput.value = date;

    // Prefer original fillForm if available.
    try{
      if(typeof fillForm === 'function'){
        fillForm(date);
      }else{
        const sc = getSchedule() || {default_open:true,default_hours:{start:'09:00',end:'16:00'},dates:{}};
        const cfg = (sc.dates && sc.dates[date]) || {};
        if($('open')) $('open').value = String(cfg.open ?? sc.default_open ?? true);
        if($('start')) $('start').value = (cfg.hours && cfg.hours.start) || (sc.default_hours && sc.default_hours.start) || '09:00';
        if($('end')) $('end').value = (cfg.hours && cfg.hours.end) || (sc.default_hours && sc.default_hours.end) || '16:00';
        if($('reason')) $('reason').value = cfg.reason || '';
      }
    }catch(err){
      console.error('fillForm failed:', err);
    }

    // Visual feedback
    document.querySelectorAll('.date-item').forEach(item=>{
      const btn = item.querySelector('[data-edit]');
      item.classList.toggle('editing', !!btn && btn.getAttribute('data-edit') === date);
    });

    const msgBox = $('message');
    if(msgBox){
      msgBox.className = 'msg';
      msgBox.textContent = t('editLoaded') + ': ' + date;
    }
    translateAdmin();
  }

  // Important fix: use event delegation so Edit continues to work even after render/translation.
  document.addEventListener('click', function(e){
    const editBtn = e.target.closest && e.target.closest('[data-edit]');
    if(editBtn){
      e.preventDefault();
      e.stopPropagation();
      safeFillForm(editBtn.getAttribute('data-edit'));
      return;
    }

    const langBtn = e.target.closest && e.target.closest('#langToggle');
    if(langBtn){
      e.preventDefault();
      setAdminLang(lang()==='th' ? 'en' : 'th');
      return;
    }
  }, true);

  const dateInput = $('date');
  if(dateInput && !dateInput.__v22ChangeBound){
    dateInput.__v22ChangeBound = true;
    dateInput.addEventListener('change', function(){
      safeFillForm(this.value);
    });
  }

  // Wrap renderDates so translated buttons still keep edit behavior.
  if(typeof renderDates === 'function' && !renderDates.__v22Wrapped){
    const oldRenderDates = renderDates;
    window.renderDates = function(){
      const result = oldRenderDates.apply(this, arguments);
      setTimeout(translateAdmin, 0);
      setTimeout(translateAdmin, 120);
      return result;
    };
    window.renderDates.__v22Wrapped = true;
  }

  window.psuAdminEditDate = safeFillForm;
  window.psuAdminSetLang = setAdminLang;

  setTimeout(translateAdmin, 0);
  setTimeout(translateAdmin, 300);
  setInterval(translateAdmin, 1200);
})();

