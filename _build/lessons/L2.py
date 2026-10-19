# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(2, 'Strengths &amp;', 'Weaknesses', 'L2')
FONTS = 'family=Baloo+2:wght@500;600;700;800&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#3B1F6B','#E0457B','#F6EDFF','#FFC93C',
  'radial-gradient(circle at 70% 20%, #7A35B8 0%, #3B1F6B 55%, #1E0D3C 100%)',
  pattern='radial-gradient(rgba(224,69,123,.10) 2px,transparent 2px)', patsize='26px 26px', fh='Baloo 2')

cover(L, [('🦸','top:10%;left:7%'),('💪','top:14%;right:8%;animation-delay:-2s'),('⚡','bottom:26%;left:9%;animation-delay:-4s'),('🌟','bottom:28%;right:10%;animation-delay:-1s'),('🏋️','top:46%;left:3%;animation-delay:-3s')],
      'Show your superpowers, and be smart about your kryptonite.')

# ---------- LEAD-IN
L.slide('s-lead','Lead-in – Superpower check','lead','Which superpower is yours?',
  '<p class="instruction">These six qualities are popular in job ads. Which <b>two</b> describe you best? Choose them, then tell me why.</p>'
  '<div class="twocol"><div><div class="tipbox"><h3>🦸 Superpower menu</h3>'
  '⚡ <b>Adaptable</b> – changes easily when things change<br>🧭 <b>Reliable</b> – people can always count on you<br>🎨 <b>Creative</b> – has fresh ideas<br>'
  '🤝 <b>Supportive</b> – helps the team<br>🧩 <b>Analytical</b> – looks carefully at details and data<br>🗣️ <b>Persuasive</b> – can convince others</div></div>'
  '<div><div class="say-it">Interviewers hear “I’m hard-working and motivated” all day. Be <b>specific</b>: a surprising word + a short proof makes you memorable.</div></div></div>'
  + sup('<b>count on</b> = trust · <b>fresh</b> = new and different · <b>convince</b> = make someone agree'))

L.slide('s-mem','Personality words','vocab','Find the word',
  '<p class="instruction">Complete each definition with a word from the word bank.</p>'
  '<div class="tipbox"><b>meticulous · resourceful · diplomatic · proactive · resilient · decisive</b></div>'
  + gap('gap-w',[
     ('A','meticulous','person pays attention to every small detail.'),
     ('A','resourceful','person finds clever ways to solve problems.'),
     ('A','diplomatic','person handles difficult people politely.'),
     ('A','proactive','person acts before problems appear.'),
     ('A','resilient','person recovers quickly after difficulty.')],
     example=('A','decisive','person makes good choices quickly.'), width=140))

# ---------- CLAIM vs PROOF
L.slide('s-proof','Claim vs proof','read','Claim vs proof',
  '<p class="instruction">A <b>claim</b> says what you are. <b>Proof</b> shows it. Read the two candidates. Then click to see what the interviewer thinks.</p>'
  + mind('I’m very organized.', 'Everyone says this. Can I believe it? I need an example.', '🧑 Candidate A')
  + mind('I keep one shared calendar for my team of eight, so nobody has ever missed a deadline in the last year.', 'Specific, numbers, a real result. I believe this person.', '🧑 Candidate B')
  + '<div class="tipbox"><h3>🧱 Strength formula</h3><span class="chip-a">Claim</span> + <span class="chip-b">Proof</span> + <span class="chip-c">Result</span></div>'
  + sup('<b>deadline</b> = the last day to finish something · <b>shared</b> = used by more than one person'))

