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
          <p class="course-description">Best courses in CSIT program</p>
        </div>
        <div class="course">
          <h4>CSC 410 Software Quality</h4>
          <p>Dr/ Mohamed</p>
          <p class="course-description">Best courses in CSIT program</p>
        </div>
        <!-- Updated to use router-link -->
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
        <router-link to="/events">
          <button class="view-events-btn">View Events</button>
        </router-link>
      </div>

      <!-- Tabs -->
      <!-- Tabs -->
      <div class="tabs">
        <router-link to="/profile" class="tab" active-class="active">
          <i class="fas fa-user"></i> About
        </router-link>
        <router-link to="/timeline" class="tab" active-class="active">
          <i class="fas fa-clock"></i> Timeline
        </router-link>
        <router-link to="/settings" class="tab" active-class="active">
          <i class="fas fa-cog"></i> Settings
        </router-link>
      </div>


      <!-- Information Sections -->
      <div class="info-section">
        <h3>University Information</h3>
        <p><strong>Student ID:</strong> 320210001</p>
        <p><strong>Full Name (AR):</strong> مؤمن علي</p>
        <p><strong>Full Name (EN):</strong> mo'men Ali </p>
        <p><strong>Nationality:</strong> Egyptian</p>
        <p><strong>National ID:</strong> 30305048754585</p>
        <p><strong>E-mail:</strong> mo'men Ali@ejust.edu.eg</p>
      </div>

      <div class="info-section">
        <h3>Contact Information</h3>
        <p><strong>Phone:</strong> +12154878511</p>
        <p><strong>Address:</strong> Alexandria</p>
        <p><strong>E-mail:</strong>mo'men Ali@ejust.edu.eg</p>
      </div>

      <div class="info-section">
        <h3>Basic Information</h3>
        <p><strong>Birth Date:</strong> 01/05/2003</p>
        <p><strong>Gender:</strong> Male</p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ProfilePage",
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

  .info-section {
    margin-bottom: 20px;
  }

    .info-section h3 {
      margin-bottom: 10px;
      font-size: 20px;
    }

    .info-section p {
      margin: 5px 0;
    }
</style>
