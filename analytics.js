// Quantum Step - Real-Time Analytics Tracking
import { db, ref, push, set } from './firebase-config.js';

async function trackVisitor() {
    // Only track once per session
    if (sessionStorage.getItem('qs_analytics_tracked')) return;

    try {
        // 1. Get IP and Location Data
        let geoData = { ip: 'Unknown', city: 'Unknown', region: 'Unknown', country_name: 'Unknown', org: 'Unknown' };
        try {
            const geoResponse = await fetch('https://ipapi.co/json/');
            geoData = await geoResponse.json();
        } catch (e) { console.warn("Geo IP fetch failed"); }

        // 2. Get Device & OS Data
        const ua = navigator.userAgent;
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

        // 3. Push to Firebase
        const newDocRef = push(ref(db, 'analytics'));
        await set(newDocRef, visitorData);

        // Mark as tracked for session
        sessionStorage.setItem('qs_analytics_tracked', 'true');
        console.log('Quantum Analytics - Logged to Firebase');

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

if (document.readyState === 'complete') {
    trackVisitor();
} else {
    window.addEventListener('load', trackVisitor);
}
