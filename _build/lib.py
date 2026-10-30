import examples as EX
# -*- coding: utf-8 -*-
import random, html, math

def esc(s): return html.escape(s, quote=False)
def q(s): return html.escape(s, quote=True)

def sup(h): return '<div class="sup">%s</div>' % h
def chal(h): return '<div class="chal">%s</div>' % h
def chipa(t): return '<span class="chip-a">%s</span>' % t
def chipb(t): return '<span class="chip-b">%s</span>' % t
def chipc(t): return '<span class="chip-c">%s</span>' % t
def green(t): return '<span style="color:#1A7A4A;font-weight:800;background:#E3F5EA;padding:1px 7px;border-radius:5px;">%s</span>' % t

BANNERS = {'lead':('banner-leadin','🔥 Lead-in'), 'vocab':('banner-vocab','📚 Vocabulary'), 'gram':('banner-grammar','🧩 Language'),
           'speak':('banner-speaking','🎤 Speaking'), 'pron':('banner-pron','🔊 Pronunciation'), 'read':('banner-reading','📖 Reading'),
           'review':('banner-review','🏁 Wrap-up'), 'hw':('banner-hw','📝 Homework')}

class Lesson:
    def __init__(self, num, title, accent_title, url_slug):
        self.num=num; self.title=title; self.accent=accent_title; self.slug=url_slug
        self.S=[]; self.js=''
    def slide(self, sid, label, kind, heading, body, banner_text=None):
        cls, txt = BANNERS[kind]
        if banner_text: txt = banner_text
        h = '<div class="slide" id="%s">\n  <div class="banner %s">%s</div>\n  <div class="slide-main"><div class="content">\n' % (sid, cls, txt)
        if heading: h += '    <h2>%s</h2>\n' % heading
        h += body + '\n  </div></div>\n</div>'
        self.S.append((sid, label, h))
    def raw(self, sid, label, h): self.S.append((sid, label, h))

def btns(check, reset, extra=''):
    return '<div class="btn-row"><button class="btn-check" onclick="%s">Check Answers</button><button class="btn-reset" onclick="%s">Reset</button>%s</div>' % (check, reset, extra)

def split(items):
    n = (len(items)+1)//2
    return items[:n], items[n:]

def gap(eid, items, example=None, width=180):
    """items: (before, ans, after[, alt]) ; example: (before, ans, after) shown as green item in left column."""
    rows=[]
    if example:
        rows.append('<div class="ex-row"><span class="example-badge">✓</span>%s %s %s</div>' % (example[0], green(example[1]), example[2]))
    for i,it in enumerate(items,1):
        alt = ' data-alt="%s"' % q(it[3]) if len(it)>3 and it[3] else ''
        rows.append('<div class="ex-row"><span class="circ-num">%d</span>%s <input class="ans-input" style="width:%dpx" type="text" data-ans="%s"%s aria-label="answer %d"> %s</div>' % (i, it[0], width, q(it[1]), alt, i, it[2]))
    l,r = split(rows)
    return '<div id="%s"><div class="fixed-two-col"><div>%s</div><div>%s</div></div>%s</div>' % (eid, ''.join(l), ''.join(r), btns("checkSlide('%s')"%eid, "resetSlide('%s')"%eid))

def mcq(eid, items, example=None):
    """items: (before, [opts], correct, after)"""
    rows=[]
    if example:
        rows.append('<div class="ex-row"><span class="example-badge">✓</span>%s %s %s</div>' % (example[0], green(example[1]), example[2]))
    for i,it in enumerate(items,1):
        opts=''.join('<button class="circ-opt" data-group="%s-%d" data-correct="%s" onclick="circPick(this)">%s</button>' % (eid,i,q(it[2]),o) for o in it[1])
        rows.append('<div class="ex-row"><span class="circ-num">%d</span>%s %s %s</div>' % (i, it[0], opts, it[3]))
    l,r = split(rows)
    return '<div id="%s"><div class="fixed-two-col"><div>%s</div><div>%s</div></div>%s</div>' % (eid, ''.join(l), ''.join(r), btns("checkCircSlide('%s')"%eid, "resetCircSlide('%s')"%eid))

