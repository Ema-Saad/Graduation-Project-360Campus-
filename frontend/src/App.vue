<template>
  <div id="app">
    <!-- Conditionally render the Navbar and Footer based on the route -->
    <NavBar v-if="!shouldHideLayout" />

    <!-- Main content area where routed components will be rendered -->
    <div class="main-content">
      <router-view />
    </div>

    <Footer v-if="!shouldHideLayout" />
  </div>
</template>

<script lang="ts">
  import { defineComponent, computed } from "vue";
  import { useRoute } from "vue-router";
  import NavBar from "./components/NavBar.vue";
  import Footer from "./components/FooterSection.vue";

  export default defineComponent({
    name: "App",
    components: {
      NavBar,
      Footer,
    },
    setup() {
      const route = useRoute();

      // Pages where the navbar and footer should be hidden
      const pagesWithoutLayout = new Set([
        "/login",
        "/forgot-password",
        "/reset-password",
        "/verification",
        "/congratulations",
        "/error" // Updated error page path
      ]);

      // Compute whether to hide the navbar and footer based on the current route
      const shouldHideLayout = computed(() => pagesWithoutLayout.has(route.path));

      return {
        shouldHideLayout
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
