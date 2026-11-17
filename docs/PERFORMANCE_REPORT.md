# Performance Report (Phases 6 & 7)

| Change | Result |
|---|---|
| Locally hosted images referenced by pages (20 PNG) converted to WebP (max width 1400px, quality 80) | 22.1 MB -> 1.9 MB (about 91% smaller) |
| `ravi-kumar-editor.png` (team/editor photo) -> WebP 400px | 370 KB -> 8.6 KB |
| References updated in HTML | all, 0 broken links after change |
| Lazy-loading | already present on 1,210 of 1,211 `<img>`; kept (the one eager image is above the fold) |
| Duplicate script tags | none found |
| `<title>` check | all 89 pages have a clean, readable title |
| Stray/raw HTML | 1 fixed (`index.html`) |
| Engine bugs fixed | `swapArticleContent` threw `ReferenceError: t is not defined` on all 43 article pages; `art.title.*` keys were never resolved (headlines stayed English in Hindi view) |

Notes: original PNG files are left in the repo for rollback. Delete them once the WebP versions are verified to cut repository size.
Lighthouse/Web Vitals were not run in this environment; run them on the deployed preview.
