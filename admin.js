import { auth, db, ref, onValue, set, update, onAuthStateChanged, signOut } from './firebase-config.js';

// DOM Elements
const accessDeniedOverlay = document.getElementById('access-denied');
const adminContent = document.getElementById('admin-content');
const adminEmailDisplay = document.getElementById('admin-email-display');
const logoutBtn = document.getElementById('logout-btn');

// Tabs
const tabBtns = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

// Tables & KPIs
const usersTableBody = document.getElementById('users-table-body');
const analyticsTableBody = document.getElementById('analytics-table-body');
const kpiTotalHits = document.getElementById('kpi-total-hits');
const kpiUniqueVisitors = document.getElementById('kpi-unique-visitors');
const kpiMobileUsers = document.getElementById('kpi-mobile-users');

// 1. Authenticate and verify Super Admin Role
onAuthStateChanged(auth, async (user) => {
    if (!user) {
        showAccessDenied("Access Denied", "You must be logged in to view this page. Redirecting...");
        setTimeout(() => window.location.href = "auth.html", 2000);
        return;
    }

    // Check role in DB
    const userRef = ref(db, 'users/' + user.uid);
    onValue(userRef, (snapshot) => {
        const userData = snapshot.val();
        if (userData && userData.role === 'super_admin') {
            // Authorized!
            accessDeniedOverlay.style.display = 'none';
            adminContent.style.display = 'block';
            adminEmailDisplay.textContent = user.email;

            // Load Data
            loadUsers();
            loadAnalytics();
        } else {
            showAccessDenied("Restricted Area", "You do not have Super Admin privileges.");
        }
    }, { onlyOnce: true });
});

function showAccessDenied(title, msg) {
    accessDeniedOverlay.innerHTML = `<h1>${title}</h1><p>${msg}</p>`;
    accessDeniedOverlay.style.display = 'flex';
    adminContent.style.display = 'none';
}

// 2. Tab Navigation
tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Remove active class from all
        tabBtns.forEach(b => b.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));

        // Add active to clicked
        btn.classList.add('active');
        document.getElementById(`tab-${btn.dataset.target}`).classList.add('active');
    });
});

// 3. Logout
logoutBtn.addEventListener('click', async () => {
    await signOut(auth);
    window.location.href = "auth.html";
});

