# V22 QA — Auto Audio + Louder, Softer Hover/Click

- Based on **V21**; no edits to 5-minute lo-fi soundtrack, portfolio artwork, CSS design, bilingual translations, pencil cursor, or content.
- Fresh browser preferences: SOUND, background music and interface sounds default ON. FX slider default 90% (previously 75%); existing deliberately saved preferences remain respected.
- Audible autoplay: attempt on initial page load, with browser permission catch; if denied, automatically retry synchronously on the first click/tap/key interaction. Never circumvent browser autoplay restrictions.
- Hover/Click/Machine effects: raised peak levels roughly 2.5–3× at new default vs V21, lower notes to soften high pitches, slightly longer envelopes. First click now retries when AudioContext is still resuming.
- Original five-minute MP3 unchanged (SHA-256 checked); music retains 2s fade, loop, mute, independent sliders, machine ducking.
- Root `index.html` in ZIP is fully self-contained with all CSS/JS, 52 preview imageData entries and one base64 MP3; FULL_HD_SITE holds 15 inline-style pages, 30 original high-resolution WebP pages, and MP3 path.
- **Copyright:** music is derived from a user-supplied YouTube audio download. Public or commercial deployment requires permission for both the composition and recording.
- Browser audible autoplay is permission-dependent. If blocked, first interaction starts audio. Browsers/devices may differ.
