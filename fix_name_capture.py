import os, re

# =========================================================
# User Name Capture Modal for all 4 tool pages
# - Shows on first visit per session (sessionStorage)
# - Greets user by name in the tool's header
# - Logs name, email, tool, timestamp to Google Sheets
#   via a Google Apps Script webhook URL
# =========================================================

WEBHOOK_PLACEHOLDER = 'YOUR_GOOGLE_APPS_SCRIPT_WEBHOOK_URL'

tool_configs = [
    {
        'file': 'tool-salary-calculator.html',
        'tool_name': 'Salary Decoder',
        'tool_key': 'salary_decoder',
        'accent': '#818cf8',
        'accent_bg': 'rgba(99,102,241,.12)',
        'welcome_subtitle': 'Get personalised tax analysis & salary insights for FY 2025-26.',
    },
    {
        'file': 'tool-home-loan-calculator.html',
        'tool_name': 'Home Loan Calculator',
        'tool_key': 'home_loan',
        'accent': '#34d399',
        'accent_bg': 'rgba(16,185,129,.12)',
        'welcome_subtitle': 'Calculate EMIs, prepayment impact & total interest for your dream home.',
    },
    {
        'file': 'tool-artha-wealth.html',
        'tool_name': 'ArthaWealth Calculator',
        'tool_key': 'artha_wealth',
        'accent': '#fbbf24',
        'accent_bg': 'rgba(251,191,36,.12)',
        'welcome_subtitle': 'Project your wealth with SIP, SWP & compound growth simulations.',
    },
    {
        'file': 'tool-job-transition.html',
        'tool_name': 'Job Transition Calculator',
        'tool_key': 'job_transition',
        'accent': '#fb7185',
        'accent_bg': 'rgba(244,63,94,.12)',
        'welcome_subtitle': 'Plan your career move financially — compare offers, bridge gaps & more.',
    },
]

def build_capture_block(cfg):
    return f"""
    <!-- User Capture Modal -->
    <div id="qs-capture-overlay" style="position:fixed;inset:0;z-index:9999;background:rgba(2,6,23,0.92);backdrop-filter:blur(14px);display:flex;align-items:center;justify-content:center;padding:1rem;">
        <div style="width:100%;max-width:440px;background:rgba(15,23,42,0.95);border:1px solid rgba(255,255,255,0.1);border-radius:1.75rem;padding:2.5rem;position:relative;box-shadow:0 32px 80px rgba(0,0,0,0.6);">
            <!-- Logo -->
            <div style="display:flex;align-items:center;gap:.75rem;margin-bottom:2rem;">
                <div style="width:38px;height:38px;border-radius:.75rem;background:{cfg['accent_bg']};border:1px solid {cfg['accent']}33;display:flex;align-items:center;justify-content:center;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{cfg['accent']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                </div>
                <span style="font-size:.9rem;font-weight:700;color:#f1f5f9;letter-spacing:-.01em;">Quantum Step Tools</span>
            </div>

            <!-- Heading -->
            <h2 style="font-size:1.5rem;font-weight:800;color:#f1f5f9;margin:0 0 .5rem;letter-spacing:-.02em;">{cfg['tool_name']}</h2>
            <p style="font-size:.875rem;color:#64748b;margin:0 0 2rem;line-height:1.5;">{cfg['welcome_subtitle']}</p>

            <!-- Form -->
            <form id="qs-capture-form" onsubmit="qsHandleCapture(event)">
                <label for="qs-name" style="display:block;font-size:.72rem;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.4rem;">Your Name</label>
                <input id="qs-name" type="text" placeholder="e.g. Rahul Sharma" required autocomplete="name"
                    style="width:100%;box-sizing:border-box;padding:.7rem 1rem;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:.875rem;color:#f1f5f9;font-size:.9rem;font-family:inherit;margin-bottom:1rem;outline:none;transition:border-color .2s;"
                    onfocus="this.style.borderColor='{cfg['accent']}'" onblur="this.style.borderColor='rgba(255,255,255,.1)'">

                <label for="qs-email" style="display:block;font-size:.72rem;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.4rem;">Work Email <span style="color:#334155;font-weight:400;text-transform:none;">(optional)</span></label>
                <input id="qs-email" type="email" placeholder="email@company.com" autocomplete="email"
                    style="width:100%;box-sizing:border-box;padding:.7rem 1rem;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:.875rem;color:#f1f5f9;font-size:.9rem;font-family:inherit;margin-bottom:1.5rem;outline:none;transition:border-color .2s;"
                    onfocus="this.style.borderColor='{cfg['accent']}'" onblur="this.style.borderColor='rgba(255,255,255,.1)'">

                <button type="submit"
                    style="width:100%;padding:.8rem 1.5rem;background:linear-gradient(135deg,{cfg['accent']},{cfg['accent']}cc);border:none;border-radius:.875rem;color:#fff;font-size:.9rem;font-weight:700;cursor:pointer;transition:all .2s;font-family:inherit;display:flex;align-items:center;justify-content:center;gap:.5rem;"
                    onmouseover="this.style.opacity='.88';this.style.transform='translateY(-1px)'" onmouseout="this.style.opacity='1';this.style.transform=''">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
                    Start Exploring
                </button>
            </form>

            <p style="text-align:center;font-size:.72rem;color:#334155;margin-top:1.25rem;">Your data is used only to personalise your experience. We never sell it.</p>
        </div>
    </div>

    <script>
        (function() {{
            const TOOL = '{cfg['tool_key']}';
            const WEBHOOK = '{WEBHOOK_PLACEHOLDER}';
            const SESSION_KEY = 'qs_user_' + TOOL;

            function qsApplyWelcome(name) {{
                // Show welcome greeting in tool header if element exists
                const greet = document.getElementById('qs-welcome-greet');
                if (greet) greet.textContent = 'Welcome, ' + name + '.';
                // Also update document title
                document.title = 'Hi ' + name + ' — ' + document.title.split(' — ').pop();
            }}

            window.qsHandleCapture = function(e) {{
                e.preventDefault();
                const name = document.getElementById('qs-name').value.trim();
                const email = document.getElementById('qs-email').value.trim();
                if (!name) return;

                // Store in session
                sessionStorage.setItem(SESSION_KEY, JSON.stringify({{ name, email }}));

                // Close modal
                const overlay = document.getElementById('qs-capture-overlay');
                if (overlay) {{ overlay.style.opacity = '0'; overlay.style.transition = 'opacity .3s'; setTimeout(() => overlay.remove(), 300); }}

                // Welcome
                qsApplyWelcome(name);

                // Log to Google Sheets (non-blocking)
                if (WEBHOOK && WEBHOOK !== '{WEBHOOK_PLACEHOLDER}') {{
                    const payload = {{ name, email, tool: TOOL, timestamp: new Date().toISOString(), url: window.location.href, referrer: document.referrer || 'direct' }};
                    navigator.sendBeacon ? navigator.sendBeacon(WEBHOOK, JSON.stringify(payload))
                        : fetch(WEBHOOK, {{ method: 'POST', body: JSON.stringify(payload), mode: 'no-cors' }}).catch(() => {{}});
                }}
            }};

            // Check if already captured this session
            const existing = sessionStorage.getItem(SESSION_KEY);
            if (existing) {{
                const {{ name }} = JSON.parse(existing);
                document.getElementById('qs-capture-overlay') && document.getElementById('qs-capture-overlay').remove();
                setTimeout(() => qsApplyWelcome(name), 100);
            }}
        }})();
    </script>
"""

