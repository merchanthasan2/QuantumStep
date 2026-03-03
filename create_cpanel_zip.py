import zipfile, os, shutil

src = r'd:\Vibe Code\Quantum Step'
zip_path = r'd:\Vibe Code\Quantum Step\quantum-step-cpanel.zip'

# Files to include in cPanel upload
include_extensions = {'.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.svg', '.ico', '.webp', '.woff', '.woff2', '.ttf'}

# Specific top-level files to include
include_files = [
    'index.html',
    'tool-salary-calculator.html',
    'tool-home-loan-calculator.html',
    'tool-artha-wealth.html',
    'tool-job-transition.html',
    'tool-buy-vs-rent.html',
    'admin-dashboard.html',
    'styles.css',
    'tool-shared.css',
    'script.js',
    'analytics.js',
    'logo-dark.png',
    'logo-light.png',
    'service_mobile_1765273855228.png',
    'site-config.json',
]

# Exclude patterns
exclude_dirs = {'node_modules', '.git', 'dist', 'Docs', '__pycache__', '.gemini', '.vscode'}
exclude_ext = {'.py', '.md', '.lock'}

if os.path.exists(zip_path):
    os.remove(zip_path)

added = []
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
    for fname in include_files:
        fp = os.path.join(src, fname)
        if os.path.exists(fp):
            zf.write(fp, fname)
            added.append(fname)
        else:
            print(f'MISSING: {fname}')

size_mb = os.path.getsize(zip_path) / (1024*1024)
print(f'\nCreated: quantum-step-cpanel.zip ({size_mb:.2f} MB)')
print(f'Files included: {len(added)}')
for f in added:
    print(f'  + {f}')
print('\nInstructions:')
print('  1. Login to cPanel > File Manager')
print('  2. Navigate to public_html/') 
print('  3. Click Upload > upload quantum-step-cpanel.zip')
print('  4. Right-click the zip > Extract')
print('  5. Done!')
