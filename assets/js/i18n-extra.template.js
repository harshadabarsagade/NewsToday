/*
 * News Today - i18n extra layer (Phase 3)
 *  1. LANGUAGE REGISTRY: all 22 Eighth Schedule languages + Angika & Bhojpuri.
 *     status "full" = complete content, "planned" = architecture ready, falls back to English.
 *  2. LANGUAGE ISOLATION: translates leftover text nodes (no data-i18n) and formats dates
 *     so an English page never shows Hindi and vice versa. Brand names are preserved.
 * Generated from gen_extra.py -> do not edit the PAIRS object by hand.
 */
(function () {
  'use strict';
  var PAIRS = /*PAIRS*/{};
  var REGISTRY = {
    en:{name:'English',native:'English',status:'full',locale:'en-IN'},
    hi:{name:'Hindi',native:'हिन्दी',status:'full',locale:'hi-IN'},
    as:{name:'Assamese',native:'অসমীয়া',status:'planned',locale:'as-IN'},
    bn:{name:'Bengali',native:'বাংলা',status:'planned',locale:'bn-IN'},
    brx:{name:'Bodo',native:'बड़ो',status:'planned',locale:'hi-IN'},
    doi:{name:'Dogri',native:'डोगरी',status:'planned',locale:'hi-IN'},
    gu:{name:'Gujarati',native:'ગુજરાતી',status:'planned',locale:'gu-IN'},
    kn:{name:'Kannada',native:'ಕನ್ನಡ',status:'planned',locale:'kn-IN'},
    ks:{name:'Kashmiri',native:'كأشُر',status:'planned',locale:'ur-IN'},
    kok:{name:'Konkani',native:'कोंकणी',status:'planned',locale:'kok-IN'},
    mai:{name:'Maithili',native:'मैथिली',status:'planned',locale:'hi-IN'},
    ml:{name:'Malayalam',native:'മലയാളം',status:'planned',locale:'ml-IN'},
    mni:{name:'Manipuri (Meitei)',native:'ꯃꯦꯇꯦꯢꯂꯣꯟ',status:'planned',locale:'en-IN'},
    mr:{name:'Marathi',native:'मराठी',status:'planned',locale:'mr-IN'},
    ne:{name:'Nepali',native:'नेपाली',status:'planned',locale:'ne-NP'},
    or:{name:'Odia',native:'ଓଡ଼ିଆ',status:'planned',locale:'or-IN'},
    pa:{name:'Punjabi',native:'ਪੰਜਾਬੀ',status:'planned',locale:'pa-IN'},
    sa:{name:'Sanskrit',native:'संस्कृतम्',status:'planned',locale:'sa-IN'},
    sat:{name:'Santali',native:'ᱥᱟᱱᱛᱟᱲᱤ',status:'planned',locale:'en-IN'},
    sd:{name:'Sindhi',native:'سنڌي',status:'planned',locale:'sd-IN'},
    ta:{name:'Tamil',native:'தமிழ்',status:'planned',locale:'ta-IN'},
    te:{name:'Telugu',native:'తెలుగు',status:'planned',locale:'te-IN'},
    ur:{name:'Urdu',native:'اردو',status:'planned',locale:'ur-IN'},
    anp:{name:'Angika',native:'अंगिका',status:'planned',locale:'hi-IN',dialect:true},
    bho:{name:'Bhojpuri',native:'भोजपुरी',status:'planned',locale:'hi-IN',dialect:true}
  };
  window.NEWS_LANGUAGES = REGISTRY;

  var REV = {}; Object.keys(PAIRS).forEach(function (k) { REV[PAIRS[k]] = k; });
  var MONTHS = {January:0,February:1,March:2,April:3,May:4,June:5,July:6,August:7,September:8,October:9,November:10,December:11};
  var orig = new WeakMap();
  var SKIP = {SCRIPT:1,STYLE:1,NOSCRIPT:1,TITLE:1,TEXTAREA:1,SVG:1,CODE:1,OPTION:1,SELECT:1};

  function fmtDate(text, locale) {
    var m, d;
    if ((m = text.match(/^([A-Z][a-z]+) (\d{1,2}), (\d{4})$/)) && MONTHS[m[1]] !== undefined)
      d = new Date(+m[3], MONTHS[m[1]], +m[2]);
    else if ((m = text.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})\s+(\d{1,2}):(\d{2})\s*(AM|PM)$/i)))
      d = new Date(+m[3], +m[2] - 1, +m[1], (+m[4] % 12) + (/pm/i.test(m[6]) ? 12 : 0), +m[5]);
    else if ((m = text.match(/^(\d{1,2})\.(\d{1,2})\.(\d{4})\s+(\d{1,2}):(\d{2})\s*(AM|PM)$/i)))
      d = new Date(+m[3], +m[1] - 1, +m[2], (+m[4] % 12) + (/pm/i.test(m[6]) ? 12 : 0), +m[5]);
    if (!d || isNaN(d)) return null;
    var hasTime = /\d:\d\d/.test(text);
    try {
      return new Intl.DateTimeFormat(locale, hasTime
        ? {day:'numeric',month:'short',year:'numeric',hour:'numeric',minute:'2-digit'}
        : {day:'numeric',month:'long',year:'numeric'}).format(d);
    } catch (e) { return null; }
  }

  function inOwnedByEngine(el) {
    for (var n = el; n && n.nodeType === 1; n = n.parentNode) {
      if (SKIP[n.tagName.toUpperCase()]) return true;
    }
    return false;
  }

  function localize(lang) {
    var eff = (lang === 'hi') ? 'hi' : 'en';
    var locale = eff === 'hi' ? 'hi-IN' : 'en-US';
    var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null), n, list = [];
    while ((n = w.nextNode())) list.push(n);
    list.forEach(function (node) {
      var p = node.parentNode; if (!p || inOwnedByEngine(p)) return;
      var raw = node.nodeValue, t = raw.trim(); if (!t) return;
      var o = orig.has(node) ? orig.get(node) : t;
      var out = null;
      var dt = fmtDate(o, locale);
      if (dt) out = dt;
      else if (eff === 'hi' && PAIRS[o]) out = PAIRS[o];
      else if (eff === 'en' && REV[o]) out = REV[o];
      else if (orig.has(node)) out = o; // restore original
      if (out !== null && out !== t) {
        if (!orig.has(node)) orig.set(node, t);
        node.nodeValue = raw.replace(t, out);
      }
    });
    // placeholders / submit buttons
    document.querySelectorAll('input[placeholder],input[type=submit]').forEach(function (el) {
      var ph = el.getAttribute('placeholder'), v = el.getAttribute('type') === 'submit' ? el.value : null;
      if (ph) { if (!el.__ph) el.__ph = ph; var s = eff==='hi' ? PAIRS[el.__ph] : REV[el.__ph]; if (s) el.setAttribute('placeholder', s); }
      if (v) { if (!el.__v) el.__v = v; var s2 = eff==='hi' ? PAIRS[el.__v] : REV[el.__v]; if (s2) el.value = s2; }
    });
  }


  // Live date/time bar (was a static, always-Hindi string frozen at build time)
  function renderClock(eff) {
    var el = null, all = document.querySelectorAll('.nav-date-text');
    for (var i = 0; i < all.length; i++) if (/\|/.test(all[i].textContent) || all[i].getAttribute('data-clock')) { el = all[i]; break; }
    if (!el) return;
    el.setAttribute('data-clock', '1');
    var loc = eff === 'hi' ? 'hi-IN' : 'en-IN', now = new Date();
    try {
      var d = new Intl.DateTimeFormat(loc, {weekday:'long', day:'numeric', month:'long', year:'numeric'}).format(now);
      var t = new Intl.DateTimeFormat('en-IN', {hour:'numeric', minute:'2-digit', hour12:true}).format(now).toUpperCase();
      el.textContent = d + ' | ' + t;
    } catch (e) {}
  }

  function run() { var l = document.documentElement.getAttribute('lang') || 'hi'; localize(l); renderClock(l === 'hi' ? 'hi' : 'en'); }

  document.addEventListener('DOMContentLoaded', function () {
    run();
    new MutationObserver(run).observe(document.documentElement, {attributes:true, attributeFilter:['lang']});
    setInterval(function () { renderClock((document.documentElement.getAttribute('lang') || 'hi') === 'hi' ? 'hi' : 'en'); }, 30000);
  });
})();
