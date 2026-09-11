from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

style_marker = '</style>'
styles = r'''

/* Glassy RSVP card inspired by the soft transparent reference. */
#invitation .rsvp-card{
    background:rgba(190,145,154,.74);
    color:#4f2730;
    border:1.5px solid rgba(255,255,255,.52);
    box-shadow:0 18px 36px rgba(83,23,27,.13);
    backdrop-filter:blur(9px);
    -webkit-backdrop-filter:blur(9px);
}
#invitation .rsvp-card h2{color:#3f2028;}
#invitation .rsvp-card .rsvp-intro{
    color:rgba(79,39,48,.72);
}
#invitation .rsvp-option{
    border:2px solid rgba(255,255,255,.78);
    background:rgba(255,255,255,.16);
    color:#4f2730;
    box-shadow:inset 0 1px 0 rgba(255,255,255,.2);
}
#invitation .rsvp-option:hover{
    background:rgba(255,255,255,.24);
}
#invitation .rsvp-option:has(input:checked){
    background:rgba(255,255,255,.28);
    border-color:rgba(255,255,255,.95);
}
#invitation .rsvp-option-icon{
    background:rgba(245,239,238,.9);
    color:#70545b;
}
#invitation .rsvp-option input:checked ~ .rsvp-option-icon{
    background:#f8f3f1;
    color:#681b20;
}
#invitation .rsvp-submit{
    background:rgba(246,229,224,.54);
    color:#7d5158;
    border:1px solid rgba(255,255,255,.38);
    box-shadow:none;
}
#invitation .rsvp-message{color:#4f2730;}
#invitation .kids-note{
    width:100%;
    max-width:680px;
    margin:-10px auto 18px;
    padding:8px 18px 0;
    text-align:center;
    color:#681b20;
    font-family:'Noto Naskh Arabic',serif;
    font-size:clamp(1.15rem,4.7vw,1.5rem);
    line-height:1.9;
}
'''

if '/* Glassy RSVP card inspired by the soft transparent reference. */' not in text:
    if style_marker not in text:
        raise SystemExit('style marker not found')
    text = text.replace(style_marker, styles + '\n' + style_marker, 1)

old = '''    </form>\n</section>\n\n</section>\n'''
new = '''    </form>\n</section>\n\n<p class="kids-note" lang="ar" dir="rtl">نتمنى لأطفالكم نوماً هنيئاً</p>\n\n</section>\n'''
if 'class="kids-note"' not in text:
    if old not in text:
        raise SystemExit('RSVP closing block not found')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
