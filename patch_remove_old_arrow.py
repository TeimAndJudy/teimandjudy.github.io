from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = '<span class="arrow" aria-hidden="true">→</span>'
new = '<span class="arrow" aria-hidden="true"></span>'
if old not in text:
    raise SystemExit('old arrow glyph not found')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
