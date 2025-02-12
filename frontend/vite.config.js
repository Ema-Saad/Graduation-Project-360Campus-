import { fileURLToPath, URL } from 'node:url';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    fs: {
      allow: [
        '/node_modules', // Allow node_modules
        'D:/Student/node_modules', // Allow node_modules from this path
        'D:/Student/vueproject5/src', // Allow src directory
      ],
    },
  },
});
