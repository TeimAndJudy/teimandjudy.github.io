from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='/* RSVP FLOWER ABOVE GLASS FIX */'
css='''\n/* RSVP FLOWER ABOVE GLASS FIX */\n/* Keep the bottom-right floral decoration above the translucent RSVP panel. */\n#invitation .rsvp-card::before{z-index:1 !important;}\n#invitation .rsvp-card > *{position:relative;z-index:2 !important;}\n#invitation .rsvp-card::after{z-index:5 !important;pointer-events:none !important;}\n'''
if marker in s:
    s=s[:s.index(marker)].rstrip()+"\n"
s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s,encoding='utf-8')
