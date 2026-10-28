# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(1, 'Welcome to the', 'Interview Lab', 'L1')
FONTS = 'family=Fredoka:wght@500;600;700&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#12324A','#1B9AAA','#E6F6F8','#FFD84D',
  'radial-gradient(circle at 25% 20%, #1B6E96 0%, #12324A 60%, #0A1B28 100%)',
  pattern='linear-gradient(rgba(27,154,170,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(27,154,170,.08) 1px,transparent 1px)', patsize='34px 34px')

cover(L, [('🧪','top:10%;left:7%'),('🔬','top:14%;right:8%;animation-delay:-2s'),('⚗️','bottom:24%;left:9%;animation-delay:-4s'),('💼','bottom:26%;right:10%;animation-delay:-1s'),('🎤','top:44%;left:3%;animation-delay:-3s')],
      'Experiment, practice and get ready for the real thing.')

# ---------- 2 FIRST FIVE MINUTES (scenarios)
L.slide('s-first','Lead-in – First five minutes','lead','Lab test: survive the first five minutes',
  '<p class="instruction">The interview starts before the first question! Choose what you would do in each moment. Then compare with the lab results.</p>'
  '<div class="twocol"><div>'
  + branch('🕘 <b>Moment 1.</b> You arrive 20 minutes early. The receptionist says, “Please take a seat. Someone will be with you soon.”',[
     ('Review my notes quietly and read the company brochure on the table.','good','Perfect. You stay calm and you learn something about the company.'),
     ('Call a friend to say I am nervous.','bad','A loud phone call in the waiting room? The receptionist notices everything.'),
     ('Scroll on my phone and eat a snack.','ok','Not terrible, but this is a missed chance to prepare and look interested.')])
  + '</div><div>'
  + branch('🤝 <b>Moment 2.</b> The interviewer shakes your hand and asks, “How are you today?”',[
     ('“Fine.”','ok','Correct but cold. A friendly answer sets the mood.'),
     ('“Very well, thank you. It’s a pleasure to meet you.”','good','Warm, polite and confident. A great start.'),
     ('“Honestly, I’m terrified and my bus was late.”','bad','Too much information. Keep the first minute positive.')])
  + '</div></div>'
  + sup('<b>brochure</b> = a small printed paper about a company · <b>terrified</b> = very afraid · <b>notice</b> = see and remember')
  + chal('Which moment makes you most nervous in real life? Tell me why, and what you will do.'))

L.slide('s-first2','Lead-in – Surprises','lead','Lab test: surprises in the room',
  '<p class="instruction">Interviews always bring surprises. Choose your best reaction.</p>'
  '<div class="twocol"><div>'
  + branch('❓ <b>Moment 3.</b> You do not understand the question.',[
     ('Guess and talk anyway.','bad','You may answer a different question. Never guess.'),
     ('“Could you rephrase that, please?”','good','Perfect. Interviewers respect people who ask politely.'),
     ('Stay silent and look at the table.','bad','Silence for too long feels uncomfortable for everyone.')])
  + '</div><div>'
  + branch('🙈 <b>Moment 4.</b> In the middle of your answer, you say a sentence with a grammar mistake.',[
     ('Stop, apologize three times and start again.','bad','Too much. This hurts your confidence more than the mistake.'),
     ('Correct it quickly if you notice, and continue smoothly.','good','Natural and calm. Even native speakers do this.'),
     ('Ignore it and keep going.','ok','Fine for small mistakes. Fix it if it changes the meaning.')])
  + '</div></div>'
  + sup('<b>rephrase</b> = say again with different words · <b>respect</b> = admire and value · <b>smoothly</b> = without stopping or problems'))

# ---------- 3 STORY WEB
L.slide('s-story','One story, many questions','read','One story, many questions',
  '<div class="twocol"><div>'
  '<div class="tipbox"><h3>🎬 The secret of good interviews</h3>Interviewers love <span class="chip-a">stories</span>. A story is proof. '
  'Prepare <span class="chip-b">a few strong stories</span> about your work, and you can use each one to answer <span class="chip-c">many different questions</span>.</div>'
  + sup('<b>proof</b> = something that shows a thing is true · <b>prepare</b> = get ready before')
  + '</div><div>'
  '<div class="say-it"><b>My story:</b> The morning the office printer broke, one hour before a big client presentation, I found a way to finish on time.</div>'
  '<p class="instruction">Which of these questions could this story answer? There are 3 in total.</p>'
  + multipick('mp-story',[
     ('How do you stay calm when things go wrong?',True),
     ('What is your notice period?',False),
     ('Tell me about a time you used your own initiative.',True),
     ('Which languages do you speak?',False),
     ('Can you give an example of good time management?',True),
     ('Do you have a driver’s license?',False)])
  + '</div></div>')

