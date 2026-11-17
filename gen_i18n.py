# -*- coding: utf-8 -*-
"""Generate assets/js/i18n.js from trans_dict.json."""
import json, re

TR = json.load(open("trans_dict.json", encoding="utf-8"))

# Build the translations object literal for JS
def js_str(s):
    return json.dumps(s, ensure_ascii=False)

# Group by section for nav/cat/ui
def section_map(section):
    out = {}
    for k, v in TR.items():
        if k.startswith(section + "."):
            leaf = k[len(section) + 1:]
            out[leaf] = v
    return out

nav_map = section_map("nav")
cat_map = section_map("cat")
ui_map = section_map("ui")

# Article titles by slug
art_titles = {}
for k, v in TR.items():
    if k.startswith("art.title."):
        slug = k[len("art.title."):]
        art_titles[slug] = v

# Footer map (data-i18n-footer leaves)
footer_map = {}
for k, v in TR.items():
    if k.startswith("footer."):
        leaf = k[len("footer."):]
        footer_map[leaf] = v

# Page map
page_map = {}
for k, v in TR.items():
    if k not in nav_map and k not in cat_map and k not in ui_map and not k.startswith("footer.") and not k.startswith("art."):
        page_map[k] = v

lines = []
lines.append("/*")
lines.append(" * News Today - Complete Multilingual Localization Engine")
lines.append(" * English (en) <-> Hindi (hi). Default: Hindi.")
lines.append(" * Persists selection in localStorage (news_today_lang).")
lines.append(" */")
lines.append("(function() {")
lines.append("  'use strict';")
lines.append("")
lines.append("  var translations = {")
for lang in ("hi", "en"):
    lines.append("    " + lang + ": {")
    # nav
    lines.append("      nav: {")
    items = list(nav_map.items())
    for i, (k, v) in enumerate(items):
        comma = "," if i < len(items) - 1 else ""
        lines.append("        " + js_str(k) + ": " + js_str(v[lang]) + comma)
    lines.append("      },")
    # cat
    lines.append("      cat: {")
    items = list(cat_map.items())
    for i, (k, v) in enumerate(items):
        comma = "," if i < len(items) - 1 else ""
        lines.append("        " + js_str(k) + ": " + js_str(v[lang]) + comma)
    lines.append("      },")
    # ui
    lines.append("      ui: {")
    items = list(ui_map.items())
    for i, (k, v) in enumerate(items):
        comma = "," if i < len(items) - 1 else ""
        lines.append("        " + js_str(k) + ": " + js_str(v[lang]) + comma)
    lines.append("      },")
    # page keys (full dotted keys for data-i18n)
    lines.append("      page: {")
    items = list(page_map.items())
    for i, (k, v) in enumerate(items):
        comma = "," if i < len(items) - 1 else ""
        lines.append("        " + js_str(k) + ": " + js_str(v[lang]) + comma)
    lines.append("      },")
    # footer
    lines.append("      footer: {")
    items = list(footer_map.items())
    for i, (k, v) in enumerate(items):
        comma = "," if i < len(items) - 1 else ""
        lines.append("        " + js_str(k) + ": " + js_str(v[lang]) + comma)
    lines.append("      },")
    # article titles
    lines.append("      artTitles: {")
    items = list(art_titles.items())
    for i, (slug, v) in enumerate(items):
        comma = "," if i < len(items) - 1 else ""
        lines.append("        " + js_str(slug) + ": " + js_str(v[lang]) + comma)
    lines.append("      },")
    lines.append("    }" + ("," if lang == "hi" else ""))
lines.append("  };")
lines.append("")
lines.append("  // Shared article body (same for all articles)")
lines.append("  var artBody = {")
lines.append("    hi: [")
for i, v in enumerate([
    TR["art.body.p0"]["hi"], TR["art.body.p1"]["hi"], TR["art.body.p2"]["hi"],
    TR["art.body.p3"]["hi"], TR["art.body.p4"]["hi"], TR["art.body.p5"]["hi"], TR["art.body.p6"]["hi"]]):
    comma = "," if i < 6 else ""
    lines.append("      " + js_str(v) + comma)
