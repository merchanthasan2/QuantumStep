import re

with open(r'd:\Vibe Code\Quantum Step\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ===== Fix 1: Remove phone contact item, add WhatsApp =====
# Remove the entire phone contact-item (look for the SVG phone icon we added)
# Pattern: contact-item containing the phone SVG or "mobile" text
html = re.sub(
    r'<div class="contact-item">\s*<div class="contact-icon"><svg[^>]+>[^<]*<rect[^>]+x="5"[^>]+y="2"[^>]+width="14".*?</div>\s*</div>',
    '',
    html,
    count=1,
    flags=re.DOTALL
)

# Also try removing any plain phone number patterns
html = re.sub(r'<div class="contact-item">.*?\+\d[\d\s\-]+.*?</div>\s*</div>', '', html, count=2, flags=re.DOTALL)

# ===== Fix 2: Add WhatsApp contact item after email =====
whatsapp_item = '''
                <div class="contact-item">
                    <div class="contact-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.348z"/>
                            <path d="M12 0C5.373 0 0 5.373 0 12c0 2.085.54 4.043 1.481 5.749L.073 23.925l6.345-1.384A11.93 11.93 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 0 1-5.012-1.37l-.358-.213-3.747.817.848-3.651-.234-.372A9.818 9.818 0 1 1 12 21.818z"/>
                        </svg>
                    </div>
                    <div class="contact-details">
                        <div class="contact-label">WhatsApp</div>
                        <a href="https://wa.me/919821312220" target="_blank" class="contact-value" style="color:inherit;text-decoration:none;">+91 98213 12220</a>
                    </div>
                </div>'''

# Insert WhatsApp after the email contact item
html = re.sub(
    r'(info@quantumstep\.in.*?</div>\s*</div>)',
    r'\1' + whatsapp_item,
    html,
    count=1,
    flags=re.DOTALL
)

# ===== Fix 3: Rename "Job Transition Tracker" in tools grid =====
html = html.replace('Job\n                            Transition\n                            Tracker', 'Job Transition\n                            Calculator')
html = html.replace('>Job Transition Tracker<', '>Job Transition Calculator<')
html = html.replace('>Job\n                            Transition\n                            Tracker<', '>Job Transition\n                            Calculator<')

# Fix title in tool-job-transition.html too
print('Contacts updated, checking job transition label...')

with open(r'd:\Vibe Code\Quantum Step\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Also fix the title in the tool page
with open(r'd:\Vibe Code\Quantum Step\tool-job-transition.html', 'r', encoding='utf-8') as f:
    tjt = f.read()
tjt = tjt.replace('Job Transition Finance Tracker', 'Job Transition Financial Calculator')
tjt = tjt.replace('Job Transition Finance Tracker | Quantum Step', 'Job Transition Financial Calculator | Quantum Step')
with open(r'd:\Vibe Code\Quantum Step\tool-job-transition.html', 'w', encoding='utf-8') as f:
    f.write(tjt)

print('All contact + label fixes done.')
