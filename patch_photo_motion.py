from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

css = r'''

/* Single-line forever title + livelier romantic photo frame. */
#invitation .forever-title{
    white-space:nowrap;
    font-size:clamp(.95rem,4.35vw,2.35rem);
    letter-spacing:.08em;
    line-height:1.2;
}
#invitation .couple-photo-frame{
    animation:frameFloat 4.2s ease-in-out infinite;
    transform-origin:center;
    will-change:transform,box-shadow;
}
#invitation .couple-photo-frame::before{
    content:"";
    position:absolute;
    inset:-6px;
    border:1px solid rgba(116,31,36,.38);
    border-radius:27px;
    pointer-events:none;
    animation:frameGlow 2.8s ease-in-out infinite;
}
#invitation .photo-heart{
    animation:photoHeartDance 3.2s ease-in-out infinite;
}
#invitation .photo-heart-two{animation-delay:-.8s;}
#invitation .photo-heart-three{animation-delay:-1.5s;}
#invitation .photo-heart-four{animation-delay:-2.2s;}
@keyframes frameFloat{
    0%,100%{transform:translateY(0) rotate(-.2deg) scale(1);box-shadow:0 12px 28px rgba(104,27,32,.13);}
    50%{transform:translateY(-7px) rotate(.35deg) scale(1.008);box-shadow:0 20px 38px rgba(104,27,32,.2);}
}
@keyframes frameGlow{
    0%,100%{opacity:.35;transform:scale(.995);}
    50%{opacity:.9;transform:scale(1.012);}
}
@keyframes photoHeartDance{
    0%,100%{transform:translateY(0) rotate(-7deg) scale(1);}
    50%{transform:translateY(-10px) rotate(9deg) scale(1.18);}
}
@media(max-width:430px){
    #invitation .forever-title{font-size:clamp(.82rem,4.1vw,1.25rem);letter-spacing:.055em;}
}
@media(prefers-reduced-motion:reduce){
    #invitation .couple-photo-frame,
    #invitation .couple-photo-frame::before,
    #invitation .photo-heart{animation:none;}
}
'''

marker = '</style>'
if 'Single-line forever title + livelier romantic photo frame.' not in text:
    if marker not in text:
        raise SystemExit('style closing tag not found')
    text = text.replace(marker, css + '\n' + marker, 1)

path.write_text(text, encoding='utf-8')
