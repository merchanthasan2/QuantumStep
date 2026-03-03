import re, os

WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbwiYK9LDhZdbx3-r66rgRmfTClEyfH0VOWMFtKPw5nSzd_YRV7YETaqTVrOCaxpn7zNtg/exec'

tool_configs = [
    {
        'file': 'tool-salary-calculator.html',
        'tool_name': 'Salary Decoder',
        'tool_key': 'salary_decoder',
        'accent': '#818cf8',
        'accent_bg': 'rgba(99,102,241,.12)',
        'subtitle': 'Personalised tax analysis & salary breakdown for FY 2025-26.',
        'share_text': 'Deep tax analysis & salary decoder for FY 2025-26',
    },
    {
        'file': 'tool-home-loan-calculator.html',
        'tool_name': 'Home Loan Calculator',
        'tool_key': 'home_loan',
        'accent': '#34d399',
        'accent_bg': 'rgba(16,185,129,.12)',
        'subtitle': 'EMI, prepayment impact & interest breakup for your home loan.',
        'share_text': 'Calculate your Home Loan EMI and total interest',
    },
    {
        'file': 'tool-artha-wealth.html',
        'tool_name': 'ArthaWealth Calculator',
        'tool_key': 'artha_wealth',
        'accent': '#fbbf24',
        'accent_bg': 'rgba(251,191,36,.12)',
        'subtitle': 'Project your wealth with SIP, SWP & compound growth.',
        'share_text': 'Plan your wealth with SIP and SWP projections',
    },
    {
        'file': 'tool-job-transition.html',
        'tool_name': 'Job Transition Calculator',
        'tool_key': 'job_transition',
        'accent': '#fb7185',
        'accent_bg': 'rgba(244,63,94,.12)',
        'subtitle': 'Financially plan your career move — compare offers & bridge gaps.',
        'share_text': 'Financially plan your job transition',
    },
]

