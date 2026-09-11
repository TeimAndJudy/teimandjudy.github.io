from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

css = r'''

/* RSVP card — personalized from the guest name in the invitation link. */
#invitation .rsvp-card{
    width:100%;
    max-width:680px;
    margin:0 auto 48px;
    padding:46px 24px 42px;
    border-radius:24px;
    background:linear-gradient(145deg,#64191d,#741f24);
    color:#fff8ed;
    box-shadow:0 18px 36px rgba(83,23,27,.14);
    font-family:'Noto Naskh Arabic',serif;
}
#invitation .rsvp-card h2{
    margin:0 0 12px;
    font-size:clamp(2rem,7vw,3rem);
    line-height:1.5;
    font-weight:700;
}
#invitation .rsvp-card .rsvp-intro{
    max-width:520px;
    margin:0 auto 30px;
    color:#f2d9cd;
    font-size:clamp(1.05rem,4.2vw,1.35rem);
    line-height:1.9;
}
#invitation .rsvp-question{
    margin:0 0 18px;
    color:#fff8ed;
    font-size:clamp(1.25rem,5vw,1.65rem);
    font-weight:600;
}
#invitation .rsvp-options{
    display:grid;
    gap:14px;
    width:100%;
    max-width:500px;
    margin:0 auto;
}
#invitation .rsvp-option{
    position:relative;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:14px;
    width:100%;
    min-height:72px;
    padding:13px 16px 13px 20px;
    border:2px solid rgba(255,248,237,.78);
    border-radius:20px;
    background:rgba(255,255,255,.07);
    color:#fff8ed;
    cursor:pointer;
    transition:transform .22s ease,background .22s ease,border-color .22s ease;
}
#invitation .rsvp-option:hover{
    transform:translateY(-2px);
    background:rgba(255,255,255,.11);
}
#invitation .rsvp-option input{
    position:absolute;
    opacity:0;
    pointer-events:none;
}
#invitation .rsvp-option-text{
    flex:1;
    text-align:center;
    font-size:clamp(1.18rem,4.7vw,1.55rem);
    line-height:1.6;
}
#invitation .rsvp-option-icon{
    display:grid;
    place-items:center;
    width:44px;
    height:44px;
    flex:0 0 44px;
    border-radius:50%;
    background:#f3e8e3;
    color:#76565a;
    font-family:Arial,sans-serif;
    font-size:24px;
    transition:background .22s ease,color .22s ease,transform .22s ease;
}
#invitation .rsvp-option:has(input:checked){
    background:rgba(255,248,237,.17);
    border-color:#fff8ed;
    transform:translateY(-1px);
}
#invitation .rsvp-option input:checked ~ .rsvp-option-icon{
    background:#fff8ed;
    color:#681b20;
    transform:scale(1.05);
}
#invitation .rsvp-submit{
    width:100%;
    max-width:500px;
    min-height:64px;
    margin:20px auto 0;
    border:0;
    border-radius:20px;
    background:#f1ddd2;
    color:#681b20;
    font-family:'Noto Naskh Arabic',serif;
    font-size:clamp(1.2rem,4.8vw,1.55rem);
    font-weight:700;
    cursor:pointer;
    box-shadow:0 8px 18px rgba(45,0,0,.16);
    transition:transform .22s ease,opacity .22s ease;
}
#invitation .rsvp-submit:hover{transform:translateY(-2px);}
#invitation .rsvp-submit:disabled{cursor:default;opacity:.72;transform:none;}
#invitation .rsvp-message{
    min-height:31px;
    margin:17px auto 0;
    color:#f7e7df;
    font-size:1.08rem;
    line-height:1.7;
}
@media(max-width:600px){
    #invitation .rsvp-card{padding:38px 16px 34px;}
    #invitation .rsvp-option{min-height:68px;padding:11px 13px 11px 16px;}
    #invitation .rsvp-option-icon{width:40px;height:40px;flex-basis:40px;font-size:21px;}
}
'''

