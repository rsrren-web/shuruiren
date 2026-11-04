# QA V19.3 — Layout, spacing and PDF completeness fix (2026-11-04)

## Requested fixes completed
- Increased left/right breathing room in project detail intros so large titles and summaries no longer sit too close to the viewport edges.
- Reduced the inline PDF presentation width and restored full-page display for all project pages; the inline reader now prioritizes complete pages and readable whitespace instead of cropped edge-filling.
- Removed the crop-window rendering from case pages to avoid incomplete/clipped PDF pages. Clicking any page still opens the original full-resolution image in the viewer.
- Reworked the About-page “What stays with me / 真正留在心里的” three-card section from heavy black cards to calmer editorial panels so they no longer read as clickable buttons.
- Removed the visible “CV / PDF” label in the About page footer note, and removed the “CV /” prefix from those About section eyebrow labels.

## Verification
- Regenerated index/work/about/contact and 11 project pages from `generate_site.py`.
- Checked generated HTML to confirm `CV / PDF ↗` no longer appears.
- Checked generated project pages to confirm the inline PDF gallery no longer uses the V19 crop-window inline style payload.
- Full-resolution portfolio WebP assets were preserved; only HTML/CSS layout and rendering behavior changed.

## Remaining note
- This QA pass verifies the generated source and packaging structure. Final visual approval should still be done by opening the delivered files on your own machine/browser.
