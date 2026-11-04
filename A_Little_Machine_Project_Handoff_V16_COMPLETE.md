# A Little Machine for Big Ideas — 网站项目完整交接（V16 · Expanded Handoff）

> **唯一当前基准：V16。** 后续版本从 V17 开始，必须在 V16 真实源码上增量开发。  
> **项目主人：Shurui Ren**；类型：English / 简体中文个人创意作品集（Designer & Illustrator）。  
> **交接整理日期：2026-11-03。**  
> **项目状态：本地可交互审核版；尚未公开部署、尚未取得项目全面公开许可。**  
> 本文是维护和决策交接，不是发布授权，也不表示对真实履历、客户成果或作品版权作过独立核实。

## 0. 给新开发者的 60 秒摘要

1. **别重做设计。** V10–V16 已确定了品牌系统、5 模式 2.5D 创意机器、4 主页面、中文与英文、Work 分类和 Contact 地图。当前基准是 **V16**，不是 V10、V13 或 V15。
2. **开发用源码，审阅用单文件。** `LittleMachine_V16_ONE_CLICK_COMPLETE.zip` 最外层 `index.html` 是自包含**交互预览**，不是正式部署目录；它里面的 `LittleMachine_V16_FULL_SOURCE.zip` 才是**真实网站源码**。正式部署应使用源码中的 `Little_Machine_Portfolio/` 内容。
3. **11 个真实作品集案例**，Design 4 / Art 3 / Game 1 / Campaigns 3 / Play 0。Work 与首页精选使用对应项目**第一张完整原 PDF 页**，原比例不裁切；11 个详情按原 PDF 顺序连续展示合计 30 页，点击可高清查看、缩放、翻页。V16 已删除详情 PDF 页面阴影。
4. **不要虚构**作品职责、项目年份、客户成果、传播数据、公开许可、CV 日期、联系方式。源 PDF 即使带有数字或客户信息，也不代表获准公开发布。
5. 修改生成器、项目数据、翻译、CSS/JS 后，再运行 `python3 generate_site.py`。**它会覆盖 4 个主 HTML、11 个项目详情和 `assets/i18n.js`**；不能只改生成后的 HTML。
6. **每次交付：** 独立可点击的交互 HTML + 完整多页面源码 ZIP + 本轮 QA/变更说明。单文件 HTML 要真正嵌入 CSS/JS/图片；最终 ZIP 从重新解压后的 `index.html` 做浏览器验证，避免“页面无样式”。

## 1. 权威交接资料及优先级

| 文件 / 资料 | 用途 | 优先级与备注 |
|---|---|---|
| `LittleMachine_V16_ONE_CLICK_COMPLETE.zip` | 当前用户可直接下载的审核交付包 | 当前 V16 审核入口 |
| 包内 `index.html` | 一键打开的独立交互预览，嵌入样式、脚本、作品图片 | 仅预览；不是生产源码 |
| 包内 `LittleMachine_V16_FULL_SOURCE.zip` | 正式站点的完整多页面源码和 WebP 素材 | **未来开发/部署的唯一代码基准** |
| `Little_Machine_Portfolio/QA_V16.md` | V16 改动和已完成测试记录 | 当前版本测试记录 |
| `Little_Machine_Portfolio/PORTFOLIO_SOURCE_MAP_V14.md` | 11 个案例的原 PDF 页码及顺序 | **当前 PDF 页面映射准绳** |
| `Little_Machine_Portfolio/V14_PDF_ASSET_MAP.json` | 30 张原始 PDF 页图的机器可读映射 | 当前素材映射 |
| `Little_Machine_Portfolio/portfolio_data.py` | 英文项目数据、项目角色、页图、顺序 | 源数据 |
| `Little_Machine_Portfolio/translations.py` | 中文翻译及当前中文项目显示名称 | 中文内容源 |
| V10 原始交接文档 | 早期经用户确认、仍未废弃的品牌与交互约束 | 与 V16 现状结合使用 |
| 源素材 `job！！！.zip` | 用户上传的 **37 份单页 PDF** 原始 Figma 作品集导出 | **素材源证据，建议新对话随同上传** |

**有冲突时**：首先以用户在当前对话中最新明确确认的要求为准，其次核对 V16 的实际源码、`QA_V16.md` 和当前 PDF 映射，再参考较早文档。README 含旧版历史记录，不能把其中 V13 的数量或展示方式误当作 V16 现状。

## 2. 版本演进与冻结规则

