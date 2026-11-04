# QA_V18 — Detail First-Screen & PDF Reading Layout

**Build date:** 2026-11-03  
**Status:** Private local review; not a public release.

## V18 changes implemented

1. All 11 case headers use a compact responsive introduction. At wider widths the title/tagline and the complete source-grounded background paragraph are side by side. At narrow widths they stack naturally. The four facts (discipline, personal role, documented page count/source page IDs, year pending verification) remain directly below.
2. The original 3-card Project Notes section is **moved in the document source order** to **after** the PDF gallery, not deleted. The original title, tagline, story, lead, approach and outcome content is unchanged. The visitor reaches the first PDF sheet right after the compact introduction and small gallery heading.
3. PDF display width cap increases **1560px → 1920px**; the site case container expands to nearly the usable screen width with narrow responsive gutters. The original 30 WebP full pages (5184×3351) and page order are **unchanged**. Image rendering uses the natural `5184 / 3351` aspect ratio and `object-fit: contain` with no stretch, crop, drop shadow or artificial sharpening.
4. The PDF gallery heading and page-to-page vertical gaps are shortened. On ≤360px-wide screens, a repetitive gallery reading hint is visually minimized but remains available to assistive technology to prioritize showing the first image on the initial screen.
5. Home, Work, About, Contact, project facts, personal roles, localization data, creative machine, work categories and source attribution are unchanged.

## Validation performed

- Generated all 4 main pages and 11 project pages from `python3 generate_site.py`.
- **110 browser-based layout measurements**: 11 cases × English/Chinese × 320×700, 390×844, 768×1024, 1440×900 and 1920×1080 (Chromium; with network-dependent Google Fonts suppressed for deterministic checks). No horizontal document overflow in these viewports; 4 facts on every page; gallery precedes the three detailed project-note cards in DOM order.
- In this test configuration, the first PDF sheet begins above the viewport bottom in all 110 configurations. Across English cases the latest initial image start: 692px at 320×700, 694px at 390×844, 530px at 768×1024, 625px at 1440×900 and 657px at 1920×1080. Actual positions vary with available fonts, zoom level, and user settings. No fixed-height clipping or line truncation was applied to case text.
- Separate interactive Chromium smoke check: English → Chinese project title updates; clicking a PDF opens the viewer; zoom-in displays 150%; Escape closes the modal; no JS page errors observed in that smoke check. Test page used a smaller image **only in the automated browser harness**; the distributed assets remain full resolution.
- Standalone V18 preview image references were matched to its embedded asset dictionary (0 missing), including full-resolution viewer page references; all 11 case page bodies replaced with V18 generated markup.

## Caveats / launch gates

- PDF whitespace **inside** the original page layouts is intentionally retained to avoid cutting off original artistic/documentary content. Wider display does not enhance details of bitmap content embedded at low resolution in the underlying PDF.
- Site fonts are loaded via Google Fonts when online; offline fallback fonts may change text wrapping. The layout is content-sized, not force-clipped. Safari, Firefox, real touch devices, full keyboard/accessibility testing, and every zoom/browser configuration remain to be checked.
- Original V17 proof of 30 source assets at 5184×3351 remains valid; no PDF has been newly re-rendered, edited, or rewritten in V18.
- Public project permissions, CV/date details, contact details and third-party claims still require independent approval. No deployment has occurred.
