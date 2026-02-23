import re

with open('d:\\Vibe Code\\Quantum Step\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tools_html = """    <!-- Tools Section -->
    <section id="tools" class="tools-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">✨ Free Resources</div>
                <h2 class="section-title">Powerful Free <span class="gradient-text">Tools</span></h2>
                <p class="section-description">Built for Indian professionals. No sign-up. No cost. Just results.</p>
            </div>

            <div class="tools-grid">
                <!-- Salary Calculator -->
                <a href="tool-salary-calculator.html" class="tool-card fade-in" style="text-decoration:none;">
                    <div class="tool-icon" style="background:rgba(99,102,241,0.1); color:#818cf8; border-color:rgba(99,102,241,0.2);">💰</div>
                    <div style="font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:#818cf8; margin-bottom:0.5rem;">Finance · Tax</div>
                    <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0.5rem;">India Salary Calculator</h3>
                    <p style="color:#94a3b8; line-height:1.6; flex-grow:1; margin-bottom:1.5rem;">New vs Old Tax Regime, in-hand salary, PF, HRA deductions &amp; AI-powered insights. FY 2025-26 ready.</p>
                    <div class="gradient-text" style="font-weight:700; font-size:0.95rem; margin-top:auto; display:flex; align-items:center; gap:8px;">
                        Open Tool <span style="font-size:1.2rem;">&rarr;</span>
                    </div>
                </a>

                <!-- ArthaWealth -->
                <a href="tool-artha-wealth.html" class="tool-card fade-in" style="text-decoration:none;">
                    <div class="tool-icon" style="background:rgba(16,185,129,0.1); color:#34d399; border-color:rgba(16,185,129,0.2);">📈</div>
                    <div style="font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:#34d399; margin-bottom:0.5rem;">Finance · Investment</div>
                    <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0.5rem;">ArthaWealth Planner</h3>
                    <p style="color:#94a3b8; line-height:1.6; flex-grow:1; margin-bottom:1.5rem;">SIP &amp; SWP calculator with visual wealth projections. Plan your financial freedom step by step.</p>
                    <div style="font-weight:700; font-size:0.95rem; margin-top:auto; display:flex; align-items:center; gap:8px; background:linear-gradient(135deg,#10b981,#06b6d4); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
                        Open Tool <span style="font-size:1.2rem;">&rarr;</span>
                    </div>
                </a>

                <!-- Home Loan -->
                <a href="tool-home-loan-calculator.html" class="tool-card fade-in" style="text-decoration:none;">
                    <div class="tool-icon" style="background:rgba(244,63,94,0.1); color:#fb7185; border-color:rgba(244,63,94,0.2);">🏠</div>
                    <div style="font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:#fb7185; margin-bottom:0.5rem;">Finance · Property</div>
                    <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0.5rem;">Home Loan Calculator</h3>
                    <p style="color:#94a3b8; line-height:1.6; flex-grow:1; margin-bottom:1.5rem;">Advanced EMI calculator with full amortization schedule, prepayment strategies &amp; interest breakdowns.</p>
                    <div style="font-weight:700; font-size:0.95rem; margin-top:auto; display:flex; align-items:center; gap:8px; background:linear-gradient(135deg,#f43f5e,#f97316); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
                        Open Tool <span style="font-size:1.2rem;">&rarr;</span>
                    </div>
                </a>
            </div>
            
            <div style="text-align:center; color:var(--text-muted); font-size:0.85rem; margin-top:3rem; letter-spacing:0.05em;">
                More tools coming soon &bull; Built &amp; maintained by Quantum Step Creations
            </div>
        </div>
    </section>"""

portfolio_html = """    <!-- Portfolio / Clients Section -->
    <section id="portfolio" class="portfolio-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Our Work</div>
                <h2 class="section-title">Trusted by <span class="gradient-text">Real Clients</span></h2>
                <p class="section-description">From edtech to fintech, we build products that perform. Click any card to visit the live project.</p>
            </div>

            <div class="portfolio-grid">
                <!-- IPN PaathShala -->
                <a href="https://www.ipn-india.in" target="_blank" rel="noopener" class="portfolio-item fade-in" style="text-decoration:none;">
                    <div class="portfolio-image" style="background:linear-gradient(135deg,#1e3a5f,#2563eb,#7c3aed);display:flex;align-items:center;justify-content:center;">
                        <span style="font-size:3.5rem;position:relative;z-index:10;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.3));">🎓</span>
                    </div>
                    <div class="portfolio-content">
                        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
                            <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0;">IPN PaathShala</h3>
                            <span style="font-size:0.7rem;background:rgba(99,102,241,.15);color:#818cf8;padding:2px 8px;border-radius:999px;font-weight:600;">EdTech</span>
                        </div>
                        <p style="color:#cbd5e1; font-size:0.95rem;">Online learning platform empowering students across India with structured courses &amp; live sessions.</p>
                    </div>
                </a>

                <!-- Royal Visa Experts -->
                <a href="https://rvxtravels.com" target="_blank" rel="noopener" class="portfolio-item fade-in" style="text-decoration:none;">
                    <div class="portfolio-image" style="background:linear-gradient(135deg,#1a1a2e,#c9a84c,#8b6914);display:flex;align-items:center;justify-content:center;">
                        <span style="font-size:3.5rem;position:relative;z-index:10;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.3));">✈️</span>
                    </div>
                    <div class="portfolio-content">
                        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
                            <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0;">Royal Visa Experts</h3>
                            <span style="font-size:0.7rem;background:rgba(245,158,11,.15);color:#fbbf24;padding:2px 8px;border-radius:999px;font-weight:600;">Travel</span>
                        </div>
                        <p style="color:#cbd5e1; font-size:0.95rem;">Premium visa consultancy &amp; travel solutions trusted by thousands of global travellers.</p>
                    </div>
                </a>

                <!-- AI Shield -->
                <a href="https://chromewebstore.google.com" target="_blank" rel="noopener" class="portfolio-item fade-in" style="text-decoration:none;">
                    <div class="portfolio-image" style="background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);display:flex;align-items:center;justify-content:center;">
                        <span style="font-size:3.5rem;position:relative;z-index:10;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.3));">🛡️</span>
                    </div>
                    <div class="portfolio-content">
                        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
                            <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0;">AI Shield</h3>
                            <span style="font-size:0.7rem;background:rgba(6,182,212,.15);color:#22d3ee;padding:2px 8px;border-radius:999px;font-weight:600;">Security</span>
                        </div>
                        <p style="color:#cbd5e1; font-size:0.95rem;">Chrome extension providing real-time AI-powered threat detection to keep your browser safe.</p>
                    </div>
                </a>

                <!-- Aaj Ka Scene -->
                <a href="https://aajkascene.netlify.app" target="_blank" rel="noopener" class="portfolio-item fade-in" style="text-decoration:none;">
                    <div class="portfolio-image" style="background:linear-gradient(135deg,#1a0533,#7c2d8e,#e879f9);display:flex;align-items:center;justify-content:center;">
                        <span style="font-size:3.5rem;position:relative;z-index:10;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.3));">🎉</span>
                    </div>
                    <div class="portfolio-content">
                        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
                            <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0;">Aaj Ka Scene</h3>
                            <span style="font-size:0.7rem;background:rgba(236,72,153,.15);color:#f472b6;padding:2px 8px;border-radius:999px;font-weight:600;">Events</span>
                        </div>
                        <p style="color:#cbd5e1; font-size:0.95rem;">India's event aggregator — discover what's happening in your city tonight across all major metros.</p>
                    </div>
                </a>

                <!-- Small Cap Sniper -->
                <a href="https://smallcapsniper.netlify.app" target="_blank" rel="noopener" class="portfolio-item fade-in" style="text-decoration:none;">
                    <div class="portfolio-image" style="background:linear-gradient(135deg,#0a1a0a,#14532d,#22c55e);display:flex;align-items:center;justify-content:center;">
                        <span style="font-size:3.5rem;position:relative;z-index:10;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.3));">📊</span>
                    </div>
                    <div class="portfolio-content">
                        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
                            <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0;">Small Cap Sniper</h3>
                            <span style="font-size:0.7rem;background:rgba(34,197,94,.15);color:#4ade80;padding:2px 8px;border-radius:999px;font-weight:600;">FinTech</span>
                        </div>
                        <p style="color:#cbd5e1; font-size:0.95rem;">Fundamental analysis tool for Indian Small &amp; MicroCap stocks — built for the serious retail investor.</p>
                    </div>
                </a>

                <!-- CTA Card -->
                <div class="portfolio-item fade-in" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:linear-gradient(135deg,rgba(99,102,241,.08),rgba(6,182,212,.06));border:1px dashed rgba(99,102,241,.3);cursor:default;min-height:300px;padding:2rem;">
                    <span style="font-size:3rem;margin-bottom:1rem;">🚀</span>
                    <h3 style="color:#f8fafc; font-size:1.5rem; font-weight:700; margin-bottom:0.5rem;">Your Product Here</h3>
                    <p style="color:#94a3b8; font-size:0.95rem; margin-bottom:1.5rem;">We build ideas that launch. Let's make yours next.</p>
                    <button class="btn btn-primary" onclick="document.getElementById('cta-primary').click()" style="font-size:0.9rem;padding:0.75rem 2rem;">Start a Project</button>
                </div>
            </div>
        </div>
    </section>"""

# Replace Tools
html = re.sub(r'<!-- Tools Section -->\s*<section id="tools".*?<!-- Bottom nudge -->.*?</section>', tools_html, html, flags=re.DOTALL)

# Replace Portfolio
html = re.sub(r'<!-- Portfolio / Clients Section -->.*?<section id="portfolio".*?</section>', portfolio_html, html, flags=re.DOTALL)

with open('d:\\Vibe Code\\Quantum Step\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