| 版本 | 核心进展 | 不能回退的决定 |
|---|---|---|
| V10 | 多页面、中英双语、2.5D Creative Machine、五模式、联系地图、风格定稿；当时 6 个**演示**项目 | V10 品牌和交互原则 |
| V11 | 导航键盘体验等维护与 README 梳理 | 不重建项目 |
| V12 | 从用户上传 PDF 接入 11 个真实作品集项目、相关图像及案例 | 用真实资料替换演示项目；不编造成果 |
| V13 | 真实图像封面、详情内容、图片查看功能增强 | 作品有图有背景，不只显示标题 |
| V14 | **第一张原 PDF 页作封面；详情全部 PDF 页面按原顺序连续阅读**；高清查看器 | 不再强行裁切/拼贴，保留原版式 |
| V15 | 双语文字与间距、中文编辑标题、原 PDF 页纸张展示、多个推荐项目入口、首页精选图比例 | 同步验收中英文，项目推荐清晰可点击 |
| **V16** | 全站中英文留白精修；删首页多余标签/线条；Work/Home 中文项目名；详情首屏信息层级重排；**移除 PDF 阴影**；修小屏溢出 | **当前唯一代码与视觉基准** |

**V16 不是完全发布完成品。** 当前的 11 个真实项目已接入，案例页与原作品集原页有关，但仍缺少项目公开许可和个人履历/联系信息的最终核实。

## 3. 品牌系统（严禁擅自推翻）

- **网站名称**：`A Little Machine for Big Ideas`。
- **定位**：设计、插画、数字媒体交叉的个人作品集，不是套模板的企业宣传站。
- **视觉方向**：Contemporary Editorial Design / Expressive Minimalism / Playful 2.5D / Typography-first Layout；现代、精致、趣味、克制、留白、纸张触感、微妙不对称。
- **主配色**：Milk White `#F7F8F5`；Ink Black `#17191D`；Electric Blue `#315EFF`；Acid Lime `#C9FF48`；White `#FFFFFF`。
- **字体**：Bricolage Grotesque（大标题）；Manrope（正文、导航）；IBM Plex Mono（标签、机器 UI）。目前通过 Google Fonts 在线加载，离线使用回退字体；不要随意替换为通用商业字体。
- **纸纹**：`assets/paper-grain.png`。本地蓝色铅笔鼠标资源 `assets/pencil-cursor.png` / `.svg`。触控设备用正常触控。
- **姓名字标**：`SHURUI REN` 中 **SHURUI 的两个 U 为 Electric Blue**，SH、R、I 和全部 REN 字母为 Ink Black；首页、About、页脚视觉一致。
- **首页名字下的 Design / Draw / Build / Play**：无论英语或中文，**所有文字都为黑色**，不能恢复蓝色局部词。
- **动效原则**：节制、清晰、适度有触感；尊重 `prefers-reduced-motion`；绝不能牺牲文字清晰度，尤其不得对整台机器及其文字层施加造成模糊的强透视缩放。
- **PDF 原页视觉**：完整页面、等比例、干净边界；**V16 明确删除 PDF 背后的叠层纸和阴影**，不要在下一版本偷偷加回去。机器本体的 2.5D 厚边框和立体阴影不受此限制。

## 4. 全站页面结构与必须保留的交互

### 4.1 导航和全局

- 四个独立正式页面：`index.html`、`work.html`、`about.html`、`contact.html`。11 个案例各有 `projects/{slug}.html`。
- 顶部 sticky navigation，Home / Work / About / Contact；桌面与手机均需可访问，手机菜单支持正常开合与键盘关闭。
- English / 简体中文切换，**不把用户送回首页**；跨页语言选择保存在 localStorage（`little-machine-language`）。音效开关状态亦持久化。
- 中英文均应完整校对：不是先把中文“修好”而英文保持旧版，也不能让中文强行逐字翻译原作品名。

### 4.2 Home

