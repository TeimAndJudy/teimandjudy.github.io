from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

styles = r'''

/* Burgundy RSVP shell + smaller translucent inner panel + instant choice. */
#invitation .rsvp-card{
    position:relative;
    overflow:hidden;
    background:linear-gradient(145deg,#64191d,#781f25);
    color:#fff8ed;
    padding:58px 46px 52px;
    border:0;
    box-shadow:0 18px 36px rgba(83,23,27,.18);
    backdrop-filter:none;
    -webkit-backdrop-filter:none;
}
#invitation .rsvp-card::before{
    content:"";
    position:absolute;
    inset:25px;
    border-radius:24px;
    background:rgba(224,190,196,.72);
    border:1.5px solid rgba(255,255,255,.46);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.24),0 12px 26px rgba(50,0,0,.12);
    backdrop-filter:blur(8px);
    -webkit-backdrop-filter:blur(8px);
    pointer-events:none;
}
#invitation .rsvp-card > *{
    position:relative;
    z-index:1;
}
#invitation .rsvp-card h2{color:#4b232c;}
#invitation .rsvp-card .rsvp-intro{color:rgba(75,35,44,.74);}
#invitation .rsvp-option{
    background:rgba(255,255,255,.16);
    color:#4b232c;
    border-color:rgba(255,255,255,.82);
}
#invitation .rsvp-option:hover{background:rgba(255,255,255,.22);}
#invitation .rsvp-option:has(input:checked){
    background:rgba(255,255,255,.30);
    border-color:#fff;
}
#invitation .rsvp-message{color:#4b232c;}
#invitation .rsvp-submit{display:none!important;}
@media(max-width:600px){
    #invitation .rsvp-card{padding:50px 28px 44px;}
    #invitation .rsvp-card::before{inset:16px;}
}
'''

if '/* Burgundy RSVP shell + smaller translucent inner panel + instant choice. */' not in text:
    text = text.replace('</style>', styles + '\n</style>', 1)

js_marker = "const rsvpMessage = document.getElementById('rsvp-message');"
auto_js = '''\n\n/* Submit RSVP immediately when a guest taps either attendance choice. */\nif (rsvpForm) {\n    rsvpForm.querySelectorAll('input[name="attendance"]').forEach(function(input){\n        input.addEventListener('change', function(){\n            if (input.checked) rsvpForm.requestSubmit();\n        });\n    });\n}\n'''

if 'Submit RSVP immediately when a guest taps either attendance choice.' not in text:
    pos = text.find(js_marker)
    if pos == -1:
        raise SystemExit('RSVP message marker not found')
    pos = pos + len(js_marker)
    text = text[:pos] + auto_js + text[pos:]

path.write_text(text, encoding='utf-8')