L.slide('s-flags','Green flags and red flags','read','Green flag or red flag?',
  '<p class="instruction">Is each answer to “What is your weakness?” a green flag or a red flag? There are 4 of each.</p>'
  + flagsort('fs-flags',[
     ('I have no weaknesses.','a'),
     ('I used to avoid public speaking, so I joined a speaking club.','b'),
     ('I’m too honest with people.','a'),
     ('I tend to take on too much, so now I plan my week every Monday.','b'),
     ('I can’t work with anyone who is slower than me.','a'),
     ('I found spreadsheets difficult, so I finished an online course.','b'),
     ('My only weakness is that I work too hard.','a'),
     ('I get nervous before presentations, but practicing out loud helps.','b')],
     ('r','🚩 Red flag'),('g','💚 Green flag'))
  + sup('<b>weakness</b> = something you are not good at yet · <b>avoid</b> = stay away from'))

# ---------- RECIPE
L.slide('s-recipe','The weakness recipe','vocab','The weakness recipe',
  '<p class="instruction">A good weakness answer has four steps. Put this answer in the best order.</p>'
  + ordergame('og-rec',[
     'I sometimes struggle to say no when colleagues ask for help.',
     'Last spring, this meant I stayed late three nights in a row.',
     'Since then, I’ve started checking my calendar before I agree to anything.',
     'Now I help people more effectively and I finish my own work on time.'], seed=3, wide=True)
  + sup('Recipe: <b>1 real weakness → 2 small example → 3 what you do → 4 progress</b>')
  + chal('Make your own recipe. The weakness must be <b>real</b> but not essential for the job.'))

# ---------- LANGUAGE
L.slide('s-gap','Language gym','vocab','Language gym',
  '<p class="instruction">Type the missing word.</p>'
  + gap('gap-lg',[
     ('I tend','to','overthink small details.'),
     ('I used to be shy, ','but','now I speak confidently.'),
     ('I’m good','at','explaining ideas simply.'),
     ('I struggled','with','time management at first.'),
     ('To improve, I’ve','started','using a weekly plan.'),
     ('I’m getting','better','at saying no.'),
     ('Since I joined the course, I’ve become much more','confident','.'),
     ('I’m always willing','to','learn new tools.')],
     example=('I’m working','on','my presentation skills.'), width=130)
  + sup('<b>tend to</b> = usually do · <b>struggle with</b> = find difficult · <b>willing to</b> = happy to'))

L.slide('s-rf','Rapid fire','vocab','Rapid fire: choose the stronger answer',
  '<p class="instruction">Which sentence sounds better in an interview? Be quick!</p>'
  + rapidfire(L,'rf-str',[
     ('Which is better?',['I’m a perfectionist.','I sometimes spend too long on details, so I now set time limits.'],1),
     ('Which is better?',['I’m a good leader. Trust me.','I led a team of five and we finished two weeks early.'],1),
     ('Which is better?',['I’m bad at everything technical.','I’m still learning advanced Excel, and I practice twice a week.'],1),
     ('Which is better?',['I can’t work under pressure.','I used to panic under pressure, but breathing and planning help me now.'],1),
     ('Which is better?',['I’m creative and hard-working.','I’m creative: I redesigned our newsletter and clicks went up 30%.'],1),
     ('Which is better?',['I’m very flexible.','When our supplier closed, I found a new one in two days.'],1)], 14))

L.slide('s-eh','Error hunt','vocab','Error hunt',
  '<p class="instruction">Each sentence has one wrong word. Click it, then type a better word.</p>'
  + errorhunt('eh-2',[
     ('I tend to spending too long on emails.',3,'spend'),
     ('I am good in solving problems.',3,'at'),
     ('I struggled about deadlines.',2,'with'),
     ('She is very reliably and honest.',3,'reliable')])
  )

