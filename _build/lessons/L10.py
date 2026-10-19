# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(10, 'Mock Interview', 'Day', 'L10')
FONTS = 'family=Poppins:wght@600;700;800&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#1B1B3A','#F5B700','#FFF8DC','#FFD84D',
  'radial-gradient(circle at 50% 15%, #4A3F9F 0%, #1B1B3A 55%, #08081A 100%)',
  pattern='radial-gradient(rgba(245,183,0,.16) 2px,transparent 2.5px)', patsize='44px 44px', fh='Poppins')

cover(L, [('🎤','top:10%;left:7%'),('🏆','top:14%;right:8%;animation-delay:-2s'),('🎬','bottom:26%;left:9%;animation-delay:-4s'),('🌟','bottom:28%;right:10%;animation-delay:-1s'),('🚀','top:46%;left:3%;animation-delay:-3s')],
      'Everything you practiced, in one big interview.')

L.slide('s-recap','Lead-in – Recap','lead','Warm-up: what do you remember?',
  '<p class="instruction">Test your memory of the course. Answer at your own pace.</p>'
  + rapidfire(L,'rf-rec',[
     ('Which order works best for “Tell me about yourself”?',['Past, present, future','Present, past, future','Future, past, present'],1),
     ('What does the S in STAR mean?',['Skill','Situation','Success'],1),
     ('Which is a stronger CV line?',['Responsible for sales.','Increased sales by 20% in one year.','Helped with sales.'],1),
     ('Which weakness answer is best?',['I have none.','I work too hard.','I used to avoid speaking, so I joined a club.'],2),
     ('Which sentence is diplomatic?',['He was lazy.','We had different working styles.','He was useless.'],1),
     ('Which is a smart question for the interviewer?',['How will success be measured?','How early can I leave?','What does your company do?'],0),
     ('“I’ve worked here ___ 2019.”',['for','since','ago'],1),
     ('What should you do if you do not understand a question?',['Guess','Ask politely for clarification','Stay silent'],1)], 12))

L.slide('s-flag','Final check','read','Strong answer or weak answer?',
  '<p class="instruction">Which answers would impress an interviewer? There are 4 of each.</p>'
  + flagsort('fs-fin',[
     ('I want this job because I need money.','a'),
     ('I admire your focus on sustainability, and I can contribute from day one.','b'),
     ('I’m a perfectionist.','a'),
     ('I used to spend too long on details, so I now set time limits.','b'),
     ('My last boss was awful.','a'),
     ('I learned a lot from my last manager, and I’m ready for new challenges.','b'),
     ('I have no questions.','a'),
     ('How will success be measured in the first six months?','b')],
     ('a','👎 Weak'),('b','👏 Strong')))

L.slide('s-mc','Mixed review','vocab','Mixed language review',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('mc-mix',[
     ('I have worked here',['for','since','ago'],'for','five years.'),
     ('I tend',['to overthink','overthinking','overthink'],'to overthink','small details.'),
     ('I am responsible',['for','of','to'],'for','the team’s budget.'),
     ('While I',['was working','worked','work'],'was working',', the system crashed.'),
     ('I’m drawn',['to','at','in'],'to','your mission.'),
     ('I look forward',['to hearing','to hear','hearing'],'to hearing','from you.'),
     ('We increased sales',['by','with','at'],'by','15%.'),
     ('Could you',['repeat','repeating','to repeat'],'repeat','that, please?')],
     example=('I','graduated','in 2018.')))

L.slide('s-og','Structure','vocab','Build a full answer',
  '<p class="instruction">Put this STAR answer in order.</p>'
  + ordergame('og-fin',[
     'Last winter, our team had to launch a new service in only three weeks.',
     'I was responsible for coordinating the schedule between four departments.',
     'I created a shared plan, held short daily meetings, and solved problems as they appeared.',
     'We launched on time, and the service gained 500 customers in the first month.'], seed=9, wide=True))

