// Quantum Step - Real-Time Analytics Tracking
// ------------------------------------------

async function trackVisitor() {
    try {
        // 1. Get IP and Location Data
        const geoResponse = await fetch('https://ipapi.co/json/');
        const geoData = await geoResponse.json();

        // 2. Get Device & OS Data
        const ua = navigator.userAgent;
        const platform = navigator.platform;

        let deviceType = 'Desktop';
        if (/tablet|ipad/i.test(ua)) deviceType = 'Tablet';
        else if (/mobile|iphone|android/i.test(ua)) deviceType = 'Mobile';

        let os = 'Unknown OS';
        if (ua.indexOf('Win') !== -1) os = 'Windows';
        if (ua.indexOf('Mac') !== -1) os = 'MacOS';
        if (ua.indexOf('Linux') !== -1) os = 'Linux';
        if (ua.indexOf('Android') !== -1) os = 'Android';
        if (ua.indexOf('like Mac') !== -1) os = 'iOS';

        const visitorData = {
            timestamp: new Date().toISOString(),
            page: window.location.pathname,
            referrer: document.referrer || 'Direct',
            ip: geoData.ip,
            city: geoData.city,
            region: geoData.region,
            country: geoData.country_name,
            isp: geoData.org,
            device: deviceType,
            os: os,
            browser: getBrowserName(ua),
            screen_resolution: `${window.screen.width}x${window.screen.height}`
        };

        console.log('Quantum Analytics - Logged:', visitorData);

        // 3. Push to Supabase (Configured for Future)
        // pushToSupabase(visitorData);

        // Storage fallback for local testing
        saveLocalLog(visitorData);

    } catch (error) {
        console.warn('Analytics tracking failed:', error);
    }
}

function getBrowserName(ua) {
    if (ua.includes('Firefox')) return 'Firefox';
    if (ua.includes('SamsungBrowser')) return 'Samsung Browser';
    if (ua.includes('Opera') || ua.includes('OPR')) return 'Opera';
    if (ua.includes('Edge')) return 'Edge';
    if (ua.includes('Chrome')) return 'Chrome';
    if (ua.includes('Safari')) return 'Safari';
    return 'Unknown';
}

function saveLocalLog(data) {
    let logs = JSON.parse(localStorage.getItem('qs_analytics_logs') || '[]');
    logs.unshift(data);
    if (logs.length > 100) logs = logs.slice(0, 100); // Keep last 100
    localStorage.setItem('qs_analytics_logs', JSON.stringify(logs));
}

// Initial session tracking
if (document.readyState === 'complete') {
    trackVisitor();
} else {
    window.addEventListener('load', trackVisitor);
}
