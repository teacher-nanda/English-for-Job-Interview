# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(7, 'Your CV:', 'Own Every Line', 'L7')
FONTS = 'family=Poppins:wght@600;700;800&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#3A2A20','#D9822B','#FFF4E6','#FFD27A',
  'radial-gradient(circle at 70% 25%, #7A5439 0%, #3A2A20 55%, #1B120C 100%)',
  pattern='linear-gradient(rgba(217,130,43,.08) 1px,transparent 1px)', patsize='100% 32px', fh='Poppins')

cover(L, [('📄','top:10%;left:7%'),('🖊️','top:14%;right:8%;animation-delay:-2s'),('📎','bottom:26%;left:9%;animation-delay:-4s'),('🔍','bottom:28%;right:10%;animation-delay:-1s'),('📚','top:46%;left:3%;animation-delay:-3s')],
      'If it is on your CV, they can ask about it.')

def tile(label, info): return '<button class="maptile" data-info="%s" onclick="mapPick(this)">%s</button>' % (q(info), label)
L.slide('s-map','CV X-ray','lead','CV X-ray: what will they ask?',
  '<p class="instruction">Click each part of a CV to see a question an interviewer may ask.</p>'
  '<div class="mapwrap"><div class="mapgrid">'
  + tile('👤 Profile','<b>Question:</b> “I see you describe yourself as a team player. Can you give me an example?”')
  + tile('💼 Experience','<b>Question:</b> “Why did you leave your job in 2022?” or “What did you do at the logistics company?”')
  + tile('🎓 Education','<b>Question:</b> “Why did you choose this course?” and “How does it help you in this job?”')
  + tile('🛠️ Skills','<b>Question:</b> “You say your Excel is advanced. What is the most complex thing you have done?”')
  + tile('🏅 Achievements','<b>Question:</b> “Tell me more about this award. What did you do?”')
  + tile('🕳️ Gaps','<b>Question:</b> “What did you do between 2020 and 2021?”')
  + '</div><div class="mapinfo">👆 Choose a part of the CV.</div></div>')

L.slide('s-flag','Strong or weak?','read','Strong or weak CV line?',
  '<p class="instruction">Is each CV line strong or weak? There are 4 of each.</p>'
  + flagsort('fs-cv',[
     ('Responsible for customers.','a'),
     ('Resolved 40+ customer requests per week with a 95% satisfaction score.','b'),
     ('Good communication skills.','a'),
     ('Presented monthly results to a team of 15 managers.','b'),
     ('Helped with various projects.','a'),
     ('Led a three-person team that launched a mobile app in four months.','b'),
     ('Hard worker, team player.','a'),
     ('Reduced shipping errors by 30% by creating a new checklist.','b')],
     ('a','😐 Weak'),('b','💪 Strong')))

L.slide('s-gap','CV language','vocab','CV language',
  '<p class="instruction">Type the missing word.</p>'
  + gap('gap-cv',[
     ('I am','responsible','for the monthly budget.'),
     ('I','handled','all customer complaints.'),
     ('I have','experience','in digital marketing.'),
     ('I am','fluent','in English and Portuguese.'),
     ('I hold a','degree','in business administration.'),
     ('I','graduated','in 2018.'),
     ('I took a','break','to care for my family.'),
     ('I am','proficient','in Excel and PowerPoint.')],
     example=('I have','worked','in sales for five years.'), width=150))

L.slide('s-mc','Tenses','vocab','Which tense? Your CV tells a story',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('mc-cv',[
     ('At my current job, I',['manage','managed','was managing'],'manage','a team of six.'),
     ('At my previous job, I',['organized','organize','have organized'],'organized','weekly workshops.'),
     ('I',['have worked','worked','work'],'have worked','here since 2020.'),
     ('From 2016 to 2019, I',['studied','have studied','study'],'studied','law.'),
     ('I',['left','have left','leave'],'left','because I wanted more responsibility.'),
     ('I',['am looking','looked','look'],'am looking','for new challenges now.'),
     ('Before that, I',['had worked','work','am working'],'had worked','as a waiter.'),
     ('Since then, I',['have gained','gain','gained'],'have gained','a lot of experience.')],
     example=('In 2019, I','joined','my current company.')))

L.slide('s-og','Walk me through','vocab','“Walk me through your CV”',
  '<p class="instruction">Put this answer in a clear order.</p>'
  + ordergame('og-walk',[
     'I studied business administration, and I graduated in 2017.',
     'My first job was in a bank, where I learned how to work with clients.',
     'In 2020, I moved to my current company, where I lead the customer team.',
     'Now I want a role with more responsibility, and this position is the perfect next step.'], seed=3, wide=True))

