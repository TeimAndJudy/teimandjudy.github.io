from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

figure_marker = '''        <span class="photo-heart photo-heart-three" aria-hidden="true">♡</span>
        <span class="photo-heart photo-heart-four" aria-hidden="true">♥</span>
    </figure>'''
figure_replacement = '''        <span class="photo-heart photo-heart-three" aria-hidden="true">♡</span>
        <span class="photo-heart photo-heart-four" aria-hidden="true">♥</span>
        <span class="frame-flower frame-flower-one" aria-hidden="true">✿</span>
        <span class="frame-flower frame-flower-two" aria-hidden="true">❀</span>
        <span class="frame-flower frame-flower-three" aria-hidden="true">✿</span>
        <span class="frame-flower frame-flower-four" aria-hidden="true">❀</span>
    </figure>'''
if figure_marker not in text:
    raise SystemExit('Photo frame marker not found')
text = text.replace(figure_marker, figure_replacement, 1)

css = r'''

/* Soft floral accents around the existing photo frame. */
#invitation .frame-flower{
    position:absolute;
    z-index:4;
    pointer-events:none;
    font-family:Georgia,'Times New Roman',serif;
    line-height:1;
    color:#d8a6ad;
    text-shadow:0 2px 7px rgba(104,27,32,.12);
    opacity:.9;
}
#invitation .frame-flower-one{
    top:-17px;
    left:18px;
    font-size:29px;
    transform:rotate(-14deg);
}
#invitation .frame-flower-two{
    top:24px;
    right:-11px;
    font-size:23px;
    color:#ead4d1;
    transform:rotate(16deg);
}
#invitation .frame-flower-three{
    bottom:22px;
    left:-12px;
    font-size:24px;
    color:#e3c1c4;
    transform:rotate(12deg);
}
#invitation .frame-flower-four{
    bottom:-15px;
    right:22px;
    font-size:30px;
    color:#cf939e;
    transform:rotate(-12deg);
}
@media(max-width:600px){
    #invitation .frame-flower-one,#invitation .frame-flower-four{font-size:24px;}
    #invitation .frame-flower-two,#invitation .frame-flower-three{font-size:19px;}
}
'''

style_marker = '</style>\n<link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@700&display=swap" rel="stylesheet">'
if style_marker not in text:
    raise SystemExit('Style marker not found')
text = text.replace(style_marker, css + '\n' + style_marker, 1)

path.write_text(text, encoding='utf-8')
