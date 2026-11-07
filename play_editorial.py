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
  ('features','A day is more than a single feeling.','一天的状态，不止一种感受。'),
  ('features_body','Movement, connection, rest and physical sensations each have their own place. Explore the daily record through four complementary views.','运动、社交、休息与身体感受，各有自己的位置。从四个不同的角度，记录一天的生活。'),
  ('activity_title','Movement, in your own terms.','用自己的方式，记录运动。'),
  ('activity_body','Choose from gym sessions, stretching, Baduanjin, tennis and hiking. Multiple selections let different activities coexist, while a separate rating captures the overall amount of movement.','健身房、拉伸、八段锦、网球和徒步可以多选，再用独立评分记录全天运动量，让不同活动都能被容纳。'),
  ('social_title','How did connection feel?','社交之后，你的感受如何？'),
  ('social_body','Work, leisure and everyday interactions sit alongside social intensity and the feeling afterwards: restorative, neutral or draining. Context matters as much as quantity.','工作、娱乐与日常场景，搭配社交强度和社交后的感受：恢复、没有明显影响，或消耗。记录的不只是数量，还有体验。'),
  ('sleep_title','Give rest a little attention.','也给休息，一点关注。'),
  ('sleep_body','Sleep quality and bedtime are recorded separately. Quick choices for sleep patterns keep the form approachable without requiring an exact sleep schedule.','将睡眠质量与入睡时间分别记录，用快捷选项描述睡眠表现，不要求填写精确的作息时间。'),
  ('pain_title','Make physical sensations specific.','把身体的感受，说得具体一点。'),
  ('pain_body','Illustrated body-area choices make it possible to record more than one location. Pain intensity, characteristics and responses provide further detail in the same flow.','用图示选择一个或多个疼痛部位，再在同一流程中记录程度、性质与反应，让身体感受得到更具体的表达。'),
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
    links=f'<div class="ed-links"><a href="{p["live_url"]}" target="_blank" rel="noopener noreferrer" data-i18n="ed_visit">VISIT WEBSITE ↗</a></div>'
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
    {period_features() if slug=='period' else ''}
    <section class="ed-end"><span class="mono">EXPLORE THE PROJECT</span><h2>{t('end')}</h2>{links}</section>{recommendation_cards(p)}</article>'''
    return s+finish(True)

def period_features():
    t=lambda key:text('period',key)
    s=f'<section class="period-features"><header><span class="mono">05 / DAILY LIFE</span><h2>{t("features")}</h2><p>{t("features_body")}</p></header><div class="period-feature-grid">'
    for i,key in enumerate(('activity','social','sleep','pain'),1):
        s+=f'''<article class="period-feature-card period-feature-{key}"><div class="period-feature-copy"><span class="mono">0{i} / {key.upper()}</span><h3>{t(key+'_title')}</h3><p>{t(key+'_body')}</p></div><a class="period-phone" href="../assets/play/period-{key}.jpg" target="_blank" rel="noopener" aria-label="View {key} interface"><img src="../assets/play/period-{key}.jpg" alt="Period — {key} recording interface" loading="lazy" width="390" height="844"></a></article>'''
    return s+'</div></section>'
