<template>
  <!-- Navbar -->
  <nav class="navbar">
    <!-- Logo on the left -->
    <div class="logo">
      <img src="@/assets/logo-icon.png" alt="Logo" />
    </div>

    <!-- Nav links (buttons) in the middle -->
    <div class="nav-links">
      <router-link :to="{ name: 'Home' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('Home') }">Home</router-link>

      <router-link :to="{ name: 'CourseList' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('CourseList') }">Materials</router-link>

      <router-link :to="{ name: 'ClassroomList' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('ClassroomList') }">My Class</router-link>

      <router-link :to="{ name: 'TimeTable' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('TimeTable') }">Time Table</router-link>

      <router-link :to="{ name: 'EventList' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('EventList') }">Events</router-link>

      <router-link :to="{ name: 'GraduationProjectList' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('GraduationProjectList') }">Graduation Project</router-link>

<a href="http://localhost:8000/index.html"
   @click="closeMobileMenu"
   class="external-link">Map</a>

    </div>

    <!-- Search bar and Profile button on the right -->
    <div class="actions">
      <div class="search-container">
        <input type="text" v-model="searchQuery" placeholder="Search..." />
        <i class="fas fa-search search-icon"></i>
      </div>

      <div class="profile-dropdown" ref="dropdownRef">
        <button @click="toggleDropdown" class="profile-btn">
          <i class="fas fa-user-circle" style="font-size: 40px; color: black;"></i>
        </button>

         <div v-if="dropdownOpen" class="dropdown-menu">
    <div class="user-info">
      <h4>{{ store.userinfo.first_name }} {{ store.userinfo.last_name }}</h4>
    </div>
    <hr />
    <button @click="goTo('ProfileView')"><i class="fas fa-user"></i> Profile</button>
    <button @click="goTo('Settings')"><i class="fas fa-cog"></i> Settings</button>
    <button @click="logout"><i class="fas fa-sign-out-alt"></i> Logout</button>
  </div>
      </div>
    </div>

    <!-- Mobile Menu Toggle -->
    <button class="mobile-menu-toggle" @click="toggleMobileMenu">☰</button>
  </nav>

  <!-- Mobile Nav Links (visible on smaller screens) -->
  <div v-if="mobileMenuOpen" class="mobile-nav-dropdown">
    <div class="mobile-nav-links">
      <router-link :to="{ name: 'Home' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('Home') }">Home</router-link>

      <router-link :to="{ name: 'CourseList' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('CourseList') }">Materials</router-link>

      <router-link :to="{ name: 'ClassroomList' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('ClassroomList') }">My Class</router-link>

      <router-link :to="{ name: 'TimeTable' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('TimeTable') }">Time Table</router-link>

      <router-link :to="{ name: 'EventList' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('EventList') }">Events</router-link>

      <router-link :to="{ name: 'GraduationProjectList' }"
                   @click="closeMobileMenu"
                   :class="{ 'active-link': isActive('GraduationProjectList') }">Graduation Project</router-link>

<a href="http://localhost:8000/index.html"
   @click="closeMobileMenu"
   class="external-link">Map</a>
    </div>
  </div>
</template>

