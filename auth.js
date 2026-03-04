import { auth, db, createUserWithEmailAndPassword, signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup, sendEmailVerification, ref, set, onAuthStateChanged } from './firebase-config.js';

// Elements
const authForm = document.getElementById('auth-form');
const authTitle = document.getElementById('auth-title');
const authSubmitBtn = document.getElementById('auth-submit-btn');
const toggleAuthModeLink = document.getElementById('toggle-auth-mode');
const toggleText = document.getElementById('toggle-text');
const nameGroup = document.getElementById('name-group');

const nameInput = document.getElementById('auth-name');
const emailInput = document.getElementById('auth-email');
const passwordInput = document.getElementById('auth-password');
const googleSignInBtn = document.getElementById('google-signin-btn');
const authMessage = document.getElementById('auth-message');

let isLoginMode = true;

// Toggle Login / Register
toggleAuthModeLink.addEventListener('click', (e) => {
    e.preventDefault();
    isLoginMode = !isLoginMode;

    if (isLoginMode) {
        authTitle.innerText = "Sign In to EngageIQ";
        authSubmitBtn.innerText = "Sign In";
        toggleText.innerText = "Don't have an account? ";
        toggleAuthModeLink.innerText = "Sign Up";
        nameGroup.style.display = "none";
        nameInput.removeAttribute("required");
    } else {
        authTitle.innerText = "Create an Account";
        authSubmitBtn.innerText = "Sign Up";
        toggleText.innerText = "Already have an account? ";
        toggleAuthModeLink.innerText = "Sign In";
        nameGroup.style.display = "block";
        nameInput.setAttribute("required", "true");
    }
    authMessage.innerText = "";
    authMessage.className = "auth-message";
});

function showMessage(msg, type = 'error') {
    authMessage.innerText = msg;
    authMessage.className = `auth-message ${type}`;
}

async function handleAuthSubmit(e) {
    e.preventDefault();
    const email = emailInput.value;
    const password = passwordInput.value;
    const name = nameInput.value;

    authSubmitBtn.disabled = true;
    authSubmitBtn.innerText = "Processing...";

    try {
        if (isLoginMode) {
            // LOGIN
            const userCredential = await signInWithEmailAndPassword(auth, email, password);
            if (!userCredential.user.emailVerified) {
                showMessage("Please verify your email address to log in.", "warning");
                authSubmitBtn.disabled = false;
                authSubmitBtn.innerText = "Sign In";
                return;
            }
            showMessage("Login successful! Redirecting...", "success");
            setTimeout(() => {
                window.location.href = "dashboard.html";
            }, 1000);
        } else {
            // REGISTER
            const userCredential = await createUserWithEmailAndPassword(auth, email, password);
            const user = userCredential.user;

            // Send verification email
            await sendEmailVerification(user);

            // Save user profile in DB (Default Tier = Free)
            await set(ref(db, 'users/' + user.uid), {
                name: name,
                email: email,
                plan: 'Free',
                createdAt: new Date().toISOString()
            });

            showMessage("Registration successful! Please check your email to verify your account.", "success");
            setTimeout(() => {
                // Switch back to login mode
                toggleAuthModeLink.click();
            }, 3000);
        }
    } catch (error) {
        showMessage(error.message, "error");
    } finally {
        if (!isLoginMode) {
            authSubmitBtn.innerText = "Sign Up";
        } else {
            authSubmitBtn.innerText = "Sign In";
        }
        authSubmitBtn.disabled = false;
    }
}

async function handleGoogleSignIn() {
    const provider = new GoogleAuthProvider();
    try {
        const result = await signInWithPopup(auth, provider);
        const user = result.user;

        // Check if user exists, if not, create Free plan basic record
        // By just saving it, it might overwrite if we don't check, but set() overwrites.
        // For a safe approach, we can update or set only essential fields without overwriting everything.
        // We will just do a blind set for now or check first.

        // More robust:
        import('https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js').then(async (module) => {
            const { get } = module;
            const snapshot = await get(ref(db, 'users/' + user.uid));
            if (!snapshot.exists()) {
                await set(ref(db, 'users/' + user.uid), {
                    name: user.displayName || 'Google User',
                    email: user.email,
                    plan: 'Free',
                    createdAt: new Date().toISOString()
                });
            }
        });

        showMessage("Google Sign-In successful! Redirecting...", "success");
        setTimeout(() => {
            window.location.href = "dashboard.html";
        }, 1000);
    } catch (error) {
        showMessage(error.message, "error");
    }
}

authForm.addEventListener('submit', handleAuthSubmit);
googleSignInBtn.addEventListener('click', handleGoogleSignIn);

// Optional: check if already logged in and verified
onAuthStateChanged(auth, (user) => {
    if (user && user.emailVerified) {
        // Automatically redirect to dash if already valid session
        window.location.href = "dashboard.html";
    }
});