// 4. Load & Manage Users
function loadUsers() {
    const usersRef = ref(db, 'users');
    onValue(usersRef, (snapshot) => {
        usersTableBody.innerHTML = "";
        const data = snapshot.val();

        if (!data) {
            usersTableBody.innerHTML = `<tr><td colspan="6" style="text-align: center;">No users found.</td></tr>`;
            return;
        }

        Object.keys(data).forEach(uid => {
            const user = data[uid];
            const date = new Date(user.createdAt).toLocaleDateString();

            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${date}</td>
                <td>${user.name || 'Anonymous'}</td>
                <td>${user.email}</td>
                <td><span style="background: ${user.role === 'super_admin' ? '#fecaca' : '#e2e8f0'}; color: ${user.role === 'super_admin' ? '#991b1b' : '#334155'}; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold;">${user.role || 'user'}</span></td>
                <td>
                    <select class="tier-select" data-uid="${uid}" ${user.role === 'super_admin' ? 'disabled' : ''}>
                        <option value="Free" ${user.plan === 'Free' ? 'selected' : ''}>Free</option>
                        <option value="Starter" ${user.plan === 'Starter' ? 'selected' : ''}>Starter</option>
                        <option value="Pro" ${user.plan === 'Pro' ? 'selected' : ''}>Pro</option>
                        <option value="Enterprise" ${user.plan === 'Enterprise' ? 'selected' : ''}>Enterprise</option>
                    </select>
                </td>
                <td>
                    <button class="btn-update-tier" style="background: #a78bfa; color:#000; border:none; padding:4px 10px; border-radius:4px; font-weight:bold; cursor:pointer;" data-uid="${uid}" ${user.role === 'super_admin' ? 'disabled' : ''}>Save Tier</button>
                    <!-- Future: <button>View Payments</button> -->
                </td>
            `;
            usersTableBody.appendChild(tr);
        });

        // Add Event Listeners to the new buttons
        document.querySelectorAll('.btn-update-tier').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const uid = e.target.dataset.uid;
                const select = document.querySelector(`select.tier-select[data-uid="${uid}"]`);
                const newTier = select.value;

                // Update Firebase
                update(ref(db, `users/${uid}`), {
                    plan: newTier
                }).then(() => {
                    e.target.innerText = "Saved!";
                    e.target.style.background = "#86efac";
                    setTimeout(() => {
                        e.target.innerText = "Save Tier";
                        e.target.style.background = "#a78bfa";
                    }, 2000);
                }).catch(err => alert("Failed to update tier: " + err.message));
            });
        });
    });
}

// 5. Load Analytics Data
function loadAnalytics() {
    const analyticsRef = ref(db, 'analytics');
    onValue(analyticsRef, (snapshot) => {
        const data = snapshot.val();
        analyticsTableBody.innerHTML = "";

        if (!data) {
            analyticsTableBody.innerHTML = `<tr><td colspan="6" style="text-align: center;">No traffic data yet.</td></tr>`;
            kpiTotalHits.textContent = "0";
            kpiUniqueVisitors.textContent = "0";
            kpiMobileUsers.textContent = "0%";
            return;
        }

        let totalHits = 0;
        let mobileHits = 0;
        const uniqueIps = new Set();

        // Sort keys by reverse timestamp (newest first)
        const entries = Object.values(data).sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

        entries.forEach(log => {
            totalHits++;
            uniqueIps.add(log.ip);
            if (log.device === 'Mobile' || log.device === 'Tablet') mobileHits++;

            const date = new Date(log.timestamp).toLocaleString();
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td style="font-size: 0.85rem;">${date}</td>
                <td>${log.page.replace('/', '') || 'Index'}</td>
                <td><div>${log.city}, ${log.country}</div><div style="font-size: 0.75rem; color:#64748b;">IP: ${log.ip}</div></td>
                <td><div>${log.device}</div><div style="font-size: 0.75rem; color:#64748b;">${log.os} / ${log.browser}</div></td>
                <td>${log.isp || 'Unknown'}</td>
                <td style="font-size: 0.85rem; max-width: 150px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${log.referrer}">${log.referrer}</td>
            `;
            analyticsTableBody.appendChild(tr);
        });

        // Update KPIs
        kpiTotalHits.textContent = totalHits;
        kpiUniqueVisitors.textContent = uniqueIps.size;
        kpiMobileUsers.textContent = totalHits > 0 ? Math.round((mobileHits / totalHits) * 100) + "%" : "0%";
    });
}

// 6. Tier Management
const DEFAULT_TIERS = {
    Free: { label: 'Free', icon: '🆓', maxSessions: 3, maxParticipants: 30, color: '#64748b' },
    Starter: { label: 'Starter', icon: '🚀', maxSessions: 10, maxParticipants: 200, color: '#6366f1' },
    Pro: { label: 'Pro', icon: '⭐', maxSessions: 50, maxParticipants: 1000, color: '#7C3AED' },
    Enterprise: { label: 'Enterprise', icon: '🏛️', maxSessions: 999, maxParticipants: 9999, color: '#f59e0b' }
};

