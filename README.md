# A Little Machine for Big Ideas — V22

**Live website: [rsrren-web.github.io/shuruiren](https://rsrren-web.github.io/shuruiren/)**

The current baseline is V22 from `Little_Machine_V22_FULL_SOURCE.zip`. It includes English/Chinese navigation, an interactive creative machine, 11 projects, 30 uncropped full-resolution portfolio pages, and the original five-minute soundtrack.

Run `python scripts/build.py` to regenerate, validate and package the site into `_site/`. Push to `main` to publish automatically through GitHub Actions. See [DEPLOYMENT.md](DEPLOYMENT.md) for maintenance and [QA_DEPLOYMENT.md](QA_DEPLOYMENT.md) for release verification.

The earlier notes below are retained as historical reference; their version and local-review status do not describe this deployment.

---

# A Little Machine for Big Ideas — V16

# V16 / Full-page PDF gallery

The confirmed V10–V15 design is retained. V16 polishes bilingual spacing, headings and the project overview without changing the creative machine. The original full-page PDF gallery remains intact. V16 is for review, **not approved for public publication**.

## View
- Use the *top-level* `index.html` supplied in the V16 delivery ZIP (self-contained preview).
- Production source is `Little_Machine_Portfolio/` and requires all sibling `assets/` files and directories to stay in place.
- Open `Little_Machine_Portfolio/index.html` with a browser or `python3 -m http.server 8000` in the website directory.

## Work / Detail
- Work uses each project’s first original PDF page in its full landscape ratio, without any crop.
- Detail displays *all pages belonging to each project* consecutively in original order. Click any page for full-resolution view.
- View original source mappings in `PORTFOLIO_SOURCE_MAP_V14.md`.

## Maintenance
- Edit `portfolio_data.py`, `generate_site.py`, `translations.py`, `assets/styles.css`, or `assets/main.js`.
- Run `python3 generate_site.py` to regenerate the 4 main HTML files, 11 cases and i18n.js.
- No npm or Node build dependency.

# Portfolio integration — historical notes (V15)

**Owner:** Shurui Ren  
**Status:** local review build, **not yet approved for public deployment**.  
**Based on:** the original V10 code, its V11 maintenance revision, and the V12 portfolio integration. V10 design decisions and core behaviors are intentionally retained.

## Portfolio integration through V15

- Replaced all **six invented concept cases** with **11 real items described in the owner-uploaded portfolio** (a ZIP of 37 single-page PDF exports). Each item is linked to the specific source pages and visually illustrated using exported source images. None of the six demo case study pages remain.
- Added 67 optimized WebP assets: 11 covers, 28 original portfolio page renditions, and 28 selected visual-story crops. Original portfolio page typography/diagrams have not been synthetically recreated or fabricated; crops are indicated by presentation context.
- Replaced case text with editorial source-based summaries, mapped provided roles to the new case studies, added bilingual copy, and added source-page disclosures to each case.
- Work remains **one filterable gallery** with the confirmed five navigation filters: Design / Art / Game / Campaigns / Play. Play is intentionally empty because no separate Play case is clearly documented. The playful machine mode and its click-through note continue to work.
- Removed unverified dates and numerical campaign metrics from public-facing pages. **YEAR TBC** means no verified project year is available. Glasessen is marked speculative and the Coldplay-inspired cover explicitly nonofficial.
- Homepage featured projects now use actual portfolio artwork, still in the original typography-first visual system.
- Contact, About, bilingual persistence, 2.5D machine and map are unchanged except where project lists require integration.

## Run the site

1. Extract this ZIP. Open `Little_Machine_Portfolio/index.html`, or use a local server:
   ```sh
   cd Little_Machine_Portfolio
   python3 -m http.server 8000
   ```
2. Browse `http://localhost:8000/`. No JS framework or npm needed.
3. The separate `A_Little_Machine_Interactive_Preview_v16.html` is an all-in-one review file with embedded image assets and hash routing; it is **not** the deployable production source.

## Maintain the site safely

- Projects, actual media references and project text: `portfolio_data.py`.
- English templates and page structure: `generate_site.py`.
- Chinese translations, project summaries, dynamic ideas: `translations.py`.
- Shared CSS: `assets/styles.css`; interactions: `assets/main.js`.
- Case images: `assets/portfolio/*.webp`.
- Regenerate pages after source changes with `python3 generate_site.py`. This overwrites the four main HTML pages, the project detail HTML pages, and `assets/i18n.js`. The generator removes old project detail HTML filenames.
- Source documentation: `PORTFOLIO_SOURCE_MAP_V14.md`; validation log: `QA_V15.md`.

## Confirmed decisions carried forward from V10

Milk White #F7F8F5; Ink Black #17191D; Electric Blue #315EFF; Acid Lime #C9FF48. Bricolage Grotesque / Manrope / IBM Plex Mono, local paper texture, small blue pencil pointer for mouse devices, unobtrusive click/hover sounds and toggle, and the stationary navigation. SHURUI has two blue U letters; REN is black. The homepage DESIGN / DRAW / BUILD / PLAY is black in both languages.

Machine buttons change prompts and screen copy; the full ticket links to corresponding Work filter. English `MAKE AN IDEA` / Chinese `一起聊创意` always links to Contact and does not generate content. No additional Lab or Experiments page. Personal location in Chinese is only 中国; English location phrasing remains as previously approved, pending owner's later confirmation. Contact preserves the interactive two-country map. Reduced-motion preferences are respected.

## Release blockers

**Do not deploy publicly until the owner reviews and approves:**

1. **Project permissions and attribution**: confirm which items can be published, particularly named partner organizations, social account screenshots, game/character art, and the nonofficial interpretation of the song “Yellow.” Confirm any client confidential material is removed. Source-portfolio inclusion is not proof of external publication rights.
2. **Dates and personal contributions**: verify each case year and what Shurui personally designed versus what collaborators developed. This release summarizes source language; it does not claim sole ownership of teamwork/technology.
3. **Campaign metrics**: screenshots and numerical claims exist in supplied PDFs but are intentionally omitted pending cross-check, context and disclosure permission.
4. **Resume and contacts**: verify CV dates, location discrepancy, public email and China-specific channels. No new phone number was published in this build.
5. **QA/launch**: full physical-device, multi-browser, accessibility and performance verification; external HTTPS URL testing, SEO previews, and deployment.

A one-file standalone preview is not a public web URL. For deployment, use **the contents of `Little_Machine_Portfolio/`**.


## V15 editorial visual narrative

Each of the 11 real portfolio-sourced draft cases now includes 2–4 visual story crops from the owner-provided PDF, source-page citations, an accessible image viewer, and an expandable set of original PDF page renditions. Source image, caption and page mappings are maintained as `VISUAL_STORIES` in `portfolio_data.py`. Keep project permissions and contact details unverified until the owner confirms. Run `python3 generate_site.py` to regenerate pages.
