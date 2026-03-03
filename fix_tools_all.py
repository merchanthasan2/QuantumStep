import re
import os

# =========================================================
# Clean SVG icons — NO emojis anywhere
# =========================================================

ICON_SALARY = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>'
ICON_HOMELOAN = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
ICON_ARTHA = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>'
ICON_JOB = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><line x1="12" y1="12" x2="12" y2="16"/><line x1="10" y1="14" x2="14" y2="14"/></svg>'

tools = [
    ('tool-salary-calculator.html', 'salary', 'Salary Decoder', ICON_SALARY),
    ('tool-home-loan-calculator.html', 'homeloan', 'Home Loan', ICON_HOMELOAN),
    ('tool-artha-wealth.html', 'artha', 'ArthaWealth', ICON_ARTHA),
    ('tool-job-transition.html', 'jobtransition', 'Job Transition', ICON_JOB),
]

def build_tool_nav(current_tid):
    nav = '\n    <!-- Tool Navigation Bar -->\n    <div style="background:rgba(15,23,42,0.95);border-bottom:1px solid rgba(255,255,255,0.06);padding:.6rem 0;position:sticky;top:70px;z-index:90;backdrop-filter:blur(20px);">\n        <div style="max-width:1200px;margin:0 auto;padding:0 1.5rem;display:flex;align-items:center;gap:.5rem;justify-content:center;flex-wrap:wrap;">\n            <span style="color:#64748b;font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-right:.25rem;">Switch Tool</span>'
    for href, tid, label, icon in tools:
        is_active = (tid == current_tid)
        if is_active:
            style = 'display:inline-flex;align-items:center;gap:.4rem;padding:.4rem 1rem;border-radius:999px;font-size:.8rem;font-weight:700;text-decoration:none;background:linear-gradient(135deg,#6366f1,#4f46e5);color:white;border:1px solid rgba(99,102,241,.5);'
            nav += f'\n            <a href="{href}" style="{style}">{icon} {label}</a>'
        else:
            style = 'display:inline-flex;align-items:center;gap:.4rem;padding:.4rem 1rem;border-radius:999px;font-size:.8rem;font-weight:600;text-decoration:none;background:rgba(255,255,255,.04);color:#94a3b8;border:1px solid rgba(255,255,255,.08);transition:all .2s;'
            hover = f'onmouseover="this.style.background=\'rgba(99,102,241,.1)\';this.style.color=\'#a5b4fc\'" onmouseout="this.style.background=\'rgba(255,255,255,.04)\';this.style.color=\'#94a3b8\'"'
            nav += f'\n            <a href="{href}" {hover} style="{style}">{icon} {label}</a>'
    nav += '\n        </div>\n    </div>\n'
    return nav

EXPORT_LIBRARY_SCRIPTS = """
    <!-- Export Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script>
        function exportToExcel() {
            const exportData = window.getExportData ? window.getExportData() : null;
            if (!exportData) { alert('Calculate results first.'); return; }
            const wb = XLSX.utils.book_new();
            const ws = XLSX.utils.aoa_to_sheet(exportData.rows);
            XLSX.utils.book_append_sheet(wb, ws, exportData.sheetName || 'Results');
            XLSX.writeFile(wb, exportData.fileName || 'QuantumStep_Export.xlsx');
        }
        async function exportToPDF() {
            const { jsPDF } = window.jspdf;
            const target = document.getElementById('results-section') || document.getElementById('export-target') || document.querySelector('.glass-panel');
            if (!target) { alert('Calculate results first.'); return; }
            const btn = document.getElementById('pdf-export-btn');
            if (btn) { btn.disabled = true; btn.textContent = 'Generating...'; }
            const canvas = await html2canvas(target, { scale: 2, backgroundColor: '#0f172a', useCORS: true });
            const imgData = canvas.toDataURL('image/png');
            const pdf = new jsPDF({ orientation: 'landscape', unit: 'px', format: [canvas.width/2, canvas.height/2] });
            pdf.addImage(imgData, 'PNG', 0, 0, canvas.width/2, canvas.height/2);
            const fname = window.getExportData ? (window.getExportData().fileName || 'QS').replace('.xlsx','')+'.pdf' : 'QuantumStep.pdf';
            pdf.save(fname);
            if (btn) { btn.disabled = false; btn.innerHTML = btn._origHTML || 'Export PDF'; }
        }
    </script>
"""

