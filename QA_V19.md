# QA V19 — 2026-11-03

Status: private review build; NOT deployed or approved for publication.

## Changes

- Restructured 11 case-study introductions using the user-provided reference's typographic information hierarchy: bold left-aligned title, tagline, complete existing verified case story, four-item horizontal facts bar. The site's existing Milk White / Electric Blue / Ink Black / Acid Lime palette, fonts, texture, creative machine, site routes and bilingual structure remain.
- Case facts now read DISCIPLINE / MY ROLE / TOOLS / YEAR. The 10 project-specific tools lists are transcribed from the supplied original Figma .fig text and normalized for software spelling (e.g., Adoube XD → Adobe XD, Procreat → Procreate). The Conflict Resolver lacks a verified project-specific list and explicitly reads TO BE CONFIRMED (工具待确认). Roles/dates were not fabricated.
- The 30 existing 5184 x 3351 WebP source-page images have NOT been replaced, recompressed, stretched or raster-upscaled in the production source. V19 uses CSS-only, per-image edge-focused framing defined by V19_SAFE_CROP_MAP.json, with generous edge-safety padding. The first page of each project may skip a small original chapter tab and pure white top spacing in the inline reading view; clicking still opens the untouched whole original image in the full-resolution viewer. Source order and gallery counts are intact.
- Increased inline display max width from 1920px to 1960px while retaining tight responsive side gutters. Original lightbox zoom and pagination remain.
- The optional ~9 MB single-file LIGHT preview embeds reduced image data to help open locally; it cannot be used to assess the full 5184px resolution. For full-resolution review download and extract the offline ZIP.

## Checks

- Generated 4 main pages + 11 detail pages using python3 generate_site.py.
- 11 projects x 2 languages x 5 viewports (320x700, 390x844, 768x1024, 1440x900, 1920x1080) = 110 Chromium DOM/layout measurements: no horizontal document overflow, 4 metadata fields, original gallery precedes additional narrative notes, first image begins within tested viewport. Narrow translations were checked as translated strings in the generated DOM.
- Actual 1440px and 390px static Chromium screenshots checked for Whales Today with correctly preserved native image ratio. Originally a global 620px image max-height interfered with the new inline crop; the V19 override `max-height:none!important` fixes it. The content-focused screenshot visually shows page text/illustration without stretching.
- The light standalone HTML has 15 page templates and 52 embedded image keys. All new per-project data-preview image references match available image keys (0 missing). Its initial homepage loaded successfully in Chromium without page errors.
- Full ~9 MB standalone preview route+zoom end-to-end automated test was attempted but the test process timed out; this is NOT counted as passing. The existing viewer JavaScript is retained, with DOM selectors/path conventions checked; real-device review is still required.
- Need additional testing on Safari, Firefox, actual phones, accessibility/font-loading variations and HTML opened through the recipient's specific file/browser context.

## Caveats

- The uploaded `.fig` was usable for text extraction, but Figma remote export was not accessible from the connected account (edit permission denied). Consequently this V19 does NOT claim new native-vector Figma renders. Production display reuses original large PDF/WebP renders and trims *display framing only*. Pure-white space within the creative layout still exists; changing that or enlarging all original typography significantly would require artboard redesign/native export approval.
- The word 'Tools' in the data bar denotes original project-specific claims, not inferred app stacks. Claims/years/publication rights remain subject to the user's final verification. This is not a public website.