- 保留编辑式大标题、**SHURUI REN**、设计理念、蓝色 2.5D **Creative Machine**、便签与作品精选。
- 五个模式：**Design / Art / Game / Campaigns / Play**；中文对应 **设计 / 艺术 / 游戏 / 品牌传播 / 趣味创作**。按钮切换机器屏幕与动态提示，伴随轻微微动效及便签反馈。
- `MAKE AN IDEA`（英文）/ `一起聊创意`（中文）**只跳 Contact**，不是自动生成创意的行为。
- 机器下整张便签均可点击，跳到 `work.html?category=<mode>`；便签视觉重叠**不得盖住 MAKE AN IDEA 字样**。需要绿色行动提示、悬浮/箭头反馈。
- 保留点击/悬浮微音效、可见声音开关；在首次用户交互前不能自动发声。
- **V16 已删除**首页右上 `ISSUE Nº 001 / ALWAYS IN PROGRESS`（中文「第001期 / 持续更新」）和机器外侧 `FIG. 01 / 图01` 字样；**不要恢复**。不等于删除所有章节编号（例如章节区块编号依然存在）。
- 第二部分精选作品使用**各项目完整 PDF 第一页的缩小版**，无裁切、自然比例、可点击；精选区标题栏底部的装饰性横线已删除。当前精选显示：Chat IT Out / Conflict Resolver、SCAVENGER、The Forest Friends Adventure。
- 首页精选项目名称在中文状态显示中文编辑标题，英文状态显示原英文名称。

### 4.3 Work

- **一个统一的作品库**，不另外创建 Labs / Experiments 页面。
- 筛选项：All / Design / Art / Game / Campaigns / Play；从便签传入 `?category=` 要自动选中，兼容旧查询 `?category=illustration` → `art`。
- 当前 11 个真实案例；**Play 分类保留可用空态**，不得为填满它而编造作品。
- 桌面编辑式两列，手机单列；统一页面展示宽度与间距，图片不裁切，采用原 PDF 页的 1728:1117 横向比例，`object-fit: contain`。
- Work 中每一个封面**必须是该项目原 PDF 的第一张页面**，不是自动生成的拼贴图或某张“最吸引人”的局部截图。卡片标题、分类、项目简介均保持中文/英文同步，整个卡片可点击。

### 4.4 Project Detail（11 个独立 Case Study）

- 当前首屏顺序：**标题与简述 → 项目概览 → 项目事实（领域 / 我的角色 / 来源页数与页码 / 年份待确认）**。中英文同等注重对齐、正文行距、版心和留白。
- 中文页面以流畅的中文**编辑展示名**为主，英文原名作为作品识别补充；英文页面保留真实原项目名称。不把中文编辑标题误认为原 PDF 的官方项目名称。
- 内容：来源 PDF 可支持的项目简介、背景、设计过程/设计内容、来源页码及全部对应原页。**原页完整呈现 ≠ 所有文案、职责、成果已经最终核实。**
- 详情中**按 PDF 原始顺序连续向下滚动阅读**；不能回到单页幻灯片主阅读方式，也不能裁掉 PDF 内容。完整原页高清图为 3456×2234 WebP。
- 每一页能点开阅读层，默认适应窗口完整显示；支持放大/缩小、重置、拖动查看、前后翻页；键盘方向键、Esc 等，手机支持触控。放大和原页阅读可达性需继续测试。
- V16 **没有 PDF 叠纸阴影**；请勿恢复。页间靠留白、规则的细边界和辅助页码区分。
- 旧的超大 `Next Project` 改为**三个明确可点击的推荐项目卡片**，具缩略图/标题/行动入口与查看全部作品入口；两种语言均要让人一眼知道可点击。
- 删除过于口号化/冗余的详情阅读标题（此前要求删除「每一页，完整呈现」）；当前阅读区以简练的「原始作品页面」等标题表达。

### 4.5 About

- 顶部以 **SHURUI REN** 为主标题（非巨大通用 `ABOUT`）；两个 U 蓝色，REN 黑色。
- 介绍与理念须保留用户原始中文意思：跨 Design / Illustration / Digital Media，问题驱动、跨领域连接、插画叙事与手作温度、屏幕界面与动效的情绪、观察力与连接力、诗意留白、有意图的动效、技术与诚意。
- 当前主要内容：创作理念、What I Do、Experience、Education、Beyond the Screen；工作/教育均为**编号纵向时间线**，不是阴影点击卡片。
- Experience 已列出 Ruoshui Design and Art Agency — Lead Designer；Justice Institute of British Columbia — Product Manager (Industrial Project)；DijiBC — Lead Designer (Industrial Project)；WeUsThem Design Agency — Junior Designer。JIBC / DijiBC 使用 **Industrial Project**，绝不擅自改回 Internship Project。
- Education 已列出 Master of Digital Media — Simon Fraser University；Bachelor of Design — NSCAD University（Interdisciplinary Design major / Illustration minor）。
- CV 原件与日期尚未最终核实，不得补造年份或提供假的 CV PDF 下载链接。
- About 的抽象草图是**占位视觉**，不能称为个人真实画像或已完成作品。将来用有公开权的原创素材替换。
- 中文个人所在地只写 **中国**，不出现具体城市/省份；英文版本保留既有 Vancouver / Canada 文案，**除非用户明确重新确认**，不擅自统一两种语言。

