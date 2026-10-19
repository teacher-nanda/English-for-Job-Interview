# -*- coding: utf-8 -*-
import sys, os, json, re, importlib
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
SH=os.path.join(HERE,'shared'); OUT=os.path.dirname(HERE)
BASEURL='https://teacher-nanda.github.io/English-for-Job-Interview/'
def rd(p): return open(p,encoding='utf-8').read()

def build(mod):
    M=importlib.import_module('lessons.'+mod); L=M.L
    ids=[s[0] for s in L.S]; labels=[s[1] for s in L.S]
    assert len(set(ids))==len(ids), 'duplicate ids'
    name='Job Interview %d — %s' % (L.num, re.sub('<[^>]+>','',L.title+' '+L.accent).replace('  ',' '))
    lesson_name=re.sub('<[^>]+>',' ',L.title+' '+L.accent); lesson_name=' '.join(lesson_name.split())
    url=BASEURL+L.slug+'/index.html'
    fonts=M.FONTS
    css=rd(SH+'/base.css').replace('AEF4 4B \\2014  A Risky Business','Job Interview %d \\2014  %s' % (L.num, lesson_name))
    css+='\n'+rd(SH+'/engine.css')+'\n'+M.THEME
    chrome=rd(SH+'/chrome.html')+'''
<div id="lvBar"><button data-lv="support" onclick="setLevel('support')">🌱 Support</button><button data-lv="standard" onclick="setLevel('standard')">🎯 Standard</button><button data-lv="challenge" onclick="setLevel('challenge')">🔥 Challenge</button></div>'''
    nav=rd(SH+'/nav.html').replace('<button onclick="this.blur();clearAllNotes()"','<button onclick="openNotebook()" style="margin-left:6px;padding:5px 12px;background:#1F7A5A;color:#fff;border:none;border-radius:7px;font-size:.82rem;cursor:pointer;font-family:inherit;">📓 Notebook</button>\n  <button onclick="this.blur();clearAllNotes()"')
    jsn=rd(SH+'/js_nav.js'); jsg=rd(SH+'/js_generic.js')
    jsg=jsg.replace("function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; }","function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; try{ localStorage.setItem(notesStoreKey, JSON.stringify(notesData)); }catch(e){} }")
    eng=rd(SH+'/engine.js'); pdf=rd(SH+'/js_pdf.js').replace('__LESSON_NAME__',lesson_name).replace('__URL__',url)
    slides_html='\n\n'.join(s[2] for s in L.S)
    html='<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>%s</title>\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?%s&display=swap" rel="stylesheet">\n<style>\n%s\n</style>\n</head>\n<body data-lesson="Lesson %d">\n%s\n<div id="deck">\n\n%s\n\n</div><!-- END #deck -->\n\n%s\n<script>\n/* ===== SLIDE NAV DATA ===== */\nvar slideIds = %s;\nvar slideLabels = %s;\n%s\n%s\n%s\n%s\n%s\n</script>\n</body>\n</html>\n' % (
        name, fonts, css, L.num, chrome, slides_html, nav, json.dumps(ids), json.dumps(labels,ensure_ascii=False), jsn, jsg, eng, L.js, pdf)
    d=os.path.join(OUT,L.slug); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(html)
    print(L.slug, len(L.S),'slides', len(html),'bytes')


