# V19.5 — Pencil Cursor Asset Repair / 2026-11-03

## Root cause
V19.4 embedded `assets/styles.css` into the HTML without resolving the stylesheet-relative `url('pencil-cursor.png')` or `url('pencil-cursor.svg')`. Because embedded CSS resolves relative links from the HTML file location, the pencil icon could not be found. Other later CSS rules also overrode the old cursor for some buttons/zoom surfaces.

## Fix
- Embedded the verified original 32×32 pencil PNG directly in a final CSS cursor rule on all 15 offline-site pages and the standalone index.html.
- Kept the pencil tip hotspot at x=4,y=28; the rule activates only when a fine mouse pointer is available. Touch devices continue to use normal touch behavior.
- Resolved the related paper grain texture reference in inlined CSS to avoid a similar missing-asset issue.
- Preserved a text-editing cursor for editable fields and grab/grabbing cursors in the zoomed image viewer.
- Modified only the CSS segment in the delivered preview HTML. The 52 embedded WebP imageData entries were compared for exact equality with V19.4, and 30 high-resolution WebP files were preserved byte-for-byte.

## Delivery checks
- Verified 32×32 cursor file decodes as RGBA/RGB PNG.
- Verified exactly 15 Full HD pages and one standalone root HTML contain the embedded cursor rule.
- Verified exact decoded embedded image-data equality before and after repair and preserved all HD image bytes.
- Verified both final ZIP files pass ZIP integrity checks.
- Browser media query and computed cursor style tested in Chromium for mouse/desktop and touchscreen context (see runtime QA if present).

## Scope
No changes were made to project text, images, page spacing, layout, or interactions. This fixes the missing pencil icon only (and missing paper texture referenced by the same incorrect CSS path behavior). Browser/OS can override custom cursors in certain restricted application previews; standard desktop browsers are recommended.