L.slide('s-eh','Error hunt','vocab','CV error hunt',
  '<p class="instruction">Each sentence has one wrong word. Click it, then type a better word.</p>'
  + errorhunt('eh-7',[
     ('I am responsible of the budget.',3,'for'),
     ('I work here since 2020.',1,'have worked','worked'),
     ('She is fluently in French.',2,'fluent'),
     ('I graduated since 2018.',2,'in')]))

L.slide('s-mind','Tricky CV questions','read','Tricky CV questions',
  '<p class="instruction">The question: <i>“Why was your last job only six months?”</i> Click to read the thoughts.</p>'
  + mind('The company was terrible.','Blaming again. Will this person say the same about us?')
  + mind('The role changed after a reorganization, so I looked for a position that matched my skills. I learned a lot about budgets in that time.','Honest, positive, and shows learning.')
  + mind('I don’t know, it just didn’t work.','No explanation. I need more.'))

L.slide('s-sim','CV interview','speak','Interview: your CV',
  '<p class="instruction">Choose the best answers.</p>'
  + sim(L,'sim-7','Ms. Albright','👩‍💼',[
     ('I see a gap on your CV between 2020 and 2021. Can you tell me about it?',[
        ('I don’t want to talk about it.',0,'Avoiding the question hurts trust.'),
        ('I took a year to care for a family member, and I also completed an online course in project management.',3,'Honest, short, and shows growth.'),
        ('I was just relaxing.',1,'Honest but not helpful.')]),
     ('You changed careers in 2022. Why?',[
        ('I wanted to use my communication skills in a more creative area.',3,'Positive reason, clear link.'),
        ('I hated my old job.',0,'Negative.'),
        ('A friend told me to.',1,'Not convincing.')]),
     ('Which line on your CV are you proudest of?',[
        ('Leading the migration to a new system. It finished a week early and under budget.',3,'Specific and proud.'),
        ('All of it is okay.',1,'Choose one.'),
        ('Nothing really.',0,'Never say this.')])],
     [(0.8,'⭐ Excellent! You own your CV.'),(0.5,'👍 Good, but add more positive detail.'),(0,'🔄 Try again: be honest, positive and specific.')]))

L.slide('s-roul','Question roulette','speak','Question roulette',
  '<p class="inst-light">Answer about your own CV.</p>'
  + roulette(L,'rl-7',[
     ['Walk me through your CV.','I studied… Then I worked… Now I…'],
     ['Why did you leave your last job?','I left because I wanted…'],
     ['Which skill on your CV is the strongest?','My strongest skill is… For example…'],
     ['Why did you choose your field of study?','I chose it because…'],
     ['What is missing from your CV that you would like to add?','I’d like to add… because…']])
  + timer('tm-7', 60))

L.slide('s-build','Answer builder','speak','Explain a gap or a change',
  '<p class="inst-light">Choose a real career change, short job, or gap.</p>'
  + ab('L7-cv','A career question',[
      ('1 · The fact','What happened, in one calm sentence?','Frame: In 20…, I decided to…'),
      ('2 · The reason','Give a positive reason.','Frame: I wanted to…'),
      ('3 · What I gained','What did you learn or achieve?','Frame: During that time, I…'),
      ('4 · The link','How does it help this job?','Frame: That experience helps me because…')],'L7-a'))

L.slide('s-wrap','CV report','review','CV report',
  '<div class="tipbox"><h3>📄 Today you can…</h3>• predict questions from each part of your CV<br>• make weak CV lines stronger<br>• use present, past and perfect tenses<br>• explain gaps and changes positively</div>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> Company knowledge and culture.</div>')

hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('hw1',[
     ('I am',['responsible','responsibility','responsibly'],'responsible','for training.'),
     ('I',['graduated','have graduated','graduate'],'graduated','in 2019.'),
     ('I',['have worked','worked','work'],'have worked','here for four years.'),
     ('She is',['fluent','fluently','fluency'],'fluent','in Spanish.'),
     ('I hold a',['degree','diploma of','grade'],'degree','in economics.'),
     ('I',['managed','manage','have managed'],'managed','a team at my last job.'),
     ('I am',['proficient','proficiently','proficiency'],'proficient','in Excel.'),
     ('I',['left','leave','have left'],'left','my last job in March.')],
     example=('I have','experience','in sales.')))
L.slide('hw-2','HW2 – Say it','hw','Practice out loud',
  '<div class="tipbox"><h3>🎧 Your plan for this week</h3>1. Read your own CV. Mark <b>three lines</b> they may ask about.<br>2. Prepare a 30-second answer for each one.<br>3. Practice “Walk me through your CV” out loud <b>three times</b>.</div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