# ---------- SIM
L.slide('s-sim','Weakness interview','speak','Interview: the weakness question',
  '<p class="instruction">Face three follow-up questions. Choose your best answer.</p>'
  + sim(L,'sim-2','Mr. Okafor','👨‍💼',[
     ('What would you say is your biggest weakness?',[
        ('Chocolate. I can’t stop eating it!',1,'A joke is risky. He needs a work-related answer.'),
        ('I sometimes say yes to too many tasks, and I’ve started planning my week to manage this.',3,'Real, work-related, and shows action.'),
        ('I don’t have any.',0,'This sounds dishonest or not self-aware.')]),
     ('Can you give an example?',[
        ('Last quarter I accepted three projects at once, so I learned to check my capacity first.',3,'Specific example plus a lesson learned.'),
        ('Um… it happens often.',0,'No example. The answer feels empty.'),
        ('Once, but it was my boss’s fault.',1,'Blaming others is a red flag.')]),
     ('And what are you doing about it now?',[
        ('Nothing, it’s not really a problem.',0,'No action means no growth.'),
        ('I use a task board and I tell people honestly when I’m full.',3,'Practical, specific action.'),
        ('I try harder.',1,'Too vague. What exactly do you do?')])],
     [(0.8,'⭐ Great! Mr. Okafor sees a self-aware, honest candidate.'),(0.5,'👍 Not bad, but add more specific actions.'),(0,'🔄 Try again: real weakness, example, action.')]))

L.slide('s-roul','Question roulette','speak','Question roulette',
  '<p class="inst-light">Press the button. Answer in about 30 seconds.</p>'
  + roulette(L,'rl-2',[
     ['Describe yourself in three words, and prove one.','I’d say I’m… For example, last year I…'],
     ['What skill would you like to improve?','I’d like to improve… so I’m…'],
     ['Tell me about a mistake and what you learned.','Once I… Since then I…'],
     ['What do your friends say is your best quality?','They say I’m… because I…'],
     ['Which of your strengths fits this job best?','I think my… is perfect because…']])
  + timer('tm-sw', 30))

L.slide('s-build','Answer builder','speak','Build your own answer',
  '<p class="inst-light">Write your own answer to <b>“What are your greatest strengths and weaknesses?”</b></p>'
  + ab('L2-sw','Strengths and weaknesses',[
      ('1 · Strength','A quality useful for the job.','Frame: One of my greatest strengths is that I’m…'),
      ('2 · Proof','A real example.','Frame: For example, last year I…'),
      ('3 · Result','What happened?','Frame: As a result, we…'),
      ('4 · Weakness','Real, but not essential for the job.','Frame: I tend to… / I used to find… difficult.'),
      ('5 · Action','What do you do about it?','Frame: To improve, I started…'),
      ('6 · Progress','How are you now?','Frame: Now I… / I’m much more… since I…')],'L2-a'))

L.slide('s-wrap','Power-up report','review','Power-up report',
  '<div class="tipbox"><h3>⚡ Today you can…</h3>• use words like <b>meticulous, resourceful, resilient</b><br>• turn a claim into proof with a result<br>• spot green and red flags in answers<br>• follow the weakness recipe: weakness → example → action → progress</div>'
  '<p class="instruction">Which answer in your notebook are you proudest of? Read it to me.</p>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> Why do you want this job?</div>')

hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('hw1',[
     ('I tend',['to forget','forgetting','forget'],'to forget','small details.'),
     ('I’m still working',['on','in','at'],'on','my confidence.'),
     ('I used',['to avoid','avoiding','avoid'],'to avoid','meetings, but now I speak up.'),
     ('I struggled',['with','to','for'],'with','deadlines in my first year.'),
     ('I’m excellent',['at','in','on'],'at','organizing events.'),
     ('I’m calmer',['since','for','during'],'since','I started yoga.'),
     ('I’m',['taking','taken','take'],'taking','a course to improve.'),
     ('I’m dependable,',['so','but','although'],'so','managers give me important tasks.')],
     example=('I’m good','at','working in a team.')))
L.slide('hw-2','HW2 – Say it','hw','Practice out loud',
  '<p class="instruction">Take your answer from the Answer Builder.</p>'
  '<div class="tipbox"><h3>🎧 Your plan for this week</h3>1. Read your answer out loud <b>three times</b>.<br>2. Record yourself <b>once</b> and listen.<br>3. Ask: <b>Is my weakness real? Do I say what I do about it?</b></div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
