# V11 QA record — A Little Machine for Big Ideas

Date: 2026-11-02 (project handoff date)
Status: maintenance release only; not a public launch or complete browser acceptance test.

## Verified with automated/static checks

- V10 archive integrity (22 files), contents and V10 generator repeatability.
- V11 Python generator runs successfully and repeated generation is deterministic.
- All generated HTML files retain local link and image/script/style targets.
- JavaScript syntax checks for `assets/main.js`, `assets/i18n.js` and preview scripts pass.
- All 10 pages, five modes, six demonstration projects and five Work categories retained.
- V11 preview contains the updated main script and localization data.

## Manual browser acceptance still required

1. In desktop and tablet widths, check sticky navigation, original 2.5D machine, clear text, ticket layering, prompt updates, cursor and sound state.
2. At 320 / 375 / 390 / 768 / 1440px widths, check no unexpected overflow, Chinese line breaks, and the machine ticket not covering MAKE AN IDEA.
3. Test menu Escape: aria-label returns to Open navigation / 打开导航 and focus returns to the toggle after a menu-link focus.
4. Switch the map by both markers and keyboard-activatable SVG country outlines; verify accessible names in each language.
5. Check ticket → Work category query, old `?category=illustration` → Art, Campaigns empty state, case study links and return links.
6. Test language persistence across pages, including About/Contact Chinese location as 中国 only.
7. Test reduced-motion preference, touch interactions, browser console, accessible contrast and screen readers.
8. Check generated website and independent preview separately; the preview is NOT production source.

Automated headless browser navigation was attempted but blocked by the execution environment's administrator policy; no claim of actual cross-browser/device acceptance is made.

## Publication blockers

- Replace all six concept demonstrations using verified project sources and permitted original artwork.
- Cross-check exact CV wording and dates before publishing, and confirm shareable email / China contact details.
- Obtain visual asset permissions, perform full QA, deploy static folder, and test public HTTPS paths.
