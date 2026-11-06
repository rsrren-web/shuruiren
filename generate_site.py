"""Generate the multilingual, build-free A Little Machine portfolio site.

Edit verified project content in portfolio_data.py, then run python3 generate_site.py.
V18 preserves V17 project material from the supplied portfolio PDF; launch permissions remain pending.
"""
from pathlib import Path
from html import escape
import json
from portfolio_data import PROJECTS, ICONS, art_markup, VISUAL_STORIES, PROJECT_TOOLS
from translations import ZH, IDEAS_ZH, SCREEN_ZH
from play_editorial import cover as editorial_cover, render as editorial_render

ROOT=Path(__file__).parent
MODES=[('design','DESIGN','DESIGN'),('art','ART','ART'),('game','GAME','GAME'),('campaigns','CAMPAIGNS','CAM<br>PAIGNS'),('play','PLAY','PLAY')]
CATEGORY={k:k for k in ('design','art','game','campaigns','play')}

def tx(key, default, html=False):
    return f'data-i18n{"-html" if html else ""}="{key}"'

def base_open(page, title, inner=False, desc='Independent creative portfolio by Shurui Ren.'):
    pre='../' if inner else ''
    active='project' if inner else page
    return f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#F7F8F5"><meta name="description" content="{escape(desc)}"><meta name="lm-audio-source" content="{pre}assets/audio/little-machine-lofi-original-tone-5min.mp3"><title>Shurui‘s Portfolio</title><link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{pre}assets/styles.css?v=editorial2"><script src="{pre}assets/i18n.js?v=editorial2" defer></script><script src="{pre}assets/main.js?v=paths2" defer></script></head><body id="top" class="page-{page}{' case-page' if inner else ''}" data-page="{page}"><a class="skip" href="#main-content" data-i18n="skip">Skip to content</a>{header(pre,active)}<main id="main-content">'''

def header(pre, active):
    links=[('home','index.html','01','Home'),('work','work.html','02','Work'),('about','about.html','03','About'),('contact','contact.html','04','Contact')]
    nav=''.join(f'<a href="{pre}{file}"{(" aria-current=\"page\"" if active==page else "")} {("class=\"nav-contact\"" if page=="contact" else "")}><span>{number}</span><b data-i18n="nav_{page}">{name}</b>{(" <strong aria-hidden=\"true\">↗</strong>" if page=="contact" else "")}</a>' for page,file,number,name in links)
    return f'''<header class="site-header"><div class="page-wrap header-inner"><a class="brand" href="{pre}index.html" aria-label="Home" data-i18n-aria-label="a11y_home"><span class="brand-symbol">SR<em>✳</em></span><span class="brand-descriptor mono" data-i18n-html="brand_descriptor">DESIGNER &amp; ILLUSTRATOR<br>VANCOUVER, CANADA</span></a>
    <nav class="main-nav" id="main-nav" aria-label="Main navigation" data-i18n-aria-label="a11y_navigation">{nav}</nav>
    <div class="header-tools"><button class="language-toggle" id="language-toggle" type="button" aria-label="Switch to Chinese"><span class="lang-en">EN</span><span class="lang-divider">/</span><span class="lang-zh">中</span></button><button class="sound-toggle" id="sound-toggle" type="button" aria-pressed="true" aria-label="Turn off interface sounds" title="Toggle interface sounds"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 10v4h4l5 4V6L8 10H4Z"/><path class="sound-wave" d="M16 9c1.5 1.5 1.5 4.5 0 6M19 6c3.2 3.2 3.2 8.8 0 12"/></svg><span class="sound-toggle-label">SOUND READY</span></button><button class="sound-settings-toggle" id="sound-settings-toggle" type="button" aria-label="Audio settings" aria-expanded="false" aria-controls="audio-settings" title="Audio settings"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 17h16M9 4v6M15 14v6"/></svg></button><div class="audio-settings" id="audio-settings" role="dialog" aria-label="Audio settings" hidden><div class="audio-panel-title"><span data-audio-heading>LITTLE MACHINE / AUDIO</span><span class="audio-panel-mark" aria-hidden="true">✳</span></div><div class="audio-panel-row"><label class="audio-panel-switch"><input type="checkbox" data-audio-music-enabled checked><span data-music-label>Background music</span></label><span class="mono audio-panel-value" data-audio-music-value>18%</span></div><p class="audio-panel-description" data-music-description>Selected track · Original tone · 5-min loop</p><input class="audio-range" type="range" min="0" max="100" step="1" value="18" data-audio-music-level aria-label="Background music volume"><div class="audio-panel-rule"></div><div class="audio-panel-row"><label class="audio-panel-switch"><input type="checkbox" data-audio-fx-enabled checked><span data-fx-label>Interface sounds</span></label><span class="mono audio-panel-value" data-audio-fx-value>90%</span></div><p class="audio-panel-description" data-fx-description>Hover / Click / Machine</p><input class="audio-range" type="range" min="0" max="100" step="1" value="90" data-audio-fx-level aria-label="Interface sounds volume"><p class="audio-panel-hint" data-audio-hint>Sound is on by default. If autoplay is blocked, your first click or key starts it.</p></div><button class="nav-toggle" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="main-nav"><span></span><span></span></button></div></div></header>'''