def home():
    cards=[('L1','Welcome to the Interview Lab','Storytelling, why interviewers ask, "Tell me about yourself"','🧪','#1B9AAA'),
           ('L2','Strengths & Weaknesses','Superpowers, green flags and red flags','🦸','#E0457B'),
           ('L3','Why this job? Your Road Map','Motivation, the job ad, career goals','🗺️','#F28C28'),
           ('L4','Your Experience in the Spotlight','Achievements, strong verbs, numbers','🏆','#C9A227'),
           ('L5','STAR Stories, Part 1','Situation · Task · Action · Result','⭐','#5B6CFF'),
           ('L6','STAR Stories, Part 2','Difficult people, change, diplomatic language','🎭','#FF6F59'),
           ('L7','Your CV','Own every line: gaps, changes and strong bullets','📄','#D9822B'),
           ('L8','Company Knowledge & Culture','Research, cultural differences, small talk','🌍','#2FB8A0'),
           ('L9','Confidence & Your Questions','Questions to ask, clarifying, confirming the appointment','💬','#FF8A5B'),
           ('L10','Mock Interview Day','Full simulation, scorecard and feedback','🎤','#F5B700')]
    h=''
    for i,(slug,t,d,e,c) in enumerate(cards,1):
        if slug: h+='<a class="card" href="%s/index.html" style="--c:%s"><div class="n">%d</div><div class="e">%s</div><h3>%s</h3><p>%s</p></a>' % (slug,c,i,e,t,d)
        else: h+='<div class="card soon" style="--c:%s"><div class="n">%d</div><div class="e">%s</div><h3>%s</h3><p>%s</p><span class="tag">coming soon</span></div>' % (c,i,e,t,d)
    page='''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Job Interview Course</title>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=DM+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:'DM Sans',system-ui,sans-serif;background:#0F2433;color:#fff}
.hero{padding:48px 32px 24px;text-align:center}.hero small{letter-spacing:.3em;text-transform:uppercase;color:#FFD84D;font-weight:800}
.hero h1{font-family:'Fredoka',sans-serif;font-size:clamp(2.4rem,5vw,4rem);margin:10px 0 6px}.hero p{font-size:1.15rem;opacity:.85;margin:0 auto;max-width:720px;line-height:1.6}
.lv{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:18px 0 0}.lv span{background:rgba(255,255,255,.12);border-radius:999px;padding:6px 16px;font-weight:700}
.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:18px;padding:24px 32px 40px;max-width:1500px;margin:0 auto}
.card{position:relative;display:block;text-decoration:none;color:#fff;background:rgba(255,255,255,.07);border:3px solid var(--c);border-radius:22px;padding:20px 18px 22px;transition:transform .15s}
a.card:hover{transform:translateY(-4px);background:rgba(255,255,255,.13)}.card .n{position:absolute;top:12px;right:16px;font-family:'Fredoka';font-size:1.6rem;opacity:.5}
.card .e{font-size:2.6rem}.card h3{font-family:'Fredoka';margin:8px 0 6px;font-size:1.3rem;line-height:1.2}.card p{margin:0;opacity:.85;line-height:1.5;font-size:1rem}
.soon{opacity:.55;border-style:dashed}.tag{display:inline-block;margin-top:10px;background:rgba(255,255,255,.15);border-radius:999px;padding:2px 12px;font-size:.8rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.nb{text-align:center;padding-bottom:40px}.nb button{background:#1F7A5A;color:#fff;border:none;border-radius:14px;padding:14px 30px;font-size:1.1rem;font-weight:800;cursor:pointer;font-family:inherit}
@media(max-width:1100px){.grid{grid-template-columns:repeat(2,1fr)}}</style></head><body>
<div class="hero"><small>Conversational English with teacher Nanda</small><h1>🎤 Job Interview Course</h1>
<p>Ten interactive lessons to prepare for job interviews in English. In every lesson you can choose your level at the top of the screen.</p>
<div class="lv"><span>🌱 Support</span><span>🎯 Standard</span><span>🔥 Challenge</span></div></div>
<div class="grid">'''+h+'''</div>
<div class="nb"><button onclick="openNotebook()">📓 Open my Interview Notebook</button></div>
<script>'''
    # notebook function only
    eng=rd(SH+'/engine.js'); start=eng.index('var AB_KEY'); end=eng.index('/* ---- course map')
    nb=eng[start:end].replace("document.querySelectorAll('.ab').forEach","(function(){})||[].forEach")
    page+= "var AB_KEY='jic::ans';\n"+eng[start:eng.index("function abBuild")]+eng[eng.index("function openNotebook"):end]+'</script></body></html>'
    open(os.path.join(OUT,'index.html'),'w',encoding='utf-8').write(page); print('home ok')

if __name__=='__main__':
    for m in (sys.argv[1:] or ['L%d'%i for i in range(1,11)]): build(m)
    home()
