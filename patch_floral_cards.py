from pathlib import Path
import base64
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

start_marker = '/* FLORAL DARK COMPACT CARDS START */'
end_marker = '/* FLORAL DARK COMPACT CARDS END */'

# Remove an earlier copy of this patch if it exists, so reruns stay clean.
pattern = re.compile(re.escape(start_marker) + r'.*?' + re.escape(end_marker), re.S)
text = pattern.sub('', text)

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180">
<g fill="none" stroke-linecap="round">
  <path d="M28 154 C52 115 78 75 129 28" stroke="#a28b69" stroke-width="2"/>
  <path d="M45 163 C72 128 105 94 171 58" stroke="#b49467" stroke-width="1.7"/>
  <path d="M18 132 C57 120 83 102 111 76" stroke="#8c7d5c" stroke-width="1.6"/>
  <path d="M106 88 C133 75 155 57 185 32" stroke="#b89b6a" stroke-width="1.4"/>
</g>
<g fill="#8d8965">
  <ellipse cx="74" cy="108" rx="7" ry="19" transform="rotate(-42 74 108)"/>
  <ellipse cx="104" cy="83" rx="7" ry="18" transform="rotate(34 104 83)"/>
  <ellipse cx="143" cy="57" rx="6" ry="17" transform="rotate(-38 143 57)"/>
  <ellipse cx="52" cy="132" rx="6" ry="16" transform="rotate(28 52 132)"/>
</g>
<g fill="#c99b5e">
  <circle cx="155" cy="42" r="3"/><circle cx="168" cy="34" r="2.8"/><circle cx="179" cy="44" r="2.3"/>
  <circle cx="126" cy="68" r="2.7"/><circle cx="138" cy="67" r="2.2"/><circle cx="148" cy="73" r="2.4"/>
</g>
<!-- large burgundy bloom -->
<g transform="translate(5 72)">
  <ellipse cx="44" cy="40" rx="28" ry="34" fill="#5b0d17"/>
  <ellipse cx="44" cy="18" rx="18" ry="28" fill="#7f1825"/>
  <ellipse cx="20" cy="36" rx="18" ry="28" fill="#6a111d" transform="rotate(-48 20 36)"/>
  <ellipse cx="68" cy="36" rx="18" ry="28" fill="#8b2130" transform="rotate(48 68 36)"/>
  <ellipse cx="28" cy="60" rx="21" ry="26" fill="#4b0b13"/>
  <ellipse cx="61" cy="60" rx="21" ry="26" fill="#67101a"/>
  <circle cx="44" cy="42" r="11" fill="#2f0710"/>
  <g fill="#c6924e"><circle cx="40" cy="38" r="2"/><circle cx="48" cy="36" r="2"/><circle cx="44" cy="46" r="2"/></g>
</g>
<!-- beige bloom -->
<g transform="translate(90 95)">
  <ellipse cx="34" cy="26" rx="16" ry="22" fill="#eadcc3"/>
  <ellipse cx="17" cy="39" rx="15" ry="21" fill="#dec9aa" transform="rotate(-42 17 39)"/>
  <ellipse cx="51" cy="39" rx="15" ry="21" fill="#f0e5cf" transform="rotate(42 51 39)"/>
  <ellipse cx="25" cy="57" rx="16" ry="20" fill="#d7c09e"/>
  <ellipse cx="46" cy="57" rx="16" ry="20" fill="#eadcc3"/>
  <circle cx="34" cy="43" r="9" fill="#b38d5d"/>
</g>
<!-- smaller burgundy bloom -->
<g transform="translate(145 88) scale(.72)">
  <ellipse cx="35" cy="34" rx="24" ry="29" fill="#6c111d"/>
  <ellipse cx="35" cy="15" rx="16" ry="23" fill="#8f2431"/>
  <ellipse cx="17" cy="34" rx="15" ry="23" fill="#57101a"/>
  <ellipse cx="53" cy="34" rx="15" ry="23" fill="#7d1724"/>
  <ellipse cx="35" cy="53" rx="18" ry="22" fill="#4f0c15"/>
  <circle cx="35" cy="34" r="9" fill="#2b0710"/>
