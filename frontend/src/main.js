// src/main.ts
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Ensure the router path is correct

/*
// 🔹 FontAwesome Imports
import { library } from '@fortawesome/fontawesome-svg-core';
import { faChevronUp, faChevronDown, faFileAlt, faVideo } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

// 🔹 Import FontAwesome CSS (for additional styles)
import '@fortawesome/fontawesome-free/css/all.css';

// Add icons to FontAwesome library
library.add(faChevronUp, faChevronDown, faFileAlt, faVideo);
*/

const app = createApp(App);

// Use the router
app.use(router);

// Register FontAwesome globally
// app.component('font-awesome-icon', FontAwesomeIcon);

// Mount the app
app.mount('#app');