function loadTiers() {
    const container = document.getElementById('tiers-container');
    if (!container) return;

    const tiersRef = ref(db, 'config/tiers');
    onValue(tiersRef, (snap) => {
        const saved = snap.val() || {};
        const tiers = { ...DEFAULT_TIERS };
        // Merge saved values
        Object.keys(tiers).forEach(key => {
            if (saved[key]) tiers[key] = { ...tiers[key], ...saved[key] };
        });

        container.innerHTML = Object.entries(tiers).map(([key, tier]) => `
            <div style="background:#0f172a;border:1px solid #334155;border-radius:12px;padding:1.25rem;display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap;">
                <div style="font-size:2rem;">${tier.icon}</div>
                <div style="flex:1;min-width:120px;">
                    <div style="font-weight:800;font-size:1.1rem;color:${tier.color};">${tier.label}</div>
                    <div style="font-size:0.8rem;color:#64748b;">Plan Tier</div>
                </div>
                <div style="display:flex;gap:1rem;flex-wrap:wrap;align-items:flex-end;">
                    <div>
                        <label style="display:block;font-size:0.7rem;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Max Sessions</label>
                        <input type="number" id="tier-${key}-sessions" value="${tier.maxSessions}" min="1"
                            style="width:100px;background:#1e293b;border:1px solid #475569;color:white;padding:0.5rem 0.75rem;border-radius:8px;outline:none;font-size:1rem;font-weight:700;">
                    </div>
                    <div>
                        <label style="display:block;font-size:0.7rem;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Max Participants</label>
                        <input type="number" id="tier-${key}-participants" value="${tier.maxParticipants}" min="1"
                            style="width:120px;background:#1e293b;border:1px solid #475569;color:white;padding:0.5rem 0.75rem;border-radius:8px;outline:none;font-size:1rem;font-weight:700;">
                    </div>
                </div>
            </div>
        `).join('');
    }, { onlyOnce: true });
}

window.saveTiers = () => {
    const tiers = {};
    Object.keys(DEFAULT_TIERS).forEach(key => {
        const sessions = document.getElementById(`tier-${key}-sessions`)?.value;
        const participants = document.getElementById(`tier-${key}-participants`)?.value;
        if (sessions && participants) {
            tiers[key] = { maxSessions: Number(sessions), maxParticipants: Number(participants) };
        }
    });
    set(ref(db, 'config/tiers'), tiers).then(() => {
        const msg = document.getElementById('tiers-save-msg');
        if (msg) { msg.style.display = 'inline'; setTimeout(() => msg.style.display = 'none', 3000); }
    }).catch(err => alert('Save failed: ' + err.message));
};

window.saveUserOverride = () => {
    const email = document.getElementById('override-email')?.value.trim();
    const maxSessions = Number(document.getElementById('override-max-sessions')?.value);
    const maxParticipants = Number(document.getElementById('override-max-participants')?.value);
    if (!email || !maxSessions || !maxParticipants) { alert('Please fill all fields.'); return; }

    // Find user by email in DB
    onValue(ref(db, 'users'), (snap) => {
        const users = snap.val() || {};
        const uid = Object.keys(users).find(k => users[k].email === email);
        if (!uid) { alert('User not found with that email.'); return; }
        update(ref(db, `users/${uid}`), { maxSessions, maxParticipants }).then(() => {
            const msg = document.getElementById('override-save-msg');
            if (msg) { msg.style.display = 'inline'; setTimeout(() => msg.style.display = 'none', 3000); }
        }).catch(err => alert('Override failed: ' + err.message));
    }, { onlyOnce: true });
};

// Call loadTiers when admin is authorized (patching into the onValue callback)
const _origLoadUsers = loadUsers;
const tiersTabBtn = document.querySelector('.tab-btn[data-target="tiers"]');
if (tiersTabBtn) {
    tiersTabBtn.addEventListener('click', loadTiers);
}

// 7. Feedback Management
const feedbackTabBtn = document.querySelector('.tab-btn[data-target="feedback"]');
if (feedbackTabBtn) {
    feedbackTabBtn.addEventListener('click', loadFeedback);
}

