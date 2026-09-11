from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = '<div class="rsvp-question">هل ستحضر؟</div>\n'
if old not in text:
    raise SystemExit('RSVP question not found')
text = text.replace(old, '', 1)
path.write_text(text, encoding='utf-8')
