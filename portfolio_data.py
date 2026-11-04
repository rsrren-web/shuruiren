"""V14 real-portfolio editorial data sourced from the owner's uploaded 37-page PDF export.
No dates, invented KPI results or publication statuses have been inserted.
Update this file (not generated HTML) and re-run generate_site.py.
"""
from pathlib import Path
from html import escape
ROOT=Path(__file__).parent

# V19: Tools transcribed project by project from the source .fig introduction text.
# Missing tools are explicitly unverified, not inferred from software in the CV.
PROJECT_TOOLS = {
    "conflict-resolver": None,
    "scavenger": "Figma, Illustrator, Photoshop, Procreate",
    "audio-comics": "Figma, Illustrator, Photoshop, Asana",
    "whales-today": "Figma, Illustrator, Photoshop, Adobe XD",
    "glasessen": "Illustrator, Procreate, Photoshop",
    "forest-friends": "Illustrator, Procreate, Photoshop",
    "contact-lens-guide": "Illustrator, Procreate, Photoshop",
    "yellow-cover": "Illustrator, Procreate, Photoshop",
    "instagram-design": "Final Cut Pro, Google Trends, BuzzSumo, Google Analytics, Facebook Insights",
    "tiktok-pets": "Final Cut Pro, Google Trends, BuzzSumo, TikTok Analytics",
    "xiaohongshu-agency": "Final Cut Pro, Google Trends, BuzzSumo"
}