### 4.6 Contact

- 保留独立 Contact 页面与可交互中国/加拿大 SVG 地图；点击高亮国家或标记切换联系地区面板。
- 两种联系方式地区不等同于用户在两国均有常住地。
- 中文个人所在地只写「中国」；保留两个可选联系地区。英文的 Vancouver / Canada 描述是历史决定，仍有待上线前核实。
- 网站通用邮箱集中写在 `assets/main.js` 的 `PERSONALIZE.email`；**公开发布前必须核实是否允许展示**。中国地区专属邮箱/微信/电话尚未提供，不得编造。
- V15/V16 已对**中文和英文**的大标题行距、断行和留白做同步修订；任何新修改都必须跨语言、桌面及手机检查。

## 5. 11 个项目：名称、分类、原页及真实性说明

> 表格中的中文名称是**V16 现有中文编辑显示名**，不是用户逐个签字核准的官方项目名。英文名称是原作品识别名称。所有案例均根据用户作品集整理，不等于获得对外发布许可；角色、项目年份和成果仍待主人确认。

| # | 英文原名 / slug | 当前中文显示名 | Work 分类 | 原 PDF 页（该项目连续展示顺序） | 页数 |
|---|---|---|---|---|---:|
| 01 | Chat IT Out / Conflict Resolver (`conflict-resolver`) | 让对话有解 | Design | 5, 6, 7, 8 | 4 |
| 02 | SCAVENGER (`scavenger`) | 寻宝小冒险 | Game | 9, 10, 11, 12, 13 | 5 |
| 03 | Immersive Audio Comics (`audio-comics`) | 让漫画发声 | Design | 14, 15, 16, 17, 18 | 5 |
| 04 | Whales Today (`whales-today`) | 与鲸同行 | Design | 19, 20, 21, 22, 23, 24 | 6 |
| 05 | Glasessen (`glasessen`) | 一层之间 | Design | 26, 27, 28, 29 | 4 |
| 06 | The Forest Friends Adventure (`forest-friends`) | 森林里的新朋友 | Art | 31 | 1 |
| 07 | Contact Lens Instruction Guide (`contact-lens-guide`) | 温柔的指引 | Art | 32 | 1 |
| 08 | Yellow / Album Cover Study (`yellow-cover`) | 一抹黄色 | Art | 30 | 1 |
| 09 | Instagram / Design Agency (`instagram-design`) | 设计，正在发声 | Campaigns | 34 | 1 |
| 10 | TikTok / Pet Supplies (`tiktok-pets`) | 毛孩子的日常 | Campaigns | 35 | 1 |
| 11 | Xiaohongshu / Design Agency (`xiaohongshu-agency`) | 让灵感被看见 | Campaigns | 36 | 1 |

**统计**：11 案例、30 原始案例页面，Design 4 / Art 3 / Game 1 / Campaigns 3 / Play 0。上传原始素材包共 37 个单页 PDF，不是 37 个全部被分配给案例。`26-1.pdf` 等可能是章节/分隔或非案例页；不要为了凑页数将其强行添加。来源映射请以 `PORTFOLIO_SOURCE_MAP_V14.md` 和 `V14_PDF_ASSET_MAP.json` 为准。

**重点的案例真实性与出版风险**：

- Conflict Resolver / Chat IT Out：设计稿、架构、交互与 AI 辅助对话方向存在于来源；不能把团队级技术实现全部归功于单个设计师。
- SCAVENGER：作品集说明与 Eyeread Inc. 的团队背景；不要杜撰正式上线、教育效果或独立开发关系。
- Immersive Audio Comics：有网站设计和研究；源页可能含推荐/评价，真实性与授权尚未独立核实。
- Whales Today：鲸鱼保护、应用与相关物料概念；不能杜撰保护成效或正式发布。
- Glasessen：**speculative / 概念品牌**，不能写成真实客户正式上市项目。
- Yellow：对现有歌曲的**非委托视觉演绎**，不能暗示正式唱片公司合作、授权封面或官方发布。
- Instagram / TikTok / Xiaohongshu：素材中存在传播或数字表现信息；对外文案避免未经核实的数据、客户身份、保密信息、账户截图。
- 其他插画/教程作品：需核实作者贡献、素材权利与是否允许公开展示。

