# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(5, 'STAR Stories', 'Part 1', 'L5')
FONTS = 'family=Poppins:wght@600;700;800&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#16226B','#5B6CFF','#EAEDFF','#FFD84D',
  'radial-gradient(circle at 80% 10%, #3B4BC4 0%, #16226B 50%, #070B2B 100%)',
  pattern='radial-gradient(rgba(91,108,255,.18) 2px,transparent 2.5px), radial-gradient(rgba(255,216,77,.20) 1.5px,transparent 2px)', patsize='60px 60px, 90px 90px', fh='Poppins')

cover(L, [('⭐','top:10%;left:7%'),('🌟','top:14%;right:8%;animation-delay:-2s'),('🌠','bottom:26%;left:9%;animation-delay:-4s'),('🚀','bottom:28%;right:10%;animation-delay:-1s'),('🌙','top:46%;left:3%;animation-delay:-3s')],
      'Situation · Task · Action · Result')

L.slide('s-lead','Lead-in – Situational questions','lead','“Tell me about a time when…”',
  '<p class="instruction">These questions all ask for a <b>story from your past</b>. Which are situational (story) questions? There are 4 in total.</p>'
  + multipick('mp-sit',[
     ('Tell me about a time you helped a stressed colleague.',True),
     ('What is your favorite software?',False),
     ('Describe a situation when you missed a deadline.',True),
     ('Where did you study?',False),
     ('Give me an example of when you learned something quickly.',True),
     ('How many languages do you speak?',False),
     ('Can you recall a time you disagreed with your manager?',True),
     ('Are you available next month?',False)])
  + sup('<b>situational</b> = about a real situation · <b>recall</b> = remember · <b>disagree</b> = have a different opinion'))

def tile(label, info): return '<button class="maptile" data-info="%s" onclick="mapPick(this)">%s</button>' % (q(info), label)
L.slide('s-star','The STAR method','read','Meet the STAR method',
  '<p class="instruction">Click each letter to see the example. The question: <i>“Tell me about a time you solved a problem under pressure.”</i></p>'
  '<div class="mapwrap"><div class="mapgrid">'
  + tile('⭐ S – Situation','<b>Situation:</b> It was Saturday morning at our cafe, and the espresso machine broke with a line of 20 customers.')
  + tile('🎯 T – Task','<b>Task:</b> As the shift leader, I had to keep customers happy and keep sales going.')
  + tile('⚙️ A – Action','<b>Action:</b> I offered free filter coffee, called a repair service, and borrowed a machine from the cafe next door.')
  + tile('🏆 R – Result','<b>Result:</b> We lost only ten minutes, no customer left, and the owner gave me a bonus.')
  + '</div><div class="mapinfo">👆 Choose a letter.</div></div>'
  + sup('<b>shift leader</b> = the person in charge during a work period · <b>borrow</b> = take and give back later'))

L.slide('s-bk','Sort the story','vocab','Sort the story into STAR',
  '<p class="instruction">Put each sentence from this story into the right box.</p>'
  + buckets('bk-star',[('s','⭐ Situation'),('t','🎯 Task'),('a','⚙️ Action'),('r','🏆 Result')],[
     ('Our online store crashed on Black Friday.','s'),('Thousands of customers were waiting.','s'),
     ('I had to restore the site in two hours.','t'),('My job was to keep customers informed.','t'),
     ('I called the hosting company and moved the store to a backup server.','a'),('I posted updates every 15 minutes.','a'),
     ('The site returned in 90 minutes.','r'),('We recovered 85% of the expected sales.','r')], seed=3, cols=4, side=True))

L.slide('s-og','Order the story','vocab','Order the story',
  '<p class="instruction">Put this STAR story in the best order.</p>'
  + ordergame('og-st',[
     'During a busy week, two of our delivery drivers got sick.',
     'I was responsible for making sure that every package arrived on time.',
     'I reorganized the routes, asked two office staff to help, and called customers to explain.',
     'All packages were delivered on time, and one client wrote a thank-you letter.'], seed=6, wide=True))

L.slide('s-mc','Which part is missing?','vocab','Which part is missing?',
  '<p class="instruction">Each story is missing one STAR part. Circle the missing part.</p>'
  + mcq('mc-miss',[
     ('“Our team had 48 hours to move offices. I had to coordinate everything. I made a plan and assigned jobs.” → Missing:',['Situation','Task','Result'],'Result',''),
     ('“I had to fix a late order. I called the customer and offered a discount. She stayed with us.” → Missing:',['Situation','Task','Action'],'Situation',''),
     ('“My coworker was upset. I listened and helped her reorganize her work. She felt better.” → Missing:',['Task','Action','Result'],'Task',''),
     ('“Sales were low in March. I wanted to improve them. The result was a 15% increase.” → Missing:',['Situation','Action','Result'],'Action','')],
     example=('“A client was angry. I apologized and fixed the problem. He thanked me.” → Missing:','Task','')))