PROJECTS = [{'slug': 'conflict-resolver', 'title': 'Chat IT Out / Conflict Resolver', 'category': 'design', 'type': 'UI / UX DESIGN', 'role': 'Research, UI design, UX and interaction design', 'format': 'AI-assisted conflict-resolution interface', 'tagline': 'A guided space for preparing, navigating and reflecting on difficult conversations.', 'lead': 'How can a digital tool support more constructive conversations?', 'story': 'The submitted portfolio describes Conflict Resolver as an AI-assisted mobile-app project, also presented as Chat IT Out. It is structured around three stages: preparation, engagement and reflection.', 'approach': 'The portfolio includes information architecture, user flows, interface art assets and screen designs. Its technical documentation describes a React/Tailwind interface, local chat history and an AI-assisted conversation flow; these are project-level details, not claimed as work performed solely by me.', 'outcome': 'Portfolio materials show interface concepts, application screens and supporting project documentation. No launch date or independently confirmed user outcomes are supplied.', 'steps': [('Three stages', 'Preparation, engagement and reflection frame the conflict-resolution journey.'), ('Experience design', 'The portfolio documents user flows, information architecture and UI artwork.'), ('Interface views', 'Chat screens and development documentation illustrate the proposed experience.')], 'number': '01', 'year': 'YEAR TBC', 'source_pages': '5, 6, 7, 8', 'cover': 'assets/portfolio/conflict-resolver-cover.webp', 'gallery': [('assets/portfolio/conflict-resolver-page-5.webp', 5), ('assets/portfolio/conflict-resolver-page-6.webp', 6), ('assets/portfolio/conflict-resolver-page-7.webp', 7), ('assets/portfolio/conflict-resolver-page-8.webp', 8)]}, {'slug': 'scavenger', 'title': 'SCAVENGER', 'category': 'game', 'type': 'AR GAME / INTERACTION', 'role': 'Illustration, UI design, UX and interaction design', 'format': 'Augmented-reality game concept', 'tagline': 'Learning through an augmented-reality scavenger game for children.', 'lead': 'A playful way to explore health and learning in an unfamiliar time.', 'story': 'Presented in the portfolio as an AR game developed by a team with Eyeread Inc. during the COVID-19 period, SCAVENGER explores educational play and healthy habits for children.', 'approach': 'The showcased screens combine a mobile interface, location and task cues, AR scenes, characters and collectible items. Supporting boards illustrate character and item exploration alongside the prototype flow.', 'outcome': 'The portfolio documents a game concept, multiple interface screens and illustrative assets. Release status and any learning impact are not specified.', 'steps': [('Learning brief', 'The concept is framed around children, health education and pandemic-era learning.'), ('Game experience', 'Mobile prototype screens show the activity flow and AR gameplay views.'), ('Visual assets', 'The portfolio includes character, object and interface illustrations.')], 'number': '02', 'year': 'YEAR TBC', 'source_pages': '9, 10, 11, 12, 13', 'cover': 'assets/portfolio/scavenger-cover.webp', 'gallery': [('assets/portfolio/scavenger-page-9.webp', 9), ('assets/portfolio/scavenger-page-10.webp', 10), ('assets/portfolio/scavenger-page-11.webp', 11), ('assets/portfolio/scavenger-page-12.webp', 12), ('assets/portfolio/scavenger-page-13.webp', 13)]}, {'slug': 'audio-comics', 'title': 'Immersive Audio Comics', 'category': 'design', 'type': 'WEB EXPERIENCE / UX', 'role': 'Project management, visual design, UX and interaction design', 'format': 'Audio-enabled webcomic platform study', 'tagline': 'Making webcomics more accessible through audio and thoughtful interaction.', 'lead': 'Combining comic reading with dialogue, music and sound effects.', 'story': 'The portfolio presents a design study for Dusk Wave Arts: a webcomic experience where audio can accompany reading, particularly for audiences who find text-heavy content difficult to access.', 'approach': 'Presented material includes home, discovery and reader screens; survey charts; sitemap, persona and wireframe examples; plus a project development timeline.', 'outcome': 'The showcased work includes an interface direction and user-research documentation. The submitted PDF also contains testimonials, but their provenance has not been independently verified, so they are not reproduced here.', 'steps': [('Research', 'Surveys and user needs helped frame the reading experience.'), ('Structure', 'Sitemap, persona and wireframe examples document the proposed journey.'), ('Reading interface', 'Web pages explore comic discovery, reading and integrated audio.')], 'number': '03', 'year': 'YEAR TBC', 'source_pages': '14, 15, 16, 17, 18', 'cover': 'assets/portfolio/audio-comics-cover.webp', 'gallery': [('assets/portfolio/audio-comics-page-14.webp', 14), ('assets/portfolio/audio-comics-page-15.webp', 15), ('assets/portfolio/audio-comics-page-16.webp', 16), ('assets/portfolio/audio-comics-page-17.webp', 17), ('assets/portfolio/audio-comics-page-18.webp', 18)]}, {'slug': 'whales-today', 'title': 'Whales Today', 'category': 'design', 'type': 'APP / VISUAL STORYTELLING', 'role': 'Illustration, UI design and UX', 'format': 'Sustainable-lifestyle app concept', 'tagline': 'An ocean-minded app concept connecting awareness, habits and visual storytelling.', 'lead': 'Encouraging attention to whale conservation through a digital experience.', 'story': 'The portfolio frames Whales Today as a sustainable-lifestyle app concept aiming to build awareness of whales and ocean protection.', 'approach': 'Multiple app screens explore information and engagement around conservation. Related boards show accessory and merchandise ideas, including a ring design, tote bag, brochure and small objects.', 'outcome': 'The source materials document prototypes, interface screens and campaign merchandise concepts. Real-world conservation impact or launch status is not established.', 'steps': [('Awareness', 'The brief centers on whales, ocean protection and sustainable living.'), ('App direction', 'Interface prototypes explore routes into information and participation.'), ('Physical touchpoints', 'Merchandise studies extend the message into everyday objects.')], 'number': '04', 'year': 'YEAR TBC', 'source_pages': '19, 20, 21, 22, 23, 24', 'cover': 'assets/portfolio/whales-today-cover.webp', 'gallery': [('assets/portfolio/whales-today-page-19.webp', 19), ('assets/portfolio/whales-today-page-20.webp', 20), ('assets/portfolio/whales-today-page-21.webp', 21), ('assets/portfolio/whales-today-page-22.webp', 22), ('assets/portfolio/whales-today-page-23.webp', 23), ('assets/portfolio/whales-today-page-24.webp', 24)]}, {'slug': 'glasessen', 'title': 'Glasessen', 'category': 'design', 'type': 'BRANDING / GRAPHIC DESIGN', 'role': 'Branding design and visual design', 'format': 'Speculative brand-identity study', 'tagline': 'A speculative visual identity connecting food coatings and material research.', 'lead': 'A brand concept grounded in the protective structure of food coatings.', 'story': 'The portfolio explicitly identifies Glasessen as speculative: a proposed identity for a sausage-coating company informed by insect and chitosan research.', 'approach': 'The wordmark and symbol reference a cross-section and protective coating. The portfolio includes logo studies, a color system, visual applications and a 5.5 × 4 inch brochure concept incorporating a reusable notebook.', 'outcome': 'The presented work shows a logo system, promotional brochure, stationery and environmental mockups; it is not presented here as a commissioned commercial brand launch.', 'steps': [('Research link', 'Insect and food-coating research informs the speculative identity.'), ('Visual identity', 'A round cross-section motif becomes a flexible mark and wordmark.'), ('Applications', 'Brochure, notebook and brand applications test the identity.')], 'number': '05', 'year': 'YEAR TBC', 'source_pages': '26, 27, 28, 29', 'cover': 'assets/portfolio/glasessen-cover.webp', 'gallery': [('assets/portfolio/glasessen-page-26.webp', 26), ('assets/portfolio/glasessen-page-27.webp', 27), ('assets/portfolio/glasessen-page-28.webp', 28), ('assets/portfolio/glasessen-page-29.webp', 29)]}, {'slug': 'forest-friends', 'title': 'The Forest Friends Adventure', 'category': 'art', 'type': 'CHILDREN’S ILLUSTRATION', 'role': 'Illustration and visual design', 'format': 'Storybook illustration', 'tagline': 'A friendly storybook world of forest characters, courage and discovery.', 'lead': 'Building a warm visual world for a young reader’s adventure.', 'story': 'The portfolio describes a children’s storybook about a lively girl who befriends animals in a magical forest, exploring friendliness, courage and curiosity.', 'approach': 'Illustrated scenes, book-cover mockups and character-rich compositions use a soft green palette and layered woodland imagery.', 'outcome': 'The portfolio presents storybook illustration and printed-book mockups; publication details are not provided.', 'steps': [('Story premise', 'A young protagonist meets animals along a forest journey.'), ('Illustration', 'The imagery develops friendly characters and imaginative woodland scenes.'), ('Book application', 'Covers and interior-spread mockups show the storybook direction.')], 'number': '06', 'year': 'YEAR TBC', 'source_pages': '31', 'cover': 'assets/portfolio/forest-friends-cover.webp', 'gallery': [('assets/portfolio/forest-friends-page-31.webp', 31)]}, {'slug': 'contact-lens-guide', 'title': 'Contact Lens Instruction Guide', 'category': 'art', 'type': 'INFORMATIONAL ILLUSTRATION', 'role': 'Illustration and visual design', 'format': 'Instructional illustration series', 'tagline': 'Step-by-step illustrated guidance with a soft, reassuring visual language.', 'lead': 'Communicating care and clarity through practical illustration.', 'story': 'The source portfolio presents a contact-lens instruction series intended to help users understand safe handling and wearing steps.', 'approach': 'The illustrated guide uses soft blue tones, simple line drawing and a compact printed format to emphasize hygiene, gentle handling and a clear sequence.', 'outcome': 'The portfolio shows instruction-sheet and hanging-card mockups. No evidence of clinical review or distribution is provided.', 'steps': [('Instruction brief', 'Make the wearing and handling sequence understandable.'), ('Illustration language', 'Soft blues and simple graphics establish a calm, clean visual tone.'), ('Print format', 'Booklet and card mockups demonstrate the instructional layout.')], 'number': '07', 'year': 'YEAR TBC', 'source_pages': '32', 'cover': 'assets/portfolio/contact-lens-guide-cover.webp', 'gallery': [('assets/portfolio/contact-lens-guide-page-32.webp', 32)]}, {'slug': 'yellow-cover', 'title': 'Yellow / Album Cover Study', 'category': 'art', 'type': 'EDITORIAL ILLUSTRATION', 'role': 'Illustration and visual design', 'format': 'Uncommissioned album-cover interpretation', 'tagline': 'An illustrated visual interpretation of a song, centered on warmth and yellow.', 'lead': 'Translating the feeling of a song into color and portraiture.', 'story': 'The supplied portfolio describes an album-cover design study inspired by Coldplay’s song “Yellow.” It is shown here as an independent interpretation, not an official or commissioned release.', 'approach': 'The design pairs a strongly yellow palette with an abstract illustrated portrait to explore warmth and emotional tone.', 'outcome': 'The portfolio presents a finished cover composition and related mockups; no commercial use or artist affiliation is claimed.', 'steps': [('Music reference', 'The color and emotional tone respond to the song “Yellow.”'), ('Portrait', 'An abstract figure becomes the main illustrative focus.'), ('Cover application', 'The artwork is explored as an album-cover design.')], 'number': '08', 'year': 'YEAR TBC', 'source_pages': '30', 'cover': 'assets/portfolio/yellow-cover-cover.webp', 'gallery': [('assets/portfolio/yellow-cover-page-30.webp', 30)]}, {'slug': 'instagram-design', 'title': 'Instagram / Design Agency', 'category': 'campaigns', 'type': 'SOCIAL MEDIA / INSTAGRAM', 'role': 'Brand visibility, content creation and audience engagement', 'format': 'Social-media promotion case', 'tagline': 'Instagram content and visual storytelling for a design agency.', 'lead': 'Bringing a design practice into a more expressive social feed.', 'story': 'The portfolio describes Instagram promotion for a design agency, including strategic content planning and visual posts to support brand visibility and audience engagement.', 'approach': 'The presented page includes Instagram interface screenshots and summary notes on content design and promotion. The original PDF also reports performance figures, which are excluded from this draft pending confirmation.', 'outcome': 'Source materials document social content and account screenshots. Quantitative results have not been independently checked.', 'steps': [('Content direction', 'The source describes targeted strategies for an agency audience.'), ('Visual posts', 'Feed imagery and social storytelling form the visible work.'), ('Campaign review', 'Account examples are shown; reported metrics await confirmation.')], 'number': '09', 'year': 'YEAR TBC', 'source_pages': '34', 'cover': 'assets/portfolio/instagram-design-cover.webp', 'gallery': [('assets/portfolio/instagram-design-page-34.webp', 34)]}, {'slug': 'tiktok-pets', 'title': 'TikTok / Pet Supplies', 'category': 'campaigns', 'type': 'SHORT-FORM VIDEO / TIKTOK', 'role': 'Strategy, content creation and community engagement', 'format': 'Social video promotion case', 'tagline': 'Pet-focused short-form content mixing product education and personality.', 'lead': 'Creating a playful, practical content rhythm for a pet retailer.', 'story': 'The portfolio describes TikTok promotion for a pet supplies retailer using short-form videos about products and pet care.', 'approach': 'It lists content strategy, video production and audience interaction as project responsibilities; the showcased page includes account and analytics screenshots.', 'outcome': 'The supplied document reports follower and sales changes, but these figures are intentionally withheld from the website draft until substantiated.', 'steps': [('Strategy', 'The portfolio describes planning around pet products and care tips.'), ('Content', 'Short-form videos showcase products and practical information.'), ('Community', 'The brief includes engagement and comment interaction.')], 'number': '10', 'year': 'YEAR TBC', 'source_pages': '35', 'cover': 'assets/portfolio/tiktok-pets-cover.webp', 'gallery': [('assets/portfolio/tiktok-pets-page-35.webp', 35)]}, {'slug': 'xiaohongshu-agency', 'title': 'Xiaohongshu / Design Agency', 'category': 'campaigns', 'type': 'SOCIAL MEDIA / XIAOHONGSHU', 'role': 'Social-media strategy and management', 'format': 'Little Red Book promotion case', 'tagline': 'Campaign planning and social storytelling on Xiaohongshu.', 'lead': 'Supporting a creative agency’s presence on a visual-first platform.', 'story': 'The portfolio presents a Little Red Book (小红书) campaign for a design agency, with account screenshots and an overview of audience growth and engagement goals.', 'approach': 'The project description focuses on platform strategy and account management. The same portfolio page also describes a separate pet accessories campaign; this case study is limited to the design-agency example.', 'outcome': 'The portfolio contains numerical claims about audience and revenue; none are reproduced here without separate verification.', 'steps': [('Platform focus', 'The campaign is built for Xiaohongshu’s visual and community format.'), ('Management', 'The portfolio identifies strategy and account management as core responsibilities.'), ('Portfolio evidence', 'The case is illustrated with screenshots from the supplied portfolio.')], 'number': '11', 'year': 'YEAR TBC', 'source_pages': '36', 'cover': 'assets/portfolio/xiaohongshu-agency-cover.webp', 'gallery': [('assets/portfolio/xiaohongshu-agency-page-36.webp', 36)]}]

