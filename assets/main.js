/** A Little Machine for Big Ideas — shared interactions for all generated HTML pages.
 *  V13 case studies derive from the submitted PDF; public release checks remain pending.
 */
const PERSONALIZE = {
  siteTitle: 'Shurui‘s Portfolio',
  nameFirst: 'SHURUI', nameSecond: 'REN', fullName: 'SHURUI REN',
  description: 'Designer and illustrator creating thoughtful digital experiences, visual stories, brands, and campaigns.',
  email: 'rsr.ren@gmail.com',
};
const LM_I18N = window.LM_TRANSLATIONS || {zh:{},ideasZh:{},screenZh:{}};
let currentLanguage = 'en';
try { currentLanguage = localStorage.getItem('little-machine-language') === 'zh' ? 'zh' : 'en'; } catch (_) {}

function isChinese() {return currentLanguage === 'zh';}
function trans(key, fallback) {return isChinese() ? (LM_I18N.zh[key] ?? fallback) : fallback;}
function applyIdentity() {
  // Named color spans are trusted static branding markup, never user-provided HTML.
  document.querySelectorAll('[data-name-first]').forEach(e => e.innerHTML = 'SH<span class="name-u">U</span>R<span class="name-u">U</span>I');
  document.querySelectorAll('[data-name-second]').forEach(e => e.innerHTML = '<span class="name-ren">REN</span>');
  document.querySelectorAll('[data-footer-name]').forEach(e => e.innerHTML = 'SH<span class="name-u">U</span>R<span class="name-u">U</span>I <span class="name-ren">REN</span>');
  document.querySelectorAll('[data-contact-email]').forEach(e => {
    e.href = 'mailto:' + PERSONALIZE.email;
    // Keep the edit location centralized in this config.
    e.innerHTML = PERSONALIZE.email + ' <span aria-hidden="true">↗</span>';
  });
  document.querySelectorAll('[data-current-year]').forEach(e => e.textContent = new Date().getFullYear());
}
function applyTranslations() {
  document.documentElement.lang = isChinese() ? 'zh-CN' : 'en';
  document.title = PERSONALIZE.siteTitle;
  document.querySelectorAll('[data-i18n-aria-label]').forEach(el=>{
    const key=el.dataset.i18nAriaLabel;
    if (!el.dataset.originalAriaLabel) el.dataset.originalAriaLabel=el.getAttribute('aria-label') || '';
    el.setAttribute('aria-label',isChinese() ? (LM_I18N.zh[key] ?? el.dataset.originalAriaLabel) : el.dataset.originalAriaLabel);
  });
  document.querySelectorAll('[data-i18n], [data-i18n-html]').forEach(el => {
    const html = el.hasAttribute('data-i18n-html');
    const key = el.getAttribute(html ? 'data-i18n-html' : 'data-i18n');
    const stash = html ? 'originalHtml' : 'originalText';
    if (!(stash in el.dataset)) el.dataset[stash] = html ? el.innerHTML : el.textContent;
    const base = el.dataset[stash];
    const translated = isChinese() ? (LM_I18N.zh[key] ?? base) : base;
    if (html) el.innerHTML = translated; else el.textContent = translated;
  });
  const langToggle = document.getElementById('language-toggle');
  if (langToggle) {
    langToggle.setAttribute('aria-label', isChinese() ? 'Switch to English' : '切换为中文');
    langToggle.dataset.activeLanguage = currentLanguage;
    langToggle.title = isChinese() ? 'Switch to English' : '切换为中文';
  }
  document.querySelectorAll('.main-nav a').forEach(link => {
    if (link.hasAttribute('aria-current')) link.setAttribute('aria-current','page');
  });
  if (typeof window.refreshMachineLanguage === 'function') window.refreshMachineLanguage();
  if (typeof window.refreshFilterCount === 'function') window.refreshFilterCount();
  if (typeof window.refreshSoundState === 'function') window.refreshSoundState();
  const menuToggle=document.querySelector('.nav-toggle');
  if (menuToggle) menuToggle.setAttribute('aria-label',menuToggle.getAttribute('aria-expanded')==='true' ? (isChinese()?'关闭导航':'Close navigation') : (isChinese()?'打开导航':'Open navigation'));
}
function setLanguage(next) {
  currentLanguage = next === 'zh' ? 'zh' : 'en';
  try {localStorage.setItem('little-machine-language',currentLanguage);} catch (_) {}
  applyTranslations();
}
function setupGlobalLanguageToggle() {
  if (window.__LM_languageToggleBound) return;
  window.__LM_languageToggleBound = true;
  document.addEventListener('click', e => {
    if (e.target.closest?.('#language-toggle')) setLanguage(isChinese() ? 'en' : 'zh');
  });
}
function setupNavigation() {
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.querySelector('.main-nav');
  if (!toggle || !menu) return;
  function close() { toggle.setAttribute('aria-expanded','false'); toggle.setAttribute('aria-label',isChinese()?'打开导航':'Open navigation'); menu.classList.remove('is-open'); }
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded',String(open));
    toggle.setAttribute('aria-label',open ? (isChinese()?'关闭导航':'Close navigation'):(isChinese()?'打开导航':'Open navigation'));
    menu.classList.toggle('is-open',open);
  });
  menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
  if (!window.__LM_escapeBound) {
    window.__LM_escapeBound = true;
    document.addEventListener('keydown',e=>{
      if(e.key!=='Escape') return;
      const openMenu=document.querySelector('.main-nav.is-open');
      const openToggle=document.querySelector('.nav-toggle[aria-expanded="true"]');
      if (!openMenu || !openToggle) return;
      const returnFocus=openMenu.contains(document.activeElement);
      openMenu.classList.remove('is-open');
      openToggle.setAttribute('aria-expanded','false');
      openToggle.setAttribute('aria-label',isChinese()?'打开导航':'Open navigation');
      if (returnFocus) openToggle.focus();
    });
  }
}
function setupFilters() {
  const controls = [...document.querySelectorAll('.filter[data-filter]')];
  if (!controls.length) {window.refreshFilterCount=null;return;}
  const projects = [...document.querySelectorAll('.project[data-category]')];
  const count = document.getElementById('filter-count');
  const empty = document.getElementById('filter-empty');
  let selected = 'all';
  const valid = new Set(controls.map(b=>b.dataset.filter));
  try {
    const param = window.LM_PREVIEW_CATEGORY || new URLSearchParams(location.search).get('category');
    if (param) { const normalized=param.toLowerCase()==='illustration'?'art':param.toLowerCase(); if (valid.has(normalized)) selected=normalized; }
  } catch (_) {}
  function reflect() {
    controls.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter===selected)));
    let showing=0;
    projects.forEach(project=>{
      const visible=selected==='all'||project.dataset.category===selected;
      project.hidden=!visible;
      if(visible) showing++;
    });
    if(count) count.textContent = (isChinese() ? '显示 ':'SHOWING ')+String(showing).padStart(2,'0')+' / '+String(projects.length).padStart(2,'0');
    if(empty) empty.hidden=showing!==0;
  }
  controls.forEach(b=>b.addEventListener('click',()=>{
    selected=b.dataset.filter;
    reflect();
    if(window.LM_PREVIEW_ROUTE){window.LM_PREVIEW_CATEGORY=selected;window.LM_PREVIEW_ROUTE('work.html',selected,true);}
    else {
      try {const url=new URL(location.href);if(selected==='all')url.searchParams.delete('category');else url.searchParams.set('category',selected);history.replaceState(history.state,'',url.href);}catch(_){}
    }
  }));
  const reset=document.querySelector('[data-reset-filter]');
  if(reset)reset.addEventListener('click',()=>controls.find(b=>b.dataset.filter==='all')?.click());
  window.refreshFilterCount=reflect;
  reflect();
}

