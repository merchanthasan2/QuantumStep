import re

with open('d:\\Vibe Code\\Quantum Step\\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hex whites
css = re.sub(r'#ffffff', '#f8fafc', css, flags=re.IGNORECASE)
css = re.sub(r'#fff', '#f8fafc', css, flags=re.IGNORECASE)

# Replace pure white rgb/rgba
css = re.sub(r'rgba?\(255,\s*255,\s*255', 'rgba(248, 250, 252', css)

# Replace 'white' keyword where appropriate (not in comments if possible, but safe enough here)
css = re.sub(r':\s*white\s*;', ': var(--text-primary);', css, flags=re.IGNORECASE)

with open('d:\\Vibe Code\\Quantum Step\\styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS whites replaced")
