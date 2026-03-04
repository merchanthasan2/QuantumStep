import fs from 'fs';

let content = fs.readFileSync('pricing.html', 'utf-8');

// Theming replacements
const replacements = [
    [/background-color:\s*#fafbfc;/g, 'background-color: #020617;'],
    [/color:\s*#0f172a;/g, 'color: #f8fafc;'],
    [/background:\s*#fafbfc;/g, 'background: #020617;'],
    [/background:\s*white;/g, 'background: rgba(15, 23, 42, 0.6);\n            backdrop-filter: blur(12px);\n            -webkit-backdrop-filter: blur(12px);\n            border: 1px solid rgba(255, 255, 255, 0.05);'],

    // Background override for the popular card border
    [/border:\s*2px solid #6366f1;/g, 'border: 2px solid #8b5cf6;'],

    // Text colors
    // Original cbd5e1 -> 64748b (darker slate)
    [/color:\s*#cbd5e1;/g, 'color: #64748b;'],
    // Original 64748b -> 94a3b8
    [/color:\s*#64748b;/g, 'color: #a78bfa;'],
    // Original 475569 -> cbd5e1
    [/color:\s*#475569;/g, 'color: #cbd5e1;'],
    // Original 1e293b -> f8fafc
    [/color:\s*#1e293b;/g, 'color: #f8fafc;'],

    // Secondary button styles
    [/background:\s*#fff;\s*border:\s*1px solid #e2e8f0;/g, 'background: rgba(255, 255, 255, 0.05);\n            border: 1px solid rgba(255, 255, 255, 0.1);'],
    [/border-color:\s*#cbd5e1;\s*background:\s*#f8fafc;/g, 'border-color: rgba(255, 255, 255, 0.2);\n            background: rgba(255, 255, 255, 0.1);'],

    // Table 
    [/border-bottom:\s*1px solid #f1f5f9;/g, 'border-bottom: 1px solid rgba(255, 255, 255, 0.05);'],

    // Badges
    [/background:\s*#f1f5f9;/g, 'background: rgba(255, 255, 255, 0.1);']
];

for (const [regex, replacement] of replacements) {
    content = content.replace(regex, replacement);
}

fs.writeFileSync('pricing.html', content);
console.log('Successfully applied dark theme colors to pricing!');