def footer(inner=False):
    pre='../' if inner else ''
    return f'''<footer class="global-footer"><div class="page-wrap global-footer-inner"><span class="mono">© <span data-current-year>2026</span> <span data-footer-name>SH<span class="name-u">U</span>R<span class="name-u">U</span>I <span class="name-ren">REN</span></span> <span data-i18n="footer_made">/ BUILT WITH CURIOSITY</span></span><div class="footer-links"><a href="{pre}work.html" data-i18n="nav_work">Work</a><a href="{pre}about.html" data-i18n="nav_about">About</a><a href="{pre}contact.html" data-i18n="nav_contact">Contact</a><a href="#top" data-i18n="back_top">TOP ↑</a></div></div></footer>'''

def finish(inner=False):return '</main>'+footer(inner)+'</body></html>'

def machine_html():
    btns=''.join(f'''<button class="machine-window" type="button" data-mode="{mode}" aria-pressed="{str(i==0).lower()}" aria-label="Select {escape(name)}"><svg viewBox="0 0 48 48" aria-hidden="true">{ICONS[mode]}</svg><span class="window-text"><span class="window-number">0{i+1}</span><span class="window-label" data-i18n="mode_{mode}">{display}</span></span></button>''' for i,(mode,name,display) in enumerate(MODES))
    return f'''<div class="machine-stage" aria-label="Interactive idea machine" data-i18n-aria-label="a11y_machine"><span class="orbit-cross one" aria-hidden="true">+</span><span class="orbit-cross two" aria-hidden="true">+</span><div class="machine-stage-label mono"><span data-i18n="machine_production">THE CREATIVE PRODUCTION UNIT</span></div><div class="machine" id="creative-machine"><div class="machine-body"><div class="machine-panel"><div class="machine-heading"><div class="product-mark">LITTLE MACHINE <span>®</span></div><div class="machine-ready mono"><i class="ready-light"></i><span id="machine-status" data-i18n="machine_ready">READY TO MAKE</span></div></div>
    <div class="machine-screen" aria-live="polite" aria-atomic="true"><div class="screen-top"><span><span data-i18n="mode_selected">MODE SELECTED</span> / <span id="screen-index">01</span></span><span>IDEA_ENGINE.EXE</span></div><div class="screen-main"><span class="screen-mode" id="screen-mode">DESIGN MODE</span><span class="screen-icon" id="screen-symbol" aria-hidden="true">✳</span></div></div>
    <div class="windows-label mono"><span data-i18n="choose_discipline">01 — CHOOSE A DISCIPLINE</span><span data-i18n="five_channels">5 CHANNELS</span></div><div class="machine-windows" role="group" aria-label="Creative disciplines" data-i18n-aria-label="a11y_disciplines">{btns}</div><div class="machine-footer"><div class="machine-dial" aria-hidden="true"></div><a class="machine-button" href="contact.html" id="generate-idea" aria-label="Make An Idea — contact Shurui" data-i18n-aria-label="a11y_make_idea"><b class="machine-button-label" data-i18n="make_idea">MAKE AN IDEA</b><span aria-hidden="true">↗</span></a><span class="machine-serial mono">LM-001<br>2026</span></div></div></div>
    <a class="machine-ticket" id="machine-ticket" href="work.html?category=design" aria-label="Explore Design work"><div class="ticket-top mono">✳ <span data-i18n="little_idea">LITTLE IDEA</span> / <span id="ticket-number">001</span><span class="ticket-corner" aria-hidden="true">↗</span></div><div class="ticket-rule"></div><p id="ticket-text" aria-live="polite">Make a tiny interface with a big personality.</p><div class="ticket-bottom"><span class="ticket-mode mono" id="ticket-mode">DESIGN</span><span class="ticket-cta" id="ticket-cta">EXPLORE DESIGN WORK <span aria-hidden="true">↗</span></span></div><span class="ticket-interact-hint mono" data-i18n="ticket_hint">CLICK THIS NOTE TO EXPLORE ↗</span></a></div><div class="machine-stage-bottom mono" data-i18n="machine_hint">PICK A WINDOW. FIND AN IDEA. EXPLORE THE WORK.</div></div>'''

def project_card(p, inner=False, pdf_first=False):
    pre='../' if inner else ''
    cat=CATEGORY.get(p['category'],'play')
    slug=p['slug']
    image = (f'<div class="project-art pdf-first-art"><img src="{pre}{escape(p["pdf_thumb"],quote=True)}" alt="{escape(p["title"]+" — complete first source PDF page",quote=True)}" loading="lazy" decoding="async" width="1728" height="1117"><span class="pdf-first-corner mono">01 / PDF</span></div>' if pdf_first else art_markup(p))
    label_key, label = 'portfolio_label', 'PORTFOLIO / DRAFT'
    if p.get('live_url'):
        image = editorial_cover(p, pre)
        label_key, label = 'play_label', 'LIVE / WEB PROJECT'
    return f'''<article class="project" data-category="{cat}"><a class="project-link" href="{pre}projects/{slug}.html" aria-label="View {escape(p['title'])} project" data-i18n-aria-label="project_{slug}_card_aria">{image}<div class="project-meta"><span class="mono">{p['number']} / <span data-i18n="project_{slug}_type">{escape(p['type'])}</span></span><small class="mono" data-i18n="{label_key}">{label}</small></div><h3 class="project-title"><span data-i18n="project_{slug}_display_title">{escape(p['title'])}</span><span class="arrow" aria-hidden="true">↗</span></h3><p class="project-description" data-i18n="project_{slug}_tagline">{escape(p['tagline'])}</p></a></article>'''

