/* ===================== JOB INTERVIEW COURSE ENGINE ===================== */
/* ---- LEVEL SWITCH (Support / Standard / Challenge) ---- */
var LV_KEY = 'jic::level';
function setLevel(l){
  document.body.classList.remove('lv-support','lv-standard','lv-challenge');
  document.body.classList.add('lv-'+l);
  try{ localStorage.setItem(LV_KEY, l); }catch(e){}
  document.querySelectorAll('[data-lv]').forEach(function(b){ b.classList.toggle('on', b.dataset.lv === l); });
}
(function(){ var l='standard'; try{ l = localStorage.getItem(LV_KEY) || 'standard'; }catch(e){} setLevel(l); })();

/* ---- FLAG SORT: each card gets one of two answers ---- */
function fsPick(btn, key){
  var card = btn.closest('.fs-card');
  card.dataset.pick = key;
  card.classList.remove('ok','bad','empty-warn');
  card.querySelectorAll('.fs-btn').forEach(function(b){ b.classList.toggle('sel', b === btn); });
}
function fsCheck(id){
  document.querySelectorAll('#'+id+' .fs-card').forEach(function(c){
    c.classList.remove('ok','bad','empty-warn');
    if (!c.dataset.pick){ c.classList.add('empty-warn'); return; }
    c.classList.add(c.dataset.pick === c.dataset.ans ? 'ok' : 'bad');
  });
}
function fsReset(id){
  document.querySelectorAll('#'+id+' .fs-card').forEach(function(c){
    c.classList.remove('ok','bad','empty-warn'); delete c.dataset.pick;
    c.querySelectorAll('.fs-btn').forEach(function(b){ b.classList.remove('sel'); });
  });
}

/* ---- MULTI PICK: tick every option that fits ---- */
function mpToggle(el){ el.classList.remove('ok','bad'); el.classList.toggle('picked'); }
function mpCheck(id){
  document.querySelectorAll('#'+id+' .mp-opt').forEach(function(o){
    o.classList.remove('ok','bad');
    if (o.classList.contains('picked')) o.classList.add(o.dataset.correct === '1' ? 'ok' : 'bad');
  });
}
function mpReset(id){ document.querySelectorAll('#'+id+' .mp-opt').forEach(function(o){ o.classList.remove('picked','ok','bad'); }); }

/* ---- ORDER CHIPS: click to place into the next empty slot ---- */
function ogClick(chip){
  var og = chip.closest('.og');
  var inSlot = chip.parentNode.classList.contains('og-slot');
  og.classList.remove('checked');
  chip.classList.remove('ok','bad');
  if (inSlot){ chip.parentNode.classList.remove('filled'); og.querySelector('.og-pool').appendChild(chip); return; }
  var slots = og.querySelectorAll('.og-slot');
  for (var i=0;i<slots.length;i++){
    if (!slots[i].querySelector('.og-chip')){ slots[i].appendChild(chip); slots[i].classList.add('filled'); return; }
  }
}
function ogCheck(id){
  document.querySelectorAll('#'+id+' .og-slot').forEach(function(s, i){
    var c = s.querySelector('.og-chip'); if (!c) return;
    c.classList.remove('ok','bad');
    c.classList.add(parseInt(c.dataset.i,10) === i ? 'ok' : 'bad');
  });
}
function ogReset(id){
  var og = document.getElementById(id), pool = og.querySelector('.og-pool');
  og.querySelectorAll('.og-slot').forEach(function(s){
    var c = s.querySelector('.og-chip'); if (c){ c.classList.remove('ok','bad'); pool.appendChild(c); } s.classList.remove('filled');
  });
}

/* ---- BUCKETS: pick a chip, then pick the bucket ---- */
var bkSel = null;
function bkChip(chip){
  if (bkSel) bkSel.classList.remove('sel');
  chip.classList.remove('ok','bad');
  bkSel = chip; chip.classList.add('sel');
}
function bkPut(bucket){
  if (!bkSel) return;
  bucket.querySelector('.bk-drop').appendChild(bkSel);
  bkSel.classList.remove('sel','ok','bad'); bkSel = null;
}
function bkCheck(id){
  var box = document.getElementById(id);
  box.querySelectorAll('.bk-chip').forEach(function(c){
    c.classList.remove('ok','bad');
    var b = c.closest('.bk-b'); if (!b) return;
    c.classList.add(b.dataset.b === c.dataset.ans ? 'ok' : 'bad');
  });
}
function bkReset(id){
  var box = document.getElementById(id), pool = box.querySelector('.bk-pool');
  box.querySelectorAll('.bk-chip').forEach(function(c){ c.classList.remove('ok','bad','sel'); pool.appendChild(c); });
  bkSel = null;
}

