/*
 * News Today - First-visit language onboarding (Phase 2)
 * Manual State -> City -> Language selection. No GPS. Persists in localStorage.
 * Uses window.setNewsLanguage (i18n.js). Languages without full content yet fall
 * back to the closest fully-supported language (hi/en) while the choice is saved.
 */
(function () {
  'use strict';
  var KEY_DONE = 'news_today_onboarded';
  var KEY_PREF = 'news_today_pref'; // {state, city, lang}
  var FULL = { en: 1, hi: 1 }; // languages with complete content today

  var REGIONS = {
    'Bihar': { cities: { 'Bhagalpur': ['hi', 'en', 'anp'], 'Patna': ['hi', 'en'] } },
    'Maharashtra': { cities: { 'Mumbai': ['mr', 'en'], 'Pune': ['mr', 'en'] } },
    'Karnataka': { cities: { 'Bengaluru': ['kn', 'en'] } },
    'Tamil Nadu': { cities: { 'Chennai': ['ta', 'en'] } },
    'West Bengal': { cities: { 'Kolkata': ['bn', 'en'] } },
    'Gujarat': { cities: { 'Ahmedabad': ['gu', 'en'] } },
    'Telangana': { cities: { 'Hyderabad': ['te', 'en'] } },
    'Kerala': { cities: { 'Kochi': ['ml', 'en'] } },
    'Rajasthan': { cities: { 'Jaipur': ['hi', 'en'] } },
    'Uttar Pradesh': { cities: { 'Lucknow': ['hi', 'en'] } },
    'Punjab': { cities: { 'Chandigarh': ['pa', 'en'] } },
    'Assam': { cities: { 'Guwahati': ['as', 'en'] } },
    'Odisha': { cities: { 'Bhubaneswar': ['or', 'en'] } }
  };
  var LANG_NAMES = {
    en: 'English', hi: 'हिन्दी (Hindi)', anp: 'अंगिका (Angika)', mr: 'मराठी (Marathi)',
    kn: 'ಕನ್ನಡ (Kannada)', ta: 'தமிழ் (Tamil)', bn: 'বাংলা (Bengali)', gu: 'ગુજરાતી (Gujarati)',
    te: 'తెలుగు (Telugu)', ml: 'മലയാളം (Malayalam)', pa: 'ਪੰਜਾਬੀ (Punjabi)',
    as: 'অসমীয়া (Assamese)', or: 'ଓଡ଼ିଆ (Odia)'
  };

  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  function applyLang(lang) {
    var eff = FULL[lang] ? lang : 'en';
    document.documentElement.setAttribute('data-pref-lang', lang);
    if (typeof window.setNewsLanguage === 'function') window.setNewsLanguage(eff);
  }

  function injectCSS() {
    var s = document.createElement('style');
    s.textContent =
      '.nt-ob{position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,.55);display:flex;align-items:center;justify-content:center;padding:16px;box-sizing:border-box}' +
      '.nt-ob *{box-sizing:border-box}' +
      '.nt-ob-card{background:#fff;color:#111;width:100%;max-width:440px;max-height:100%;overflow:auto;border-radius:14px;padding:24px;font-family:Inter,Arial,sans-serif;box-shadow:0 20px 60px rgba(0,0,0,.35)}' +
      '.nt-ob h2{margin:0 0 6px;font-size:22px;line-height:1.25}' +
      '.nt-ob p{margin:0 0 16px;font-size:14px;color:#555}' +
      '.nt-ob label{display:block;font-size:13px;font-weight:600;margin:12px 0 6px}' +
      '.nt-ob select{width:100%;min-height:44px;padding:10px 12px;font-size:16px;border:1px solid #ccc;border-radius:8px;background:#fff;color:#111}' +
      '.nt-ob button{min-height:44px;width:100%;margin-top:18px;border:0;border-radius:8px;background:#111;color:#fff;font-size:16px;font-weight:600;cursor:pointer}' +
      '.nt-ob button[disabled]{opacity:.4;cursor:not-allowed}' +
      '.nt-ob .nt-skip{background:transparent;color:#555;margin-top:6px;font-weight:500;text-decoration:underline}';
    document.head.appendChild(s);
  }

  function opt(v, t) { var o = document.createElement('option'); o.value = v; o.textContent = t; return o; }

  function build() {
    injectCSS();
    var wrap = document.createElement('div');
    wrap.className = 'nt-ob';
    wrap.setAttribute('role', 'dialog');
    wrap.setAttribute('aria-modal', 'true');
    wrap.setAttribute('aria-labelledby', 'nt-ob-title');
    wrap.innerHTML =
      '<div class="nt-ob-card">' +
      '<h2 id="nt-ob-title">Welcome to News Today \u2013 Choose Your Language</h2>' +
      '<p>Select your state, city and preferred language. You can change this anytime.</p>' +
      '<label for="nt-state">State</label><select id="nt-state"></select>' +
      '<label for="nt-city">City</label><select id="nt-city" disabled></select>' +
      '<label for="nt-lang">Preferred Language</label><select id="nt-lang" disabled></select>' +
      '<button type="button" id="nt-go" disabled>Continue</button>' +
      '<button type="button" class="nt-skip" id="nt-skip">Skip \u2013 use English</button>' +
      '</div>';
    document.body.appendChild(wrap);

    var st = wrap.querySelector('#nt-state'), ci = wrap.querySelector('#nt-city'),
        la = wrap.querySelector('#nt-lang'), go = wrap.querySelector('#nt-go');

    st.appendChild(opt('', 'Select state'));
    Object.keys(REGIONS).forEach(function (s) { st.appendChild(opt(s, s)); });

    st.addEventListener('change', function () {
      ci.innerHTML = ''; la.innerHTML = ''; la.disabled = true; go.disabled = true;
      if (!st.value) { ci.disabled = true; return; }
      ci.appendChild(opt('', 'Select city'));
      Object.keys(REGIONS[st.value].cities).forEach(function (c) { ci.appendChild(opt(c, c)); });
      ci.disabled = false;
    });
    ci.addEventListener('change', function () {
      la.innerHTML = ''; go.disabled = true;
      if (!ci.value) { la.disabled = true; return; }
      REGIONS[st.value].cities[ci.value].forEach(function (l) { la.appendChild(opt(l, LANG_NAMES[l])); });
      la.disabled = false; go.disabled = false;
    });

    function finish(state, city, lang) {
      set(KEY_DONE, '1');
      set(KEY_PREF, JSON.stringify({ state: state, city: city, lang: lang }));
      applyLang(lang);
      document.body.removeChild(wrap);
      document.documentElement.style.overflow = '';
    }
    go.addEventListener('click', function () { finish(st.value, ci.value, la.value); });
    wrap.querySelector('#nt-skip').addEventListener('click', function () { finish('', '', 'en'); });
    document.addEventListener('keydown', function esc(e) {
      if (e.key === 'Escape' && document.body.contains(wrap)) { finish('', '', 'en'); document.removeEventListener('keydown', esc); }
    });
    document.documentElement.style.overflow = 'hidden';
    st.focus();
  }

  document.addEventListener('DOMContentLoaded', function () {
    if (get(KEY_DONE) === '1') {
      try { var p = JSON.parse(get(KEY_PREF) || '{}'); if (p.lang) document.documentElement.setAttribute('data-pref-lang', p.lang); } catch (e) {}
      return;
    }
    build();
  });
})();
