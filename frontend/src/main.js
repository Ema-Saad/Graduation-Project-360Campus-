// src/main.ts
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Adjust path if necessary

const app = createApp(App);

// Use the router
app.use(router);

// Mount the app
app.mount('#app');
