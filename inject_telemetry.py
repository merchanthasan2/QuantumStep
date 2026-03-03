"""
Inject telemetry collector into all 5 tool pages.
Captures: IP, city, country, ISP, device type, OS, browser, screen, viewport,
timezone, language, referrer, UTM params, connection type.
"""

import glob, re

TELEMETRY_SCRIPT = '''<script id="qs-telemetry">
(function(){
    // Collect browser-side telemetry immediately
    function getDeviceType() {
        var ua = navigator.userAgent;
        if (/tablet|ipad|playbook|silk/i.test(ua)) return 'Tablet';
        if (/mobi|android|iphone|ipod|windows phone|blackberry|opera mini/i.test(ua)) return 'Mobile';
        return 'Desktop';
    }
    function getOS() {
        var ua = navigator.userAgent;
        if (/Windows NT 10/.test(ua)) return 'Windows 10/11';
        if (/Windows NT 6.3/.test(ua)) return 'Windows 8.1';
        if (/Windows NT 6.1/.test(ua)) return 'Windows 7';
        if (/Windows/.test(ua)) return 'Windows';
        if (/Mac OS X ([\\d_]+)/.test(ua)) return 'macOS ' + ua.match(/Mac OS X ([\\d_]+)/)[1].replace(/_/g,'.');
        if (/iPhone OS ([\\d_]+)/.test(ua)) return 'iOS ' + ua.match(/iPhone OS ([\\d_]+)/)[1].replace(/_/g,'.');
        if (/Android ([\\d.]+)/.test(ua)) return 'Android ' + ua.match(/Android ([\\d.]+)/)[1];
        if (/Linux/.test(ua)) return 'Linux';
        return 'Unknown';
    }
    function getBrowser() {
        var ua = navigator.userAgent;
        if (/Edg\\//.test(ua)) return 'Edge ' + (ua.match(/Edg\\/(\\d+)/)||['','?'])[1];
        if (/OPR\\/|Opera/.test(ua)) return 'Opera';
        if (/Chrome\\/(\\d+)/.test(ua) && !/Chromium/.test(ua)) return 'Chrome ' + ua.match(/Chrome\\/(\\d+)/)[1];
        if (/Firefox\\/(\\d+)/.test(ua)) return 'Firefox ' + ua.match(/Firefox\\/(\\d+)/)[1];
        if (/Safari\\/(\\d+)/.test(ua) && !/Chrome/.test(ua)) return 'Safari';
        if (/MSIE|Trident/.test(ua)) return 'Internet Explorer';
        return 'Other';
    }
    function getUTM() {
        var p = new URLSearchParams(location.search);
        return {
            source: p.get('utm_source') || '',
            medium: p.get('utm_medium') || '',
            campaign: p.get('utm_campaign') || ''
        };
    }
    var utm = getUTM();
    var tel = {
        device_type: getDeviceType(),
        os: getOS(),
        browser: getBrowser(),
        user_agent: navigator.userAgent,
        screen: screen.width + 'x' + screen.height,
        viewport: window.innerWidth + 'x' + window.innerHeight,
        language: navigator.language || '',
        timezone: Intl && Intl.DateTimeFormat ? Intl.DateTimeFormat().resolvedOptions().timeZone : '',
        connection: (navigator.connection && navigator.connection.effectiveType) || '',
        referrer: document.referrer || 'direct',
        landing_url: location.href,
        utm_source: utm.source,
        utm_medium: utm.medium,
        utm_campaign: utm.campaign,
        ip: '', city: '', region: '', country: '', isp: '', lat: '', lon: ''
    };

    // Fetch IP + geo from free API (1000 req/day free)
    fetch('https://ipapi.co/json/')
        .then(function(r){ return r.json(); })
        .then(function(d){
            tel.ip      = d.ip || '';
            tel.city    = d.city || '';
            tel.region  = d.region || '';
            tel.country = d.country_name || '';
            tel.isp     = d.org || '';
            tel.lat     = d.latitude || '';
            tel.lon     = d.longitude || '';
        })
        .catch(function(){}) // Silently fail if blocked
        .finally(function(){
            sessionStorage.setItem('qs_telemetry', JSON.stringify(tel));
        });

    // Store immediately even without geo (geo updates async)
    sessionStorage.setItem('qs_telemetry', JSON.stringify(tel));

    // Expose for use by loggers
    window.qsGetTelemetry = function() {
        try { return JSON.parse(sessionStorage.getItem('qs_telemetry') || '{}'); }
        catch(e) { return {}; }
    };
})();
</script>'''

# Tool files
files = glob.glob(r'd:\\Vibe Code\\Quantum Step\\tool-*.html')

for fp in files:
    fname = fp.split('\\')[-1]
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'qs-telemetry' in html:
        print(f'SKIP: {fname}')
        continue

    # Insert telemetry script right after <head> open or before </head>
    html = html.replace('</head>', TELEMETRY_SCRIPT + '\n</head>', 1)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'OK: {fname}')

print('\nDone.')
