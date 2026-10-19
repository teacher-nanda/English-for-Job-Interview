# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(3, 'Why this job?', 'Your Road Map', 'L3')
FONTS = 'family=Nunito:wght@700;800;900&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#A8431A','#F28C28','#FFF1E0','#FFD166',
  'radial-gradient(circle at 20% 80%, #F28C28 0%, #B5451B 45%, #4A1D0C 100%)',
  pattern='repeating-linear-gradient(135deg, rgba(242,140,40,.07) 0 14px, transparent 14px 28px)', patsize='auto', fh='Nunito')

cover(L, [('🗺️','top:10%;left:7%'),('🧭','top:14%;right:8%;animation-delay:-2s'),('🚗','bottom:26%;left:9%;animation-delay:-4s'),('🏔️','bottom:28%;right:10%;animation-delay:-1s'),('🌅','top:46%;left:3%;animation-delay:-3s')],
      'Where are you going, and why is this job on your road?')

# ---------- JOB AD
L.slide('s-ad','Lead-in – Read the ad','lead','Read the job ad like a detective',
  '<div class="twocol"><div>'
  '<div class="tipbox"><h3>📋 GreenLoop Bikes</h3><b>Customer Success Specialist</b><br><br>'
  'We are a fast-growing company that repairs and resells used city bikes. We care about the planet and about our riders.<br><br>'
  '<b>You will:</b> help customers by phone and chat, solve delivery problems, and suggest ideas to improve our service.<br><br>'
  '<b>You are:</b> friendly, organized and curious. You enjoy teamwork and you have 1+ year of customer service experience.<br><br>'
  '<b>We offer:</b> training, a four-day trial period and a clear path to team leader.</div>'
  + sup('<b>resell</b> = sell again · <b>trial period</b> = the first test weeks of a new job · <b>path</b> = way forward')
  + '</div><div>'
  '<p class="instruction">Which <b>3</b> details from the ad could you mention in your answer to “Why do you want this job?”</p>'
  + multipick('mp-ad',[
     ('The company cares about the planet.',True),
     ('The ad is written in a friendly tone.',False),
     ('There is a clear path to team leader.',True),
     ('The company is in a big building.',False),
     ('You suggest ideas to improve the service.',True),
     ('The ad has a nice logo.',False)])
  + '</div></div>')

L.slide('s-bk','Three roads to “Why us?”','vocab','Three reasons to say “I want this job”',
  '<p class="instruction">The strongest answers combine three things: the <b>company</b>, the <b>role</b>, and <b>you</b>. Sort each reason into the right box.</p>'
  + buckets('bk-why',[('c','🏢 The company'),('r','🛠️ The role'),('m','🙋 Me')],[
     ('I admire your focus on sustainability','c'),('Your training program is well known','c'),('You have grown fast in two years','c'),
     ('I would solve problems every day','r'),('I would speak with customers directly','r'),('The role lets me suggest ideas','r'),
     ('I have two years in customer service','m'),('I love teamwork and helping people','m'),('I want to grow into a leadership role','m')], seed=4, side=True)
  + sup('<b>admire</b> = respect and like a lot · <b>sustainability</b> = protecting the planet for the future'))

L.slide('s-mem','Motivation phrases','vocab','Say it another way',
  '<p class="instruction">Complete each sentence with a phrase from the word bank. The meaning stays the same.</p>'
  '<div class="tipbox"><b>drawn to · aligns with · make an impact · long-term · thrive · contribute</b></div>'
  + gap('gap-m',[
     ('I’m attracted to your mission = I’m','drawn to','your mission.'),
     ('It matches my values = It','aligns with','my values.'),
     ('I want to have a real effect = I want to','make an impact','.'),
     ('for many years = for the','long-term','.'),
     ('I do very well in busy teams = I','thrive','in busy teams.')],
     example=('I can give ideas = I can','contribute','ideas.'), width=150))

L.slide('s-gap','Say it well','vocab','Say it well',
  '<p class="instruction">Type the missing word.</p>'
  + gap('gap-1',[
     ('I’m really drawn','to','your mission.'),
     ('This job matches my','skills','and my interests.'),
     ('I’d love to','contribute','to a team like yours.'),
     ('I see myself','growing','with the company.'),
     ('I’m looking forward','to','learning from your team.'),
     ('Your values','align','with mine.'),
     ('I want to make a real','impact','.'),
     ('I’m ready to take the next','step','in my career.')],
     example=('I’m excited','about','this opportunity.'), width=130))

L.slide('s-mc','Goals','vocab','Talk about your future',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('mc-g',[
     ('In five years, I',['hope to','hope','hoping'],'hope to','lead a small team.'),
     ('I’m planning',['to','for','on to'],'to','get a certificate next year.'),
     ('My goal',['is','are','be'],'is','to become a specialist.'),
     ('I’d like',['to develop','developing','develop'],'to develop','my leadership skills.'),
     ('I see myself',['becoming','become','to become'],'becoming','a manager.'),
     ('I’m',['aiming','aimed','aim'],'aiming','for a senior position.'),
     ('By then, I',['will have learned','learn','learned'],'will have learned','a lot.'),
     ('I want to',['keep','keeping','kept'],'keep','growing in this field.')],
     example=('I’m hoping','to','learn new skills.')))

