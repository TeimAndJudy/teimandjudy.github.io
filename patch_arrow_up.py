from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

styles = r'''

/* Fine-tune cover arrow vertical alignment. */
.open-btn .arrow{
    top:calc(50% - 5px);
}
'''

if '/* Fine-tune cover arrow vertical alignment. */' not in text:
    text = text.replace('</style>', styles + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
