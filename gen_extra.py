# -*- coding: utf-8 -*-
"""Build assets/js/i18n-extra.js (leftover-text layer + language registry) from
trans_dict.json (en<->hi pairs) + extra_dict.json (manual en->hi pairs).
Run: python gen_extra.py"""
import json
TR=json.load(open('trans_dict.json',encoding='utf-8'))
EX=json.load(open('extra_dict.json',encoding='utf-8'))
pairs={}
for v in TR.values():
    e,h=v['en'].strip(),v['hi'].strip()
    if e and h and e!=h and len(e)>2: pairs[e]=h
for k,v in EX.items():
    k=k.strip()
    if any('\u0900'<=c<='\u097f' for c in k): pairs[v]=k   # hi->en entry (key is Hindi)
    else: pairs[k]=v
js=open('assets/js/i18n-extra.template.js',encoding='utf-8').read().replace('/*PAIRS*/{}',json.dumps(pairs,ensure_ascii=False))
open('assets/js/i18n-extra.js','w',encoding='utf-8').write(js)
print('pairs',len(pairs))
