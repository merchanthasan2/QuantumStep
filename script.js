// ===================================
// QUANTUM STEP CREATIONS - FRESH REDESIGN
// Modern Interactions & Animations
// ===================================

// Execute loading screen logic immediately
initLoadingScreen();

// Wait for DOM to load for other components
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initScrollAnimations();
    initGSAPAnimations();
    initCounters();
    initModal();
    initForms();
});

// Loading Screen
function initLoadingScreen() {
    const loadingScreen = document.getElementById('loading-screen');
    if (!loadingScreen) return;

    const hideLoader = () => {
        loadingScreen.classList.add('hidden');
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 500);
    };

    // Primary: hide when fully loaded
    if (document.readyState === 'complete') {
        hideLoader();
    } else {
        window.addEventListener('load', hideLoader);

        // Safety fallback: hide after 3.5s regardless (more aggressive than 5s)
        setTimeout(hideLoader, 3500);
    }
}

// Navigation
function initNavigation() {
    const nav = document.getElementById('main-nav');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Scroll detection — passive listener avoids blocking touch scroll
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    }, { passive: true });

    // Mobile menu toggle
    mobileMenuBtn.addEventListener('click', () => {
        navMenu.classList.toggle('active');

        // Animate hamburger
        const spans = mobileMenuBtn.querySelectorAll('span');
        if (navMenu.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translateY(10px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translateY(-10px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });

    // Smooth scroll
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href');

            // Allow normal navigation for external/page links
            if (!targetId || !targetId.startsWith('#')) return;

            e.preventDefault();
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 70;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });

                // Close mobile menu
                navMenu.classList.remove('active');
                const spans = mobileMenuBtn.querySelectorAll('span');
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    });
}

// Scroll Animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe all fade-in elements
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
}

// GSAP Animations
function initGSAPAnimations() {
    gsap.registerPlugin(ScrollTrigger);

    // Service cards stagger
    gsap.from('.service-card', {
        scrollTrigger: {
            trigger: '.services-section',
            start: 'top 70%',
            toggleActions: 'play none none reverse'
        },
        opacity: 0,
        y: 60,
        stagger: 0.15,
        duration: 0.8,
        ease: 'power3.out'
    });

    // AI Section
    gsap.from('.ai-feature', {
        scrollTrigger: {
            trigger: '.ai-section',
            start: 'top 70%'
        },
        opacity: 0,
        x: -40,
        stagger: 0.2,
        duration: 0.8,
        ease: 'power2.out'
    });

    // KPI Cards
    gsap.from('.kpi-card', {
        scrollTrigger: {
            trigger: '.why-section',
            start: 'top 70%'
        },
        opacity: 0,
        y: 40,
        stagger: 0.15,
        duration: 0.8,
        ease: 'power3.out'
    });

    // Engagement Nodes
    gsap.from('.engagement-node', {
        scrollTrigger: {
            trigger: '.engagement-section',
            start: 'top 70%'
        },
        opacity: 0,
        scale: 0.8,
        stagger: 0.2,
        duration: 1,
        ease: 'elastic.out(1, 0.5)'
    });

    // Pricing cards
    gsap.from('.pricing-card', {
        scrollTrigger: {
            trigger: '.pricing-section',
            start: 'top 70%',
            toggleActions: 'play none none reverse'
        },
        opacity: 0,
        y: 60,
        stagger: 0.15,
        duration: 0.8,
        ease: 'power3.out'
    });

    // Section titles
    gsap.utils.toArray('.section-title').forEach(title => {
        gsap.from(title, {
            scrollTrigger: {
                trigger: title,
                start: 'top 85%',
                toggleActions: 'play none none reverse'
            },
            opacity: 0,
            y: 40,
            duration: 0.8,
            ease: 'power3.out'
        });
    });

    // Contact form and info
    gsap.from('.contact-form', {
        scrollTrigger: {
            trigger: '.contact-section',
            start: 'top 70%',
            toggleActions: 'play none none reverse'
        },
        opacity: 0,
        x: -50,
        duration: 0.8,
        ease: 'power3.out'
    });

    gsap.from('.contact-info', {
        scrollTrigger: {
            trigger: '.contact-section',
            start: 'top 70%',
            toggleActions: 'play none none reverse'
        },
        opacity: 0,
        x: 50,
        duration: 0.8,
        ease: 'power3.out'
    });
}

