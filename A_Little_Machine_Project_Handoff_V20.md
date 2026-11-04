# A Little Machine for Big Ideas — V20 SOUND Handoff

**唯一新基准：V20（基于 V19.5）。** 只增加原创声音系统并提高 Hover 感知音量，保留全部品牌、11 项目、30 张高清原图、About 与 Contact、铅笔光标、中英文。

- 生产源码：`Little_Machine_Portfolio/`。只修改 `generate_site.py` / `assets/main.js` / `assets/styles.css` 等源文件后运行 `python3 generate_site.py`。
- 原创 Web Audio 背景循环与 FX 都位于 `assets/main.js` 的 `setupSoundEffects()`。BPM 100，每 24 小节循环；不依赖远程音频资源。
- `header()` 内含声音设置面板，CSS 在 styles.css 文件末尾。SOUND 主控全局静音，设置面板单独调整背景音乐和交互音效，默认音乐 18% / FX 75%。首次有效用户交互后尝试启动音乐。
- **交付必须**从最终 ZIP 解压测试最外层的独立 `index.html` 以及 `FULL_HD_SITE/`，并验证 CSS、JavaScript、52 组预览图片的完整数据、30 张完整源图、声音开关与页内导航。
- 独立 HTML 的 `imageData` 不能执行全局 `.replace('V19','V20')` 等字符串替换，否则可能损坏 WebP Base64 压缩流。
- 私有审核阶段：内容授权、年份等仍待最后确认。
