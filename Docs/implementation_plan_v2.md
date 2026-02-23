# Implementation Plan - Branding, Governance & SEO

This plan addresses the latest user feedback regarding branding, nomenclature, icon safety (SVG only), SEO indexing, and the addition of multiple high-end content sections.

## User Review Required
> [!IMPORTANT]
> - All emojis and font-based icons will be replaced with clean SVG paths for a premium look.
> - Section headers will be unified: "Expertise" -> "Services", "Our Work" -> "Portfolio".
> - New sections will follow the existing glassmorphic/aurora theme strictly.

## Proposed Changes

### [Branding & Content Expansion]

#### [MODIFY] [index.html](file:///d:/Vibe%20Code/Quantum%20Step/index.html)
- **Hero Update**:
  - Add a "Free Consultation" secondary button next to "Start Your Project".
- **AI Influence Section (New)**:
  - Position: Below Hero.
  - Content: "How We Use AI to Build Better Software?"
  - Features: Reliable Software, Smarter Features, Cost-Efficient Development.
  - Sidebar: Premium 3D render of a tech robot/phone interface.
- **Service Section (Grid Upgrade)**:
  - Transition to a 6-card layout for "Our Services".
  - Categories: Software Consulting, Custom Software Solutions, Web & Mobile App Development, SaaS & Cloud Platform Development, AI, IoT & Next-Gen Tech, Ongoing Support & Optimization.
- **Tech Focus & KPIs (New)**:
  - "Why Quantum Step for Enterprise Software Development?"
  - KPI Grid: 24+ Years of Expertise, 40% Average Cost Saving, 85% Faster Time-to-Market, 98% Client Retention Rate.
- **Engagement Models (New)**:
  - "Engagement Types – Choose How We Work Together".
  - Models: Dedicated Team, Staff Augmentation, Hybrid Model.
- **Tech Ecosystem (New)**:
  - "Powering Your Vision with the Latest Tech".
  - Floating logo orbit visual with React, Vue, Angular, Node, etc.

#### [MODIFY] [tool-home-loan-calculator.html](file:///d:/Vibe%20Code/Quantum%20Step/tool-home-loan-calculator.html)
- **Icon Audit**: Replace emojis with SVGs.
- **SEO**: Add specific meta tags for "Home Loan Calculator India".

### [Governance & Documentation]
- All plans and design decisions are mirrored in `/Docs`.
- Maintain `PDR.md` as the source of truth for architecture and branding.

## Verification Plan
### Automated Tests
- Check for non-ASCII characters (emojis) using grep patterns.
- Verify meta tags presence.
- Test responsive layout of the new 6-card grid.

### Manual Verification
- Visual walk-through of the new Sections to ensure theme consistency.
- Verify "Free Consultation" scroll-to-contact functionality.
