// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBZMuRG_fQbpWMblW_NIUwSJW7NmPSwMKk",
  authDomain: "engageiq-vibe-777777.firebaseapp.com",
  databaseURL: "https://engageiq-vibe-777777-default-rtdb.firebaseio.com",
  projectId: "engageiq-vibe-777777",
  storageBucket: "engageiq-vibe-777777.firebasestorage.app",
  messagingSenderId: "375466830126",
  appId: "1:375466830126:web:0575cb349c745e4ad7b2bf"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export { app };
