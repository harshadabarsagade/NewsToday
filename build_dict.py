# -*- coding: utf-8 -*-
"""Build the centralized en<->hi translation dictionary and write i18n.js."""
import json

# key -> {en, hi}
# Brand / proper nouns stay identical in both languages.
TR = {}

def add(key, en, hi=None):
    TR[key] = {"en": en, "hi": hi if hi is not None else en}

# ---------- Language names ----------
add("langName", "English", "हिन्दी")

# ---------- Navigation ----------
add("nav.home", "Home", "होम")
add("nav.allPages", "All Pages", "सभी पेज")
add("nav.newsCategories", "News Categories", "समाचार श्रेणियाँ")
add("nav.about", "About", "हमारे बारे में")
add("nav.subscription", "Subscription", "सदस्यता")
add("nav.authors", "Authors", "संपादकीय टीम")
add("footer.editorialTeam", "Editorial Team", "संपादकीय टीम")
add("nav.editorProfile", "Editor Profile", "संपादक प्रोफाइल")
add("nav.contact", "Contact", "संपर्क करें")
add("nav.privacyPolicy", "Privacy Policy", "गोपनीयता नीति")
add("nav.terms", "Terms & Conditions", "नियम एवं शर्तें")
add("nav.subscribe", "Subscribe", "सब्सक्राइब करें")
add("nav.readMore", "Read More", "पूरी खबर पढ़ें")
add("nav.latestNews", "Latest News", "ताज़ा ख़बरें")

# ---------- Categories ----------
add("cat.topStories", "Top Global Stories", "प्रमुख वैश्विक समाचार")
add("cat.worldNews", "World News", "विश्व समाचार")
add("cat.economy", "Economy", "अर्थव्यवस्था")
add("cat.technology", "Technology", "तकनीक")
add("cat.scienceHealth", "Science & Health", "विज्ञान एवं स्वास्थ्य")
add("cat.lifestyleCulture", "Lifestyle & Culture", "जीवनशैली एवं संस्कृति")
add("cat.sports", "Sports & Entertainment", "खेल और मनोरंजन")
add("cat.entertainment", "Entertainment", "मनोरंजन")
add("cat.otherNews", "Other News", "अन्य ख़बरें")
add("cat.globalMarkets", "Global Markets", "वैश्विक बाजार")
add("cat.globalStories", "Global Stories", "वैश्विक कहानियाँ")

# ---------- UI ----------
add("ui.seeAll", "See All", "सभी देखें")
add("ui.viewProfile", "View Profile", "प्रोफाइल देखें")
add("ui.owner", "Owner / Editor: Ravi Shankar Sinha", "स्वामी / संपादक: रवि शंकर सिन्हा")
add("ui.quickLinks", "Quick Links", "मुख्य लिंक")
add("ui.legalLinks", "Legal Links", "महत्वपूर्ण लिंक")
add("ui.contactOffice", "Contact Office", "संपर्क कार्यालय")
add("ui.date", "Sunday, October 26, 2025", "रविवार, 26 अक्टूबर 2025")

# ---------- Footer ----------
add("footer.subscribeHeading", "Subscribe to Our Newsletter to Stay ahead with daily headlines.", "दैनिक मुख्य समाचारों से जुड़े रहने के लिए न्यूज़लेटर सब्सक्राइब करें।")
add("footer.footerText", "Truthful, accurate and impartial journalism with you every moment - the latest news from Bhagalpur and the country and the world.", "सच्ची, सटीक और निष्पक्ष पत्रकारिता के साथ हर पल आपके साथ - भागलपुर और देश-दुनिया की ताज़ा ख़बरें।")
add("footer.socialText", "Connect with us on social media:", "सोशल मीडिया पर जुड़ें:")
add("footer.allRightsReserved", "© 2026 News Today. All Rights Reserved. - Made By Mohit Raj & Team", "© 2026 News Today. सर्वाधिकार सुरक्षित। - मोहित राज एवं टीम द्वारा निर्मित")
add("footer.headOffice", "Head Office: Bhikhanpur, Bhagalpur, Bihar, India", "कार्यालय: भीखनपुर, भागलपुर, बिहार, भारत")
add("footer.phone", "Phone: +91 99731 89133", "फोन: +91 99731 89133")
add("footer.email", "Email: ravingsinha25@gmail.com", "ईमेल: ravingsinha25@gmail.com")
add("footer.ctaTitle", "Join over 1 million aware readers - don't miss any big news.", "10 लाख से अधिक जागरूक पाठकों के साथ जुड़ें - कोई बड़ी खबर न चूकें।")
add("footer.ctaSubtext", "Stay informed wherever you are — join our growing community of readers and followers across social platforms.", "Stay informed wherever you are — join our growing community of readers and followers across social platforms.")
add("footer.subscribePart1", "Subscribe to our newsletter to", "दैनिक मुख्य समाचारों से जुड़े रहने के लिए")
add("footer.subscribePart2", "stay ahead with daily headlines.", "न्यूज़लेटर सब्सक्राइब करें।")
add("footer.formPlaceholder", "Enter your email", "अपना ईमेल दर्ज करें")
add("footer.formSubmit", "Subscribe", "सब्सक्राइब करें")
add("footer.formWait", "Please wait...", "कृपया प्रतीक्षा करें...")
add("footer.formSuccess", "Thank you! Your submission has been received!", "धन्यवाद! आपका सबमिशन प्राप्त हो गया है!")
add("footer.formError", "Oops! Something went wrong while submitting the form.", "ओहॉ! फॉर्म सबमिट करने में कुछ गड़बड़ हो गई।")