## 6. PDF 原页与图像素材规范

- 原始素材：用户上传 `job！！！.zip`，内含 37 个单页 PDF。**请保留原文件**，它是未来再渲染高质量图片、核对内容与权属的证据。
- 工作封面：`assets/portfolio/{slug}-pdf-first.webp`；原画面比例为 **1728×1117**；每项目从对应源 PDF 的**第一页**取材，不裁切不变形。
- 详情高清页：`assets/portfolio/{slug}-page-{N}.webp`，原始渲染尺寸 **3456×2234**。页面顺序由 `portfolio_data.py` 中 `gallery` 与 `V14_PDF_ASSET_MAP.json` 决定。
- `assets/portfolio/` 当前还有 11 个 `{slug}-cover.webp` 旧版资源；**不应把这些早期封面/局部裁切重新用在 V16 Work 或详情原页阅读中**。
- 该目录共 **52 个 WebP**：11 张原页缩略封面 + 30 张高清原页 + 11 张旧封面资源。不要将历史 README 中的“67 张”误称为 V16 当前资源数量。
- 图片可能保留用户原始 PDF 中的客户名称、数字、评价或第三方素材。网站的文案即使未重复某个数字，**图片里依然可能看得到**：正式上线前必须逐页审查，必要时征得用户确认再对公开版作遮挡/替换。

## 7. 文件树与源文件维护职责

```text
LittleMachine_V16_ONE_CLICK_COMPLETE.zip
├── index.html                       # 唯一直接打开的独立预览（内嵌 CSS/JS/图像）
├── LittleMachine_V16_FULL_SOURCE.zip  # 正式网站源代码 ZIP
├── A_Little_Machine_Project_Handoff_V16.md
├── 00_先读_点击打开说明.txt
└── V16_项目详情_中文效果.png

LittleMachine_V16_FULL_SOURCE.zip
└── Little_Machine_Portfolio/
    ├── index.html                  # 生产首页
    ├── work.html                   # Work 列表及筛选
    ├── about.html                  # 简介/经历/教育
    ├── contact.html                # 地图与联系信息
    ├── projects/                   # 11 个独立 Case Study HTML
    ├── assets/
    │   ├── styles.css             # 共用视觉、排版、响应式、动画
    │   ├── main.js                # 导航、语言、音效、筛选、机器、图片阅读器、邮箱
    │   ├── i18n.js                # **自动生成**的翻译文件
    │   ├── portfolio/             # 52 个 WebP（原页、缩略封面及旧封面）
    │   ├── paper-grain.png
    │   ├── pencil-cursor.png
    │   ├── pencil-cursor.svg
    │   └── favicon.svg
    ├── portfolio_data.py           # 11 项真实项目的英文源数据、详情图与角色字段
    ├── translations.py            # 中文译文和中文编辑标题源
    ├── generate_site.py           # 生成主页面/项目页/i18n
    ├── templates/world-map.html    # 交互地图 SVG 模板
    ├── V14_PDF_ASSET_MAP.json
    ├── PORTFOLIO_SOURCE_MAP_V14.md
    ├── PORTFOLIO_SOURCE_MAP_V13.md
    ├── V13_ASSET_MAP.json
    ├── QA_V11.md … QA_V16.md
    ├── README.md
    └── A_Little_Machine_Project_Handoff_V16.md
```

### 修改与再生成流程

1. 将源码 ZIP 解压，进入 `Little_Machine_Portfolio/`。用版本控制或先备份完整项目目录。
2. 修改项目题名、背景、类型、职责、PDF 页图及顺序 → `portfolio_data.py`；核对原始 PDF 和来源映射后修改，不得编造数据。
3. 修改中文翻译、中文项目显示名、标签 → `translations.py`；文案中的英文模板、布局结构 → `generate_site.py`。
4. 修改字号、留白、响应式、机器与 PDF 显示样式 → `assets/styles.css`；菜单、语言、Work 筛选、机器、Contact、高清阅读器 → `assets/main.js`。
5. 在网站目录运行 `python3 generate_site.py`。它会**覆盖并再生成** `index.html`、`work.html`、`about.html`、`contact.html`、11 个 `projects/*.html` 和 `assets/i18n.js`。**勿只改生成后的 HTML 或 i18n.js。**
6. 本地检查：`python3 -m http.server 8000`，访问 `http://localhost:8000/`；或直接双击源码的 `index.html`，但部分路径/跨浏览器功能以服务器预览为准。
7. **单文件预览不是由现有 `generate_site.py` 自动生成**。需要单独从**最新的正式页面与素材**制作 HTML 自包含包装，不能把依赖外部 `assets/styles.css` 的生产 `index.html` 直接改名当单文件预览。
8. 每版交付两个核心物：可打开的最新**自包含 HTML 预览**、完整**多页面源码 ZIP**；如继续采用一键 ZIP，最外层只放一个明显的 `index.html` 入口，内部源码请继续单独 ZIP 收纳。

