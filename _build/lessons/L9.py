# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(9, 'Confidence &', 'Your Questions', 'L9')
FONTS = 'family=Fredoka:wght@500;600;700&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#5A1A4A','#FF8A5B','#FFEFE8','#FFD84D',
  'radial-gradient(circle at 75% 20%, #A63D86 0%, #5A1A4A 55%, #2B0A24 100%)',
  pattern='radial-gradient(rgba(255,138,91,.14) 2px,transparent 2px)', patsize='32px 32px', fh='Fredoka')

cover(L, [('💬','top:10%;left:7%'),('💪','top:14%;right:8%;animation-delay:-2s'),('🌬️','bottom:26%;left:9%;animation-delay:-4s'),('🙋','bottom:28%;right:10%;animation-delay:-1s'),('📧','top:46%;left:3%;animation-delay:-3s')],
      'Stay calm, ask smart questions, and finish strong.')

L.slide('s-lead','Lead-in – Calm toolkit','lead','Your calm toolkit',
  '<p class="instruction">Which of these help you stay calm? There are 4 helpful ideas.</p>'
  + multipick('mp-calm',[
     ('Breathe slowly: in for four, out for six.',True),
     ('Drink three cups of coffee first.',False),
     ('Practice your answers out loud the day before.',True),
     ('Arrive early so you do not rush.',True),
     ('Compare yourself with other candidates.',False),
     ('Remember: it is a conversation, not a test.',True),
     ('Stay awake all night to prepare.',False),
     ('Avoid thinking about the interview at all.',False)])
  + sup('<b>breathe</b> = take air in and out · <b>rush</b> = hurry · <b>candidate</b> = a person who wants the job'))

L.slide('s-bk','Before, during, after','vocab','Before, during, or after?',
  '<p class="instruction">When is the best time for each action?</p>'
  + buckets('bk-time',[('b','🕘 Before'),('d','🎤 During'),('a','📬 After')],[
     ('Practice your answers aloud','b'),('Prepare three questions to ask','b'),('Choose your outfit','b'),
     ('Pause before you answer','d'),('Ask for clarification','d'),('Smile and make eye contact','d'),
     ('Send a thank-you email','a'),('Write notes about what went well','a'),('Follow up politely after a week','a')], seed=5, side=True))

L.slide('s-flag','Your questions','read','Smart question or weak question?',
  '<p class="instruction">At the end of the interview, they ask: “Do you have any questions for us?” Is each question smart or weak? There are 4 of each.</p>'
  + flagsort('fs-q',[
     ('How will success be measured in this role?','b'),
     ('How many vacation days do I get?','a'),
     ('What does a typical first month look like?','b'),
     ('Can I leave early on Fridays?','a'),
     ('What are the biggest challenges for this team?','b'),
     ('What does your company do?','a'),
     ('What opportunities are there to grow here?','b'),
     ('When will I get promoted?','a')],
     ('a','👎 Weak (for now)'),('b','👍 Smart')))

L.slide('s-gap','Clarify','vocab','Clarify politely',
  '<p class="instruction">Type the missing word.</p>'
  + gap('gap-cl',[
     ('Could you','repeat','that, please?'),
     ('Sorry, I didn’t','catch','that.'),
     ('Do you','mean','the first or second project?'),
     ('Just to make','sure','I understand, you are asking about teamwork?'),
     ('Could you give me an','example',', please?'),
     ('Let me','think','about that for a moment.'),
     ('That’s a','great','question.'),
     ('If I understand','correctly',', you’d like to know about my experience.')],
     example=('Could you','clarify','that, please?'), width=130))

L.slide('s-og','Email','vocab','Confirm the appointment',
  '<p class="instruction">Put this email in the correct order.</p>'
  + ordergame('og-em',[
     'Dear Ms. Patel,',
     'Thank you for inviting me to an interview next Tuesday at 10 a.m.',
     'I would like to confirm that I will be there, and I will bring a copy of my CV.',
     'Best regards, Alex'], seed=7, wide=True))

