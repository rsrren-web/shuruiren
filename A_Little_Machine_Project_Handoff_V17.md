# A Little Machine for Big Ideas — V17 交接补充

> **当前唯一基准：V17（2026-11-03）**。正式编辑基于 `Little_Machine_Portfolio/` 源码；不可从 V10–V16 重新设计或覆盖。此前 V16 完整交接文档的品牌与交互约束除本补充外全部继续有效。
> 当前仍为私有本地作品集审核版本；不是公开部署网址，客户/作品素材授权尚待最终确认。

## 本轮更新

- 参考用户提供的“标题/完整项目介绍/横向信息栏”布局，仅借鉴排版，保持自有 Milk White `#F7F8F5`、Ink Black `#17191D`、Electric Blue `#315EFF`、Acid Lime `#C9FF48`、纸纹及 Bricolage Grotesque / Manrope / IBM Plex Mono。
- 11 个案例的首屏依次为：原项目名称（中文为已有编辑中文名）→ 一句话简介 → 从原作品集整理的项目背景 → 四项资料（领域、个人角色、PDF 页数及编号、待确认的年份）。四个栏目是真实已有字段，不凭参考图添加 Industry / Tools / Team 等没有确认的信息。
- 30 张 PDF 全页图从用户原始 `job！！！.zip` 重新渲染为 **5184×3351 WebP**；此前 V16 版本为 3456×2234。PDF 原始顺序及比例不变，仍可放大、拖动、上一页/下一页。原 PDF 中较低清的嵌入图片本身无法凭重新渲染提高原生细节。
- 详情原页最大显示宽度提高至 **1560px**，按屏幕缩放并缩小两侧不必要留白；原页仍无阴影、无裁切。
- 未修改主页创意机器、Work 11 案例、分类、Contact 地图、About、中文所在地约定或任何项目真实性披露。

## 正式源代码和审阅文件

- 最外层 `index.html`：唯一可双击打开的**单文件交互审核预览**，内嵌 CSS / JS / 作品图片，不是生产部署源代码。
- 内层 `LittleMachine_V17_FULL_SOURCE.zip`：**生产网站源码**，解压后 `Little_Machine_Portfolio/` 含四个主页面、11 个项目详情、所有素材与 Python 生成器。
- `assets/styles.css`：V17 排版和 PDF 宽度规则在文件末尾。
- `generate_site.py`：详情头部模板 (`v17-case-lead`) 的唯一 HTML 源。
- `assets/portfolio/*-page-*.webp`：新的 30 张高清页；不要替换成旧的 `*-cover.webp` 局部裁切资源。
- `V17_PDF_ASSET_MAP.json` 与 `PORTFOLIO_SOURCE_MAP_V17.md`：新版尺寸和来源映射。V14 页码与顺序保持权威。
- `QA_V17.md`：本轮验收范围、未完成事项。
- `A_Little_Machine_Project_Handoff_V16_COMPLETE.md`：完整历史规范和项目真实性约束；**以本 V17 补充更新的排版及尺寸优先**。

## 继续开发

任何英文源文案或页面结构修改请先改 `generate_site.py`，中文译文改 `translations.py`，项目数据改 `portfolio_data.py`，全站 CSS 在 `assets/styles.css`，脚本在 `assets/main.js`。在网站根目录执行 `python3 generate_site.py`，会覆盖 4 个主页面、11 个详情页和 `assets/i18n.js`。请勿只改生成后的 HTML。

V18 及后续每轮必须提供独立可交互 HTML + 完整源码 ZIP + QA；从最终 ZIP 解压出的**最外层唯一 index.html** 检查 CSS、图片加载、双语和交互，避免旧版本无样式问题。未取得作品公开许可、CV 日期、联系信息最终确认前，不得声称已上线。
