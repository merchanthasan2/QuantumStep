import re

# ==========================================
# 1. UPDATE index.html: Footer + SEO + Industry Icon Section
# ==========================================

with open(r'd:\Vibe Code\Quantum Step\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# --- SEO HEAD UPDATE ---
old_head = '''    <meta name="description"
        content="Quantum Step Creations - Full-Stack Development Experts in Mumbai. We build Websites, Web Apps, Full-Stack Solutions & Mobile Apps.">
    <meta name="keywords"
        content="web development, full-stack, web apps, mobile apps, Mumbai, quantum step, website design">

    <!-- OpenGraph -->
    <meta property="og:title" content="Quantum Step Creations - No-Code Web Mastery">
    <meta property="og:description" content="Mumbai\'s Premier Low-Code Agency | Websites in Weeks, Not Months">
    <meta property="og:type" content="website">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Quantum Step Creations">

    <title>Quantum Step Creations - No-Code Web Mastery | Mumbai</title>'''

new_head = '''    <meta name="description" content="Quantum Step Creations - Custom Software Development Agency in Mumbai. We build Web Apps, Mobile Apps, SaaS Platforms, ERP Systems, AI Solutions & more. 80+ happy clients across 12+ countries.">
    <meta name="keywords" content="software development Mumbai, custom web application development, mobile app development India, SaaS development, ERP software, AI chatbot development, React developer Mumbai, Node.js development, full stack developer Mumbai, quantum step creations">
    <meta name="author" content="Quantum Step Creations">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://quantumstep.in/">

    <!-- OpenGraph -->
    <meta property="og:title" content="Quantum Step Creations | Custom Software Development Mumbai">
    <meta property="og:description" content="Transform your business with custom software, web & mobile apps, AI integration, and SaaS platforms. 80+ clients served across 12+ countries. Based in Mumbai.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://quantumstep.in/">
    <meta property="og:image" content="https://quantumstep.in/logo-light.png">
    <meta property="og:locale" content="en_IN">
    <meta property="og:site_name" content="Quantum Step Creations">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Quantum Step Creations | Custom Software Development Mumbai">
    <meta name="twitter:description" content="80+ clients. 12+ countries. Custom web apps, mobile apps, AI & SaaS. Mumbai-based software agency.">
    <meta name="twitter:image" content="https://quantumstep.in/logo-light.png">

    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Quantum Step Creations",
      "description": "Custom software development agency in Mumbai specializing in web apps, mobile apps, SaaS, AI, and IoT.",
      "url": "https://quantumstep.in",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Any",
      "offers": { "@type": "Offer", "priceCurrency": "INR" },
      "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "80" }
    }
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Quantum Step Creations",
      "image": "https://quantumstep.in/logo-light.png",
      "url": "https://quantumstep.in",
      "telephone": "+91-98765-43210",
      "email": "contact@quantumstep.com",
      "address": { "@type": "PostalAddress", "addressLocality": "Mumbai", "addressCountry": "IN" },
      "geo": { "@type": "GeoCoordinates", "latitude": "19.0760", "longitude": "72.8777" },
      "openingHoursSpecification": { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "18:00" },
      "sameAs": ["https://www.linkedin.com/company/quantumstep", "https://www.instagram.com/quantumstepcreations"]
    }
    </script>

    <title>Quantum Step Creations | Custom Software Development Agency Mumbai</title>'''

content = content.replace(old_head, new_head, 1)
print('SEO head updated' if 'LocalBusiness' in content else 'SEO head NOT updated')

# --- INDUSTRY ICON SECTION (insert after ecosystem section) ---
industry_icons_section = """
    <!-- Industry Icon Grid Section -->
    <section class="industry-icons-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Verticals</div>
                <h2 class="section-title">Software Built for the Challenges of <span class="gradient-text">Your Industry</span></h2>
                <p class="section-description">The future is fast. Your software should be faster. Our software product development helps you lead your industry, not follow.</p>
            </div>
            <div class="industry-icons-grid">
                <div class="industry-icon-item fade-in">
                    <div class="industry-icon-wrap" style="background:rgba(99,102,241,.08);border-color:rgba(99,102,241,.2);">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#818cf8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13" rx="2"/><path d="M16 8h4l3 5v3h-7V8Z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
                    </div>
                    <span>Automotive</span>
                </div>
                <div class="industry-icon-item fade-in">
                    <div class="industry-icon-wrap" style="background:rgba(16,185,129,.08);border-color:rgba(16,185,129,.2);">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                    </div>
                    <span>Real Estate</span>
                </div>
                <div class="industry-icon-item fade-in">
                    <div class="industry-icon-wrap" style="background:rgba(245,158,11,.08);border-color:rgba(245,158,11,.2);">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2m4 7v2m-6-4h12"/></svg>
                    </div>
                    <span>Manufacturing</span>
                </div>
                <div class="industry-icon-item fade-in">
                    <div class="industry-icon-wrap" style="background:rgba(56,189,248,.08);border-color:rgba(56,189,248,.2);">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="15" rx="2"/><path d="M16 3h-4l-2 4h8l-2-4ZM9 3H5l-2 4"/><path d="M12 15v2m-4-2v2m8-2v2"/></svg>
                    </div>
                    <span>BFSI</span>
                </div>
                <div class="industry-icon-item fade-in">
                    <div class="industry-icon-wrap" style="background:rgba(244,63,94,.08);border-color:rgba(244,63,94,.2);">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#fb7185" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                    </div>
                    <span>Healthcare</span>
                </div>
                <div class="industry-icon-item fade-in">
                    <div class="industry-icon-wrap" style="background:rgba(168,85,247,.08);border-color:rgba(168,85,247,.2);">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>
                    </div>
                    <span>Media &amp; Entertainment</span>
                </div>
                <div class="industry-icon-item fade-in">
                    <div class="industry-icon-wrap" style="background:rgba(20,184,166,.08);border-color:rgba(20,184,166,.2);">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#2dd4bf" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0"/></svg>
                    </div>
                    <span>Retail</span>
                </div>
                <div class="industry-icon-item fade-in">
                    <div class="industry-icon-wrap" style="background:rgba(99,102,241,.08);border-color:rgba(99,102,241,.2);">
                        <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#a5b4fc" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8m-4-4v4"/><path d="M7 10l2 2 4-4"/></svg>
                    </div>
                    <span>Technology</span>
                </div>
            </div>
        </div>
    </section>
"""

content = content.replace('    <!-- Tech Ecosystem Section -->', industry_icons_section + '    <!-- Tech Ecosystem Section -->', 1)
print('Industry icons section inserted' if 'industry-icons-section' in content else 'Industry icons NOT inserted')

# --- FOOTER WITH SOCIAL ICONS ---
old_footer = '''    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-logo">
                <img src="logo-light.png" alt="Quantum Step Creations" class="footer-logo-image">
            </div>
            <p>&copy; 2025 Quantum Step Creations | Mumbai, India | Crafted with ❤️</p>
        </div>
    </footer>'''

new_footer = '''    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-logo">
                <img src="logo-light.png" alt="Quantum Step Creations" class="footer-logo-image">
            </div>
            <div class="footer-nav" style="display:flex;justify-content:center;gap:2rem;flex-wrap:wrap;margin-bottom:1.5rem;">
                <a href="#services" style="color:var(--text-muted);text-decoration:none;font-size:.9rem;transition:color .2s;" onmouseover="this.style.color=\'#818cf8\'" onmouseout="this.style.color=\'\'">Services</a>
                <a href="#tools" style="color:var(--text-muted);text-decoration:none;font-size:.9rem;transition:color .2s;" onmouseover="this.style.color=\'#818cf8\'" onmouseout="this.style.color=\'\'">Tools</a>
                <a href="#portfolio" style="color:var(--text-muted);text-decoration:none;font-size:.9rem;transition:color .2s;" onmouseover="this.style.color=\'#818cf8\'" onmouseout="this.style.color=\'\'">Portfolio</a>
                <a href="#industries" style="color:var(--text-muted);text-decoration:none;font-size:.9rem;transition:color .2s;" onmouseover="this.style.color=\'#818cf8\'" onmouseout="this.style.color=\'\'">Industries</a>
                <a href="#faq" style="color:var(--text-muted);text-decoration:none;font-size:.9rem;transition:color .2s;" onmouseover="this.style.color=\'#818cf8\'" onmouseout="this.style.color=\'\'">FAQ</a>
                <a href="#contact" style="color:var(--text-muted);text-decoration:none;font-size:.9rem;transition:color .2s;" onmouseover="this.style.color=\'#818cf8\'" onmouseout="this.style.color=\'\'">Contact</a>
            </div>
            <div class="footer-social" style="display:flex;justify-content:center;gap:1rem;margin-bottom:1.5rem;">
                <a href="https://www.linkedin.com/company/quantumstep" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" style="width:42px;height:42px;border-radius:50%;background:rgba(10,102,194,.15);border:1px solid rgba(10,102,194,.3);display:flex;align-items:center;justify-content:center;color:#0A66C2;text-decoration:none;font-size:1.1rem;transition:all .3s;" onmouseover="this.style.background=\'rgba(10,102,194,.3)\';this.style.transform=\'translateY(-4px)\'" onmouseout="this.style.background=\'rgba(10,102,194,.15)\';this.style.transform=\'\'">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zm2-3a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/></svg>
                </a>
                <a href="https://www.instagram.com/quantumstepcreations" target="_blank" rel="noopener noreferrer" aria-label="Instagram" style="width:42px;height:42px;border-radius:50%;background:rgba(225,48,108,.12);border:1px solid rgba(225,48,108,.25);display:flex;align-items:center;justify-content:center;color:#E1306C;text-decoration:none;font-size:1.1rem;transition:all .3s;" onmouseover="this.style.background=\'rgba(225,48,108,.25)\';this.style.transform=\'translateY(-4px)\'" onmouseout="this.style.background=\'rgba(225,48,108,.12)\';this.style.transform=\'\'">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>
                </a>
                <a href="https://twitter.com/quantumstep" target="_blank" rel="noopener noreferrer" aria-label="X (Twitter)" style="width:42px;height:42px;border-radius:50%;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;color:#f8fafc;text-decoration:none;font-size:1.1rem;transition:all .3s;" onmouseover="this.style.background=\'rgba(255,255,255,.12)\';this.style.transform=\'translateY(-4px)\'" onmouseout="this.style.background=\'rgba(255,255,255,.06)\';this.style.transform=\'\'">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.277 5.653zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </a>
                <a href="https://wa.me/919876543210" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp" style="width:42px;height:42px;border-radius:50%;background:rgba(37,211,102,.1);border:1px solid rgba(37,211,102,.25);display:flex;align-items:center;justify-content:center;color:#25D166;text-decoration:none;font-size:1.1rem;transition:all .3s;" onmouseover="this.style.background=\'rgba(37,211,102,.22)\';this.style.transform=\'translateY(-4px)\'" onmouseout="this.style.background=\'rgba(37,211,102,.1)\';this.style.transform=\'\'">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.348z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.085.54 4.043 1.481 5.749L.073 23.925l6.345-1.384A11.93 11.93 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 0 1-5.012-1.37l-.358-.213-3.747.817.848-3.651-.234-.372A9.818 9.818 0 1 1 12 21.818z"/></svg>
                </a>
            </div>
            <p style="color:var(--text-muted);font-size:.875rem;">&copy; 2025 Quantum Step Creations | Mumbai, India | Crafted with ❤️</p>
        </div>
    </footer>'''

content = content.replace(old_footer, new_footer, 1)
print('Footer with social icons updated' if 'footer-social' in content else 'Footer NOT updated')

with open(r'd:\Vibe Code\Quantum Step\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('index.html saved')