// Counter Animation
function initCounters() {
    const counters = document.querySelectorAll('.stat-number');
    let hasAnimated = false;

    const animateCounter = (counter) => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };

        updateCounter();
    };

    // Trigger animation when stats section is in view
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasAnimated) {
                hasAnimated = true;
                counters.forEach((counter, index) => {
                    setTimeout(() => {
                        animateCounter(counter);
                    }, index * 150);
                });
            }
        });
    }, { threshold: 0.5 });

    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        observer.observe(statsSection);
    }
}

// Modal
function initModal() {
    const modal = document.getElementById('cta-modal');
    const ctaBtn = document.getElementById('cta-primary');
    const closeBtn = document.querySelector('.modal-close');

    if (!modal || !ctaBtn || !closeBtn) return;

    ctaBtn.addEventListener('click', () => {
        modal.classList.add('active');
        gsap.from('.modal-content', {
            scale: 0.9,
            opacity: 0,
            duration: 0.3,
            ease: 'back.out(1.7)'
        });
    });

    closeBtn.addEventListener('click', () => {
        gsap.to('.modal-content', {
            scale: 0.9,
            opacity: 0,
            duration: 0.2,
            ease: 'power2.in',
            onComplete: () => {
                modal.classList.remove('active');
            }
        });
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            gsap.to('.modal-content', {
                scale: 0.9,
                opacity: 0,
                duration: 0.2,
                ease: 'power2.in',
                onComplete: () => {
                    modal.classList.remove('active');
                }
            });
        }
    });
}

// Forms
function initForms() {
    const contactForm = document.getElementById('contact-form');
    const modalForm = document.getElementById('modal-form');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Show success message
            gsap.to(contactForm, {
                opacity: 0,
                y: -20,
                duration: 0.5,
                onComplete: () => {
                    contactForm.innerHTML = `
                        <div style="text-align: center; padding: 3rem;">
                            <h3 style="font-size: 2rem; margin-bottom: 1rem; background: var(--gradient-primary); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                                Thank You! 🎉
                            </h3>
                            <p style="color: var(--text-secondary); font-size: 1.125rem;">
                                We'll get back to you within 24 hours.
                            </p>
                        </div>
                    `;
                    gsap.to(contactForm, { opacity: 1, y: 0, duration: 0.5 });
                }
            });
        });
    }

    if (modalForm) {
        modalForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Show success message
            gsap.to(modalForm, {
                opacity: 0,
                y: -20,
                duration: 0.5,
                onComplete: () => {
                    modalForm.innerHTML = `
                        <div style="text-align: center; padding: 2rem;">
                            <h3 style="font-size: 1.75rem; margin-bottom: 1rem; background: var(--gradient-primary); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                                Submitted! ✨
                            </h3>
                            <p style="color: var(--text-secondary);">
                                We'll contact you shortly.
                            </p>
                        </div>
                    `;
                    gsap.to(modalForm, { opacity: 1, y: 0, duration: 0.5 });

                    setTimeout(() => {
                        gsap.to('.modal-content', {
                            scale: 0.9,
                            opacity: 0,
                            duration: 0.2,
                            ease: 'power2.in',
                            onComplete: () => {
                                document.getElementById('cta-modal').classList.remove('active');
                            }
                        });
                    }, 2500);
                }
            });
        });
    }
}

// Add hover effect to cards
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.service-card, .portfolio-item, .pricing-card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            gsap.to(this, {
                scale: 1.02,
                duration: 0.3,
                ease: 'power2.out'
            });
        });

        card.addEventListener('mouseleave', function () {
            gsap.to(this, {
                scale: 1,
                duration: 0.3,
                ease: 'power2.out'
            });
        });
    });
});

// Parallax effect for floating shapes — RAF-throttled for smooth mobile performance
(function () {
    let ticking = false;
    const shapes = document.querySelectorAll('.shape');

    // Only run parallax on non-touch (desktop) devices to avoid mobile jank
    const isTouchDevice = window.matchMedia('(hover: none) and (pointer: coarse)').matches;
    if (isTouchDevice || shapes.length === 0) return;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(() => {
                const scrolled = window.pageYOffset;
                shapes.forEach((shape, index) => {
                    const speed = 0.1 + (index * 0.05);
                    shape.style.transform = `translateY(${scrolled * speed}px)`;
                });
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });
}());
