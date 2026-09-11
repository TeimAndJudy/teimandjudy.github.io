from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
marker = '/* REMOVE RSVP TOP-RIGHT FLORAL STICKER */'
css = '''\n/* REMOVE RSVP TOP-RIGHT FLORAL STICKER */\n#invitation .rsvp-card::before{\n    display:none !important;\n    content:none !important;\n    background:none !important;\n    border:0 !important;\n    box-shadow:none !important;\n}\n'''
if marker not in text:
    text = text.replace('</style>', css + '\n</style>', 1)
path.write_text(text, encoding='utf-8')
print('Removed RSVP top-right floral sticker')