L.slide('s-gap','Connectors','vocab','Link your story',
  '<p class="instruction">Type the connector: <b>so, because, however, as a result, then, after that</b>.</p>'
  + gap('gap-c',[
     ('The delivery was late,','so','I called the customer.'),
     ('I stayed late','because','the deadline was close.'),
     ('I tried one plan. ','However',', it did not work.'),
     ('I made a new plan.','Then','I asked my team for help.'),
     ('We worked all weekend. ','As a result',', we finished on time.'),
     ('I listened carefully.','After that','I explained my idea.'),
     ('I was nervous,','but','I did my best.'),
     ('I checked the data','before','sending the report.')],
     example=('It was raining,','so','we moved the event inside.'), width=130))

L.slide('s-pron','Pronunciation','vocab','The -ed sound',
  '<p class="instruction">Past verbs end in three different sounds. Say each word, then sort it.</p>'
  + buckets('bk-ed',[('t','/t/ worked'),('d','/d/ solved'),('id','/ɪd/ needed')],[
     ('helped','t'),('fixed','t'),('stopped','t'),('changed','d'),('planned','d'),('managed','d'),('decided','id'),('wanted','id'),('started','id')], seed=2))

L.slide('s-sim','STAR interview','speak','Interview: tell me a story',
  '<p class="instruction">Choose the best answers.</p>'
  + sim(L,'sim-5','Ms. Tanaka','👩‍💼',[
     ('Tell me about a time you worked under pressure.',[
        ('Once I had a lot of work and I did it all.',1,'No details. Which situation?'),
        ('Last June, our manager left suddenly the week before a launch, and I had to run the final checks.',3,'Clear situation and task.'),
        ('I never feel pressure.',0,'Not believable.')]),
     ('What did you do?',[
        ('First I listed all urgent tasks. Then I split them with two colleagues and checked each one twice.',3,'Clear actions in order.'),
        ('We worked hard.',1,'Too vague.'),
        ('I told the others what to do.',1,'More detail needed.')]),
     ('How did it end?',[
        ('The launch happened on time, with no errors, and I was asked to lead the next one.',3,'Positive, specific result.'),
        ('It was fine.',1,'Not strong enough.'),
        ('I don’t remember.',0,'You need to remember your examples.')])],
     [(0.8,'⭐ Excellent STAR story!'),(0.5,'👍 Good, add more specific details.'),(0,'🔄 Try again: situation, task, action, result.')]))

L.slide('s-roul','Question roulette','speak','Question roulette',
  '<p class="inst-light">Answer using STAR. Aim for 90 seconds.</p>'
  + roulette(L,'rl-5',[
     ['Tell me about a time you solved a problem.','Situation: … Task: … Action: … Result: …'],
     ['Describe a time you helped a colleague.','Last year, my colleague… I…'],
     ['Tell me about a time you learned from a mistake.','I once… so I… Now I…'],
     ['Give an example of working under pressure.','The deadline was… I had to…'],
     ['Tell me about a time you disagreed with someone.','We disagreed about… I…']])
  + timer('tm-5', 90))

L.slide('s-build','Answer builder','speak','Build your own STAR story',
  '<p class="inst-light">Choose a real story from your story bank.</p>'
  + ab('L5-star','My STAR story',[
      ('S · Situation','Where and when?','Frame: Last… at my job, …'),
      ('T · Task','What was your responsibility?','Frame: I had to… / My job was to…'),
      ('A · Action','What did YOU do? (2–3 steps)','Frame: First, I… Then I… After that, I…'),
      ('R · Result','What happened? Add a number if you can.','Frame: As a result, we… I learned that…')],'L5-a'))

L.slide('s-wrap','Star report','review','Star report',
  '<div class="tipbox"><h3>⭐ Today you can…</h3>• recognize situational questions<br>• organize a story with S, T, A, R<br>• find the missing part of a story<br>• link your actions with connectors<br>• pronounce past verbs: /t/, /d/, /ɪd/</div>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> More STAR stories.</div>')

hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('hw1',[
     ('I was tired,',['so','because','however'],'so','I went to bed early.'),
     ('I stayed late',['because','so','then'],'because','the report was due.'),
     ('The first plan failed.',['However','So','Because'],'However',', the second one worked.'),
     ('We trained for weeks.',['As a result','Because','But'],'As a result',', we won.'),
     ('I called the client.',['Then','Because','So'],'Then','I sent an email.'),
     ('I made a list,',['and','because','however'],'and','I started with the urgent tasks.'),
     ('I listened first.',['After that','Because','However'],'After that','I gave my opinion.'),
     ('It was late,',['but','so','because'],'but','I kept working.')],
     example=('It was cold,','so','I wore a coat.')))
L.slide('hw-2','HW2 – Say it','hw','Practice out loud',
  '<div class="tipbox"><h3>🎧 Your plan for this week</h3>1. Tell your STAR story out loud <b>three times</b>.<br>2. Record it once. Is it under <b>two minutes</b>?<br>3. Check: <b>Does it have all four parts?</b></div>'
  + timer('tm-hw', 90) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