VISUAL_STORIES = {'conflict-resolver': [{'page': 8,
                        'file': 'assets/portfolio/conflict-resolver-visual-01.webp',
                        'en': 'Conversation screens and flow states',
                        'zh': '对话界面与交互状态'},
                       {'page': 7,
                        'file': 'assets/portfolio/conflict-resolver-visual-02.webp',
                        'en': 'Information architecture and user journey diagrams',
                        'zh': '信息架构与用户旅程图'},
                       {'page': 6,
                        'file': 'assets/portfolio/conflict-resolver-visual-03.webp',
                        'en': 'Research and technical architecture material',
                        'zh': '研究与技术架构资料'}],
 'scavenger': [{'page': 13,
                'file': 'assets/portfolio/scavenger-visual-01.webp',
                'en': 'Illustrated AR game presentation',
                'zh': 'AR 游戏插画与整体展示'},
               {'page': 10, 'file': 'assets/portfolio/scavenger-visual-02.webp', 'en': 'Mobile interface sequence', 'zh': '移动端界面流程'},
               {'page': 12,
                'file': 'assets/portfolio/scavenger-visual-03.webp',
                'en': 'Characters, objects and process boards',
                'zh': '角色、道具与创作过程'}],
 'audio-comics': [{'page': 14,
                   'file': 'assets/portfolio/audio-comics-visual-01.webp',
                   'en': 'Illustrated webcomic discovery interface',
                   'zh': '有声漫画发现页界面'},
                  {'page': 15,
                   'file': 'assets/portfolio/audio-comics-visual-02.webp',
                   'en': 'Website and reading screen concepts',
                   'zh': '网站与阅读界面概念'},
                  {'page': 18,
                   'file': 'assets/portfolio/audio-comics-visual-03.webp',
                   'en': 'Final visual mockup shown in the portfolio',
                   'zh': '作品集中的最终视觉样机'}],
 'whales-today': [{'page': 20,
                   'file': 'assets/portfolio/whales-today-visual-01.webp',
                   'en': 'Mobile app concept and whale imagery',
                   'zh': '移动应用原型与鲸鱼视觉'},
                  {'page': 21,
                   'file': 'assets/portfolio/whales-today-visual-02.webp',
                   'en': 'Selected product screens',
                   'zh': '应用界面展示'},
                  {'page': 22,
                   'file': 'assets/portfolio/whales-today-visual-03.webp',
                   'en': 'Ring design and physical-object studies',
                   'zh': '戒指设计与实体物件探索'},
                  {'page': 23,
                   'file': 'assets/portfolio/whales-today-visual-04.webp',
                   'en': 'Merchandise and print applications',
                   'zh': '周边与印刷应用'}],
 'glasessen': [{'page': 27,
                'file': 'assets/portfolio/glasessen-visual-01.webp',
                'en': 'Visual research, logotype and mark system',
                'zh': '视觉研究、字标与图形系统'},
               {'page': 28, 'file': 'assets/portfolio/glasessen-visual-02.webp', 'en': 'Printed brand collateral', 'zh': '品牌印刷物料'},
               {'page': 29,
                'file': 'assets/portfolio/glasessen-visual-03.webp',
                'en': 'Identity in context and mockups',
                'zh': '品牌应用场景与样机'}],
 'forest-friends': [{'page': 31,
                     'file': 'assets/portfolio/forest-friends-visual-01.webp',
                     'en': 'Illustrated storybook mockup',
                     'zh': '童书插画与实体书样机'},
                    {'page': 31,
                     'file': 'assets/portfolio/forest-friends-visual-02.webp',
                     'en': 'Illustrated forest story scene',
                     'zh': '森林故事插画场景'}],
 'contact-lens-guide': [{'page': 32,
                         'file': 'assets/portfolio/contact-lens-guide-visual-01.webp',
                         'en': 'Instruction booklet illustration',
                         'zh': '说明手册插画'},
                        {'page': 32,
                         'file': 'assets/portfolio/contact-lens-guide-visual-02.webp',
                         'en': 'Folded instruction card mockup',
                         'zh': '折页说明卡展示'}],
 'yellow-cover': [{'page': 30,
                   'file': 'assets/portfolio/yellow-cover-visual-01.webp',
                   'en': 'Main Yellow illustration study',
                   'zh': 'Yellow 主视觉插画'},
                  {'page': 30,
                   'file': 'assets/portfolio/yellow-cover-visual-02.webp',
                   'en': 'Exploration in cover applications',
                   'zh': '封面应用探索'}],
 'instagram-design': [{'page': 34,
                       'file': 'assets/portfolio/instagram-design-visual-01.webp',
                       'en': 'Instagram account and content examples',
                       'zh': 'Instagram 账号与内容示例'},
                      {'page': 34,
                       'file': 'assets/portfolio/instagram-design-visual-02.webp',
                       'en': 'Content feed and publishing presentation',
                       'zh': '内容发布与视觉信息展示'}],
 'tiktok-pets': [{'page': 35,
                  'file': 'assets/portfolio/tiktok-pets-visual-01.webp',
                  'en': 'Short-form video profile and content',
                  'zh': '短视频账号与内容展示'},
                 {'page': 35,
                  'file': 'assets/portfolio/tiktok-pets-visual-02.webp',
                  'en': 'Selected video and account screenshots',
                  'zh': '视频与账号截图'}],
 'xiaohongshu-agency': [{'page': 36,
                         'file': 'assets/portfolio/xiaohongshu-agency-visual-01.webp',
                         'en': 'Xiaohongshu account and content example',
                         'zh': '小红书账号与内容示例'},
                        {'page': 36,
                         'file': 'assets/portfolio/xiaohongshu-agency-visual-02.webp',
                         'en': 'Visual social platform screenshots',
                         'zh': '视觉社交平台截图'}]}

