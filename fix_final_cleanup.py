import re

# Fix 1: Add complete service card CSS to styles.css
# Fix 2: Remove emojis from index.html contact items and footer
# Fix 3: Fix industry icons section id for nav link

# ======================== CSS FIX ========================
with open(r'd:\Vibe Code\Quantum Step\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

service_css = """
/* ============================================================
   Services Section
   ============================================================ */
.services-section {
    padding: var(--spacing-3xl, 5rem) 0;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 2.5rem;
}

.service-card {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 1.5rem;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.service-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    border-color: rgba(99, 102, 241, 0.25);
}

.service-image {
    min-height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    overflow: hidden;
}

.service-image svg {
    flex-shrink: 0;
    filter: drop-shadow(0 0 20px currentColor);
    opacity: 0.85;
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.service-card:hover .service-image svg {
    opacity: 1;
    transform: scale(1.05);
}

.service-content {
    padding: 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.service-content h3 {
    font-size: 1rem;
    font-weight: 700;
    color: #f1f5f9;
    margin: 0 0 0.75rem;
    letter-spacing: -0.01em;
}

.service-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.service-list li {
    font-size: 0.82rem;
    color: #94a3b8;
    padding-left: 1.1rem;
    position: relative;
    line-height: 1.4;
}

.service-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 7px;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #6366f1;
}
"""

if '.service-card' not in css:
    css += service_css
    print('Service card CSS added')
else:
    # Update existing to ensure min-height is set
    css = re.sub(
        r'(\.service-image\s*\{)([^}]*?)(\})',
        lambda m: m.group(1) + '\n    min-height: 180px;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    padding: 2rem;\n    overflow: hidden;\n' + m.group(3),
        css, count=1, flags=re.DOTALL
    ) if 'min-height' not in css[css.find('.service-image'):css.find('.service-image')+200] else css
    print('Service card CSS updated')

with open(r'd:\Vibe Code\Quantum Step\styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# ======================== HTML FIXES ========================
with open(r'd:\Vibe Code\Quantum Step\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: Replace emoji contact icons with SVGs in contact section
html = html.replace(
    '<div class="contact-icon">📧</div>',
    '<div class="contact-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg></div>'
)
html = html.replace(
    '<div class="contact-icon">📱</div>',
    '<div class="contact-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/></svg></div>'
)
html = html.replace(
    '<div class="contact-icon">📍</div>',
    '<div class="contact-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></div>'
)

# Fix 2: Remove ❤️ emoji from footer (replace with SVG heart)
html = html.replace(
    'Crafted with ❤️',
    'Crafted with <svg width="13" height="13" viewBox="0 0 24 24" fill="#f43f5e" stroke="none" style="display:inline;vertical-align:middle;margin:0 .1rem;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'
)

# Fix 3: Add id="industries" to the industry icons section (for nav link)
html = html.replace(
    '<section class="industry-icons-section">',
    '<section id="industries" class="industry-icons-section">',
    1
)

# Fix 4: Ensure the engagement/why section does not break nav flow
# Check title tag update
print('HTML emoji replacements applied')
print(f'industries id set: {"id=\"industries\"" in html}')

with open(r'd:\Vibe Code\Quantum Step\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('All fixes applied. Done.')