# ---------- Article content (shared body) ----------
add("art.headline", "Breakthrough in Renewable Energy Storage Could Transform Global Power Supply", "नवीकरणीय ऊर्जा भंडारण में सफलता वैश्विक बिजली आपूर्ति को बदल सकती है")
add("art.author", "Ravi Shankar Sinha", "रवि शंकर सिन्हा")
add("art.date", "November 24, 2025", "24 नवंबर, 2025")
add("art.body.p0", "Global stock markets rallied sharply this week as investors reacted positively to new data showing that inflation in the United States and other major economies has continued to cool, easing fears of prolonged monetary tightening by central banks.", "इस सप्ताह वैश्विक शेयर बाजारों में तेजी आई क्योंकि निवेशकों ने नए डेटा पर सकारात्मक प्रतिक्रिया दी जिसमें पता चला कि संयुक्त राज्य अमेरिका और अन्य बड़ी अर्थव्यवस्थाओं में मुद्रास्फीति ठंडी हो रही है, जिससे केंद्रीय बैंकों द्वारा लंबे समय तक मौद्रिक कसने के डर को कम किया गया है।")
add("art.body.p1", "The Dow Jones Industrial Average climbed more than 2.4%, its strongest weekly gain since June, while the S&P 500 and Nasdaq Composite each jumped 2.1% and 2.8%, respectively. European and Asian markets followed suit, with the FTSE 100, DAX, and Nikkei 225 all closing higher as investor sentiment improved across global exchanges. According to the latest report from the U.S. Bureau of Labor Statistics, the Consumer Price Index (CPI) rose by just 0.2% in September, bringing the annual inflation rate down to 3.1% — slightly below economists’ expectations. The steady decline in price growth has raised hopes that the Federal Reserve may soon begin to ease its aggressive interest rate policy.", "डाउ जोन्स इंडस्ट्रियल एवरेज 2.4% से अधिक चढ़ा, जो जून के बाद का सबसे बड़ा साप्ताहिक लाभ है, जबकि एसएंडपी 500 और नैस्डैक कंपोजिट क्रमशः 2.1% और 2.8% बढ़े। यूरोपीय और एशियाई बाजारों ने भी इसका अनुसरण किया, जहां एफटीएसई 100, डैक्स और निक्केई 225 सभी ऊंचे पर बंद हुए क्योंकि वैश्विक एक्सचेंजों में निवेशक भावना में सुधार हुआ। अमेरिकी श्रम सांख्यिकी ब्यूरो की नवीनतम रिपोर्ट के अनुसार, उपभोक्ता मूल्य सूचकांक (सीपीआई) सितंबर में सिर्फ 0.2% बढ़ा, जिससे वार्षिक मुद्रास्फीति दर घटकर 3.1% रह गई — अर्थशास्त्रियों की उम्मीदों से थोड़ा कम। मूल्य वृद्धि में स्थिर गिरावट ने उम्मीदें बढ़ाई हैं कि फेडरल रिजर्व जल्द ही अपनी आक्रामक ब्याज दर नीति में ढील देना शुरू कर सकता है।")
add("art.body.p2", "\u201cThis is a clear signal that inflationary pressures are stabilizing,\u201d said Janet Howell, Senior Market Analyst at GlobalEdge Capital. \u201cInvestors are starting to believe the Fed might actually pull off a soft landing — slowing inflation without causing a recession.\u201d", "\u201cयह मुद्रास्फीति के दबाव के स्थिर होने का स्पष्ट संकेत है,\u201d ग्लोबलएज कैपिटल में वरिष्ठ बाजार विश्लेषक जेनेट हॉवेल ने कहा। \u201cनिवेशकों को विश्वास होने लगा है कि फेड वास्तव में एक सॉफ्ट लैंडिंग हासिल कर सकता है — मंदी का कारण बने बिना मुद्रास्फीति को धीमा करना।\u201d")
add("art.body.p3", "The Dow Jones Industrial Average climbed more than 2.4%, its strongest weekly gain since June, while the S&P 500 and Nasdaq Composite each jumped 2.1% and 2.8%, respectively. European and Asian markets followed suit, with the FTSE 100, DAX, and Nikkei 225 all closing higher as investor sentiment improved across global exchanges. According to the latest report from the U.S. Bureau of Labor Statistics, the Consumer Price Index (CPI) rose by just 0.2% in September, bringing the annual inflation rate down to 3.1% — slightly below economists’ expectations. The steady decline in price growth has raised hopes that the Federal Reserve may soon begin to ease its aggressive interest rate policy.", "डाउ जोन्स इंडस्ट्रियल एवरेज 2.4% से अधिक चढ़ा, जो जून के बाद का सबसे बड़ा साप्ताहिक लाभ है, जबकि एसएंडपी 500 और नैस्डैक कंपोजिट क्रमशः 2.1% और 2.8% बढ़े। यूरोपीय और एशियाई बाजारों ने भी इसका अनुसरण किया, जहां एफटीएसई 100, डैक्स और निक्केई 225 सभी ऊंचे पर बंद हुए क्योंकि वैश्विक एक्सचेंजों में निवेशक भावना में सुधार हुआ। अमेरिकी श्रम सांख्यिकी ब्यूरो की नवीनतम रिपोर्ट के अनुसार, उपभोक्ता मूल्य सूचकांक (सीपीआई) सितंबर में सिर्फ 0.2% बढ़ा, जिससे वार्षिक मुद्रास्फीति दर घटकर 3.1% रह गई — अर्थशास्त्रियों की उम्मीदों से थोड़ा कम। मूल्य वृद्धि में स्थिर गिरावट ने उम्मीदें बढ़ाई हैं कि फेडरल रिजर्व जल्द ही अपनी आक्रामक ब्याज दर नीति में ढील देना शुरू कर सकता है।")
add("art.body.p4", "\u201cThis is a clear signal that inflationary pressures are stabilizing,\u201d said Janet Howell, Senior Market Analyst at GlobalEdge Capital. \u201cInvestors are starting to believe the Fed might actually pull off a soft landing — slowing inflation without causing a recession.\u201d", "\u201cयह मुद्रास्फीति के दबाव के स्थिर होने का स्पष्ट संकेत है,\u201d ग्लोबलएज कैपिटल में वरिष्ठ बाजार विश्लेषक जेनेट हॉवेल ने कहा। \u201cनिवेशकों को विश्वास होने लगा है कि फेड वास्तव में एक सॉफ्ट लैंडिंग हासिल कर सकता है — मंदी का कारण बने बिना मुद्रास्फीति को धीमा करना।\u201d")
add("art.body.p5", "The Dow Jones Industrial Average climbed more than 2.4%, its strongest weekly gain since June, while the S&P 500 and Nasdaq Composite each jumped 2.1% and 2.8%, respectively. European and Asian markets followed suit, with the FTSE 100, DAX, and Nikkei 225 all closing higher as investor sentiment improved across global exchanges. According to the latest report from the U.S. Bureau of Labor Statistics, the Consumer Price Index (CPI) rose by just 0.2% in September, bringing the annual inflation rate down to 3.1% — slightly below economists’ expectations. The steady decline in price growth has raised hopes that the Federal Reserve may soon begin to ease its aggressive interest rate policy.", "डाउ जोन्स इंडस्ट्रियल एवरेज 2.4% से अधिक चढ़ा, जो जून के बाद का सबसे बड़ा साप्ताहिक लाभ है, जबकि एसएंडपी 500 और नैस्डैक कंपोजिट क्रमशः 2.1% और 2.8% बढ़े। यूरोपीय और एशियाई बाजारों ने भी इसका अनुसरण किया, जहां एफटीएसई 100, डैक्स और निक्केई 225 सभी ऊंचे पर बंद हुए क्योंकि वैश्विक एक्सचेंजों में निवेशक भावना में सुधार हुआ। अमेरिकी श्रम सांख्यिकी ब्यूरो की नवीनतम रिपोर्ट के अनुसार, उपभोक्ता मूल्य सूचकांक (सीपीआई) सितंबर में सिर्फ 0.2% बढ़ा, जिससे वार्षिक मुद्रास्फीति दर घटकर 3.1% रह गई — अर्थशास्त्रियों की उम्मीदों से थोड़ा कम। मूल्य वृद्धि में स्थिर गिरावट ने उम्मीदें बढ़ाई हैं कि फेडरल रिजर्व जल्द ही अपनी आक्रामक ब्याज दर नीति में ढील देना शुरू कर सकता है।")
add("art.body.p6", "\u201cThis is a clear signal that inflationary pressures are stabilizing,\u201d said Janet Howell, Senior Market Analyst at GlobalEdge Capital. \u201cInvestors are starting to believe the Fed might actually pull off a soft landing — slowing inflation without causing a recession.\u201d", "\u201cयह मुद्रास्फीति के दबाव के स्थिर होने का स्पष्ट संकेत है,\u201d ग्लोबलएज कैपिटल में वरिष्ठ बाजार विश्लेषक जेनेट हॉवेल ने कहा। \u201cनिवेशकों को विश्वास होने लगा है कि फेड वास्तव में एक सॉफ्ट लैंडिंग हासिल कर सकता है — मंदी का कारण बने बिना मुद्रास्फीति को धीमा करना।\u201d")
add("art.h4.0", "Global Confidence Strengthens.", "वैश्विक विश्वास मजबूत हो रहा है।")
add("art.h4.1", "Tech and Financial Stocks Lead the Rally.", "टेक और वित्तीय शेयर रैली का नेतृत्व कर रहे हैं।")
add("art.h4.2", "The next major event on investors\u2019 calendars is the upcoming Federal Open Market Committee (FOMC) meeting into 2026.", "निवेशकों के कैलेंडर पर अगली बड़ी घटना आगामी फेडरल ओपन मार्केट कमेटी (एफओएमसी) बैठक 2026 में है।")

