# News Today (न्यूज़ टुडे)

A modern, fast, fully independent, and responsive digital news website publication based in **Bhikhanpur, Bhagalpur, Bihar, India**.

## Project Highlights
- **100% Static & GitHub Pages Ready:** Completely independent static site designed to run cleanly on GitHub Pages or any static CDN.
- **Bilingual Translation System:** Full site-wide localization between हिन्दी (Hindi - Default) and English without mixed-language artifacts.
- **Editorial Category Icons:** Bold, crisp 36px Lucide SVG vector iconography across all section headers.
- **Ravi Shankar Sinha Editorial Presence:** Single editor & owner profile integrated across header, team, and article metadata.
- **Comprehensive Coverage:** 89 complete HTML pages spanning World News, Economy, Technology, Politics, Education, Sports, Lifestyle, Science & Health, and Opinion.
- **Cleaned Navigation:** No extraneous promotional badges, templates, or external redirects.

## Technology Stack
- Semantic HTML5 & CSS3
- Responsive Webflow interaction runtime (independent & locally hosted assets)
- Custom bilingual translation engine (`assets/js/i18n.js`)
- Lucide SVG editorial icons
- Google Fonts (`Inter` & `Inter Tight`)

## Deployment to GitHub Pages
1. Push this repository to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial News Today production release"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
2. In your GitHub repository:
   - Go to **Settings** > **Pages**.
   - Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
   - Select branch **main** and folder **/ (root)**.
   - Click **Save**.
3. `.nojekyll` is already included to prevent Jekyll from ignoring folders starting with underscores or dots.

## Licensing & Third-Party Notices
- For third-party libraries and licenses, see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- For asset licensing audit and copyright notices, see [ASSET_LICENSE_AUDIT.md](ASSET_LICENSE_AUDIT.md).
