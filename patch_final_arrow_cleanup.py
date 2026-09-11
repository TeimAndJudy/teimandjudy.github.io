from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Normalize the button content to exactly one text arrow.
text, n = re.subn(r'(<button class="open-btn"[^>]*>\s*)<span class="arrow" aria-hidden="true">.*?</span>', r'\1<span class="arrow" aria-hidden="true">→</span>', text, count=1, flags=re.S)
if n != 1:
    raise SystemExit('open button arrow span not found')

styles = r'''

/* FINAL cover arrow cleanup: one normal arrow, centered; only the button pulses. */
.open-btn{
    position:relative!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    width:125px!important;
    min-height:70px!important;
    padding:0!important;
    border-radius:40px!important;
    overflow:visible!important;
    transform-origin:center!important;
    animation:finalCoverButtonPulse 1.7s ease-in-out infinite!important;
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
    font-size:42px!important;
    font-weight:300!important;
    line-height:1!important;
    letter-spacing:0!important;
    color:#fff8ef!important;
    transform:translate(-50%,-54%)!important;
    animation:none!important;
}
.open-btn .arrow::before,
.open-btn .arrow::after{
    content:none!important;
    display:none!important;
}
@keyframes finalCoverButtonPulse{
    0%,100%{transform:scale(1);box-shadow:0 10px 25px rgba(75,0,0,.28);}
    50%{transform:scale(1.09);box-shadow:0 15px 34px rgba(75,0,0,.38);}
}
@media(max-width:600px){
    .open-btn{width:112px!important;min-height:64px!important;}
    .open-btn .arrow{font-size:38px!important;}
}
@media(prefers-reduced-motion:reduce){
    .open-btn{animation:none!important;}
}
'''

marker = '/* FINAL cover arrow cleanup: one normal arrow, centered; only the button pulses. */'
if marker not in text:
    text = text.replace('</style>', styles + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
