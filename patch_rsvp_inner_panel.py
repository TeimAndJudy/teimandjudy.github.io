from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Wrap the RSVP content in one translucent inner panel.
if 'class="rsvp-inner-panel"' not in text:
    pattern = re.compile(r'(<section class="rsvp-card"[^>]*>)(.*?)(</section>)', re.S)
    match = pattern.search(text)
    if not match:
        raise SystemExit('RSVP section not found')
    replacement = match.group(1) + '\n    <div class="rsvp-inner-panel">' + match.group(2) + '\n    </div>\n' + match.group(3)
    text = text[:match.start()] + replacement + text[match.end():]

start = '/* RSVP INNER GLASS PANEL START */'
end = '/* RSVP INNER GLASS PANEL END */'
text = re.sub(re.escape(start) + r'.*?' + re.escape(end), '', text, flags=re.S)

css = r'''
/* RSVP INNER GLASS PANEL START */
#invitation .rsvp-card{
    background:linear-gradient(150deg,#4a0911 0%,#5b0d17 48%,#6b111b 100%) !important;
    padding:18px !important;
    overflow:visible !important;
}

#invitation .rsvp-inner-panel{
    width:100%;
    padding:30px 18px 28px;
    border-radius:22px;
    background:rgba(218,176,184,.30);
    border:1.5px solid rgba(255,244,236,.42);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.10),0 10px 24px rgba(38,0,7,.10);
    backdrop-filter:blur(8px);
    -webkit-backdrop-filter:blur(8px);
    position:relative;
    z-index:2;
}

#invitation .rsvp-inner-panel h2,
#invitation .rsvp-inner-panel .rsvp-intro,
#invitation .rsvp-inner-panel .rsvp-message{
    color:#fff7ef !important;
}

#invitation .rsvp-inner-panel .rsvp-option{
    background:rgba(255,239,238,.14) !important;
    border-color:rgba(255,248,241,.78) !important;
}

#invitation .rsvp-inner-panel .rsvp-option-text{
    color:#fff5ee !important;
}

@media(max-width:600px){
    #invitation .rsvp-card{padding:14px !important;}
    #invitation .rsvp-inner-panel{padding:28px 14px 25px;border-radius:20px;}
}
/* RSVP INNER GLASS PANEL END */
'''

if '</style>' not in text:
    raise SystemExit('Closing style tag not found')
text = text.replace('</style>', css + '\n</style>', 1)
path.write_text(text, encoding='utf-8')
print('Restored burgundy RSVP card with translucent inner panel')
