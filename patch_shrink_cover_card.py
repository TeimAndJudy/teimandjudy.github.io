from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

start = '/* SMALLER COVER CARD START */'
end = '/* SMALLER COVER CARD END */'
text = re.sub(re.escape(start) + r'.*?' + re.escape(end), '', text, flags=re.S)

css = r'''
/* SMALLER COVER CARD START */
/* Only reduce the cream cover card itself. Keep all text/button sizes unchanged. */
#cover .card{
    width:min(620px,88vw) !important;
    min-height:790px !important;
    padding-top:44px !important;
    padding-bottom:40px !important;
}

@media(max-width:600px){
    #cover .card{
        width:88vw !important;
        min-height:700px !important;
        padding-left:18px !important;
        padding-right:18px !important;
    }
}
/* SMALLER COVER CARD END */
'''

if '</style>' not in text:
    raise SystemExit('Closing style tag not found')
text = text.replace('</style>', css + '\n</style>', 1)
path.write_text(text, encoding='utf-8')
print('Reduced only the cream cover card size')
