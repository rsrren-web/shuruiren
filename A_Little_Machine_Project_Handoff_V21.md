# A Little Machine for Big Ideas — V21 Lo-fi Background Music Handoff

**V21 是唯一当前工作基准。**继承 V20，用户要求将原 Web Audio 合成背景乐替换为 **01 / 原曲氛围版 · 5 分钟循环**。不得改变此前审定的视觉、11 个作品、30 张全幅 PDF 原图、铅笔光标、中文/英文及交互音效。

- 音频来源：用户自行上传 YouTube 播放列表，另行制作并选定了 `01_Original_Tone_5min_Loop.mp3`；V21 对该 MP3 **逐字节直接采用**，无二次降噪或改变高频。公共部署及商用必须先核实录音及底层音乐版权许可。
- 源码：`Little_Machine_Portfolio/`；音乐 `assets/audio/little-machine-lofi-original-tone-5min.mp3`，所有页面的 `<meta name="lm-audio-source">` 定位该文件。脚本在 `assets/main.js` 的 `setupSoundEffects()`，音乐原生 Audio 元素播放，Web Audio 只负责 Hover/Click/Machine。
- SOUND 全局静音、单独音乐/FX 开关和音量、初次点击/按键激活、两秒淡入、创意机器短暂 ducking 均继承 V20 交互。保留 V20 localStorage 设置键以兼容用户旧配置。
- 构建：运行 `python3 generate_site.py`，再按照 `build_v21.py` 从已验证的 V20 单文件安全生成 ZIP。禁止直接全局 `.replace()` 包含 imageData/Base64 的完整 HTML。
- 交付：最外层 `index.html` 自包含 HTML/CSS/JS/52 预览 WebP/完整 5 分钟音频，打开即可离线预览；`FULL_HD_SITE/` 是独立资源高清版，包含 30 张 5184×3351 全幅 WebP 和一个 MP3。另有可编辑源码 ZIP。
- 验证：`QA_V21.md` 与最终 ZIP 的 SHA-256、文件结构、页面相对资源、实际浏览器行为；发布前人工验证目标设备并确认全部作品、音乐授权。
