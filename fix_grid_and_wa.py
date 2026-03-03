import re

with open(r'd:\Vibe Code\Quantum Step\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ===== FIX 1: Tools grid — replace inline grid style to 3-col max =====
# The tools section uses a div with grid style inline
# Change auto-fit to max 3 cols for 5-tool 3+2 layout
html = re.sub(
    r'(class="tools-grid"[^>]*style=")[^"]*(")',
    r'\1display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;\2',
    html, count=1
)
# Also try without inline style on the grid div
if 'tools-grid' in html:
    print('tools-grid found')
else:
    print('tools-grid NOT found, checking for inline grid in tools section')

# Fix via styles.css too
with open(r'd:\Vibe Code\Quantum Step\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Patch tool card grid if defined in CSS
if '.tools-grid' in css:
    css = re.sub(
        r'(\.tools-grid\s*\{[^}]*grid-template-columns\s*:)[^;]+;',
        r'\1 repeat(3, 1fr);',
        css, count=1
    )
    print('Patched .tools-grid in CSS')
else:
    # Add it as new rule at end
    css += """
/* Tools grid — 3 columns max for balanced layout */
.tools-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 1.5rem;
}

@media (max-width: 900px) {
    .tools-grid { grid-template-columns: repeat(2, 1fr) !important; }
}

@media (max-width: 580px) {
    .tools-grid { grid-template-columns: 1fr !important; }
}

/* Make the 5th card span fully so it looks intentional on row 2 */
.tools-grid .tool-card:nth-child(4),
.tools-grid .tool-card:last-child:nth-child(5) {
    /* Keep default */
}
"""
    print('Added .tools-grid CSS rule')

# Also patch the inline style on the tools grid div
html = re.sub(
    r'(<div[^>]+class="tools-grid"[^>]*>)',
    lambda m: re.sub(r'style="[^"]*"', '', m.group(0)) if 'style' in m.group(0) else m.group(0),
    html, count=1
)

with open(r'd:\Vibe Code\Quantum Step\styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# ===== FIX 2: WhatsApp prominent CTA in contact section =====
WA_CTA = '''
                    <!-- WhatsApp CTA -->
                    <a href="https://wa.me/919821312220?text=Hi%20Quantum%20Step!%20I%20found%20your%20website%20and%20would%20like%20to%20discuss%20a%20project." 
                        target="_blank" rel="noopener noreferrer"
                        style="display:flex;align-items:center;gap:1rem;padding:1.25rem 1.5rem;background:linear-gradient(135deg,rgba(37,211,102,.15),rgba(37,211,102,.08));border:1px solid rgba(37,211,102,.3);border-radius:1.25rem;text-decoration:none;margin-top:1.5rem;transition:all .25s;group;"
                        onmouseover="this.style.background='linear-gradient(135deg,rgba(37,211,102,.25),rgba(37,211,102,.15))';this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 24px rgba(37,211,102,.15)'"
                        onmouseout="this.style.background='linear-gradient(135deg,rgba(37,211,102,.15),rgba(37,211,102,.08))';this.style.transform='';this.style.boxShadow=''">
                        <div style="width:48px;height:48px;border-radius:50%;background:rgba(37,211,102,.15);border:1px solid rgba(37,211,102,.3);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="#25D166">
                                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.348z"/>
                                <path d="M12 0C5.373 0 0 5.373 0 12c0 2.085.54 4.043 1.481 5.749L.073 23.925l6.345-1.384A11.93 11.93 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 0 1-5.012-1.37l-.358-.213-3.747.817.848-3.651-.234-.372A9.818 9.818 0 1 1 12 21.818z"/>
                            </svg>
                        </div>
                        <div>
                            <div style="font-size:.7rem;font-weight:700;color:#25D166;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.2rem;">Talk to us now</div>
                            <div style="font-size:1rem;font-weight:700;color:#f1f5f9;">Chat on WhatsApp</div>
                            <div style="font-size:.78rem;color:#64748b;margin-top:.1rem;">+91 98213 12220 · Typically replies in minutes</div>
                        </div>
                        <div style="margin-left:auto;color:#25D166;">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                        </div>
                    </a>'''

# Insert AFTER the contact-info closing div (before </div> of contact-info wrapper)
# Find the location of contact-info div end
html = html.replace(
    '<div class="contact-info">',
    '<div class="contact-info">' + WA_CTA,
    1
)

with open(r'd:\Vibe Code\Quantum Step\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('All fixes applied.')
