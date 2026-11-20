# -*- coding: utf-8 -*-
"""Inject data-i18n attributes into all HTML pages + fix malformed footer."""
import re, glob, json

TR = json.load(open("trans_dict.json", encoding="utf-8"))

# text -> (key, en_text) from both en and hi values
text2key = {}
for key, v in TR.items():
    for lang in ("en", "hi"):
        t = v[lang].strip()
        if t and t not in text2key:
            text2key[t] = (key, v["en"].strip())

sorted_texts = sorted(text2key.keys(), key=len, reverse=True)

FILES = sorted(glob.glob('*.html') + glob.glob('news-category/*.html') +
               glob.glob('news-posts/*.html') + glob.glob('author-posts/*.html') +
               glob.glob('product/*.html'))

NON_TRANS = set(['•', '|', '/', '–', '—', '·'])
PROPER = set(['News Today','Ravi Shankar Sinha','Janet Howell','GlobalEdge Capital',
    'U.S. Bureau of Labor Statistics','Federal Reserve','Dow Jones','S&P','Nasdaq',
    'FTSE','DAX','Nikkei','FOMC','Mohit Raj','The Daily Placeholder','Inter','Inter Tight'])

def is_proper_or_technical(t):
    if t in NON_TRANS: return True
    if re.fullmatch(r'[\d\s\.,:$/%+\-()#@]+', t): return True
    if t.startswith('http') or t.startswith('www') or '@' in t or 'tel:' in t or 'mailto:' in t: return True
    if t.startswith('#') and len(t) > 1: return True
    if t in PROPER: return True
    return False

def fix_malformed_footer(html):
    def repl(m):
        rel, page, linktext, cls, keyattr, hinditext = m.groups()
        url = (rel or '') + page + '.html'
        return '<a href="%s" class="%s" data-i18n="footer.%s">%s</a>' % (url, cls, keyattr, hinditext)
    html = re.sub(
        r'<a href="<a href="(\.\./)?(privacy-policy|terms-conditions)\.html" class="footer-navtext">([^<]+)</a>" class="footer-navtext" data-i18n-nav="(privacyPolicy|terms)">([^<]+)</a>',
        repl, html)
    return html

def strip_blocks(html):
    """Protect <script> and <style> blocks; return (parts, protectors)"""
    protectors = []
    def guard(m):
        protectors.append(m.group(0))
        return "\x00PROTECT%d\x00" % (len(protectors) - 1)
    html = re.sub(r'<script\b[^>]*>.*?</script>', guard, html, flags=re.S)
    html = re.sub(r'<style\b[^>]*>.*?</style>', guard, html, flags=re.S)
    return html, protectors

def restore_blocks(html, protectors):
    for i, p in enumerate(protectors):
        html = html.replace("\x00PROTECT%d\x00" % i, p)
    return html

def inject_data_i18n(html):
    pattern = re.compile(r'(>)\s*([^<>]{2,})\s*(<)')
    def repl(m):
        gt, text, lt = m.group(1), m.group(2), m.group(3)
        t = text.strip()
        if not t or is_proper_or_technical(t):
            return m.group(0)
        # Idempotency: skip if already inside a data-i18n span
        start = m.start()
        last_lt = html.rfind('<', 0, start)
        if last_lt != -1 and 'data-i18n=' in html[last_lt:start]:
            return m.group(0)
        lookup = text2key.get(t)
        if not lookup:
            return m.group(0)
        key, en = lookup
        # Keep current text as fallback; add data-i18n
        return '%s<span data-i18n="%s">%s</span>%s' % (gt, key, text, lt)
    return pattern.sub(repl, html)

total_fixed = 0
total_injected = 0
total_spans = 0
for path in FILES:
    html = open(path, encoding='utf-8', errors='ignore').read()
    orig = html
    html = fix_malformed_footer(html)
    if html != orig:
        total_fixed += 1
    inner, prot = strip_blocks(html)
    inner2 = inject_data_i18n(inner)
    html2 = restore_blocks(inner2, prot)
    if html2 != html:
        total_injected += 1
    total_spans += html2.count('data-i18n="') - html.count('data-i18n="')
    open(path, 'w', encoding='utf-8').write(html2)

print("Pages with footer fixed:", total_fixed, "of", len(FILES))
print("Pages with data-i18n injected:", total_injected, "of", len(FILES))
print("Net new data-i18n spans:", total_spans)