L.slide('s-stories','My story bank','speak','Your story bank',
  '<p class="inst-light">Choose <b>three</b> real stories from your work or studies. Write a short title for each one. Then tell me about them.</p>'
  + ab('L1-stories','My story bank',[
     ('Story 1','A time you worked with other people.','Frame: The time I worked with… on…'),
     ('Story 2','A time you solved a problem.','Frame: The time I had to solve…'),
     ('Story 3','A time you were proud of your result.','Frame: The time I finished… successfully.')],'L1-b')
  + chal('For each story, name <b>two different interview questions</b> it could answer.'))

# ---------- 4 MISSION MAP
def tile(label, info): return '<button class="maptile" data-info="%s" onclick="mapPick(this)">%s</button>' % (q(info), label)
L.slide('s-map','Mission control','lead','Mission control: your course',
  '<p class="instruction">Click each mission to see what you will do. Which mission do you need most?</p>'
  '<div class="mapwrap"><div class="mapgrid">'
  + tile('🎯 Common questions','<b>Mission:</b> win the questions every interviewer asks. You will learn <u>why</u> they ask, what to say, and what to avoid.')
  + tile('🎭 Situational questions','<b>Mission:</b> prove your soft skills with real stories. Your tool: the STAR method.')
  + tile('📄 Your CV','<b>Mission:</b> turn every line of your CV into a strong talking point. Expect questions about everything on it!')
  + tile('💪 Confidence','<b>Mission:</b> stay calm, ask smart questions, and work with your strengths.')
  + tile('🔎 Company knowledge','<b>Mission:</b> do your homework. Read the job ad, research the company, and use what you find.')
  + tile('🌍 Culture awareness','<b>Mission:</b> understand how interviews work in other countries: what is normal, polite or surprising.')
  + '</div><div class="mapinfo">👆 Choose a mission.</div></div>'
  '<p class="inst-light" style="margin-top:14px;">In every lesson, we also train: <span class="pill">vocabulary</span><span class="pill">grammar</span><span class="pill">pronunciation</span><span class="pill">connectors</span></p>')

# ---------- 5 INTERVIEWER'S MIND (typed matching)
pur = ('<div class="tipbox"><h3>🧠 What is the interviewer thinking?</h3>'
 '<b>a.</b> Are this person’s salary hopes realistic?<br>'
 '<b>b.</b> How does this person react to feedback?<br>'
 '<b>c.</b> What is this person’s attitude to the old job and boss?<br>'
 '<b>d.</b> Did this person research us? Do they really care?<br>'
 '<b>e.</b> Who is the real person outside of work?<br>'
 '<b>f.</b> What do other people think of this person’s work?</div>')
qs = [('Do you have any questions for us?','d'),('How do you handle criticism?','b'),('What salary are you expecting?','a'),
      ('Why are you leaving your current job?','c'),('What do you do in your free time?','e'),('What would your last manager say about you?','f')]
rows = ['<div class="ex-row"><span class="example-badge">✓</span><span style="color:#1A7A4A;font-weight:800;background:#E3F5EA;padding:1px 9px;border-radius:5px;margin-right:10px;display:inline-block;min-width:56px;text-align:center;">%s</span>%s</div>' % (qs[0][1], qs[0][0])]
for i,(t,a) in enumerate(qs[1:],1):
    rows.append('<div class="ex-row"><span class="circ-num">%d</span><input class="ans-input" style="width:56px;margin-right:10px" type="text" maxlength="1" data-ans="%s" aria-label="thought %d">%s</div>' % (i,a,i,t))
L.slide('s-mind','Inside the interviewer’s mind','vocab','Inside the interviewer’s mind',
  '<p class="instruction">Every question has a secret purpose. Match each question to the thought behind it. Type the letter.</p>'
  '<div class="twocol"><div id="ex-mind">' + ''.join(rows) + btns("checkSlide('ex-mind')","resetSlide('ex-mind')") + '</div><div>' + pur + '</div></div>'
  + sup('<b>criticism</b> = saying what is wrong with your work · <b>current</b> = now · <b>realistic</b> = possible, not a dream · <b>attitude</b> = the way you think and feel about something')
  + chal('Choose one question. Tell me what a <b>bad</b> answer sounds like, and what the interviewer would think.'))

