# A Little Machine for Big Ideas — V19 Project Handoff

**Only current base:** V19 (2026-11-03), built from V18, not from V10–V17. Private local review only.

## User-approved V19 scope

1. 11 project leads take layout cues from the supplied editorial screenshot, NOT its green palette: large bold title, concise story/overview and horizontal fact rule, then immediately the original project images. No original source-grounded story or later notes were deleted.
2. Third project fact changes from documented PDF page count to **Tools**; source values transcribed from provided `job！！！.fig`. Conflict Resolver tools remain explicitly unverified.
3. 30 original PDF-sourced image files remain unchanged at 5184 × 3351. The inline reader uses the `V19_SAFE_CROP_MAP.json` crop coordinates via browser clipping to reduce blank margins, while the full original image is used unchanged on image zoom. Do not accidentally reintroduce `.visual-image-button img{max-height:620px}` onto cropped inline WebP; V19 overrides it.

## Development instructions

Edit `portfolio_data.py` (`PROJECT_TOOLS`), `translations.py`, `generate_site.py`, `assets/styles.css`, `assets/main.js` as needed; run `python3 generate_site.py`. Do not edit generated detail HTML in isolation. Preserve 11 case study pages, four major site pages, bilingual mode, creative machine, work category filters, Contact map, high-res viewer. The design style remains Bricolage Grotesque / Manrope / IBM Plex Mono and #F7F8F5, #17191D, #315EFF, #C9FF48.

## Delivery

- `A_Little_Machine_Interactive_Preview_v19_LITE.html`: single-file ~9 MB interactive *lower-resolution* HTML, direct browser open; embedding images is for convenient review only.
- `A_Little_Machine_V19_Offline_Website_OPEN_INDEX.zip`: extract completely; `index.html` is at the archive root with `projects/` and `assets/`. Original full-resolution files retained.
- `Little_Machine_V19_FULL_SOURCE.zip`: complete production website source and generator in `Little_Machine_Portfolio/`.
- `QA_V19.md`: validation summary and known browser gaps.

## Follow-ups

A new vector quality export directly from Figma would require that Figma access is granted to the connected account, or that the user exports per-frame PDF/SVG/PNG at verified frame bounds. Do not claim the current WebP is vector. Original embedded bitmap quality is bounded by the provided source. All public permission, CV dates, client specifics and external outcome claims still require review.