# Article titles per slug -> Hindi
TITLES_HI = {
"70-nations-gathered-this-weekend-in-geneva-to-finalize-agreement-at-reducing-global-carbon-emissions": "इस सप्ताह के अंत में 70 देशों ने वैश्विक कार्बन उत्सर्जन को कम करने के समझौते को अंतिम रूप देने के लिए जिनेवा में एकत्र हुए",
"a-deep-dive-into-the-evolution-of-digital-journalism-and-algorithm-driven-content-feeds": "डिजिटल पत्रकारिता और एल्गोरिदम-चालित सामग्री फ़ीड के विकास में गहराई से उतरना",
"a-thrilling-final-match-saw-an-unexpected-champion-rise-stunning-fans-and-analysts-alike": "एक रोमांचक अंतिम मैच में एक अप्रत्याशित चैंपियन का उदय हुआ, प्रशंसकों और विश्लेषकों को आश्चर्यचकित किया",
"after-two-decades-of-dominance-the-legendary-player-bids-farewell-in-an-emotional-press": "दो दशकों के प्रभुत्व के बाद, दिग्गज खिलाड़ी एक भावुक प्रेस में विदाई लेता है",
"ai-breakthroughs-surge-as-leading-tech-firms-launch-advanced-smart-assistants": "प्रमुख तकनीकी फर्मों द्वारा उन्नत स्मार्ट सहायकों के लॉन्च के रूप में AI सफलताओं में वृद्धि",
"ai-evolution-speeds-up-as-industry-giants-showcase-future-ready-assistants": "उद्योग के दिग्गजों द्वारा भविष्य के लिए तैयार सहायकों का प्रदर्शन किए जाने पर AI विकास में तेजी",
"ai-momentum-grows-as-tech-heavyweights-present-revolutionary-smart-assistants": "तकनीकी दिग्गजों द्वारा क्रांतिकारी स्मार्ट सहायक प्रस्तुत किए जाने पर AI गति बढ़ती है",
"ai-revolution-accelerates-as-tech-giants-unveil-next-gen-intelligent-assistants-2": "तकनीकी दिग्गजों द्वारा अगली पीढ़ी के बुद्धिमान सहायकों का अनावरण किए जाने पर AI क्रांति में तेजी",
"ai-revolution-accelerates-as-tech-giants-unveil-next-gen-intelligent-assistants": "तकनीकी दिग्गजों द्वारा अगली पीढ़ी के बुद्धिमान सहायकों का अनावरण किए जाने पर AI क्रांति में तेजी",
"an-opinion-piece-on-how-authentic-reporting-and-human-ethics-remain-irreplaceable-even": "प्रामाणिक रिपोर्टिंग और मानव नैतिकता कैसे अप्रतिस्थापनीय बनी हुई है इस पर एक राय लेख",
"artificial-intelligence-tools-are-transforming-how-teams-collaborate-automating-tasks-workplace-efficiency": "कृत्रिम बुद्धिमत्ता उपकरण इस तरह से टीमों के सहयोग करने के तरीके को बदल रहे हैं, कार्यों को स्वचालित करना कार्यस्थल दक्षता",
"breakthrough-in-renewable-energy-storage-could-transform-global-power-supply-2": "नवीकरणीय ऊर्जा भंडारण में सफलता वैश्विक बिजली आपूर्ति को बदल सकती है",
"breakthrough-in-renewable-energy-storage-could-transform-global-power-supply": "नवीकरणीय ऊर्जा भंडारण में सफलता वैश्विक बिजली आपूर्ति को बदल सकती है",
"central-banks-signal-policy-shift-amid-inflation-cooldown": "मुद्रास्फीति शीतलन के बीच केंद्रीय बैंकों ने नीति में बदलाव का संकेत दिया",
"chatbots-redefine-online-learning-as-students-embrace-virtual-tutors": "छात्रों द्वारा आभासी ट्यूटरों को अपनाए जाने पर चैटबॉट ऑनलाइन शिक्षा को पुनः परिभाषित कर रहे हैं",
"cinema-revenues-hit-a-new-post-pandemic-high-fueled-by-blockbuster-releases-and-strong-attendance": "महामारी के बाद सिनेमा राजस्व एक नए उच्च स्तर पर पहुंचा, ब्लॉकबस्टर रिलीज और मजबूत उपस्थिति से ईंधन",
"crude-oil-prices-climbed-to-new-yearly-highs-amid-renewed-geopolitical": "नवीकृत भू-राजनीतिक अस्थिरता के बीच कच्चे तेल की कीमतें नई वार्षिक ऊंचाई पर चढ़ीं",
"demand-for-mental-health-support-tools-continues-to-rise-as-people-seek": "मानसिक स्वास्थ्य सहायता उपकरणों की मांग बढ़ती जा रही है क्योंकि लोग मांग कर रहे हैं",
"emerging-asian-economies-are-outperforming-forecasts-driving-global-gdp-growth-upward": "उभरती एशियाई अर्थव्यवस्थाएं पूर्वानुमानों से बेहतर प्रदर्शन कर रही हैं, वैश्विक जीडीपी वृद्धि को बढ़ावा दे रही हैं",
"global-leaders-commit-to-ambitious-climate-goals-at-geneva-summit": "विश्व नेताओं ने जिनेवा शिखर सम्मेलन में महत्वाकांक्षी जलवायु लक्ष्यों के लिए प्रतिबद्धता जताई",
"global-markets-react-positively-to-trade-agreement-between-asia-and-europe": "एशिया और यूरोप के बीच व्यापार समझौते पर वैश्विक बाजारों ने सकारात्मक प्रतिक्रिया दी",
"innovation-booms-in-ai-as-top-tech-brands-debut-their-latest-intelligent-systems": "शीर्ष तकनीकी ब्रांडों द्वारा अपने नवीनतम बुद्धिमान प्रणालियों की शुरुआत किए जाने पर AI में नवाचार तेजी से बढ़ रहा है",
"major-cities-adopt-ai-traffic-systems-to-combat-congestion-and-pollution": "भीड़भाड़ और प्रदूषण से लड़ने के लिए प्रमुख शहरों ने AI ट्रैफिक सिस्टम अपनाए",
"major-streaming-giants-are-in-fierce-competition-to-secure-exclusive-deals-with-top-creators": "शीर्ष रचनाकारों के साथ विशेष सौदे सुरक्षित करने में प्रमुख स्ट्रीमिंग दिग्गजों के बीच कड़ी प्रतिस्पर्धा",
"markets-responded-positively-to-the-european-central-banks-signal": "बाजारों ने यूरोपीय केंद्रीय बैंक के संकेत पर सकारात्मक प्रतिक्रिया दी",
"more-people-are-embracing-minimalist-lifestyles-focusing-on-possessions": "अधिक लोग न्यूनतम जीवनशैली अपना रहे हैं, संपत्तियों पर ध्यान केंद्रित कर रहे हैं",
"next-gen-ai-takes-center-stage-as-major-tech-companies-reveal-intelligent-tools": "प्रमुख तकनीकी कंपनियों द्वारा बुद्धिमान उपकरण प्रकट किए जाने पर अगली पीढ़ी का AI केंद्र स्तर पर",
"plant-based-products-are-taking-over-restaurant-menus-and-grocery": "पौधे-आधारित उत्पाद रेस्तरां मेनू और किराने की दुकानों पर कब्जा कर रहे हैं",
"recent-satellite-data-shows-the-arctic-ice-melting-faster-than-expected": "हालिया उपग्रह डेटा दिखाता है कि आर्कटिक बर्फ अपेक्षा से तेजी से पिघल रही है",
"researchers-have-corrected-genetic-mutations-in-human-cells": "शोधकर्ताओं ने मानव कोशिकाओं में आनुवंशिक उत्परिवर्तन को सही कर लिया है",
"rising-energy-costs-threaten-small-business-recovery": "बढ़ती ऊर्जा लागत छोटे व्यवसाय की रिकवरी को खतरे में डाल रही है",
"scientists-develop-a-next-gen-vaccine-that-could-target-multiple": "वैज्ञानिकों ने एक अगली पीढ़ी का टीका विकसित किया है जो कई को लक्षित कर सकता है",
"stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown-2": "मुद्रास्फीति शीतलन के बाद निवेशकों का विश्वास बहाल होने पर शेयर बाजारों में उछाल",
"stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown-3": "मुद्रास्फीति शीतलन के बाद निवेशकों का विश्वास बहाल होने पर शेयर बाजारों में उछाल",
"stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown": "मुद्रास्फीति शीतलन के बाद निवेशकों का विश्वास बहाल होने पर शेयर बाजारों में उछाल",
"streaming-platforms-compete-for-viewers-as-subscriptions-hit-record-highs-2": "दर्शकों के लिए स्ट्रीमिंग प्लेटफॉर्म प्रतिस्पर्धा कर रहे हैं क्योंकि सदस्यता रिकॉर्ड उच्च स्तर पर पहुंची",
"streaming-platforms-compete-for-viewers-as-subscriptions-hit-record-highs": "दर्शकों के लिए स्ट्रीमिंग प्लेटफॉर्म प्रतिस्पर्धा कर रहे हैं क्योंकि सदस्यता रिकॉर्ड उच्च स्तर पर पहुंची",
"tech-titans-drive-ai-forward-with-cutting-edge-intelligent-assistant-releases": "तकनीकी दिग्गज अत्याधुनिक बुद्धिमान सहायक रिलीज के साथ AI को आगे बढ़ा रहे हैं",
"the-dollars-slight-decline-has-boosted-emerging-market-currencies": "डॉलर में मामूली गिरावट ने उभरते बाजार मुद्राओं को बढ़ावा दिया है",
"the-gaming-industry-continues-to-boom-as-esports-leagues-attract-massive-corporate-sponsors": "ईस्पोर्ट्स लीगों द्वारा बड़े कॉर्पोरेट प्रायोजकों को आकर्षित किए जाने पर गेमिंग उद्योग फल-फूल रहा है",
"understanding-why-people-crave-constant-updates-and-how-it-affects-mental-health": "लोग लगातार अपडेट क्यों चाहते हैं और यह मानसिक स्वास्थ्य को कैसे प्रभावित करता है इसे समझना",
"wellness-retreats-are-becoming-the-go-to-vacation-choice-blending": "वेलनेस रिट्रीट छुट्टी की पसंदीदा पसंद बन रहे हैं, मिश्रण",
"young-professionals-are-moving-away-from-crowded-cities-to-embrace": "युवा पेशेवर भीड़भाड़ वाले शहरों से दूर जा रहे हैं, अपनाने के लिए"
}

