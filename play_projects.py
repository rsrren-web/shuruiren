"""Live projects supplied by Shurui; descriptions checked against their public UI and README."""
PLAY_PROJECTS = [
    dict(slug='period', title='周期生活助手 / Period', category='play', type='VIBE CODING / WEB APP',
         number='12', role='Vibe coding', tools='HTML, CSS, JavaScript, PWA',
         tagline='A daily space for cycle awareness, mood and everyday routines.',
         story='周期生活助手 brings cycle tracking and everyday wellbeing records into a browser app. Its navigation connects Today, Calendar, Trends and More, with a layered form for recording how the day feels.',
         lead='How can cycle information and everyday observations live together in a simple daily interface?',
         approach='The recording form groups mood, energy, stress, activity, social life, sleep and physical symptoms. The repository documents offline caching and JSON import/export alongside the calendar and trend views.',
         outcome='A publicly accessible web app with a working daily-record interface. Cloud sync reported an unavailable connection during this review; successful synchronization is not claimed. Cycle estimates are for everyday planning, not contraception or diagnosis.',
         caption='Actual daily-record form, shown before any entries were made. Personal cycle history is not shown.',
         live_url='https://rsrren-web.github.io/period/#today', repo_url='https://github.com/rsrren-web/period',
         cover='assets/play/period.jpg', pdf_thumb='assets/play/period.jpg'),
    dict(slug='wenyi', title='问易 / Wenyi', category='play', type='VIBE CODING / WEB APP',
         number='13', role='Vibe coding', tools='React, TypeScript, Vite, Tailwind CSS',
         tagline='An interactive way to explore the I Ching and its sixty-four hexagrams.',
         story='问易 is a static web app for browsing the sixty-four I Ching hexagrams and exploring a question through a randomly selected hexagram. A dark interface pairs classical text with search, navigation and a question field.',
         lead='How can a traditional text become an approachable, explorable browser experience?',
         approach='The app uses a shared detail view for hexagram browsing and question results. The repository documents session-based result persistence and locally generated summary images, with text and image resources bundled into the site.',
         outcome='The live homepage and hexagram directory are publicly accessible. The implementation uses React and TypeScript and is deployed on GitHub Pages. This is an exploration of a cultural text; no predictive accuracy or user-impact metrics are claimed.',
         caption='Actual homepage of 问易, captured from the published project.',
         live_url='https://rsrren-web.github.io/wenyi/', repo_url='https://github.com/rsrren-web/wenyi',
         cover='assets/play/wenyi.jpg', pdf_thumb='assets/play/wenyi.jpg'),
]

PLAY_ZH = {
 'play_live':'打开真实项目 ↗', 'play_source':'查看 GitHub 源码 ↗', 'play_label':'已上线 / 网页项目',
 'play_origin':'真实网站 / VIBE CODING', 'play_screenshot':'真实界面', 'play_notes':'项目记录 / 真实网站与源码',
 'play_back':'返回 PLAY 作品', 'play_stack':'技术栈',
 'play_evidence':'项目介绍依据真实网站与公开仓库；截图采集于 2026-11-06。',
 'work_description':'按领域浏览作品：包括原作品集中的设计案例，以及已上线的 Vibe Coding 项目。',
 'work_bottom_note':'作品集案例与真实网页项目 / 在项目详情中查看来源和网站入口。',
}
_COPY = {
 'period': dict(display_title='周期生活助手', type='VIBE CODING / 网页应用', role='Vibe coding',
   tagline='把周期、情绪与日常状态放在一起记录。',
   story='周期生活助手是一款在浏览器中使用的周期与生活状态记录应用。「今天」「日历」「趋势」「更多」构成主要导航，分层记录表单将每日感受组织在一起。',
   lead='怎样把周期信息与日常观察放进一个简单的每日界面？',
   approach='记录表单按情绪、精力、压力、运动、社交、睡眠和身体症状分组。仓库同时记录了离线缓存、JSON 导入导出，以及日历和趋势视图的实现。',
   outcome='真实网站可以访问并打开每日记录表单。本次查看时云端同步提示连接不可用，因此不宣称已验证同步成功。周期估算供生活安排参考，不用于避孕或医疗诊断。',
   caption='真实的每日记录表单，截图时尚未填写；未展示个人经期历史。'),
 'wenyi': dict(display_title='问易', type='VIBE CODING / 网页应用', role='Vibe coding',
   tagline='在浏览器里探索《易经》与六十四卦。',
   story='问易是一款纯静态的《易经》六十四卦查询与起卦应用。深色界面将经典文字、卦象检索、浏览导航和提问入口放在一起；起卦通过随机选择卦象进行探索。',
   lead='怎样让传统文本成为容易进入、可以探索的网页体验？',
   approach='卦象浏览与起卦结果使用统一的详情组件。仓库记录了在当前标签页会话中保留结果、在浏览器本地生成摘要图片的实现，文字与图片资源随网站提供。',
   outcome='真实首页与六十四卦目录可以公开访问。项目使用 React 和 TypeScript，发布在 GitHub Pages。这里展示的是传统文化文本的交互探索，不宣称预测准确率或未经核实的用户成效。',
   caption='从已发布的问易网站采集的真实首页截图。'),
}
for _slug, _fields in _COPY.items():
    for _key, _value in _fields.items():
        PLAY_ZH[f'project_{_slug}_{_key}'] = _value
    PLAY_ZH[f'project_{_slug}_card_aria'] = '查看「'+_fields['display_title']+'」作品详情'
