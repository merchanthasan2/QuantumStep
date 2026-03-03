import os

with open('tool-home-loan-calculator.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to insert the Amortization component right after the <!-- Action Button --> div
target_str = """<!-- Action Button -->
                <div class="flex justify-end pt-4">
                    <button class="bg-indigo-600 hover:bg-indigo-500 text-white px-5 py-3 rounded-lg font-bold shadow-lg shadow-indigo-600/20 transition-all flex items-center gap-2">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                        Yearly EMI Breakdown
                    </button>
                </div>"""

new_button = """<!-- Action Button -->
                <div class="flex justify-end pt-4">
                    <button id="btn-show-amortization" class="bg-indigo-600 hover:bg-indigo-500 text-white px-5 py-3 rounded-lg font-bold shadow-lg shadow-indigo-600/20 transition-all flex items-center gap-2 outline-none">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                        Yearly EMI Breakdown
                    </button>
                </div>
                
                <!-- Amortization Modal / Section -->
                <div id="amortization-section" class="hidden glass-panel p-6 rounded-xl border border-gray-700 mt-8 mb-8 pb-4">
                    <div class="flex justify-between items-center mb-6">
                        <h3 class="text-xl font-bold text-white">Yearly Amortization Schedule</h3>
                        <button id="btn-hide-amortization" class="text-gray-400 hover:text-white px-3 py-1 bg-gray-800 rounded-md">✕ Close</button>
                    </div>
                    <div class="overflow-x-auto max-h-[400px] overflow-y-auto">
                        <table class="min-w-full text-left text-sm whitespace-nowrap">
                            <thead class="sticky top-0 bg-slate-800 text-gray-300">
                                <tr>
                                    <th class="px-4 py-3 font-semibold rounded-tl-lg">Year</th>
                                    <th class="px-4 py-3 font-semibold">Opening Balance</th>
                                    <th class="px-4 py-3 font-semibold">EMI Paid</th>
                                    <th class="px-4 py-3 font-semibold text-rose-400">Interest Paid</th>
                                    <th class="px-4 py-3 font-semibold text-emerald-400">Principal Paid</th>
                                    <th class="px-4 py-3 font-semibold rounded-tr-lg">Closing Balance</th>
                                </tr>
                            </thead>
                            <tbody id="amortization-tbody" class="divide-y divide-gray-700/50 block w-full mt-1">
                                <!-- JS populated -->
                            </tbody>
                        </table>
                    </div>
                </div>"""

logic_str = "            const renterWins = renterNetWealth > buyerNetWealth;"

new_logic = """            const renterWins = renterNetWealth > buyerNetWealth;

            // Compute Yearly Amortization Data
            let balance = loanAmount;
            
            // Get commencement year
            const commenceDateStr = document.getElementById('inp-commence').value;
            let currentYear = new Date().getFullYear();
            if(commenceDateStr && commenceDateStr.includes('-')) {
                currentYear = parseInt(commenceDateStr.split('-')[0]);
            }
            
            let tbodyHtml = '';
            
            for(let y=1; y<=tenure; y++) {
                let yearlyInterest = 0;
                let yearlyPrincipal = 0;
                let openingBal = balance;
                
                for(let m=1; m<=12; m++) {
                    let interestForMonth = balance * r;
                    let principalForMonth = emi - interestForMonth;
                    yearlyInterest += interestForMonth;
                    yearlyPrincipal += principalForMonth;
                    balance -= principalForMonth;
                    if(balance < 0) balance = 0;
                }
                
                tbodyHtml += `<tr class="hover:bg-slate-700/30 transition-colors w-full table table-fixed">
                    <td class="px-4 py-3 text-gray-300 w-1/6">Year ${y} (${currentYear + y - 1})</td>
                    <td class="px-4 py-3 text-gray-400 w-1/6 font-mono">${formatCrLakh(openingBal)}</td>
                    <td class="px-4 py-3 text-gray-300 font-medium w-1/6 font-mono">${formatCrLakh(emi * 12)}</td>
                    <td class="px-4 py-3 text-rose-300/80 w-1/6 font-mono">${formatCrLakh(yearlyInterest)}</td>
                    <td class="px-4 py-3 text-emerald-300/80 w-1/6 font-mono">${formatCrLakh(yearlyPrincipal)}</td>
                    <td class="px-4 py-3 text-white font-medium w-1/6 font-mono">${formatCrLakh(balance)}</td>
                </tr>`;
            }
            document.getElementById('amortization-tbody').innerHTML = tbodyHtml;"""

event_listener_str = "        document.addEventListener('DOMContentLoaded', calculate);"

new_event_listener = """        document.addEventListener('DOMContentLoaded', () => {
            calculate();
            const btnShow = document.getElementById('btn-show-amortization');
            if(btnShow) {
                btnShow.addEventListener('click', () => {
                    const sec = document.getElementById('amortization-section');
                    sec.classList.remove('hidden');
                    // Scroll to it
                    sec.scrollIntoView({behavior: 'smooth', block: 'start'});
                });
            }
            const btnHide = document.getElementById('btn-hide-amortization');
            if(btnHide) {
                btnHide.addEventListener('click', () => {
                    document.getElementById('amortization-section').classList.add('hidden');
                });
            }
        });"""

content = content.replace(target_str, new_button)
content = content.replace(logic_str, new_logic)
content = content.replace(event_listener_str, new_event_listener)

with open('tool-home-loan-calculator.html', 'w', encoding='utf-8') as f:
    f.write(content)