EXPORT_BUTTONS = """
                <!-- Export Panel -->
                <div style="display:flex;align-items:center;gap:.75rem;flex-wrap:wrap;margin-top:1.5rem;padding:1rem 1.5rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:1rem;">
                    <span style="display:flex;align-items:center;gap:.4rem;color:#94a3b8;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                        Export
                    </span>
                    <button onclick="exportToExcel()" style="display:inline-flex;align-items:center;gap:.45rem;padding:.5rem 1.1rem;background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.25);border-radius:.65rem;color:#34d399;font-size:.82rem;font-weight:600;cursor:pointer;transition:all .2s;font-family:inherit;" onmouseover="this.style.background='rgba(16,185,129,.2)'" onmouseout="this.style.background='rgba(16,185,129,.1)'">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                        Excel
                    </button>
                    <button id="pdf-export-btn" onclick="exportToPDF()" style="display:inline-flex;align-items:center;gap:.45rem;padding:.5rem 1.1rem;background:rgba(244,63,94,.1);border:1px solid rgba(244,63,94,.25);border-radius:.65rem;color:#fb7185;font-size:.82rem;font-weight:600;cursor:pointer;transition:all .2s;font-family:inherit;" onmouseover="this.style.background='rgba(244,63,94,.2)'" onmouseout="this.style.background='rgba(244,63,94,.1)'">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><path d="M9 13h6M9 17h4"/></svg>
                        PDF
                    </button>
                </div>
"""

SHARE_SECTION = """                <!-- Share Section -->
                <div class="glass-panel rounded-2xl p-6 mt-4">
                    <h3 class="font-semibold text-gray-300 mb-4" style="display:flex;align-items:center;gap:.5rem;">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>
                        Share this Tool
                    </h3>
                    <div class="flex gap-3 flex-wrap">
                        <button onclick="shareTool('whatsapp')"
                            class="flex items-center gap-2 px-4 py-2 bg-[#25D366]/20 text-[#25D366] rounded-lg hover:bg-[#25D366]/30 transition-colors font-medium text-sm border border-[#25D366]/30">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.348z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.085.54 4.043 1.481 5.749L.073 23.925l6.345-1.384A11.93 11.93 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 0 1-5.012-1.37l-.358-.213-3.747.817.848-3.651-.234-.372A9.818 9.818 0 1 1 12 21.818z"/></svg>
                            WhatsApp
                        </button>
                        <button onclick="shareTool('linkedin')"
                            class="flex items-center gap-2 px-4 py-2 bg-[#0A66C2]/20 text-[#0A66C2] rounded-lg hover:bg-[#0A66C2]/30 transition-colors font-medium text-sm border border-[#0A66C2]/30">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zm2-3a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/></svg>
                            LinkedIn
                        </button>
                        <button onclick="shareTool('facebook')"
                            class="flex items-center gap-2 px-4 py-2 bg-[#1877F2]/20 text-[#1877F2] rounded-lg hover:bg-[#1877F2]/30 transition-colors font-medium text-sm border border-[#1877F2]/30">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
                            Facebook
                        </button>
                        <button onclick="shareTool('twitter')"
                            class="flex items-center gap-2 px-4 py-2 bg-[#1DA1F2]/20 text-[#1DA1F2] rounded-lg hover:bg-[#1DA1F2]/30 transition-colors font-medium text-sm border border-[#1DA1F2]/30">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.277 5.653zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                            X / Twitter
                        </button>
                    </div>
                </div>"""

tool_configs = [
    {
        'file': r'd:\Vibe Code\Quantum Step\tool-artha-wealth.html',
        'tid': 'artha',
        'export_sheet': 'ArthaWealth',
        'export_file': 'ArthaWealth_Calculator.xlsx',
    },
    {
        'file': r'd:\Vibe Code\Quantum Step\tool-home-loan-calculator.html',
        'tid': 'homeloan',
        'export_sheet': 'HomeLoan',
        'export_file': 'HomeLoan_Calculator.xlsx',
    },
    {
        'file': r'd:\Vibe Code\Quantum Step\tool-salary-calculator.html',
        'tid': 'salary',
        'export_sheet': 'SalaryDecoder',
        'export_file': 'Salary_Decoder.xlsx',
    },
    {
        'file': r'd:\Vibe Code\Quantum Step\tool-job-transition.html',
        'tid': 'jobtransition',
        'export_sheet': 'JobTransition',
        'export_file': 'Job_Transition_Calculator.xlsx',
    },
]

