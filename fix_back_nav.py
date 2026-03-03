import os
import re

tool_files = [
    'tool-salary-calculator.html',
    'tool-home-loan-calculator.html',
    'tool-artha-wealth.html',
    'tool-job-transition.html',
]

back_link = '''
            <a href="index.html" style="display:inline-flex;align-items:center;gap:.4rem;padding:.4rem .9rem;border-radius:999px;font-size:.78rem;font-weight:600;text-decoration:none;background:rgba(255,255,255,.05);color:#94a3b8;border:1px solid rgba(255,255,255,.1);transition:all .2s;margin-right:.5rem;" onmouseover="this.style.color=\'#f1f5f9\';this.style.background=\'rgba(255,255,255,.1)\'" onmouseout="this.style.color=\'#94a3b8\';this.style.background=\'rgba(255,255,255,.05)\'">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
                quantumstep.in
            </a>'''

for fname in tool_files:
    fpath = os.path.join(r'd:\Vibe Code\Quantum Step', fname)
    if not os.path.exists(fpath):
        print(f'NOT FOUND: {fname}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the logo href to also point back to index.html
    content = re.sub(
        r'(<a[^>]+class="[^"]*logo[^"]*"[^>]+href=")[^"]*(")',
        r'\1index.html\2',
        content, count=1
    )

    # Add "← quantumstep.in" at the START of the tool switcher div
    # Find the Tool Navigation Bar div content
    old_switchlabel = '<span style="color:#64748b;font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-right:.25rem;">Switch Tool</span>'
    new_switchlabel = back_link + '\n            <span style="color:#344e70;font-size:.7rem;margin:0 .25rem;">|</span>\n            <span style="color:#64748b;font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-right:.25rem;">Switch Tool</span>'
    
    if 'quantumstep.in' not in content:
        content = content.replace(old_switchlabel, new_switchlabel, 1)
        print(f'  Back link added to {fname}')
    else:
        print(f'  Back link already exists in {fname}')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Done: {fname}')

print('\nAll tool pages updated.')