def mini_section(tag, label, title, p, url, link_key, link_label):
    return f'''<a class="home-editorial-link" href="{url}"><span class="mono">{tag} / <span data-i18n="{label[0]}">{label[1]}</span></span><strong {tx(title[0],title[1],True)}>{title[1]}</strong><span class="mono discover-arrow" data-i18n="{link_key}">{link_label} ↗</span></a>'''

def home():
    selected=[PROJECTS[0],PROJECTS[1],PROJECTS[5]]
    s=base_open('home','A Little Machine for Big Ideas')
    s+='''<section class="hero" aria-labelledby="hero-heading"><div class="page-wrap"><div class="hero-meta"><span class="mono"><i class="meta-dot"></i> <span data-i18n="hero_meta">AN INDEPENDENT CREATIVE PRACTICE</span></span></div><div class="hero-grid"><div class="hero-copy"><div class="hero-sup mono"><span class="sup-line"></span><span data-i18n="hero_hello">HELLO, I'M THE PERSON BEHIND THE IDEAS</span></div><h1 class="hero-title" id="hero-heading"><span data-name-first>SH<span class="name-u">U</span>R<span class="name-u">U</span>I</span><span data-name-second><span class="name-ren">REN</span></span></h1><div class="identity" data-i18n-html="hero_identity"><div>Design. <span class="blue">Draw.</span></div><div class="indent">Build. <span class="blue">Play.</span></div></div><div class="hero-description"><span class="asterisk" aria-hidden="true">✳</span><p data-personal-description data-i18n="hero_description">Designer and illustrator creating thoughtful digital experiences, visual stories, brands, and campaigns.</p></div><a class="hero-nudge" href="work.html"><span class="nudge-icon" aria-hidden="true">↓</span><span class="mono" data-i18n="hero_discover">EXPLORE THE WORK</span></a></div>'''+machine_html()+'''</div><div class="hero-bottom"><span class="mono" data-i18n="hero_brand_line">01 / A LITTLE MACHINE FOR BIG IDEAS.</span><span class="little-arrows" aria-hidden="true">↓ ↓ ↓</span><span class="mono" data-i18n="hero_bottom">DESIGN / ART / GAME / CAMPAIGNS / PLAY</span></div></div></section>'''
    s+='''<section class="work-section home-featured" id="featured-work"><div class="page-wrap"><div class="section-topline"><div class="section-index"><span class="index-square">02</span><span class="mono" data-i18n="featured_label">FEATURED / LITTLE PREVIEW</span></div><span class="mono" data-i18n="demo_warning">REAL PROJECTS / EDITORIAL REVIEW</span></div><div class="work-intro"><h2 data-i18n-html="featured_heading">Ideas in<br><span class="blue">the making.</span></h2><div class="work-summary"><span class="mono" data-i18n="featured_eyebrow">A CURATED GLIMPSE</span><p data-i18n="featured_body">Selected work from the submitted portfolio: digital experiences, interactive play and illustration.</p><a class="text-arrow-link" href="work.html" data-i18n="featured_action">EXPLORE ALL WORK ↗</a></div></div><div class="work-grid featured-grid v15-featured-grid">'''+''.join(project_card(p,pdf_first=True) for p in selected)+'''</div></div></section>'''
    s+='''<section class="home-next"><div class="page-wrap"><div class="home-next-grid">'''+mini_section('03',('home_about_label','THE PERSON'),('home_about_title','Not one<br>kind of <em>thing.</em>'),'','', '', '') if False else '' # Built immediately below.
    s+='''<section class="home-next"><div class="page-wrap"><div class="home-next-grid"><a class="home-editorial-link" href="about.html"><span class="mono">03 / <span data-i18n="home_about_label">THE PERSON</span></span><strong data-i18n-html="home_about_title">Not one<br>kind of <em>thing.</em></strong><span class="mono discover-arrow" data-i18n="home_about_action">EXPLORE MY CV ↗</span></a><a class="home-editorial-link" href="contact.html"><span class="mono">04 / <span data-i18n="home_contact_label">TWO PLACES, ONE HELLO</span></span><strong data-i18n-html="home_contact_title">Got a<br><em>little idea?</em></strong><span class="mono discover-arrow" data-i18n="home_contact_action">GET IN TOUCH ↗</span></a></div></div></section>'''
    return s+finish()

