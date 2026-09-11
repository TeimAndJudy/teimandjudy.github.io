from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

text = text.replace('يسرّنا أن ندعوكم', 'دعوة خاصة إلى', 1)
text = text.replace('''<!-- BOTTOM TEXT -->\n\n<div class="arabic-text">\nلحضور عشاء زفافنا\n</div>\n\n\n\n<!-- OPEN BUTTON -->''', '''<!-- OPEN BUTTON -->''', 1)
text = text.replace('''<button class="open-btn" onclick="openInvitation()">\n\nOPEN\n\n<span class="arrow">\n⟶\n</span>\n\n</button>''', '''<button class="open-btn" onclick="openInvitation()" aria-label="فتح الدعوة">\n<span class="arrow" aria-hidden="true">⟶</span>\n</button>''', 1)

css = '''\n\n/* Personalized cover refinement: private invitation + clear arrow-only button. */\n.guest-box{margin-bottom:32px;}\n.open-btn{\n    width:125px;\n    min-height:70px;\n    padding:0;\n    border-radius:40px;\n    display:flex;\n    align-items:center;\n    justify-content:center;\n    letter-spacing:0;\n}\n.open-btn .arrow{\n    display:block;\n    margin:0;\n    font-family:Georgia,'Times New Roman',serif;\n    font-size:46px;\n    line-height:1;\n    transform:translateY(-2px);\n}\n@media(max-width:600px){\n    .guest-box{margin-bottom:28px;}\n    .open-btn{width:112px;min-height:64px;}\n    .open-btn .arrow{font-size:42px;}\n}\n'''
marker = '</style>\n<link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@700&display=swap" rel="stylesheet">'
if 'Personalized cover refinement:' not in text:
    text = text.replace(marker, css + marker, 1)

path.write_text(text, encoding='utf-8')