const IDEA_MODES=[
 {id:'design',screen:'DESIGN MODE',label:'DESIGN',symbol:'▤',ideas:[
 'Make a tiny interface with a big personality.','Turn a complex journey into a clear visual story.',
 'Design a system that makes someone smile.','Give a familiar screen an unexpected detail.']},
 {id:'art',screen:'ART MODE',label:'ART',symbol:'✎',ideas:[
 'Draw a shape that looks like a good question.','Invent a flower that grows on another planet.',
 'Build a character from three simple forms.','Illustrate the feeling of an exciting new idea.']},
 {id:'game',screen:'GAME MODE',label:'GAME',symbol:'◆',ideas:[
 'Build a game where the rules change with the weather.','Imagine a world you can explore in one minute.',
 'Turn a simple button press into a tiny adventure.','Design a game about collecting impossible objects.']},
 {id:'campaigns',screen:'CAMPAIGNS',label:'CAMPAIGNS',symbol:'✦',ideas:[
 'Turn one campaign message into five visual stories.','Create a social series with a recognisable rhythm.',
 'Make a launch campaign that invites participation.','Design a playful set of posts around one bold idea.']},
 {id:'play',screen:'PLAY MODE',label:'PLAY',symbol:'✳',ideas:[
 'What if a website acted like a tiny toy?','Invent a machine that turns questions into shapes.',
 'Mix two unrelated ideas and make them friends.','Build something just because it makes you curious.']},
];
function setupMachine() {
  const machine=document.getElementById('creative-machine');
  if (!machine) {window.refreshMachineLanguage=null;return;}
  const windows=[...machine.querySelectorAll('.machine-window')];
  const screen=document.getElementById('screen-mode');
  const index=document.getElementById('screen-index');
  const symbol=document.getElementById('screen-symbol');
  const status=document.getElementById('machine-status');
  const screenPanel=machine.querySelector('.machine-screen');
  const ticket=document.getElementById('machine-ticket');
  const ticketText=document.getElementById('ticket-text');
  const ticketMode=document.getElementById('ticket-mode');
  const ticketNum=document.getElementById('ticket-number');
  const ticketCTA=document.getElementById('ticket-cta');
  let active=0,printed=1,ideaIndex=0;
  const lastByMode=new Array(5).fill(-1);
  let timer;
  function modeLabel(mode){return trans('mode_'+mode.id,mode.label);}
  function refresh() {
    const mode=IDEA_MODES[active];
    windows.forEach((b,i)=>{b.setAttribute('aria-pressed',String(i===active));b.setAttribute('aria-label',(isChinese()?'选择':'Select ')+modeLabel(IDEA_MODES[i]));});
    screen.textContent=isChinese() ? (LM_I18N.screenZh[mode.id] || mode.screen) : mode.screen;
    index.textContent=String(active+1).padStart(2,'0');
    symbol.textContent=mode.symbol;
    const localized=LM_I18N.ideasZh[mode.id] || mode.ideas;
    ticketText.textContent=isChinese()?localized[ideaIndex]:mode.ideas[ideaIndex];
    ticketMode.textContent=modeLabel(mode);
    ticketCTA.innerHTML = (isChinese() ? '探索' + modeLabel(mode) + '作品' : 'EXPLORE ' + mode.label + ' WORK') + ' <span aria-hidden="true">↗</span>';
    ticket.href='work.html?category='+mode.id;
    ticket.setAttribute('aria-label', isChinese() ? '打开' + modeLabel(mode) + '分类的作品页面' : 'Open ' + mode.label + ' projects');
    ticketNum.textContent=String(printed).padStart(3,'0');
  }
  function print() {
    const mode=IDEA_MODES[active];
    let next=Math.floor(Math.random()*mode.ideas.length);
    if(next===lastByMode[active])next=(next+1)%mode.ideas.length;
    lastByMode[active]=next;
    ideaIndex=next;printed++;
    refresh();
    // Restart the brief, tactile print sequence for every channel selection.
    // Preserve the existing 2.5D transform: only the screen content, dial and paper move.
    clearTimeout(timer);
    ticket.classList.remove('eject');
    machine.classList.remove('processing');
    screenPanel?.classList.remove('is-refreshing');
    void ticket.offsetWidth;
    machine.classList.add('processing');
    screenPanel?.classList.add('is-refreshing');
    screenPanel?.setAttribute('aria-busy','true');
    ticket.classList.add('eject');
    status.textContent=isChinese()?'灵感已打印！':'IDEA PRINTED!';
    timer=setTimeout(()=>{
      machine.classList.remove('processing');
      screenPanel?.classList.remove('is-refreshing');
      screenPanel?.removeAttribute('aria-busy');
      status.textContent=trans('machine_ready','READY TO MAKE');
    },650);
  }
  windows.forEach((b,i)=>b.addEventListener('click',()=>{active=i;print();}));
  window.refreshMachineLanguage=refresh;
  refresh();
}
function setupMap() {
  const map=document.getElementById('contact-map');
  if(!map)return;
  function choose(country){
    if(!['canada','china'].includes(country))return;
    map.querySelectorAll('.map-pin').forEach(btn=>{
      const on=btn.dataset.mapSelect===country;
      btn.classList.toggle('is-active',on);btn.setAttribute('aria-pressed',String(on));
    });
    map.querySelectorAll('.map-region').forEach(path=>{
      path.classList.toggle('is-active',path.dataset.country===country);
      path.setAttribute('aria-pressed',String(path.dataset.country===country));
    });
    document.querySelectorAll('.location-info[data-contact-country]').forEach(panel=>{
      panel.hidden=panel.dataset.contactCountry!==country;
    });
  }
  map.querySelectorAll('[data-map-select], .map-region[data-country]').forEach(target=>{
    const handler=()=>choose(target.dataset.mapSelect||target.dataset.country);
    target.addEventListener('click',handler);
    target.addEventListener('keydown',e=>{
      if((e.key==='Enter'||e.key===' ')&&target.matches('.map-region')){e.preventDefault();handler();}
    });
  });
  choose('canada');
}