L.slide('s-mindread','Read the interviewer’s mind','speak','Read the interviewer’s mind',
  '<p class="instruction">The question is: <i>“Why are you leaving your current job?”</i> First, decide if each answer is good. Then click the button to read the interviewer’s thoughts.</p>'
  + mind('My boss was terrible and the pay was awful.', 'If this person speaks like that about the old boss, what will they say about us? Hmm…')
  + mind('I learned a lot in my last job, and now I’m ready for more responsibility.', 'Positive, honest and ambitious. I like this answer.')
  + mind('I don’t know. I just wanted a change.', 'No plan, no reason. Is this person serious about this job?')
  + sup('<b>ambitious</b> = wants to succeed and grow · <b>responsibility</b> = a duty or a job that you are in charge of')
  + chal('Now give your own answer. You may <b>not</b> say anything negative about your old job.'))

# ---------- 6 SANDWICH ORDER
L.slide('s-order','Build the perfect intro','vocab','Build a perfect “Tell me about yourself”',
  '<p class="instruction">A great introduction has a clear path: <b>present → past → future</b>. Put these four sentences in the best order.</p>'
  + ordergame('og-intro',[
     'I’m a project coordinator at a travel company, where I organize group tours across Europe.',
     'Before that, I studied tourism and spent two summers working as a hotel receptionist.',
     'Those jobs taught me to stay calm with customers and to solve problems quickly.',
     'Now I’m looking for a role where I can lead bigger projects, and that’s why I applied here.'], seed=5, wide=True)
  + sup('<b>coordinator</b> = a person who organizes people and activities · <b>receptionist</b> = a person who welcomes visitors')
  + chal('Write your own four sentences with the same path. Do not use the word <b>“passionate”</b>.'))

L.slide('s-wo','Word order workshop','vocab','Word order workshop',
  '<p class="instruction">Click the words in the right order to make a natural sentence from an interview.</p>'
  + wordorder('wo-1',[
     'I have been working as a coordinator for four years.',
     'Before that I studied tourism at university.',
     'What I enjoy most is helping people solve problems.',
     'I am looking for a role with more responsibility.'],
     example='I graduated in 2019 and joined my current company the same year.')
  + sup('Start with the subject: <b>I</b> · then the verb · then the details (where? when? how long?).'))

# ---------- 7 TIMELINE GAP FILL
L.slide('s-gap','Talk about your timeline','vocab','Talk about your timeline',
  '<p class="instruction">Type the missing word: <b>in, for, since, ago, or during</b>.</p>'
  + gap('gap-tl',[
     ('I graduated','in','2018 and started working right away.'),
     ('I have worked here','for','six years.'),
     ('She joined the team three months','ago','.'),
     ('We have used this software','since','January.'),
     ('I managed two projects','during','my last year at the company.'),
     ('He moved to Toronto','in','2021.'),
     ('I have been a nurse','since','2015.'),
     ('I started my first job five years','ago','.')],
     example=('I have studied English','for','ten years.'), width=110)
  + sup('<b>for</b> + a period of time (six years) · <b>since</b> + a starting point (2015) · <b>ago</b> = back from now · <b>in</b> + a year or month'))

# ---------- 8 RAPID FIRE + ERROR HUNT
L.slide('s-rf','Rapid fire','vocab','Rapid fire: for, since, ago, in',
  '<p class="instruction">Answer fast! Each question has a timer. How many can you get right?</p>'
  + rapidfire(L,'rf-time',[
     ('I have lived here ___ 2017.',['for','since','ago'],1),
     ('I finished university six years ___.',['ago','since','for'],0),
     ('She has led this team ___ two years.',['since','in','for'],2),
     ('We opened the new office ___ March.',['in','since','for'],0),
     ('He has been unemployed ___ last summer.',['for','since','ago'],1),
     ('I changed careers a long time ___.',['since','ago','during'],1),
     ('They have worked together ___ ten months.',['for','since','in'],0),
     ('I learned English ___ high school.',['during','since','ago'],0)], 12))

L.slide('s-eh','Error hunt','vocab','Error hunt',
  '<p class="instruction">Each sentence has one wrong word. Click it, then type a better word.</p>'
  + errorhunt('eh-1',[
     ('I have worked here since three years.',4,'for'),
     ('She graduated at 2018.',2,'in'),
     ('I finished my degree two years before.',6,'ago'),
     ('He has lived in Boston for 2019.',5,'since')])
  + sup('Tip: <b>for</b> = how long · <b>since</b> = from when · <b>ago</b> = how long back from now'))