# ---------- Additional category names (homepage pills / article badges) ----------
add("cat.business", "Business", "व्यवसाय")
add("cat.environment", "Environment", "पर्यावरण")
add("cat.scienceEnvironment", "Science & Environment", "विज्ञान एवं पर्यावरण")
add("cat.lifestyle", "Lifestyle", "जीवनशैली")
add("cat.globalNews", "Global News", "विश्व समाचार")
add("cat.otherNews", "Other news", "अन्य ख़बरें")

# Article titles per slug (use real sentence-case titles from the HTML)
import json as _json, os as _os
_realtitles_path = "/tmp/articles.json"
if _os.path.exists(_realtitles_path):
    _real_arts = _json.load(open(_realtitles_path, encoding="utf-8"))
    for _slug, _a in _real_arts.items():
        if _slug in TITLES_HI:
            add("art.title." + _slug, _a["title"], TITLES_HI[_slug])

for slug, hi in TITLES_HI.items():
    if "art.title." + slug not in TR:
        add("art.title." + slug, slug.replace("-", " ").title(), hi)

# Article category mapping per slug
CAT_HI = {
"70-nations-gathered-this-weekend-in-geneva-to-finalize-agreement-at-reducing-global-carbon-emissions": "Global News",
"a-deep-dive-into-the-evolution-of-digital-journalism-and-algorithm-driven-content-feeds": "Other news",
"a-thrilling-final-match-saw-an-unexpected-champion-rise-stunning-fans-and-analysts-alike": "Sports and Entertainment",
"after-two-decades-of-dominance-the-legendary-player-bids-farewell-in-an-emotional-press": "Sports and Entertainment",
"ai-breakthroughs-surge-as-leading-tech-firms-launch-advanced-smart-assistants": "Technology",
"ai-evolution-speeds-up-as-industry-giants-showcase-future-ready-assistants": "Technology",
"ai-momentum-grows-as-tech-heavyweights-present-revolutionary-smart-assistants": "Technology",
"ai-revolution-accelerates-as-tech-giants-unveil-next-gen-intelligent-assistants-2": "Technology",
"ai-revolution-accelerates-as-tech-giants-unveil-next-gen-intelligent-assistants": "Technology",
"an-opinion-piece-on-how-authentic-reporting-and-human-ethics-remain-irreplaceable-even": "Other news",
"artificial-intelligence-tools-are-transforming-how-teams-collaborate-automating-tasks-workplace-efficiency": "Technology",
"breakthrough-in-renewable-energy-storage-could-transform-global-power-supply-2": "Global Stories",
"breakthrough-in-renewable-energy-storage-could-transform-global-power-supply": "Global Stories",
"central-banks-signal-policy-shift-amid-inflation-cooldown": "Economy",
"chatbots-redefine-online-learning-as-students-embrace-virtual-tutors": "Other news",
"cinema-revenues-hit-a-new-post-pandemic-high-fueled-by-blockbuster-releases-and-strong-attendance": "Entertainment",
"crude-oil-prices-climbed-to-new-yearly-highs-amid-renewed-geopolitical": "Economy",
"demand-for-mental-health-support-tools-continues-to-rise-as-people-seek": "Other news",
"emerging-asian-economies-are-outperforming-forecasts-driving-global-gdp-growth-upward": "Economy",
"global-leaders-commit-to-ambitious-climate-goals-at-geneva-summit": "Global News",
"global-markets-react-positively-to-trade-agreement-between-asia-and-europe": "Global Markets",
"innovation-booms-in-ai-as-top-tech-brands-debut-their-latest-intelligent-systems": "Technology",
"major-cities-adopt-ai-traffic-systems-to-combat-congestion-and-pollution": "Technology",
"major-streaming-giants-are-in-fierce-competition-to-secure-exclusive-deals-with-top-creators": "Entertainment",
"markets-responded-positively-to-the-european-central-banks-signal": "Economy",
"more-people-are-embracing-minimalist-lifestyles-focusing-on-possessions": "Lifestyle & Culture",
"next-gen-ai-takes-center-stage-as-major-tech-companies-reveal-intelligent-tools": "Technology",
"plant-based-products-are-taking-over-restaurant-menus-and-grocery": "Lifestyle & Culture",
"recent-satellite-data-shows-the-arctic-ice-melting-faster-than-expected": "Science & Health",
"researchers-have-corrected-genetic-mutations-in-human-cells": "Science & Health",
"rising-energy-costs-threaten-small-business-recovery": "Economy",
"scientists-develop-a-next-gen-vaccine-that-could-target-multiple": "Science & Health",
"stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown-2": "Economy",
"stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown-3": "Economy",
"stock-markets-surge-as-investors-regain-confidence-after-inflation-cooldown": "Economy",
"streaming-platforms-compete-for-viewers-as-subscriptions-hit-record-highs-2": "Entertainment",
"streaming-platforms-compete-for-viewers-as-subscriptions-hit-record-highs": "Entertainment",
"tech-titans-drive-ai-forward-with-cutting-edge-intelligent-assistant-releases": "Technology",
"the-dollars-slight-decline-has-boosted-emerging-market-currencies": "Economy",
"the-gaming-industry-continues-to-boom-as-esports-leagues-attract-massive-corporate-sponsors": "Sports and Entertainment",
"understanding-why-people-crave-constant-updates-and-how-it-affects-mental-health": "Other news",
"wellness-retreats-are-becoming-the-go-to-vacation-choice-blending": "Lifestyle & Culture",
"young-professionals-are-moving-away-from-crowded-cities-to-embrace": "Lifestyle & Culture",
}