window.loadFeedback = function () {
    const list = document.getElementById('feedback-list');
    const filter = document.getElementById('feedback-session-filter')?.value;
    const publicOnly = document.getElementById('feedback-public-only')?.checked;
    if (!list) return;
    list.innerHTML = 'Loading...';

    onValue(ref(db, 'sessions'), (snap) => {
        const sessions = snap.val() || {};
        const allFeedback = [];

        // Populate session filter dropdown
        const filterSelect = document.getElementById('feedback-session-filter');
        if (filterSelect && filterSelect.options.length <= 1) {
            Object.entries(sessions).forEach(([id, s]) => {
                const opt = document.createElement('option');
                opt.value = id;
                opt.textContent = s.title || id;
                filterSelect.appendChild(opt);
            });
        }

        Object.entries(sessions).forEach(([sessionId, session]) => {
            if (filter && sessionId !== filter) return;
            const feedbacks = session.feedback || {};
            Object.entries(feedbacks).forEach(([fbKey, fb]) => {
                if (publicOnly && !fb.isPublic) return;
                allFeedback.push({ sessionId, sessionTitle: session.title, fbKey, ...fb });
            });
        });

        if (!allFeedback.length) {
            list.innerHTML = '<div style="text-align:center;color:#64748b;padding:2rem;">No feedback found.</div>';
            return;
        }

        // Sort newest first
        allFeedback.sort((a, b) => b.submittedAt - a.submittedAt);

        list.innerHTML = allFeedback.map(fb => `
            <div style="background:#0f172a;border:1px solid #334155;border-radius:12px;padding:1.25rem;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.75rem;">
                    <div>
                        <span style="font-size:1.5rem;">${fb.emoji || '—'}</span>
                        <strong style="color:#f1f5f9;margin-left:0.5rem;">${fb.participantName || 'Anonymous'}</strong>
                        <span style="color:#64748b;font-size:0.8rem;margin-left:0.5rem;">${fb.participantEmail || ''}</span>
                    </div>
                    <div style="display:flex;gap:0.5rem;align-items:center;">
                        <span style="background:${fb.isPublic ? 'rgba(16,185,129,0.1)' : 'rgba(100,116,139,0.1)'};color:${fb.isPublic ? '#10b981' : '#64748b'};border:1px solid ${fb.isPublic ? 'rgba(16,185,129,0.3)' : '#334155'};padding:2px 10px;border-radius:99px;font-size:0.75rem;font-weight:700;">${fb.isPublic ? '✓ Public' : 'Private'}</span>
                        <span style="color:#475569;font-size:0.75rem;">${new Date(fb.submittedAt).toLocaleDateString()}</span>
                    </div>
                </div>
                <div style="color:#cbd5e1;font-size:0.9rem;margin-bottom:0.5rem;">${fb.text || '<em style="color:#475569">No written comment</em>'}</div>
                <div style="font-size:0.75rem;color:#475569;margin-bottom:0.75rem;">Session: <strong style="color:#7C3AED;">${fb.sessionTitle || fb.sessionId}</strong></div>
                ${fb.adminReply ? `<div style="background:rgba(124,58,237,0.1);border-left:3px solid #7C3AED;padding:0.75rem;border-radius:4px;margin-bottom:0.75rem;"><span style="font-size:0.7rem;font-weight:800;color:#7C3AED;text-transform:uppercase;">Your Reply</span><br><span style="color:#c4b5fd;">${fb.adminReply}</span></div>` : ''}
                <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
                    <button onclick="toggleFeedbackPublic('${fb.sessionId}','${fb.fbKey}',${!fb.isPublic})" style="background:${fb.isPublic ? '#334155' : '#10b981'};color:white;border:none;padding:4px 12px;border-radius:6px;font-size:0.8rem;font-weight:700;cursor:pointer;">${fb.isPublic ? 'Make Private' : 'Make Public'}</button>
                    <button onclick="replyToFeedback('${fb.sessionId}','${fb.fbKey}')" style="background:#7C3AED;color:white;border:none;padding:4px 12px;border-radius:6px;font-size:0.8rem;font-weight:700;cursor:pointer;">Reply</button>
                </div>
            </div>
        `).join('');
    }, { onlyOnce: true });
};

window.toggleFeedbackPublic = (sessionId, fbKey, makePublic) => {
    update(ref(db, `sessions/${sessionId}/feedback/${fbKey}`), { isPublic: makePublic })
        .then(() => window.loadFeedback())
        .catch(err => alert('Error: ' + err.message));
};

window.replyToFeedback = (sessionId, fbKey) => {
    const reply = prompt('Your reply to this feedback:');
    if (reply === null) return;
    update(ref(db, `sessions/${sessionId}/feedback/${fbKey}`), { adminReply: reply })
        .then(() => window.loadFeedback())
        .catch(err => alert('Error: ' + err.message));
};
