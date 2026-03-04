
import { initializeApp } from "firebase/app";
import { getDatabase, ref, get, update } from "firebase/database";

const firebaseConfig = {
    apiKey: "AIzaSyBZMuRG_fQbpWMblW_NIUwSJW7NmPSwMKk",
    authDomain: "engageiq-vibe-777777.firebaseapp.com",
    projectId: "engageiq-vibe-777777",
    storageBucket: "engageiq-vibe-777777.firebasestorage.app",
    messagingSenderId: "375466830126",
    appId: "1:375466830126:web:0575cb349c745e4ad7b2bf",
    databaseURL: "https://engageiq-vibe-777777-default-rtdb.firebaseio.com"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

async function upgradeUser(email) {
    const usersRef = ref(db, 'users');
    const snapshot = await get(usersRef);
    const users = snapshot.val();

    if (!users) {
        console.log("No users found.");
        process.exit(1);
    }

    let targetUid = null;
    for (const uid in users) {
        if (users[uid].email === email) {
            targetUid = uid;
            break;
        }
    }

    if (targetUid) {
        await update(ref(db, `users/${targetUid}`), {
            plan: 'Pro',
            role: 'super_admin'
        });
        console.log(`Successfully upgraded ${email} (${targetUid}) to Pro plan with super_admin role.`);
    } else {
        console.log(`User with email ${email} not found.`);
    }
    process.exit(0);
}

upgradeUser('happy143@gmail.com');
