# -*- coding: utf-8 -*-
# Support-level model sentences. Shown only when the student chooses the Support level.
# AB[(builder_key, step_number)] and RL[(roulette_id, question_number)]  (both start at 0)

AB = {
 ('L1-stories',0): 'The time I worked with two colleagues on a new price list for our customers.',
 ('L1-stories',1): 'The time I had to solve a problem with a late delivery on a Friday afternoon.',
 ('L1-stories',2): 'The time I finished a training program for new employees successfully.',

 ('L1-intro',0): 'I’m currently working as a sales assistant at a furniture store in Chicago.',
 ('L1-intro',1): 'Before that, I studied business and worked for two years in customer service.',
 ('L1-intro',2): 'Those experiences taught me to listen carefully and to stay calm with customers.',
 ('L1-intro',3): 'Now I’m looking for a role where I can help a team grow, and that’s why I applied here.',

 ('L2-sw',0): 'One of my greatest strengths is that I’m very organized.',
 ('L2-sw',1): 'For example, last year I created a weekly planner for my team of six.',
 ('L2-sw',2): 'As a result, we finished all our projects on time and nobody missed a deadline.',
 ('L2-sw',3): 'I tend to say yes to too many tasks at the same time.',
 ('L2-sw',4): 'To improve, I started checking my calendar before I accept anything new.',
 ('L2-sw',5): 'Now I’m much more realistic about my time, and I finish my own work first.',

 ('L3-why',0): 'I admire your company because you repair and resell used bikes, and that helps the planet.',
 ('L3-why',1): 'The role of customer success specialist is perfect because I love helping people solve problems.',
 ('L3-why',2): 'I have two years of customer service experience, which means I can start helping from day one.',
 ('L3-why',3): 'In the long term, I hope to grow into a team leader role with your company.',

 ('L4-ach',0): 'Last year, our team had many customer complaints about slow answers.',
 ('L4-ach',1): 'I was responsible for improving our email and chat service.',
 ('L4-ach',2): 'I designed a new set of ready-made answers and trained five colleagues to use them.',
 ('L4-ach',3): 'As a result, we reduced our answer time from two days to four hours.',

 ('L5-star',0): 'Last winter at my job, our online store stopped working during a big sale.',
 ('L5-star',1): 'My job was to keep customers informed and bring the store back quickly.',
 ('L5-star',2): 'First, I called the hosting company. Then I posted updates every 20 minutes. After that, I tested every order.',
 ('L5-star',3): 'As a result, the store was back in two hours and we kept 80% of our sales. I learned that clear communication calms people.',

 ('L6-star',0): 'We had different priorities about the order of tasks for a big client.',
 ('L6-star',1): 'I needed to find a plan that worked for both of us before the deadline.',
 ('L6-star',2): 'I listened to her ideas first, then I suggested we combine our two plans.',
 ('L6-star',3): 'In the end, we delivered on time and we still use that plan. I learned that listening first saves time.',

 ('L7-cv',0): 'In 2021, I decided to change from retail to customer service.',
 ('L7-cv',1): 'I wanted to work more with people and solve problems every day.',
 ('L7-cv',2): 'During that time, I completed a communication course and learned to use a new support system.',
 ('L7-cv',3): 'That experience helps me because I can start working with your tools immediately.',

 ('L8-co',0): 'The company repairs used bikes and sells them online to city customers.',
 ('L8-co',1): 'I read that you opened a new workshop last month.',
 ('L8-co',2): 'Their value of caring for the planet resonates with me because I cycle to work every day.',
 ('L8-co',3): 'I’d love to learn more about how your team trains new employees.',

 ('L9-q',0): 'What does a typical first month look like in this role?',
 ('L9-q',1): 'Could you tell me more about the team I would work with?',
 ('L9-q',2): 'What opportunities are there to learn new skills in this company?',
 ('L9-q',3): 'Thank you for your time. I look forward to hearing from you.',

 ('L10-sc',0): 'I was good at giving specific examples, and I stayed calm.',
 ('L10-sc',1): 'Next time I will speak a little more slowly and add more numbers.',
 ('L10-sc',2): 'My best answer was the STAR story, because it had a clear result.',
 ('L10-sc',3): 'Before my interview, I will practice my introduction three times and research the company for 30 minutes.',
}