# ---------- 9 SIMULATOR
L.slide('s-sim','Mini interview','speak','Mini interview: win the first impression',
  '<p class="instruction">You are in the first two minutes of an interview. Choose the best answer each time and watch the interviewer’s impression change.</p>'
  + sim(L,'sim-1','Ms. Rivera','👩‍💼',[
     ('Good morning! Please, tell me a little about yourself.',[
        ('I was born in a small town and I had a very happy childhood with my family…',1,'Too personal and too far back. Start with your present job.'),
        ('I’m a project coordinator at a travel company. I organize group tours, and I’ve been doing it for four years.',3,'Clear, short and professional. A perfect start.'),
        ('Well… I don’t know, my CV says everything.',0,'This sounds closed and unprepared.')]),
     ('Nice! Why did you apply for this position?',[
        ('I need a job, and your office is close to my house.',0,'Honest, but it does not show interest in the job.'),
        ('I saw the job ad and the salary looked good.',1,'Money is fine, but it is not the main reason to show.'),
        ('I admire your focus on sustainable travel, and I want to lead projects like that.',3,'Specific and motivated. They see you researched the company.')]),
     ('What would your colleagues say about you?',[
        ('They would say I’m calm under pressure and always willing to help.',3,'Short, positive, and believable.'),
        ('That I’m perfect and I never make mistakes.',0,'Nobody is perfect. This sounds unrealistic.'),
        ('I’m not sure. We don’t talk much.',1,'This worries the interviewer about your teamwork.')])],
     [(0.8,'⭐ Excellent! Ms. Rivera is impressed and wants to continue.'),(0.5,'👍 Good start. A few answers were too general.'),(0,'🔄 Not yet. Try again with shorter, more specific answers.')]))

# ---------- 10 PITCH + ROULETTE
L.slide('s-pitch','60-second pitch','speak','Your 60-second pitch',
  '<p class="inst-light">Press start and introduce yourself. Use <b>present → past → future</b>.</p>'
  + timer('tm-pitch', 60)
  + roulette(L,'rl-1',[
     ['Tell me about yourself.','I’m currently… Before that, I… Now I’m looking for…'],
     ['What is your current job, and what do you do every day?','I work as a… My main tasks are…'],
     ['How would you describe yourself in three words?','I’d say I’m… , … and …'],
     ['What has been the highlight of your career so far?','The highlight was when I…'],
     ['Why should we choose you?','You should choose me because…']])
  + chal('After your pitch, I will ask <b>one surprising follow-up</b> question.'))

# ---------- BUILDER
L.slide('s-build','Answer builder','speak','Build your own introduction',
  '<p class="inst-light">Write your own answer to <b>“Tell me about yourself.”</b></p>'
  + ab('L1-intro','Tell me about yourself',[
      ('1 · Present','Your job or studies now.','Frame: I’m currently working as…'),
      ('2 · Past','Experience that prepared you.','Frame: Before that, I…'),
      ('3 · Skills','What did you learn?','Frame: Those experiences taught me to…'),
      ('4 · Future','Why this job?','Frame: Now I’m looking for…')],'L1-a'))

# ---------- WRAP
L.slide('s-wrap','Lab report','review','Lab report',
  '<div class="tipbox"><h3>🧪 Today you can…</h3>• separate interview myths from facts<br>• use one story for many questions<br>• explain what the interviewer is really thinking<br>• tell your story in order: present, past, future<br>• use <b>for, since, ago, in</b> correctly</div>'
  '<p class="instruction">Which part of your introduction is strongest? Which part needs more work?</p>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> Strengths and weaknesses.</div>')

# ---------- HOMEWORK
hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option for each sentence.</p>'
  + mcq('hw1',[
     ('I have worked here',['for','since','ago'],'for','five years.'),
     ('I joined the company in',['2019','since 2019','2019 ago'],'2019','.'),
     ('We finished the project two weeks',['ago','for','since'],'ago','.'),
     ('She has been a teacher',['since','for','ago'],'since','2016.'),
     ('I',['studied','have studied','study'],'studied','marketing in 2017.'),
     ('He',['has worked','worked','works'],'has worked','here for six months now.'),
     ('Before that, I',['was working','am working','will work'],'was working','in a bank.'),
     ('Now I',['am looking','look','looked'],'am looking','for a bigger challenge.')],
     example=('I have lived here','since','2020.')))
L.slide('hw-2','HW2 – Say it','hw','Practice out loud',
  '<p class="instruction">Take your answer from the Answer Builder.</p>'
  '<div class="tipbox"><h3>🎧 Your plan for this week</h3>1. Read your introduction out loud <b>three times</b>.<br>2. Record yourself <b>once</b> and listen.<br>3. Is it <b>under one minute</b>? Does it go present → past → future?</div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