# ---------- Other page-specific visible text ----------
# key -> (en, hi)
PAGE = {
"index.title": ("News Today - Daily Breaking News, Stories & Headlines", "हिन्दी में ब्रेकिंग न्यूज़, कहानियाँ और शीर्षक - News Today"),
"index.desc": ("News Today is a modern newspaper and media outlet based in Bhikhanpur, Bhagalpur, Bihar. Deliver breaking news, in-depth stories, and engaging journalism with a fast, responsive layout.", "News Today भिक्खनपुर, भागलपुर, बिहार में स्थित एक आधुनिक समाचार पत्र और मीडिया आउटलेट है। तेज़, रिस्पॉन्सिव लेआउट के साथ ब्रेकिंग न्यूज़, गहरी कहानियाँ और आकर्षक पत्रकारिता प्रदान करता है।"),
"top.label1": ("ब्रेकिंग न्यूज़: बाज़ारों में नई आर्थिक नीतियों का असर", "ब्रेकिंग न्यूज़: बाज़ारों में नई आर्थिक नीतियों का असर"),
"top.label2": ("चुनाव 2025: शुरुआती रुझानों में चौंकाने वाले नतीजे", "चुनाव 2025: शुरुआती रुझानों में चौंकाने वाले नतीजे"),
"top.label3": ("तकनीक: दिग्गज टेक कंपनी ने पेश किया अगली पीढ़ी का एआई चिप", "तकनीक: दिग्गज टेक कंपनी ने पेश किया अगली पीढ़ी का एआई चिप"),
"top.label4": ("शिक्षा: नई राष्ट्रीय शिक्षा नीति में बड़े सुधारों की घोषणा", "शिक्षा: नई राष्ट्रीय शिक्षा नीति में बड़े सुधारों की घोषणा"),
"404.title": ("Not Found | News Today - Leading News & Media", "मिली नहीं | News Today - अग्रणी समाचार और मीडिया"),
"404.heading": ("Oops! Page Not Found", "ओहॉ! पेज नहीं मिला"),
"404.desc": ("Looks like the news took a different route. The page you’re trying to access might have been moved, deleted, or temporarily unavailable.", "देखने में आ रहा है कि खबर ने कोई अलग रास्ता ले लिया है। जिस पेज तक आप पहुंचने की कोशिश कर रहे हैं, वह हटाया जा सकता है, हटाया जा सकता है, या अस्थायी रूप से अनुपलब्ध हो सकता है।"),
"404.home": ("Return to Homepage", "होमपेज पर लौटें"),
"about.title": ("About | News Today - Leading News & Media", "हमारे बारे में | News Today - अग्रणी समाचार और मीडिया"),
"about.heading": ("Our Team", "हमारी टीम"),
"authors.title": ("Authors | News Today - Leading News & Media", "लेखक | News Today - अग्रणी समाचार और मीडिया"),
"authors.heading": ("Meet the Authors", "लेखकों से मिलें"),
"changelog.title": ("Changelog | News Today - Leading News & Media", "चेंजलॉग | News Today - अग्रणी समाचार और मीडिया"),
"changelog.heading": ("Changelog", "चेंजलॉग"),
"checkout.title": ("Checkout | News Today - Leading News & Media", "चेकआउट | News Today - अग्रणी समाचार और मीडिया"),
"contact.title": ("Contact Us | News Today - Leading News & Media", "संपर्क करें | News Today - अग्रणी समाचार और मीडिया"),
"contact.heading": ("We’re Here to Listen", "हम यहां सुनने के लिए हैं"),
"contact.call": ("Give us a call", "हमें कॉल करें"),
"contact.email": ("Send us an email", "हमें एक ईमेल भेजें"),
"contact.visit": ("Visit us in person", "हमसे व्यक्तिगत रूप से मिलें"),
"contact.form": ("Contact Form", "संपर्क फॉर्म"),
"contact.respond": ("We aim to respond to all messages within 24–48 hours.", "हम 24-48 घंटों के भीतर सभी संदेशों का जवाब देने का लक्ष्य रखते हैं।"),
"contact.agree": ("By reaching out to us, you agree to our", "हमसे संपर्क करके, आप हमारी सहमति देते हैं"),
"license.title": ("License | News Today - Leading News & Media", "लाइसेंस | News Today - अग्रणी समाचार और मीडिया"),
"shop.title": ("Shop | News Today - Leading News & Media", "दुकान | News Today - अग्रणी समाचार और मीडिया"),
"shop.heading": ("Shop with us", "हमारे साथ खरीदारी करें"),
"styleguide.title": ("Styleguide | News Today - Leading News & Media", "स्टाइलगाइड | News Today - अग्रणी समाचार और मीडिया"),
"styleguide.heading": ("Styleguide", "स्टाइलगाइड"),
"subscription.title": ("Subscription | News Today - Leading News & Media", "सदस्यता | News Today - अग्रणी समाचार और मीडिया"),
"subscription.heading": ("Our subscription plans", "हमारी सदस्यता योजनाएं"),
"terms.title": ("Terms & Conditions | News Today - Leading News & Media", "नियम एवं शर्तें | News Today - अग्रणी समाचार और मीडिया"),
"form.required": ("* Required", "* अनिवार्य"),
"form.fullName": ("Full Name *", "पूर्ण नाम *"),
"form.street": ("Street Address *", "गली का पता *"),
"form.city": ("City *", "शहर *"),
"form.state": ("State/Province", "राज्य/प्रांत"),
"form.zip": ("Zip/Postal Code *", "ज़िप/डाक कोड *"),
"form.country": ("Country *", "देश *"),
"nav.india": ("India", "भारत"),
}