L.slide('s-sim','Mock interview','speak','The mock interview: part 1',
  '<p class="instruction">Six questions. Choose the best answer each time.</p>'
  + sim(L,'sim-10','Mr. Hartley','🧑‍💼',[
     ('Good morning, and thank you for coming. Please tell me about yourself.',[
        ('I’m a coordinator in logistics. Before that I studied business, and now I’m looking for more responsibility.',3,'Present, past and future.'),
        ('I was born in 1991 and I like football.',0,'Not relevant.'),
        ('What do you want to know?',1,'Take the lead.')]),
     ('Why do you want to work here?',[
        ('I admire your focus on customer service, and my experience matches the role.',3,'Company and you.'),
        ('You are close to home.',0,'Not motivating.'),
        ('I need a change.',1,'Too vague.')]),
     ('What is your greatest strength?',[
        ('I’m resourceful. When a supplier closed, I found a new one within two days.',3,'Claim plus proof.'),
        ('I’m perfect.',0,'Unbelievable.'),
        ('I’m hard-working.',1,'Everyone says this.')]),
     ('And your greatest weakness?',[
        ('I used to say yes to everything. Now I plan my week and discuss priorities.',3,'Real, with action.'),
        ('I don’t have any.',0,'Not honest.'),
        ('I’m too nice.',1,'A common cliche.')]),
     ('Tell me about a time you handled a disagreement.',[
        ('A colleague and I disagreed about deadlines. I listened, suggested a shared plan, and we finished on time.',3,'STAR, diplomatic.'),
        ('I avoid conflict.',1,'Not an answer.'),
        ('My coworker was impossible.',0,'Blaming.')]),
     ('Do you have any questions for us?',[
        ('Yes. What are the biggest challenges for the team this year?',3,'Smart.'),
        ('No.',1,'Missed chance.'),
        ('How soon can I get a raise?',0,'Too early.')])],
     [(0.8,'🏆 Outstanding! You are ready for the real thing.'),(0.5,'👍 Very good. Review the lessons where you lost points.'),(0,'🔄 Try again, and use your notebook.')]))

L.slide('s-roul','Mock interview','speak','The mock interview: part 2 (spoken)',
  '<p class="inst-light">Now we do it out loud. Press the button for each question. I will play the interviewer.</p>'
  + roulette(L,'rl-10',[
     ['Tell me about yourself.','Present → past → future.'],
     ['Why do you want this job?','Company + role + you.'],
     ['What are your strengths and weaknesses?','Claim + proof; weakness + action.'],
     ['Tell me about your biggest achievement.','Situation, task, action, result with numbers.'],
     ['Tell me about a conflict or a difficult change.','Stay diplomatic.'],
     ['What do you know about our company?','I read that… I admire…'],
     ['Why are you leaving your current job?','Stay positive.'],
     ['Do you have any questions for us?','How will success be measured…?']])
  + timer('tm-10', 90))

L.slide('s-score','Scorecard','review','Your scorecard',
  '<p class="inst-light">After the spoken mock interview, we will write feedback together.</p>'
  + ab('L10-sc','Mock interview scorecard',[
      ('1 · What went well','Two things you did well.','Frame: I was good at…'),
      ('2 · To improve','Two things to practice.','Frame: Next time I will…'),
      ('3 · Best answer','Which answer was your best? Why?','Frame: My best answer was… because…'),
      ('4 · My action plan','What will you do before the real interview?','Frame: Before my interview, I will…')],'L10-a'))

L.slide('s-wrap','Graduation','review','🎓 Course complete!',
  '<div class="tipbox"><h3>🏆 You can now…</h3>• introduce yourself with a clear story<br>• talk about strengths and weaknesses with proof<br>• explain your motivation and goals<br>• describe achievements with numbers<br>• tell STAR stories, even about difficult situations<br>• explain your CV with confidence<br>• use company research and polite language<br>• ask smart questions and finish with confidence</div>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">🌟 <b>You are ready.</b> Breathe, smile, and tell your story.</div>')

hwcover(L, 'Final practice')
L.slide('hw-1','HW1 – Final plan','hw','Your final plan',
  '<div class="tipbox"><h3>📋 Before your real interview</h3>1. Read your Interview Notebook <b>once a day</b>.<br>2. Record your answer to <b>“Tell me about yourself.”</b><br>3. Prepare <b>three STAR stories</b> and <b>three questions</b> to ask.<br>4. Research the company for <b>30 minutes</b>.</div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