<script>
  
  import { useGlobalStore } from '@/global_store.js'

  export default {
    data() {
      return {
        searchQuery: '',
        mobileMenuOpen: false,
        dropdownOpen: false,
        store: useGlobalStore()
      };
    },
    computed: {
      // Computed property to check if the current route matches
      isActive() {
        return (routeName) => {
          return this.$route.name === routeName;
        };
      }
          /* 
        isActive() {
    return (routeName) => {
      return this.$route.name === routeName;
    };
  }*/

    },
     mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside);
  },
    methods: {
      goTo(target) {
        // Close the dropdown menu and mobile menu before navigating
        this.dropdownOpen = false;
        this.closeMobileMenu();

        // Handle navigation for profile or settings
        this.$router.push({ name: target })
      },
      toggleMobileMenu() {
        this.mobileMenuOpen = !this.mobileMenuOpen;
      },
      closeMobileMenu() {
        this.mobileMenuOpen = false; // Close the mobile menu when a link is clicked
      },
      toggleDropdown() {
        this.dropdownOpen = !this.dropdownOpen;
      },
      logout() {
        this.store.logout()
        this.dropdownOpen = false; // Close the dropdown menu on logout
        this.$router.replace({ name: 'Login' });
      },
       handleClickOutside(event) {
      const dropdown = this.$refs.dropdownRef;
      if (dropdown && !dropdown.contains(event.target)) {
        this.dropdownOpen = false;
      }
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
    height: 55px;
    width: 150px;
  }

  .nav-links {
    display: flex;
    gap: 15px;
  }

  .nav-links a {
  text-decoration: none;
  font-family: 'Segoe UI', 'Inter', 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 600;
  font-weight: 500;
  padding: 10px 16px;
  border-radius: 8px;
  color: #333;
  transition: all 0.3s ease;
  position: relative;
}

  .nav-links a:hover {
  color: #1a3dd1; /* Deep refined blue */
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.15); /* Softer, less intrusive */
  background-color: #f0f4ff; /* Light blue background hint */
  border-radius: 6px;
  transition: color 0.25s ease-in-out, background-color 0.25s ease-in-out, text-shadow 0.25s ease-in-out;
}

.nav-links a::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: 6px;
  width: 0%;
  height: 2px;
  background-color: orange;
  transition: width 0.3s ease, left 0.3s ease;
  transform: translateX(-50%);
}

 .nav-links a:hover::after {
  width: 80%;
}

/* Active Link Styling */
.active-link {
  background-color: orange;
  color: white !important;
  font-weight: 700;
  border-radius: 8px;
  box-shadow: 0 3px 6px rgba(255, 165, 0, 0.3);
}
.active-link:hover {
  background-color: #f0f4ff; /* Same as normal hover */
  color: #1a3dd1 !important; /* Same refined blue text */
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
  border-radius: 6px;
  box-shadow: none; /* Remove orange glow to match normal hover */
}

.mobile-nav-links .active-link:hover {
  background-color: #ffe0b3; /* Same as mobile hover */
  color: #3b3b98;
  box-shadow: none;
}

.mobile-nav-links .active-link {
  background-color: orange;
  color: white !important;
  font-weight: 700;
  border-radius: 6px;
  box-shadow: 0 2px 5px rgba(255, 165, 0, 0.25);
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

 .profile-dropdown {
  position: relative;
  display: inline-block;
}
.profile-btn {
  background: none;
  border: none;
  cursor: pointer;
}
.profile-btn:hover {
  background: none; /* keep transparent */
}

.profile-btn:hover i {
  color: darkorange !important; /* refined blue */
  transform: scale(1.08);
  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.1));
}

.profile-btn i {
  font-size: 40px;
  color: #333;
  transition: color 0.3s;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: #fff2e3;
  border: 1px solid #ddd;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  z-index: 100;
  padding: 20px;
  min-width: 220px;
  display: flex;
  flex-direction: column;
  font-size: 16px;
}

.user-info h4 {
  margin: 0 0 10px 0;
  font-size: 18px;
  font-weight: 600;
  color: #222;
}

.dropdown-menu button {
  background: none;
  border: none;
  padding: 10px 8px;
  margin: 4px 0;
  text-align: left;
  cursor: pointer;
  font-size: 15px;
  display: flex;
  align-items: center;
  color: #333;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.dropdown-menu button i {
  margin-right: 8px;
  font-size: 16px;
}

.dropdown-menu button:hover {
  background-color:darkorange;
  color: black;
}

  /* Mobile Navbar Styles */
  .mobile-menu-toggle {
    display: none;
    font-size: 24px;
    background: none;
    border: none;
    cursor: pointer;
  }
  .mobile-nav-links a {
  color: #333;
  font-size: 16px;
  padding: 10px 12px;
  border-radius: 6px;
  text-decoration: none;
  transition: background-color 0.3s, color 0.3s;
}

.mobile-nav-links a:hover {
  background-color: #ffe0b3;
  color: #3b3b98;
}

.mobile-nav-links .active-link {
  background-color: orange;
  color: white;
  font-weight: bold;
  border-radius: 6px;
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
