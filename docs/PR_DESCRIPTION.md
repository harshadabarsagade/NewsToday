# Regional i18n, mobile alignment & UI finalization

Branch: `feature/regional-i18n-mobile-alignment` -> `mohitraj8503/NewsToday:main`

## What changed
| Phase | Change |
|---|---|
| 1 Audit | Found: engine crash on all 43 article pages (`t` undefined), `art.title.*` keys never resolved (English headlines in Hindi view), stray raw HTML in `index.html`, ticker/footer strings stored in the wrong language, static always-Hindi date bar, inline hacks making Our Team misaligned |
| 2 Onboarding | `assets/js/lang-onboarding.js`: first-visit "Welcome to News Today - Choose Your Language" dialog (State -> City -> Language), regional mapping per brief, manual only (no GPS), persisted in `localStorage`, Esc/Skip = English |
| 3 Engine | Fixed engine bugs in `gen_i18n.py` + `i18n.js`; added `i18n-extra.js` (leftover-text isolation layer, locale date formatting, live date/time bar) and `window.NEWS_LANGUAGES` registry for all 22 Eighth Schedule languages + Angika + Bhojpuri. Dictionaries: `trans_dict.json`, `extra_dict.json`; regenerate with `python gen_i18n.py && python gen_extra.py` |
| 4 Alignment | Our Team uses Economy's padding/grid (`.nt-aligned-section`); inline overrides removed; Lifestyle heading hack removed; compact profile card. Economy untouched |
| 5 Mobile | `assets/css/overrides.css`: 320-1440px, no horizontal overflow, 44px touch targets, 16px inputs, language dropdown kept in viewport, stacked cards |
| 6/7 Perf & cleanup | 21 images -> WebP (22.1 MB -> 1.9 MB), raw HTML fixed, no broken links (3,902 refs) |
| 8/9 | License audit updated; no secrets; PR from branch, not pushed to main |

## Test results (jsdom, all 89 pages, both languages)
- English view: 0 Hindi leftovers on 89/89 pages
- Hindi view: 58/89 pages fully clean; remaining items are template/legal pages (see `docs/LANGUAGE_COVERAGE.md`)
- Onboarding: shows on first visit, correct languages for Pune, persists, closes

## NOT done / needs follow-up
- Only English + Hindi have full content; other languages fall back to English by design (architecture ready).
- Privacy/terms legal text, changelog/styleguide/license template pages, product descriptions: not translated.
- Hindi strings added here are machine-assisted: please have a native speaker review.
- Real-device mobile screenshots and Lighthouse were not run in the build environment; attach before merge.

## Deliverables
`docs/LANGUAGE_COVERAGE.md`, `docs/LINK_AUDIT.md`, `docs/PERFORMANCE_REPORT.md`