## 8. 实际验证与测试范围（不可夸大）

### 来源已有 V16 QA（`QA_V16.md`）

- Chromium 下 11 案例 × 英/中 2 种语言 × 1440/390px 2 个视口 = **44 组详情审查**；记录为无 JavaScript 页面错误、无横向溢出、四项事实信息正常、PDF 原页无阴影。
- 320px 视口对主页面及示例详情有抽查，无报告的横向溢出。
- Work 的 11 个中文显示名、首页精选中文显示名、高清阅读器点击/150% 放大/Esc 关闭等已测。
- 源预览嵌入必要图片/图标/纸纹，Google Fonts 仍在线请求，离线使用 fallback。
- V16 审阅版本由最终 ZIP 解压出的 `index.html` 在 Chromium 中作过样式/内容渲染验证。

### 本次扩充交接时额外复核

- `LittleMachine_V16_ONE_CLICK_COMPLETE.zip`：**5 个条目**，压缩包 CRC 完整性检查通过；最外层只有一个 HTML 入口。
- `A_Little_Machine_Full_Source_v16.zip`：**90 个条目**，压缩包 CRC 完整性检查通过；正式站点 15 个 HTML（加 `templates/world-map.html` 模板使 ZIP 内 `.html` 文件总数为 16）。
- 在独立副本运行 `python3 generate_site.py`：退出码 0；**15 个正式页面 + `assets/i18n.js` 重新生成后 SHA-256 与原始 V16 文件一致**。
- 15 个正式 HTML 的本地 `href`/`src` 路径逐项检查：**无缺失路径**。
- `assets/portfolio` 中确认为 52 个 WebP；项目 `gallery` 映射合计 30 页，11 个项目、分类数量与交接一致。

### 未经完整验收，不能写“全部正常”

- 未完成完整 Safari / Firefox / Edge 实体环境、iOS/Android、平板和真实触屏手势测试；已有 Chromium 视口模拟不等于实体设备测试。
- 未完成屏幕阅读器、全键盘路径、WCAG 对比度与焦点、可缩放文字、音效偏好和动效偏好在所有平台的完整验收。
- 未完成真实公网 HTTPS 的深链、相对路径、缓存、图像性能、SEO、社交分享卡片等验收。
- 未完成 11 案例逐条法律/版权/客户授权与数字真实性审核；**本地能打开不等于可以上线**。

## 9. 已知风险、未完成事项与优先级

### P0 — 正式发布前必须解决

1. **作品许可**：与主人逐个确认 11 项能否公开，涉及客户、团队、社媒账号截图、标志、照片、插画、引用、人物资料的权限；尤其官方/非官方关联和机构名称。
2. **原页隐私与真实性**：原始 PDF 图里可能有无法公开的 KPI、客户信息、评价或截图；逐页检查。审核版忠实保留原图，发布版可能需经过主人批准后处理敏感内容。
3. **角色/日期/成果**：向主人核实每个案例的个人职责、年份、团队协作、成果表述；不凭空补写“独立负责”“成功提升”等声明。
4. **CV**：取得/核实最终 `SR's CV.pdf`（或用户提供的权威 CV）；Education/Experience 目前沿用旧交接摘要，不推测起止时间。源作品集中的简历页 `2.pdf` 可作参考，但不自动代替正式 CV 核对。
5. **联系方式与地址**：确认 `PERSONALIZE.email` 是否对外公开；如需微信/电话/中国邮箱由主人提供；英文 Vancouver / Canada 文案是否仍符合个人期望需主人确认。中文个人所在地仍只写「中国」。
6. **About 占位素材**：核实其是否需要替换为用户授权原创插画/个人图像；在未替换前不能误称为本人真实作品。

### P1 — 上线质量与持续精修

