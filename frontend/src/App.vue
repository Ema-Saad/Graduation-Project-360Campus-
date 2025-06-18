<template>
  <div id="app">
    <!-- Conditionally render the Navbar based on the route -->
    <NavBar v-if="!shouldHideLayout" />
    <!-- Main content area where routed components will be rendered -->
    <div class="main-content">
      <router-view />
    </div>

    <!-- Conditionally render the Footer based on the route -->
    <Footer v-if="!shouldHideLayout" /> <!-- Render Footer for student routes -->
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useRoute } from "vue-router";
import { useGlobalStore } from '@/global_store.js';
import NavBar from "./components/NavBar.vue";
import Footer from "./components/FooterSection.vue";

export default defineComponent({
  name: "App",

  data() {
    const global_store = useGlobalStore();

    return {
      person_kind: computed(() => global_store.userinfo.person_type ?? ''),
    }
  },

  async created() {
    const global_store = useGlobalStore();

    this.$router.beforeEach((to, from) => {
      if (to.name !== 'Login' && !global_store.is_authenticated) return { name: 'Login' };
      else return true;
    });
  },

  methods: {
    async download_file(endpoint) {
      const global_store = useGlobalStore();
      await global_store.download_file();

    },
    async request_api_endpoint(endpoint: string, method: string, data?: any, headers?: any): Promise<any> {
      const global_store = useGlobalStore();
      return await global_store.request_api_endpoint(endpoint, method, data, headers);

    },
    async login(username: string, password: string): Promise<boolean> {
      const global_store = useGlobalStore();
      return await global_store.login(username, password);

    }
  },

  components: {
    NavBar,
    Footer,
  },
  setup() {
    const route = useRoute();

    // Pages where the navbar and footer should be hidden (for both student and doctor pages)
    const pagesWithoutLayout = new Set([
      "/login",
      "/forgot-password",
      "/reset-password",
      "/verification",
      "/congratulations",
      "/error", // Updated error page path
      "/doctor/login",
      "/doctor/forgot-password",
      "/doctor/reset-password",
      "/doctor/verification",
      "/doctor/congratulations",
      "/doctor/error" // Updated error page path for doctor
    ]);

    // Compute whether to hide the navbar and footer based on the current route
    const shouldHideLayout = computed(() => pagesWithoutLayout.has(route.path));

    return {
      shouldHideLayout,
    };
  },
});
</script>


<style scoped>
  #app {
    display: flex;
    flex-direction: column;
    height: 100vh; /* Make sure the page takes full height of the viewport */
  }

  .main-content {
    flex: 1; /* This ensures the main content area will expand to take up the available space */
    padding-bottom: 30px; /* Adds a small padding to avoid content touching the footer */
  }
</style>