for k,(en,hi) in PAGE.items():
    add(k, en, hi)

# ---------- About / Contact specific ----------
add("editor.owner", "Editor-in-Chief & Owner", "संपादक-प्रमुख एवं स्वामी")
add("contact.formHeading", "Contact Form", "संपर्क फॉर्म")
add("contact.respondTime", "We aim to respond to all messages within 24–48 hours.", "हम 24-48 घंटों के भीतर सभी संदेशों का जवाब देने का लक्ष्य रखते हैं।")
add("contact.joinCommunity", "Join our growing community — where stories inform, inspire, and connect.", "हमारे बढ़ते समुदाय से जुड़ें — जहां कहानियां सूचित, प्रेरित और जोड़ती हैं।")
add("contact.addressLine", "Bhikhanpur, Bhagalpur, Bihar, India", "भीखनपुर, भागलपुर, बिहार, भारत")

# ---------- Homepage hero & category pills ----------
add("home.metaTitle", "News Today | Bhagalpur Latest News", "News Today | भागलपुर ताज़ा ख़बरें")
add("home.heroDesc", "World leaders gathered in Geneva to discuss urgent actions for global warming, pledging new commitments to renewable energy and emission reduction by 2030.", "विश्व नेताओं ने जिनेवा में वैश्विक तापन के लिए तत्काल कार्रवाई पर चर्चा की, नवीकरणीय ऊर्जा और 2030 तक उत्सर्जन कम करने के नए प्रतिबद्धता जताई।")
add("home.aiTech", "AI TECH", "एआई टेक")
add("home.followUs", "Follow us for", "हमारे साथ जुड़ें")
add("home.realTimeUpdates", "real-time updates", "रियल-टाइम अपडेट")
add("home.breakingStories", "and breaking stories from around the world.", "और दुनिया भर की ब्रेकिंग खबरें।")
add("home.readFullStory", "Read full story", "पूरी खबर पढ़ें")
add("home.allFrom", "All from", "सभी से")
add("home.getUpdates", "Get updates on the go — connect with us across your favorite social networks.", "चलते-फिरते अपडेट पाएं — अपने पसंदीदा सोशल नेटवर्क पर हमसे जुड़ें।")
add("home.keepUp", "Keep up with the latest news — be part of our audience on social media.", "ताज़ा खबरों से अपडेट रहें — सोशल मीडिया पर हमारे दर्शकों का हिस्सा बनें।")
add("home.stayInformed", "Stay informed wherever you are — join our community of readers and followers across social platforms.", "जहां भी हों, सूचित रहें — सोशल प्लेटफॉर्म पर हमारे पाठकों और फॉलोअर्स के समुदाय से जुड़ें।")
add("cat.health", "Health", "स्वास्थ्य")
add("cat.wellness", "Wellness", "वेलनेस")
add("cat.climateChange", "Climate Change", "जलवायु परिवर्तन")
add("cat.astronomy", "Astronomy", "खगोल विज्ञान")
add("cat.sports", "Sports", "खेल")
add("cat.movies", "Movies", "फिल्में")
add("cat.tennis", "Tennis", "टेनिस")
add("cat.esports", "Esports", "ईस्पोर्ट्स")
add("cat.streaming", "Streaming", "स्ट्रीमिंग")
add("cat.lifestyle", "Lifestyle", "जीवनशैली")
add("cat.food", "Food", "भोजन")
add("cat.travel", "Travel", "यात्रा")
add("cat.remoteWork", "Remote Work", "रिमोट वर्क")