/** V21: selected 5-minute lo-fi soundtrack, using the user-supplied original-tone MP3.
 * An HTMLMediaElement is used rather than MediaElementAudioSourceNode because
 * local file:// browsing and data: preview URLs can behave differently under CORS.
 * This keeps offline playback reliable, while Web Audio retains the V20 UI effects.
 * The selected music is user-provided; public deployment requires appropriate rights.
 */
function setupSoundEffects() {
  if (window.__LM_soundInitialized) { window.refreshSoundState?.(); return; }
  window.__LM_soundInitialized = true;
  const AudioEngine = window.AudioContext || window.webkitAudioContext;
  const storageKey = 'little-machine-audio-v20'; // Retain existing V20 user settings.
  const prevKey = 'little-machine-sound';
  const read = (key) => { try { return localStorage.getItem(key); } catch (_) { return null; } };
  const save = () => {
    try {
      localStorage.setItem(storageKey, JSON.stringify({enabled, musicEnabled, fxEnabled, musicLevel, fxLevel}));
      localStorage.setItem(prevKey, enabled ? 'on' : 'off');
    } catch (_) { /* Local-file or private modes can disable storage. */ }
  };
  let enabled = read(prevKey) !== 'off';
  let musicEnabled = true;
  let fxEnabled = true;
  let musicLevel = 18;
  let fxLevel = 90;
  try {
    const stored = JSON.parse(read(storageKey) || 'null');
    if (stored && typeof stored === 'object') {
      if (typeof stored.enabled === 'boolean') enabled = stored.enabled;
      if (typeof stored.musicEnabled === 'boolean') musicEnabled = stored.musicEnabled;
      if (typeof stored.fxEnabled === 'boolean') fxEnabled = stored.fxEnabled;
      if (Number.isFinite(stored.musicLevel)) musicLevel = Math.max(0, Math.min(100, stored.musicLevel));
      if (Number.isFinite(stored.fxLevel)) fxLevel = Math.max(0, Math.min(100, stored.fxLevel));
    }
  } catch (_) {}
  let engine = null, fxBus = null, audio = null;
  let activated = false, playing = false, playPending = false, musicError = '';
  let autoplayBlocked = false, playRequest = 0, effectsPlayed = 0;
  let lastHover = 0, fadeFrame = null, duckTimer = null;
  const trackSource = document.querySelector('meta[name="lm-audio-source"]')?.getAttribute('content');
  // Resolve once: the document URL can change while this same player keeps running.
  const trackUrl = trackSource ? new URL(trackSource, location.href).href : '';
  function reflect() {
    const toggle = document.getElementById('sound-toggle');
    if (toggle) {
      const listening = enabled && (playing || (activated && fxEnabled));
      toggle.setAttribute('aria-pressed', String(enabled));
      toggle.setAttribute('aria-label', enabled ? (isChinese()?'关闭全部声音':'Mute all sound') : (isChinese()?'开启全部声音':'Turn on sound'));
      toggle.title = enabled ? (isChinese()?'点击静音 · 浏览器允许时自动播放':'Click to mute · plays automatically when permitted') : (isChinese()?'点击打开声音':'Click to enable sound');
      const txt = toggle.querySelector('.sound-toggle-label');
      if (txt) txt.textContent = enabled ? (listening ? (isChinese()?'声音 开':'SOUND ON') : (isChinese()?'声音待启':'SOUND READY')) : (isChinese()?'声音 关':'SOUND OFF');
    }
    const settings = document.getElementById('audio-settings');
    if (!settings) return;
    const label = (sel, val) => { const el=settings.querySelector(sel); if(el) el.textContent=val; };
    label('[data-audio-heading]', isChinese()?'小机器 / 声音':'LITTLE MACHINE / AUDIO');
    label('[data-music-label]', isChinese()?'背景音乐':'Background music');
    label('[data-music-description]', isChinese()?'所选音乐 · 原曲氛围 · 5 分钟循环':'Selected track · Original tone · 5-min loop');
    label('[data-fx-label]', isChinese()?'交互音效':'Interface sounds');
    label('[data-fx-description]', isChinese()?'悬停 / 点击 / 创意机器':'Hover / Click / Machine');
    label('[data-audio-hint]', !enabled ? (isChinese()?'当前已静音，可点击 SOUND 再开启。':'Muted. Use SOUND to turn audio back on.') :
      musicError ? (isChinese()?'音乐无法播放；请确认音频文件存在且浏览器允许播放。':'Music unavailable. Check the audio file and playback permission.') :
      activated ? (isChinese()?'背景音乐已就绪，可随时调整或关闭。':'Sound is active. Adjust or mute whenever you like.') :
      (isChinese()?'声音默认开启；若浏览器拦截自动播放，首次点击或按键后即会响起。':'Sound is on by default. If autoplay is blocked, your first click or key starts it.'));
    const m=settings.querySelector('[data-audio-music-enabled]'); if(m) m.checked=musicEnabled;
    const f=settings.querySelector('[data-audio-fx-enabled]'); if(f) f.checked=fxEnabled;
    const ml=settings.querySelector('[data-audio-music-level]'); if(ml) {ml.value=String(musicLevel); ml.disabled=!musicEnabled;}
    const fl=settings.querySelector('[data-audio-fx-level]'); if(fl) {fl.value=String(fxLevel); fl.disabled=!fxEnabled;}
    label('[data-audio-music-value]', Math.round(musicLevel)+'%');
    label('[data-audio-fx-value]', Math.round(fxLevel)+'%');
    const settingsToggle=document.getElementById('sound-settings-toggle');
    if(settingsToggle) {settingsToggle.setAttribute('aria-label',isChinese()?'声音设置':'Audio settings');settingsToggle.title=isChinese()?'声音设置':'Audio settings';}
    settings.setAttribute('aria-label',isChinese()?'声音设置':'Audio settings');
  }
  function ensureEffects() {
    if (!enabled || !AudioEngine) return false;
    if (!engine) {
      try {
        engine = new AudioEngine();
        fxBus = engine.createGain();
        fxBus.gain.value = fxLevel / 100;
        fxBus.connect(engine.destination);
      } catch (_) {engine=null;return false;}
    }
    if (engine.state === 'suspended') engine.resume().catch(()=>{});
    return true;
  }
  function ensureTrack() {
    if (audio) return true;
    if (!trackUrl) { musicError='Missing audio source'; reflect(); return false; }
    try {
      audio = new Audio();
      audio.preload='auto'; // Try autoplay once; fall back to the first trusted user gesture.
      audio.loop=true;
      audio.src=trackUrl;
      audio.volume=0.04; // Audible nonzero playback: the browser decides whether autoplay is permitted.
      audio.id='little-machine-background-audio';
      audio.hidden=true;
      document.body.append(audio);
      audio.addEventListener('error',()=>{
        musicError='Audio load error ('+(audio?.error?.code||'?')+')';
        playing=false; playPending=false; reflect();
      });
      return true;
    } catch (_) { audio=null; musicError='Cannot create audio player'; reflect(); return false; }
  }
  function musicTarget() { return enabled && musicEnabled && musicLevel > 0 ? (musicLevel / 100) * 0.70 : 0; }
  function cancelFade() { if (fadeFrame!==null) {cancelAnimationFrame(fadeFrame);fadeFrame=null;} }
  function fadeMusic(seconds = 1.8, factor = 1, pauseWhenDone = false) {
    if (!audio) return;
    cancelFade();
    const start=performance.now(), from=audio.volume, to=musicTarget()*factor;
    if (seconds<=0) {audio.volume=Math.max(0,Math.min(1,to));if(pauseWhenDone)audio.pause();return;}
    const step = now => {
      const p=Math.min(1,(now-start)/(seconds*1000));
      // Smoothstep makes the beginning and end of the transition imperceptible.
      const eased=p*p*(3-2*p);
      audio.volume=Math.max(0,Math.min(1,from+(to-from)*eased));
      if (p<1) fadeFrame=requestAnimationFrame(step);
      else {fadeFrame=null;if(pauseWhenDone)audio.pause();}
    };
    fadeFrame=requestAnimationFrame(step);
  }
  function tone(start, finish, duration, volume, delay=0, shape='sine') {
    if (!enabled || !fxEnabled || !activated || !engine) return;
    if (engine.state!=='running') {
      if (engine.state==='suspended') engine.resume().then(()=>{
        if (enabled && fxEnabled && activated && engine?.state==='running') tone(start,finish,duration,volume,delay,shape);
      }).catch(()=>{});
      return;
    }
    const t=engine.currentTime + delay;
    const osc=engine.createOscillator(), gain=engine.createGain();
    osc.type=shape;
    osc.frequency.setValueAtTime(start,t);
    osc.frequency.exponentialRampToValueAtTime(finish,t+duration);
    gain.gain.setValueAtTime(0.0001,t);
    gain.gain.exponentialRampToValueAtTime(Math.max(0.0002,volume),t+Math.min(0.012,duration/3));
    gain.gain.exponentialRampToValueAtTime(0.0001,t+duration);
    osc.connect(gain);gain.connect(fxBus);
    osc.start(t);osc.stop(t+duration+0.007);effectsPlayed++;
  }
  function startMusic(fromGesture = false) {
    if (!enabled || !musicEnabled || musicLevel<=0 || document.hidden) return;
    if (!ensureTrack()) return;
    if (!audio.paused && !(fromGesture && playPending)) {playing=true;autoplayBlocked=false;fadeMusic(0.36);reflect();return;}
    // A first gesture must be able to retry even if an earlier autoplay play()
    // promise has not yet settled. Superseded promises must not change UI state.
    if (playPending && !fromGesture) return;
    cancelFade();
    playPending=true;
    const request=++playRequest;
    try {
      const promise=audio.play();
      const ready=()=>{
        if(request!==playRequest)return;
        playPending=false;
        if (!enabled || !musicEnabled || document.hidden) {audio.pause();audio.volume=0.04;playing=false;reflect();return;}
        musicError='';autoplayBlocked=false;activated=true;playing=true;fadeMusic(2.0);reflect();
      };
      const failure=err=>{
        if(request!==playRequest)return;
        playPending=false;playing=false;
        autoplayBlocked=err?.name==='NotAllowedError';
        musicError=autoplayBlocked?'':'Playback failed: '+String(err?.name||'error');
        reflect();
      };
      if(promise?.then)promise.then(ready).catch(failure);
      else ready();
    } catch(err) {
      if(request===playRequest){playPending=false;playing=false;autoplayBlocked=err?.name==='NotAllowedError';musicError=autoplayBlocked?'':'Playback failed';reflect();}
    }
  }
  function stopMusic(immediate=false) {
    playing=false;
    if(duckTimer!==null){clearTimeout(duckTimer);duckTimer=null;}
    if(audio)fadeMusic(immediate?0:0.24,0,true);
  }
  function startFromGesture() {
    if (!enabled) return;
    activated=true;
    ensureEffects();
    startMusic(true);
    reflect();
  }
  function duck() {
    if (!playing || !audio) return;
    if(duckTimer!==null)clearTimeout(duckTimer);
    fadeMusic(0.08,0.55);
    duckTimer=setTimeout(()=>{duckTimer=null;if(playing)fadeMusic(0.75);},170);
  }
  function sound(kind) {
    // Warm, longer envelopes and ~2.5–3x stronger peaks than V21;
    // keep the upper pitches restrained for comfortable repeated browsing.
    if (kind==='hover') tone(520,640,0.120,0.082);
    else if (kind==='machine') {
      tone(370,560,0.145,0.068,0,'triangle');
      tone(640,520,0.115,0.046,0.080);
      duck();
    } else tone(420,540,0.125,0.072,0,'triangle');
  }
  function toggleSettings(open) {
    const panel=document.getElementById('audio-settings');
    const button=document.getElementById('sound-settings-toggle');
    if(!panel || !button) return;
    const show=typeof open==='boolean' ? open : panel.hidden;
    panel.hidden=!show;
    button.setAttribute('aria-expanded',String(show));
    if(show) reflect();
  }
  window.refreshSoundState=reflect;
  window.__LM_audioDebug=()=>({enabled,musicEnabled,fxEnabled,musicLevel,fxLevel,activated,playing,autoplayBlocked,playPending,playRequest,effectsPlayed,contextState:engine?.state||'not-created',trackPresent:Boolean(audio),trackPaused:audio?.paused??true,trackCurrentTime:audio?.currentTime??0,trackDuration:audio?.duration??0,trackReadyState:audio?.readyState??0,trackVolume:audio?.volume??0,trackError:musicError});
  reflect();
  document.addEventListener('click',e=>{
    const target=e.target.closest?.('button');
    if(target?.id==='sound-toggle') {
      enabled=!enabled; save();
      if(!enabled){stopMusic();}
      else {startFromGesture();sound('click');}
      reflect();return;
    }
    if(target?.id==='sound-settings-toggle'){toggleSettings();return;}
    if(!e.target.closest?.('#audio-settings, #sound-settings-toggle'))toggleSettings(false);
  });
  document.addEventListener('change',e=>{
    const el=e.target;
    if(el?.matches?.('[data-audio-music-enabled]')) {musicEnabled=el.checked;save();if(musicEnabled)startFromGesture();else stopMusic();reflect();}
    if(el?.matches?.('[data-audio-fx-enabled]')) {fxEnabled=el.checked;save();reflect();}
  });
  document.addEventListener('input',e=>{
    const el=e.target;
    if(el?.matches?.('[data-audio-music-level]')) {musicLevel=Math.max(0,Math.min(100,Number(el.value)));save();if(musicLevel>0&&musicEnabled&&enabled&&!playing)startMusic();else fadeMusic(0.12);reflect();}
    if(el?.matches?.('[data-audio-fx-level]')) {fxLevel=Math.max(0,Math.min(100,Number(el.value)));save();if(fxBus)fxBus.gain.setTargetAtTime(fxLevel/100,engine.currentTime,0.03);reflect();}
  });
  document.addEventListener('pointerdown',event=>{
    if(event.target.closest?.('#sound-toggle'))return;
    startFromGesture();
    if(event.target.closest?.('#sound-settings-toggle, #audio-settings'))return;
    const action=event.target.closest?.('button, a, [role="button"]');
    if(action) sound(action.classList.contains('machine-window')?'machine':'click');
  });
  document.addEventListener('keydown',event=>{
    if(event.key==='Escape'){toggleSettings(false);return;}
    if(event.repeat || ['Shift','Control','Alt','Meta','Tab'].includes(event.key))return;
    if(event.target.closest?.('#sound-toggle'))return;
    startFromGesture();
    if(event.target.closest?.('#sound-settings-toggle, #audio-settings'))return;
    const action=event.target.closest?.('button, a, [role="button"]');
    if(action && ['Enter',' '].includes(event.key))sound(action.classList.contains('machine-window')?'machine':'click');
  });
  document.addEventListener('pointerover',event=>{
    if(event.pointerType && event.pointerType!=='mouse' && event.pointerType!=='pen')return;
    const action=event.target.closest?.('button, a, [role="button"]');
    if(!action || action.closest('#audio-settings') || (event.relatedTarget instanceof Node && action.contains(event.relatedTarget)))return;
    const now=performance.now();if(now-lastHover<100)return;
    lastHover=now;sound('hover');
  });
  document.addEventListener('visibilitychange',()=>{
    if(document.hidden){stopMusic(true);}
    else if(enabled) startMusic();
  });
  // Audible autoplay is browser-controlled. Attempt now and retry on the first
  // trusted click/tap/key if denied. Do not override an explicit mute preference.
  if(enabled && musicEnabled) startMusic(false);
}