html = r'''

<section class="rsvp-card" lang="ar" dir="rtl" aria-labelledby="rsvp-title">
    <h2 id="rsvp-title">تأكيد الحضور</h2>
    <p class="rsvp-intro">حضوركم شرف عظيم لنا، نرجو تأكيد الحضور حتى نتمكن من إعداد أجمل استقبال لكم.</p>
    <form id="rsvp-form">
        <input type="hidden" id="rsvpGuestInput" name="guest" value="ضيفنا العزيز">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <div class="rsvp-question">هل ستحضر؟</div>
        <div class="rsvp-options">
            <label class="rsvp-option">
                <input type="radio" name="attendance" value="سأكون حاضراً" required>
                <span class="rsvp-option-text">سأكون حاضراً</span>
                <span class="rsvp-option-icon" aria-hidden="true">✓</span>
            </label>
            <label class="rsvp-option">
                <input type="radio" name="attendance" value="عذراً، لن أتمكن من الحضور" required>
                <span class="rsvp-option-text">عذراً، لن أتمكن من الحضور</span>
                <span class="rsvp-option-icon" aria-hidden="true">×</span>
            </label>
        </div>
        <button class="rsvp-submit" type="submit">تأكيد</button>
        <div class="rsvp-message" id="rsvp-message" role="status" aria-live="polite"></div>
    </form>
</section>
'''

js = r'''

/* RSVP: guest identity comes from the personalized invitation URL. */
const rsvpGuestInput = document.getElementById('rsvpGuestInput');
if (rsvpGuestInput) rsvpGuestInput.value = guest;

const rsvpForm = document.getElementById('rsvp-form');
const rsvpMessage = document.getElementById('rsvp-message');
if (rsvpForm) {
    rsvpForm.addEventListener('submit', async function(event) {
        event.preventDefault();
        const selected = rsvpForm.querySelector('input[name="attendance"]:checked');
        if (!selected) {
            rsvpMessage.textContent = 'يرجى اختيار أحد الخيارين.';
            return;
        }

        const submitButton = rsvpForm.querySelector('.rsvp-submit');
        submitButton.disabled = true;
        submitButton.textContent = 'جارٍ الإرسال…';
        rsvpMessage.textContent = '';

        const data = new FormData(rsvpForm);
        data.set('guest', guest);
        data.set('_subject', 'Wedding RSVP — ' + guest);

        try {
            const endpoint = 'https://formsubmit.co/ajax/' + atob('am91ZHkubW91aGFmZmVsQGhvdG1haWwuY29t');
            const response = await fetch(endpoint, {
                method:'POST',
                headers:{'Accept':'application/json'},
                body:data
            });
            const result = await response.json().catch(function(){ return {}; });
            if (!response.ok || result.success === false) throw new Error('submit failed');

            rsvpMessage.textContent = 'شكراً لكم، تم تسجيل ردّكم ♡';
            submitButton.textContent = 'تم التأكيد ✓';
            rsvpForm.querySelectorAll('input[name="attendance"]').forEach(function(input){
                input.disabled = true;
            });
        } catch (error) {
            rsvpMessage.textContent = 'تعذّر إرسال الرد الآن، يرجى المحاولة مرة أخرى.';
            submitButton.disabled = false;
            submitButton.textContent = 'تأكيد';
        }
    });
}
'''

if '/* RSVP card — personalized from the guest name in the invitation link. */' not in text:
    style_marker = '</style>'
    if style_marker not in text:
        raise SystemExit('style marker not found')
    text = text.replace(style_marker, css + '\n' + style_marker, 1)

if 'id="rsvp-form"' not in text:
    invite_end = '\n</section>\n\n\n\n<script>'
    if invite_end not in text:
        raise SystemExit('invitation end marker not found')
    text = text.replace(invite_end, html + '\n</section>\n\n\n\n<script>', 1)

old_guest = '''const guest =\nparams.get("guest");\n\nif(guest){\n\n    document\n    .getElementById("guestName")\n    .textContent = guest;\n\n}\n'''
new_guest = '''const guestParam = params.get("guest");\nconst guest = (guestParam || "ضيفنا العزيز").trim() || "ضيفنا العزيز";\n\ndocument\n.getElementById("guestName")\n.textContent = guest;\n'''
if old_guest in text:
    text = text.replace(old_guest, new_guest, 1)
elif 'const guestParam = params.get("guest");' not in text:
    raise SystemExit('guest script marker not found')

if '/* RSVP: guest identity comes from the personalized invitation URL. */' not in text:
    open_marker = '\n\n/* =========================\n   OPEN\n========================= */'
    if open_marker not in text:
        raise SystemExit('open marker not found')
    text = text.replace(open_marker, js + open_marker, 1)

path.write_text(text, encoding='utf-8')