L.slide('s-wo','Word order workshop','vocab','Word order workshop',
  '<p class="instruction">Click the words in order.</p>'
  + wordorder('wo-9',[
     'Could I ask what the next steps are?',
     'Thank you for your time today.',
     'I would love to hear more about the team.',
     'Please let me know if you need anything else.'],
     example='I look forward to hearing from you.'))

L.slide('s-sim','Closing the interview','speak','Interview: finish strong',
  '<p class="instruction">Choose the best answers.</p>'
  + sim(L,'sim-9','Ms. Patel','👩‍💼',[
     ('Would you like to explain that again? I did not hear the last part.',[
        ('Of course. What I meant was that I led the project from start to finish.',3,'Calm and clear.'),
        ('I already said it.',0,'Impolite.'),
        ('Never mind.',1,'You lose the chance to explain.')]),
     ('Do you have any questions for us?',[
        ('Yes. How will success be measured in the first six months?',3,'Smart and forward-looking.'),
        ('No, I think I’m fine.',1,'Missed opportunity.'),
        ('When can I take a vacation?',0,'Not the right moment.')]),
     ('Thank you for coming in. We will contact you next week.',[
        ('Thank you for your time. I enjoyed our conversation, and I look forward to hearing from you.',3,'Polite and positive.'),
        ('Okay, bye.',1,'Too short.'),
        ('Please call me today.',0,'Too pushy.')])],
     [(0.8,'⭐ Great! You finished with confidence.'),(0.5,'👍 Good, but a stronger ending is possible.'),(0,'🔄 Try again: be polite, curious and calm.')]))

L.slide('s-roul','Question roulette','speak','Question roulette',
  '<p class="inst-light">Practice staying calm. Take a breath first!</p>'
  + roulette(L,'rl-9',[
     ['Do you have any questions for us?','I’d like to ask about… / How will…?'],
     ['Is there anything else you’d like to add?','Yes, I’d like to add that…'],
     ['How do you handle stress?','When I feel stressed, I…'],
     ['What would you do if you did not understand a question?','I would politely ask…'],
     ['Do you have any concerns about the job?','I’d like to understand more about…']])
  + timer('tm-9', 45))

L.slide('s-build','Answer builder','speak','Your three questions',
  '<p class="inst-light">Prepare smart questions for the end of the interview.</p>'
  + ab('L9-q','Questions for the interviewer',[
      ('1 · About the role','A question about daily work or success.','Frame: What does… look like?'),
      ('2 · About the team','A question about people or culture.','Frame: Could you tell me more about…?'),
      ('3 · About growth','A question about learning or the future.','Frame: What opportunities are there to…?'),
      ('4 · Closing line','A polite closing sentence.','Frame: Thank you for your time. I look forward to…')],'L9-a'))

L.slide('s-wrap','Confidence report','review','Confidence report',
  '<div class="tipbox"><h3>💪 Today you can…</h3>• use calming habits before and during an interview<br>• ask smart questions at the end<br>• clarify politely when you do not understand<br>• confirm an appointment by email</div>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> Mock Interview Day!</div>')

hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('hw1',[
     ('Could you',['repeat','repeating','to repeat'],'repeat','that, please?'),
     ('I didn’t',['catch','catched','caught'],'catch','your last words.'),
     ('Just to make',['sure','certain','safe'],'sure','I understand…'),
     ('I look forward',['to hearing','to hear','hearing'],'to hearing','from you.'),
     ('Thank you',['for','to','at'],'for','your time.'),
     ('Could I',['ask','asking','to ask'],'ask','about the next steps?'),
     ('Let me',['think','to think','thinking'],'think','about that.'),
     ('I’d like to',['confirm','confirming','confirmed'],'confirm','the appointment.')],
     example=('I’d like to','ask','a question.')))
L.slide('hw-2','HW2 – Write it','hw','Write and practice',
  '<div class="tipbox"><h3>✍️ Your plan for this week</h3>1. Write <b>three smart questions</b> in your notebook.<br>2. Write a short <b>thank-you email</b> (four sentences).<br>3. Practice your closing sentence out loud <b>three times</b>.</div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
