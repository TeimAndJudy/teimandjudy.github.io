from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Use a visually balanced arrow glyph.
text = text.replace('<span class="arrow" aria-hidden="true">⟶</span>', '<span class="arrow" aria-hidden="true">→</span>', 1)

styles = r'''

/* Pulse the whole open button; keep the arrow perfectly centered and still. */
.open-btn{
    position:relative;
    overflow:visible;
    display:flex;
    align-items:center;
    justify-content:center;
    transform-origin:center;
    animation:coverButtonPulse 1.7s ease-in-out infinite;
    will-change:transform,box-shadow;
}
.open-btn .arrow{
    position:absolute!important;
    left:50%!important;
    top:50%!important;
    width:auto!important;
    height:auto!important;
    margin:0!important;
    padding:0!important;
    display:block!important;
    font-family:Arial,'Helvetica Neue',sans-serif!important;
    font-size:44px!important;
    font-weight:300!important;
    line-height:1!important;
    letter-spacing:0!important;
    transform:translate(-50%,-50%)!important;
    animation:none!important;
    will-change:auto!important;
}
@keyframes coverButtonPulse{
    0%,100%{
        transform:scale(1);
        box-shadow:0 10px 25px rgba(75,0,0,.28);
    }
    50%{
        transform:scale(1.09);
        box-shadow:0 15px 34px rgba(75,0,0,.38);
    }
}
@media(max-width:600px){
    .open-btn .arrow{font-size:42px!important;}
}
@media(prefers-reduced-motion:reduce){
    .open-btn{animation:none;}
    .open-btn .arrow{animation:none!important;}
}
'''

marker = '/* Pulse the whole open button; keep the arrow perfectly centered and still. */'
if marker not in text:
    if '</style>' not in text:
        raise SystemExit('style tag not found')
    text = text.replace('</style>', styles + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