def work():
    s=base_open('work','Work — A Little Machine')
    s+='''<section class="work-section standalone-work"><div class="page-wrap"><div class="section-topline"><div class="section-index"><span class="index-square">02</span><span class="mono" data-i18n="work_kicker">THE PORTFOLIO / FIVE DISCIPLINES</span></div><span class="mono" data-i18n="demo_warning">REAL PROJECTS / EDITORIAL REVIEW</span></div><div class="work-intro"><h1 data-i18n-html="work_heading">Things made<br>along <span class="blue">the way.</span></h1><div class="work-summary"><span class="mono" data-i18n="discipline_summary">DESIGN / ART / GAME / CAMPAIGNS / PLAY</span><p data-i18n="work_description">Browse by discipline: portfolio case studies alongside live Vibe Coding projects.</p></div></div><div class="filters" role="group" aria-label="Filter projects by discipline" data-i18n-aria-label="a11y_filters">'''
    s+=''.join(f'<button class="filter" type="button" data-filter="{cat}" aria-pressed="{str(i==0).lower()}" data-i18n="filter_{cat}">{label}</button>' for i,(cat,label) in enumerate([('all','All work'),('design','Design'),('art','Art'),('game','Game'),('campaigns','Campaigns'),('play','Play')]))
    s+='''<span class="filter-count mono" id="filter-count" aria-live="polite">SHOWING 13 / 13</span></div><div class="work-grid" id="project-grid">'''+''.join(project_card(p,pdf_first=True) for p in PROJECTS)+'''</div><div class="filter-empty" id="filter-empty" hidden><span class="empty-star" aria-hidden="true">✳</span><h2 data-i18n="empty_heading">This channel is warming up.</h2><p data-i18n="empty_body">No project in this category has been documented in the supplied portfolio yet.</p><button type="button" class="empty-reset" data-reset-filter data-i18n="empty_reset">VIEW ALL WORK ↗</button></div><div class="work-bottom-note mono" data-i18n="work_bottom_note">PORTFOLIO CASE STUDIES & LIVE WEB PROJECTS / SOURCES AND LINKS IN EACH PROJECT.</div></div></section>'''
    return s+finish()

