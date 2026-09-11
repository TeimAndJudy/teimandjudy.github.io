from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

start = '/* SLIGHTLY SMALLER INVITATION CARDS START */'
end = '/* SLIGHTLY SMALLER INVITATION CARDS END */'
text = re.sub(re.escape(start) + r'.*?' + re.escape(end), '', text, flags=re.S)

css = r'''
/* SLIGHTLY SMALLER INVITATION CARDS START */
#invitation .love-card,
#invitation .reception-card,
#invitation .venue-card,
#invitation .rsvp-card{
    width:min(88%,595px) !important;
    max-width:595px !important;
}

#invitation .love-card,
#invitation .reception-card,
#invitation .venue-card{
    padding-left:20px !important;
    padding-right:20px !important;
}

@media(max-width:600px){
    #invitation .love-card,
    #invitation .reception-card,
    #invitation .venue-card,
    #invitation .rsvp-card{
        width:87vw !important;
    }
}
/* SLIGHTLY SMALLER INVITATION CARDS END */
'''

if '</style>' not in text:
    raise SystemExit('Closing style tag not found')
text = text.replace('</style>', css + '\n</style>', 1)
path.write_text(text, encoding='utf-8')
print('Slightly reduced all invitation card sizes')
