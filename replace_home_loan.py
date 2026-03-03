import os

with open('tool-home-loan-calculator.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div class="tool-container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">'
end_marker = '</body>'
start_idx = content.find(start_marker)
end_idx = content.rfind(end_marker)

replacement = """<div class="tool-container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">

        <!-- Header -->
        <header class="page-header mb-10 flex flex-col sm:flex-row sm:items-end sm:justify-between border-b border-gray-800 pb-6 gap-4 relative z-10 mt-8">
            <div>
                <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-white">HOME LOAN VS RENT <span class="text-indigo-500">CALCULATOR</span></h1>
                <p id="qs-welcome-greet" class="text-sm text-gray-400 mt-2 font-medium tracking-wide"></p>
            </div>
            <a href="index.html#tools" class="text-sm font-medium text-gray-400 hover:text-indigo-400 transition-colors">Back to Tools</a>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
            
            <!-- Left Column: Inputs -->
            <div class="space-y-6">
                <!-- Loan Details -->
                <div class="glass-panel p-6 rounded-xl border border-gray-800/50 space-y-4">
                    <h2 class="text-lg font-bold text-white mb-4">🏠 Loan Details</h2>
                    
                    <div>
                        <label class="block text-sm text-gray-400 font-medium mb-1">Commencement Date</label>
                        <input type="month" id="inp-commence" value="2025-02" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                    </div>
                    <div>
                        <label class="block text-sm text-gray-400 font-medium mb-1">Property Value (₹)</label>
                        <input type="text" id="inp-property" value="10000000" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none font-bold text-lg">
                    </div>
                    <div>
                        <div class="flex justify-between text-sm text-gray-400 font-medium mb-1">
                            <span>Down Payment (%)</span>
                            <span id="dp-amt-label" class="text-indigo-400">₹ 20,00,000</span>
                        </div>
                        <input type="number" id="inp-dp-pct" value="20" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm text-gray-400 font-medium mb-1">Loan Interest Rate (%)</label>
                            <input type="number" step="0.1" id="inp-rate" value="8.5" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                        </div>
                        <div>
                            <label class="block text-sm text-gray-400 font-medium mb-1">Loan Tenure (Years)</label>
                            <input type="number" id="inp-tenure" value="20" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm text-gray-400 font-medium mb-1">Buying Brokerage (%)</label>
                        <input type="number" step="0.1" id="inp-brokerage" value="1.0" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                    </div>
                </div>

                <!-- Renting Details -->
                <div class="glass-panel p-6 rounded-xl border border-gray-800/50 space-y-4">
                    <h2 class="text-lg font-bold text-white mb-4">Monthly Rent</h2>
                    
                    <div>
                        <div class="flex justify-between text-sm text-gray-400 font-medium mb-1">
                            <span>Monthly Rent (₹)</span>
                            <span id="annual-rent-label" class="text-amber-400">₹ 3.6L/year</span>
                        </div>
                        <input type="text" id="inp-rent" value="30000" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                    </div>
                    <div>
                        <label class="block text-sm text-gray-400 font-medium mb-1">Annual Rent Increase (%)</label>
                        <input type="number" step="0.1" id="inp-rent-inc" value="5.0" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                    </div>
                </div>

                <!-- Market Assumptions -->
                <div class="glass-panel p-6 rounded-xl border border-gray-800/50 space-y-4">
                    <h2 class="text-lg font-bold text-white mb-4">Market & Maintenance Assumptions</h2>

                    <div>
                        <label class="block text-sm text-gray-400 font-medium mb-1">Investment Instrument</label>
                        <select id="inp-invest-inst" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                            <option value="mf">Mutual Funds (Equity)</option>
                            <option value="fd">Fixed Deposits</option>
                            <option value="bonds">Bonds</option>
                        </select>
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm text-gray-400 font-medium mb-1">Expected Annual Return (%)</label>
                            <input type="number" step="0.1" id="inp-return" value="12.0" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                        </div>
                        <div>
                            <label class="block text-sm text-gray-400 font-medium mb-1">Annual Property Appreciation (%)</label>
                            <input type="number" step="0.1" id="inp-appr" value="5.0" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm text-gray-400 font-medium mb-1">Annual Maintenance Cost (% of PV)</label>
                            <input type="number" step="0.1" id="inp-maint" value="0.5" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                        </div>
                        <div>
                            <label class="block text-sm text-gray-400 font-medium mb-1">Annual Property Tax (% of PV)</label>
                            <input type="number" step="0.1" id="inp-tax" value="0.2" class="w-full bg-slate-800 border border-slate-600 rounded px-3 py-2 text-white outline-none">
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Column: Results & Projections -->
            <div class="space-y-6">
                <!-- KPI Totals -->
                <div class="grid grid-cols-2 gap-4">
                    <div class="glass-panel p-6 rounded-xl border-l-[6px] border-l-rose-500 bg-slate-800/50">
                        <p class="text-gray-400 text-sm font-semibold mb-1">Total Buying Cost</p>
                        <h3 class="text-3xl font-extrabold text-white" id="res-total-buy">₹ 0</h3>
                    </div>
                    <div class="glass-panel p-6 rounded-xl border-l-[6px] border-l-emerald-500 bg-slate-800/50">
                        <p class="text-gray-400 text-sm font-semibold mb-1">Total Renting Cost</p>
                        <h3 class="text-3xl font-extrabold text-white" id="res-total-rent">₹ 0</h3>
                    </div>
                </div>

                <!-- Buy Outright Projection -->
                <div class="glass-panel p-6 rounded-xl border border-gray-700">
                    <h4 class="text-white font-bold mb-2">Buy Outright</h4>
                    <p class="text-gray-400 text-sm leading-relaxed" id="res-buy-outright-text">
                        If you bought the property outright today for ₹ 0, its projected value after 20 years would be <span class="font-bold text-white">₹ 0</span>.
                    </p>
                </div>

                <!-- Loan Summary -->
                <div class="glass-panel p-6 rounded-xl border border-gray-700 bg-[#0f172a]">
                    <h4 class="text-white font-bold mb-4">Loan Summary</h4>
                    <div class="space-y-3 text-sm">
                        <div class="flex justify-between items-center border-b border-gray-800 pb-2">
                            <span class="text-gray-400">Loan Amount</span>
                            <span class="text-white font-bold" id="res-loan-amount">₹ 0 L</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-gray-800 pb-2">
                            <span class="text-gray-400">Monthly EMI</span>
                            <span class="text-indigo-400 font-bold" id="res-emi">₹ 0</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-gray-800 pb-2">
                            <span class="text-gray-400">Total Interest Paid</span>
                            <span class="text-white font-bold" id="res-interest-paid">₹ 0 L</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-gray-800 pb-2">
                            <span class="text-gray-400">Total Maintenance Paid</span>
                            <span class="text-white font-bold" id="res-maint-paid">₹ 0</span>
                        </div>
                        <div class="flex justify-between items-center">
                            <span class="text-gray-400">Total Property Tax Paid</span>
                            <span class="text-white font-bold" id="res-tax-paid">₹ 0 L</span>
                        </div>
                    </div>
                </div>

                <!-- Final Verdict -->
                <div id="verdict-box" class="p-6 rounded-xl text-center border mt-8 transition-all">
                    <h2 id="verdict-title" class="text-2xl font-black mb-3 text-white">Calculating...</h2>
                    <p id="verdict-desc" class="text-gray-300 text-sm leading-relaxed">Please wait...</p>
                </div>

                <!-- Action Button -->
                <div class="flex justify-end pt-4">
                    <button class="bg-indigo-600 hover:bg-indigo-500 text-white px-5 py-3 rounded-lg font-bold shadow-lg shadow-indigo-600/20 transition-all flex items-center gap-2">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                        Yearly EMI Breakdown
                    </button>
                </div>

            </div>
        </div>
    </div> <!-- Close tool-container -->

    <script>
        const formatCrLakh = (num) => {
            if(num >= 10000000) {
                return "₹ " + (num / 10000000).toFixed(2) + " Cr";
            } else if (num >= 100000) {
                return "₹ " + (num / 100000).toFixed(2) + " L";
            } else {
                return "₹ " + Math.round(num).toLocaleString('en-IN');
            }
        };

        const parseNum = (str) => parseFloat(String(str).replace(/[^0-9.]/g, '')) || 0;
        
        const inps = ['property', 'dp-pct', 'rate', 'tenure', 'brokerage', 'rent', 'rent-inc', 'return', 'appr', 'maint', 'tax'];
        inps.forEach(i => {
            const el = document.getElementById('inp-' + i);
            if(el) {
                if(i === 'property' || i === 'rent') {
                    el.addEventListener('blur', e => e.target.value = Math.round(parseNum(e.target.value)).toLocaleString('en-IN'));
                }
                el.addEventListener('input', calculate);
            }
        });

        function calculate() {
            const propValue = parseNum(document.getElementById('inp-property').value);
            const dpPct = parseNum(document.getElementById('inp-dp-pct').value);
            const rate = parseNum(document.getElementById('inp-rate').value);
            const tenure = parseNum(document.getElementById('inp-tenure').value);
            const brokeragePct = parseNum(document.getElementById('inp-brokerage').value);
            const rent = parseNum(document.getElementById('inp-rent').value);
            const rentIncPct = parseNum(document.getElementById('inp-rent-inc').value);
            const invRetPct = parseNum(document.getElementById('inp-return').value);
            const apprPct = parseNum(document.getElementById('inp-appr').value);
            const maintPct = parseNum(document.getElementById('inp-maint').value);
            const taxPct = parseNum(document.getElementById('inp-tax').value);

            document.getElementById('dp-amt-label').textContent = formatCrLakh(propValue * (dpPct/100));
            document.getElementById('annual-rent-label').textContent = formatCrLakh(rent * 12) + "/year";

            const loanAmount = propValue * (1 - dpPct/100);
            const dpAmount = propValue * (dpPct/100);
            const r = rate / 12 / 100;
            const n = tenure * 12;
            
            let emi = 0;
            if (loanAmount > 0 && r > 0 && n > 0) {
                emi = (loanAmount * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
            }
            const totalInterests = emi * n - loanAmount;
            
            let totalMaint = 0;
            let totalTax = 0;
            for(let y=0; y<tenure; y++) {
                let pv = propValue * Math.pow(1 + apprPct/100, y);
                totalMaint += pv * (maintPct/100);
                totalTax += pv * (taxPct/100);
            }
            
            const brokerageCost = propValue * (brokeragePct/100);
            const totalBuyingCost = dpAmount + (emi * n) + totalMaint + totalTax + brokerageCost;
            const finalPropValue = propValue * Math.pow(1 + apprPct/100, tenure);
            
            let totalRentingCost = 0;
            for(let y=0; y<tenure; y++) {
                totalRentingCost += rent * 12 * Math.pow(1 + rentIncPct/100, y);
            }

            let investValue = dpAmount * Math.pow(1 + invRetPct/100/12, tenure * 12);
            let monthlyInvestRate = invRetPct / 100 / 12;
            for(let m=0; m<n; m++) {
                let y = Math.floor(m/12);
                let currentRent = rent * Math.pow(1 + rentIncPct/100, y);
                let currentAssessedPV = propValue * Math.pow(1 + apprPct/100, y);
                let monthlyOpex = (currentAssessedPV * (maintPct/100) + currentAssessedPV * (taxPct/100)) / 12;
                let cashOutflowBuy = emi + monthlyOpex;
                let cashOutflowRent = currentRent;
                
                let savings = cashOutflowBuy - cashOutflowRent;
                investValue += (savings) * Math.pow(1 + monthlyInvestRate, n - m - 1);
            }

            const buyerNetWealth = finalPropValue; 
            const renterNetWealth = investValue;

            document.getElementById('res-total-buy').textContent = formatCrLakh(totalBuyingCost);
            document.getElementById('res-total-rent').textContent = formatCrLakh(totalRentingCost);
            
            document.getElementById('res-buy-outright-text').innerHTML = `If you bought the property outright today for ${formatCrLakh(propValue)}, its projected value after ${tenure} years would be <span class="font-bold text-white">${formatCrLakh(finalPropValue)}</span>.`;
            
            document.getElementById('res-loan-amount').textContent = formatCrLakh(loanAmount);
            document.getElementById('res-emi').textContent = "₹ " + Math.round(emi).toLocaleString('en-IN');
            document.getElementById('res-interest-paid').textContent = formatCrLakh(totalInterests);
            document.getElementById('res-maint-paid').textContent = formatCrLakh(totalMaint);
            document.getElementById('res-tax-paid').textContent = formatCrLakh(totalTax);

            const diff = Math.abs(renterNetWealth - buyerNetWealth);
            const renterWins = renterNetWealth > buyerNetWealth;
            
            const verdictTitle = renterWins ? "Renting is Better" : "Buying is Better";
            const verdictDesc = renterWins 
                ? `Over ${tenure} years, renting and investing the difference yields a net benefit of ${formatCrLakh(diff)} compared to buying.`
                : `Over ${tenure} years, buying yields a net wealth advantage of ${formatCrLakh(diff)} compared to renting & investing.`;
                
            const vb = document.getElementById('verdict-box');
            vb.className = "p-6 rounded-xl text-center border transition-all " + 
                (renterWins ? "bg-amber-500/10 border-amber-500/40" : "bg-emerald-500/10 border-emerald-500/40");
            
            document.getElementById('verdict-title').className = "text-2xl font-black mb-3 " + (renterWins ? "text-amber-400" : "text-emerald-400");
            document.getElementById('verdict-title').textContent = verdictTitle;
            document.getElementById('verdict-desc').textContent = verdictDesc;

            if (window.qsLogCalc) qsLogCalc('buy_vs_rent_v2', {
                pv: propValue, dp: dpPct, rent: rent, renterWins: renterWins
            });
        }

        document.addEventListener('DOMContentLoaded', calculate);
    </script>
"""

new_content = content[:start_idx] + replacement + '\n' + content[end_idx:]

with open('tool-home-loan-calculator.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
