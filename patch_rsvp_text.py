from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = 'حضوركم شرف عظيم لنا، نرجو تأكيد الحضور حتى نتمكن من إعداد أجمل استقبال لكم.'
new = 'يسرّنا حضوركم، ونرجو تأكيد الحضور أو الاعتذار قبل 20/9.'
if old not in text:
    raise SystemExit('Expected RSVP intro text not found')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