for cfg in tool_configs:
    fpath = os.path.join(r'd:\Vibe Code\Quantum Step', cfg['file'])
    if not os.path.exists(fpath):
        print(f'NOT FOUND: {cfg["file"]}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old capture overlay if any
    content = re.sub(r'\s*<!-- User Capture Modal -->.*?</script>', '', content, count=1, flags=re.DOTALL)

    # Inject capture block right after <body>
    capture_html = build_capture_block(cfg)
    content = content.replace('<body>', '<body>' + capture_html, 1)

    # Add a welcome greeting span inside the tool header (if not present)
    # Place just after the first <h1 in the main content area
    if 'qs-welcome-greet' not in content:
        content = re.sub(
            r'(</h1>\s*)',
            r'\1<p id="qs-welcome-greet" style="font-size:.9rem;color:#64748b;margin:.25rem 0 0;font-weight:500;letter-spacing:-.01em;"></p>\n',
            content, count=1
        )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Done: {cfg["file"]}')


# =========================================================
# Create Google Apps Script for the user to deploy
# =========================================================
gas_script = """// Google Apps Script — Quantum Step Tool Lead Logger
// 1. Open Google Sheets → Extensions → Apps Script
// 2. Paste this code, click Save
// 3. Deploy → New Deployment → Web App
//    - Execute as: Me
//    - Access: Anyone
// 4. Copy the Deployment URL and paste into each tool HTML
//    where it says: YOUR_GOOGLE_APPS_SCRIPT_WEBHOOK_URL

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Leads') 
      || SpreadsheetApp.getActiveSpreadsheet().insertSheet('Leads');
    
    // Add headers if first row is empty
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Timestamp', 'Name', 'Email', 'Tool', 'URL', 'Referrer']);
      sheet.getRange(1, 1, 1, 6).setFontWeight('bold').setBackground('#1e293b').setFontColor('#f1f5f9');
    }
    
    const data = JSON.parse(e.postData.contents);
    sheet.appendRow([
      data.timestamp || new Date().toISOString(),
      data.name || '',
      data.email || '',
      data.tool || '',
      data.url || '',
      data.referrer || ''
    ]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch(err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Also supports GET for testing
function doGet(e) {
  return ContentService.createTextOutput('Quantum Step Lead Logger is active.');
}
"""

gas_path = r'd:\Vibe Code\Quantum Step\Docs\google-apps-script-lead-logger.js'
os.makedirs(os.path.dirname(gas_path), exist_ok=True)
with open(gas_path, 'w', encoding='utf-8') as f:
    f.write(gas_script)

print(f'\nGoogle Apps Script saved to: Docs/google-apps-script-lead-logger.js')
print('\nSetup instructions:')
print('1. Open a Google Sheet')
print('2. Extensions → Apps Script')
print('3. Paste the contents of google-apps-script-lead-logger.js')
print('4. Deploy → New Deployment → Web App (Anyone can access)')
print('5. Replace YOUR_GOOGLE_APPS_SCRIPT_WEBHOOK_URL in each tool HTML')
print('\nAll done.')
