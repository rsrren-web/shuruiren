# V17 QA / 2026-11-03

## Delivered changes
- V16-based, 11 case-detail intros changed to a source-grounded editorial information hierarchy: title / tagline / overview at top, horizontal 4-field facts band below. No reference screenshot palette or typography was copied.
- English and simplified-Chinese headings, spacing, role labels and project overview share the same responsive system. The original project names and source stories are preserved.
- Every original PDF page re-rendered at 3x / 5184×3351 pixels WebP quality 92 from the user's single-page PDFs; 30 source pages, unchanged order. Old full-page WebP were 3456×2234.
- Detail PDF page maximum width increased from 1170 to 1560 px (at 1440px viewport: 1372px). Responsive side margins of 34px at desktop, 23px at tablet and 12px at mobile. Full-page pictures remain uncropped with no drop shadow.
- Home machine, Work filtering, original cover ratio, About, Contact, bilingual navigation, image lightbox controls untouched.

## Validation
- All 11 cases × 2 languages × 5 viewports (320,390,768,1440,1920): 110 layout checks in Chromium browser testing; no horizontal scrolling; 4 facts and appropriate PDF page sequences present.
- English and Chinese desktop screenshots inspected; Chinese 390px screenshot inspected.
- Image sources checked: 30 WebP at 5184×3351, all match the original source map.
- Python page generator output deterministic, all local href/src references resolved, JS syntax checks and ZIP integrity checks passed.
- Single-entry standalone preview includes CSS, JS and image data; final extracted ZIP HTML checked.

## Known limits / publication controls
- Some embedded bitmap images in original PDFs have smaller native sizes. More rendering pixels improves vector text and linework but cannot restore detail missing from original bitmaps.
- Google Fonts still loads online; offline fallback is available.
- No comprehensive Safari/Firefox/physical-device/assistive-technology audit; further check mobile PDF viewer touch gestures.
- Launch blocked pending verified project publication permissions, personal role/year attribution, CV, public email and other contact details.
