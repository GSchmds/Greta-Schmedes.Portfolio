import json, os
S=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(S,'..','site')
lines=open(S+'/medal_stripped.html').read().split('\n')
CSS='\n'.join(lines[7:252])
ENGINE=open(S+'/engine.js').read()

EXTRA='''
.panel .shot{background:none;border:0;padding:0}
.panel .shot img+img{margin-top:14px}
.cdesc{margin:0;line-height:1.5}
.tabicons{margin-top:18px;display:grid;gap:10px}.tabicons img{display:block;max-width:100%;height:auto;border-radius:12px}
.step-imgs img{background:none;border:0}
.step-imgs.sm img{width:auto;max-width:100%;max-height:390px}
.step-below{margin-top:22px}.step-below figure{margin:0}.step-below img{display:block;max-width:100%;height:auto;border-radius:6px}.step-below figcaption{font-size:.78rem;color:var(--ink-2);margin-top:6px}.panel .shot img{border-radius:0}
.msr-ctl{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;margin-bottom:18px}.msr-ctl input{width:min(260px,100%);accent-color:var(--ev-high)}
.msr{list-style:none;margin:0;padding:0;display:grid;gap:10px}.msr li{display:grid;grid-template-columns:minmax(120px,170px) minmax(0,1fr) 165px 100px;gap:6px 14px;align-items:center;padding:12px 0;border-top:1px solid var(--rule)}
.msr .bars{display:grid;gap:3px}.msr .bars i{display:block;height:8px;border-radius:4px}.msr .bars .o{background:var(--ink)}.msr .bars .r{background:var(--ev-high)}
.pillx{font-family:var(--f-mono);font-size:.78rem;padding:3px 10px;border-radius:99px;border:1.5px solid currentColor;white-space:nowrap}.pillx.ok{color:#1d7a2a}.pillx.no{color:#b3261e}

.cmp-imgs.eq{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start}.cmp-imgs.eq img{height:560px;width:auto;max-width:100%}.cmp-imgs.eq figcaption{margin-top:8px}
@media(max-width:640px){.cmp-imgs.eq img{height:auto;width:100%}.msr li{grid-template-columns:1fr auto}.msr .bars{grid-column:1/-1}}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .pillx.ok{color:#7ee08b}:root:not([data-theme="light"]) .pillx.no{color:#ff9b93}}
.facts dd a{color:inherit;font-weight:600;text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1.5px}.facts dd a:hover{text-decoration-thickness:3px}
#try-fig.stack{grid-template-columns:minmax(0,1fr)}
#try-fig.stack img{width:100%;height:auto}
.cap{font-size:.85rem;color:var(--ink-2);margin-top:8px}
img.wide{width:100%;height:auto;border-radius:8px;display:block}
.hero figure img{width:100%;height:auto;border-radius:8px;display:block}
.blk{display:flex;flex-direction:column;gap:20px}
.stake{display:grid;grid-template-columns:auto repeat(2,minmax(0,1fr));gap:10px}
.stake .ax{font-family:var(--f-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2);writing-mode:vertical-rl;transform:rotate(180deg);text-align:center;grid-row:1/3}
.stake .q{border:1px solid var(--rule);border-radius:8px;padding:14px;display:flex;flex-direction:column;gap:10px;background:var(--paper-2);min-width:0}
.stake .q.key{border-color:var(--ink);border-width:2px}
.stake .q h4{margin:0;font-family:var(--f-display);text-transform:uppercase;font-size:1.2rem;letter-spacing:.03em}
.stake .q p{font-size:.85rem;color:var(--ink-2)}
.stake .names{display:flex;flex-wrap:wrap;gap:6px}
.stake .names span{padding:3px 10px;border-radius:99px;background:var(--paper);border:1px solid var(--rule);font-size:.88rem}
.stake .xl{font-family:var(--f-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2);text-align:center}
.chal{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px;align-items:start;margin-top:16px}
.chal-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.chal-list button{width:100%;text-align:left;border:1.5px solid var(--rule);background:transparent;border-radius:8px;padding:10px 14px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:6px 12px;cursor:pointer}
.chal-list button[aria-pressed="true"]{border-color:var(--ink);background:var(--paper-2)}
.chal-list .meter{grid-column:1/-1}
.chal-detail{border:1px solid var(--rule);border-radius:8px;padding:20px;background:var(--paper-2);display:flex;flex-direction:column;gap:12px;min-width:0}
.chal-detail .big{font-family:var(--f-display);font-weight:700;font-size:4rem;line-height:1}
.chal-detail .big small{font-size:1.1rem;color:var(--ink-2);margin-left:6px}
.meter.lg{height:12px}
.chk{--jc:#EBCC2A;display:flex;flex-direction:column;gap:18px;border:1px solid var(--rule);border-radius:8px;padding:20px;background:var(--paper-2);margin-top:14px;max-width:760px}
.chk fieldset{border:0;padding:0;margin:0;min-width:0}
.chk legend{font-weight:600;margin-bottom:10px;padding:0}
.chk .icons{display:flex;flex-wrap:wrap;gap:8px}
.ico{display:flex;flex-direction:column;align-items:center;gap:2px;min-width:78px;padding:10px 8px;border:1.5px solid var(--rule);border-radius:8px;background:var(--paper);cursor:pointer;font-size:.8rem}
.ico[aria-pressed="true"]{border-color:var(--ink);box-shadow:inset 0 -4px 0 var(--jc)}
.chk .boxes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 18px}
.cb{display:flex;gap:10px;align-items:center;cursor:pointer}
.cb input{width:20px;height:20px;accent-color:var(--ink)}
.chk .notes{display:flex;flex-direction:column;gap:6px;font-size:.9rem}
.chk textarea{font:inherit;color:inherit;background:var(--paper);border:1.5px solid var(--rule);border-radius:8px;padding:10px;resize:vertical}
.chk .btn:not(.ghost){background:var(--ink);color:var(--paper)}
.entries{margin:16px 0 0;padding-left:0;list-style:none;display:grid;gap:8px;max-width:760px}
.entries li{border-left:4px solid var(--jc,var(--rule));padding:6px 12px;background:var(--paper-2);border-radius:0 6px 6px 0}
.qz{border:1px solid var(--rule);border-radius:8px;padding:22px;background:var(--paper-2);max-width:760px;margin-top:14px;display:flex;flex-direction:column;gap:14px}
.qbar{display:flex;gap:6px}
.qbar i{flex:1;height:10px;border-radius:5px;background:var(--rule)}
.qbar i.ok{background:#2E8B3D}
.qbar i.bad{background:var(--warn)}
.qq{font-size:1.7rem}
.opts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.opt{padding:12px 14px;border:1.5px solid var(--rule);border-radius:8px;background:var(--paper);text-align:left;cursor:pointer}
.opt:hover:not(:disabled){border-color:var(--ink)}
.opt.ok{background:#2E8B3D;color:#fff;border-color:#2E8B3D}
.opt.bad{background:var(--warn);color:#fff;border-color:var(--warn)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .opt.bad{color:#14161A}}
.cmp-imgs{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-bottom:18px}
.cmp-imgs figure{margin:0}
.cmp-imgs img{width:100%;height:auto;border-radius:8px;display:block}
@media (max-width:760px){.chal{grid-template-columns:minmax(0,1fr)}.opts,.chk .boxes{grid-template-columns:minmax(0,1fr)}.stake{grid-template-columns:auto repeat(2,minmax(0,1fr));gap:8px}.stake .q{padding:10px}}
'''

SHELL='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(title)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
%(css)s
:root{--ev-hurdle:%(c1)s; --ev-high:%(c2)s; --ev-long:%(c3)s}
%(extra)s
</style></head><body>
<div class="wrap">
<header class="top">
  <span class="mono">Greta Schmedes · Case study</span>
  <nav class="mono" aria-label="Sections">
    <a href="#brief">Brief</a><a href="#design">Design</a><a href="#try">Try it</a><a href="#build">Build</a><a href="#changes">Changes</a><a href="#tests">Tests</a>
  </nav>
