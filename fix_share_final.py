import re
import os

# =========================================================
# Comprehensive fix script:
# 1. Link tool-shared.css to all 4 tool pages
# 2. Remove duplicate share sections (inline bottom share)
# 3. Add compact corner share icons to each tool's header
# 4. Fix .share-bar floating CSS display
# =========================================================

tool_files = [
    ('tool-salary-calculator.html', 'salary'),
    ('tool-home-loan-calculator.html', 'homeloan'),
    ('tool-artha-wealth.html', 'artha'),
    ('tool-job-transition.html', 'jobtransition'),
]

# Corner share widget — anchored inside tool header (not floating)
def corner_share_html(tool_label, tool_url_fragment):
    share_text_map = {
        'salary': 'Deep tax analysis & salary decoder for FY 2025-26 — by Quantum Step',
        'homeloan': 'Calculate your Home Loan EMI, prepayment impact & interest breakup — by Quantum Step',
        'artha': 'Plan your wealth with SIP, SWP & compound growth projections — by Quantum Step',
        'jobtransition': 'Financially plan your job transition with this free calculator — by Quantum Step',
    }
    share_text = share_text_map.get(tool_url_fragment, 'Discover free financial tools by Quantum Step')
    
    return f"""
    <!-- Share Icons (Top Corner) -->
    <div id="tool-share-corner" style="position:fixed;top:120px;right:1.5rem;z-index:500;display:flex;flex-direction:column;gap:.5rem;align-items:center;">
        <span style="font-size:.6rem;color:#475569;text-transform:uppercase;letter-spacing:.08em;font-weight:700;writing-mode:vertical-rl;margin-bottom:.25rem;">Share</span>
        <button title="Share on WhatsApp" onclick="(function(){{const u=encodeURIComponent(window.location.href),t=encodeURIComponent('{share_text}');window.open('https://wa.me/?text='+t+'%20'+u,'_blank')}})()" style="width:36px;height:36px;border-radius:50%;background:rgba(37,211,102,.12);border:1px solid rgba(37,211,102,.25);display:flex;align-items:center;justify-content:center;color:#25D166;cursor:pointer;transition:all .2s;" onmouseover="this.style.background='rgba(37,211,102,.25)';this.style.transform='scale(1.1)'" onmouseout="this.style.background='rgba(37,211,102,.12)';this.style.transform=''">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.348z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.085.54 4.043 1.481 5.749L.073 23.925l6.345-1.384A11.93 11.93 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 0 1-5.012-1.37l-.358-.213-3.747.817.848-3.651-.234-.372A9.818 9.818 0 1 1 12 21.818z"/></svg>
        </button>
        <button title="Share on LinkedIn" onclick="(function(){{const u=encodeURIComponent(window.location.href);window.open('https://www.linkedin.com/sharing/share-offsite/?url='+u,'_blank')}})()" style="width:36px;height:36px;border-radius:50%;background:rgba(10,102,194,.12);border:1px solid rgba(10,102,194,.25);display:flex;align-items:center;justify-content:center;color:#0A66C2;cursor:pointer;transition:all .2s;" onmouseover="this.style.background='rgba(10,102,194,.25)';this.style.transform='scale(1.1)'" onmouseout="this.style.background='rgba(10,102,194,.12)';this.style.transform=''">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zm2-3a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/></svg>
        </button>
        <button title="Share on X" onclick="(function(){{const u=encodeURIComponent(window.location.href),t=encodeURIComponent('{share_text}');window.open('https://twitter.com/intent/tweet?text='+t+'&url='+u,'_blank')}})()" style="width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;color:#e2e8f0;cursor:pointer;transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,.14)';this.style.transform='scale(1.1)'" onmouseout="this.style.background='rgba(255,255,255,.06)';this.style.transform=''">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.277 5.653zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </button>
        <button title="Share on Facebook" onclick="(function(){{const u=encodeURIComponent(window.location.href);window.open('https://www.facebook.com/sharer/sharer.php?u='+u,'_blank')}})()" style="width:36px;height:36px;border-radius:50%;background:rgba(24,119,242,.12);border:1px solid rgba(24,119,242,.25);display:flex;align-items:center;justify-content:center;color:#1877F2;cursor:pointer;transition:all .2s;" onmouseover="this.style.background='rgba(24,119,242,.25)';this.style.transform='scale(1.1)'" onmouseout="this.style.background='rgba(24,119,242,.12)';this.style.transform=''">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
        </button>
    </div>
"""

for fname, tid in tool_files:
    fpath = os.path.join(r'd:\Vibe Code\Quantum Step', fname)
    if not os.path.exists(fpath):
        print(f'NOT FOUND: {fname}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Link tool-shared.css (after styles.css link)
    if 'tool-shared.css' not in content:
        content = content.replace(
            '<link rel="stylesheet" href="styles.css">',
            '<link rel="stylesheet" href="styles.css">\n  <link rel="stylesheet" href="tool-shared.css">',
            1
        )
        print(f'  Linked tool-shared.css to {fname}')

    # 2. Remove ALL .share-bar floating elements and old inline share sections
    # Remove the inline glass-panel "Share this Tool" section at the bottom
    content = re.sub(
        r'\s*<!-- Share Section -->.*?</div>\s*</div>\s*</div>',
        '\n            </div>\n        </div>',
        content,
        count=1,
        flags=re.DOTALL
    )

    # Remove the old floating .share-bar div if injected by script
    content = re.sub(r'\s*<div class="share-bar"[^>]*>.*?</div>\s*', '\n', content, flags=re.DOTALL)

    # 3. Add corner share icons (fixed position) - only if not already there
    if 'tool-share-corner' not in content:
        share_html = corner_share_html('', tid)
        content = content.replace('<body>', '<body>' + share_html, 1)
        print(f'  Added corner share to {fname}')

    # 4. Remove the old Social Share Script (inline shareTool function) - keep export scripts
    content = re.sub(
        r'\s*<!-- Social Share Script -->\s*<script>.*?function shareTool.*?</script>',
        '',
        content,
        count=1,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Done: {fname}')


# =========================================================
# Fix services section — add min-height to service-image
# so SVG icons are always visible
# =========================================================
print('\nFixing service card CSS...')
with open(r'd:\Vibe Code\Quantum Step\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check if service-image has proper height
if '.service-image' in css:
    # Find and update service-image to ensure display works
    css = re.sub(
        r'(\.service-image\s*\{[^}]*?)(height:\s*[^;]+;)?([^}]*?\})',
        lambda m: m.group(0) if 'min-height' in m.group(0) else m.group(1) + 'min-height: 200px;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    overflow: hidden;\n' + m.group(3),
        css,
        count=1,
        flags=re.DOTALL
    )
else:
    css += """
/* Service Cards */
.service-image {
    min-height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.service-image svg {
    flex-shrink: 0;
}

.service-content {
    padding: 1.5rem;
}

.service-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: .5rem;
}

.service-list li {
    font-size: .875rem;
    color: var(--text-secondary, #94a3b8);
    padding-left: 1.25rem;
    position: relative;
}

.service-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--color-primary, #6366f1);
}
"""

with open(r'd:\Vibe Code\Quantum Step\styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Service CSS fixed')
print('\nAll done.')
