# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(8, 'Company Knowledge', '& Culture', 'L8')
FONTS = 'family=Nunito:wght@700;800;900&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#1F3B73','#2FB8A0','#E7F5FF','#FFD166',
  'radial-gradient(circle at 30% 20%, #3A66C4 0%, #1F3B73 55%, #0B1836 100%)',
  pattern='radial-gradient(rgba(47,184,160,.14) 2px,transparent 2px)', patsize='30px 30px', fh='Nunito')

cover(L, [('🌍','top:10%;left:7%'),('🔎','top:14%;right:8%;animation-delay:-2s'),('🏢','bottom:26%;left:9%;animation-delay:-4s'),('☕','bottom:28%;right:10%;animation-delay:-1s'),('🤝','top:46%;left:3%;animation-delay:-3s')],
      'Do your homework, and know the unwritten rules.')

L.slide('s-lead','Lead-in – Research','lead','Research like a pro',
  '<p class="instruction">You have one hour to prepare for an interview at a company. Which <b>4</b> research actions are the most useful?</p>'
  + multipick('mp-res',[
     ('Read the “About us” page and the company values.',True),
     ('Check the company’s name on a map.',False),
     ('Search for recent news about the company.',True),
     ('Read the full job ad and highlight keywords.',True),
     ('Memorize the CEO’s birthday.',False),
     ('Look at how the company talks to customers online.',True),
     ('Count the company’s social media posts.',False),
     ('Learn the names of all employees.',False)])
  + sup('<b>values</b> = what a company believes is important · <b>keyword</b> = an important word · <b>recent</b> = not long ago'))

L.slide('s-bk','Where to look','vocab','Where do you find it?',
  '<p class="instruction">Where is the best place to find each piece of information?</p>'
  + buckets('bk-src',[('w','🌐 Company website'),('n','📰 News'),('j','📋 Job ad')],[
     ('The mission and values','w'),('A list of products and services','w'),('The company’s history','w'),
     ('A new office opening last month','n'),('A recent award or partnership','n'),('Changes in the market','n'),
     ('The main responsibilities of the role','j'),('Required skills and experience','j'),('Benefits and working hours','j')], seed=6, side=True))

L.slide('s-gap','Language','vocab','Show you did your homework',
  '<p class="instruction">Type the missing word.</p>'
  + gap('gap-hw',[
     ('I read on your website','that','you opened a new branch.'),
     ('I was impressed','by','your sustainability report.'),
     ('I noticed','that','you won an award last year.'),
     ('I came across an article','about','your expansion.'),
     ('I’m particularly interested','in','your training program.'),
     ('Your mission really','resonates','with me.'),
     ('I’ve been following your company','since','last year.'),
     ('I’d love to learn more','about','your team culture.')],
     example=('I did some','research','before today.'), width=130))

L.slide('s-flag','Culture','read','Culture check: polite or risky?',
  '<p class="instruction">In many English-speaking workplaces, is each behavior usually appropriate or risky? There are 4 of each.</p>'
  + flagsort('fs-cul',[
     ('Arrive five to ten minutes early.','a'),
     ('Ask about politics in the first minute.','b'),
     ('Shake hands firmly and smile.','a'),
     ('Check your phone during the interview.','b'),
     ('Make friendly eye contact.','a'),
     ('Talk about your salary before they ask.','b'),
     ('Send a short thank-you email afterward.','a'),
     ('Speak badly about your last boss.','b')],
     ('a','✅ Appropriate'),('b','⚠️ Risky'))
  + sup('<b>appropriate</b> = right for the situation · <b>risky</b> = might cause a problem · <b>eye contact</b> = looking at the other person'))

L.slide('s-st','Small talk','vocab','Small talk starters',
  '<p class="instruction">Put this friendly small talk at the start of an interview in a natural order.</p>'
  + ordergame('og-st',[
     'Good morning, it’s a pleasure to meet you.',
     'Thank you. It’s nice to be here. Your office is beautiful.',
     'Thanks! Did you find us easily?',
     'Yes, the directions were very clear, and the trip was easy.'], seed=2, wide=True)
  + chal('Continue the small talk with <b>two more</b> natural sentences.'))