function setupVisualViewer() {
  if(window.__LM_visualViewerBound) return;
  window.__LM_visualViewerBound = true;
  let active=0, lastFocus=null, zoom=1, panX=0, panY=0;
  const pointers=new Map();
  let dragOrigin=null, pinchStart=null;
  const modal=()=>document.getElementById('case-lightbox');
  const pages=()=>[...document.querySelectorAll('.v14-page-trigger')];
  const clamp=(v,low,high)=>Math.min(high,Math.max(low,v));
  function updateTransform(){
    const m=modal();if(!m)return;
    const img=m.querySelector('.lightbox-photo');
    img.style.transform=`translate(${panX}px, ${panY}px) scale(${zoom})`;
    m.querySelector('[data-lightbox-zoom-value]').textContent=Math.round(zoom*100)+'%';
    m.querySelector('.v14-lightbox-stage').classList.toggle('is-zoomed',zoom>1.01);
  }
  function setZoom(next){
    zoom=clamp(next,1,4);if(zoom===1){panX=0;panY=0;}
    updateTransform();
  }
  function showPage(index){
    const all=pages(),m=modal();if(!m||!all.length)return;
    active=(index+all.length)%all.length;
    const button=all[active],source=button.querySelector('img');
    const image=m.querySelector('.lightbox-photo');
    image.src=button.dataset.previewFull||button.dataset.full||source.currentSrc||source.src;
    image.alt=source.alt;
    m.querySelector('.lightbox-caption').textContent=String(active+1).padStart(2,'0')+' / '+String(all.length).padStart(2,'0')+'  —  '+source.alt;
    pointers.clear();dragOrigin=null;pinchStart=null;zoom=1;panX=0;panY=0;updateTransform();
  }
  function open(button){
    const m=modal();if(!m)return;
    lastFocus=button;m.hidden=false;document.body.classList.add('has-lightbox');
    showPage(pages().indexOf(button));m.querySelector('[data-lightbox-close]')?.focus();
  }
  function close(){const m=modal();if(!m||m.hidden)return;m.hidden=true;document.body.classList.remove('has-lightbox');m.querySelector('.lightbox-photo').removeAttribute('src');pointers.clear();lastFocus?.focus?.();}
  document.addEventListener('click',e=>{
    const target=e.target.closest?.('button');if(!target)return;
    if(target.classList.contains('v14-page-trigger')){open(target);return;}
    if(!modal()||modal().hidden)return;
    if(target.matches('[data-lightbox-close]'))close();
    else if(target.matches('[data-lightbox-prev]'))showPage(active-1);
    else if(target.matches('[data-lightbox-next]'))showPage(active+1);
    else if(target.matches('[data-lightbox-zoom-in]'))setZoom(zoom+.5);
    else if(target.matches('[data-lightbox-zoom-out]'))setZoom(zoom-.5);
    else if(target.matches('[data-lightbox-reset]'))setZoom(1);
  });
  document.addEventListener('keydown',e=>{
    const m=modal();if(!m||m.hidden)return;
    if(e.key==='Escape'){e.preventDefault();close();}
    else if(e.key==='ArrowLeft'){e.preventDefault();showPage(active-1);}
    else if(e.key==='ArrowRight'){e.preventDefault();showPage(active+1);}
    else if(e.key==='+' || e.key==='='){e.preventDefault();setZoom(zoom+.5);}
    else if(e.key==='-'){e.preventDefault();setZoom(zoom-.5);}
    else if(e.key==='0'){e.preventDefault();setZoom(1);}
    else if(e.key==='Tab'){
      const controls=[...m.querySelectorAll('button')];
      if(e.shiftKey&&document.activeElement===controls[0]){e.preventDefault();controls[controls.length-1].focus();}
      if(!e.shiftKey&&document.activeElement===controls[controls.length-1]){e.preventDefault();controls[0].focus();}
    }
  });
  function coords(){return [...pointers.values()];}
  document.addEventListener('pointerdown',e=>{
    const stage=e.target.closest?.('[data-lightbox-stage]');if(!stage||modal()?.hidden)return;
    stage.setPointerCapture?.(e.pointerId);
    pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
    if(pointers.size===1)dragOrigin={x:e.clientX,y:e.clientY,panX,panY};
    else if(pointers.size===2){const a=coords();pinchStart={distance:Math.hypot(a[0].x-a[1].x,a[0].y-a[1].y),zoom};dragOrigin=null;}
  });
  document.addEventListener('pointermove',e=>{
    if(!pointers.has(e.pointerId)||modal()?.hidden)return;
    pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
    if(pointers.size===2 && pinchStart){const a=coords();setZoom(pinchStart.zoom*Math.hypot(a[0].x-a[1].x,a[0].y-a[1].y)/Math.max(1,pinchStart.distance));}
    else if(pointers.size===1 && dragOrigin && zoom>1){panX=dragOrigin.panX+(e.clientX-dragOrigin.x);panY=dragOrigin.panY+(e.clientY-dragOrigin.y);updateTransform();}
  });
  function clearPointer(e){pointers.delete(e.pointerId);pinchStart=null;dragOrigin=null;}
  document.addEventListener('pointerup',clearPointer);
  document.addEventListener('pointercancel',clearPointer);
  document.addEventListener('wheel',e=>{
    const stage=e.target.closest?.('[data-lightbox-stage]');if(!stage||modal()?.hidden||!e.ctrlKey)return;
    e.preventDefault();setZoom(zoom+(e.deltaY<0?.25:-.25));
  },{passive:false});
}

