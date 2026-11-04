# A Little Machine for Big Ideas — V16 接手文档

> **当前唯一基准：V16（2026-11-03）**。此前 V10–V15 的设计与交互确认均继续有效。
> **状态**：本地可交互审核版本；未对外部署，也未完成作品公开许可与 CV / 联系信息核验。

## 一、交付包

- `index.html`：**最外层唯一可以双击打开的独立交互预览**，全站 15 个页面通过内置导航和 hash 路由模拟；CSS、JS、图片已嵌入，Font 服务在线加载、离线 fallback。可直接在 Chrome / Edge / Safari 浏览器打开；**不是生产部署所需的全部静态页面**。
- `LittleMachine_V16_FULL_SOURCE.zip`：正式网站完整源码，解压后 `Little_Machine_Portfolio/` 包含四主页面、`projects/` 中 11 个详情页、`assets/styles.css`、`assets/main.js`、`assets/i18n.js`、完整 PDF 页面 WebP 素材、Python 源数据和生成器。
- `A_Little_Machine_Project_Handoff_V16.md`：本交接文档。
- `V16_验收概览.txt`：用户简明操作说明。

**打开方法**：解压交付 ZIP，双击最外层 `index.html`。不要单独移动源码子目录内的 HTML 文件；正式部署应使用源码 ZIP 内的 `Little_Machine_Portfolio/` 目录内容。

## 二、不可擅自修改的品牌与交互

- Contemporary Editorial Design / Expressive Minimalism / Playful 2.5D；Milk `#F7F8F5`、Ink `#17191D`、Blue `#315EFF`、Lime `#C9FF48`、White `#FFFFFF`，本地纸纹。
- 标题 Bricolage Grotesque；正文 Manrope；信息标签 IBM Plex Mono。SHURUI 的两个 U 为蓝色，其他字母包括 REN 为黑色；Home 的 Design/Draw/Build/Play 全黑。
- Home 五模式 Design / Art / Game / Campaigns / Play（中文：设计 / 艺术 / 游戏 / 品牌传播 / 趣味创作）；机器屏幕与便签会响应点击；整张便签跳入对应 Work 筛选；MAKE AN IDEA / 一起聊创意 → Contact；尊重降低动态效果偏好，保留音效开关与较小蓝铅笔光标。
- Home / Work / About / Contact 四个独立页面，sticky nav；语言切换跨页面保持。About 以姓名为标题、经历与教育为时间线。Contact 保留中国与加拿大地图；中文个人所在地只称「中国」，英文描述暂留原定稿、未经确认不更改。
- Work 保留 5 分类及 Play 空态，不新增 Lab/Experiments。11 个项目使用各自**原 PDF 第一页**为 Work 封面，原比例不裁切；Case Study 连续向下展示该项目**所有原 PDF 页面**，可高清放大与前后切换。

## 三、11 个项目

01. Chat IT Out / Conflict Resolver
02. SCAVENGER
03. Immersive Audio Comics
04. Whales Today
05. Glasessen
06. The Forest Friends Adventure
07. Contact Lens Instruction Guide
08. Yellow / Album Cover Study
09. Instagram / Design Agency
10. TikTok / Pet Supplies
11. Xiaohongshu / Design Agency

项目中文名称来自 V15 已核准文案，V16 已拓展到首页精选和 Work 卡片（此前仅在详情页翻译）。原英文名保留。每个详情页显示简介、项目背景、领域、提供资料中的角色、对应 PDF 页数与来源页码、年份待确认；不编造结果。完整 PDF 页面按来源顺序展示。

## 四、V16 相对 V15 改动

- 中英文页面节奏与阅读层级统一精修（段落宽度、章节留白、卡片间距、手机布局）。
- 首页右上删去「第001期 / 持续更新」；机器外侧删去 FIG. 01 / 图01 编号；精选作品区的标签下横线已删除。
- 首页精选与 Work 的项目名称中英文均正确切换。
- 详情首屏重新按“标题及简述 → 概览 → 领域/角色/页数/年份”排列，降低过大字形、提高可读性。
- 详情内 PDF 原页移除叠层纸张与阴影，仅保留轻微边界线及可点击放大提示。
- 修复英文移动端 PDF 阅读区 390px 溢出，未改变原作品比例。

## 五、修改入口

1. 项目数据/英文导读/原图映射：`portfolio_data.py`（真实素材据作品集，仅可核实后修改）。
2. HTML 页面结构、主文案模板：`generate_site.py`。
3. 中文源翻译：`translations.py`；**不直接编辑生成的 `assets/i18n.js`**。
4. 布局与视觉：`assets/styles.css`；交互与联系邮箱：`assets/main.js`。
5. 在 `Little_Machine_Portfolio/` 运行 `python3 generate_site.py`，会重写四主页面、11 详情页和 `assets/i18n.js`。避免只编辑生成后的 HTML 而造成回退。
6. 本地预览：`python3 -m http.server 8000`；网站根目录是源码中的 `Little_Machine_Portfolio`，不是最外层单文件预览。

## 六、测试与遗留问题

- 见 `QA_V16.md`：Chromium 下 11 项 × 两语言 × 1440/390px 共 44 组无脚本错误和横向溢出；320px 亦抽查了各主页面与示例详情。
- 静态源码生成和归档完整性已检查，但**未**执行完整真实设备、多浏览器、屏幕阅读器验收。
- 仍需确认：真实 Portfolio 对外展示授权、未核实的外部营销数字、CV 起止时间、公开邮箱及中国专属联系信息、版权、正式 HTTPS 域名和 SEO。
- 如项目继续迭代，命名 V17、V18……；每轮交付**独立单文件 HTML 预览 + 完整源码 ZIP + 简明 QA**。不要恢复旧 V15 的 PDF 页面投影。