L.slide('s-mc','Language','vocab','Polite phrases',
  '<p class="instruction">Circle the most polite option.</p>'
  + mcq('mc-pol',[
     ('',['Could you repeat that, please?','Say it again.','What?'],'Could you repeat that, please?',''),
     ('',['Would you mind explaining that?','Explain that.','I don’t get it.'],'Would you mind explaining that?',''),
     ('',['I’m afraid I don’t agree completely.','You are wrong.','No way.'],'I’m afraid I don’t agree completely.',''),
     ('',['It’s a pleasure to meet you.','Hi.','Okay, who are you?'],'It’s a pleasure to meet you.',''),
     ('',['Thank you for your time.','Thanks, bye.','Finally, it’s over.'],'Thank you for your time.',''),
     ('',['I’d like to learn more about the team.','Tell me about the team.','I want to know the team.'],'I’d like to learn more about the team.','')],
     example=('','Could you give me an example, please?','')))

L.slide('s-sim','Small talk and research','speak','Interview: show your research',
  '<p class="instruction">Choose the best answers.</p>'
  + sim(L,'sim-8','Mr. Costa','👨‍💼',[
     ('Did you have any trouble getting here today?',[
        ('No, thank you. The directions were clear, and I enjoyed the walk.',3,'Friendly and brief.'),
        ('Yes, the traffic was terrible and your street is hard to find.',1,'A little negative.'),
        ('Why do you ask?',0,'Sounds defensive.')]),
     ('What do you know about our company?',[
        ('I read that you opened a new branch last month, and I admire your focus on customer service.',3,'Specific and recent.'),
        ('Not much. I only saw the job ad.',0,'No preparation.'),
        ('You are a big company.',1,'Too general.')]),
     ('Why does our culture appeal to you?',[
        ('I like that you promote teamwork. At my last job, I enjoyed working in small groups.',3,'Links culture to experience.'),
        ('I don’t know about your culture.',0,'Prepare before!'),
        ('The salary looks good.',1,'Not about culture.')])],
     [(0.8,'⭐ Excellent! Well-researched and polite.'),(0.5,'👍 Good, but add more specific facts.'),(0,'🔄 Try again: use facts and polite language.')]))

L.slide('s-roul','Question roulette','speak','Question roulette',
  '<p class="inst-light">Answer using what you know about a real company.</p>'
  + roulette(L,'rl-8',[
     ['What do you know about our company?','I read that… I admire…'],
     ['Why do you think our values suit you?','Your value of… matches mine because…'],
     ['Who do you think our main competitors are?','I believe… and… are your main competitors.'],
     ['What do you think of our latest product or project?','I was impressed by… because…'],
     ['What would you like to know about our team?','I’d love to learn more about…']])
  + timer('tm-8', 45))

L.slide('s-build','Answer builder','speak','Your company profile',
  '<p class="inst-light">Choose a real company where you would like to work.</p>'
  + ab('L8-co','My company research',[
      ('1 · What they do','Products, services, customers.','Frame: The company…'),
      ('2 · Something recent','News, award, project.','Frame: I read that…'),
      ('3 · A value I share','Which value matches yours?','Frame: Their value of… resonates with me because…'),
      ('4 · A question I have','What would you like to learn?','Frame: I’d love to learn more about…')],'L8-a'))

L.slide('s-wrap','Culture report','review','Culture report',
  '<div class="tipbox"><h3>🌍 Today you can…</h3>• plan useful research before an interview<br>• show your homework with natural phrases<br>• spot polite and risky behavior<br>• start friendly small talk</div>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> Confidence and your questions.</div>')

hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('hw1',[
     ('I was impressed',['by','of','on'],'by','your growth.'),
     ('I noticed',['that','what','which'],'that','you opened a new store.'),
     ('I came',['across','through','on'],'across','an article about you.'),
     ('Your mission really',['resonates','resounds','repeats'],'resonates','with me.'),
     ('I’m interested',['in','on','at'],'in','your training program.'),
     ('I’ve been following you',['since','for','during'],'since','2022.'),
     ('Would you',['mind','like','care'],'mind','repeating that?'),
     ('It’s a pleasure',['to meet','meeting','meet'],'to meet','you.')],
     example=('I did some','research','first.')))
L.slide('hw-2','HW2 – Research task','hw','Research task',
  '<div class="tipbox"><h3>🔎 Your mission</h3>Choose one real company.<br>1. Write <b>three facts</b> about it.<br>2. Write <b>one value</b> you share.<br>3. Say it out loud with: <b>“I read that… I admire…”</b></div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