/** Keep the document and audio engine alive across ordinary portfolio links.
 * Each HTML page remains a usable direct entry point and a no-JavaScript fallback.
 */
function setupContinuousNavigation() {
  if (window.__LM_navigationBound || window.LM_PREVIEW_ROUTE || !/^https?:$/.test(location.protocol)) return;
  window.__LM_navigationBound = true;
  const script = [...document.scripts].find(el => /\/assets\/main\.js(?:\?|$)/.test(el.src));
  if (!script) return;
  const siteRoot = new URL('../', script.src);
  const knownPages = new Set(['', 'index.html', 'work.html', 'about.html', 'contact.html']);
  // Preserve the loaded shell assets when history changes from a root page to a case.
  document.querySelectorAll('head [href], head script[src]').forEach(el => {
    const attr = el.hasAttribute('href') ? 'href' : 'src';
    el.setAttribute(attr, new URL(el.getAttribute(attr), location.href).href);
  });
  let pending = null, sequence = 0;
  function supported(url) {
    if (url.origin !== siteRoot.origin || !url.pathname.startsWith(siteRoot.pathname)) return false;
    const path = url.pathname.slice(siteRoot.pathname.length);
    return knownPages.has(path) || /^projects\/[a-z0-9-]+\.html$/.test(path);
  }
  function rememberScroll() {
    history.replaceState({...history.state, lmScroll: [scrollX, scrollY]}, '', location.href);
  }
  history.scrollRestoration = 'manual';
  rememberScroll();
  let scrollFrame = null;
  window.addEventListener('scroll', () => {
    if (pending || scrollFrame !== null) return;
    scrollFrame = requestAnimationFrame(() => {
      scrollFrame = null;
      if (!pending) rememberScroll();
    });
  }, {passive:true});
  function placeScroll(url, position) {
    let anchor = null;
    try { anchor = url.hash ? document.getElementById(decodeURIComponent(url.hash.slice(1))) : null; } catch (_) {}
    if (position) window.scrollTo({left:position[0], top:position[1], behavior:'instant'});
    else if (anchor) anchor.scrollIntoView({behavior:'instant'});
    else window.scrollTo({top:0, left:0, behavior:'instant'});
  }
  async function navigate(url, {pop=false, position=null} = {}) {
    const request = ++sequence;
    pending?.abort();
    const controller = new AbortController();
    pending = controller;
    document.querySelector('main')?.setAttribute('aria-busy', 'true');
    const timeout = setTimeout(() => controller.abort(), 15000);
    try {
      const response = await fetch(url.href, {signal:controller.signal});
      if (!response.ok || !response.headers.get('content-type')?.includes('text/html')) throw new Error('Page unavailable');
      const resolved = new URL(response.url);
      if (!supported(resolved)) throw new Error('Unexpected navigation target');
      resolved.hash = url.hash;
      const next = new DOMParser().parseFromString(await response.text(), 'text/html');
      if (!next.querySelector('#main-content') || !next.querySelector('meta[name="lm-audio-source"]')) throw new Error('Not a portfolio page');
      if (request !== sequence) return;
      // Change the URL before importing relative image, link and viewer paths.
      if (!pop) history.pushState({lmScroll:[0,0]}, '', resolved.href);
      document.title = PERSONALIZE.siteTitle;
      const description = document.querySelector('meta[name="description"]');
      if (description) description.content = next.querySelector('meta[name="description"]')?.content || '';
      for (const attr of [...document.body.attributes]) document.body.removeAttribute(attr.name);
      for (const attr of [...next.body.attributes]) document.body.setAttribute(attr.name, attr.value);
      // Never detach the media element: removing a playing <audio> can interrupt it.
      const player = document.getElementById('little-machine-background-audio');
      for (const node of [...document.body.childNodes]) {
        if (node !== player) node.remove();
      }
      document.body.append(...[...next.body.childNodes].map(node => document.importNode(node, true)));
      initLittleMachine(); // Global handlers/audio are guarded; new page elements are rebound.
      const main = document.getElementById('main-content');
      main?.setAttribute('tabindex', '-1');
      main?.focus({preventScroll:true});
      placeScroll(resolved, position);
    } catch (_) {
      if (request === sequence) location.assign(url.href); // Keep links usable after network/parser failures.
    } finally {
      clearTimeout(timeout);
      if (request === sequence) {
        pending = null;
        document.querySelector('main')?.removeAttribute('aria-busy');
      }
    }
  }
  document.addEventListener('click', event => {
    if (event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest?.('a[href]');
    if (!link || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
    const url = new URL(link.href, location.href);
    if (!supported(url)) return;
    if (url.pathname === location.pathname && url.search === location.search && url.hash) return;
    event.preventDefault();
    rememberScroll();
    navigate(url);
  });
  window.addEventListener('popstate', event => {
    const url = new URL(location.href);
    if (supported(url)) navigate(url, {pop:true, position:event.state?.lmScroll || null});
    else location.reload();
  });
}

function initLittleMachine() {
  if (!document.body.dataset.englishTitle) document.body.dataset.englishTitle=document.title;
  applyIdentity();
  setupGlobalLanguageToggle();
  setupNavigation();
  setupFilters();
  setupMachine();
  setupMap();
  setupSoundEffects();
  setupVisualViewer();
  applyTranslations();
  setupContinuousNavigation();
}
window.initLittleMachine=initLittleMachine;
document.addEventListener('DOMContentLoaded',initLittleMachine);