def build_modal(cfg):
    return f'''
    <!-- QS Name Capture Modal -->
    <div id="qs-capture-overlay" style="position:fixed;inset:0;z-index:9999;background:rgba(2,6,23,0.93);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);display:flex;align-items:center;justify-content:center;padding:1rem;">
        <div style="width:100%;max-width:420px;background:rgba(15,23,42,0.97);border:1px solid rgba(255,255,255,0.09);border-radius:1.75rem;padding:2.25rem;box-shadow:0 32px 80px rgba(0,0,0,0.7);">
            <div style="display:flex;align-items:center;gap:.65rem;margin-bottom:1.75rem;">
                <div style="width:36px;height:36px;border-radius:.65rem;background:{cfg['accent_bg']};border:1px solid {cfg['accent']}44;display:flex;align-items:center;justify-content:center;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="{cfg['accent']}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                </div>
                <span style="font-size:.85rem;font-weight:700;color:#e2e8f0;">Quantum Step Tools</span>
            </div>
            <h2 style="font-size:1.4rem;font-weight:800;color:#f1f5f9;margin:0 0 .4rem;letter-spacing:-.02em;">{cfg['tool_name']}</h2>
            <p style="font-size:.82rem;color:#475569;margin:0 0 1.75rem;line-height:1.55;">{cfg['subtitle']}</p>
            <form onsubmit="qsCapture(event)">
                <label style="display:block;font-size:.7rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.35rem;">Your Name</label>
                <input id="qs-name" type="text" placeholder="e.g. Rahul Sharma" required autocomplete="name"
                    style="width:100%;box-sizing:border-box;padding:.65rem .9rem;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:.85rem;color:#f1f5f9;font-size:.88rem;font-family:inherit;margin-bottom:.9rem;outline:none;transition:border-color .2s;"
                    onfocus="this.style.borderColor='{cfg['accent']}80'" onblur="this.style.borderColor='rgba(255,255,255,.09)'">
                <label style="display:block;font-size:.7rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.35rem;">Work Email <span style="font-weight:400;text-transform:none;">(optional)</span></label>
                <input id="qs-email" type="email" placeholder="you@company.com" autocomplete="email"
                    style="width:100%;box-sizing:border-box;padding:.65rem .9rem;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:.85rem;color:#f1f5f9;font-size:.88rem;font-family:inherit;margin-bottom:1.4rem;outline:none;transition:border-color .2s;"
                    onfocus="this.style.borderColor='{cfg['accent']}80'" onblur="this.style.borderColor='rgba(255,255,255,.09)'">
                <button type="submit" style="width:100%;padding:.75rem 1.25rem;background:linear-gradient(135deg,{cfg['accent']},{cfg['accent']}aa);border:none;border-radius:.85rem;color:#fff;font-size:.88rem;font-weight:700;cursor:pointer;font-family:inherit;display:flex;align-items:center;justify-content:center;gap:.45rem;transition:opacity .2s;" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
                    Start Exploring
                </button>
            </form>
            <p style="text-align:center;font-size:.68rem;color:#1e293b;margin-top:1rem;">Your information is never shared or sold.</p>
        </div>
    </div>

    <!-- QS Corner Share Icons -->
    <div style="position:fixed;top:130px;right:1.25rem;z-index:490;display:flex;flex-direction:column;gap:.45rem;align-items:center;">
        <span style="font-size:.58rem;color:#334155;text-transform:uppercase;letter-spacing:.09em;font-weight:700;writing-mode:vertical-rl;margin-bottom:.2rem;">Share</span>
        <button title="WhatsApp" onclick="(function(){{var u=encodeURIComponent(location.href),t=encodeURIComponent('{cfg['share_text']} — by Quantum Step');window.open('https://wa.me/?text='+t+'%20'+u,'_blank')}})()" style="width:34px;height:34px;border-radius:50%;background:rgba(37,211,102,.1);border:1px solid rgba(37,211,102,.2);display:flex;align-items:center;justify-content:center;color:#25D166;cursor:pointer;transition:all .2s;padding:0;" onmouseover="this.style.background='rgba(37,211,102,.22)';this.style.transform='scale(1.1)'" onmouseout="this.style.background='rgba(37,211,102,.1)';this.style.transform=''"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.348z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.085.54 4.043 1.481 5.749L.073 23.925l6.345-1.384A11.93 11.93 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 0 1-5.012-1.37l-.358-.213-3.747.817.848-3.651-.234-.372A9.818 9.818 0 1 1 12 21.818z"/></svg></button>
        <button title="LinkedIn" onclick="(function(){{window.open('https://www.linkedin.com/sharing/share-offsite/?url='+encodeURIComponent(location.href),'_blank')}})()" style="width:34px;height:34px;border-radius:50%;background:rgba(10,102,194,.1);border:1px solid rgba(10,102,194,.2);display:flex;align-items:center;justify-content:center;color:#0A66C2;cursor:pointer;transition:all .2s;padding:0;" onmouseover="this.style.background='rgba(10,102,194,.22)';this.style.transform='scale(1.1)'" onmouseout="this.style.background='rgba(10,102,194,.1)';this.style.transform=''"><svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zm2-3a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/></svg></button>
        <button title="X / Twitter" onclick="(function(){{var u=encodeURIComponent(location.href),t=encodeURIComponent('{cfg['share_text']}');window.open('https://twitter.com/intent/tweet?text='+t+'&url='+u,'_blank')}})()" style="width:34px;height:34px;border-radius:50%;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;color:#cbd5e1;cursor:pointer;transition:all .2s;padding:0;" onmouseover="this.style.background='rgba(255,255,255,.12)';this.style.transform='scale(1.1)'" onmouseout="this.style.background='rgba(255,255,255,.05)';this.style.transform=''"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.277 5.653zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></button>
    </div>

    <script>
    (function() {{
        var TOOL = '{cfg['tool_key']}';
        var WEBHOOK = '{WEBHOOK_URL}';
        var KEY = 'qs_user_' + TOOL;

        function welcome(name) {{
            var g = document.getElementById('qs-welcome-greet');
            if (g) g.textContent = 'Welcome back, ' + name + '.';
            document.title = name + ' \u2014 ' + document.title;
        }}

        window.qsCapture = function(e) {{
            e.preventDefault();
            var name = document.getElementById('qs-name').value.trim();
            var email = (document.getElementById('qs-email') || {{}}).value || '';
            if (!name) return;
            sessionStorage.setItem(KEY, JSON.stringify({{name: name, email: email}}));
            var ov = document.getElementById('qs-capture-overlay');
            if (ov) {{ ov.style.opacity = '0'; ov.style.transition = 'opacity .35s'; setTimeout(function() {{ ov.remove(); }}, 350); }}
            welcome(name);
            var payload = JSON.stringify({{name: name, email: email, tool: TOOL, timestamp: new Date().toISOString(), url: location.href, referrer: document.referrer || 'direct'}});
            try {{ navigator.sendBeacon(WEBHOOK, payload); }} catch(e2) {{ fetch(WEBHOOK, {{method:'POST', body: payload, mode:'no-cors'}}).catch(function(){{}}); }}
        }};

        var existing = sessionStorage.getItem(KEY);
        if (existing) {{
            var data = JSON.parse(existing);
            var ov = document.getElementById('qs-capture-overlay');
            if (ov) ov.remove();
            setTimeout(function() {{ welcome(data.name); }}, 200);
        }}
    }})();
    </script>
'''

for cfg in tool_configs:
    fpath = os.path.join(r'd:\Vibe Code\Quantum Step', cfg['file'])
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old inject attempts
    content = re.sub(r'\s*<!-- QS Name Capture Modal -->.*?</script>', '', content, count=1, flags=re.DOTALL)
    content = re.sub(r'\s*<!-- User Capture Modal -->.*?</script>', '', content, count=1, flags=re.DOTALL)
    content = re.sub(r'\s*<!-- QS Corner Share Icons -->.*?</div>\s*\n\s*<script>.*?</script>', '', content, count=1, flags=re.DOTALL)

    # Inject RIGHT AFTER the opening <body ...> tag using regex
    modal_html = build_modal(cfg)
    content = re.sub(
        r'(<body[^>]*>)',
        lambda m: m.group(0) + modal_html,
        content, count=1
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Injected: {cfg["file"]}')

# Verify
print('\nVerification:')
for cfg in tool_configs:
    fpath = os.path.join(r'd:\Vibe Code\Quantum Step', cfg['file'])
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f'  {cfg["file"]}: modal={("qs-capture-overlay" in c)}, webhook={("AKfycbwi" in c)}, share={("qs-capture-overlay" in c)}')

print('\nDone.')
