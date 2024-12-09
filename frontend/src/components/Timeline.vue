<template>
  <div class="profile-container">
    <!-- Left Section -->
    <div class="profile-left">
      <!-- Profile Image Section -->
      <div class="profile-image-wrapper">
        <img src="@/assets/profile.png" alt="User Image" class="profile-photo" />
        <button class="profile-edit-btn">Edit profile</button>
      </div>

      <!-- Courses Section -->
      <div class="profile-courses">
        <h3>Courses</h3>
        <div class="profile-course">
          <h4>CSC 410 Software Quality</h4>
          <p>Dr/ Mohamed</p>
          <p class="profile-course-description">Best courses in CSIT program</p>
        </div>
        <div class="profile-course">
          <h4>CSC 410 Software Quality</h4>
          <p>Dr/ Mohamed</p>
          <p class="profile-course-description">Best courses in CSIT program</p>
        </div>
        <!-- Updated to use router-link for navigation -->
        <router-link to="/my-courses">
          <button class="courses-view-btn">View my courses</button>
        </router-link>
      </div>

      <!-- Separator Line with Label -->
      <div class="skills-separator">
        <span class="skills-label">Skills</span>
      </div>

      <!-- Skills Section -->
      <div class="profile-skills">
        <ul>
          <li>UI/UX</li>
          <li>Web - Design</li>
          <li>Coding</li>
          <li>Project Management</li>
        </ul>
      </div>
    </div>

    <!-- Right Section -->
    <div class="profile-right">
      <!-- User Information Header -->
      <div class="user-info-header">
        <h1 class="user-fullname">Mo'men Ali</h1>
        <p class="user-department">CSIT</p>
        <p class="user-address">
          <i class="fas fa-map-marker-alt"></i> Alexandria
        </p>
        <router-link to="/events">
          <button class="events-view-btn">View Events</button>
        </router-link>
      </div>

      <!-- Tabs -->
      <div class="profile-tabs">
        <router-link to="/profile" class="profile-tab" :class="{ active: $route.path === '/profile' }">
          <i class="fas fa-user"></i> About
        </router-link>
        <router-link to="/timeline" class="profile-tab" :class="{ active: $route.path === '/timeline' }">
          <i class="fas fa-clock"></i> Timeline
        </router-link>
        <router-link to="/settings" class="profile-tab" :class="{ active: $route.path === '/settings' }">
          <i class="fas fa-cog"></i> Settings
        </router-link>
      </div>

      <!-- Timeline Sections -->
      <div class="timeline-section">
        <h3>Assignment (To-Do)</h3>
        <p v-if="showAssignments"><strong>Task 1:</strong> Complete project documentation</p>
        <p v-if="showAssignments"><strong>Task 2:</strong> Review code for milestone 2</p>
        <div class="view-btn-container">
          <button class="timeline-view-btn" @click="toggleAssignments">View</button>
        </div>
      </div>

      <!-- Separator Between Sections -->
      <div class="section-separator"></div>

      <div class="timeline-section">
        <h3>Online Lecture</h3>
        <p v-if="showLectures"><strong>Topic:</strong> Advanced Software Testing</p>
        <p v-if="showLectures"><strong>Date:</strong> 27/11/2024</p>
        <div class="view-btn-container">
          <button class="timeline-view-btn" @click="toggleLectures">View</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ProfilePage",
    data() {
      return {
        showAssignments: false, // Track visibility of assignments
        showLectures: false,    // Track visibility of lectures
      };
    },
    methods: {
      toggleAssignments() {
        this.showAssignments = !this.showAssignments; // Toggle visibility of assignments
      },
      toggleLectures() {
        this.showLectures = !this.showLectures; // Toggle visibility of lectures
      },
    },
  };
</script>

<style scoped>
  /* General Layout */
  .profile-container {
    display: flex;
    gap: 30px;
    max-width: 1200px;
    margin: auto;
    padding: 20px;
    font-family: Arial, sans-serif;
    color: #333;
  }

  /* Left Section */
  .profile-left {
    width: 30%;
  }

  .profile-image-wrapper {
    position: relative;
    text-align: center;
    margin-bottom: 20px;
  }

  .profile-photo {
    width: 100%;
    border-radius: 10px;
    object-fit: cover;
  }

  .profile-edit-btn {
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

  .profile-courses {
    margin-bottom: 30px;
  }

    .profile-courses h3 {
      margin-bottom: 10px;
    }

  .profile-course {
    margin-bottom: 15px;
  }

    .profile-course h4 {
      font-weight: bold;
      margin: 5px 0;
    }

  .profile-course-description {
    color: #777;
  }

  .courses-view-btn {
    background-color: #3b3780;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  /* Separator Line with Label */
  .skills-separator {
    position: relative;
    margin: 20px 0;
    text-align: center;
  }

    .skills-separator:before {
      content: "";
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 1px;
      background: #ccc;
      z-index: 1;
    }

  .skills-label {
    position: relative;
    background: white;
    padding: 0 10px;
    font-size: 16px;
    color: #555;
    z-index: 2;
  }

  /* Skills Section */
  .profile-skills ul {
    list-style: none;
    padding: 0;
  }

    .profile-skills ul li {
      margin-bottom: 8px;
    }

  /* Right Section */
  .profile-right {
    width: 70%;
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 10px;
  }

  .user-info-header {
    text-align: left;
    margin-bottom: 20px;
  }

  .user-fullname {
    font-size: 28px;
    font-weight: bold;
    color: #333;
  }

  .user-department {
    font-size: 16px;
    color: #555;
  }

  .user-address {
    font-size: 14px;
    color: #777;
  }

  .events-view-btn {
    background-color: #3b3780;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    margin-top: 15px;
    cursor: pointer;
  }

  /* Tabs */
  .profile-tabs {
    display: flex;
    gap: 20px;
    margin: 20px 0;
    border-bottom: 1px solid #ddd;
  }

  .profile-tab {
    text-decoration: none;
    color: #555;
    padding: 10px 15px;
    font-size: 16px;
  }

    .profile-tab.active {
      font-weight: bold;
      color: #3b3780;
      border-bottom: 3px solid #3b3780;
    }

  .timeline-section {
    margin-bottom: 20px;
  }

    .timeline-section h3 {
      margin-bottom: 10px;
      font-size: 20px;
    }

    .timeline-section p {
      margin: 5px 0;
    }

  /* Normal Separator Between Sections */
  .section-separator {
    height: 1px;
    background-color: #ddd;
    margin: 20px 0;
  }

  /* View Button Alignment */
  .view-btn-container {
    display: flex;
    justify-content: flex-end;
  }

  .timeline-view-btn {
    background-color: #3b3780;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    font-size: 14px;
    cursor: pointer;
    margin-top: 10px;
    transition: background-color 0.3s;
  }

    .timeline-view-btn:hover {
      background-color: #2a265a;
    }
</style>
