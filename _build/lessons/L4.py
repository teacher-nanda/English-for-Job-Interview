# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(4, 'Your Experience', 'in the Spotlight', 'L4')
FONTS = 'family=Playfair+Display:wght@700;800;900&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#0B5D45','#C9A227','#FFF8E1','#FFE680',
  'radial-gradient(circle at 50% 15%, #1F9C73 0%, #0B5D45 50%, #052B20 100%)',
  pattern='linear-gradient(45deg, rgba(201,162,39,.07) 25%, transparent 25%, transparent 75%, rgba(201,162,39,.07) 75%), linear-gradient(45deg, rgba(201,162,39,.07) 25%, transparent 25%, transparent 75%, rgba(201,162,39,.07) 75%)', patsize='40px 40px', fh='Playfair Display')

cover(L, [('🏆','top:10%;left:7%'),('🥇','top:14%;right:8%;animation-delay:-2s'),('🎖️','bottom:26%;left:9%;animation-delay:-4s'),('📈','bottom:28%;right:10%;animation-delay:-1s'),('⭐','top:46%;left:3%;animation-delay:-3s')],
      'Every good answer needs proof. Let\'s polish your trophies.')

L.slide('s-rf1','Lead-in – Stronger sentence','lead','Which sentence wins the trophy?',
  '<p class="instruction">Experience questions are about proof. Choose the stronger sentence each time.</p>'
  + rapidfire(L,'rf-lead',[
     ('Which is stronger?',['I was in charge of sales.','I grew monthly sales by 18% in six months.'],1),
     ('Which is stronger?',['I trained twelve new employees.','I helped with training.'],0),
     ('Which is stronger?',['I handled many customer complaints.','I resolved about 40 customer complaints a week.'],1),
     ('Which is stronger?',['I worked on a website project.','I redesigned our website and cut loading time in half.'],1),
     ('Which is stronger?',['I organized a conference for 300 guests.','I did some event stuff.'],0)], 12))

L.slide('s-flag','Vague or specific?','read','Vague or specific?',
  '<p class="instruction">Is each sentence vague or specific? There are 4 of each.</p>'
  + flagsort('fs-vs',[
     ('I did lots of things in my last job.','a'),
     ('I managed a budget of $50,000 for three campaigns.','b'),
     ('I worked with many clients.','a'),
     ('I answered about 60 emails and calls a day.','b'),
     ('I helped the team a bit.','a'),
     ('I trained five interns, and four received job offers.','b'),
     ('I was responsible for various tasks.','a'),
     ('I cut the delivery time from five days to two.','b')],
     ('a','🌫️ Vague'),('b','🎯 Specific')))

L.slide('s-gap','Action verbs','vocab','Pick the power verb',
  '<p class="instruction">Complete each sentence with a verb from the word bank.</p>'
  '<div class="tipbox"><b>led · designed · negotiated · increased · organized · reduced · created · coordinated · managed</b></div>'
  + gap('gap-v',[
     ('I','led','a team of six people.'),
     ('I','designed','a new training program.'),
     ('I','negotiated','a better price with our suppliers.'),
     ('I','increased','our social media followers by 40%.'),
     ('I','organized','a charity event for 200 guests.'),
     ('I','reduced','waiting times by ten minutes.'),
     ('I','created','a database for all our clients.'),
     ('I','coordinated','three departments during the move.')],
     example=('I','managed','a team of four.'), width=140))

L.slide('s-mc','Past or present perfect?','vocab','Tenses for your experience',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('mc-t',[
     ('I',['have worked','worked','work'],'have worked','in retail for six years now.'),
     ('In 2020, I',['joined','have joined','join'],'joined','a small design studio.'),
     ('I',['have managed','managed','manage'],'have managed','more than ten projects so far.'),
     ('Last year, we',['launched','have launched','launch'],'launched','a new app.'),
     ('I',['have never missed','never missed','never miss'],'have never missed','a deadline.'),
     ('Before that, I',['was working','am working','work'],'was working','at a hospital.'),
     ('I',['have been leading','lead','led'],'have been leading','the team since March.'),
     ('When I',['arrived','have arrived','arrive'],'arrived','the project was in trouble.')],
     example=('I','started','my career in 2016.')))

L.slide('s-og','Project story','vocab','Tell the story of a proud project',
  '<p class="instruction">Put the story in order: <b>background → my role → what I did → result</b>.</p>'
  + ordergame('og-pr',[
     'Last year, our bakery wanted to sell online, but we had no website.',
     'I volunteered to lead the project with one designer.',
     'I chose the platform, wrote all the product descriptions and tested every order.',
     'In three months, online orders grew from zero to 30% of our sales.'], seed=2, wide=True))