RL = {
 ('rl-1',0): 'I’m currently a sales assistant. Before that, I studied business. Now I’m looking for a role with more responsibility.',
 ('rl-1',1): 'I work as a sales assistant. My main tasks are helping customers, organizing the shelves and answering emails.',
 ('rl-1',2): 'I’d say I’m organized, friendly and curious.',
 ('rl-1',3): 'The highlight was when I trained three new colleagues and they passed their first month with excellent results.',
 ('rl-1',4): 'You should choose me because I learn quickly, I work well in a team, and I care about customers.',

 ('rl-2',0): 'I’d say I’m reliable, creative and calm. For example, last year I found a new supplier in two days when our old one closed.',
 ('rl-2',1): 'I’d like to improve my presentation skills, so I’m practicing with short talks every week.',
 ('rl-2',2): 'Once I forgot to send an important report. Since then I use reminders for every deadline.',
 ('rl-2',3): 'They say I’m patient because I always take time to explain things to new colleagues.',
 ('rl-2',4): 'I think my organization is perfect for this job because you need someone who manages many tasks.',

 ('rl-3',0): 'I admire your focus on sustainability, and I’d love to contribute to a team with that mission.',
 ('rl-3',1): 'I was attracted to the chance to solve problems every day and to learn from experienced colleagues.',
 ('rl-3',2): 'In five years, I hope to lead a small team and train new employees.',
 ('rl-3',3): 'I know that you repair used bikes, and I like that you care about the environment.',
 ('rl-3',4): 'I would stay if I keep learning and growing. I value honest feedback and teamwork.',

 ('rl-4',0): 'My biggest achievement was reducing our answer time by 50%. I redesigned our help guide and trained the team.',
 ('rl-4',1): 'I led a project to move our files to a new system. We finished a week early.',
 ('rl-4',2): 'My main responsibilities were answering customers, updating orders, and preparing weekly reports.',
 ('rl-4',3): 'I’m proudest of training five new employees, because all of them stayed with the company.',
 ('rl-4',4): 'I’ve learned that clear communication solves most problems. For example, a short daily meeting stopped many mistakes.',

 ('rl-5',0): 'Situation: our website crashed. Task: bring it back fast. Action: I called the hosting company and updated customers. Result: it worked again in two hours.',
 ('rl-5',1): 'Last year, my colleague was behind on a report. I stayed one hour and helped her organize the data.',
 ('rl-5',2): 'I once sent an order to the wrong address, so I called the customer and fixed it the same day. Now I always check addresses twice.',
 ('rl-5',3): 'The deadline was Friday morning. I had to finish three reports, so I made a list and asked a colleague for help.',
 ('rl-5',4): 'We disagreed about the schedule. I listened to her reasons, and we agreed on a plan that worked for both of us.',

 ('rl-6',0): 'We disagreed about who should present. I suggested we list each person’s strengths. In the end, we shared the presentation.',
 ('rl-6',1): 'The customer was understandably upset about a late delivery, so I apologized, checked the order and offered a solution.',
 ('rl-6',2): 'When our team merged with another one, I learned the new tools in two weeks and helped others.',
 ('rl-6',3): 'My manager told me my reports were too long. I decided to use a short template, and now they take half the time.',
 ('rl-6',4): 'A colleague was overwhelmed, so I offered to take two of her tasks and showed her a simple planning method.',

 ('rl-7',0): 'I studied business. Then I worked in a bank for three years. Now I’m a customer service coordinator.',
 ('rl-7',1): 'I left because I wanted more responsibility and a chance to lead projects.',
 ('rl-7',2): 'My strongest skill is communication. For example, I explained a complex price change to 80 customers by phone.',
 ('rl-7',3): 'I chose it because I enjoy working with people and I wanted a career with many options.',
 ('rl-7',4): 'I’d like to add my volunteer work, because it shows that I can organize events and work with teams.',

 ('rl-8',0): 'I read that you opened a new workshop last month. I admire your focus on the environment.',
 ('rl-8',1): 'Your value of teamwork matches mine because I enjoy solving problems with colleagues.',
 ('rl-8',2): 'I believe two large bike shops and an online marketplace are your main competitors.',
 ('rl-8',3): 'I was impressed by your new repair service because it makes bikes affordable for everyone.',
 ('rl-8',4): 'I’d love to learn more about how the team shares ideas and supports each other.',

 ('rl-9',0): 'Yes, I’d like to ask how success will be measured in the first six months.',
 ('rl-9',1): 'Yes, I’d like to add that I learn quickly, and I’m excited about this opportunity.',
 ('rl-9',2): 'When I feel stressed, I make a list, take a deep breath and start with the most urgent task.',
 ('rl-9',3): 'I would politely ask, “Could you repeat that, please?” or “Do you mean…?”',
 ('rl-9',4): 'I’d like to understand more about the daily work and the biggest challenges of the team.',

 ('rl-10',0): 'I’m currently a coordinator. Before that, I studied business. Now I’m looking for more responsibility.',
 ('rl-10',1): 'I admire your focus on customer service. The role matches my experience, and I want to grow with you.',
 ('rl-10',2): 'I’m resourceful: I found a new supplier in two days. I used to say yes to everything, so now I plan my week.',
 ('rl-10',3): 'I reduced our answer time by 50%. I redesigned our guide and trained five colleagues.',
 ('rl-10',4): 'We disagreed about deadlines. I listened, suggested a shared plan, and we finished on time.',
 ('rl-10',5): 'I read that you opened a new branch, and I admire your focus on the environment.',
 ('rl-10',6): 'I’m ready for more responsibility, and I’d like a role where I can lead projects.',
 ('rl-10',7): 'How will success be measured in the first six months?',
}
