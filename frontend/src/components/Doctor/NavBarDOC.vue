<template>
  <!-- Navbar -->
  <nav class="navbar">
    <!-- Logo on the left -->
    <div class="logo">
      <img src="@/assets/logoa.png" alt="Logo" />
    </div>

    <!-- Nav links (buttons) in the middle -->
    <div class="nav-links">
      <router-link :to="'/doctor'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor') }">Home</router-link>

      <router-link :to="'/doctor-materials'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-materials') }">Materials</router-link>

      <router-link :to="'/doctor-myclass'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-myclass') }">My Class</router-link>

      <router-link :to="'/doctor-timetable'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-timetable') }">Time Table</router-link>

      <router-link :to="'/doctor-events'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-events') }">Events</router-link>

      <router-link :to="'/doctor-graduation'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-graduation') }">Graduation Project</router-link>

      <router-link :to="'/doctor-map'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-map') }">Map</router-link>
    </div>

    <!-- Search bar and Profile button on the right -->
    <div class="actions">
      <div class="search-container">
        <input type="text" v-model="searchQuery" placeholder="Search..." />
        <i class="fas fa-search search-icon"></i>
      </div>

      <div class="profile-dropdown">
        <button @click="toggleDropdown" class="profile-btn">
          <i class="fas fa-user-circle" style="font-size: 40px; color: #0a35ae;"></i>
        </button>

        <div v-if="dropdownOpen" class="dropdown-menu">
          <h4>Dr. John Doe</h4>
          <button @click="goToProfile">
            <i class="fas fa-user"></i> My Profile
          </button>
          <button @click="goToSettings">
            <i class="fas fa-cog"></i> Settings
          </button>
          <button @click="logout">
            <i class="fas fa-sign-out-alt"></i> Logout
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu Toggle -->
    <button class="mobile-menu-toggle" @click="toggleMobileMenu">☰</button>
  </nav>

  <!-- Mobile Nav Links (visible on smaller screens) -->
  <div v-if="mobileMenuOpen" class="mobile-nav-dropdown">
    <div class="mobile-nav-links">
      <router-link :to="'/doctor'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor') }">Home</router-link>

      <router-link :to="'/doctor-materials'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-materials') }">Materials</router-link>

      <router-link :to="'/doctor-myclass'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-myclass') }">My Class</router-link>

      <router-link :to="'/doctor-timetable'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-timetable') }">Time Table</router-link>

      <router-link :to="'/doctor-events'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-events') }">Events</router-link>

      <router-link :to="'/doctor-graduation'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-graduation') }">Graduation Project</router-link>

      <router-link :to="'/doctor-map'"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('/doctor-map') }">Map</router-link>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        searchQuery: '',
        mobileMenuOpen: false,
        dropdownOpen: false
      };
    },
    computed: {
      isActive() {
        return (route) => {
          return this.$route.path === route;
        };
      }
    },
    methods: {
      goToProfile() {
        this.dropdownOpen = false;
        this.closeMobileMenu();
        this.$router.push('/doctor-profile'); // Updated path
      },
      goToSettings() {
        this.dropdownOpen = false;
        this.closeMobileMenu();
        this.$router.push('/doctor-settings'); // Updated path
      },
      toggleMobileMenu() {
        this.mobileMenuOpen = !this.mobileMenuOpen;
      },
      closeMobileMenu() {
        this.mobileMenuOpen = false;
      },
      toggleDropdown() {
        this.dropdownOpen = !this.dropdownOpen;
      },
      logout() {
        localStorage.removeItem('auth-token');
        this.dropdownOpen = false;
        this.$router.push('/doctor/login'); // Ensure this route exists
      }
    }
  };
</script>



<style scoped>
  /* Basic Navbar Styles */
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    background-color: white;
    color: black;
    border-bottom: 1px solid #ccc;
    position: relative;
  }

  .logo img {
    height: 40px;
  }

  .nav-links {
    display: flex;
    gap: 15px;
  }

    .nav-links a {
      text-decoration: none;
      color: black;
      font-size: 16px;
      cursor: pointer;
      padding: 10px;
      transition: color 0.3s ease;
    }

      .nav-links a:hover {
        color: blue;
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        transition: color 0.3s ease, text-shadow 0.3s ease;
      }

  .active-link {
    color: orange !important;
  }

  .actions {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .search-container {
    position: relative;
  }

    .search-container input {
      padding: 8px 30px 8px 10px;
      font-size: 16px;
      border-radius: 5px;
      border: 1px solid #ccc;
      width: 200px;
      background-color: #fff2e3;
    }

  .search-icon {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 16px;
    color: gray;
  }

  .profile-btn {
    background-color: transparent;
    border: none;
    cursor: pointer;
  }

  .dropdown-menu {
    position: absolute;
    top: 100%;
    right: 0;
    background-color: #fff2e3;
    border: 1px solid #ccc;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    z-index: 100;
    padding: 25px;
    display: flex;
    flex-direction: column;
    min-width: 250px;
    font-size: 20px;
    color: rgb(0, 0, 0);
  }

    .dropdown-menu button {
      background-color: transparent;
      border: none;
      padding: 10px;
      text-align: left;
      cursor: pointer;
      color: black;
    }

      .dropdown-menu button:hover {
        background-color: orange;
        color: black;
      }

    .dropdown-menu i {
      font-size: 24px;
      margin-right: 8px;
    }

  /* Mobile Navbar Styles */
  .mobile-menu-toggle {
    display: none;
    font-size: 24px;
    background: none;
    border: none;
    cursor: pointer;
  }

  @media screen and (max-width: 768px) {
    .nav-links {
      display: none;
    }

    .mobile-menu-toggle {
      display: block;
    }

    .actions input {
      width: 150px;
    }
  }

  @media screen and (max-width: 480px) {
    .actions input {
      width: 120px;
    }
  }

  .mobile-nav-links {
    position: absolute;
    top: 70px;
    right: 10px;
    background-color: #fff2e3;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    z-index: 200;
    padding: 15px;
    width: 200px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

    .mobile-nav-links a {
      color: black;
      font-size: 16px;
      padding: 10px;
      text-decoration: none;
      border-radius: 5px;
      transition: background-color 0.3s;
    }

      .mobile-nav-links a:hover {
        background-color: orange;
        color: black;
      }

    .mobile-nav-links button {
      background-color: white;
      color: black;
      font-size: 16px;
      padding: 10px;
      border: none;
      text-align: left;
      cursor: pointer;
    }

      .mobile-nav-links button:hover {
        color: gray;
      }
</style>