</header>

<section class="hero" aria-labelledby="t">
  <div class="hero-copy">
    <div class="eyebrow mono"><span class="bars3" aria-hidden="true"><i style="background:var(--ev-hurdle);box-shadow:0 0 0 1px var(--ink-2)"></i><i style="background:var(--ev-high)"></i><i style="background:var(--ev-long)"></i></span>%(eyebrow)s</div>
    <h1 id="t">%(h1)s</h1>
    <p class="lede">%(lede)s</p>
    <dl class="facts">%(facts)s</dl>
  </div>
  <figure style="margin:0"><img src="%(hero)s" alt="%(heroalt)s"><figcaption class="cap">%(herocap)s</figcaption></figure>
</section>

<section class="sec" id="brief"><div class="lab mono">Brief</div><div class="sec-body">
  <div class="sec-head"><h2>%(bh)s</h2><p>%(bp)s</p></div>
  <div class="two"><dl class="specs">%(specs)s</dl>%(bside_html)s</div>
  <div id="blocks" class="blk" style="gap:40px"></div>
</div></section>

<section class="sec" id="design"><div class="lab mono">Design</div><div class="sec-body">
  <div class="sec-head"><h2>%(dh)s</h2><p>%(dp)s</p></div>
  <div class="tabs" role="tablist" aria-label="Design stages" id="tabs"></div>
  <div class="panel" id="panel" role="tabpanel" aria-live="polite"></div>
</div></section>

<section class="sec" id="try"><div class="lab mono">Try it</div><div class="sec-body">
  <div class="sec-head"><h2>%(th)s</h2><p>%(tp)s</p></div>
  <div id="try-body"></div>
  <div class="fig-row" id="try-fig"></div>
</div></section>

<section class="sec" id="build"><div class="lab mono">Build</div><div class="sec-body">
  <div class="sec-head"><h2>%(bsh)s</h2><p>Pick a step to see what I did and what went wrong.</p></div>
  <div class="steps"><ol class="rail" id="rail" aria-label="Steps"></ol><div class="step-body" id="step" aria-live="polite"></div></div>
</div></section>

<section class="sec" id="changes"><div class="lab mono">Changes</div><div class="sec-body">
  <div class="sec-head"><h2>%(ch)s</h2><p>%(cp)s</p></div>
  <div class="pvb" id="pvb" data-state="built">
    <div class="seg" role="radiogroup" aria-label="Compare" id="cmpSeg"></div>
    <div class="cmp-imgs" id="cmpImgs"></div>
    <div class="tbl-wrap"><table class="cmp"><thead id="cmpHead"></thead><tbody id="cmp"></tbody></table></div>
  </div>
</div></section>

<section class="sec" id="tests"><div class="lab mono">Tests</div><div class="sec-body">
  <div class="sec-head"><h2>%(tsh)s</h2><p>%(tsp)s</p></div>
  <div class="test-bar"><div class="score" id="score"></div><div class="seg" role="group" aria-label="Filter tests" id="filters"></div></div>
  <ul class="tests" id="tests-list"></ul>
</div></section>

<section class="sec" id="next"><div class="lab mono">Reflection</div><div class="sec-body">
  <div class="sec-head"><h2>What I would change</h2></div>
  <div class="cols3 imp" id="improve"></div>
  <div class="sec-head" style="margin-top:16px"><h3>What I take into UI/UX work</h3></div>
  <div class="cols3" id="takeaways"></div>
</div></section>

<footer class="foot">
  <div><p class="mono">Let's connect</p><p class="mail" id="mail">gschmedes1@gmail.com</p></div>
  <button class="btn ghost" type="button" id="copy">Copy email</button>
