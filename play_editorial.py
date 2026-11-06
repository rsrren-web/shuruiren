"""Editorial presentation using the live projects' own interface captures."""
from html import escape

COPY = {
 'period': [
  ('hero','A little closer to yourself.','和自己的节奏，靠近一点。'),
  ('intro','A daily companion for noticing patterns in your body and your everyday life. Cycle information, feelings and routines share one quiet space.','一个观察身体与日常变化的小工具。把周期、感受与生活习惯放在同一个安静的空间里。'),
  ('idea','Everyday observations, connected.','让日常的细节，彼此连接。'),
  ('idea_body','A cycle is only part of the picture. Mood, energy, sleep and activity add context. The app brings these observations together through Today, Calendar and Trends.','周期只是身体状态的一部分。情绪、精力、睡眠和活动让记录有了更多上下文。「今天」「日历」和「趋势」把这些观察连接起来。'),
  ('detail','Start with how you feel.','从今天的感受开始。'),
  ('detail_body','An emoji-led mood selector gives the daily record a clear starting point. Energy and stress follow as separate ratings, keeping different kinds of observations distinct.','用表情和短标签作为每日记录的入口。精力与压力分别评分，让不同的感受各有位置。'),
  ('flow1','Notice','观察'),('flow2','Record','记录'),('flow3','Reflect','回看'),
  ('flowbody1','Start with the Today view.','从「今天」了解当前状态。'),('flowbody2','Move through grouped daily observations.','按分组填写日常感受。'),('flowbody3','Explore calendar and trend views.','通过日历与趋势回看变化。'),
  ('screen','Room for the everyday.','给每天的感受，留一个位置。'),
  ('screen_body','The daily form separates state, activity and social life, sleep and digestion, pain and physical sensations into navigable groups.','每日表单将状态、活动社交、睡眠排便、疼痛和体感拆成可导航的分组。'),
  ('end','Make space for a daily check-in.','留一点时间，关心自己。'),
 ],
 'wenyi': [
  ('hero','An old text. A new encounter.','古老的文字，新的相遇。'),
  ('intro','An interactive reading of the I Ching: ask a question, explore a hexagram, or follow your curiosity through a library of sixty-four possibilities.','把《易经》变成一次可以探索的阅读：带着问题起卦，查看一卦，或在六十四卦中随意漫游。'),
  ('idea','A space between asking and exploring.','在提问与探索之间。'),
  ('idea_body','Wenyi offers two ways into the same body of text: a question-led random selection, and a browsable hexagram library. Both lead into a shared reading experience.','问易提供两条进入文本的路径：带着问题随机起卦，或直接浏览卦象目录。两种入口汇入同一套阅读界面。'),
  ('detail','Sixty-four starting points.','六十四种阅读的起点。'),
  ('detail_body','Search by name, keyword or number, then narrow the library by palace and element. Hexagram symbols, names and short texts form a consistent card rhythm.','通过卦名、关键词或序号检索，再按宫位和五行筛选。卦象符号、名称和短文组成统一的卡片节奏。'),
  ('flow1','Ask','提问'),('flow2','Explore','探索'),('flow3','Read','阅读'),
  ('flowbody1','Enter a question on the homepage.','在首页输入想探索的问题。'),('flowbody2','Draw a hexagram or browse the library.','随机起卦，或浏览卦象目录。'),('flowbody3','Continue into text and related hexagrams.','阅读文本，继续查看关联卦象。'),
  ('screen','Less noise. More room to read.','让文字，成为画面的中心。'),
  ('screen_body','A near-black canvas and pale blue typography give the homepage a restrained atmosphere. The question field remains the primary action, with browsing close at hand.','近黑色背景与浅蓝文字构成克制的首页。提问入口是主要操作，卦象浏览则保持在触手可及的位置。'),
  ('end','Follow a question somewhere new.','带着一个问题，开始探索。'),
 ]}

def translations():
    return {f'ed_{slug}_{key}':zh for slug,rows in COPY.items() for key,en,zh in rows}