L.slide('s-wo','Word order workshop','vocab','Word order workshop',
  '<p class="instruction">Click the words in order to build natural experience sentences.</p>'
  + wordorder('wo-4',[
     'I led a team of eight people for two years.',
     'My biggest achievement was saving the company ten thousand dollars.',
     'I am responsible for training all new employees.',
     'Working under pressure has taught me to stay calm.'],
     example='I managed a budget of fifty thousand dollars.'))

L.slide('s-eh','Error hunt','vocab','Error hunt',
  '<p class="instruction">Each sentence has one wrong word. Click it, then type a better word.</p>'
  + errorhunt('eh-4',[
     ('I have led the team in 2022.',1,'led','have led'),
     ('She is responsible of the budget.',3,'for'),
     ('I increased sales with 20 percent.',3,'by'),
     ('He worked there since five years.',3,'for')])
  )

L.slide('s-sim','Experience interview','speak','Interview: your experience',
  '<p class="instruction">Choose the best answers.</p>'
  + sim(L,'sim-4','Mr. Duarte','👨‍💼',[
     ('Tell me about your most relevant experience.',[
        ('I’ve done a lot of things in many places.',0,'Too vague.'),
        ('For four years I’ve managed customer accounts for a software firm, with about 80 clients.',3,'Clear time, role and numbers.'),
        ('Everything is on my CV.',1,'Do not just point to the CV.')]),
     ('What was your biggest achievement?',[
        ('I helped reduce customer complaints by 35% after redesigning our help center.',3,'Specific, with a result.'),
        ('I was employee of the month once.',1,'Nice, but tell me why.'),
        ('I haven’t really achieved anything big.',0,'Never say this.')]),
     ('What was your role in that project?',[
        ('I led it from the start, with a team of three.',3,'Clear role.'),
        ('We all just did things together.',1,'Say what YOU did.'),
        ('My manager did most of it.',0,'Never take credit away from yourself.')])],
     [(0.8,'⭐ Excellent! Specific, confident, and full of results.'),(0.5,'👍 Good, but add more numbers.'),(0,'🔄 Try again with more detail and numbers.')]))

L.slide('s-roul','Question roulette','speak','Question roulette',
  '<p class="inst-light">Press the button. Use at least one number or result.</p>'
  + roulette(L,'rl-4',[
     ['What is your biggest professional achievement?','My biggest achievement was… I…'],
     ['Tell me about a project you led.','I led a project to… We…'],
     ['What did you do in your last job every day?','My main responsibilities were…'],
     ['Which accomplishment are you most proud of?','I’m proudest of… because…'],
     ['What have you learned from your experience?','I’ve learned that… For example…']])
  + timer('tm-4', 45))

L.slide('s-build','Answer builder','speak','Build your own achievement story',
  '<p class="inst-light">Choose a real project or achievement.</p>'
  + ab('L4-ach','My biggest achievement',[
      ('1 · Background','What was happening?','Frame: Last year, our team…'),
      ('2 · My role','What was your job?','Frame: I was responsible for…'),
      ('3 · Actions','What did you do?','Frame: I designed / led / organized…'),
      ('4 · Result','Add a number if you can.','Frame: As a result, we increased / reduced…')],'L4-a'))

L.slide('s-wrap','Spotlight report','review','Spotlight report',
  '<div class="tipbox"><h3>🏆 Today you can…</h3>• replace vague sentences with specific ones<br>• use power verbs like <b>led, designed, negotiated</b><br>• choose between past simple and present perfect<br>• tell a proud-project story in four steps</div>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> STAR stories.</div>')

hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('hw1',[
     ('I',['have worked','worked','work'],'have worked','here since 2018.'),
     ('Last month, I',['finished','have finished','finish'],'finished','a big project.'),
     ('I am responsible',['for','of','to'],'for','new clients.'),
     ('We increased sales',['by','with','at'],'by','15%.'),
     ('I',['have trained','trained','train'],'have trained','over 50 people so far.'),
     ('In 2019, she',['was promoted','has promoted','promotes'],'was promoted','to manager.'),
     ('I',['managed','manage','am managing'],'managed','the budget last year.'),
     ('Our team',['has grown','grew','grow'],'has grown','a lot recently.')],
     example=('I','joined','the company in 2019.')))
L.slide('hw-2','HW2 – Say it','hw','Practice out loud',
  '<div class="tipbox"><h3>🎧 Your plan for this week</h3>1. Write <b>three</b> achievements with numbers.<br>2. Pick the best one and tell it out loud <b>three times</b>.<br>3. Ask yourself: <b>Did I include a result?</b></div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
