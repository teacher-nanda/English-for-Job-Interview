# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(6, 'STAR Stories', 'Part 2', 'L6')
FONTS = 'family=Baloo+2:wght@500;600;700;800&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#0E4D5C','#FF6F59','#E8F8F7','#FFD166',
  'radial-gradient(circle at 20% 20%, #1C8DA3 0%, #0E4D5C 55%, #062830 100%)',
  pattern='radial-gradient(rgba(255,111,89,.12) 2px,transparent 2px)', patsize='28px 28px', fh='Baloo 2')

cover(L, [('🎭','top:10%;left:7%'),('🤝','top:14%;right:8%;animation-delay:-2s'),('🌪️','bottom:26%;left:9%;animation-delay:-4s'),('🧩','bottom:28%;right:10%;animation-delay:-1s'),('💬','top:46%;left:3%;animation-delay:-3s')],
      'Hard people, big changes, and calm, smart language.')

L.slide('s-lead','Lead-in – Blunt or diplomatic?','lead','Blunt or diplomatic?',
  '<p class="instruction">Interviewers love calm, respectful language about difficult situations. Is each sentence blunt or diplomatic? There are 4 of each.</p>'
  + flagsort('fs-dip',[
     ('He was lazy and never helped.','a'),
     ('We had different working styles, so I suggested a clear plan.','b'),
     ('My manager was a disaster.','a'),
     ('My manager and I saw some things differently, so I asked for regular feedback.','b'),
     ('The client was crazy.','a'),
     ('The client was understandably frustrated, so I listened first.','b'),
     ('Everyone ignored my idea.','a'),
     ('My idea was not chosen, but I learned how to present it better.','b')],
     ('a','💥 Blunt'),('b','🕊️ Diplomatic'))
  + sup('<b>blunt</b> = too direct, can sound rude · <b>diplomatic</b> = polite and careful · <b>frustrated</b> = annoyed because something is not working'))

L.slide('s-gap','Soft language','vocab','Soften your language',
  '<p class="instruction">Type the missing word to make each sentence sound more diplomatic.</p>'
  + gap('gap-soft',[
     ('We had a small','misunderstanding','about the deadline.'),
     ('We had different','priorities','at that time.'),
     ('I tried to see it from his','perspective','.'),
     ('We agreed to','compromise','on the schedule.'),
     ('I asked for','feedback','to improve our teamwork.'),
     ('The situation was','challenging','but not impossible.'),
     ('I stayed calm and','professional','.'),
     ('In the end, we found a','solution','that worked for everyone.')],
     example=('We had a','disagreement','about the budget.'), width=150))

L.slide('s-mind','What do they hear?','read','What does the interviewer hear?',
  '<p class="instruction">The question is: <i>“Tell me about a conflict with a coworker.”</i> Click to read the interviewer’s thoughts.</p>'
  + mind('She was impossible, so I stopped talking to her.','If conflict means silence, how will this person work in our team?')
  + mind('We disagreed about who should lead. I suggested we list each person’s strengths, and we agreed on a plan.','Calm, practical and focused on a solution. Great.')
  + mind('I never have conflicts with anyone.','Never? Either this person avoids problems or is not being honest.')
  + chal('Now tell me your own conflict story. Do not criticize the other person.'))

L.slide('s-og','Conflict story','vocab','Put the conflict story in order',
  '<p class="instruction">Put this STAR story in the best order.</p>'
  + ordergame('og-conf',[
     'Last spring, a coworker and I disagreed about how to organize our shared files.',
     'I needed to find a system that worked for both of us before a big audit.',
     'I invited her for coffee, listened to her ideas, and suggested we combine them.',
     'We created one clear system, passed the audit, and still use it today.'], seed=4, wide=True))

L.slide('s-mc','Language','vocab','Past tenses in stories',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('mc-p',[
     ('While we',['were reviewing','reviewed','review'],'were reviewing','the plan, the client called.'),
     ('I',['had','have','was having'],'had','a disagreement with a teammate last year.'),
     ('By the time I arrived, she',['had left','left','has left'],'had left','.'),
     ('I',['decided','have decided','was deciding'],'decided','to talk to her directly.'),
     ('We',['were','are','have been'],'were','under a lot of pressure back then.'),
     ('After we',['spoke','speak','have spoken'],'spoke',', things improved.'),
     ('I',['realized','realize','have realized'],'realized','I needed to listen more.'),
     ('The project',['was','is','has been'],'was','finished a week early.')],
     example=('When I','joined','the team, everything was new.')))

