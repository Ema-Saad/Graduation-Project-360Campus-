<template>
  <div class="user-profile">
    <!-- Left Section -->
    <div class="left-section">
      <!-- Profile Image Section -->
      <div class="profile-image-container">
        <img src="@/assets/profile.png" alt="User Image" class="profile-image" />
        <button class="edit-profile-btn">Edit profile</button>
      </div>

      <!-- Courses Section -->
      <div class="courses-section">
        <h3>Courses</h3>
        <div class="course">
          <h4>CSC 410 Software Quality</h4>
          <p>Dr/ Mohamed</p>
          <p class="course-description">Best courses in csit program</p>
        </div>
        <div class="course">
          <h4>CSC 410 Software Quality</h4>
          <p>Dr/ Mohamed</p>
          <p class="course-description">Best courses in csit program</p>
        </div>
        <!-- Updated button to use router-link for navigation -->
        <router-link to="/my-courses">
          <button class="view-courses-btn">View my courses</button>
        </router-link>
      </div>

      <!-- Separator Line with Label -->
      <div class="separator">
        <span class="separator-label">Skills</span>
      </div>

      <!-- Skills Section -->
      <div class="skills-section">
        <ul>
          <li>UI/UX</li>
          <li>Web - Design</li>
          <li>Coding</li>
          <li>Project Management</li>
        </ul>
      </div>
    </div>

    <!-- Right Section -->
    <div class="right-section">
      <!-- User Information -->
      <div class="user-info-header">
        <h1 class="user-name">Mo'men Ali</h1>
        <p class="user-role">CSIT</p>
        <p class="user-location">
          <i class="fas fa-map-marker-alt"></i> Alexandria
        </p>
        <button class="view-events-btn">View Events</button>
      </div>

      <!-- Tabs -->
      <div class="tabs">
        <router-link to="/about" class="tab" active-class="active">
          <i class="fas fa-user"></i> About
        </router-link>
        <router-link to="/timeline" class="tab" active-class="active">
          <i class="fas fa-clock"></i> Timeline
        </router-link>
        <router-link to="/settings" class="tab" active-class="active">
          <i class="fas fa-cog"></i> Settings
        </router-link>
      </div>

      <!-- Dark Mode Settings Section -->
      <div class="settings-section">
        <h3>Theme</h3>
        <p>Choose a preferred theme for the extension</p>
        <div class="theme-toggle">
          <button class="theme-btn light"
                  :class="{ active: theme === 'light' }"
                  @click="setTheme('light')">
            🌞 LIGHT
          </button>
          <button class="theme-btn dark"
                  :class="{ active: theme === 'dark' }"
                  @click="setTheme('dark')">
            🌙 Dark
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        theme: 'light', // Default theme
      };
    },
    methods: {
      setTheme(selectedTheme) {
        this.theme = selectedTheme;
        document.body.setAttribute('data-theme', selectedTheme); // Apply theme globally
      },
    },
  };
</script>

<style scoped>
  /* General Layout */
  .user-profile {
    display: flex;
    gap: 30px;
    max-width: 1200px;
    margin: auto;
    padding: 20px;
    font-family: Arial, sans-serif;
    color: #333;
  }

  /* Left Section */
  .left-section {
    width: 30%;
  }

  .profile-image-container {
    position: relative;
    text-align: center;
    margin-bottom: 20px;
  }

  .profile-image {
    width: 100%;
    border-radius: 10px;
    object-fit: cover;
  }

  .edit-profile-btn {
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #3b3780;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    font-size: 14px;
    cursor: pointer;
  }

  .courses-section {
    margin-bottom: 30px;
  }

    .courses-section h3 {
      margin-bottom: 10px;
    }

  .course {
    margin-bottom: 15px;
  }

    .course h4 {
      font-weight: bold;
      margin: 5px 0;
    }

  .course-description {
    color: #777;
  }

  .view-courses-btn {
    background-color: #3b3780;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  /* Separator Line with Label */
  .separator {
    position: relative;
    margin: 20px 0;
    text-align: center;
  }

    .separator:before {
      content: "";
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 1px;
      background: #ccc;
      z-index: 1;
    }

  .separator-label {
    position: relative;
    background: white;
    padding: 0 10px;
    font-size: 16px;
    color: #555;
    z-index: 2;
  }

  /* Skills Section */
  .skills-section ul {
    list-style: none;
    padding: 0;
  }

    .skills-section ul li {
      margin-bottom: 8px;
    }

  /* Right Section */
  .right-section {
    width: 70%;
  }

  .user-info-header {
    text-align: left;
    margin-bottom: 20px;
  }

  .user-name {
    font-size: 28px;
    font-weight: bold;
  }

  .user-role {
    font-size: 16px;
    color: #555;
  }

  .user-location {
    font-size: 14px;
    color: #777;
  }

  .view-events-btn {
    background-color: #3b3780;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    margin-top: 15px;
    cursor: pointer;
  }

  /* Tabs */
  .tabs {
    display: flex;
    gap: 20px;
    margin: 20px 0;
    border-bottom: 1px solid #ddd;
  }

  .tab {
    text-decoration: none;
    color: #555;
    padding: 10px 15px;
    font-size: 16px;
  }

    .tab.active {
      font-weight: bold;
      color: #3b3780;
      border-bottom: 3px solid #3b3780;
    }

  /* Dark Mode Settings */
  .settings-section {
    background-color: #f7f7f7;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    font-family: 'Arial', sans-serif;
    max-width: 500px;
    margin: auto;
  }

    .settings-section h3 {
      font-size: 18px;
      margin-bottom: 10px;
      color: #333;
    }

    .settings-section p {
      font-size: 14px;
      margin-bottom: 20px;
      color: #555;
    }

  .theme-toggle {
    display: flex;
    gap: 10px;
    justify-content: space-between;
  }

  .theme-btn {
    flex: 1;
    padding: 10px;
    font-size: 14px;
    cursor: pointer;
    border: none;
    border-radius: 4px;
    transition: background-color 0.3s ease, color 0.3s ease;
  }

    .theme-btn.light {
      background-color: #fff;
      color: #333;
      border: 1px solid #ddd;
    }

      .theme-btn.light:hover {
        background-color: #e0e0e0;
      }

    .theme-btn.dark {
      background-color: #333;
      color: #fff;
      border: 1px solid #333;
    }

      .theme-btn.dark:hover {
        background-color: #555;
      }

    .theme-btn.active {
      border: 2px solid #007bff;
    }
</style>
