<template>
  <!-- Conditionally render the Navbar and Footer based on the route -->
  <NavBar v-if="!shouldHideNavBar" />

  <!-- Main content area where routed components will be rendered -->
  <div class="main-content">
    <router-view />
  </div>

  <Footer v-if="!shouldHideFooter" />
</template>

<script lang="ts">
  import { defineComponent, computed } from "vue";
  import { useRoute } from "vue-router";
  import NavBar from "./components/NavBar.vue";
  import Footer from "./components/FooterSection.vue";
  import axios from 'axios';

  export default defineComponent({
    name: "App",
    data() {
      return {
        authtoken: '',
      }
    },
    methods: {
      async login(username, password) {
        try {
          let response = await axios.post('http://127.0.0.1:8000/api/auth/login', { username, password });
          
          if (response.status === 200) {

            this.authtoken = response.data['token'];
            return true;

          } else {

            return false;
          }
        } catch (err) {
          throw err;
        }
      }
    },
    components: {
      NavBar,
      Footer,
    },
    setup() {
      const route = useRoute();

      // Pages where the navbar and footer should be hidden
      const authPages = [
        "/login",
        "/forgot-password",
        "/reset-password",
        "/verification",
        "/congratulations",
      ];

      // Define error pages or paths where navbar and footer should be hidden
      const errorPages = ["/error-page"];

      // Compute whether to hide the navbar based on the current route
      const shouldHideNavBar = computed(() => {
        return authPages.includes(route.path) || errorPages.includes(route.path);
      });

      // Compute whether to hide the footer based on the current route
      const shouldHideFooter = computed(() => {
        return authPages.includes(route.path) || errorPages.includes(route.path);
      });

      return {
        shouldHideNavBar,
        shouldHideFooter,
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
