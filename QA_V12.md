# V12 QA Log — 2026-11-02

## Completed checks

- All 37 single-page PDFs in the supplied ZIP inspected by text extraction and visual contact sheets.
- 11 source-grounded projects mapped to 4 Design, 3 Art, 1 Game and 3 Campaigns; Play empty is intentional.
- 39 optimized real portfolio visuals extracted (11 covers and 28 page images).
- Source generator re-run; all generated case studies replace the six old demo pages, not alongside them.
- The standalone single-file HTML preview contains all 15 generated HTML pages, inlined styles, JavaScript, translations and 39 images.
- Browser smoke test (Chromium, scripted DOM view of the interactive preview): Home loads; Work shows 11/11; filters 4/11, 3/11, 1/11, 3/11, 0/11; Play empty state shows; case-detail and 4-source-page gallery present; Chinese switch produces `zh-CN`; browser reported zero JavaScript page errors in that run.
- Chromium simulated 390px viewport confirms no horizontal overflow, mobile navigation opens and Escape closes it; no JavaScript page errors in that run.
- Source code passes Python compilation; all 15 HTML files and their local `href`/`src` dependencies resolved, deterministic regeneration verified, and the ZIP archive integrity check passed.

## Not yet fully verified

- Physical mobile/tablet testing, Safari and Firefox, screen-reader testing and all hover/audio interactions. Chromium file URL navigation is blocked in this container; the interactive preview was tested through DOM content injection instead. The 390px browser check is **emulation**, not a real device.
- Full graphic QA across all 11 individual case pages and all languages; below-the-fold lazy loading in standard source files depends on scrolling.
- Copyright/public exhibition permissions, actual responsibilities, date accuracy and independently sourced marketing KPIs.
- End-to-end hosted HTTPS links, Google Fonts performance and live public URL.

**This is an editorial review build, not a deployed/public release.**
