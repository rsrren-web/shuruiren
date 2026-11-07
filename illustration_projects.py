"""Illustration supplied directly by the portfolio owner."""
from html import escape

ILLUSTRATIONS = [dict(
    slug='live-in-the-present', title='Live in the present', category='art',
    type='ILLUSTRATION', number='14', artwork=True,
    tagline='Traditional drawing techniques meet digital colour, line and texture.',
    cover='assets/art/live-in-the-present.png',
    pdf_thumb='assets/art/live-in-the-present.png',
)]

ART_ZH = {
 'project_live-in-the-present_display_title':'Live in the present',
 'project_live-in-the-present_type':'插画',
 'project_live-in-the-present_tagline':'传统绘画技巧，与数字色彩、线条和肌理相遇。',
 'project_live-in-the-present_card_aria':'查看 Live in the present 插画作品',
 'art_label':'插画作品', 'art_back':'返回艺术作品',
 'art_view':'放大查看完整作品 ↗', 'art_medium':'工具与技法',
 'art_traditional':'传统绘画技巧', 'art_about':'关于这幅作品',
 'art_present_about':'人物、手绘线条与颗粒肌理分布在画面两侧，中央由柔和的渐变色与流动的白色曲线连接。作品结合 Procreate、Adobe Illustrator 与传统绘画技巧。',
}

def render(p,base_open,finish,recommendations):
    image='../'+p['cover']
    return base_open('project',p['title'],True,p['tagline'])+f'''<article class="page-wrap art-piece">
    <div class="case-top"><a class="back-link" href="../work.html?category=art">← <span data-i18n="art_back">BACK TO ART</span></a><span class="mono">14 / ILLUSTRATION</span></div>
    <header class="art-heading"><span class="mono" data-i18n="art_label">ILLUSTRATION</span><h1>Live in the present</h1><p data-i18n="project_live-in-the-present_tagline">{p['tagline']}</p></header>
    <figure class="art-full" data-protected-art><img src="{image}" alt="Live in the present — illustration by Shurui Ren" width="2880" height="1646" fetchpriority="high" draggable="false"><figcaption><span class="mono">LIVE IN THE PRESENT</span><span class="mono">© SHURUI REN</span></figcaption></figure>
    <section class="art-description"><div><span class="mono" data-i18n="art_about">ABOUT THE ARTWORK</span><p data-i18n="art_present_about">Figures, drawn lines and grainy textures gather on either side of the composition, connected by soft colour gradients and flowing white curves. The piece combines Procreate, Adobe Illustrator and traditional drawing techniques.</p></div><div><span class="mono" data-i18n="art_medium">TOOLS & TECHNIQUES</span><ul><li>Procreate</li><li>Adobe Illustrator</li><li data-i18n="art_traditional">Traditional drawing techniques</li></ul></div></section>
    {recommendations(p)}</article>'''+finish(True)