</footer>
</div>
<script>window.CASE=%(data)s;</script>
<script>
%(engine)s
</script>
</body></html>
'''

def facts(rows): return ''.join('<dt>%s</dt><dd>%s</dd>'%r for r in rows)
def specs(rows): return ''.join('<dt>%s</dt><dd>%s</dd>'%r for r in rows)

def build(fn,cfg,data):
    cfg=dict(cfg); cfg.setdefault('ch',''); cfg.setdefault('cp','')
    cfg['bside_html']=('<p class="muted measure">'+cfg['bside']+'</p>') if cfg.get('bside') else ''
    cfg['facts']=facts(cfg['facts']); cfg['specs']=specs(cfg['specs'])
    cfg.update(css=CSS,extra=EXTRA,engine=ENGINE,data=json.dumps(data,ensure_ascii=False))
    html=SHELL%cfg
    if 'cmp' not in data:
        import re
        html=re.sub(r'<section class="sec" id="changes">.*?</section>\n','',html,flags=re.S)
        html=html.replace('<a href="#changes">Changes</a>','')
    open(OUT+'/'+fn,'w').write(html)
    print(fn,len(html)//1024,'KB')

# ================= BROKE BLOCKER =================
bb_cfg=dict(title='Broke Blocker',c1='#653498',c2='#8338EC',c3='#AEF359',
 eyebrow='Syncasso · Financial education',h1='Broke Blocker',
 lede='A gamified money app that helps young adults avoid debt before it starts. Designed in Figma and shaped by two surveys and three expert reviews.',
 facts=[('Type','University project, Leeuwarden, 02.2025 to 04.2025'),('Client','Syncasso, a company that helps people avoid debt'),('My role','UI/UX design, mascot and badge illustration, prototyping in Figma'),('Tools','Figma, interview, persona, two surveys, paper prototype'),('Result','Mobile app prototype with challenges, badges, charts, dark mode and settings'),('Figma','<a href="https://www.figma.com/design/eWE9Hb4FvKsI6VV705dCW0/MF-APP--shared-?node-id=0-1&t=zJ5UwtqzIcOgb3iw-1" target="_blank" rel="noopener">Syncasso finance app ↗</a>')],
 hero='img/sy-challenges.png',heroalt='Two phone screens from the final design showing individual and group saving challenges with progress bars.',herocap='Final design: individual and group challenges.',
 bh='Stop debt before it starts',
 bp='Syncasso helps people avoid debt rather than manage it once it exists. They asked for a financial tool for young adults in their green and purple brand, with a transparent tone and plain language, and they left room for creative ideas.',
 specs=[('Audience','Young adults'),('Purpose','Prevent debt, not fix it'),('Brand','Green and purple, simple words'),('Feel','Engaging, with gamification and live visuals'),('Reach','The interview mentioned WhatsApp and AI chat')],
 bside='',
 dh='Five versions, one app',dp='I moved from paper to Figma in five stages and asked users and an expert to react at each one.',
 th='Explore the challenges',tp='These are the real challenges from the final screens. Choose Individual or Group, then a challenge, to see its saving range and progress.',
 bsh='Nine steps from interview to final',
  tsh='What the survey and the experts found',tsp='After the prototype was partly interactive I ran a second survey. Open a row for the detail and what I did about it.')
bb=dict(
 noimg='Interview notes were text only, so there is no photo.',
 pills=['Strong','Mixed'],
 blocks=[
  dict(type='bars',title='What young adults said about look and feel',note='First survey, before any design work. People could pick more than one answer.',polls=[
   dict(q='Which colour pair do you trust most for money?',rows=[['Navy and white',54.3,1],['Blue and white',32.6,0],['Blue and purple',23.9,0]]),
   dict(q='Which colours feel secure?',rows=[['Lime green',45.5,1],['Violet or purple',34.1,0],['Mint blue',27.3,0],['Electric blue',18.2,0]]),
   dict(q='What should the design be?',rows=[['Minimalist',41.3,1],['Modern and sleek',23.9,0]]),
   dict(q='Which mood suits it?',rows=[['Muted and chill',52.2,1],['Bold and poppin’',43.5,0]])]),
  dict(type='text',text='My persona Alex is a young adult juggling work, study and a tight budget. Alex feels the stress of limited money and would gain most from challenges, friends to compete with and charts that update in real time.'),
  dict(type='img',src='img/sy-persona.jpg',alt='Empathy map and persona sheet for Alex.',cap='The persona sheet for Alex: says, thinks, does, feels, pains and gains.')],
 des=[
  dict(k='Paper',img='img/sy-paper.jpg',alt='Seven paper prototype sketches of the app screens.',tried='Paper sketches of the core functions and the structure of the app.',said='I shared the paper version with the target group, watched how they used it and noted where they got confused.',saidLabel='What I did with it',took='The flow and the screen order, fixed before any visual work.'),
  dict(k='Low-fi',img='img/sy-paper-lf.jpg',alt='Seven grey low-fidelity wireframes of the app screens.',tried='Grey Figma wireframes for the same seven screens as the paper version. No colour, only flow.',said='The paper version had already shown where people got confused, so the wireframes only needed to carry the same structure into Figma.',saidLabel='What I did with it',took='A clean base to add content and colour to.'),
  dict(k='Mid-fi',img='img/sy-midfi.png',alt='Mid-fidelity Figma screens with purple headers on a dark canvas.',tried='Defined layouts, clear labels and one purpose per page: overview, transaction history and settings. Basic UI elements only.',said='An expert asked for euros instead of dollars, more realistic figures and stronger security. They also asked me to show fewer expenses openly and to make the app’s purpose and effect clearer.',saidLabel='What the expert said',took='Euros, realistic numbers and a more private way to show spending.'),
  dict(k='Second review',img='img/sy-iter2.png',alt='High-fidelity screens in purple and mint, two rows on a dark canvas.',tried='Same-size challenge cards, badges used more playfully, new title positions and more green to signal growth. I also tested a piggy bank in place of the battery icon and a lightly animated squirrel mascot.',said='A UI/UX expert suggested real-looking transactions instead of full bank integration, and a clean, organised home screen. They also suggested moving explanations into a separate tab.',saidLabel='What the expert said',took='Real-looking data. The team kept the battery icon and dropped the animated mascot so the app would not overwhelm people.'),
  dict(k='Final',img='img/sy-final-round.png',alt='The final screens with purple, mint and lime, plus the mascot holding a sign.',tried='A horizontal progress bar with the percentage underneath, individual and group challenges as full screens with no extra scrolling, a new badge font with percentages, and the mascot head in a corner with a small +1 animation.',said='A last expert round found the menus plain next to the badges, so I made the menus more visual.',saidLabel='What the expert said',took='A finished set of screens with quiet, optional fun.')],
 tryit=dict(type='challenges',modes=[
   dict(name='Individual',saved='€20',items=[['No-Spend Challenge',50,'€50 to €100','A month of spending only on essentials. No unnecessary purchases.'],['52-Week Challenge',78,'€1,378','Save €1 in week 1, €2 in week 2, and so on.'],['Round-Up Challenge',28,'€20 to €100','A Month of every time you make a purchase, round up to the nearest dollar and transfer the difference to savings.'],['Cash-Only Challenge',58,'€50 to €200 per week','Set a strict budget and only use cash for expenses; once it’s gone, no more spending!'],['Meal-Prep Challenge',37,'€150 to €500','Cook at home for 30 days straight instead of eating out or getting takeout.']]),
   dict(name='Group',saved='€40',items=[['Savings Race',69,'€500','Set a goal (e.g., save $500 in 3 months). Whoever reaches it first wins a free homemade dinner from the rest!'],['No-Eating-Out Challenge',30,'€100 to €400 per month','Challenge each other to avoid takeout or restaurant meals for a month. Share recipes and home-cooked meals!'],['€5 Penalty Jar',10,'€50 to €200 per month','Every time someone impulse-buys something unnecessary, they put €5 in a jar. At the end, use it for a shared goal.'],['Bill-Splitter Challenge',91,'€20 to €100 per month','If you live with roommates or family, challenge each other to lower utility bills for the next month. Whoever saves the most gets a small reward!'],['Budget Buddy Challenge',45,'€10 to €50','Pair up and hold each other accountable for a budget goal. Weekly check-ins and motivation help keep you on track!']])],
   fig=dict(img='img/sy-badges.png',alt='Six round badges for the different savings challenges in a row.',h='A badge for every challenge',p='I drew the badges so progress feels like collecting something, not like looking at a bank statement. After the last expert review each badge also shows its percentage.',stack=True)),
 steps=[
  dict(t='Interview the client',p='Syncasso explained the brand rules, how much creative freedom I had and why they work on prevention. WhatsApp and AI-driven outreach came up as ways to reach young adults. It told me the app should be preventive, simple and motivating.',snag=None,imgs=[]),
  dict(t='Meet Alex',p='I built the persona Alex from the interview and desk research. Alex made the target group concrete and pointed to gamification and real-time visuals as the features that would help most.',snag=None,imgs=[['img/sy-persona.jpg','Empathy map and persona for Alex']]),
  dict(t='Survey the look',p='A visual preferences survey set the direction: navy, mint and lime for trust, purple as a brand colour, and a balance of minimalist and structured. Users also wanted casual, clear language, not formal banking text.',snag=None,imgs=[['img/sy-palette.jpg','Colour palette chosen from the survey']]),
  dict(t='Sketch on paper',p='My group sketched the core functions on paper first, so we could test the flow without spending time on visuals. I put the same screens into grey Figma wireframes right after.',snag=None,imgs=[['img/sy-paper.jpg','Paper prototype sketches'],['img/sy-paper-lf.jpg','Grey low-fidelity wireframes in Figma']]),
  dict(t='Mid-fi and the first expert',p='The mid-fidelity version gave every page one job and clear labels. An expert reviewed it and I turned the notes into a to-do list: euros, realistic figures, stronger security and less exposed spending.',snag='The first version used dollars and unrealistic figures, which made it look like a mock-up.',imgs=[['img/sy-midfi.png','Mid-fidelity screens']]),
  dict(t='Second expert, more play',p='A UI/UX expert asked for a clean home screen and uniform challenge cards. I made all cards the same size, tried moving explanations to a tab, used badges more playfully and added green for growth.',snag='I tested a piggy bank instead of the battery icon and an animated squirrel mascot. The team decided against both.',imgs=[['img/sy-iter2.png','Second iteration screens']]),
  dict(t='Draw the mascot and badges',p='I illustrated the mascot and the challenge badges so the app would feel friendly rather than serious. The first survey on the prototype rated the mascot 4.4 out of 5.',snag='Some users said the mascot’s colours should match the widgets and the app, so I adjusted it to the app’s palette.',imgs=[['img/sy-mascot.png','The mascot, calm and cheering'],['img/sy-badges.png','Challenge badges']]),
  dict(t='Last expert round',p='The final review was about detail. I laid the progress bar out horizontally with the percentage below it, made the challenge lists full screen, updated the badge font and added percentages to the badges. The mascot became a head in the corner with a small +1.',snag=None,imgs=[['img/sy-final-round.png','Final screens'],['img/sy-mascot-flag.png','Mascot holding the +1 sign']]),
  dict(t='Test the prototype',p='A second survey went to the target group with the partly interactive prototype and the mascot. 80% rated the visual design 4 or 5, and 60% found navigation very easy. The suggestions were button feedback, hover effects, clearer widgets and a simpler sign-up.',snag='A prototype with limited interactivity made it hard for people to judge how the app would respond.',imgs=[['img/sy-signinoverview.png','Sign-in and overview screens']])],
 tests=[
  dict(c='The visual design looks good',m='Prototype survey',ok=1,res='80% rated 4 or 5',d='The overall visual design received mostly high ratings. 80% gave it a 4 or 5.'),
  dict(c='The app is easy to navigate',m='Prototype survey',ok=1,res='60% very easy',d='60% found navigation very easy. Icons, labels and placement helped people understand what things do. The answers were split between mostly and completely helpful, so there is room to improve.'),
  dict(c='Charts are easy to understand',m='Prototype survey',ok=0,res='60% rated highly',d='Line, bar and pie charts were mostly understandable, but only 60% rated them highly. Users asked for every widget, icon and button to be clearly labelled.'),
  dict(c='The mascot is liked',m='Prototype survey',ok=1,res='4.4 out of 5',d='The mascot averaged 4.4 out of 5. 60% felt it showed the friendly, approachable personality I wanted.',img='img/sy-mascot.png',alt='The mascot illustration'),
  dict(c='The mascot matches the app',m='Prototype survey',ok=0,res='Adjusted',d='Some feedback said the mascot’s theme should match the widgets and the app’s colours. I adjusted the concept to the app’s look.',pill='Fixed'),
  dict(c='Sign-up is smooth',m='Prototype survey',ok=0,res='Simplify',d='The sign-up page might need adjusting. The suggestion was to simplify onboarding to avoid early frustration.'),
  dict(c='The interactive pages explain what the app does',m='Prototype survey',ok=1,res='Most users agreed',d='Most users found that the interactive pages communicated the app’s function. Better button feedback, hover effects and animations would make it feel more responsive.')],
 improve=[['Make it feel more alive','The survey asked for better button feedback, hover effects and animations once the prototype is fully interactive. I would build those in earlier.'],['Simplify the sign-up','Onboarding was the one screen people could be frustrated by. I would test a shorter flow.']],
 take=[['Mix interviews and surveys','The interview and persona gave me empathy. The surveys fine-tuned colour, layout and interactivity. I need both.'],['Ask an expert at every fidelity','Paper, mid-fi and final each got a review, and each review changed something concrete.']])

# ================= HEALTH JOURNAL =================
hj_cfg=dict(title='Health Journal',c1='#090F39',c2='#2188BB',c3='#EBCC2A',
 eyebrow='Frisius MC · Behaviour change',h1='Health Journal',
 lede='Printable journals that help patients notice their eating habits after weight-loss surgery, written for people who may find medical text hard to read.',
 facts=[('Type','University project, Leeuwarden, 11.2025 to 01.2026'),('Client','Frisius MC Leeuwarden, bariatric care'),('My role','Journal design and prototyping in Figma, product manager for the team'),('Tools','Figma, Kanban board, stand-ups, retrospectives'),('Result','A series of three journals with a repeatable daily check-up page'),('Figma','<a href="https://www.figma.com/design/OAKk5AKzs64jycAPq3ayMB/Jounral?node-id=0-1&t=kVftgM3y585lacsj-1" target="_blank" rel="noopener">All prototypes ↗</a> · <a href="https://www.figma.com/design/QOGjcXmhA7NUOS6s0Jcu9g/Frisius-MC?node-id=0-1&t=CjoK41Iz6FB6wJ4R-1" target="_blank" rel="noopener">Final journal ↗</a>')],
 hero='img/fm-covers.png',heroalt='Covers of journals 1, 2 and 3 in the same navy and blue with a different accent colour each.',herocap='Covers of journals 1, 2 and 3.',
 bh='A journal that does not judge',
 bp='After bariatric surgery, small habits like drinking with meals or eating too fast can cause pain and setbacks. Frisius MC wanted a journal patients can fill in without stress. Many patients are between 40 and 75, often with lower education, and there is a real risk of low literacy.',
 specs=[('Audience','Bariatric patients, mostly 40 to 75 years old'),('Reading level','Plain language, low-literacy risk'),('Habits','Wait 30 minutes between food and drink, chew 20 to 30 times, no fizzy drinks'),('Tone','Supportive and reassuring, not scary'),('First goal','Noticing habits, not changing everything at once')],
 bside='Patients cannot change everything at once, so the first journal, Noticing the habit, helps them see how mood, eating and body reactions connect. The series has three journals, each with its own colour theme.',
 dh='Five versions, one daily page',dp='I went from sketch to final in about nine weeks. The client reacted to the first prototype and a patient reviewer reacted to the second.',
 th='Fill in today’s check-up',tp='This is the daily page from journal 1. Pick how you feel, tick what applies and say how your body felt after eating. Nothing leaves this page. The colour buttons show the three journals.',
 bsh='Nine steps from research to final',
 ch='Before and after patient feedback',cp='A patient reviewer, reached through the client, changed more than I expected. Switch between the two versions to see which parts moved.',
 tsh='Did it hold up?',tsp='I checked the journal against the client, a patient reviewer and my own requirements. Open a row for the detail.')
hj=dict(
 noimg='Desk work this step, so there is no photo.',
 pills=['Held up','Changed'],
 blocks=[
  dict(type='cards',title='What I saw in a real patient session',items=[['Dense diagrams lose people','When a complex diagram appeared, people tilted their heads or looked away. I chose simple icons and short prompts over diagrams.'],['Real photos hold attention','Concrete visuals from real surgery raised attention. I kept visuals concrete and recognisable.'],['Risk talk is emotional','When health risks came up, patients looked at their loved ones. The tone had to be supportive and reassuring, never fear-based.']]),
  dict(type='img',src='img/hj-observe.jpg',alt='Photos from the session with annotations, next to the client documents.',cap='Observation notes and the client documents I used as a base.')],
 des=[
  dict(k='Sketch',imgs=[['img/hj-sketch2.png','Sketch of the daily check-up page and the notes page.'],['img/hj-sketch1.png','Sketch of the welcome page and the thank-you page.']],tried='Rough sketches of one repeatable structure: a welcome page, a daily check-up, a notes page and a thank-you page. The same layout every day cuts the effort of learning it.',said='This stage was for brainstorming the structure and layout before any styling.',saidLabel='What it was for',took='The two-part daily page: check-up plus notes.'),
  dict(k='Prototype 1',imgs=[['img/hj-p1-2.png','Prototype 1: daily check-up page with colourful face stickers.'],['img/hj-p1-1.png','Prototype 1: welcome and thank-you pages.']],icons=[['img/hj-p1-icons.png','Prototype 1: the five feeling stickers.']],tried='A first Figma version without a final colour palette, with colourful face stickers for how you feel. We showed it anyway to test the strategy before the visuals.',said='The client liked the idea and said they had not thought of a journal for mood and feelings around food. Later a patient reviewer found the stickers childish, “Doodle” unserious, and the plus and minus signs insecure.',saidLabel='What people said',took='The structure. The tone had to change.'),
  dict(k='Prototype 2',imgs=[['img/hj-p2-2.png','Prototype 2: daily check-up page with outline faces.'],['img/hj-p2-1.png','Prototype 2: welcome and thank-you pages.']],icons=[['img/hj-p2-icons.png','Prototype 2: the five feeling icons as outlines.']],tried='Built in the same week as the client feedback and sent for patient testing on Friday. The colourful stickers became simple outline faces on the same layout.',said='No direct test results came back. Feedback arrived weeks later through the client from a patient reviewer.',saidLabel='What happened',took='Fast iteration under pressure.'),
  dict(k='Prototype 3',imgs=[['img/hj-p3-2.png','Prototype 3: daily check-up page with emoji and a serif heading font.'],['img/hj-p3-1.png','Prototype 3: welcome and thank-you pages.']],icons=[['img/hj-p3-icons.png','Prototype 3: the five feelings as regular emoji.']],tried='Regular emoji instead of drawn faces, and a serif font for the headings, changed after research.',said='A small external test compared the colourful stickers with regular emoji. The regular emoji felt less childish.',saidLabel='What the test said',took='Regular emoji over colourful stickers. The serif font stayed.'),
  dict(k='Final',imgs=[['img/hj-final2.png','Final daily check-up page with simple line icons.'],['img/hj-final1.png','Final welcome page and end-of-journal page.']],icons=[['img/hj-final-icons.png','Final feeling icons: good, normal, sad, angry and tired.']],tried='Changes made with patient feedback: more mature line icons, “Doodle” removed, “not applicable” added and neutral wording that lets patients reach their own insights.',said='The reviewer’s points: do not label items positive or negative, do not mark eating in a hurry as positive, remove the big versus small bites distinction and fix items sitting in the wrong row.',saidLabel='What the reviewer said',took='A journal that respects patients: neutral, simple and quick.')],
 tryit=dict(type='checkup',saved='Saved. Small steps are what matter.',
   journals=[['Journal 1','#EBCC2A'],['Journal 2','#5ECCFD'],['Journal 3','#9CDD46']],
   q1=[['Good','check'],['Normal','dash'],['Sad','drop'],['Angry','x'],['Tired','z']],
   q2=['Ate fast','Ate slow','Chewed little','Chewed a lot','Kept eating after full','Stopped when full','Did not take breaks','Took breaks'],
   q3=[['Good','check'],['Normal','dash'],['Sick','wave'],['Heartburn','flame'],['Pain','x'],['Tired','z']],
   fig=dict(img='img/hj-icons-test.png',alt='Three rows of icons: colourful face stickers, regular emoji and simple line icons.',h='Icons, tested twice',p='From top to bottom: the colourful stickers, the regular emoji and the final line icons. A small external test showed regular emojis felt less childish than the colourful stickers. After the patient reviewer’s feedback I changed the icons again to simple line icons, keeping the journal look.',stack=True)),
 steps=[
  dict(t='Read the client’s documents',p='Population data, bariatric guidelines and surgical information became the content I could not get wrong: eating pace, stopping when full, 30 minutes between food and drink, routine and consistency.',snag='At first there was too much information and no clear way to turn it into design decisions.',imgs=[]),
  dict(t='Observe a patient session',p='I sat in on a real information session. People were attentive at first, but a complex diagram made them tilt their heads or look away. Real photos raised attention. Talk of risks made people look at their loved ones.',snag=None,imgs=[['img/hj-observe.jpg','Observation photos with my notes']]),
  dict(t='Write the requirements',p='Each insight became a rule I could check: short sentences and one instruction per line, the same page every day, icons and scales instead of diagrams, quick answers with optional writing, and small daily prompts with feedback.',snag=None,imgs=[]),
  dict(t='Sketch the structure',p='In week 4 I sketched one repeatable structure: a daily check-up and space for notes. The aim was accessibility, because the same layout every day lowers the effort.',snag=None,imgs=[['img/hj-sketch2.png','Sketch: daily check-up and notes'],['img/hj-sketch1.png','Sketch: welcome and thank-you pages']]),
  dict(t='Show prototype 1',p='I built Prototype 1 in Figma without a final palette. It was visually unfinished, but we presented it to get feedback on the strategy first. The client liked the idea of a journal for mood and feelings around food.',snag='The prototype looked unfinished, so I had to explain that it was a test of the strategy, not of the visuals.',imgs=[['img/hj-p1-2.png','Prototype 1: daily check-up'],['img/hj-p1-1.png','Prototype 1: welcome and thank-you pages']]),
  dict(t='Prototype 2 in a week',p='Based on the client meeting I improved clarity and built Prototype 2 the same week. We sent it on Friday for patient testing. It showed I can prototype quickly under pressure.',snag='No direct test results came back, so there was nothing to react to for a while.',imgs=[['img/hj-p2-2.png','Prototype 2: daily check-up'],['img/hj-p2-1.png','Prototype 2: welcome and thank-you pages']]),
  dict(t='Listen to the patient reviewer',p='In week 8 a patient reviewer sent detailed feedback by email: do not label items positive or negative, it felt childish, remove the big versus small bites distinction, do not mark eating in a hurry as positive, fix items in the wrong row and add “not applicable”.',snag='The design felt childish and judged habits as good or bad, the opposite of what I wanted.',imgs=[['img/hj-p3-2.png','Prototype 3: daily check-up']]),
  dict(t='Final iteration',p='In week 9 I redesigned the icons to be more mature and rewrote content to be neutral. A small external test picked regular emojis over coloured ones, and after the reviewer’s comments I moved to simple line icons. I then extended the look into journals 2 and 3.',snag=None,imgs=[['img/hj-final2.png','Final daily check-up'],['img/hj-final1.png','Final welcome and end pages']]),
  dict(t='Run the team',p='I acted as product manager: a weekly Kanban board for priorities, stand-ups for progress and blockers, and short retrospectives. It kept the multidisciplinary team on track when the team and concept changed.',snag='Earlier feedback told me to delegate more and record decisions more formally. That stayed on my list.',imgs=[['img/hj-retro.jpg','Trello board: short retrospectives, week 8'],['img/hj-kanban.jpg','Trello board: Kanban, week 8']])],
 cmp=dict(a='Before feedback',b='After feedback',cols=['What','Before','After','Why'],
  rows=[['Icons','Colourful emoji stickers','Simple, more mature line icons','The stickers looked too childish.'],
        ['Section title','“Doodle”','Removed','“Doodle” sounds unserious.'],
        ['Rating marks','Plus and minus signs','Removed','They gave patients a sense of insecurity and black-and-white thinking.'],
        ['Wording','Items grouped as positive or negative','Neutral wording. Eating in a hurry no longer marked positive. Big versus small bites dropped.','Helps patients reach their own insights without shame.'],
        ['Answer options','Fixed answers','“Not applicable” added','Not every item applies to every patient.'],
        ['Font','First font','Font changed after research','Chosen for the target group.']],
  imgs=[['img/hj-p1-2.png','Prototype 1 daily page'],['img/hj-final2.png','Final daily page']]),
 tests=[
  dict(c='The client sees value in the concept',m='Client meeting',ok=1,res='Client liked it',d='The client had not thought of a journal for mood and feelings around food. That confirmed the concept had real value and gave me direction.'),
  dict(c='It feels respectful, not childish',m='Patient reviewer, via the client',ok=0,res='Felt childish',d='The reviewer said it felt childish. I redesigned the icons, replaced the stickers and removed “Doodle”.',pill='Changed'),
  dict(c='It does not label habits good or bad',m='Patient reviewer, via the client',ok=0,res='Plus and minus signs',d='Positive and negative framing can lead to black-and-white thinking and shame. I removed the signs and moved to neutral wording.',pill='Changed'),
  dict(c='Every question can be answered',m='Patient reviewer, via the client',ok=0,res='Missing option',d='Some items did not apply to everyone, so I added “not applicable”.',pill='Changed'),
  dict(c='Language is short and supportive',m='Checked against my requirements',ok=1,res='Met',d='The intro says “This journal is for you” and “No perfect answers, this is not a test”. Instructions are short and numbered.'),
  dict(c='The same page every day',m='Checked against my requirements',ok=1,res='Met',d='The daily check-up always has the same three questions and the same split between check-up and notes, so nobody relearns it.'),
  dict(c='It takes seconds to fill in',m='Checked against my requirements',ok=1,res='Met',d='Checkboxes and circled icons are quick. The notes area is optional and has prompts for people who want to write more.')],
 improve=[['Test tone and icons earlier','I would test wording and icons with at least one or two users before building more, to confirm the tone feels supportive and not childish or moralising.'],['Get patient results sooner','Waiting for feedback through the client cost weeks. I would plan a direct test in the first half of the project.'],['Make decisions visible','I would record who decides what, so the team depends less on me and the workflow looks more professional.']],
 take=[['Tone is part of accessibility','In healthcare, motivating does not mean playful. Sometimes it means respectful, neutral and non-judgmental.'],['Good design reduces effort','The best improvements came from making the journal simpler, clearer and more predictable.'],['Process visibility is a design skill','Showing sketches, versions and rationale made my work easier to assess and to discuss with the team.']])

# ================= FRISIAN LINK =================
fl_cfg=dict(title='Frisian Link',c1='#701509',c2='#DF6D0F',c3='#C8D300',
 eyebrow='Aeres VMBO · Social Domain Achtkarspelen Tytsjerksteradiel',h1='Frisian Link',
 lede='A safe website where students share projects about Frisian culture, take quizzes and compete as classes. The slogan is Be proud, be Frisian.',
 facts=[('Type','University project, Buitenpost and Leeuwarden, 04.2025 to 06.2025'),('Client','Aeres VMBO Leeuwarden, through a Social Domain workshop'),('My role','Team captain, interface design in Figma, front-end coding in HTML and CSS'),('Tools','Figma, HTML, CSS, Miro, Coda, MoSCoW'),('Result','Working website: pinboard home, quiz, upload, challenges and class leaderboard')],
 hero='img/fw-login.jpg',heroalt='The coded login page: the heart-and-landscape logo, the tagline Be Proud, Be Frisian, and username and password fields.',herocap='The coded login page.',
 bh='Pride without the risk',
 bp='Aeres VMBO wanted a place where students aged 12 to 16 share photos, art, poems, music and videos about Frisian culture. It had to be safe from cyberbullying, easy to use and, at first, open only to the school. The school was being renovated, so we could not meet students.',
 specs=[('Audience','Students aged 12 to 16'),('Goal','Pride in Frisian culture'),('Safety','No cyberbullying'),('Access','School only, at first'),('Time','One study period, seven weeks')],
 bside='We combined a youth survey at a Social Domain workshop with desk research on Frisian culture, teenage behaviour online and educational design. I was team captain, and we met in person every Tuesday and Thursday.',
 dh='Four decisions that shaped the site',dp='Each decision answers something the survey or the research told us. Open one to see what we tried and what we kept.',
 th='Take the quiz',tp='I coded the quiz as three questions with four answers each. With my limited JavaScript, the progress bar turns green for a right answer and red for a wrong one. These are the three Chapter 1 questions from the site, Land of Water and Survival. The answer key here is mine.',
 bsh='Eleven steps from brief to coded site',
 ch='Before and after feedback',cp='After feedback on the Figma layout I refined the coded site. Switch between the two to see what changed.',
 tsh='What the evidence says',tsp='Most of the proof comes from the workshop survey and from checking the site against the Figma design. One gap matters too. Open a row for the detail.')
fl=dict(
 noimg='No image for this step.',
 pills=['Supported','Gap'],
 blocks=[
  dict(type='bars',title='What young people at the workshop said',note='Our own survey. Percentages are shares of answers.',polls=[
   dict(q='Would you be interested in joining a challenge?',rows=[['Yes',90.9,1],['No',9.1,0]]),
   dict(q='Would competing for points appeal to you?',rows=[['Yes',81.8,1],['Maybe',9.1,0],['No',9.1,0]]),
   dict(q='Which challenge topics?',rows=[['Traditions',33.3,0],['Photography',33.3,0],['Places',33.3,0]])]),
  dict(type='stake',title='Who I had to keep close',note='I mapped power against influence to decide who needed updates and who needed my attention.',q=[
   dict(h='Keep informed',names=['Parents','Teachers'],p='Ensure ease of use, gather feedback and make the site engaging.'),
   dict(h='Minimal effort',names=['Future students'],p='Not actively involved or deeply interested in the outcome, at least not yet.'),
   dict(h='Key players',key=1,names=['Client','Development team'],p='Maximum effort. Update them regularly, involve them in decisions and prioritise their feedback.'),
   dict(h='Keep satisfied',names=['Students'],p='Occasional updates and consultation, especially for integration and educational relevance.')])],
 des=[
  dict(k='Pinboard home',img='img/fw-home.jpg',alt='The coded home page with a pinboard of student photos, search and filters.',tried='A Pinterest-inspired pinboard of student posts, with personalised fonts and background colours limited to school-approved options.',said='Young people wanted to share many kinds of content, from traditions to places and photos, and they liked visual, simple layouts.',saidLabel='Why',took='The pinboard layout, which the coded site keeps.'),
  dict(k='Safe reactions',img='img/fw-post.jpg',alt='A single post in the coded site, with the photo and its details.',tried='No comment sections. Students react with preset positive buttons, and uploads use only approved fonts and colours.',said='Privacy and cyberbullying were the main worries for the school and for the young people we asked.',saidLabel='Why',took='A positive space by design, not by moderation.'),
  dict(k='Quiz and class score',img='img/fw-quizstart.jpg',alt='The coded quiz page with a class leaderboard table.',tried='A quiz about Frisian history and culture, and a leaderboard that shows class scores instead of individual scores.',said='Most young people liked challenges and points. Class scores keep the competition friendly.',saidLabel='Why',took='Competition between classes, not between students.'),
  dict(k='Look and avatars',img='img/sd-colors.jpg',alt='Three colour theme options for the site with orange, red, lime and green.',tried='Kawaii-style animal avatars, an orange, red, lime and green palette from the school’s branding, and a heart-and-landscape logo.',said='Research on 12 to 16-year-olds suggested a colourful, playful and intuitive style.',saidLabel='Why',took='A friendly look that is easy to read for young teens.')],
 tryit=dict(type='quiz',qs=[['Why did early Frisians build terpen (artificial mounds)?',['To grow food on them','To avoid wild animals','To protect from floods','To store treasure'],2],['What was the relationship between the Frisians and the Romans?',['The Romans conquered Friesland','The Frisians and Romans traded peacefully','The Romans avoided Friesland completely','The Frisians joined the Roman army'],1],['Which natural element shaped early Frisian life?',['Mountains','Forests','The Sea','Deserts'],2]],
   fig=dict(img='img/fl-quiz-ba.jpg',alt='The quiz progress bar before answering (orange), after a right answer (green) and after a wrong answer (red).',h='Colour feedback instead of JavaScript',p='I did not know enough JavaScript to score a quiz properly, so I used what I could do in HTML and CSS: the progress bar turns green for a right answer and red for a wrong one.',stack=True)),
 steps=[
  dict(t='Map the stakeholders',p='I grouped stakeholders by power and influence. The client and development team were key players. Students needed to stay satisfied, parents and teachers kept informed, and future students got minimal effort. It showed me where to spend my time.',snag=None,imgs=[['img/fl-stake.jpg','Stakeholder tables: interests, influence, involvement']]),
  dict(t='Survey and desk research',p='We surveyed young people at a Social Domain workshop and ran desk research on Frisian culture and history, behaviour of 12 to 16-year-olds, and educational design with quizzes and leaderboards.',snag='Renovations at Aeres meant we could not speak to students, and the client was available for only one workshop.',imgs=[]),
  dict(t='Plan with MoSCoW and Coda',p='We sorted features into must, should, could and won’t have, with an owner, a target group and a target week for each. Must haves were uploads, quizzes and leaderboards. Badges and multilingual support were could haves. A full mobile app was a won’t have. Coda held notes, tasks and weekly progress.',snag=None,imgs=[['img/fl-moscow-1.jpg','Must have and should have'],['img/fl-moscow-2.jpg','Could have and won’t have']]),
  dict(t='Present progress to the group',p='Every week our team showed what we had done. Progress list from presentation 2: a survey for feedback, the workshop with the client, content for the website, contact with the school for student interviews, first prototypes and character designs. Presentation 1 introduced the concept, a space for students to share and present themselves and their art in a local historical context, and four sketched pages.',snag=None,imgs=[['img/sd-concept.jpg','Presentation 1: our concept'],['img/sd-idea-hist.jpg','Presentation 1: design idea, history and home page'],['img/sd-idea-up.jpg','Presentation 1: design idea, upload and leaderboard or quiz page']]),
  dict(t='Logo, colour and type',p='We sketched logo ideas, including frogs, cows and clogs, and settled on a heart-and-landscape mark that sits next to the Aeres MBO logo. We compared three colour themes built from orange, red, lime and green, and tested heading and body fonts in specimen sheets.',snag=None,imgs=[['img/sd-logos.jpg','Presentation 2: logo sketches and the final mark'],['img/sd-colors.jpg','Presentation 2: colour themes'],['img/sd-type.jpg','Presentation 2: typography options']]),
  dict(t='Paper to Figma',p='We split the team by strength: character design, storyline, Figma and development. The work moved from paper prototype to mid and high-fidelity Figma, and I supported the high-fidelity phase.',snag=None,imgs=[]),
  dict(t='Split the code',p='My teammate and I split the site in two halves. Mine was the homepage, quiz, quiz result, individual upload page, current, this week’s and past challenges, and the leaderboard. I matched layout, colour, type and interactions to the Figma file.',snag=None,imgs=[['img/fl-figma-challenge.jpg','Figma prototype: this week’s challenge'],['img/fl-figma-board.jpg','Figma prototype: leaderboard']]),
  dict(t='Build the quiz',p='The quiz has three questions with four answers each. A progress bar turns green for a correct answer and red for a wrong one, and a result page shows the score with options to try again or explore more.',snag='I did not know enough JavaScript to score a quiz properly, so the feedback is colour-based.',imgs=[['img/fl-quiz-ba.jpg','Quiz progress bar: before, right answer, wrong answer'],['img/fw-q1.jpg','Question 1'],['img/fw-q2.jpg','Question 2'],['img/fw-q3.jpg','Question 3']]),
  dict(t='Leaderboard, upload and challenges',p='The leaderboard shows class rankings and scores. The upload page keeps the steps simple, and challenge pages separate current, this week’s and past tasks. All pages share one structure and are built to adjust to screen size.',snag=None,imgs=[['img/fl-board-ba.jpg','Leaderboard: coded site and Figma prototype'],['img/fw-upload.jpg','Coded upload page'],['img/fw-challenges.jpg','Coded challenges page'],['img/fw-past.jpg','Past challenges'],['img/fw-result.jpg','Quiz result page']]),
  dict(t='Learn and debug',p='I used Codecademy for the basics, W3Schools for quick answers and my older brother, who works in IT, for file organisation, correct HTML structure, debugging and responsive CSS.',snag='It took a lot of time and effort to deliver everything my half needed.',imgs=[]),
  dict(t='Refine after feedback',p='I adjusted alignment, spacing and typography to match the Figma mock-ups, added visual feedback for quiz answers and improved the upload forms with categorised drop-downs and hover states.',snag=None,imgs=[])],
 cmp=dict(a='Before feedback',b='After feedback',cols=['What','Before','After','Why'],
  rows=[['Alignment and spacing','Inconsistent spacing and alignment, especially in profile sections and quiz buttons. Weak hierarchy.','Consistent padding, grid layout, structured navigation and headings.','Feedback on the Figma layout.'],
        ['Quiz','Answers without visual hints.','Options indicate right and wrong with colour cues.','Students need to see the result straight away.'],
        ['Leaderboard','Weak hierarchy between class names and scores.','Legible, with clear hierarchy between class names and scores.','Competition should be easy to read.'],
        ['Upload pages','Not yet refined.','Better button alignment and categorised drop-downs.','Clear upload steps for students.'],
        ['Interaction','No interactive visual hints.','Hover states, quiz feedback and categorised drop-downs.','Usability.'],
        ['Responsiveness','Figma frames only.','Cleaner component spacing and scalable layout elements.','The coded site had to adapt to different screens.']],
  imgs=[['img/fl-quiz-ba.jpg','Quiz page'],['img/fl-board-ba.jpg','Leaderboard: coded site and Figma prototype']]),
 tests=[
  dict(c='Young people want to join challenges',m='Workshop survey',ok=1,res='90.9% yes',d='Almost everyone we asked was interested in joining a challenge.'),
  dict(c='Competing for points appeals',m='Workshop survey',ok=1,res='81.8% yes',d='Most said competing for points appeals to them. 9.1% said maybe and 9.1% said no. That is why the leaderboard counts classes, not individuals.'),
  dict(c='The site matches the Figma design',m='Compared page by page',ok=1,res='Matches',d='The final site closely resembles the high-fidelity design: pinboard-inspired layout, buttons and interactivity, colour scheme and typography, visual clarity and consistency.',img='img/fl-final-vs-figma.jpg',alt='The coded challenges page next to the Figma prototype'),
  dict(c='The quiz gives clear feedback',m='Built and reviewed',ok=1,res='Colour cues',d='Each option shows a clear correct or incorrect state with colour.'),
  dict(c='Pages adapt to different screens',m='My own check',ok=1,res='Built to adjust',d='I built my half to adjust to screen size. I have not run a formal device test, so this is a self-check.',pill='Self-check'),
  dict(c='Students at Aeres tried it',m='Test plan',ok=0,res='Not possible',d='The school was being renovated and our request to speak to students was denied. We relied on the workshop survey, desk research and client feedback sessions.',pill='Gap')],
 improve=[['Learn JavaScript properly','The quiz shows right and wrong with colour only. With more JavaScript I would score answers, store results and update the leaderboard.'],['Test with real students','The renovation blocked direct testing. I would ask for a short on-site session earlier, even with a handful of students.'],['Plan feedback rounds in','Limited client availability meant one workshop and little feedback. I would book feedback moments at the start.']],
 take=[['Design to code teaches the details','Matching the Figma file exactly taught me about spacing, hierarchy and grids more than designing alone.'],['Lead with structure','Twice-weekly check-ins, Coda and MoSCoW kept the team focused when access to the client and students fell through.'],['Adapt when access falls through','Without direct user input I leaned on desk research and the survey, and I learned to make confident decisions with the evidence I had.']])


# ================= REPLICATE =================
rp_cfg=dict(title='Scissors Replicate',c1='#1F3D2A',c2='#3FAE3A',c3='#C9D8CF',
 eyebrow='Product Design · Fusion 360 and hands-on making',h1='Scissors Replicate',
 lede='An exact copy of a pair of Leitz scissors, built twice: as a rendered Fusion 360 model and as a hand-made foam model, then tested against the original.',
 facts=[('Type','School project, Product Design, 2021'),('Brief','Replicate project: an aesthetic model of a product I own'),('My role','CAD modelling in Fusion 360, hand-making, testing and evaluation'),('Tools','Fusion 360, foam, vice, coping saw, files, sandpaper, paint, double-sided tape, survey form'),('Result','A rendered CAD model and a painted foam replicate, tested for size, looks and feedback')],
 hero='img/rp-compare.jpg',heroalt='Three photos in a row: the original Leitz scissors, my Fusion 360 model and my finished physical replicate.',herocap='Original, CAD and physical model.',
 bh='Copy it exactly',
 bp='The brief asked for an aesthetic model: pick a product you own and replicate it as a CAD model and as a physical model, to judge its size and looks. Neither has to work. I chose Leitz scissors, with curved two-colour grips, a pivot screw and two blades.',
 specs=[('Product','Leitz scissors'),('Goal','Exact CAD and physical copy'),('Size limit','Within 2 mm'),('Software','Fusion 360'),('Tests','Size, aesthetics, ergonomics')],
 bside='I had to keep the original with me the whole time, so every shape, width and colour could be checked against it. The same brief asked me to plan three tests, run them and say how to improve.',
 dh='Where the copy matched, and where it did not',dp='Three things stood out when I compared the original, the CAD model and the physical model. Open one to see what I did and what I would change.',
 th='Check the size',tp='These are the measurements from my size experiment, in millimetres. The limit I set was 2 mm. Move the slider to see how many measurements would pass with a stricter or looser limit.',
 bsh='Nine steps from CAD to finished model',
 ch='Original against replicate',cp='This is how my replicate differs from the original, and what I would do next time. Switch between the two.',
 tsh='What the three tests found',tsp='Each test had a method and a success rule that I wrote before testing. Open a row to see the result.')
rp=dict(
 noimg='No image for this step.',
 pills=['Pass','Partly'],
 blocks=[
  dict(type='cards',title='What the brief asked for',items=[['An exact replicate','A rendered model in Fusion 360 and a physical model of a product I own. Neither has to function.'],['The same size and look','Size, scale, colour and texture should match the original.'],['Three planned tests','Size, aesthetics and ergonomics, each with a method and a success rule.']]),
  dict(type='bars',title='How six people rated the replicate',note='Rating from 1 to 10 in my survey. Success meant above 8.',polls=[dict(q='Rating of the replicate against the original',rows=[['9 out of 10',33.3,0],['10 out of 10',66.7,1]])])],
 des=[
  dict(k='CAD and physical',img='img/rp-compare.jpg',alt='The original scissors, the Fusion 360 model and the physical model side by side.',tried='A rendered Fusion 360 model with the green grips, white body, pivot screw and the Leitz logo on the blade, and a foam model painted to match.',said='Side by side, the shape and proportions of all three are very close.',saidLabel='Compared with',took='The CAD model carries the logo. The physical model does not.'),
  dict(k='Colour',img='img/rp-size.jpg',alt='The physical replicate next to the original scissors.',tried='I painted the foam white, then green and silver, using two paints I found at home that looked close to the original.',said='Four of six testers said the colour should be more accurate. My green is darker and brighter than the original.',saidLabel='Testers said',took='Next time I would mix green and yellow to get closer to the original.'),
  dict(k='Blade placement',img='img/rp-blades.jpg',alt='My drawing comparing the original and the replicate, with the blades marked.',tried='I stuck the two blades flat on top of each other.',said='Comparing the two models, I saw that the blades on the original are not stacked completely.',saidLabel='I noticed',took='I would change the measurements so the blades sit like the original.')],
 tryit=dict(type='measure',tol=2,rows=[['Height',207,206],['Left handle width',39,37],['Right handle width',35,34],['Blade height',95,90],['Blade width',15,14]],
   fig=dict(img='img/rp-size.jpg',alt='The physical replicate and the original scissors next to each other.',h='Measured against the original',p='I measured the original and the replicate and compared them. Four of five measurements were within 2 mm. The blade height was 5 mm off.',stack=False)),
 steps=[
  dict(t='Model it in Fusion 360',small=True,p='The brief asked for a rendered CAD model that matches the product in size, scale and appearance. My model has the two-colour grips, the pivot screw and the Leitz logo on the blade.',snag=None,imgs=[['img/rp-compare.jpg','Original, CAD and physical model']]),
  dict(t='Draw and cut the foam',small=True,p='I separated the original scissors and drew each piece on foam, then checked that width, height and length were the same. I put the foam in a vice and cut out the shape with a coping saw.',snag='Cutting the curves at the top was hard without cutting too much. I took my time and left a little extra to file away later.',imgs=[['img/rp-s1.jpg','Stage 1: shapes cut out of foam']]),
  dict(t='Drill starter holes',small=True,p='I drilled three holes on the right side and two on the left so the coping saw could cut the edges without damaging the parts.',snag='Taking the saw blade out and putting it back was hard at first. I worked it out by asking around and trying it myself.',imgs=[['img/rp-s2.jpg','Stage 2: drilled holes']]),
  dict(t='Mark what to remove',small=True,p='I measured the widths on the original with a ruler, marked them on the foam, joined the dots and scribbled out the foam to remove. I also marked small foam blocks for the three screws, cutting one block in half to get the third.',snag=None,imgs=[['img/rp-s3.jpg','Stage 3: measured and marked foam']]),
  dict(t='Cut the shape and the screws',small=True,p='I cut away the marked parts with the coping saw, then cut and filed the screws.',snag='I cut the left blade on the wrong side and had to break it off and stick it back on at the end. My first screw lost too much when I filed it. On the second try I stopped in time.',imgs=[['img/rp-s4.jpg','Stage 4: cut handles and blades']],below=[['img/rp-screws.jpg','First and second screw attempts']]),
  dict(t='File and sand',small=True,p='I used a file for the big pieces and sandpaper for detail, then drew pencil lines to show where each colour would go.',snag='The top bit was too tight for the file. I tore a small piece of sandpaper and smoothed it by hand.',imgs=[['img/rp-s5.jpg','Stage 5: filed and sanded parts']]),
  dict(t='Paint it white',small=True,p='I painted the whole model white in layers so none of the green foam showed through.',snag='The paint covered my pencil marks, so I had to measure and draw the green areas again.',imgs=[['img/rp-s6.jpg','Stage 6: white base coat']]),
  dict(t='Paint green and silver',small=True,p='I looked for paints at home that matched the original, picked a green and a silver, and used a fine brush for straight lines without paint spilling over.',snag=None,imgs=[['img/rp-s7.jpg','Stage 7: green and silver']]),
  dict(t='Stick it together',small=True,p='I tested double-sided tape on two spare foam pieces first, then used it for the real model: handles, then the blade on top, then the screws.',snag='The smallest screw would not stick at first. It worked after a few tries.',imgs=[['img/rp-s8.jpg','Stage 8: finished model']])],
 cmp=dict(a='Original',b='Replicate',cols=['What','Original','Replicate','Next time'],
  rows=[['Colour','Softer yellow-green grips.','A darker, brighter green.','Mix green and yellow to match.'],
        ['Blade placement','The blades are not stacked completely.','I stuck the blades flat on top of each other.','Change the measurements to match.'],
        ['Logo','Leitz titanium logo on the blade.','The logo is missing from the physical model.','List the important details before building.'],
        ['Height','20.7 cm','20.6 cm','Within the limit.'],
        ['Blade height','9.5 cm','9 cm','The one measurement outside the limit.']],
  eq=True,imgs=[['img/rp-size.jpg','Replicate and original'],['img/rp-blades.jpg','My drawing of the differences']]),
 tests=[
  dict(c='The size matches the original',m='Experiment',ok=1,res='4 of 5',d='I measured both models. Four of five measurements were within the limit I set. Blade height was 5 mm off (9.5 cm against 9 cm). The others were 1 or 2 mm off.',img='img/rp-size.jpg',alt='The physical replicate next to the original.'),
  dict(c='It looks like the original',m='Field test',ok=1,res='9 and 10',d='Six people rated the replicate from 1 to 10. Two gave a 9 and four gave a 10, above the 8 I needed.',img='img/rp-poll.jpg',alt='Bar chart of six ratings: two nines and four tens.'),
  dict(c='It holds up to expert feedback',m='Expert appraisal',ok=1,res='2 kinds',d='My rule was that more than two improvements would be a fail. Six people gave two kinds of feedback: four said the colour could be more accurate and one asked for a change to the blades. One found nothing to improve.',img='img/rp-feedback.jpg',alt='Written feedback from six people.')],
 improve=[['Match the colour','I would mix green and yellow to get closer to the original grips.'],['Place the blades like the original','The original blades are not stacked completely. I would change my measurements to match.'],['Keep a checklist of details','I forgot the Leitz logo on the physical model. Before building I would list every detail that has to be included.']],
 take=[['Slow cutting beats force','Cutting the blades without pushing hard kept them from breaking off, and filing a little at a time saved my screws.'],['Test small first','Trying the tape on spare foam showed me how I would stick the real pieces together.'],['Write the details down','Both my missing logo and the blade placement came from details I did not list at the start.']])

build('case-broke-blocker.html',bb_cfg,bb)
build('case-replicate.html',rp_cfg,rp)
build('case-health-journal.html',hj_cfg,hj)
build('case-frisian-link.html',fl_cfg,fl)