lines.append("    ],")
lines.append("    en: [")
for i, v in enumerate([
    TR["art.body.p0"]["en"], TR["art.body.p1"]["en"], TR["art.body.p2"]["en"],
    TR["art.body.p3"]["en"], TR["art.body.p4"]["en"], TR["art.body.p5"]["en"], TR["art.body.p6"]["en"]]):
    comma = "," if i < 6 else ""
    lines.append("      " + js_str(v) + comma)
lines.append("    ],")
lines.append("  };")
lines.append("")
lines.append("  var artH4 = {")
lines.append("    hi: [")
for i, k in enumerate(["art.h4.0", "art.h4.1", "art.h4.2"]):
    comma = "," if i < 2 else ""
    lines.append("      " + js_str(TR[k]["hi"]) + comma)
lines.append("    ],")
lines.append("    en: [")
for i, k in enumerate(["art.h4.0", "art.h4.1", "art.h4.2"]):
    comma = "," if i < 2 else ""
    lines.append("      " + js_str(TR[k]["en"]) + comma)
lines.append("    ],")
lines.append("  };")
lines.append("")
lines.append("  var artCatEn = {};")
lines.append("")
lines.append("  function get(key) {")
lines.append("    var t = translations[currentLang];")
lines.append("    if (!t) return key;")
lines.append("    // direct page key")
lines.append("    if (t.page && t.page[key] !== undefined) return t.page[key];")
lines.append("    return key;")
lines.append("  }")
lines.append("")
lines.append("  var currentLang = localStorage.getItem('news_today_lang') || 'hi';")
lines.append("")
lines.append("  function applyLanguage(lang) {")
lines.append("    if (!translations[lang]) lang = 'hi';")
lines.append("    currentLang = lang;")
lines.append("    localStorage.setItem('news_today_lang', lang);")
lines.append("    var t = translations[lang];")
lines.append("")
lines.append("    document.documentElement.lang = lang;")
lines.append("    if (lang === 'ur') { document.body.setAttribute('dir', 'rtl'); }")
lines.append("    else { document.body.removeAttribute('dir'); }")
lines.append("")
lines.append("    // Language button text")
lines.append("    var btn = document.querySelector('.lang-selector-btn .lang-btn-text');")
lines.append("    if (btn) btn.textContent = t.langName || translations.hi.langName;")
lines.append("")
lines.append("    // data-i18n (full dotted key, e.g. nav.home, cat.worldNews, page.xxx)")
lines.append("    document.querySelectorAll('[data-i18n]').forEach(function(el) {")
lines.append("      var key = el.getAttribute('data-i18n');")
lines.append("      var val = null;")
lines.append("      if (t.page && t.page[key] !== undefined) val = t.page[key];")
lines.append("      else if (key.indexOf('nav.') === 0 && t.nav && t.nav[key.slice(4)] !== undefined) val = t.nav[key.slice(4)];")
lines.append("      else if (key.indexOf('cat.') === 0 && t.cat && t.cat[key.slice(4)] !== undefined) val = t.cat[key.slice(4)];")
lines.append("      else if (key.indexOf('ui.') === 0 && t.ui && t.ui[key.slice(3)] !== undefined) val = t.ui[key.slice(3)];")
lines.append("      else if (key.indexOf('footer.') === 0 && t.footer && t.footer[key.slice(7)] !== undefined) val = t.footer[key.slice(7)];")
lines.append("      if (val !== null && val !== undefined) el.textContent = val;")
lines.append("    });")
lines.append("")
lines.append("    // Legacy attribute conventions")
lines.append("    document.querySelectorAll('[data-i18n-nav]').forEach(function(el) {")
lines.append("      var key = el.getAttribute('data-i18n-nav');")
lines.append("      if (t.nav && t.nav[key] !== undefined) el.textContent = t.nav[key];")
lines.append("    });")
lines.append("    document.querySelectorAll('[data-i18n-cat]').forEach(function(el) {")
lines.append("      var key = el.getAttribute('data-i18n-cat');")
lines.append("      if (t.cat && t.cat[key] !== undefined) el.textContent = t.cat[key];")
lines.append("    });")
lines.append("    document.querySelectorAll('[data-i18n-ui]').forEach(function(el) {")
lines.append("      var key = el.getAttribute('data-i18n-ui');")
lines.append("      if (t.ui && t.ui[key] !== undefined) el.textContent = t.ui[key];")
lines.append("    });")
lines.append("    document.querySelectorAll('[data-i18n-footer]').forEach(function(el) {")
lines.append("      var key = el.getAttribute('data-i18n-footer');")
lines.append("      if (key === 'quickLinks') el.textContent = t.ui.quickLinks;")
lines.append("      else if (key === 'legalLinks') el.textContent = t.ui.legalLinks;")
lines.append("      else if (key === 'contactUs') el.textContent = t.ui.contactOffice;")
lines.append("      else if (key === 'address') el.textContent = t.nav.headOffice;")
lines.append("      else if (t.footer && t.footer[key] !== undefined) el.textContent = t.footer[key];")
lines.append("    });")
lines.append("")
lines.append("    // Subscribe buttons")
lines.append("    document.querySelectorAll('.primary-button-text').forEach(function(el) {")
lines.append("      el.textContent = t.nav.subscribe;")
lines.append("    });")
lines.append("")
lines.append("    // Article content swap (news posts)")
lines.append("    swapArticleContent(lang);")
lines.append("")
lines.append("    // Active state on dropdown items")
lines.append("    document.querySelectorAll('.lang-dropdown-item').forEach(function(item) {")
lines.append("      if (item.getAttribute('data-lang') === lang) item.classList.add('active');")
lines.append("      else item.classList.remove('active');")
lines.append("    });")
lines.append("  }")
lines.append("")
lines.append("  function swapArticleContent(lang) {")
lines.append("    var isPost = document.querySelector('.news-details-heading') || document.querySelector('.world-news-title');")
lines.append("    if (!isPost) return;")
lines.append("    var slug = null;")
lines.append("    var m = window.location.pathname.match(/news-posts\\/([^\\/]+)\\.html$/);")
lines.append("    if (m) slug = m[1];")
lines.append("    if (!slug) return;")
lines.append("")
lines.append("    // Title")
lines.append("    var h1 = document.querySelector('.news-details-heading');")
lines.append("    if (h1 && t.artTitles && t.artTitles[slug] !== undefined) h1.textContent = t.artTitles[slug];")
lines.append("")
lines.append("    // Category")
lines.append("    var catLinks = document.querySelectorAll('.news-category-text');")
lines.append("    catLinks.forEach(function(link) {")
lines.append("      var txt = link.textContent.trim();")
lines.append("      // map en category -> hi")
lines.append("      var mapped = null;")
lines.append("      if (lang === 'hi') {")
lines.append("        if (txt === 'World News') mapped = 'विश्व समाचार';")
lines.append("        else if (txt === 'Economy') mapped = 'अर्थव्यवस्था';")
lines.append("        else if (txt === 'Technology') mapped = 'तकनीक';")
lines.append("        else if (txt === 'Science & Health' || txt === 'Science & Environment') mapped = 'विज्ञान एवं स्वास्थ्य';")
lines.append("        else if (txt === 'Lifestyle & Culture') mapped = 'जीवनशैली एवं संस्कृति';")
lines.append("        else if (txt === 'Sports & Entertainment' || txt === 'Sports and Entertainment') mapped = 'खेल और मनोरंजन';")
lines.append("        else if (txt === 'Entertainment') mapped = 'मनोरंजन';")
lines.append("        else if (txt === 'Other news' || txt === 'अन्य ख़बरें') mapped = 'अन्य ख़बरें';")
lines.append("        else if (txt === 'Global Markets') mapped = 'वैश्विक बाजार';")
lines.append("        else if (txt === 'Global Stories') mapped = 'वैश्विक कहानियाँ';")
lines.append("        else if (txt === 'Global News') mapped = 'विश्व समाचार';")
lines.append("      }")
lines.append("      if (mapped) link.textContent = mapped;")
lines.append("    });")
lines.append("")
lines.append("    // Author name")
lines.append("    var author = document.querySelector('.author-name-main');")
lines.append("    if (author) author.textContent = (lang === 'hi') ? 'रवि कुमार' : 'Ravi Kumar';")
lines.append("")
lines.append("    // Date")
lines.append("    var dateEls = document.querySelectorAll('.news-category-text');")
lines.append("    dateEls.forEach(function(el) {")
lines.append("      var txt = el.textContent.trim();")
lines.append("      if (txt === 'November 24, 2025' && lang === 'hi') el.textContent = '24 नवंबर, 2025';")
lines.append("      else if (txt === 'November 25, 2025' && lang === 'hi') el.textContent = '25 नवंबर, 2025';")
lines.append("      else if (txt === '24 नवंबर, 2025' && lang === 'en') el.textContent = 'November 24, 2025';")
lines.append("      else if (txt === '25 नवंबर, 2025' && lang === 'en') el.textContent = 'November 25, 2025';")
lines.append("    });")
lines.append("")
lines.append("    // Body paragraphs + h4")
lines.append("    var body = document.querySelector('.news-details-content');")
lines.append("    if (body) {")
lines.append("      var paras = body.querySelectorAll('p');")
lines.append("      var h4s = body.querySelectorAll('h4');")
lines.append("      var pData = (lang === 'hi') ? artBody.hi : artBody.en;")
lines.append("      var hData = (lang === 'hi') ? artH4.hi : artH4.en;")
lines.append("      paras.forEach(function(p, i) {")
lines.append("        if (pData[i] !== undefined) p.textContent = pData[i];")
lines.append("      });")
lines.append("      h4s.forEach(function(h, i) {")
lines.append("        if (hData[i] !== undefined) h.textContent = hData[i];")
lines.append("      });")
lines.append("    }")
lines.append("  }")
lines.append("")
lines.append("  // Meta title / description")
lines.append("  function updateMeta(lang) {")
lines.append("    var slug = null;")
lines.append("    var m = window.location.pathname.match(/news-posts\\/([^\\/]+)\\.html$/);")
lines.append("    if (m) slug = m[1];")
lines.append("    var t = translations[lang];")
lines.append("    if (slug && t.artTitles && t.artTitles[slug]) {")
lines.append("      var title = t.artTitles[slug];")
lines.append("      var mt = document.querySelector('meta[property=\"og:title\"]');")
lines.append("      if (mt) mt.setAttribute('content', title);")
lines.append("      var tt = document.querySelector('meta[name=\"twitter:title\"]');")
lines.append("      if (tt) tt.setAttribute('content', title);")
lines.append("      var htag = document.querySelector('title');")
lines.append("      if (htag) htag.textContent = title + ' | News Today';")
lines.append("      var md = document.querySelector('meta[name=\"description\"]');")
lines.append("      if (md) md.setAttribute('content', title);")
lines.append("      var td = document.querySelector('meta[name=\"twitter:description\"]');")
lines.append("      if (td) td.setAttribute('content', title);")
lines.append("    }")
lines.append("  }")
lines.append("")
lines.append("  window.setNewsLanguage = function(lang) {")
lines.append("    applyLanguage(lang);")
lines.append("    updateMeta(lang);")
lines.append("  };")
lines.append("")
lines.append("  document.addEventListener('DOMContentLoaded', function() {")
lines.append("    applyLanguage(currentLang);")
lines.append("    updateMeta(currentLang);")
lines.append("")
lines.append("    document.querySelectorAll('.lang-dropdown-item').forEach(function(item) {")
lines.append("      item.addEventListener('click', function(e) {")
lines.append("        e.preventDefault();")
lines.append("        var selected = this.getAttribute('data-lang');")
lines.append("        applyLanguage(selected);")
lines.append("        updateMeta(selected);")
lines.append("        this.parentElement.style.display = 'none';")
lines.append("      });")
lines.append("    });")
lines.append("")
lines.append("    // Close dropdown on outside click / ESC")
lines.append("    document.addEventListener('click', function(e) {")
lines.append("      var wrap = document.querySelector('.lang-selector-wrap');")
lines.append("      if (wrap && !wrap.contains(e.target)) {")
lines.append("        var menu = document.querySelector('.lang-dropdown-menu');")
lines.append("        if (menu) menu.style.display = 'none';")
lines.append("      }")
lines.append("    }, true);")
lines.append("    document.addEventListener('keydown', function(e) {")
lines.append("      if (e.key === 'Escape') {")
lines.append("        var menu = document.querySelector('.lang-dropdown-menu');")
lines.append("        if (menu) menu.style.display = 'none';")
lines.append("      }")
lines.append("    });")
lines.append("  });")
lines.append("")
lines.append("})();")
lines.append("")
out = "\n".join(lines) + "\n"
open("assets/js/i18n.js", "w", encoding="utf-8").write(out)
print("i18n.js written:", len(out), "chars")
