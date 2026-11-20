# Asset License Audit

This document summarizes the provenance and licensing audit of assets in the News Today project:

## 1. Photography & Editorial Imagery
- **Status:** Demo / Editorial Stock Images from template export.
- **Usage Recommendation:** While suitable for demo/staging, replace temporary stock images with original high-resolution photography or royalty-free licensed media (Unsplash, Pexels, CC0) prior to large-scale commercial publishing.
- **Editor Profile Photo:** Enhanced custom portrait of Editor-in-Chief Ravi Shankar Sinha (`assets/cdn.prod.website-files.com/692401e8be8549a781fdbbad/ravi-kumar-editor.webp`) - Authorized for News Today publication.

## 2. Branding & Trademarks
- **Publication Name:** News Today (न्यूज़ टुडे)
- **Publisher / Editor:** Ravi Shankar Sinha
- **Head Office:** Bhikhanpur, Bhagalpur, Bihar, India
- **Copyright Notice:** © 2026 News Today. All Rights Reserved. - Made By Mohit Raj & Team.

## 3. Redirection & External Link Verification
- **Audit Result:** All external template preview and Webflow marketplace links have been systematically replaced with local relative links (`../index.html`, `../about.html`, `../news-category/other-news.html`, etc.).
- **Promotional Overlays:** Floating promotional buttons and badge injection modules have been permanently deactivated.

## 3. Changes in feature/regional-i18n-mobile-alignment
- 20 locally hosted template images and the editor portrait were converted to WebP (same artwork, same licence status as the originals; originals kept in the repo for rollback).
- Fonts (Inter / Inter Tight) are loaded from Google Fonts under the SIL Open Font License. No new third-party assets were added.
- No secrets or API keys were added or committed (scan run on all HTML/JS/JSON/YAML/Python files; only vendor-minified libraries matched generic keywords).