# ---------- FAQ ----------
add("faq.q1", "What is The Daily Placeholder?", "The Daily Placeholder क्या है?")
add("faq.a1", "Quas vel perferendis accusantium eum cum voluptates libero doloribus voluptates. A et quia qui quia. Sunt tempore est sit facilis. Ducimus est ut neque sunt eum iusto. Consequatur quia occaecati enim omnis repudiandae labore.", "यह एक प्लेसहोल्डर उत्तर है।")
add("faq.q2", "Can I contribute or submit an article?", "क्या मैं लेख योगदान या सबमिट कर सकता हूं?")
add("faq.a2", "Aut dicta iusto neque ea voluptates. Id cupiditate cum sequi eum neque dolorem dicta quisquam non.", "हां, आप हमें संपर्क पेज के माध्यम से लेख सबमिट कर सकते हैं।")
add("faq.q3", "How can I subscribe to your newsletter?", "मैं आपके न्यूज़लेटर की सदस्यता कैसे ले सकता हूं?")
add("faq.a3", "You can subscribe using the email subscription form in the footer.", "आप फुटर में ईमेल सब्सक्रिप्शन फॉर्म का उपयोग करके सदस्यता ले सकते हैं।")
add("faq.q4", "How do you ensure the accuracy of your news?", "आप अपनी खबरों की सटीकता कैसे सुनिश्चित करते हैं?")
add("faq.a4", "Our editorial team verifies all facts before publishing.", "हमारी संपादकीय टीम प्रकाशित करने से पहले सभी तथ्यों का सत्यापन करती है।")
add("faq.q5", "Is The Daily Placeholder affiliated?", "क्या The Daily Placeholder संबद्ध है?")
add("faq.a5", "It is an independent news platform.", "यह एक स्वतंत्र समाचार मंच है।")
add("faq.q6", "How often is the website updated?", "वेबसाइट कितनी बार अपडेट होती है?")
add("faq.a6", "The website is updated multiple times daily with breaking news.", "वेबसाइट ब्रेकिंग न्यूज़ के साथ दिन में कई बार अपडेट होती है।")