def flagsort(eid, items, a, b):
    """items: (text, 'a'|'b'); a,b: (key,label)"""
    cards=[]
    for t,ans in items:
        k = a[0] if ans=='a' else b[0]
        cards.append('<div class="fs-card" data-ans="%s"><span class="fs-t">%s</span><button class="fs-btn" onclick="fsPick(this,\'%s\')">%s</button><button class="fs-btn" onclick="fsPick(this,\'%s\')">%s</button></div>' % (k, t, a[0], a[1], b[0], b[1]))
    l,r = split(cards)
    return '<div id="%s"><div class="fs"><div class="fs-col">%s</div><div class="fs-col">%s</div></div>%s</div>' % (eid, ''.join(l), ''.join(r), btns("fsCheck('%s')"%eid, "fsReset('%s')"%eid))

def multipick(eid, items):
    """items: (text, bool correct) - shown in given order, 2 cols top-to-bottom"""
    opts=['<button class="mp-opt" data-correct="%d" onclick="mpToggle(this)">%s</button>' % (1 if c else 0, t) for t,c in items]
    l,r = split(opts)
    return '<div id="%s"><div class="mp"><div class="stack">%s</div><div class="stack">%s</div></div>%s</div>' % (eid, ''.join(l), ''.join(r), btns("mpCheck('%s')"%eid, "mpReset('%s')"%eid))

def shuffled(n, seed):
    idx=list(range(n)); rnd=random.Random(seed)
    for _ in range(50):
        rnd.shuffle(idx)
        if idx!=list(range(n)) and all(idx[i]!=i for i in range(min(n,3))): break
    return idx

def ordergame(eid, items, seed=7, wide=False):
    """items listed in CORRECT order."""
    n=len(items)
    slots=''.join('<div class="og-slot" data-n="%d"></div>' % (i+1) for i in range(n))
    chips=''.join('<button class="og-chip" data-i="%d" onclick="ogClick(this)">%s</button>' % (i, items[i]) for i in shuffled(n, seed))
    return '<div class="og%s" id="%s"><div class="og-slots">%s</div><div class="og-pool">%s</div>%s</div>' % (' wide' if wide else '', eid, slots, chips, btns("ogCheck('%s')"%eid, "ogReset('%s')"%eid))

def buckets(eid, bks, chips, seed=5, cols=None, side=False):
    """bks: [(key,label)], chips: [(text,key)]"""
    n=len(chips); order=shuffled(n, seed)
    pool=''.join('<button class="bk-chip" data-ans="%s" onclick="bkChip(this);event.stopPropagation()">%s</button>' % (chips[i][1], chips[i][0]) for i in order)
    bb=''.join('<div class="bk-b" data-b="%s" onclick="bkPut(this)"><h4>%s</h4><div class="bk-drop"></div></div>' % (k,l) for k,l in bks)
    return '<div class="bk%s" id="%s"><div class="bk-pool">%s</div><div class="bk-row" style="--cols:%d">%s</div>%s</div>' % (' side' if side else '', eid, pool, cols or len(bks), bb, btns("bkCheck('%s')"%eid, "bkReset('%s')"%eid))

def timer(eid, sec):
    return '<div class="tm" id="%s" data-sec="%d"><div class="tm-d">%d</div><button class="tm-go" onclick="tmStart(this)">▶ Start</button><button onclick="tmReset(this)">↺</button></div>' % (eid, sec, sec)

def roulette(L, eid, items, label='🎲 Ask me!'):
    import json
    items=[list(it)+[EX.RL.get((eid,i_),'')] for i_,it in enumerate(items)]
    L.js += 'RL[%s]=%s;\n' % (json.dumps(eid), json.dumps(items, ensure_ascii=False))
    return '<div class="rl" id="%s"><div class="rl-q">Press the button to get your interview question.</div><div class="rl-f sup"></div><button onclick="rlNext(\'%s\')">%s</button></div>' % (eid, eid, label)

def branch(situation, opts):
    """opts: (text, rate good|ok|bad, feedback)"""
    o=''.join('<button class="br-opt" data-rate="%s" data-fb="%s" onclick="brPick(this)">%s</button>' % (r, q(fb), t) for t,r,fb in opts)
    return '<div class="br"><div class="say-it">%s</div>%s<div class="br-fb"></div></div>' % (situation, o)