def text(slug,key):
    en=next(en for k,en,zh in COPY[slug] if k==key)
    return f'<span data-i18n="ed_{slug}_{key}">{escape(en)}</span>'

def cover(p,pre=''):
    slug=p['slug']
    name='Period' if slug=='period' else '问易'
    image='period.jpg' if slug=='period' else 'wenyi.jpg'
    return f'''<div class="ed-cover ed-{slug}"><div class="ed-orbit" aria-hidden="true"></div><div class="ed-cover-label mono">PLAY / VIBE CODING</div><div class="ed-cover-copy"><strong>{name}</strong><span>{text(slug,'hero')}</span></div><div class="ed-device"><img src="{pre}assets/play/{image}" alt="{escape(p['title'])} interface" loading="lazy"></div><span class="ed-cover-foot mono">{'DAILY RHYTHMS / WEB APP' if slug=='period' else 'I CHING / INTERACTIVE EXPLORATION'}</span></div>'''

def render(p,base_open,finish,recommendation_cards):
    slug=p['slug']; t=lambda key:text(slug,key)
    links=f'<div class="ed-links"><a href="{p["live_url"]}" target="_blank" rel="noopener noreferrer" data-i18n="ed_visit">VISIT WEBSITE ↗</a><a href="{p["repo_url"]}" target="_blank" rel="noopener noreferrer" data-i18n="ed_source">SOURCE CODE ↗</a></div>'
    s=base_open('project',p['title'],True,p['tagline'])
    s+=f'''<article class="page-wrap ed-case ed-case-{slug}"><div class="case-top"><a class="back-link" href="../work.html?category=play">← <span data-i18n="play_back">BACK TO PLAY</span></a><span class="mono">{p['number']} / WEB EXPERIENCE</span></div>
    <header class="ed-title"><div><span class="mono">PLAY — VIBE CODING</span><h1 data-i18n="project_{slug}_display_title">{escape(p['title'])}</h1></div><div><p>{t('hero')}</p>{links}</div></header>
    {cover(p,'../')}
    <section class="ed-overview"><div><span class="mono">01 / <span data-i18n="ed_overview">OVERVIEW</span></span><h2>{t('idea')}</h2></div><div><p class="ed-lede">{t('intro')}</p><p>{t('idea_body')}</p><dl><div><dt data-i18n="case_role">MY ROLE</dt><dd>Vibe coding</dd></div><div><dt data-i18n="play_stack">TECH STACK</dt><dd>{escape(p['tools'])}</dd></div></dl></div></section>
    <section class="ed-feature"><div class="ed-feature-copy"><span class="mono">02 / <span data-i18n="ed_interaction">INTERACTION</span></span><h2>{t('detail')}</h2><p>{t('detail_body')}</p></div><a class="ed-detail-image" href="../assets/play/{'period.jpg' if slug=='period' else 'wenyi-library.jpg'}" target="_blank" rel="noopener"><img src="../assets/play/{'period.jpg' if slug=='period' else 'wenyi-library.jpg'}" alt="{'Mood selection' if slug=='period' else 'Hexagram library'}" loading="lazy"></a></section>
    <section class="ed-flow"><span class="mono">03 / <span data-i18n="ed_journey">EXPERIENCE FLOW</span></span><div>'''
    for i in range(1,4):
        s+=f'<article><span class="ed-step mono">0{i} ↗</span><h3>{t("flow"+str(i))}</h3><p>{t("flowbody"+str(i))}</p></article>'
    s+=f'''</div></section><section class="ed-screen"><div><span class="mono">04 / <span data-i18n="ed_interface">INTERFACE</span></span><h2>{t('screen')}</h2><p>{t('screen_body')}</p></div><a href="../assets/play/{slug}.jpg" target="_blank" rel="noopener"><img src="../assets/play/{slug}.jpg" alt="{escape(p['title'])} interface" loading="lazy"></a></section>
    <section class="ed-end"><span class="mono">EXPLORE THE PROJECT</span><h2>{t('end')}</h2>{links}</section>{recommendation_cards(p)}</article>'''
    return s+finish(True)