ICONS = {
 'design': '<rect x="6" y="8" width="36" height="30" rx="2"/><path d="M6 17h36M14 12h.1M20 12h.1M14 24h11M14 30h19"/>',
 'art': '<path d="M24 5c-10 0-19 9-19 19s7 18 17 18c4 0 6-2 6-5 0-2-2-3-2-5s2-4 5-4h5c5 0 8-3 8-8C44 11 34 5 24 5Z"/><circle cx="15" cy="19" r="2"/><circle cx="23" cy="12" r="2"/><circle cx="33" cy="16" r="2"/>',
 'game': '<path d="m13 18-4 2c-3 1-4 5-5 12-1 6 3 9 8 5l8-6h8l8 6c5 4 9 1 8-5-1-7-2-11-5-12l-4-2H13Z"/><path d="M15 23v10M10 28h10"/><circle cx="32" cy="25" r="1.5"/><circle cx="37" cy="30" r="1.5"/>',
 'campaigns': '<path d="M8 19h10l19-9v28l-19-9H8zM17 30l4 10h8M41 17l5-3M41 31l5 3"/>',
 'play': '<path d="M24 5 29 18 43 17 33 27 37 41 24 34 11 41 15 27 5 17 19 18 24 5Z"/><circle cx="24" cy="25" r="3"/>',
}



# V14 source-page first-image covers, exactly the first PDF page in each project.
for _project in PROJECTS:
    _project['pdf_thumb'] = f"assets/portfolio/{_project['slug']}-pdf-first.webp"

def art_markup(project, detail=False):
    """Real cover imagery extracted from supplied PDF, separate from the retained machine icon system."""
    pre='../' if detail else ''
    cls='project-art real-project-art case-art' if detail else 'project-art real-project-art'
    cover=escape(pre+project['cover'],quote=True)
    alt=escape(project['title']+' — artwork and project presentation from the uploaded portfolio',quote=True)
    return f'<div class="{cls}"><img src="{cover}" alt="{alt}" loading="eager" decoding="async"></div>'