def ab(key, title, steps, order):
    """steps: (label, hint, support_frame)"""
    s=''
    for i_,(lab,hint,frame) in enumerate(steps):
        ex_=EX.AB.get((key,i_))
        if frame and ex_: frame += '</span><span class="ab-ex">💡 Example: ' + ex_.replace('<','&lt;')
        s += '<div class="ab-step"><div class="ab-lab">%s</div><div class="ab-hint">%s</div>%s<textarea class="ab-in" rows="2" aria-label="%s"></textarea></div>' % (lab, hint, sup('<span class="ab-sup">%s</span>' % frame) if frame else '', q(lab))
    return ('<div class="ab" data-key="%s" data-title="%s" data-order="%s">%s<div class="btn-row"><button class="btn-check" onclick="abBuild(this)">✨ Build my answer</button><button class="btn-reset" onclick="abClear(this)">Clear</button><button class="btn-suggest" onclick="openNotebook()">📓 My Interview Notebook</button></div><div class="ab-out"></div></div>' % (key, q(title), order, s))

def cover(L, chips, tagline):
    ch=''.join('<div class="cv-chip" style="%s">%s</div>' % (st, e) for e,st in chips)
    lv='''<div class="lv-pick">
      <button data-lv="support" onclick="setLevel('support')">🌱 Support<small>sentence starters + word help</small></button>
      <button data-lv="standard" onclick="setLevel('standard')">🎯 Standard<small>the full lesson (B2)</small></button>
      <button data-lv="challenge" onclick="setLevel('challenge')">🔥 Challenge<small>tougher questions, no help</small></button></div>'''
    h='''<div class="slide active" id="s1">
  %s
  <div class="title-inner">
    <div class="course-tag">Job Interview Course · Lesson %d</div>
    <div class="title-label">Conversational English</div>
    <div class="title-sub">with teacher Nanda</div>
    <div class="title-main">%s<br><span class="title-accent">%s</span></div>
    <div class="title-sub" style="margin:14px 0 0;position:relative;z-index:3;">%s</div>
    %s
    <a href="../index.html" title="All lessons" style="position:absolute;bottom:70px;left:32px;font-size:1.7rem;line-height:1;text-decoration:none;filter:drop-shadow(0 1px 3px rgba(0,0,0,.3));z-index:5;">🏠</a>
    <div style="position:absolute;bottom:70px;right:32px;z-index:5;"><button class="cover-btn" onclick="goToId('hw-cover')" style="padding:11px 24px;font-size:.95rem;cursor:pointer;">📝 Homework</button></div>
  </div>
</div>''' % (ch, L.num, L.title, L.accent, tagline, lv)
    L.raw('s1','Cover',h)

def hwcover(L, text='Practice at home'):
    h='''<div class="slide" id="hw-cover">
  <div class="title-inner">
    <div class="course-tag">Lesson %d · Homework</div>
    <div class="title-main">%s</div>
    <div class="title-sub" style="margin-top:14px;position:relative;z-index:3;">Use only what we practiced in this lesson. Take your time!</div>
    <a href="#" onclick="goTo(0);return false;" style="position:absolute;bottom:70px;left:32px;font-size:1.7rem;text-decoration:none;z-index:5;">🏠</a>
  </div>
</div>''' % (L.num, text)
    L.raw('hw-cover','Homework Cover',h)


def theme(c1,c2,c3,c4,cover,pattern='none',patsize='auto',fh='Fredoka',ink=None,bodyfont="'DM Sans','Segoe UI',system-ui,sans-serif",extra=''):
    return (":root{--c1:%s;--c2:%s;--c3:%s;--c4:%s;--ink:%s;--fh:'%s';--pattern:%s;--patsize:%s;}\n"
            "body{font-family:%s;background:%s;}\n#s1,#hw-cover{background:%s;align-items:center;justify-content:center;}\n"
            ".rl:not(.spun) .rl-f{display:none !important;}\n%s\n") % (c1,c2,c3,c4,ink or c1,fh,pattern,patsize,bodyfont,c1,cover,extra)

# ---------------- new interactive builders ----------------
import json as _json

