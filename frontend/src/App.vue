<template>
  <div id="app">
    <!-- Conditionally render the Navbar based on the route -->
    <NavBarStudent v-if="!shouldHideLayout && !isDoctor" />
    <NavBarDoctor v-if="!shouldHideLayout && isDoctor" /> <!-- Render NavBarDoctor for doctor routes -->
    <!-- Main content area where routed components will be rendered -->
    <div class="main-content">
      <router-view />
    </div>

    <!-- Conditionally render the Footer based on the route -->
    <Footer v-if="!shouldHideLayout && !isDoctor" /> <!-- Render Footer for student routes -->
    <FooterDOC v-if="!shouldHideLayout && isDoctor" /> <!-- Render FooterDOC for doctor routes -->
  </div>
</template>

<script lang="ts">
  import { defineComponent, computed } from "vue";
  import { useRoute } from "vue-router";
  import NavBarStudent from "./components/Student/NavBar.vue";
  import NavBarDoctor from "./components/Doctor/NavBarDOC.vue";  // Import doctor's navbar
  import Footer from "./components/Student/FooterSection.vue";
  import FooterDOC from "./components/Doctor/FooterDOC.vue"; // Import doctor's footer

  export default defineComponent({
    name: "App",
    components: {
      NavBarStudent,
      NavBarDoctor,
      Footer,
      FooterDOC, // Register FooterDOC component
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

      // Logic to choose the correct navbar based on the route
      const isDoctor = computed(() => route.path.startsWith('/doctor')); // This still checks for /doctor prefix

      return {
        shouldHideLayout,
        isDoctor
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