def about():
    s=base_open('about','About & CV — A Little Machine')
    s=s.replace('data-i18n-html="brand_descriptor"', 'data-i18n-html="brand_descriptor_about"', 1)
    s+='''<section class="about-section standalone-about about-v7"><div class="page-wrap">
      <div class="section-topline"><div class="section-index"><span class="index-square">03</span><span class="mono" data-i18n="about_kicker">ABOUT / CURRICULUM VITAE</span></div><span class="mono" data-i18n="about_location_short">VANCOUVER, CANADA ✳</span></div>
      <div class="about-editorial-intro">
        <div class="about-visual-column">
          <div class="about-sketch-card" aria-label="Abstract sketchbook-inspired composition, reserved for a future original personal drawing" data-i18n-aria-label="about_sketch_aria">
            <div class="about-sketch-top mono"><span>FIG. 02 / <span data-i18n="about_sketch_title">CREATIVE FIELD NOTES</span></span><span class="sketch-cross" aria-hidden="true">✳</span></div>
            <svg class="about-sketch-art" viewBox="0 0 380 420" role="img" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
              <path d="M40 80C85 31 146 20 191 82S291 148 332 95" fill="none" stroke="#17191D" stroke-width="4" stroke-linecap="round" stroke-dasharray="10 13"/>
              <path d="M50 165C116 83 177 147 194 203S286 277 329 192" fill="none" stroke="#315EFF" stroke-width="14" stroke-linecap="round"/>
              <path d="M50 169C112 86 175 151 192 207S281 280 328 194" fill="none" stroke="#17191D" stroke-width="3.2" stroke-linecap="round"/>
              <path d="M85 262c-31-28-6-79 34-70 25 6 29 32 53 31 25 0 38-40 70-29 38 13 30 62-5 77-35 15-39 46-82 37-36-9-41-16-70-46z" fill="#C9FF48" stroke="#17191D" stroke-width="4" stroke-linejoin="round"/>
              <g fill="none" stroke="#17191D" stroke-width="3.5" stroke-linecap="round">
              <path d="M253 45l20 18m-5-23l-9 27m32-8l-31-5"/><path d="M66 343l17-17 17 16-18 18z"/><path d="M241 328l12-9 13 9-13 10z"/><path d="M275 335l7-19 11 15"/>
              </g>
              <path d="M125 348c44-17 88-15 127 4" fill="none" stroke="#315EFF" stroke-width="4" stroke-linecap="round"/>
              <circle cx="316" cy="278" r="32" fill="#315EFF" stroke="#17191D" stroke-width="4"/><path d="M296 277h40m-20-20v40" stroke="#F7F8F5" stroke-width="4"/>
            </svg>
            <div class="about-sketch-baseline mono"><span data-i18n="about_sketch_axis">OBSERVE — CONNECT — MAKE</span><span>✳ / 001</span></div>
          </div>
          <p class="about-sketch-caption mono" data-i18n="about_sketch_caption">An abstract sketch-study placeholder. Your own illustration or self-portrait can live here later.</p>
          <div class="about-side-card about-side-card-v7"><span class="mono" data-i18n="about_now">CURRENT BASE</span><strong data-i18n-html="aside_base">VANCOUVER<br>CANADA</strong><span class="mono" data-i18n="about_identity">DESIGNER &amp; ILLUSTRATOR</span></div>
        </div>
        <div class="about-story-column">
          <p class="about-kicker mono" data-i18n="about_eyebrow">A NOTE FROM THE MAKER / CV SUMMARY</p>
          <h1 class="about-title about-name-title" data-i18n-html="about_heading" aria-label="Shurui Ren"><span class="name-line">SH<span class="name-u">U</span>R<span class="name-u">U</span>I</span><span class="name-line name-ren">REN</span></h1>
          <div class="about-body about-longform">
            <p class="about-lede" data-i18n="about_story_1">I've always been exploring the spaces between Design, Illustration, and Digital Media.</p>
            <p data-i18n="about_story_2">Studying Interdisciplinary Design taught me to start with problems and look across disciplines for answers. Later, during my master's in Digital Media, I began bringing the storytelling of illustration and the warmth of handmade work into screens, so interfaces and motion could have emotion and room to breathe.</p>
            <p data-i18n="about_story_3">To me, creativity is the sum of observation and connection: noticing details others might miss and bringing seemingly unrelated things together into something that feels naturally whole.</p>
            <p data-i18n="about_story_4">I love poetic imagery, considered white space, and motion with intention. I keep experimenting with tools and media, exploring their unique qualities and technological possibilities. Ultimately, I care most about how the work makes people feel—technology makes it possible, and sincerity makes it resonate.</p>
          </div>
        </div>
      </div>
      <div class="about-quote-band"><span class="mono" data-i18n="about_quote_kicker">A LITTLE CREATIVE PRINCIPLE / 001</span><blockquote data-i18n="about_quote">Technology makes it possible. Sincerity makes it resonate.</blockquote><span class="about-quote-star" aria-hidden="true">✳</span></div>
      <section class="about-field-section" aria-labelledby="about-fields-title">
        <div class="about-section-heading"><span class="mono about-section-no">CV / 01 — <span data-i18n="about_fields_label">WHAT I DO</span></span><h2 id="about-fields-title" data-i18n-html="about_fields_heading">Different tools.<br>One curious mind.</h2><p data-i18n="about_fields_intro">I move between disciplines depending on the story, the problem, and the feeling a project needs.</p></div>
        <div class="about-field-grid">
          <article class="about-field-card"><span class="mono about-field-index">01 / DESIGN</span><span class="about-field-icon" aria-hidden="true">⌘</span><h3 data-i18n="about_field_1_title">Digital experiences</h3><p data-i18n="about_field_1_body">UI/UX design, interfaces, and digital products.</p></article>
          <article class="about-field-card"><span class="mono about-field-index">02 / ART</span><span class="about-field-icon" aria-hidden="true">✳</span><h3 data-i18n="about_field_2_title">Illustration &amp; storytelling</h3><p data-i18n="about_field_2_body">Visual narratives, characters, and poetic imagery.</p></article>
          <article class="about-field-card"><span class="mono about-field-index">03 / CAMPAIGNS</span><span class="about-field-icon" aria-hidden="true">↗</span><h3 data-i18n="about_field_3_title">Brand &amp; campaigns</h3><p data-i18n="about_field_3_body">Brand identities, campaign visuals, and communication design.</p></article>
          <article class="about-field-card"><span class="mono about-field-index">04 / MEDIA</span><span class="about-field-icon" aria-hidden="true">◉</span><h3 data-i18n="about_field_4_title">Digital media &amp; motion</h3><p data-i18n="about_field_4_body">Digital media, video editing, and motion thinking.</p></article>
          <article class="about-field-card"><span class="mono about-field-index">05 / PLAY</span><span class="about-field-icon" aria-hidden="true">⌁</span><h3 data-i18n="about_field_5_title">3D &amp; experimentation</h3><p data-i18n="about_field_5_body">3D modeling and exploratory creative tools.</p></article>
          <article class="about-field-card"><span class="mono about-field-index">06 / PEOPLE</span><span class="about-field-icon" aria-hidden="true">↔</span><h3 data-i18n="about_field_6_title">Collaboration &amp; leadership</h3><p data-i18n="about_field_6_body">Working across roles and guiding shared design decisions.</p></article>
        </div>
      </section>
      <section class="about-journey" aria-labelledby="about-journey-title">
        <div class="about-section-heading about-journey-heading"><span class="mono about-section-no">CV / 02 — <span data-i18n="cv_experience">EXPERIENCE</span></span><h2 id="about-journey-title" data-i18n-html="about_experience_heading">Places I've learned<br>to make things.</h2><p data-i18n="about_experience_intro">A selection of verified organization names and role titles from my CV summary. Dates and detailed responsibilities will follow once the source CV is confirmed.</p></div>
        <div class="about-timeline">
          <article class="about-timeline-item"><span class="timeline-mark mono">01</span><div><h3>Ruoshui Design and Art Agency</h3><p data-i18n="cv_role_lead">Lead Designer</p></div><span class="timeline-type mono" data-i18n="cv_agency">AGENCY</span></article>
          <article class="about-timeline-item"><span class="timeline-mark mono">02</span><div><h3>Justice Institute of British Columbia</h3><p data-i18n="cv_role_pm">Product Manager (Industrial Project)</p></div><span class="timeline-type mono" data-i18n="cv_industrial">INDUSTRIAL PROJECT</span></article>
          <article class="about-timeline-item"><span class="timeline-mark mono">03</span><div><h3>DijiBC</h3><p data-i18n="cv_role_diji">Lead Designer (Industrial Project)</p></div><span class="timeline-type mono" data-i18n="cv_industrial">INDUSTRIAL PROJECT</span></article>
          <article class="about-timeline-item"><span class="timeline-mark mono">04</span><div><h3>WeUsThem Design Agency</h3><p data-i18n="cv_role_junior">Junior Designer</p></div><span class="timeline-type mono" data-i18n="cv_agency">AGENCY</span></article>
        </div>
      </section>
      <section class="about-education about-journey about-education-journey" aria-labelledby="about-education-title">
        <div class="about-section-heading about-journey-heading"><span class="mono about-section-no">03 — <span data-i18n="cv_education">EDUCATION</span></span><h2 id="about-education-title" data-i18n-html="about_edu_heading">Learning across<br>boundaries.</h2></div>
        <div class="about-timeline about-education-timeline">
          <article class="about-timeline-item"><span class="timeline-mark mono">01</span><div><h3>Simon Fraser University</h3><p data-i18n="cv_degree_master">Master of Digital Media</p></div><span class="timeline-type mono" data-i18n="sfu_country">SFU / CANADA</span></article>
          <article class="about-timeline-item"><span class="timeline-mark mono">02</span><div><h3>NSCAD University</h3><p data-i18n="cv_degree_bachelor">Bachelor of Design — Major in Interdisciplinary Design, Minor in Illustration</p></div><span class="timeline-type mono" data-i18n="nscad_country">NSCAD / CANADA</span></article>
        </div>
      </section>
      <section class="about-beyond" aria-labelledby="about-beyond-title"><div class="about-section-heading"><span class="mono about-section-no">04 — <span data-i18n="about_beyond_label">BEYOND THE SCREEN</span></span><h2 id="about-beyond-title" data-i18n="about_beyond_heading">What stays with me.</h2><p data-i18n="about_beyond_intro">A small map of the ideas that shape how I approach creative work.</p></div><div class="about-beyond-grid">
        <article><span class="about-beyond-num mono">01 / <span data-i18n="about_beyond_1_label">NOTICE</span></span><h3 data-i18n="about_beyond_1_title">Look closer.</h3><p data-i18n="about_beyond_1_body">Details that are easy to miss can be the beginning of a better idea.</p></article>
        <article><span class="about-beyond-num mono">02 / <span data-i18n="about_beyond_2_label">CONNECT</span></span><h3 data-i18n="about_beyond_2_title">Make connections.</h3><p data-i18n="about_beyond_2_body">Unexpected relationships between fields, materials, and tools create new possibilities.</p></article>
        <article><span class="about-beyond-num mono">03 / <span data-i18n="about_beyond_3_label">FEEL</span></span><h3 data-i18n="about_beyond_3_title">Leave a feeling.</h3><p data-i18n="about_beyond_3_body">The best result is not just something that works, but something that resonates.</p></article>
      </div></section>
      <div class="about-cv-note"><p data-i18n="cv_disclaimer">This page is based on the CV summary provided in the project handoff. Dates, detailed responsibilities, and a downloadable CV will be added after the source document is verified.</p></div>
      <a class="cv-contact-link" href="contact.html"><span data-i18n="about_connect">HAVE SOMETHING IN MIND? LET'S TALK.</span><strong aria-hidden="true">↗</strong></a>
    </div></section>'''
    return s+finish()

