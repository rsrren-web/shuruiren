# GitHub Pages deployment

Current updates: browser tabs use `Shurui‘s Portfolio`. Ordinary internal links
replace page content while retaining one connected audio player, so background
music continues through page changes and browser Back/Forward. Direct page URLs
still work; full reloads, new tabs and a network-failure navigation fallback create
a new document and may restart audio. Original image and soundtrack files are unchanged.

Website: https://rsrren-web.github.io/shuruiren/

The website uses the original V22 multipage source. Its 15 pages, 52 WebP images,
30 complete 5184 × 3351 portfolio pages, audio, typography and interactions are
preserved. Historical handoff documents describe earlier review states.
The owner requested public deployment on 2026-11-04 (UTC). This is publication
authorization, not independent verification of third-party media licensing.

## Build and maintain

Run `python scripts/build.py` from this repository. No third-party Python packages
are needed. The build regenerates pages, checks resource paths and original asset
hashes, and copies only website files into `_site/`.

Edit `generate_site.py`, `portfolio_data.py`, `translations.py`, or shared files
under `assets/`. Do not edit generated HTML as the permanent source. If deliberately
replacing an asset, update `scripts/asset-integrity.json` after verifying the change.

Push changes to `main`. The Pages workflow builds, validates and publishes `_site/`.
GitHub Pages must use **GitHub Actions** as its publishing source. The default
GitHub domain is used; no purchased domain, backend or paid subscription is needed.
Availability remains subject to GitHub's service and plan policies.

The offline single-file preview and original archives are preserved in the supplied
handoff package. They are not used as the production entry point.
