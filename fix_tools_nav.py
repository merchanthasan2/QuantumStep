import re
import os

# =====================================
# Fix 1: Fix floating social share bar in ALL tool pages
# The floating bar overlaps the local "Share this Tool" section.
# Solution: In CSS, hide the floating share-bar on tool pages.
# We add a data-page="tool" attribute to the body and hide .share-bar.
# =====================================

tool_files = [
    r'd:\Vibe Code\Quantum Step\tool-artha-wealth.html',
    r'd:\Vibe Code\Quantum Step\tool-home-loan-calculator.html',
    r'd:\Vibe Code\Quantum Step\tool-salary-calculator.html',
    r'd:\Vibe Code\Quantum Step\tool-job-transition.html',
]

for fpath in tool_files:
    if not os.path.exists(fpath):
        print(f'NOT FOUND: {fpath}')
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find share-bar divs and remove them from tool pages (they have their own share section)
    # The floating share-bar was added by script.js, which is only loaded on index.html
    # But if there's an inline share-bar in the tool pages, remove it.
    # More importantly: add CSS to hide floating bars per-tool and add tool navigation.

    # Check if already has tool nav
    if 'tool-nav-bar' in content:
        print(f'Already has tool nav: {os.path.basename(fpath)}')
    
    # Get the tool name from the file
    fname = os.path.basename(fpath)
    if 'artha-wealth' in fname:
        current_tool = 'artha'
        tool_title = 'ArthaWealth Calculator'
    elif 'home-loan' in fname:
        current_tool = 'homeloan'
        tool_title = 'Home Loan Calculator'
    elif 'salary' in fname:
        current_tool = 'salary'
        tool_title = 'Salary Decoder'
    elif 'job-transition' in fname:
        current_tool = 'jobtransition'
        tool_title = 'Job Transition Tracker'
    else:
        current_tool = 'unknown'
        tool_title = 'Tool'

    # Build tool switcher bar (appears just below the existing nav)
    # Define all 4 tools
    tools = [
        ('tool-salary-calculator.html', '💰', 'Salary Decoder', 'salary'),
        ('tool-home-loan-calculator.html', '🏠', 'Home Loan', 'homeloan'),
        ('tool-artha-wealth.html', '📈', 'ArthaWealth', 'artha'),
        ('tool-job-transition.html', '💼', 'Job Tracker', 'jobtransition'),
    ]

    tool_nav_html = '''
    <!-- Tool Navigation Bar -->
    <div style="background:rgba(15,23,42,0.95);border-bottom:1px solid rgba(255,255,255,0.06);padding:.6rem 0;position:sticky;top:70px;z-index:90;backdrop-filter:blur(20px);">
        <div style="max-width:1200px;margin:0 auto;padding:0 1.5rem;display:flex;align-items:center;gap:.5rem;justify-content:center;flex-wrap:wrap;">
            <span style="color:#64748b;font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;margin-right:.5rem;">Switch Tool:</span>'''

    for href, icon, label, tid in tools:
        is_active = (tid == current_tool)
        if is_active:
            style = "display:inline-flex;align-items:center;gap:.4rem;padding:.4rem 1rem;border-radius:999px;font-size:.8rem;font-weight:700;text-decoration:none;background:linear-gradient(135deg,#6366f1,#4f46e5);color:white;border:1px solid rgba(99,102,241,.5);"
        else:
            style = "display:inline-flex;align-items:center;gap:.4rem;padding:.4rem 1rem;border-radius:999px;font-size:.8rem;font-weight:600;text-decoration:none;background:rgba(255,255,255,.04);color:#94a3b8;border:1px solid rgba(255,255,255,.08);transition:all .2s;"
        hover_attr = '' if is_active else ' onmouseover="this.style.background=\'rgba(99,102,241,.1)\';this.style.color=\'#a5b4fc\'" onmouseout="this.style.background=\'rgba(255,255,255,.04)\';this.style.color=\'#94a3b8\'"'
        tool_nav_html += f'\n            <a href="{href}"{hover_attr} style="{style}">{icon} {label}</a>'

    tool_nav_html += '''
        </div>
    </div>
'''

    # Find the share-bar div and fix it: Make the local share buttons visible, hide the floating global one
    # The floating share-bar is injected by script.js (only included in index.html)
    # But some tool pages include it. Let's also ensure the share bar overlap is fixed in CSS.
    
    # Add inline CSS to hide any .share-bar floating element on tool pages
    hide_sharebar_css = '''
    <style>
        /* Hide floating share bar - use inline share section instead */
        .share-bar { display: none !important; }
    </style>
    '''
    
    # Check if the style tag already exists
    if '/* Hide floating share bar' not in content:
        content = content.replace('</head>', hide_sharebar_css + '</head>', 1)
        print(f'  Added share-bar hide CSS to {os.path.basename(fpath)}')

    # Insert tool nav after the </nav> tag in the header
    # Most tool pages have a <nav> element, find it and insert after
    if 'tool-nav-bar' not in content and '<!-- Tool Navigation Bar -->' not in content:
        # Insert after the first </nav>
        content = content.replace('</nav>', '</nav>' + tool_nav_html, 1)
        print(f'  Added tool nav to {os.path.basename(fpath)}')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed: {os.path.basename(fpath)}')


# =====================================
# Fix 2: Reorder sections in index.html
# Move: Metrics, Industry Excellence, Growth Segments, FAQ
# FROM: after Portfolio → BEFORE: Portfolio
# New order: Services → Ecosystem → Industry Icons → Metrics → Industry Excellence → Growth → FAQ → Tools → Portfolio → Contact
# =====================================

print('\nReordering homepage sections...')

with open(r'd:\Vibe Code\Quantum Step\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract named sections using regex
def extract_section(html, start_comment, end_section='</section>'):
    """Extract a section by its HTML comment marker"""
    idx = html.find(start_comment)
    if idx == -1:
        return None, html
    # Find closing </section>
    close_idx = html.find(end_section, idx)
    if close_idx == -1:
        return None, html
    close_idx += len(end_section)
    section = html[idx:close_idx]
    remaining = html[:idx] + html[close_idx:]
    return section, remaining

metrics_section, content = extract_section(content, '<!-- Arsenal Metrics Section -->')
industry_section, content = extract_section(content, '<!-- Industry Excellence Section -->')
growth_section, content = extract_section(content, '<!-- Growth Segments Section -->')
faq_section, content = extract_section(content, '<!-- FAQ Section -->')

print(f'Extracted: metrics={bool(metrics_section)}, industry={bool(industry_section)}, growth={bool(growth_section)}, faq={bool(faq_section)}')

# Now insert them before portfolio section
if all([metrics_section, industry_section, growth_section, faq_section]):
    insert_block = '\n' + metrics_section + '\n\n' + industry_section + '\n\n' + growth_section + '\n\n' + faq_section + '\n\n'
    content = content.replace('    <!-- Portfolio / Clients Section -->', insert_block + '    <!-- Portfolio / Clients Section -->', 1)
    print('Sections reordered: Metrics/Industry/Growth/FAQ now appear before Portfolio')
else:
    print('Warning: Some sections were not found, skipping reorder')

with open(r'd:\Vibe Code\Quantum Step\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone - all fixes applied.')