# ---------- Footer link fix (Hindi text already present; ensure translatable) ----------
add("footer.subscriptionLink", "Subscription Plans", "सदस्यता योजनाएं")

# ---------- Exact-match remaining UI strings ----------
add("form.name", "Name*", "नाम*")
add("form.email", "Email*", "ईमेल*")
add("form.phone", "Phone*", "फोन*")
add("form.message", "Message*", "संदेश*")
add("contact.privacyLink", "Privacy Policy.", "गोपनीयता नीति।")
add("author.editor", "Editor-in-Chief", "संपादक-प्रमुख")
add("cat.sportsEnt", "Sports and Entertainment", "खेल और मनोरंजन")
add("cat.economyGlobal", "Economy / Global Markets", "अर्थव्यवस्था / वैश्विक बाजार")
# FAQ answers (placeholder content)
add("faq.a1", "Quas vel perferendis accusantium eum cum voluptates libero doloribus voluptates. A et quia qui quia. Sunt tempore est sit facilis. Ducimus est ut neque sunt eum iusto. Consequatur quia occaecati enim omnis repudiandae labore.", "यह एक प्लेसहोल्डर उत्तर है।")
add("faq.a2", "Aut dicta iusto neque ea voluptates. Id cupiditate cum sequi eum neque dolorem dicta quisquam non.", "हां, आप हमें संपर्क पेज के माध्यम से लेख सबमिट कर सकते हैं।")

json.dump(TR, open("trans_dict.json","w"), ensure_ascii=False, indent=1)
print(f"Total translation keys: {len(TR)}")
print("Saved trans_dict.json")