/* ---- TIMER ---- */
var tmHandles = {};
function tmBeep(){ try{ var C = new (window.AudioContext||window.webkitAudioContext)(); var o=C.createOscillator(), g=C.createGain(); o.connect(g); g.connect(C.destination); o.frequency.value=880; g.gain.value=.15; o.start(); setTimeout(function(){ o.stop(); C.close(); }, 450); }catch(e){} }
function tmStart(btn){
  var box = btn.closest('.tm'), d = box.querySelector('.tm-d'), id = box.id;
  if (tmHandles[id]){ clearInterval(tmHandles[id]); tmHandles[id]=null; btn.textContent='▶ Start'; return; }
  var left = parseInt(box.dataset.left || box.dataset.sec, 10);
  if (left <= 0) left = parseInt(box.dataset.sec,10);
  btn.textContent = '⏸ Pause'; box.classList.remove('done');
  tmHandles[id] = setInterval(function(){
    left--; box.dataset.left = left; d.textContent = left;
    if (left <= 0){ clearInterval(tmHandles[id]); tmHandles[id]=null; btn.textContent='▶ Start again'; d.textContent="Time's up!"; box.classList.add('done'); tmBeep(); }
  }, 1000);
}
function tmReset(btn){
  var box = btn.closest('.tm'); clearInterval(tmHandles[box.id]); tmHandles[box.id]=null;
  box.dataset.left = box.dataset.sec; box.querySelector('.tm-d').textContent = box.dataset.sec; box.classList.remove('done');
  box.querySelector('.tm-go').textContent = '▶ Start';
}

/* ---- ROULETTE ---- */
var RL = {};
function rlNext(id){
  var list = RL[id], box = document.getElementById(id);
  var n = nextNoRepeat('rl-'+id, list.length);
  box.querySelector('.rl-q').textContent = list[n][0];
  var f = box.querySelector('.rl-f'); if (f){ f.textContent = list[n][1] || ''; if (list[n][2]){ var x=document.createElement('div'); x.className='rl-ex'; x.textContent='💡 Example: '+list[n][2]; f.appendChild(x); } }
  box.classList.add('spun');
}

/* ---- BRANCHING SCENARIO ---- */
function brPick(btn){
  var br = btn.closest('.br');
  br.querySelectorAll('.br-opt').forEach(function(b){ b.classList.remove('sel'); });
  btn.classList.add('sel');
  var fb = br.querySelector('.br-fb');
  fb.className = 'br-fb show ' + btn.dataset.rate;
  fb.innerHTML = btn.dataset.fb;
}