</g>
</svg>'''
floral_b64 = base64.b64encode(svg.encode('utf-8')).decode('ascii')

css = f'''
{start_marker}
/* Darker, slightly smaller invitation cards with burgundy + beige floral corners. */
#invitation .love-card,
#invitation .reception-card,
#invitation .venue-card,
#invitation .rsvp-card{{
    width:min(91%,620px) !important;
    max-width:620px !important;
    margin:0 auto 56px !important;
    padding:42px 22px !important;
    border-radius:28px !important;
    background:linear-gradient(150deg,#4b0b12 0%,#5d0f18 46%,#71151f 100%) !important;
    color:#fff8ed !important;
    border:1px solid rgba(247,225,208,.26) !important;
    box-shadow:0 22px 42px rgba(72,8,17,.22) !important;
    position:relative !important;
    overflow:visible !important;
    isolation:isolate;
}}

#invitation .love-card::before,
#invitation .reception-card::before,
#invitation .venue-card::before,
#invitation .rsvp-card::before,
#invitation .love-card::after,
#invitation .reception-card::after,
#invitation .venue-card::after,
#invitation .rsvp-card::after{{
    content:"";
    position:absolute;
    width:150px;
    height:124px;
    background-image:url("data:image/svg+xml;base64,{floral_b64}");
    background-repeat:no-repeat;
    background-size:contain;
    pointer-events:none;
    z-index:0;
    opacity:.98;
    filter:drop-shadow(0 7px 10px rgba(57,4,12,.12));
}}

#invitation .love-card::before,
#invitation .reception-card::before,
#invitation .venue-card::before,
#invitation .rsvp-card::before{{
    left:-48px;
    top:-38px;
    transform:rotate(-7deg);
}}

#invitation .love-card::after,
#invitation .reception-card::after,
#invitation .venue-card::after,
#invitation .rsvp-card::after{{
    right:-47px;
    bottom:-37px;
    transform:rotate(173deg);
}}

#invitation .love-card > *,
#invitation .reception-card > *,
#invitation .venue-card > *,
#invitation .rsvp-card > *{{
    position:relative;
    z-index:1;
}}

/* Keep the soft inner RSVP panel but deepen it so it sits elegantly inside the dark outer card. */
#invitation .rsvp-inner,
#invitation .rsvp-panel,
#invitation .rsvp-form-wrap{{
    background:rgba(226,188,191,.22) !important;
    border:1px solid rgba(255,245,235,.34) !important;
    backdrop-filter:blur(7px);
    -webkit-backdrop-filter:blur(7px);
}}

#invitation .rsvp-card h2,
#invitation .rsvp-card .rsvp-intro,
#invitation .rsvp-card .rsvp-message{{
    color:#fff4e9 !important;
}}

#invitation .venue-name{{color:#ead0c5 !important;}}
#invitation .wedding-calendar{{max-width:490px !important;}}
#invitation .venue-map-frame{{max-width:500px !important;}}

@media(max-width:600px){{
    #invitation .love-card,
    #invitation .reception-card,
    #invitation .venue-card,
    #invitation .rsvp-card{{
        width:90vw !important;
        padding:36px 16px !important;
        border-radius:24px !important;
        margin-bottom:52px !important;
    }}
    #invitation .love-card::before,
    #invitation .reception-card::before,
    #invitation .venue-card::before,
    #invitation .rsvp-card::before,
    #invitation .love-card::after,
    #invitation .reception-card::after,
    #invitation .venue-card::after,
    #invitation .rsvp-card::after{{
        width:112px;
        height:93px;
    }}
    #invitation .love-card::before,
    #invitation .reception-card::before,
    #invitation .venue-card::before,
    #invitation .rsvp-card::before{{left:-30px;top:-27px;}}
    #invitation .love-card::after,
    #invitation .reception-card::after,
    #invitation .venue-card::after,
    #invitation .rsvp-card::after{{right:-29px;bottom:-27px;}}
}}
{end_marker}
'''

if '</style>' not in text:
    raise SystemExit('style closing tag not found')
text = text.replace('</style>', css + '\n</style>', 1)
path.write_text(text, encoding='utf-8')
print('Applied floral compact dark cards CSS')