1. 双语完整 QA：Home / Work / About / Contact / 11 Case Study，在 320、390、768、1024、1440px 等典型视口和不同操作系统浏览器核对断行、字号、留白、对齐、图片完整显示。
2. 继续检查小字可读性、信息层级和无障碍：键盘可达、语义标题、焦点、图片描述、弹层滚动锁定/焦点返回、放大拖动、动效降低模式、音效开关。
3. 检查 PDF 高清资源、懒加载与性能。原页 WebP 较大；可在不改变原图的前提下提升缓存、压缩与优先级。
4. 校对 11 个中文编辑标题及英文原名、项目简介与“我的角色”。当前中文显示名已实现，不表示用户逐条最终审定。
5. 检查 metadata、Open Graph、favicon、标题、外链和邮件行为；彻底清理 README 的历史旧版内容，但不要误删已确认功能。
6. 建立可重复的正式源码 ↔ 自包含预览生成流程，消除“预览更新了但源码没更新”的风险。

### P2 — 部署与域名

1. 取得主人明确的“可以公开”的确认后，使用**正式源码** `Little_Machine_Portfolio/` 内容发布到 Netlify / Cloudflare Pages / GitHub Pages 等静态托管；**不要直接把审阅预览的单页 `index.html` 当多页面网站上线**。
2. 测试真实 HTTPS URL：主导航、11 项深链、Work 筛选参数、跨页语言、地图、邮件、PDF 高清图和字体。
3. 如有自定义域名，再配置 DNS、SEO、社交媒体预览以及最小必要统计（尊重隐私）。

## 10. 用户已明确确认 —— 不必重复提问

- 名称、编辑式极简+Playful 2.5D 创意机器方向与指定配色/字体系统。
- 蓝色铅笔光标、轻量悬浮/点击音效、可见开关、机器微动效、降低动态效果偏好。
- Home / Work / About / Contact 四主页面、sticky nav、独立 Work、五分类（Design / Art / Game / Campaigns / Play）、中文对应分类。
- `MAKE AN IDEA` / `一起聊创意` 跳 Contact；整张灵感便签跳对应 Work 分类，不能遮住按钮字。
- SHURUI 两个 U 蓝、REN 黑；首页 Design/Draw/Build/Play 文字黑；About 大字用姓名；Experience/Education 编号时间线；JIBC/DijiBC 为 Industrial Project。
- 中文个人所在地只写「中国」，不写省市；中加联系地图仍保留；英文历史描述未经新确认不自动统一。
- V14 起 Work 每项用**原 PDF 第一页**完整缩略封面；详情按原顺序**连续纵向滚动**显示每一页；点击高清放大、前后切换，不进行局部裁切。
- V15 起中英文同等精修，项目推荐变成 3 个明显可点的小卡片；首页精选图片遵循原 PDF 比例。
- V16 起删除首页多余“第 001 期/持续更新”和“FIG. 01/图01”标注、精选标题下装饰线；首页与 Work 中文显示对应的中文编辑项目标题；详情首屏更易读；**删除可点击 PDF 页背后阴影**。
- 后续每次都需可用的完整交付，不接受“打开后只有源码文字/缺 CSS”的预览体验。**从最终 ZIP 解压后验证真实入口**。

## 11. 经常犯错 / 明确禁止回退

- **错把自包含预览当部署源码**；或只移动生产 `index.html`，导致 `assets/styles.css` 失联，网页变成蓝色超链接和纯文本默认布局。
- **混淆两个 index.html**：当前一键 ZIP 最外层唯一 HTML 是独立预览；内部源码压缩包的 `Little_Machine_Portfolio/index.html` 才是生产首页。请在交付说明中讲清二者。
- **只改生成结果，不改生成器/翻译源**；再次生成就丢改动。
- 恢复 V13 的局部裁切、拼图封面或 V15 的 PDF 阴影；随意改变 PDF 页顺序；把 11 项说成只有标题。
- 为 Play 类别造一个没有来源的项目，或重建 Lab / Experiments 页面。
- 中英只改一种语言，不同步检查另一种语言的字号、换行和留白。
- 把未经核实的客户、技术、贡献、发布日期、CV 日期或 KPI 写成既定事实。
- 误以为用户仅提供 PDF 就授予所有第三方素材的公开发布权限。
- 使用无法公开分享的 sandbox 链接充当已部署的正式网站地址。

## 12. 下一次迭代的安全工作流程

