import re

with open(r'd:\Vibe Code\Quantum Step\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== TECH ECOSYSTEM SECTION REPLACEMENT =====
tech_new = """    <!-- Tech Ecosystem Section -->
    <section id="ecosystem" class="ecosystem-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Modern Stack</div>
                <h2 class="section-title">Powering Your Vision with the <span class="gradient-text">Latest Tech</span></h2>
                <p class="section-description">At the heart of every great product is the right technology. We leverage the most powerful tools to build software that's fast, secure, and future-ready.</p>
            </div>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:1.5rem;margin-top:2rem;">
                <!-- React -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="#61DAFB"><circle cx="12" cy="12" r="2.5"/><ellipse cx="12" cy="12" rx="10" ry="4" fill="none" stroke="#61DAFB" stroke-width="1.2"/><ellipse cx="12" cy="12" rx="10" ry="4" fill="none" stroke="#61DAFB" stroke-width="1.2" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4" fill="none" stroke="#61DAFB" stroke-width="1.2" transform="rotate(120 12 12)"/></svg>
                    <span>React</span>
                </div>
                <!-- Vue -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36"><polygon points="12,2 22,20 2,20" fill="none" stroke="#41B883" stroke-width="1.5"/><polygon points="12,7 18.9,20 5.1,20" fill="none" stroke="#35495E" stroke-width="1"/></svg>
                    <span>Vue.js</span>
                </div>
                <!-- Angular -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="#DD0031"><path d="M12 2L2 6.5l1.5 11.5L12 22l8.5-4 1.5-11.5Z"/><path d="M12 2v20M7 16l5-12 5 12M8.5 13h7" fill="none" stroke="white" stroke-width="1.2"/></svg>
                    <span>Angular</span>
                </div>
                <!-- Node.js -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 2L3 7v10l9 5 9-5V7Z" fill="#339933" stroke="none"/><text x="12" y="14" text-anchor="middle" fill="white" font-size="5" font-family="monospace">JS</text></svg>
                    <span>Node.js</span>
                </div>
                <!-- Flutter -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="none"><path d="M4 12L13 3h7L10 13z" fill="#54C5F8"/><path d="M10 13l10-10v7L14 16z" fill="#01579B"/><path d="M4 12l6 6 4-4-3.5-2z" fill="#29B6F6"/><path d="M10 18l4.5-4.5L17 16l-7 7z" fill="#01579B"/></svg>
                    <span>Flutter</span>
                </div>
                <!-- Firebase -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="none"><path d="M4 20L7 8l4 4 2-8 7 16z" fill="#FFCA28"/><path d="M4 20l3-12 4 4" fill="#FFA000"/><path d="M10 12l2-8 8 16" fill="#FF6F00" opacity=".7"/></svg>
                    <span>Firebase</span>
                </div>
                <!-- AWS -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36"><path d="M7 14c-.75 2-2.5 3.5-4 3.5a4.5 4.5 0 0 1 0-9c.5 0 1 .1 1.5.25M17 14c.75 2 2.5 3.5 4 3.5a4.5 4.5 0 0 0 0-9 4 4 0 0 0-1.5.25M6 12a6 6 0 1 1 12 0" fill="none" stroke="#FF9900" stroke-width="1.5" stroke-linecap="round"/></svg>
                    <span>AWS</span>
                </div>
                <!-- PostgreSQL -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="none"><ellipse cx="12" cy="7" rx="8" ry="3.5" stroke="#336791" stroke-width="1.5"/><path d="M4 7v10c0 1.93 3.58 3.5 8 3.5s8-1.57 8-3.5V7" stroke="#336791" stroke-width="1.5"/><path d="M4 12c0 1.93 3.58 3.5 8 3.5s8-1.57 8-3.5" stroke="#336791" stroke-width="1" stroke-dasharray="2 2"/></svg>
                    <span>PostgreSQL</span>
                </div>
                <!-- Docker -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="none"><rect x="2" y="11" width="4" height="3" rx=".5" stroke="#2496ED" stroke-width="1.2"/><rect x="7" y="11" width="4" height="3" rx=".5" stroke="#2496ED" stroke-width="1.2"/><rect x="12" y="11" width="4" height="3" rx=".5" stroke="#2496ED" stroke-width="1.2"/><rect x="7" y="7" width="4" height="3" rx=".5" stroke="#2496ED" stroke-width="1.2"/><rect x="12" y="7" width="4" height="3" rx=".5" stroke="#2496ED" stroke-width="1.2"/><path d="M20 12a4 4 0 0 0-4-4H2l-1 3c0 3 3 5 8 5h7a4 4 0 0 0 4-4Z" stroke="#2496ED" stroke-width="1.2"/></svg>
                    <span>Docker</span>
                </div>
                <!-- Python -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="none"><path d="M12 2C9 2 7 3.5 7 6v2h5v1H5C2.5 9 1 11 1 13.5S2.5 18 5 18h2v-2.5C7 13 9 12 12 12s5 1 5 3.5V18h2c2.5 0 4-2 4-4.5S21.5 9 19 9h-2V6c0-2.5-2-4-5-4z" stroke="#3776AB" stroke-width="1.2"/><circle cx="9.5" cy="5.5" r="1" fill="#FFD43B"/><circle cx="14.5" cy="18.5" r="1" fill="#3776AB"/></svg>
                    <span>Python</span>
                </div>
                <!-- Next.js -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="none"><circle cx="12" cy="12" r="10" stroke="white" stroke-width="1.2"/><path d="M8 16V8l8 9V8" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                    <span>Next.js</span>
                </div>
                <!-- MongoDB -->
                <div class="tech-pill fade-in">
                    <svg viewBox="0 0 24 24" width="36" height="36" fill="none"><path d="M12 2C8 2 6 8 6 12s2 8 6 10c4-2 6-6 6-10S16 2 12 2z" fill="#4DB33D"/><path d="M12 4v16" stroke="#231F20" stroke-width="1.5"/><path d="M12 4c1 2 2 5 2 8s-1 7-2 9" stroke="#A8C8A0" stroke-width=".8"/></svg>
                    <span>MongoDB</span>
                </div>
            </div>
        </div>
    </section>"""

pattern_tech = r'    <!-- Tech Ecosystem Section -->.*?    </section>'
new_content = re.sub(pattern_tech, tech_new, content, flags=re.DOTALL)

if new_content == content:
    print('TECH PATTERN NOT FOUND')
else:
    content = new_content
    print('Tech ecosystem replaced')

# ===== ADD 4 NEW SECTIONS BEFORE CONTACT =====
new_sections = """
    <!-- Arsenal Metrics Section -->
    <section id="metrics" class="metrics-section">
        <div class="container">
            <div class="metrics-hero">
                <div class="metrics-left fade-in">
                    <div class="section-badge" style="width:fit-content;">Industry Leader</div>
                    <h2><span class="gradient-text">Your Digital Dominance</span><br>That Outlives Market Shifts</h2>
                    <p>We don't just build tech — we forge unshakeable competitive foundations. For leaders who refuse to be disrupted.</p>
                    <ul class="metrics-feature-list">
                        <li>Battle-tested expertise</li>
                        <li>Future-proof architecture</li>
                        <li>Scalable solutions</li>
                        <li>24/7 support guarantee</li>
                    </ul>
                    <div style="margin-top:2rem;">
                        <button class="btn btn-primary" onclick="window.location.href='#contact'" style="padding:.75rem 2rem;font-size:0.95rem;">Explore Our Arsenal &rarr;</button>
                    </div>
                </div>
                <div class="metrics-card fade-in">
                    <div class="metrics-card-header">
                        <div>
                            <h3>&#9642; Quantum Metrics</h3>
                            <p style="font-size:.8rem;color:rgba(255,255,255,.75);margin:0;">Proven Excellence &amp; Industry Leadership</p>
                        </div>
                        <span style="font-size:1.75rem;">&#127942;</span>
                    </div>
                    <p style="padding:1rem 1.75rem .5rem;font-size:.85rem;color:var(--text-muted);font-weight:600;text-transform:uppercase;letter-spacing:.05em;">Performance Indicators</p>
                    <div class="metrics-grid" id="metrics-grid">
                        <div class="metric-item"><div class="metric-icon">&#9889;</div><div class="metric-value">24+</div><div class="metric-label">Years Experience</div></div>
                        <div class="metric-item"><div class="metric-icon">&#128230;</div><div class="metric-value">150+</div><div class="metric-label">Projects Delivered</div></div>
                        <div class="metric-item"><div class="metric-icon">&#129309;</div><div class="metric-value">80+</div><div class="metric-label">Happy Clients</div></div>
                        <div class="metric-item"><div class="metric-icon">&#127758;</div><div class="metric-value">12+</div><div class="metric-label">Countries Served</div></div>
                    </div>
                    <div class="metrics-rates" id="metrics-rates">
                        <div class="rate-item"><div class="rate-value" style="color:#10b981;">98%</div><div class="rate-label">Success Rate</div></div>
                        <div class="rate-item"><div class="rate-value" style="color:#818cf8;">96%</div><div class="rate-label">Client Retention</div></div>
                        <div class="rate-item"><div class="rate-value" style="color:#f59e0b;">94%</div><div class="rate-label">On-Time Delivery</div></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Industry Excellence Section -->
    <section id="industries" class="industry-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Industry Expertise</div>
                <h2 class="section-title">Industry-Specific <span class="gradient-text">Excellence</span></h2>
                <p class="section-description">Specialized solutions engineered for your industry's unique challenges. Deep domain expertise across <strong>6 core industries</strong> with proven transformation results.</p>
            </div>
            <div class="industry-grid" id="industry-grid">
                <div class="industry-card fade-in"><div class="industry-card-header"><div class="industry-icon">&#127981;</div><div><div class="industry-name">Manufacturing</div><div class="industry-category">Industrial</div></div></div><div class="industry-highlight">&#8599; AI automation &mdash; 40% faster assembly</div><p class="industry-desc">Smart factories that predict maintenance, optimize workflows, and eliminate downtime with advanced IoT.</p><div class="industry-stats"><div class="industry-stat"><div class="industry-stat-value">40% efficiency</div><div class="industry-stat-label">Impact</div></div><div class="industry-stat"><div class="industry-stat-value">6-12 months</div><div class="industry-stat-label">Timeline</div></div></div><button class="industry-btn" onclick="window.location.href='#contact'">Explore Solutions</button></div>
                <div class="industry-card fade-in"><div class="industry-card-header"><div class="industry-icon">&#128663;</div><div><div class="industry-name">Automotive</div><div class="industry-category">Transportation</div></div></div><div class="industry-highlight">&#8599; 100% digital commerce</div><p class="industry-desc">Complete digital transformation from traditional sales to modern e-commerce with full ERP integration.</p><div class="industry-stats"><div class="industry-stat"><div class="industry-stat-value">100% digital</div><div class="industry-stat-label">Impact</div></div><div class="industry-stat"><div class="industry-stat-value">18 months</div><div class="industry-stat-label">Timeline</div></div></div><button class="industry-btn" onclick="window.location.href='#contact'">Explore Solutions</button></div>
                <div class="industry-card fade-in"><div class="industry-card-header"><div class="industry-icon">&#128666;</div><div><div class="industry-name">Logistics</div><div class="industry-category">Supply Chain</div></div></div><div class="industry-highlight">&#8599; Real-time visibility &mdash; 22% fuel savings</div><p class="industry-desc">Connected supply chains with predictive analytics and route optimization for maximum efficiency.</p><div class="industry-stats"><div class="industry-stat"><div class="industry-stat-value">22% savings</div><div class="industry-stat-label">Impact</div></div><div class="industry-stat"><div class="industry-stat-value">3-6 months</div><div class="industry-stat-label">Timeline</div></div></div><button class="industry-btn" onclick="window.location.href='#contact'">Explore Solutions</button></div>
                <div class="industry-card fade-in"><div class="industry-card-header"><div class="industry-icon">&#128717;</div><div><div class="industry-name">Retail</div><div class="industry-category">Commerce</div></div></div><div class="industry-highlight">&#8599; eStores outperforming physical revenue</div><p class="industry-desc">Digital-first retail experiences that drive customer loyalty and sales growth through seamless omnichannel.</p><div class="industry-stats"><div class="industry-stat"><div class="industry-stat-value">300% growth</div><div class="industry-stat-label">Impact</div></div><div class="industry-stat"><div class="industry-stat-value">4-8 months</div><div class="industry-stat-label">Timeline</div></div></div><button class="industry-btn" onclick="window.location.href='#contact'">Explore Solutions</button></div>
                <div class="industry-card fade-in"><div class="industry-card-header"><div class="industry-icon">&#127962;</div><div><div class="industry-name">Real Estate</div><div class="industry-category">Property</div></div></div><div class="industry-highlight">&#8599; PropTech revolution in progress</div><p class="industry-desc">Smart building management and digital property experiences with advanced analytics and automation.</p><div class="industry-stats"><div class="industry-stat"><div class="industry-stat-value">50% automation</div><div class="industry-stat-label">Impact</div></div><div class="industry-stat"><div class="industry-stat-value">6-10 months</div><div class="industry-stat-label">Timeline</div></div></div><button class="industry-btn" onclick="window.location.href='#contact'">Explore Solutions</button></div>
                <div class="industry-card fade-in"><div class="industry-card-header"><div class="industry-icon">&#127968;</div><div><div class="industry-name">BFSI</div><div class="industry-category">Financial</div></div></div><div class="industry-highlight">&#8599; Zero compliance-violation modernization</div><p class="industry-desc">Secure financial platforms with full regulatory compliance and modern UX for enhanced customer experience.</p><div class="industry-stats"><div class="industry-stat"><div class="industry-stat-value">100% compliant</div><div class="industry-stat-label">Impact</div></div><div class="industry-stat"><div class="industry-stat-value">12-18 months</div><div class="industry-stat-label">Timeline</div></div></div><button class="industry-btn" onclick="window.location.href='#contact'">Explore Solutions</button></div>
            </div>
        </div>
    </section>

    <!-- Growth Segments Section -->
    <section id="growth" class="growth-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Who We Serve</div>
                <h2 class="section-title">Scale With the <span class="gradient-text">Power of Your Ambition</span></h2>
                <p class="section-description">From emerging startup visionaries to global enterprise titans — we engineer technology that merges into your business for a resilient and scalable backbone.</p>
            </div>
            <div class="growth-grid">
                <div class="growth-card fade-in">
                    <div class="growth-badge">&#128640; For Startups</div>
                    <p class="growth-quote">"From napkin sketch to market dominance in 8 months."</p>
                    <p class="growth-desc">We accelerate your journey from idea to a market-ready MVP, securing your foothold and attracting early adopters.</p>
                    <ul class="growth-features"><li>Rapid Prototyping &amp; MVP Development</li><li>Reduced Time-to-Market</li><li>Cost-Effective Scalable Architecture</li><li>Data-Driven Iteration for Product-Market Fit</li></ul>
                    <div class="growth-footer"><div class="growth-footer-item"><div class="growth-footer-label">Timeline</div><div class="growth-footer-value">2-6 months</div></div><div class="growth-footer-item"><div class="growth-footer-label">Focus</div><div class="growth-footer-value">Speed &amp; Scale</div></div><div class="growth-footer-item"><div class="growth-footer-label">Result</div><div class="growth-footer-value" style="color:#10b981;">85% Launch Rate</div></div></div>
                    <button class="growth-btn" onclick="window.location.href='#contact'">Get Started &rarr;</button>
                </div>
                <div class="growth-card featured fade-in">
                    <div class="growth-badge">&#128200; Most Popular &mdash; For Growing SMEs</div>
                    <p class="growth-quote">"Supercharge your growth and outpace competitors."</p>
                    <p class="growth-desc">We optimize and scale your existing operations, removing bottlenecks with robust technology solutions.</p>
                    <ul class="growth-features"><li>Process Automation &amp; System Integration</li><li>Enhanced Operational Efficiency</li><li>Advanced Data &amp; Growth Analytics</li><li>Scalable Infrastructure for Uninterrupted Growth</li></ul>
                    <div class="growth-footer"><div class="growth-footer-item"><div class="growth-footer-label">Timeline</div><div class="growth-footer-value">6-12 months</div></div><div class="growth-footer-item"><div class="growth-footer-label">Focus</div><div class="growth-footer-value">Integration</div></div><div class="growth-footer-item"><div class="growth-footer-label">Result</div><div class="growth-footer-value" style="color:#818cf8;">40% Cost Reduction</div></div></div>
                    <button class="growth-btn" onclick="window.location.href='#contact'">Get Started &rarr;</button>
                </div>
                <div class="growth-card fade-in">
                    <div class="growth-badge">&#127963; For Large Enterprises</div>
                    <p class="growth-quote">"Transform legacy systems into agile, innovation powerhouses."</p>
                    <p class="growth-desc">We modernize your digital core with cutting-edge solutions ensuring security, efficiency, and market leadership.</p>
                    <ul class="growth-features"><li>Enterprise-Grade Digital Transformation</li><li>Legacy System Modernization &amp; Cloud Migration</li><li>AI &amp; ML Integration for Intelligent Operations</li><li>Enhanced Security, Compliance, and Global Scalability</li></ul>
                    <div class="growth-footer"><div class="growth-footer-item"><div class="growth-footer-label">Timeline</div><div class="growth-footer-value">12-24 months</div></div><div class="growth-footer-item"><div class="growth-footer-label">Focus</div><div class="growth-footer-value">Innovation</div></div><div class="growth-footer-item"><div class="growth-footer-label">Result</div><div class="growth-footer-value" style="color:#f59e0b;">99.9% Uptime</div></div></div>
                    <button class="growth-btn" onclick="window.location.href='#contact'">Get Started &rarr;</button>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section id="faq" class="faq-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">FAQs</div>
                <h2 class="section-title">Frequently <span class="gradient-text">Asked Questions</span></h2>
                <p class="section-description">Get answers to common questions about our digital transformation services.</p>
            </div>
            <div class="faq-list" id="faq-list">
                <div class="faq-item"><div class="faq-question" onclick="toggleFaq(this)"><span>Q: Why should businesses choose Quantum Step as their technology partner?</span><div class="faq-icon">+</div></div><div class="faq-answer">We combine 24+ years of deep domain expertise with cutting-edge AI-assisted development. Every project gets dedicated architects, transparent communication, and a results-first approach — not just code delivery.</div></div>
                <div class="faq-item"><div class="faq-question" onclick="toggleFaq(this)"><span>Q: What types of digital solutions does Quantum Step provide?</span><div class="faq-icon">+</div></div><div class="faq-answer">We cover the full spectrum — from custom web &amp; mobile apps and SaaS platforms to AI integration, IoT systems, ERP tools, and e-commerce. If it runs on software, we build it.</div></div>
                <div class="faq-item"><div class="faq-question" onclick="toggleFaq(this)"><span>Q: What factors influence the cost and timeline of a project?</span><div class="faq-icon">+</div></div><div class="faq-answer">Scope complexity, number of integrations, target platforms (web/mobile/both), and your desired go-live date all play a role. We provide detailed estimates after a free discovery call.</div></div>
                <div class="faq-item"><div class="faq-question" onclick="toggleFaq(this)"><span>Q: What development methodology does Quantum Step follow?</span><div class="faq-icon">+</div></div><div class="faq-answer">We follow an Agile/Scrum approach with 2-week sprints, regular demos, and continuous feedback loops — so you always know exactly where your product stands.</div></div>
                <div class="faq-item"><div class="faq-question" onclick="toggleFaq(this)"><span>Q: Do you help with system integration and data migration?</span><div class="faq-icon">+</div></div><div class="faq-answer">Absolutely. We have deep experience integrating CRMs, ERPs, third-party APIs, and payment gateways. Data migration is handled with zero-downtime strategies.</div></div>
                <div class="faq-item"><div class="faq-question" onclick="toggleFaq(this)"><span>Q: Can you integrate AI capabilities into existing legacy systems?</span><div class="faq-icon">+</div></div><div class="faq-answer">Yes. We layer modern AI features (predictive analytics, chatbots, recommendation engines) onto existing systems without requiring a full rebuild.</div></div>
                <div class="faq-item"><div class="faq-question" onclick="toggleFaq(this)"><span>Q: Do you provide ongoing maintenance and technical support?</span><div class="faq-icon">+</div></div><div class="faq-answer">Yes, we offer flexible support retainers covering performance monitoring, security patches, bug fixes, and feature enhancements — on a monthly or quarterly basis.</div></div>
                <div class="faq-item"><div class="faq-question" onclick="toggleFaq(this)"><span>Q: How do we get started?</span><div class="faq-icon">+</div></div><div class="faq-answer">Simply click 'Free Consultation' above or fill out our contact form. We'll schedule a 30-minute discovery call to understand your goals and outline a roadmap — at no cost.</div></div>
            </div>
        </div>
    </section>

"""

# Insert all new sections before Contact section
pattern_contact = r'(\n\n    <!-- Contact Section -->)'
new_content = re.sub(pattern_contact, new_sections + r'\g<1>', content, count=1, flags=re.DOTALL)

if new_content == content:
    print('CONTACT PATTERN NOT FOUND')
else:
    content = new_content
    print('New sections inserted')

# Also add FAQ toggle JS before </body>
faq_js = """
    <script>
        function toggleFaq(el) {
            const item = el.parentElement;
            const wasOpen = item.classList.contains('open');
            document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
            if (!wasOpen) item.classList.add('open');
        }
    </script>
"""

new_content = content.replace('</body>', faq_js + '</body>', 1)
if new_content == content:
    print('BODY TAG NOT FOUND')
else:
    content = new_content
    print('FAQ JS injected')

with open(r'd:\Vibe Code\Quantum Step\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('ALL DONE')