def sim(L, eid, who, avatar, turns, verdicts):
    """turns: [(question, [(option text, score 0-3, feedback), ...]), ...]; verdicts: [(min_fraction, text)] high->low"""
    data={'who':who,'turns':[{'q':q_,'opts':[{'t':t,'s':s,'fb':fb} for t,s,fb in opts]} for q_,opts in turns],'verdicts':verdicts}
    L.js += 'SIM[%s]=%s;\n' % (_json.dumps(eid), _json.dumps(data, ensure_ascii=False))
    return ('<div class="sim" id="%s"><div class="sim-top"><span class="sim-face">🙂</span><span class="sim-who">%s %s</span><span>Impression</span><div class="sim-meter"><div class="sim-fill"></div></div></div>'
            '<div class="sim-log"></div><div class="sim-opts"></div>'
            '<div class="sim-end"><div class="sim-verdict"></div><button onclick="simInit(\'%s\')">↺ Try again</button></div></div>') % (eid, avatar, who, eid)

def rapidfire(L, eid, items, sec=12):
    """items: [(question html, [options], correct index)]"""
    its=[]
    for n,(a,b,c) in enumerate(items):
        idx=list(range(len(b))); random.Random(11+n).shuffle(idx)
        its.append({'q':a,'o':[b[i] for i in idx],'a':idx.index(c)})
    data={'sec':sec,'items':its}
    L.js += 'RF[%s]=%s;\n' % (_json.dumps(eid), _json.dumps(data, ensure_ascii=False))
    return ('<div class="rf" id="%s"><div class="rf-play"><div class="rf-head"><span class="rf-n"></span><span class="rf-score"></span></div><div class="rf-track"><div class="rf-bar"></div></div>'
            '<div class="rf-q"></div><div class="rf-opts"></div></div><div class="rf-end"><div class="rf-result"></div><button onclick="rfInit(\'%s\')">↺ Play again</button></div></div>') % (eid, eid)

def memory(eid, pairs, seed=3):
    cards=[]
    for i,(a,b) in enumerate(pairs): cards += [(i,a),(i,b)]
    random.Random(seed).shuffle(cards)
    cs=''.join('<button class="mem-c" data-p="%d" onclick="memFlip(this)">%s</button>' % (p,t) for p,t in cards)
    return ('<div class="mem" id="%s" data-moves="0"><div class="mem-top"><span class="mem-moves">Moves: 0</span><button onclick="memReset(\'%s\')">↺ Shuffle</button></div>'
            '<div class="mem-grid">%s</div><div class="mem-win">🎉 You found all the pairs!</div></div>') % (eid, eid, cs)

def wordorder(eid, sentences, example=None, seed=4):
    h=''
    if example:
        h += '<div class="wo-item"><div class="wo-line ok"><span class="example-badge">✓</span> %s</div></div>' % example
    for k,s in enumerate(sentences):
        w=s.split(' '); idx=shuffled(len(w), seed+k)
        tiles=''.join('<button class="wo-t" onclick="woClick(this)">%s</button>' % w[i] for i in idx)
        h += '<div class="wo-item" data-ans="%s"><div class="wo-line"></div><div class="wo-pool">%s</div></div>' % (q(s), tiles)
    return '<div id="%s">%s%s</div>' % (eid, h, btns("woCheck('%s')"%eid, "woReset('%s')"%eid))

def errorhunt(eid, items):
    """items: (sentence, wrong word index (0-based), correction[, alt])"""
    h=''
    for n,it in enumerate(items,1):
        s,wi,fix=it[0],it[1],it[2]; alt=it[3] if len(it)>3 else ''
        words=''.join('<button class="eh-w" data-i="%d" onclick="ehPick(this)">%s</button>' % (i,w) for i,w in enumerate(s.split(' ')))
        h += '<div class="eh-item" data-wrong="%d"><span class="circ-num">%d</span>%s<span class="eh-fixlab">→ better:</span> <input class="eh-in" type="text" data-ans="%s" data-alt="%s" aria-label="correction %d"></div>' % (wi,n,words,q(fix),q(alt),n)
    return '<div id="%s">%s%s</div>' % (eid, h, btns("ehCheck('%s')"%eid, "ehReset('%s')"%eid))

def mind(answer, thought, who='🧑‍💼 Candidate'):
    return ('<div class="mindwrap"><div class="say"><b>%s:</b> %s</div><button class="mindbtn" onclick="this.nextElementSibling.classList.toggle(\'show\')">🧠 What is the interviewer thinking?</button>'
            '<div class="thought">%s</div></div>') % (who, answer, thought)
