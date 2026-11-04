# V13 Validation & publication guardrails

## Verified in this handoff

- 15 generated HTML pages (four primary pages + 11 individual real portfolio-sourced project cases).
- 67 WebP media assets: 11 case covers, 28 editorial crops, 28 portfolio-page images.
- Every one of the 15 generated pages has valid local `href` / `src` links; no missing local image or CSS/JS references in static validation.
- Preview route: machine CAMPAIGNS mode → full ticket → Work with 3 matching projects.
- Filter controls: Design=4, Art=3, Game=1, Campaigns=3, Play=0, All=11. Empty Play state displays normally.
- Chinese selection: Work translations and case visual captions display correctly; contact China panel uses the China-only location label.
- SCAVENGER visual gallery: real portfolio-sourced imagery loads; image modal opens, arrow keys switch image, Esc closes the modal; original page accordion opens. No JS page errors were detected in these checks.
- Work: all 11 cover images decoded to non-zero width.
- Mobile: 390px preview width checked with no horizontal overflow; navigation opened and closed via Esc.
- Zip integrity to be verified during final packaging.

## Not yet verified / publication blockers

- Full live browser-to-server test was blocked by local navigation restrictions; browser testing used the all-in-one review HTML.
- Full physical-device and cross-browser accessibility/performance QA remains open.
- Project rights, roles, dates, external metric claims, CV and public contact details require owner review. All results lacking substantiation are withheld.
- The Play category remains intentionally empty; no invented project fills it.

Images are cropped directly from supplied PDF pages; no new client outcome or design imagery was invented.