def contact():
    svg=(ROOT/'templates/world-map.html').read_text(encoding='utf-8')
    s=base_open('contact','Contact — A Little Machine')
    s+='''<section class="contact-section contact-page"><div class="page-wrap"><div class="contact-heading-row"><div class="section-index"><span class="index-square">04</span><span class="mono" data-i18n="contact_kicker">SOMEWHERE BETWEEN HERE & THERE</span></div><span class="mono" data-i18n="contact_available">OPEN TO CONVERSATIONS ✳</span></div><div class="contact-grid"><h1 class="contact-title" data-i18n-html="contact_heading">TWO PLACES.<br>ONE <span>HELLO.</span></h1><div class="contact-right"><span class="mono" data-i18n="contact_intro_tag">PICK A PLACE ON THE MAP</span><p data-i18n="contact_intro">Based in Vancouver and connected across borders. Choose Canada or China to see the available contact details.</p><a class="contact-email" data-contact-email href="mailto:rsr.ren@gmail.com">rsr.ren@gmail.com <span aria-hidden="true">↗</span></a></div></div>
    <div class="contact-map-layout"><div class="contact-map" id="contact-map"><div class="map-heading"><span class="mono" data-i18n="world_connections">WORLD / CONNECTIONS</span><span class="mono" data-i18n="map_hint">SELECT A HIGHLIGHTED COUNTRY ↘</span></div><div class="map-canvas">'''+svg+'''<button class="map-pin canada is-active" type="button" data-map-select="canada" aria-pressed="true"><span class="pin-dot"></span><span class="pin-label" data-i18n="map_canada_label">CANADA</span></button><button class="map-pin china" type="button" data-map-select="china" aria-pressed="false"><span class="pin-dot"></span><span class="pin-label" data-i18n="map_china_label">CHINA</span></button></div><div class="map-bottom"><span class="mono" data-i18n="map_footer_left">CLICK A MARKER OR COUNTRY TO SWITCH</span><span class="mono">49° N — 35° N ✳</span></div></div>
    <div class="location-panel" aria-live="polite"><div class="location-panel-top"><span class="mono" data-i18n="location_channel">CONTACT CHANNEL</span><span class="location-led" aria-hidden="true"></span></div><div class="location-info" data-contact-country="canada"><span class="location-number mono" data-i18n="continent_na">01 / NORTH AMERICA</span><h2 data-i18n="location_canada">Canada.</h2><p class="location-place" data-i18n="location_vancouver">Vancouver, British Columbia</p><div class="contact-detail-rule"></div><div class="contact-field"><span class="mono" data-i18n="contact_email_label">EMAIL</span><a data-contact-email href="mailto:rsr.ren@gmail.com">rsr.ren@gmail.com ↗</a></div><p class="location-note" data-i18n="canada_note">Currently listed portfolio email. Location confirmed as Vancouver, Canada.</p></div>
    <div class="location-info" data-contact-country="china" hidden><span class="location-number mono" data-i18n="continent_asia">02 / ASIA</span><h2 data-i18n="location_china">China.</h2><p class="location-place" data-i18n="china_place">China contact point — to be confirmed</p><div class="contact-detail-rule"></div><div class="contact-field"><span class="mono" data-i18n="contact_email_label">EMAIL</span><a data-contact-email href="mailto:rsr.ren@gmail.com">rsr.ren@gmail.com ↗</a></div><p class="location-note" data-i18n="china_note">This is the general portfolio email. China-specific email, WeChat, and phone have not been provided yet.</p></div><div class="location-panel-bottom mono" data-i18n="contact_privacy">ONLY VERIFIED PUBLIC CONTACT DETAILS ARE SHOWN.</div></div></div></div></section>'''
    return s+finish()