L.slide('s-og','Build the answer','vocab','Build a strong “Why us?” answer',
  '<p class="instruction">Put the answer in a smooth order: <b>company → role → me → future</b>.</p>'
  + ordergame('og-why',[
     'I’ve followed GreenLoop for a year, and I admire how you give old bikes a second life.',
     'The role is exactly what I enjoy: solving problems and talking to customers.',
     'In my last job, I improved our response time by a third, so I know I can contribute quickly.',
     'In the long term, I’d love to grow into team leader with you.'], seed=8, wide=True))

L.slide('s-rf','Rapid fire','vocab','Rapid fire: smart or weak?',
  '<p class="instruction">Which reason sounds smarter in an interview? Be quick!</p>'
  + rapidfire(L,'rf-why',[
     ('Which is better?',['I need money.','I’m excited by the chance to grow in a fast-moving company.'],1),
     ('Which is better?',['Your office is close to my house.','Your recent expansion shows great opportunities.'],1),
     ('Which is better?',['I read about your sustainability program and loved it.','Everyone says you’re a good company.'],0),
     ('Which is better?',['I hope this job is easy.','I’m looking for a challenge that matches my skills.'],1),
     ('Which is better?',['This role fits my experience in customer service.','I’ve tried everything else.'],0),
     ('Which is better?',['I just saw your ad.','I was impressed by your ad, especially the training program.'],1)], 14))

L.slide('s-sim','Why us?','speak','Interview: “Why us?”',
  '<p class="instruction">Choose the best answers for the hiring manager.</p>'
  + sim(L,'sim-3','Ms. Lindgren','👩‍💼',[
     ('Why do you want to work at GreenLoop?',[
        ('I want to work anywhere that pays on time.',0,'Not motivated by the company.'),
        ('I care about sustainability, and I admire how you repair and resell bikes.',3,'Specific and sincere.'),
        ('I heard you’re growing, so it looked like a safe job.',1,'Too general.')]),
     ('Why this role in particular?',[
        ('I enjoy solving customer problems, and I’d love to suggest ideas for improvement.',3,'Role and interests connect.'),
        ('It seems easy.',0,'Never say this.'),
        ('It’s similar to my old job.',1,'Fine, but explain what you’d bring.')]),
     ('Where do you see yourself in five years?',[
        ('Growing into a team leader role here.',3,'Matches the ad’s career path.'),
        ('Running my own company.',1,'Honest, but it shows you may leave.'),
        ('No idea.',0,'No direction is a worry.')])],
     [(0.8,'⭐ Excellent! Ms. Lindgren sees a motivated, well-prepared candidate.'),(0.5,'👍 Good, but try to be more specific.'),(0,'🔄 Try again: mention the company, the role and your future.')]))

L.slide('s-roul','Question roulette','speak','Question roulette',
  '<p class="inst-light">Press the button and answer in 30 seconds.</p>'
  + roulette(L,'rl-3',[
     ['Why do you want to work for us?','I admire… because… and I’d love to…'],
     ['What attracted you to this role?','I was attracted to… because…'],
     ['Where do you see yourself in five years?','In five years, I hope to…'],
     ['What do you know about our company?','I know that you… and I like that…'],
     ['What would make you stay with us long-term?','I would stay if… I value…']])
  + timer('tm-3', 30))

L.slide('s-build','Answer builder','speak','Build your own “Why this job?” answer',
  '<p class="inst-light">Use a real job ad you like.</p>'
  + ab('L3-why','Why do you want this job?',[
      ('1 · The company','What do you admire about it?','Frame: I admire… because…'),
      ('2 · The role','What attracts you to the work?','Frame: The role of… is perfect because…'),
      ('3 · Me','Which skill or experience fits?','Frame: I have… which means I can…'),
      ('4 · Future','Where can this job take you?','Frame: In the long term, I hope to…')],'L3-a'))

L.slide('s-wrap','Road-map report','review','Road-map report',
  '<div class="tipbox"><h3>🗺️ Today you can…</h3>• read a job ad for useful details<br>• explain “Why us?” with company, role and you<br>• talk about goals with <b>I hope to / I see myself…</b><br>• say why you want to stay long-term</div>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> Your experience in the spotlight.</div>')

hwcover(L)
L.slide('hw-1','HW1 – Language check','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option.</p>'
  + mcq('hw1',[
     ('I’m drawn',['to','at','on'],'to','companies with a strong mission.'),
     ('Your values',['align','aligned','aligns'],'align','with mine.'),
     ('I’d like',['to contribute','contributing','contribute'],'to contribute','to your team.'),
     ('I hope',['to become','becoming','become'],'to become','a manager.'),
     ('I’m looking forward',['to','for','at'],'to','joining your team.'),
     ('My goal',['is','are','be'],'is','to learn quickly.'),
     ('I want to make a real',['impact','impacts','impacted'],'impact','here.'),
     ('I see myself',['growing','grow','to grow'],'growing','with the company.')],
     example=('I’m excited','about','this role.')))
L.slide('hw-2','HW2 – Research task','hw','Do your research',
  '<div class="tipbox"><h3>🔎 Detective mission</h3>Choose a real company you like.<br>1. Find <b>two facts</b> about it (news, values, products).<br>2. Find <b>one detail</b> in the job ad that excites you.<br>3. Use them in your answer. Practice it out loud <b>three times</b>.</div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
