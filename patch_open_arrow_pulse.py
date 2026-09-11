from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

marker = '/* Perfectly centered pulsing cover arrow. */'
styles = r'''

/* Perfectly centered pulsing cover arrow. */
.open-btn{
    position:relative;
    overflow:visible;
}
.open-btn .arrow{
    position:absolute;
    left:50%;
    top:50%;
    margin:0;
    line-height:1;
    transform:translate(-50%,-50%);
    transform-origin:center;
    animation:coverArrowPulse 1.7s ease-in-out infinite;
    will-change:transform,opacity;
}
@keyframes coverArrowPulse{
    0%,100%{transform:translate(-50%,-50%) scale(1);opacity:.92;}
    50%{transform:translate(-50%,-50%) scale(1.18);opacity:1;}
}
@media(prefers-reduced-motion:reduce){
    .open-btn .arrow{animation:none;}
}
'''

if marker not in text:
    if '</style>' not in text:
        raise SystemExit('style tag not found')
    text = text.replace('</style>', styles + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
