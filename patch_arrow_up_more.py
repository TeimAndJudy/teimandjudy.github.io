from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

styles = r'''

/* Raise cover arrow a little more. */
.open-btn .arrow{
    top:calc(50% - 10px);
}
'''

if '/* Raise cover arrow a little more. */' not in text:
    text = text.replace('</style>', styles + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