/* ---- ANSWER BUILDER + INTERVIEW NOTEBOOK ---- */
var AB_KEY = 'jic::ans';
function abLoad(){ try{ return JSON.parse(localStorage.getItem(AB_KEY)) || {}; }catch(e){ return {}; } }
function abSave(o){ try{ localStorage.setItem(AB_KEY, JSON.stringify(o)); }catch(e){} }
function abStepsKey(ab){ return 'jic::in::' + ab.dataset.key; }
function abBuild(btn){
  var ab = btn.closest('.ab'), parts = [];
  ab.querySelectorAll('.ab-in').forEach(function(t){ var v = t.value.trim(); if (v) parts.push(v); });
  var out = ab.querySelector('.ab-out');
  if (!parts.length){ out.innerHTML = '<span class="ab-warn">Write at least one part first.</span>'; out.classList.add('show'); return; }
  var text = parts.join(' ');
  var all = abLoad(); all[ab.dataset.key] = {title: ab.dataset.title, text: text, lesson: document.body.dataset.lesson || '', order: ab.dataset.order || ab.dataset.key};
  abSave(all);
  out.innerHTML = '<b>Your answer</b><p>' + text.replace(/</g,'&lt;') + '</p><span class="ab-ok">✓ Saved to your Interview Notebook</span>';
  out.classList.add('show');
}
function abClear(btn){
  var ab = btn.closest('.ab');
  ab.querySelectorAll('.ab-in').forEach(function(t){ t.value=''; });
  try{ localStorage.removeItem(abStepsKey(ab)); }catch(e){}
  var all = abLoad(); delete all[ab.dataset.key]; abSave(all);
  var out = ab.querySelector('.ab-out'); out.classList.remove('show'); out.innerHTML='';
}
document.querySelectorAll('.ab').forEach(function(ab){
  var saved = null; try{ saved = JSON.parse(localStorage.getItem(abStepsKey(ab))); }catch(e){}
  ab.querySelectorAll('.ab-in').forEach(function(t, i){
    if (saved && saved[i]) t.value = saved[i];
    t.addEventListener('input', function(){
      var vals = []; ab.querySelectorAll('.ab-in').forEach(function(x){ vals.push(x.value); });
      try{ localStorage.setItem(abStepsKey(ab), JSON.stringify(vals)); }catch(e){}
    });
  });
});
function openNotebook(){
  var all = abLoad(), keys = Object.keys(all).sort(function(a,b){ return String(all[a].order).localeCompare(String(all[b].order)); });
  if (!keys.length){ alert('Your Interview Notebook is empty. Build an answer in a lesson first!'); return; }
  var win = window.open('', '_blank'), cards = '';
  keys.forEach(function(k){ var a = all[k]; cards += '<div class="c"><div class="h">'+a.lesson+' · '+a.title+'</div><p>'+String(a.text).replace(/</g,'&lt;')+'</p></div>'; });
  var today = new Date().toLocaleDateString('en-US',{weekday:'long',year:'numeric',month:'long',day:'numeric'});
  win.document.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>My Interview Notebook</title><style>'+
    'body{font-family:"DM Sans","Segoe UI",sans-serif;max-width:800px;margin:0 auto;padding:0 0 30px;color:#1C2B3A}'+
    '.hero{background:linear-gradient(135deg,#12324A,#1B6E96);color:#fff;padding:32px 34px;border-radius:0 0 24px 24px}'+
    '.hero small{letter-spacing:.2em;text-transform:uppercase;color:#FFD84D;font-weight:800}.hero h1{margin:6px 0 4px;font-size:2.1rem}.hero p{margin:0;opacity:.9}'+
    '.tip{margin:22px 28px;background:#FFF8E1;border:3px solid #FFD84D;border-radius:18px;padding:14px 20px;font-size:1.02rem;line-height:1.6}'+
    '.c{margin:0 28px 16px;border:1px solid #D5DEE5;border-radius:12px;overflow:hidden;break-inside:avoid}.h{background:#12324A;color:#fff;padding:8px 14px;font-weight:700}'+
    '.c p{margin:0;padding:12px 16px;line-height:1.75;font-size:1.05rem}*{print-color-adjust:exact;-webkit-print-color-adjust:exact}</style></head><body>'+
    '<div class="hero"><small>Conversational English with teacher Nanda</small><h1>🎤 My Interview Notebook</h1><p>'+today+'</p></div>'+
    '<div class="tip"><b>How to use this page:</b> read each answer out loud. Then say it again without looking, in your own words. Practice a little every day!</div>'+cards+'</body></html>');
  win.document.close(); setTimeout(function(){ win.print(); }, 600);
}

/* ---- course map ---- */
function mapPick(btn){
  var box = btn.closest('.mapwrap');
  box.querySelectorAll('.maptile').forEach(function(b){ b.classList.remove('on'); });
  btn.classList.add('on');
  box.querySelector('.mapinfo').innerHTML = btn.dataset.info;
}
/* ---- tick list ---- */
function tickToggle(el){ el.classList.toggle('picked'); }

