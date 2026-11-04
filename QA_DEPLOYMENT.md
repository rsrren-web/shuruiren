# V22 GitHub Pages release verification

## Continuous music navigation update

Verified on the live deployment of commit `c333297`:

- Playing music advanced from 7.622606s on Home to 8.13818s on Work and
  8.616571s on SCAVENGER, without pausing or resetting.
- Browser Back and Forward kept playback advancing (26.250044s to 26.322083s).
- About → Contact navigation preserved Chinese language and continued at 28.559422s.
- The DOM contained exactly one audio player after navigation; its absolute audio
  URL and nested project image URLs resolved correctly.
- Muting persisted through navigation and category filtering; playback paused at
  43.892333s and resumed at 44.029614s when re-enabled on Home.
- Project viewer zoom, map region selection, Play empty state, menu open/Escape and
  bilingual switching worked after content replacement. No error-level browser logs.
- JavaScript syntax and the full static build/resource/integrity checks passed.

This confirms browser playback state and continuity. It is not a physical-device
listening test on every browser. Full reloads/new tabs remain independent documents.

## Original deployment record

Date: 2026-11-04 (UTC)

Live URL: https://rsrren-web.github.io/shuruiren/

## Verified

- Original source/site archives passed their recorded SHA-256 checks and ZIP CRC checks.
- All 15 regenerated pages match the V22 source pages after line-ending normalization.
- All 60 source assets are unchanged; 52 WebP images decoded successfully, including
  all 30 full-resolution portfolio pages at 5184 × 3351. The 300-second soundtrack
  has the SHA-256 recorded in the handoff manifest.
- JavaScript syntax checks passed for `assets/main.js` and `assets/i18n.js`.
- Resource-path checks passed, including nested project pages and audio references.
- The GitHub Actions build and deployment succeeded. HTTPS is enforced.
- All 15 deployed HTML pages and 60 assets returned HTTP 200 and matched the local
  release bytes (text comparison normalizes line endings). `.nojekyll` is build
  metadata, not a publicly served asset.
- Live browser layout checks: all 15 pages in English at 390px; all 15 pages in
  both English and Chinese at 320px and 1440px. All 75 combinations had headings,
  no horizontal document overflow, and uncropped `contain` styles on portfolio images.
- Home screenshot visually reviewed: paper background, blue name accents, creative
  machine, project images and embedded pencil cursor present.
- Machine Play mode updates the ticket URL; ticket opens the Play empty state.
- Work filters show All 11, Design 4, Art 3, Game 1, Campaigns 3, Play 0.
- SCAVENGER viewer opens, zooms to 150%, advances to page 2 of 5 and closes with Escape.
- Contact China/Canada controls switch the corresponding information panels.
- At 390px the mobile menu opens; sound settings fit within the viewport, display
  music 18% / FX 90%, and close with Escape.
- No error-level browser console entries were reported in the final interaction check.

## Limits

The local preview server was unreachable, so browser checks used the deployed HTTPS
site. This release did not redo physical iPhone/Android/Safari tests, pinch gestures,
screen-reader certification, or subjective five-minute listening/loop tests. Browser
autoplay restrictions continue to apply. Licensing and factual claims in supplied
portfolio content have not been independently certified.

Only deployment tooling/documentation was added; original website source, artwork,
soundtrack and visual design were preserved. The original offline preview remains
in the supplied handoff package and was not rebuilt for this hosting-only release.
