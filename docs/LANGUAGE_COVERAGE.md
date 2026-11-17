# Language Coverage Matrix (Phase 3 / Phase 10)

Method: every page was loaded in jsdom in each language; all visible text nodes were scanned (scripts, styles, `<option>` country lists and brand names excluded).

- **English view:** 89/89 pages contain no Hindi text.
- **Hindi view:** 58/89 pages contain no English text. Remaining items are listed below.

## Language support registry (`assets/js/i18n-extra.js` -> `window.NEWS_LANGUAGES`)

| Status | Languages |
|---|---|
| Full content | English (en), Hindi (hi) |
| Architecture ready, falls back to English until translated | Assamese, Bengali, Bodo, Dogri, Gujarati, Kannada, Kashmiri, Konkani, Maithili, Malayalam, Manipuri/Meitei, Marathi, Nepali, Odia, Punjabi, Sanskrit, Santali, Sindhi, Tamil, Telugu, Urdu |
| Regional dialects (architecture ready) | Angika (anp), Bhojpuri (bho) |

To add a language: add its strings to `trans_dict.json` (new column) and extend `gen_i18n.py`; the registry and onboarding already know the language code.

## Per-page results

| Page | EN view: Hindi left | HI view: English left |
|---|---:|---:|
| 404.html | 0 | 0 |
| about.html | 0 | 2 |
| author-posts/benjamin-lee.html | 0 | 2 |
| author-posts/david-lee.html | 0 | 2 |
| author-posts/emma-carter.html | 0 | 2 |
| author-posts/emma-richards.html | 0 | 2 |
| author-posts/ethan-clarke.html | 0 | 2 |
| author-posts/hannah-scott.html | 0 | 2 |
| author-posts/isabella-ruiz-2.html | 0 | 2 |
| author-posts/isabella-ruiz.html | 0 | 2 |
| author-posts/james-patel.html | 0 | 2 |
| author-posts/lucas-carter-2.html | 0 | 2 |
| author-posts/lucas-carter.html | 0 | 2 |
| author-posts/michael-turner-2.html | 0 | 2 |
| author-posts/michael-turner.html | 0 | 2 |
| author-posts/noah-anderson-2.html | 0 | 2 |
| author-posts/noah-anderson.html | 0 | 2 |
| author-posts/ryan-mitchell.html | 0 | 2 |
| author-posts/sofia-alvarez.html | 0 | 2 |
| authors.html | 0 | 2 |
| changelog.html | 0 | 12 |
| checkout.html | 0 | 0 |
| contact-us.html | 0 | 2 |
| index.html | 0 | 0 |
| license.html | 0 | 1 |
| news-category/economy.html | 0 | 0 |
| news-category/global-markets.html | 0 | 0 |
| news-category/global-news.html | 0 | 0 |
| news-category/global-stories.html | 0 | 0 |
| news-category/lifestyle-culture.html | 0 | 0 |
| news-category/other-news.html | 0 | 0 |
| news-category/science-health.html | 0 | 0 |
| news-category/sports-and-entertainment.html | 0 | 0 |
| news-category/technology.html | 0 | 0 |
| news-category/world-news.html | 0 | 0 |
| news-posts/70-nations-gathered-this-weekend-in-geneva-to-finalize-agreement-at-reducing-global-carbon-emissions.html | 0 | 0 |
| news-posts/a-deep-dive-into-the-evolution-of-digital-journalism-and-algorithm-driven-content-feeds.html | 0 | 0 |
| news-posts/a-thrilling-final-match-saw-an-unexpected-champion-rise-stunning-fans-and-analysts-alike.html | 0 | 0 |
| news-posts/after-two-decades-of-dominance-the-legendary-player-bids-farewell-in-an-emotional-press.html | 0 | 0 |
| news-posts/ai-breakthroughs-surge-as-leading-tech-firms-launch-advanced-smart-assistants.html | 0 | 0 |
| news-posts/ai-evolution-speeds-up-as-industry-giants-showcase-future-ready-assistants.html | 0 | 0 |
| news-posts/ai-momentum-grows-as-tech-heavyweights-present-revolutionary-smart-assistants.html | 0 | 0 |
| news-posts/ai-revolution-accelerates-as-tech-giants-unveil-next-gen-intelligent-assistants-2.html | 0 | 0 |
| news-posts/ai-revolution-accelerates-as-tech-giants-unveil-next-gen-intelligent-assistants.html | 0 | 0 |
| news-posts/an-opinion-piece-on-how-authentic-reporting-and-human-ethics-remain-irreplaceable-even.html | 0 | 0 |
| news-posts/artificial-intelligence-tools-are-transforming-how-teams-collaborate-automating-tasks-workplace-efficiency.html | 0 | 0 |
| news-posts/breakthrough-in-renewable-energy-storage-could-transform-global-power-supply-2.html | 0 | 0 |
| news-posts/breakthrough-in-renewable-energy-storage-could-transform-global-power-supply.html | 0 | 0 |
| news-posts/central-banks-signal-policy-shift-amid-inflation-cooldown.html | 0 | 0 |
| news-posts/chatbots-redefine-online-learning-as-students-embrace-virtual-tutors.html | 0 | 0 |
| news-posts/cinema-revenues-hit-a-new-post-pandemic-high-fueled-by-blockbuster-releases-and-strong-attendance.html | 0 | 0 |
| news-posts/crude-oil-prices-climbed-to-new-yearly-highs-amid-renewed-geopolitical.html | 0 | 0 |
| news-posts/demand-for-mental-health-support-tools-continues-to-rise-as-people-seek.html | 0 | 0 |
| news-posts/emerging-asian-economies-are-outperforming-forecasts-driving-global-gdp-growth-upward.html | 0 | 0 |
| news-posts/global-leaders-commit-to-ambitious-climate-goals-at-geneva-summit.html | 0 | 0 |
| news-posts/global-markets-react-positively-to-trade-agreement-between-asia-and-europe.html | 0 | 0 |
| news-posts/innovation-booms-in-ai-as-top-tech-brands-debut-their-latest-intelligent-systems.html | 0 | 0 |
| news-posts/major-cities-adopt-ai-traffic-systems-to-combat-congestion-and-pollution.html | 0 | 0 |
| news-posts/major-streaming-giants-are-in-fierce-competition-to-secure-exclusive-deals-with-top-creators.html | 0 | 0 |
| news-posts/markets-responded-positively-to-the-european-central-banks-signal.html | 0 | 0 |
| news-posts/more-people-are-embracing-minimalist-lifestyles-focusing-on-possessions.html | 0 | 0 |
| news-posts/next-gen-ai-takes-center-stage-as-major-tech-companies-reveal-intelligent-tools.html | 0 | 0 |
| news-posts/plant-based-products-are-taking-over-restaurant-menus-and-grocery.html | 0 | 0 |
| news-posts/recent-satellite-data-shows-the-arctic-ice-melting-faster-than-expected.html | 0 | 0 |
| news-posts/researchers-have-corrected-genetic-mutations-in-human-cells.html | 0 | 0 |
| news-posts/rising-energy-costs-threaten-small-business-recovery.html | 0 | 0 |
| news-posts/scientists-develop-a-next-gen-vaccine-that-could-target-multiple.html | 0 | 0 |
| news-posts/stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown-2.html | 0 | 0 |
| news-posts/stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown-3.html | 0 | 0 |
| news-posts/stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown.html | 0 | 0 |
| news-posts/streaming-platforms-compete-for-viewers-as-subscriptions-hit-record-highs-2.html | 0 | 0 |
| news-posts/streaming-platforms-compete-for-viewers-as-subscriptions-hit-record-highs.html | 0 | 0 |
| news-posts/tech-titans-drive-ai-forward-with-cutting-edge-intelligent-assistant-releases.html | 0 | 0 |
| news-posts/the-dollars-slight-decline-has-boosted-emerging-market-currencies.html | 0 | 0 |
| news-posts/the-gaming-industry-continues-to-boom-as-esports-leagues-attract-massive-corporate-sponsors.html | 0 | 0 |
| news-posts/understanding-why-people-crave-constant-updates-and-how-it-affects-mental-health.html | 0 | 0 |
| news-posts/wellness-retreats-are-becoming-the-go-to-vacation-choice-blending.html | 0 | 0 |
| news-posts/young-professionals-are-moving-away-from-crowded-cities-to-embrace.html | 0 | 0 |
| privacy-policy.html | 0 | 12 |
| product/century-tee-club.html | 0 | 0 |
| product/century-threads.html | 0 | 1 |
| product/hundred-styles.html | 0 | 1 |
| product/infinite-t-shirts.html | 0 | 1 |
| product/limitless-threads.html | 0 | 1 |
| product/presspoint-official-mug.html | 0 | 1 |
| shop.html | 0 | 0 |
| styleguide.html | 0 | 14 |
| subscription.html | 0 | 12 |
| terms-conditions.html | 0 | 12 |

## Known gaps (need human translation / content decision)

- `privacy-policy.html`, `terms-conditions.html`: legal text. Not machine-translated on purpose; needs a reviewed translation.
- `changelog.html`, `styleguide.html`, `license.html`: Webflow template pages with placeholder/Lorem Ipsum content. Recommend removing from the public site or leaving English-only.
- `product/*.html`: product descriptions are template placeholder copy.
- The text "The Daily Placeholder" (template leftover) appears in FAQ/testimonials; treated as a brand name and preserved. Recommend replacing with "News Today".
- All Hindi strings added in this PR (`extra_dict.json`) are machine-assisted and should be reviewed by a native speaker before release.