for cfg in tool_configs:
    fpath = cfg['file']
    if not os.path.exists(fpath):
        print(f'NOT FOUND: {fpath}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Remove old tool nav (any variant) ---
    # Remove everything between <!-- Tool Navigation Bar --> ... end of its wrapping div
    old_nav_pattern = r'\n    <!-- Tool Navigation Bar -->.*?</div>\n'
    content = re.sub(old_nav_pattern, '\n', content, flags=re.DOTALL)

    # --- Insert fresh tool nav (SVG icons, no emojis) ---
    new_nav = build_tool_nav(cfg['tid'])
    content = content.replace('</nav>', '</nav>' + new_nav, 1)

    # --- Replace share section ---
    old_share_pattern = r'                <!-- Share Section -->.*?</div>\s*</div>'
    content = re.sub(old_share_pattern, SHARE_SECTION, content, flags=re.DOTALL, count=1)

    # --- Remove old export panel if any (to avoid duplicates) ---
    old_export_pattern = r'    <!-- Export Libraries -->.*?</script>\n'
    content = re.sub(old_export_pattern, '', content, count=1, flags=re.DOTALL)
    old_export_panel_pattern = r'    <!-- Export Panel Scripts -->.*?</script>\n'
    content = re.sub(old_export_panel_pattern, '', content, count=1, flags=re.DOTALL)
    old_export_buttons_pattern = r'                <!-- Export Panel -->.*?</div>\n'
    content = re.sub(old_export_buttons_pattern, '', content, count=1, flags=re.DOTALL)

    # --- Inject export buttons before share section ---
    content = content.replace('                <!-- Share Section -->', EXPORT_BUTTONS + '\n                <!-- Share Section -->', 1)

    # --- Add export data getter + libraries before </body> ---
    export_data_script = f"""
    <script>
        if (typeof window.getExportData === 'undefined') {{
            window.getExportData = function() {{
                const rows = [['Quantum Step Creations - {cfg["export_sheet"]} Report'], ['Generated: ' + new Date().toLocaleDateString('en-IN')], ['']];
                document.querySelectorAll('table').forEach(table => {{
                    const headers = [];
                    table.querySelectorAll('thead th').forEach(th => headers.push(th.textContent.trim()));
                    if (headers.length) rows.push(headers);
                    table.querySelectorAll('tbody tr').forEach(tr => {{
                        const row = [];
                        tr.querySelectorAll('td').forEach(td => row.push(td.textContent.trim()));
                        if (row.some(c => c)) rows.push(row);
                    }});
                    rows.push([]);
                }});
                return {{ rows, sheetName: '{cfg["export_sheet"]}', fileName: '{cfg["export_file"]}' }};
            }};
        }}
    </script>
"""
    content = content.replace('</body>', export_data_script + EXPORT_LIBRARY_SCRIPTS + '</body>', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Done: {os.path.basename(fpath)}')

# --- Styles.css: nav CTA btn + industry icon grid CSS ---
with open(r'd:\Vibe Code\Quantum Step\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

additions = ""
if '.nav-cta-btn' not in css:
    additions += """
.nav-cta-btn {
    display: inline-flex;
    align-items: center;
    padding: .45rem 1.1rem;
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    color: #fff !important;
    border-radius: 999px;
    font-size: .85rem;
    font-weight: 700;
    text-decoration: none;
    transition: all var(--transition-base);
    box-shadow: 0 0 16px rgba(99,102,241,.3);
    letter-spacing: .02em;
}
.nav-cta-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 20px rgba(99,102,241,.5);
    background: linear-gradient(135deg, #818cf8, #6366f1);
}
"""

if '.industry-icons-section' not in css:
    additions += """
.industry-icons-section {
    padding: var(--spacing-3xl) 0;
    background: var(--bg-darker);
    border-top: 1px solid rgba(255,255,255,.04);
    border-bottom: 1px solid rgba(255,255,255,.04);
}
.industry-icons-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 1.5rem;
    margin-top: 2.5rem;
}
.industry-icon-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: .75rem;
    text-align: center;
}
.industry-icon-wrap {
    width: 72px;
    height: 72px;
    border-radius: 1.25rem;
    border: 1px solid rgba(255,255,255,.08);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all var(--transition-base);
}
.industry-icon-item:hover .industry-icon-wrap {
    transform: translateY(-5px);
    box-shadow: 0 8px 24px rgba(99,102,241,.15);
}
.industry-icon-item span {
    font-size: .8rem;
    font-weight: 600;
    color: var(--text-secondary);
    line-height: 1.3;
}
"""

if additions:
    css += additions
    with open(r'd:\Vibe Code\Quantum Step\styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print('CSS additions applied')

print('\nAll done.')