def recommendation_cards(p):
    # Three distinct alternatives: immediate next, another discipline, and a later project.
    idx=next(i for i,item in enumerate(PROJECTS) if item['slug']==p['slug'])
    chosen=[]
    for offset in (1,2,4,6,8,10):
        item=PROJECTS[(idx+offset)%len(PROJECTS)]
        if item['slug']==p['slug'] or any(c['slug']==item['slug'] for c in chosen):continue
        if len(chosen)==1 and item['category']==chosen[0]['category']:continue
        chosen.append(item)
        if len(chosen)==3:break
    if len(chosen)<3:
        for item in PROJECTS:
            if item['slug']!=p['slug'] and item not in chosen:chosen.append(item)
            if len(chosen)==3:break
    rows=[]
    for item in chosen:
        slug=item['slug']
        rows.append(f'''<a class="v15-recommend-card" href="{escape(slug)}.html" aria-label="Explore {escape(item['title'],quote=True)}"><div class="v15-recommend-thumb"><img src="../{escape(item['pdf_thumb'],quote=True)}" loading="lazy" decoding="async" width="1728" height="1117" alt="{escape(item['title'],quote=True)} — project preview"></div><div class="v15-recommend-copy"><span class="mono">{escape(item['number'])} / <span data-i18n="filter_{item['category']}">{escape(item['category']).upper()}</span></span><strong data-i18n="project_{slug}_display_title">{escape(item['title'])}</strong><span class="v15-recommend-action" data-i18n="v15_view_project">VIEW PROJECT ↗</span></div></a>''')
    return f'''<section class="v15-more-projects"><div class="v15-more-heading"><div><span class="mono" data-i18n="v15_explore_kicker">STAY CURIOUS / MORE WORK</span><h2 data-i18n="v15_explore_heading">Keep exploring.</h2></div><a href="../work.html" data-i18n="v15_view_all">VIEW ALL PROJECTS ↗</a></div><div class="v15-recommend-grid">{''.join(rows)}</div></section>'''

def tools_markup(p):
    original=PROJECT_TOOLS.get(p['slug'])
    if not original:
        return '<span data-i18n="case_tools_pending">TO BE CONFIRMED</span>'
    return escape(original)

def detail(p,nxt):
    if p.get('live_url'):
        return play_detail(p)
    slug=p['slug']; prefix='project_'+slug+'_'; idx=p['number']
    s=base_open('project',p['title'],True,p['tagline'])
    s+=f'''<div class="page-wrap v14-case v15-case v17-case-wrap v18-case-wrap v19-case-wrap"><div class="case-top"><a class="back-link" href="../work.html"><span aria-hidden="true">←</span> <span data-i18n="all_work">ALL WORK</span></a><span class="mono"><span data-i18n="case_project">PROJECT</span> {idx} / {len(PROJECTS):02d} &nbsp; ✳ &nbsp; <span data-i18n="portfolio_label">PORTFOLIO / DRAFT</span></span></div>
    <section class="v17-case-lead v18-case-lead v19-case-lead" aria-label="Case study introduction"><div class="v17-case-intro v18-case-intro v19-case-intro"><div class="v17-case-hero v18-case-hero"><span class="case-label mono"><span data-i18n="{prefix}type">{escape(p['type'])}</span> <span class="v17-separator" aria-hidden="true">/</span> <span data-i18n="case_portfolio_origin">FROM SUBMITTED PORTFOLIO</span></span><h1 class="case-title" data-i18n="{prefix}display_title">{escape(p['title'])}</h1><span class="v15-case-original mono">{escape(p['title'])}</span><p class="v17-case-tagline" data-i18n="{prefix}tagline">{escape(p['tagline'])}</p></div><div class="v17-case-summary v18-case-summary"><span class="mono" data-i18n="v16_project_overview">PROJECT OVERVIEW</span><p data-i18n="{prefix}story">{escape(p['story'])}</p></div></div><dl class="v17-case-facts"><div><dt data-i18n="case_discipline">DISCIPLINE</dt><dd data-i18n="{prefix}type">{escape(p['type'])}</dd></div><div><dt data-i18n="case_role">MY ROLE</dt><dd data-i18n="{prefix}role">{escape(p['role'])}</dd></div><div><dt data-i18n="case_tools">TOOLS</dt><dd>{tools_markup(p)}</dd></div><div><dt data-i18n="v16_year">YEAR</dt><dd data-i18n="case_year_pending">YEAR TBC</dd></div></dl></section>
    {gallery_markup(p)}
    <section class="v15-project-notes" aria-label="Project context and documented work"><div class="v15-notes-intro"><span class="mono" data-i18n="v15_project_notes">PROJECT NOTES / FROM THE PORTFOLIO</span><h2 data-i18n="v15_project_context">A closer look.</h2></div><div class="v15-notes-grid"><article><span class="mono">01 / <span data-i18n="v15_question">THE QUESTION</span></span><p data-i18n="{prefix}lead">{escape(p['lead'])}</p></article><article><span class="mono">02 / <span data-i18n="v15_approach">THE APPROACH</span></span><p data-i18n="{prefix}approach">{escape(p['approach'])}</p></article><article><span class="mono">03 / <span data-i18n="v15_documented">WHAT'S DOCUMENTED</span></span><p data-i18n="{prefix}outcome">{escape(p['outcome'])}</p></article></div></section>
    {recommendation_cards(p)}
    <p class="case-warning"><span data-i18n="case_warning">PORTFOLIO-SOURCED REVIEW DRAFT: project dates, permissions and external claims require verification before publication.</span> <span class="mono"><span data-i18n="case_source_pages">SOURCE PDF PAGES</span>: {escape(p['source_pages'])}</span></p></div>'''
    return s+finish(True)

