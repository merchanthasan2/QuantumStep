import re

with open(r'd:\Vibe Code\Quantum Step\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

services_new = """    <!-- Services Section -->
    <section id="services" class="services-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Our Services</div>
                <h2 class="section-title">Our Software Development <span class="gradient-text">Services</span></h2>
                <p class="section-description">
                    Our software product development helps you solve operational challenges, launch a new product, or modernize outdated systems.
                </p>
            </div>

            <div class="services-grid">
                <div class="service-card fade-in">
                    <div class="service-image" style="background:linear-gradient(135deg,#1e2d4d,#2a3f6f,#3b52a0);display:flex;align-items:center;justify-content:center;">
                        <svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="rgba(129,140,248,0.9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/><path d="M3 12h3m12 0h3M12 3v3m0 12v3"/></svg>
                    </div>
                    <div class="service-content">
                        <h3>Software Consulting Service</h3>
                        <ul class="service-list">
                            <li>Digital Product Planning</li>
                            <li>Tech Stack Selection</li>
                            <li>Architecture &amp; Growth Roadmap</li>
                        </ul>
                    </div>
                </div>

                <div class="service-card fade-in">
                    <div class="service-image" style="background:linear-gradient(135deg,#1a3a2a,#1e5c3a,#26804f);display:flex;align-items:center;justify-content:center;">
                        <svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="rgba(52,211,153,0.9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8m-4-4v4"/><path d="M7 8h.01M11 8h6M7 12h10"/></svg>
                    </div>
                    <div class="service-content">
                        <h3>Custom Software Solutions</h3>
                        <ul class="service-list">
                            <li>Workflow Automation Tools</li>
                            <li>Vendor &amp; Contract Management (VMS, CLM)</li>
                            <li>ERP, HR, Payroll &amp; Attendance Platforms</li>
                        </ul>
                    </div>
                </div>

                <div class="service-card fade-in">
                    <div class="service-image" style="background:linear-gradient(135deg,#1a1a3e,#2d2d7a,#4040b0);display:flex;align-items:center;justify-content:center;">
                        <svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="rgba(165,180,252,0.9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/><rect x="2" y="6" width="5" height="8" rx="1"/></svg>
                    </div>
                    <div class="service-content">
                        <h3>Web &amp; Mobile App Development</h3>
                        <ul class="service-list">
                            <li>Client &amp; Internal Portals</li>
                            <li>On-demand Delivery, Wallet, Fitness Apps</li>
                            <li>Custom CRMs &amp; Communication Tools</li>
                        </ul>
                    </div>
                </div>

                <div class="service-card fade-in">
                    <div class="service-image" style="background:linear-gradient(135deg,#0d2438,#0f3460,#1a5276);display:flex;align-items:center;justify-content:center;">
                        <svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="rgba(56,189,248,0.9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/></svg>
                    </div>
                    <div class="service-content">
                        <h3>SaaS &amp; Cloud Platform Development</h3>
                        <ul class="service-list">
                            <li>Learning Management Systems (LMS)</li>
                            <li>Subscription &amp; Billing Platforms</li>
                            <li>Marketing &amp; Collaboration Tools</li>
                        </ul>
                    </div>
                </div>

                <div class="service-card fade-in">
                    <div class="service-image" style="background:linear-gradient(135deg,#2d1a3e,#4a1a6b,#6b21a8);display:flex;align-items:center;justify-content:center;">
                        <svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="rgba(216,180,254,0.9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V7h1a7 7 0 0 1 7 7h1a1 1 0 0 1 0 2h-1v1a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-1H2a1 1 0 0 1 0-2h1a7 7 0 0 1 7-7h1V5.73c-.6-.34-1-.99-1-1.73a2 2 0 0 1 2-2z"/><path d="M9 14h.01M12 14h.01M15 14h.01"/></svg>
                    </div>
                    <div class="service-content">
                        <h3>AI, IoT &amp; Next-Gen Tech</h3>
                        <ul class="service-list">
                            <li>AI Chatbots &amp; Analytics Dashboards</li>
                            <li>Fleet/Factory Monitoring (IoT)</li>
                            <li>Smart Energy &amp; Document Tools</li>
                        </ul>
                    </div>
                </div>

                <div class="service-card fade-in">
                    <div class="service-image" style="background:linear-gradient(135deg,#1a2a1a,#1e4d2b,#276738);display:flex;align-items:center;justify-content:center;">
                        <svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="rgba(74,222,128,0.9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22C6.5 22 2 17.5 2 12S6.5 2 12 2s10 4.5 10 10"/><path d="M12 6v6l4 2"/><path d="M18 14v4h4"/><path d="M18 22v.01"/></svg>
                    </div>
                    <div class="service-content">
                        <h3>Ongoing Support &amp; Optimization</h3>
                        <ul class="service-list">
                            <li>Performance Tuning</li>
                            <li>Bug Fixing &amp; Security Patches</li>
                            <li>Continuous Monitoring &amp; Upgrades</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

# Escape slashes for regex replacement
pattern = r'    <!-- Services Section -->.*?    </section>'
new_content = re.sub(pattern, services_new, content, flags=re.DOTALL)

if new_content == content:
    print('ERROR: Pattern not matched')
else:
    with open(r'd:\Vibe Code\Quantum Step\index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('SUCCESS: Services section replaced')