L.slide('s-wo','Word order workshop','vocab','Word order workshop',
  '<p class="instruction">Click the words in order.</p>'
  + wordorder('wo-6',[
     'I asked her what she needed from me.',
     'We decided to meet every Friday to share updates.',
     'Instead of arguing, I tried to understand her point of view.',
     'It was a difficult situation, but we solved it together.'],
     example='I took a deep breath and listened carefully.'))

L.slide('s-sim','Difficult situations','speak','Interview: difficult situations',
  '<p class="instruction">Choose the best answers.</p>'
  + sim(L,'sim-6','Mr. Fontaine','👨‍💼',[
     ('Tell me about a time you disagreed with a colleague.',[
        ('It happens all the time. People are difficult.',0,'Negative about other people.'),
        ('Last year a colleague and I disagreed about a deadline, so I suggested a short meeting to find a plan.',3,'Calm, specific, solution focused.'),
        ('I always agree with everyone.',1,'Not realistic.')]),
     ('How did you handle it?',[
        ('I listened first, then explained my concerns and we split the tasks.',3,'Clear steps and a result.'),
        ('I told my manager to fix it.',1,'Show what YOU did.'),
        ('I ignored it.',0,'Avoiding the problem is a red flag.')]),
     ('Tell me about a big change at work.',[
        ('When our team merged with another one, I learned the new tools in two weeks and helped others.',3,'Positive and proactive.'),
        ('I hate change.',0,'Not a good attitude.'),
        ('It was fine.',1,'Add detail.')])],
     [(0.8,'⭐ Excellent! Calm, diplomatic and clear.'),(0.5,'👍 Good, but add more detail.'),(0,'🔄 Try again: stay positive and show your actions.')]))

L.slide('s-roul','Question roulette','speak','Question roulette',
  '<p class="inst-light">Answer with the STAR method. Stay diplomatic!</p>'
  + roulette(L,'rl-6',[
     ['Tell me about a conflict with a coworker.','We disagreed about… I suggested… In the end…'],
     ['Describe a time you dealt with a difficult customer.','The customer was understandably… so I…'],
     ['Tell me about a big change you handled.','When… changed, I…'],
     ['Describe a time you received tough feedback.','My manager told me… I decided to…'],
     ['Tell me about a time you helped someone who was struggling.','A colleague was…, so I…']])
  + timer('tm-6', 90))

L.slide('s-build','Answer builder','speak','Build your own STAR story',
  '<p class="inst-light">Choose a real difficult situation. Stay diplomatic.</p>'
  + ab('L6-star','A difficult situation',[
      ('S · Situation','What was happening? Use soft language.','Frame: We had different… about…'),
      ('T · Task','What did you need to achieve?','Frame: I needed to…'),
      ('A · Action','What did YOU do?','Frame: I listened… then I suggested…'),
      ('R · Result','How did it end? What did you learn?','Frame: In the end, we… I learned that…')],'L6-a'))

L.slide('s-wrap','Report','review','Calm and clear report',
  '<div class="tipbox"><h3>🎭 Today you can…</h3>• replace blunt words with diplomatic ones<br>• tell a conflict story without criticizing<br>• use past tenses in stories<br>• talk about change in a positive way</div>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> Your CV.</div>')

hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('hw1',[
     ('We had a',['misunderstanding','mistaking','misunderstood'],'misunderstanding','about the schedule.'),
     ('I tried to see it from her',['perspective','prospect','perception'],'perspective','.'),
     ('We agreed to',['compromise','compromising','compromised'],'compromise','on the budget.'),
     ('While I',['was working','worked','work'],'was working',', the phone rang.'),
     ('After we',['talked','talk','have talked'],'talked',', everything improved.'),
     ('I asked for',['feedback','feedbacks','a feedback'],'feedback','to improve.'),
     ('It was a',['challenging','challenge','challenged'],'challenging','situation.'),
     ('In the end, we',['found','find','have found'],'found','a solution.')],
     example=('We had different','priorities','then.')))
L.slide('hw-2','HW2 – Say it','hw','Practice out loud',
  '<div class="tipbox"><h3>🎧 Your plan for this week</h3>1. Tell your difficult-situation story out loud <b>three times</b>.<br>2. Record it once. Is every sentence <b>respectful</b>?<br>3. Check: <b>Does it end with a result and a lesson?</b></div>'
  + timer('tm-hw', 90) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
