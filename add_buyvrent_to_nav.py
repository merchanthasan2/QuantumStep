import re

with open(r'd:\Vibe Code\Quantum Step\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Buy vs Rent to the tools grid in index.html
new_tool_card = '''
                <a href="tool-buy-vs-rent.html" class="tool-card fade-in" style="text-decoration:none;">
                    <div class="tool-icon"
                        style="background:rgba(56,189,248,0.1); color:#38bdf8; border-color:rgba(56,189,248,0.2);">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                            <line x1="12" y1="22" x2="12" y2="12"/>
                        </svg>
                    </div>
                    <div
                        style="font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:#38bdf8; margin-bottom:0.5rem;">
                        Real Estate · Finance</div>
                    <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0.5rem;">Buy vs Rent
                        Calculator</h3>
                    <p style="color:#94a3b8; line-height:1.6; flex-grow:1; margin-bottom:1.5rem;">Should you buy or keep renting?
                        Compare true cost of home ownership vs renting with opportunity cost analysis for Indian professionals.</p>
                    <div
                        style="font-weight:700; font-size:0.95rem; margin-top:auto; display:flex; align-items:center; gap:8px; background:linear-gradient(135deg,#38bdf8,#818cf8); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
                        Open Tool <span style="font-size:1.2rem;">&rarr;</span>
                    </div>
                </a>'''

# Insert before the closing of the tools grid div
html = html.replace(
    '''            <div
                style="text-align:center; color:var(--text-muted); font-size:0.85rem; margin-top:3rem; letter-spacing:0.05em;">
                Premium Tools &bull; Built &amp; maintained by Quantum Step Creations
            </div>''',
    new_tool_card + '''
            <div
                style="text-align:center; color:var(--text-muted); font-size:0.85rem; margin-top:3rem; letter-spacing:0.05em;">
                Premium Tools &bull; Built &amp; maintained by Quantum Step Creations
            </div>'''
)

with open(r'd:\Vibe Code\Quantum Step\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update tool nav in all 4 existing tools to include the 5th
BVR_LINK = '''
            <a href="tool-buy-vs-rent.html" onmouseover="this.style.background='rgba(99,102,241,.1)';this.style.color='#a5b4fc'" onmouseout="this.style.background='rgba(255,255,255,.04)';this.style.color='#94a3b8'" style="display:inline-flex;align-items:center;gap:.4rem;padding:.4rem 1rem;border-radius:999px;font-size:.8rem;font-weight:600;text-decoration:none;background:rgba(255,255,255,.04);color:#94a3b8;border:1px solid rgba(255,255,255,.08);transition:all .2s;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><line x1="12" y1="22" x2="12" y2="12"/></svg> Buy vs Rent
            </a>'''

tool_files = [
    'tool-salary-calculator.html',
    'tool-home-loan-calculator.html',
    'tool-artha-wealth.html',
    'tool-job-transition.html',
]

for fname in tool_files:
    fpath = rf'd:\Vibe Code\Quantum Step\{fname}'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'tool-buy-vs-rent.html' not in c:
        # Add before closing </div> of the tool nav
        c = c.replace(
            '\n        </div>\n    </div>\n',
            BVR_LINK + '\n        </div>\n    </div>\n',
            1
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'  Added Buy vs Rent link to {fname}')
    else:
        print(f'  Already has link: {fname}')

print('Done.')
