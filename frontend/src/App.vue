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
import NavBar from "./components/NavBar.vue";
import Footer from "./components/FooterSection.vue";

export default defineComponent({
  name: "App",
  data() {
    return {
      authtoken: '',
      person_kind: '',
    }
  },
  async created() {
    let part = document.cookie
                      .split('; ')
                      .filter((p) => p.startsWith('authtoken='))[0];

    if (part) {
      this.authtoken = part.split('=')[1];

      const person_kind_response = await fetch('http://127.0.0.1:8000/api/role', {
        headers: {
          Authorization: `Token ${this.authtoken}`,
        }
      });

      const response_text = await person_kind_response.text();
      this.person_kind = response_text.substr(1, response_text.length - 2);
    }

    this.$router.beforeEach((to, from) => {
      if (to.name !== 'Login' && !this.authtoken) return { name: 'Login' };
      else return true;
    });
  },
  methods: {
    async download_file(endpoint) {
      try {
        if (!this.authtoken) {
          throw new Error("Authentication required");
        }

        const url = `http://127.0.0.1:8000/${endpoint}`;
        let options = {
          method: 'get',
          mode: 'cors',
          headers: {
            Authorization: `Token ${this.authtoken}`
          }
        };

        let response = await fetch(url, options);
        if (!response.ok)
          throw new Error(await response.text());

        let data = await response.blob();

        console.log(response);

        let filename = response.headers.get('Content-Disposition');
        filename = filename.split(';')[1];
        filename = filename.split('=')[1].replaceAll('\"', '');

        let dummy_element = document.createElement('a');
        dummy_element.href = window.URL.createObjectURL(data);
        dummy_element.download = filename;
        document.body.appendChild(dummy_element);
        dummy_element.click();
        dummy_element.remove();

      } catch(err) {
        throw err;
      }
    },
    async request_api_endpoint(endpoint: string, method: string, data?: any): Promise<any> {
      try {
        const url = `http://127.0.0.1:8000/${endpoint}`;
        
        // Only add the Authorization header if authtoken is non-empty.
        const headers: HeadersInit = {};
        if (this.authtoken) {
          headers["Authorization"] = `Token ${this.authtoken}`;
        }
        
        const options: RequestInit = {
          method: method,
          mode: 'cors',
          headers: headers,
        };

        if (data && method.toLowerCase() === 'get') {
          options.body = new URLSearchParams(data);
        } else if (data && method.toLowerCase() === 'post') {
          options.body = data;
        }
        const response = await fetch(url, options);
        
        // Optionally check for errors before returning the JSON.
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(JSON.stringify(errorData));
        }
        
        return await response.json();
      } catch (err) {
        throw err;
      }
    },
    async login(username: string, password: string): Promise<boolean> {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/auth/login', {
          method: 'POST',
          mode: 'cors',
          body: new URLSearchParams({ username, password }),
        });

        if (response.status === 200) {
          const data = await response.json();
          this.authtoken = data['token'];

          document.cookie = `authtoken=${this.authtoken}`;

          const person_kind_response = await fetch('http://127.0.0.1:8000/api/role', {
            headers: {
              Authorization: `Token ${this.authtoken}`,
            }
          });

          const response_text = await person_kind_response.text();
          this.person_kind = response_text.substr(1, response_text.length - 2);

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
