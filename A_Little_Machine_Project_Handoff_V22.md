# A Little Machine for Big Ideas — V22 Sound Autoplay & FX Handoff

**Current baseline V22**, inheriting all V21 content/visuals/images/music. All updates in `Little_Machine_Portfolio/assets/main.js` (`setupSoundEffects()`) and the generated controls in `generate_site.py`.

## Requested changes
- Louder, warmer Hover/Click/Machine: V22 amplitudes 0.082 / 0.072 / 0.068+0.046, softer pitches 520–640Hz / 420–540Hz / 370–560Hz etc., longer envelopes, default FX level 90 (new visits). Saved user FX levels are respected but the sound generator itself is louder.
- `AudioContext` may still be suspended on first click; its resume promise now retries the queued tone to avoid losing that click sound.
- V21 original-tone 5-minute Lo-fi MP3 remains **byte-identical**. New load-time autoplay attempt uses nonzero volume to test real audible-playback permission, fades into 18% user-set music level over ~2 seconds when permitted. If the browser reports `NotAllowedError`, first tap/click/key automatically retries without false missing-file error.
- On first visit SOUND/Music/FX all default enabled; stored explicit off settings are respected. SOUND toggle, audio settings, independent volume, loop, machine ducking and SPA navigation preserved.

## Build and files
- `python3 generate_site.py` regenerates 15 routes. Then `python3 /mnt/data/v22_auto/build_v22.py` safely embeds changed JS and converted HTML page bodies into a known verified V21 single-file preview without modifying any of the 52 preview imageData payloads or the 5-minute MP3 base64.
- Release `A_Little_Machine_V22_AUTO_AUDIO_COMPLETE_SITE.zip`: root self-contained `index.html`; `FULL_HD_SITE/` 15 route pages / 30 HD images / one external MP3; README, QA.
- Separate one-file preview, source ZIP and QA. Respect all V20 complete handoff constraints.

## Constraints
- Modern browsers may block autoplay with sound until the first interaction; impossible to force. Use a proper user gesture rather than muted/unmute circumvention.
- YouTube-derived audio is not claimed as original; verify rights before public deployment.
- After edits, check both final unzipped root HTML and HD project pages; compare SHA of all original high-resolution WebP images and soundtrack to V21; assert imageData identical.