1. 获取 V16 一键 ZIP 和原始 PDF ZIP；解压 V16 完整源码并建立独立 V17 工作目录。
2. 先阅读本文、`QA_V16.md`、`PORTFOLIO_SOURCE_MAP_V14.md`；实际打开审核版确认当前外观，记录变更前截图。
3. 逐条将用户的新增要求写入变更清单，并标记“保留、不动”的模块；**不做无关重构**。
4. 只改对应的 `portfolio_data.py`、`translations.py`、`generate_site.py`、`assets/styles.css`、`assets/main.js` 以及必要素材；修正当前问题，不恢复旧版本被否决的视觉。
5. 生成 → 核对页面与翻译 → 浏览器测试中英文及多视口 → 检查 11 项/30 页及分类筛选 → 测试图片阅读器/机器/地图/导航 → 检查真实发布风险。
6. 产出新版单 HTML 自包含预览，**从最终 ZIP 实际解压**，用电脑浏览器检验只有一个明显打开入口、页面不是纯文本、图片都有、导航能点、样式正常。
7. 打包完整开发源码、编辑说明和 QA 结果；明确“已完成、未完成、待确认”，交付新版 **V17**。除非用户另行授权，不主动上线或替用户公开网站。

## 13. 给下一段 ChatGPT / 新开发者可直接复制的交接指令

> 请接手 Shurui Ren 的 **A Little Machine for Big Ideas** 中英双语个人作品集网站。**以随附 V16 正式多页面源码为唯一基准，从 V17 继续迭代，不要从头设计。** 请先阅读 `A_Little_Machine_Project_Handoff_V16_COMPLETE.md`、源码内 `QA_V16.md` 与 `PORTFOLIO_SOURCE_MAP_V14.md`，并打开 V16 顶层自包含 `index.html` 对照现有设计。
>
> 严格保留 Electric Blue / Milk White / Acid Lime 编辑式排版、纸纹与字体、SHURUI 两个蓝色 U、倾斜 2.5D 机器、五模式、可点击灵感便签、MAKE AN IDEA/一起聊创意跳 Contact、双语跨页保持、Work 11 个真实案例与五分类、中国/加拿大地图及中文版所在地仅写“中国”等既定决定。
>
> **Work 采用 11 个项目各自原 PDF 第一页的完整等比例缩略图；11 个详情页按各自原 PDF 页序连续展示共 30 页、支持高清放大/缩小和前后切换，不能裁切或恢复 PDF 阴影。** 首页精选采用完整 PDF 比例，中文 Work/Home 显示现有中文编辑标题，英文保持原名。保留 V16 对中英文共同的字号、对齐和留白修订。旧的“第 001 期/持续更新”“FIG. 01/图01”及精选区装饰横线不恢复。详情页有清晰的标题、简介和四项项目事实，并有 3 个可点击的相关项目推荐。
>
> 内容取自用户提交的 37 页 PDF 素材 `job！！！.zip`，以 `PORTFOLIO_SOURCE_MAP_V14.md` 和 `V14_PDF_ASSET_MAP.json` 为准。项目角色、年份、公开许可、传播数字、CV 及联系方式仍未最终验证，不许编造或直接公开网站。
>
> 开发前先核对源文件；修改项目/翻译/模板/样式/交互时更新对应 `.py`、CSS、JS，运行 `python3 generate_site.py`，不要只改生成的 HTML。中英文与桌面/手机必须同等验收。每轮交付新版**完整 HTML 自包含预览 + 正式多页面源码 ZIP + QA/变更说明**，并**从最终 ZIP 解压后实际打开预览进行样式、素材和交互验证**，避免再次出现无样式纯文本网页。

## 14. 完整性标识（供接手核验）

- `LittleMachine_V16_ONE_CLICK_COMPLETE.zip`：**SHA-256** `7fc50bd55824027d9104349ac18c9cd90c5792542b36480bf6a6b1dcb4586616`
- `A_Little_Machine_Full_Source_v16.zip`（与一键包内同版源码）：**SHA-256** `288cf4dc407637ae247613e500a8a52e45bbb1dac132b835e492c11f08317a64`
- 如新开发者收到的 ZIP 与此哈希不同，需确认是重命名还是内容已更新；不能在未核查的情况下称其为原样 V16 基准。

---

**交接结论：** V16 已具备完整的品牌视觉、多页面双语架构、11 个来自原作品集的案例、30 张 PDF 原页连续阅读和高清放大。**未完成对外授权、履历/联系信息核实、全部真实设备与跨浏览器验收及正式部署。** 下一步从 V16 安全增量迭代，而不是重新设计或直接公开上线。