def play_detail(p):
    return editorial_render(p,base_open,finish,recommendation_cards)

def gallery_markup(p):
    slug=p['slug']; pages=p['gallery']; total=len(pages)
    page_html=[]
    for index,(rel,page_no) in enumerate(pages,1):
        image='../'+rel
        alt=f"{p['title']} — complete portfolio PDF page {page_no}, page {index} of {total}"
        page_html.append(f'''<figure class="v14-pdf-sheet v19-pdf-sheet"><button class="visual-image-button v14-page-trigger v19-page-trigger" type="button" data-full="{escape(image,quote=True)}" aria-label="View full original page {index} of {total}: {escape(alt,quote=True)}"><span class="v19-page-window"><img src="{escape(image,quote=True)}" alt="{escape(alt,quote=True)}" width="5184" height="3351" loading="{'eager' if index==1 else 'lazy'}" decoding="async"></span><span class="v14-enlarge" aria-hidden="true">↗</span></button><figcaption class="v14-pdf-caption mono"><span><span data-i18n="v14_page_label">PAGE</span> {index:02d} / {total:02d}</span><span><span data-i18n="case_portfolio_page">PORTFOLIO PAGE</span> {page_no:02d} &nbsp; · &nbsp; <span data-i18n="v14_click_enlarge">CLICK TO ENLARGE</span> ↗</span></figcaption></figure>''')
    return f'''<section class="v14-pdf-gallery" id="project-visuals" aria-label="Full original PDF pages in source order"><div class="v14-gallery-heading"><div><span class="mono" data-i18n="v14_original_order">ORIGINAL PDF / IN PAGE ORDER</span><h2 data-i18n="v15_gallery_title">Original pages.</h2></div><div class="v14-gallery-info"><strong class="mono">{total:02d} <span data-i18n="v14_pages_total">PAGES</span></strong><p data-i18n="v14_reading_hint">Scroll to read each complete page, or select any page for high-resolution zoom and navigation.</p></div></div><div class="v14-pdf-pages">{''.join(page_html)}</div></section>
    <div class="case-lightbox v14-lightbox" id="case-lightbox" role="dialog" aria-modal="true" aria-label="Portfolio full-page image viewer" hidden><div class="v14-lightbox-toolbar"><span class="mono" data-i18n="v14_viewer_heading">PDF PAGE VIEWER / FULL RESOLUTION</span><div class="v14-viewer-controls"><button data-lightbox-zoom-out type="button" aria-label="Zoom out">−</button><span class="mono v14-zoom-value" data-lightbox-zoom-value aria-live="polite">100%</span><button data-lightbox-zoom-in type="button" aria-label="Zoom in">+</button><button data-lightbox-reset type="button" aria-label="Reset zoom" data-i18n="v14_fit">FIT</button><button class="lightbox-close" type="button" data-lightbox-close aria-label="Close image">×</button></div></div><div class="v14-lightbox-stage" data-lightbox-stage tabindex="0"><img class="lightbox-photo" alt="" draggable="false"></div><div class="v14-lightbox-bottom"><button type="button" data-lightbox-prev aria-label="Previous page">←</button><p class="lightbox-caption mono" aria-live="polite"></p><button type="button" data-lightbox-next aria-label="Next page">→</button></div></div>'''

if __name__=='__main__':
    # Regenerate the bilingual runtime dictionary from its source of truth.
    translations_json=json.dumps({'zh':ZH,'ideasZh':IDEAS_ZH,'screenZh':SCREEN_ZH},ensure_ascii=False,indent=2)
    (ROOT/'assets'/'i18n.js').write_text('/* Generated from translations.py. */\nwindow.LM_TRANSLATIONS = '+translations_json+';\n',encoding='utf-8')
    for file,fn in [('index.html',home),('work.html',work),('about.html',about),('contact.html',contact)]:
        (ROOT/file).write_text(fn(),encoding='utf-8')
    for old in (ROOT/'projects').glob('*.html'):
        if old.stem not in {p['slug'] for p in PROJECTS}: old.unlink()
    for i,p in enumerate(PROJECTS):
        (ROOT/'projects'/f'{p["slug"]}.html').write_text(detail(p,PROJECTS[(i+1)%len(PROJECTS)]),encoding='utf-8')
    print(f'Generated home, work, about, contact and {len(PROJECTS)} portfolio-sourced project pages.')
