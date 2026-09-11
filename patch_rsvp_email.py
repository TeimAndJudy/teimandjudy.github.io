from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
old="am91ZHkubW91aGFmZmVsQGhvdG1haWwuY29t"
new="am91ZHltb3VoYWZmZWxAZ21haWwuY29t"
if old not in s:
    raise SystemExit('Old RSVP email token not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
