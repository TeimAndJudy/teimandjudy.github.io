from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

if 'class="venue-card"' in text:
    raise SystemExit('Venue card already exists')

venue_html = '''
<section class="venue-card" lang="ar" dir="rtl" aria-labelledby="venue-title">
    <h2 id="venue-title">مكان الدعوة</h2>
    <p class="venue-name" lang="en" dir="ltr">Quattro Hotel Aleppo</p>
    <div class="venue-map-frame">
        <iframe
            title="Quattro Hotel Aleppo map"
            src="https://www.google.com/maps?q=Quattro%20Hotel%20Aleppo&output=embed"
            loading="lazy"
            allowfullscreen
            referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <a class="venue-map-link"
       href="https://www.google.com/maps/search/?api=1&query=Quattro+Hotel+Aleppo"
       target="_blank"
       rel="noopener noreferrer">الاتجاهات <span aria-hidden="true">↗</span></a>
</section>

'''

marker = '<section class="rsvp-card"'
if marker not in text:
    raise SystemExit('RSVP card marker not found')
text = text.replace(marker, venue_html + marker, 1)

venue_css = r'''

/* Venue card with embedded Google map, placed above RSVP. */
#invitation .venue-card{
    width:100%;
    max-width:680px;
    margin:0 auto 48px;
    padding:46px 24px 42px;
    border-radius:24px;
    background:linear-gradient(145deg,#64191d,#741f24);
    color:#fff8ed;
    box-shadow:0 18px 36px rgba(83,23,27,.14);
    font-family:'Noto Naskh Arabic',serif;
    text-align:center;
}
#invitation .venue-card h2{
    margin:0 0 8px;
    font-size:clamp(2rem,7vw,3rem);
    line-height:1.45;
    font-weight:700;
}
#invitation .venue-name{
    direction:ltr;
    margin:0 auto 24px;
    color:#f2d9cd;
    font-family:'Cormorant Garamond',serif;
    font-size:clamp(1.35rem,5vw,1.85rem);
    line-height:1.5;
    letter-spacing:.02em;
}
#invitation .venue-map-frame{
    width:100%;
    max-width:540px;
    margin:0 auto 22px;
    border-radius:22px;
    overflow:hidden;
    border:2px solid rgba(255,248,237,.65);
    background:#f4eadf;
    box-shadow:0 12px 28px rgba(35,0,0,.22);
}
#invitation .venue-map-frame iframe{
    display:block;
    width:100%;
    height:330px;
    border:0;
}
#invitation .venue-map-link{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:9px;
    min-width:180px;
    min-height:56px;
    padding:10px 24px;
    border-radius:18px;
    background:#f1ddd2;
    color:#681b20;
    text-decoration:none;
    font-size:clamp(1.15rem,4.6vw,1.45rem);
    font-weight:700;
    box-shadow:0 8px 18px rgba(45,0,0,.16);
    transition:transform .22s ease,opacity .22s ease;
}
#invitation .venue-map-link:hover{transform:translateY(-2px);opacity:.97;}
#invitation .venue-map-link:focus-visible{outline:2px solid #fff8ed;outline-offset:4px;}
@media(max-width:600px){
    #invitation .venue-card{padding:38px 16px 34px;}
    #invitation .venue-map-frame iframe{height:285px;}
}
'''

style_marker = '</style>'
if style_marker not in text:
    raise SystemExit('Style closing tag not found')
text = text.replace(style_marker, venue_css + '\n' + style_marker, 1)

path.write_text(text, encoding='utf-8')
