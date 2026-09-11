from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = '''#invitation .venue-map-link{\n    display:inline-flex;\n    align-items:center;\n    justify-content:center;\n    gap:9px;\n    min-width:180px;\n    min-height:56px;\n    padding:10px 24px;\n    border-radius:18px;\n    background:#f1ddd2;\n    color:#681b20;\n    text-decoration:none;\n    font-size:clamp(1.15rem,4.6vw,1.45rem);\n    font-weight:700;\n    box-shadow:0 8px 18px rgba(45,0,0,.16);\n    transition:transform .22s ease,opacity .22s ease;\n}\n'''
new = '''#invitation .venue-map-link{\n    display:inline-flex;\n    align-items:center;\n    justify-content:center;\n    gap:9px;\n    padding:6px 4px;\n    background:transparent;\n    color:#fff8ed;\n    text-decoration:none;\n    font-size:clamp(1.15rem,4.6vw,1.45rem);\n    font-weight:700;\n    box-shadow:none;\n    border-radius:0;\n    min-width:0;\n    min-height:0;\n    transition:transform .22s ease,opacity .22s ease;\n}\n'''
if old not in text:
    raise SystemExit('Venue directions style block not found')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