/* ===================== INTERVIEW SIMULATOR ===================== */
var SIM = {};
function simFace(p){ return p>=.75?'😀':p>=.5?'🙂':p>=.3?'😐':'😕'; }
function simInit(id){
  var box=document.getElementById(id); box.dataset.i=0; box.dataset.score=0;
  box.querySelector('.sim-log').innerHTML=''; box.querySelector('.sim-opts').innerHTML=''; box.querySelector('.sim-end').style.display='none';
  simMeter(id); simAsk(id);
}
function simMeter(id){
  var box=document.getElementById(id), d=SIM[id], max=d.turns.length*3, p=(parseInt(box.dataset.score,10))/max;
  box.querySelector('.sim-fill').style.width=Math.round(p*100)+'%'; box.querySelector('.sim-face').textContent=simFace(parseInt(box.dataset.i,10)===0?.5:p);
}
function simBubble(id, cls, html){
  var log=document.getElementById(id).querySelector('.sim-log'), b=document.createElement('div'); b.className='sim-b '+cls; b.innerHTML=html; log.appendChild(b); log.scrollTop=log.scrollHeight; return b;
}
function simAsk(id){
  var box=document.getElementById(id), d=SIM[id], i=parseInt(box.dataset.i,10);
  if (i>=d.turns.length){
    var p=parseInt(box.dataset.score,10)/(d.turns.length*3), v=d.verdicts[d.verdicts.length-1][1];
    for (var k=0;k<d.verdicts.length;k++){ if (p>=d.verdicts[k][0]){ v=d.verdicts[k][1]; break; } }
    var e=box.querySelector('.sim-end'); e.style.display='block'; e.querySelector('.sim-verdict').innerHTML=simFace(p)+' '+v; return;
  }
  var t=d.turns[i]; simBubble(id,'them','<b>'+d.who+':</b> '+t.q);
  var o=box.querySelector('.sim-opts'); o.innerHTML='';
  t.opts.forEach(function(op,k){ var b=document.createElement('button'); b.className='sim-opt'; b.innerHTML=op.t; b.onclick=function(){ simPick(id,k); }; o.appendChild(b); });
}
function simPick(id,k){
  var box=document.getElementById(id), d=SIM[id], i=parseInt(box.dataset.i,10), op=d.turns[i].opts[k];
  box.querySelector('.sim-opts').innerHTML='';
  simBubble(id,'me',op.t);
  box.dataset.score=parseInt(box.dataset.score,10)+op.s; box.dataset.i=i+1; simMeter(id);
  var r=op.s>=3?'good':op.s>=2?'ok':'bad';
  setTimeout(function(){ simBubble(id,'fb '+r, op.fb); setTimeout(function(){ simAsk(id); },900); },500);
}

/* ===================== RAPID FIRE ===================== */
var RF = {}, rfTimers = {};
function rfInit(id){ var b=document.getElementById(id); b.dataset.i=0; b.dataset.score=0; b.dataset.streak=0; b.dataset.best=0; b.querySelector('.rf-end').style.display='none'; b.querySelector('.rf-play').style.display='block'; rfShow(id); }
function rfShow(id){
  var box=document.getElementById(id), d=RF[id], i=parseInt(box.dataset.i,10);
  clearInterval(rfTimers[id]);
  if (i>=d.items.length){ box.querySelector('.rf-play').style.display='none'; var e=box.querySelector('.rf-end'); e.style.display='block'; var s=parseInt(box.dataset.score,10);
    e.querySelector('.rf-result').innerHTML='⭐ '+s+' / '+d.items.length+' &nbsp;·&nbsp; best streak: '+box.dataset.best+' 🔥'; return; }
  var it=d.items[i]; box.querySelector('.rf-n').textContent=(i+1)+' / '+d.items.length; box.querySelector('.rf-score').textContent='⭐ '+box.dataset.score+'  🔥 '+box.dataset.streak;
  box.querySelector('.rf-q').innerHTML=it.q;
  var o=box.querySelector('.rf-opts'); o.innerHTML='';
  it.o.forEach(function(t,k){ var b=document.createElement('button'); b.className='rf-opt'; b.innerHTML=t; b.onclick=function(){ rfPick(id,k,b); }; o.appendChild(b); });
}
function rfPick(id,k,btn){
  var box=document.getElementById(id), d=RF[id], i=parseInt(box.dataset.i,10); clearInterval(rfTimers[id]);
  box.querySelectorAll('.rf-opt').forEach(function(x){x.disabled=true;});
  if (k===d.items[i].a){ btn.classList.add('ok'); box.dataset.score=parseInt(box.dataset.score,10)+1; box.dataset.streak=parseInt(box.dataset.streak,10)+1; box.dataset.best=Math.max(parseInt(box.dataset.best,10),parseInt(box.dataset.streak,10)); }
  else { btn.classList.add('bad'); box.dataset.streak=0; }
  box.querySelector('.rf-score').textContent='⭐ '+box.dataset.score+'  🔥 '+box.dataset.streak;
  box.dataset.i=i+1; setTimeout(function(){ rfShow(id); },800);
}

