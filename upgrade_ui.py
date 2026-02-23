import re

with open('d:\\Vibe Code\\Quantum Step\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure absolutely no `#fff`, `#ffffff` or `white` strings exist in styling
html = re.sub(r'#ffffff', '#e2e8f0', html, flags=re.IGNORECASE)
html = re.sub(r'#fff', '#e2e8f0', html, flags=re.IGNORECASE)
html = re.sub(r'color:\s*white', 'color:#f8fafc', html, flags=re.IGNORECASE)
html = re.sub(r'rgba?\(255,\s*255,\s*255', 'rgba(241, 245, 249', html, flags=re.IGNORECASE)

# BETTER ICONS
salary_svg = '''
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <rect x="2" y="6" width="20" height="12" rx="2"></rect>
    <circle cx="12" cy="12" r="2"></circle>
    <path d="M6 12h.01M18 12h.01"></path>
</svg>
'''

wealth_svg = '''
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <line x1="12" y1="20" x2="12" y2="10"></line>
    <line x1="18" y1="20" x2="18" y2="4"></line>
    <line x1="6" y1="20" x2="6" y2="16"></line>
    <polyline points="4 14 10 9 15 13 21 6"></polyline>
</svg>
'''

home_svg = '''
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
    <polyline points="9 22 9 12 15 12 15 22"></polyline>
</svg>
'''

html = html.replace('💰', salary_svg)
html = html.replace('📈', wealth_svg)
html = html.replace('🏠', home_svg)

with open('d:\\Vibe Code\\Quantum Step\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated icons and strictly removed white from HTML inline styles.")
