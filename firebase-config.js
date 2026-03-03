// Firebase configuration and initialization for EngageIQ
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getDatabase, ref, onValue, set, update, push, child } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";

const firebaseConfig = {
    projectId: "engageiq-vibe-777777",
    appId: "1:375466830126:web:0575cb349c745e4ad7b2bf",
    storageBucket: "engageiq-vibe-777777.firebasestorage.app",
    apiKey: "AIzaSyBZMuRG_fQbpWMblW_NIUwSJW7NmPSwMKk",
    authDomain: "engageiq-vibe-777777.firebaseapp.com",
    messagingSenderId: "375466830126",
    projectNumber: "375466830126",
    databaseURL: "https://engageiq-vibe-777777-default-rtdb.firebaseio.com"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

export { db, ref, onValue, set, update, push, child };