/* ===================== MEMORY PAIRS ===================== */
var memLock = {};
function memFlip(card){
  var box=card.closest('.mem'), id=box.id;
  if (memLock[id] || card.classList.contains('open') || card.classList.contains('done')) return;
  card.classList.add('open');
  var open=box.querySelectorAll('.mem-c.open:not(.done)');
  if (open.length===2){
    box.dataset.moves=(parseInt(box.dataset.moves||0,10)+1); box.querySelector('.mem-moves').textContent='Moves: '+box.dataset.moves;
    if (open[0].dataset.p===open[1].dataset.p){ open.forEach(function(c){ c.classList.add('done'); }); 
      if (box.querySelectorAll('.mem-c.done').length===box.querySelectorAll('.mem-c').length) box.querySelector('.mem-win').style.display='block'; }
    else { memLock[id]=true; setTimeout(function(){ open.forEach(function(c){ c.classList.remove('open'); }); memLock[id]=false; },950); }
  }
}
function memReset(id){
  var box=document.getElementById(id), g=box.querySelector('.mem-grid'), cs=Array.prototype.slice.call(g.children);
  cs.sort(function(){ return Math.random()-.5; }).forEach(function(c){ c.classList.remove('open','done'); g.appendChild(c); });
  box.dataset.moves=0; box.querySelector('.mem-moves').textContent='Moves: 0'; box.querySelector('.mem-win').style.display='none';
}

/* ===================== WORD ORDER ===================== */
function woClick(t){
  var it=t.closest('.wo-item'), line=it.querySelector('.wo-line'), pool=it.querySelector('.wo-pool');
  line.classList.remove('ok','bad'); t.classList.remove('ok','bad');
  if (t.parentNode===pool) line.appendChild(t); else pool.appendChild(t);
}
function woCheck(id){
  document.querySelectorAll('#'+id+' .wo-item').forEach(function(it){
    var line=it.querySelector('.wo-line'); line.classList.remove('ok','bad');
    var w=[].map.call(line.querySelectorAll('.wo-t'),function(x){return x.textContent;}).join(' ');
    if (!w) return; line.classList.add(norm(w)===norm(it.dataset.ans)?'ok':'bad');
  });
}
function woReset(id){ document.querySelectorAll('#'+id+' .wo-item').forEach(function(it){ var p=it.querySelector('.wo-pool'); it.querySelectorAll('.wo-line .wo-t').forEach(function(t){ p.appendChild(t); }); it.querySelector('.wo-line').classList.remove('ok','bad'); }); }

/* ===================== ERROR HUNT ===================== */
function ehPick(w){
  var it=w.closest('.eh-item'); it.classList.remove('ok','bad','empty-warn');
  it.querySelectorAll('.eh-w').forEach(function(x){ x.classList.remove('sel'); }); w.classList.add('sel'); it.dataset.pick=w.dataset.i;
}
function ehCheck(id){
  document.querySelectorAll('#'+id+' .eh-item').forEach(function(it){
    it.classList.remove('ok','bad','empty-warn');
    var inp=it.querySelector('.eh-in'), v=norm(inp.value), alts=(inp.dataset.alt||'').split('|').map(norm).filter(Boolean);
    if (it.dataset.pick===undefined || !v){ it.classList.add('empty-warn'); return; }
    it.classList.add((it.dataset.pick===it.dataset.wrong && (v===norm(inp.dataset.ans)||alts.indexOf(v)>-1))?'ok':'bad');
  });
}
function ehReset(id){ document.querySelectorAll('#'+id+' .eh-item').forEach(function(it){ it.classList.remove('ok','bad','empty-warn'); delete it.dataset.pick; it.querySelectorAll('.eh-w').forEach(function(x){x.classList.remove('sel');}); it.querySelector('.eh-in').value=''; }); }

window.addEventListener('load', function(){ document.querySelectorAll('.sim').forEach(function(b){ simInit(b.id); }); document.querySelectorAll('.rf').forEach(function(b){ rfInit(b.id); }); });
