<template>
  <div class="user-profile">
    <!-- Left Section -->
    <div class="left-section">
      <!-- Profile Image Section -->
      <div class="profile-image-container">
        <img src="@/assets/profilepic.png" alt="User Image" class="profile-image" />
        <button class="edit-profile-btn" @click="showPopup = true">Edit profile</button>
      </div>
      <!-- Separator Line with Label -->
      <div class="separator">
        <span class="separator-label">Courses</span>
      </div>

      <!-- Courses Section -->
      <div class="courses-section">
        <div class="course">
          <h4>CSC 410 Software Quality</h4>
          <p class="course-description">Dr/ Mohamed</p>
          <p class="course-description">Best courses in csit program</p>
        </div>
        <div class="course">
          <h4>CSC 410 Software Quality</h4>
          <p class="course-description">Dr/ Mohamed</p>
          <p class="course-description">Best courses in csit program</p>
        </div>
        <router-link to="/my-courses">
          <button class="view-courses-btn">View my courses</button>
        </router-link>
      </div>

      <!-- Separator Line with Label -->
      <div class="separator">
        <span class="separator-label">Events</span>
      </div>

      <!-- Events Section -->
      <div class="events-section">
        <ul>
          <li>Event 1</li>
          <li>Event 2</li>
          <li>Event 3</li>
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
        <div class="button-container">
          <button class="view-events-btn">View Events</button>
          <button class="download-report-btn" @click="downloadReport">Download Report</button>
        </div>
      </div>

      <!-- Tabs -->
      <div class="tabs">
        <router-link to="/profile" class="tab" :class="{ active: $route.path === '/profile' }">
          <i class="fas fa-user"></i> About
        </router-link>
        <router-link to="/timeline" class="tab" active-class="active">
          <i class="fas fa-clock"></i> Timeline
          <span v-if="taskCount > 0" class="task-count">{{ taskCount }}</span>
        </router-link>
        <router-link to="/settings" class="tab" :class="{ active: $route.path === '/settings' }">
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

      <!-- Language Selection Section -->
      <div class="settings-section">
        <h3>Language</h3>
        <p>Choose a preferred language for the extension</p>
        <div class="language-toggle">
          <button v-for="lang in languages"
                  :key="lang.value"
                  @click="selectedLanguage = lang.value"
                  :class="{
                    'active-language': selectedLanguage === lang.value,
                    'inactive-language': selectedLanguage !== lang.value
                  }">
            {{ lang.label }}
          </button>
        </div>
      </div>
    </div>

    <!-- Popup Modal (Edit Profile) -->
    <div v-if="showPopup" class="popup-overlay">
      <div class="popup-content">
        <button class="close-btn" @click="closePopup">✖</button>

        <!-- Profile Picture Section -->
        <div class="profile-pic-container">
          <span class="profile-pic-label">Profile Picture</span>
          <img :src="profilePicture" alt="Profile Picture" class="profile-pic" />
          <label class="upload-btn">
            Upload
            <input type="file" class="hidden" @change="uploadImage">
          </label>
        </div>
        <hr class="separator">
        <h2 class="user-name">{{ profile.fullNameEn }}</h2>
        <span class="profile-name-label">Profile Name</span>
        <hr class="separator">
        <h3 class="section-title">University Information</h3>
        <div class="details-line">
          <span class="details-label">Details</span>
        </div>
        <div class="info-section">
          <p>
            <label for="studentId">Student ID:</label> <span style="color: blue;">{{ profile.studentId }}</span>
          </p>
          <p>
            <label for="fullNameAr">Full Name (AR):</label>
            <span style="color: blue;">{{ profile.fullNameAr }}</span>
          </p>
          <p>
            <label for="fullNameEn">Full Name (EN):</label>
            <span style="color: blue;">{{ profile.fullNameEn }}</span>
          </p>
          <p>
            <label for="nationality">Nationality:</label>
            <span style="color: blue;">{{ profile.nationality }}</span>
          </p>
          <p>
            <label for="nationalId">National ID:</label>
            <span style="color: blue;">{{ profile.nationalId }}</span>
          </p>
          <p>
            <label for="email">Email:</label> <span style="color: blue;">{{ profile.email }}</span>
          </p>
        </div>

        <h3 class="section-title">Contact Information</h3>
        <div class="info-section">
          <p>
            <label for="phone">Phone:</label> <input id="phone" v-model="profile.phone" class="editable-input" type="tel" />
          </p>
          <p>
            <label for="address">Address:</label> <input id="address" v-model="profile.address" class="editable-input" />
          </p>
          <p>
            <label for="contactEmail">Email:</label> <input id="contactEmail" v-model="contact.email" class="editable-input" type="email" />
          </p>
        </div>

        <h3 class="section-title">Basic Information</h3>
        <div class="info-section">
          <p>
            <label for="birthDate">Birth Date:</label>
            <span style="color: blue;">{{ profile.birthDate }}</span>
          </p>

          <p>
            <label for="gender">Gender:</label> <span>{{ profile.gender }}</span>
          </p>
        </div>
        <hr class="separator">
        <!-- events Section -->
        <div class="title-container">
          <h3 class="section-title">events</h3>
        </div>

        <div class="events-section">
          <ul>
            <li v-for="(event, index) in profile.events" :key="index">
              {{ event }}
              <button class="remove-event-btn" @click="removeEvent(index)">Remove</button>
            </li>
          </ul>
        </div>

        <!-- Save Button -->
        <button class="save-btn" @click="saveProfile">Save</button>
      </div>
    </div>
  </div>
</template>

<script>
  import profilePicture from '@/assets/profilepic.png';

  export default {
    name: "ProfilePage",
    data() {
      return {
        showInput: false,
        showPopup: false,
        profilePicture: profilePicture, // Default or uploaded image
        newEvent: '',
        taskCount: 4,
        profile: {
          studentId: "320210001",
          fullNameAr: "مؤمن علي",
          fullNameEn: "Mo'men Ali",
          nationality: "Egyptian",
          nationalId: "30305048754585",
          email: "Mo'men Ali@ejust.edu.eg",
          phone: "+121548778511",
          address: "Alexandria",
          birthDate: "2003-06-06",
          gender: "Male",
          events: ["Event1", "Event2", "Event3"]
        },
        contact: {
          email: "Mo'men Ali@gmail.com" // New contact email
        },
        theme: 'light', // Default theme
        selectedLanguage: 'Arabic',
        languages: [
          { label: 'Arabic', value: 'Arabic' },
          { label: 'English', value: 'English' }
        ]
      };
    },
    methods: {
      // Method to open the popup
      openPopup() {
        this.showPopup = true;
      },
      // Method to close the popup
      closePopup() {
        this.showPopup = false;
      },
      // Method to save profile information (could involve API calls)
      saveProfile() {
        alert("Profile saved!");
        this.closePopup();
      },
      // Method for handling image upload
      uploadImage(event) {
        const file = event.target.files[0];
        if (file) {
          this.profilePicture = URL.createObjectURL(file);
        }
      },
      removeEvent(index) {
        this.profile.events.splice(index, 1);
      },
      // Method to set the theme
      setTheme(selectedTheme) {
        this.theme = selectedTheme;
        document.body.setAttribute('data-theme', selectedTheme); // Apply theme globally
      },
      // Method to download report (keeping existing functionality)
      downloadReport() {
        const reportContent = `
          Name: Mo'men Ali
          Role: CSIT Student
          Location: Alexandria
          Email: mo'men@ejust.edu.eg
        `;
        const blob = new Blob([reportContent], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'user-report.txt';
        link.click();
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
    object-fit: cover;
    border-radius: 3px;
    border: 1px solid #ccc;
  }

  .edit-profile-btn {
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #3b3780;
    color: white;
    border: none;
    padding: 6px 20px;
    border-radius: 5px;
    font-size: 14px;
    cursor: pointer;
  }

    .edit-profile-btn:hover {
      background-color: darkorange;
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

    .view-courses-btn:hover {
      background-color: darkorange
    }

  /* Separator Line with Label */
  .separator {
    position: relative;
    margin: 20px 0;
    text-align: left; /* Shift the separator to the left */
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
    font-weight: bold;
    right: 15px; /* Ensure label aligns to the left */
  }
  /* Events Section */
  .events-section ul {
    list-style: none;
    padding: 0;
  }

    .events-section ul li {
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

  .view-events-btn, .download-report-btn {
    background-color: #3b3780;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
  }

    .view-events-btn:hover, .download-report-btn:hover {
      background-color: darkorange;
    }

  .view-events-btn {
    padding: 10px 30px;
  }

  .download-report-btn {
    margin-left: 10px; /* Adds space to the left of the second button */
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
    .tab:hover {
      color: #3b3780; /* Change color to blue on hover */
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
    margin-bottom: 40px; /* Add this line for space between the sections */
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

  /* Language Toggle Styles */
  .language-toggle {
    display: flex;
    gap: 8px;
    margin-top: 10px;
  }

    .language-toggle button {
      flex: 1;
      padding: 10px;
      font-size: 14px;
      cursor: pointer;
      border: none;
      border-radius: 4px;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

  .active-language {
    background-color: #3f3d56;
    color: white;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  }

  .inactive-language {
    background-color: #e0e0e0;
    color: #555;
  }

    .inactive-language:hover {
      background-color: #d6d6d6;
    }
  .task-count {
    position: absolute;
    top: 44%;
    right: 50%;
    background-color: darkorange;
    color: white;
    padding: 4px 6px;
    border-radius: 50%;
    font-size: 12px;
    font-weight: bold;
  }
  /* Popup Modal (Edit Profile) */
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

    .popup-overlay .section-title {
      color: #777; /* Change text color to gray */
    }


  .popup-content {
    background: white;
    padding: 30px;
    border-radius: 10px;
    max-width: 600px;
    width: 90%;
    max-height: 90vh;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    position: relative;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
  }

    .popup-content h2 {
      font-size: 24px;
      margin-bottom: 20px;
      text-align: center;
    }

  .scrollable-content {
    overflow-y: auto; /* Enable vertical scrolling */
    flex: 1; /* Allow this section to take up remaining space */
    margin-bottom: 20px; /* Space between scrollable content and save button */
  }

  .popup-overlay .close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #333;
  }

    .popup-overlay .close-btn:hover {
      color: darkorange;
    }

  .popup-overlay .upload-section {
    text-align: center;
    margin-bottom: 20px;
  }

  .popup-overlay .upload-btn {
    position: absolute;
    top: -2px; /* Move it slightly downward */
    left: 50px; /* Shift it slightly to the right */
    background-color: #3b3780;
    color: white;
    padding: 8px 25px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }

    .popup-overlay .upload-btn:hover {
      background-color: darkorange;
    }

  .popup-overlay .hidden {
    display: none;
  }

  .popup-overlay .separator {
    border-top: 1px solid #ccc; /* Style the line */
    margin: 10px 0; /* Add margin above and below */
  }

  .popup-overlay .profile-pic-container {
    text-align: center;
    position: relative;
    margin-top: 30px; /* Adjust this value as needed to shift image down */
    margin-bottom: 15px;
  }

  .popup-overlay .profile-pic {
    width: 20%; /* Adjust width as needed */
    height: 10%; /* Adjust height for a rectangular shape */
    border-radius: 10px; /* Slightly rounded corners */
    object-fit: cover;
    border-radius: 3px;
    border: 1px solid #ccc;
  }

  .popup-overlay .profile-pic-label {
    position: absolute;
    top: 5px;
    right: 10px;
    font-size: 16px;
    font-weight: bold;
    color: black;
  }

  .popup-overlay .profile-name-section {
    position: relative;
    margin-top: 60px;
  }

  .popup-overlay .profile-name-label {
    position: absolute;
    top: 40%;
    right: 50px; /* Aligns the label to the right */
    font-size: 16px;
    font-weight: bold;
    color: black;
  }

  .popup-overlay .profile-name-section h2 {
    font-size: 22px;
    font-weight: bold;
    text-align: right; /* Optional: Aligns the header text to the right */
  }

  .popup-overlay .profile-name-section p {
    font-size: 14px;
    color: #777;
    text-align: right; /* Optional: Aligns paragraph text to the right */
  }

  .popup-overlay .divider {
    border: 0;
    height: 1px;
    background: #ddd;
    margin: 20px 0;
  }

  .title-container {
    display: flex;
    justify-content: flex-end;
  }

  .popup-overlay .title-container .section-title {
    color: black;
    margin-right: 20px;
    margin-top: 0px;
    font-size: 20px;
  }

  .popup-overlay .events-section {
    display: flex;
    flex-direction: column; /* Stack the events vertically */
    align-items: center; /* Center the events horizontally */
    width: 100%; /* Ensure full width of container */
    position: relative; /* Make the parent container relative for positioning the button */
  }

    .popup-overlay .events-section ul {
      list-style-type: none;
      padding: 0;
      display: flex;
      flex-direction: column; /* Keep events in a column */
      align-items: center; /* Center the events horizontally */
      justify-content: center; /* Center the events vertically if needed */
      width: 100%; /* Ensure full width for the ul */
    }

    .popup-overlay .events-section li {
      margin-bottom: 10px; /* Space between events */
      text-align: center; /* Center the text inside each event */
    }


  .remove-event-btn {
    background-color: #3b3780;
    color: white;
    border: none;
    padding: 5px 10px;
    margin-left: 70px;
    cursor: pointer;
    border-radius: 5px;
  }

    .remove-event-btn:hover {
      background-color: darkorange;
    }
  .popup-overlay .save-btn {
    background-color: #3b3780;
    color: white;
    padding: 8px 14px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    font-size: 16px;
    margin-top: 30px; /* Push the button to the bottom */
  }

    .popup-overlay .save-btn:hover {
      background-color: darkorange;
    }

  .save-event-btn {
    background-color: #3b3780;
    color: white;
    padding: 8px 15px;
    border: none;
    cursor: pointer;
    font-size: 16px;
    margin-left: 10px; /* Space between input and button */
    transition: background-color 0.3s ease;
    position: absolute; /* Position the button relative to the parent */
    top: 0px; /* Adjust this to shift it upwards */
    right: -18px; /* Adjust this to shift it to the right */
    border: none;
    border-radius: 5px;
    z-index: 1; /* Ensure the button stays on top */
  }

    /* Change button color on hover */
    .save-event-btn:hover {
      background-color: darkorange;
    }

  .popup-overlay .details-line {
    position: relative;
    margin-top: 10px; /* Reduced margin from top */
    margin-bottom: 20px;
    text-align: right; /* Shift to the right */
  }

  .popup-overlay .details-label {
    font-size: 18px;
    font-weight: bold;
    color: black;
    position: relative;
    display: inline-block;
    padding: 0 20px;
    background-color: #fff;
    top: -50px; /* Shift the label upwards slightly */
    right: 15px
  }

  /* Target the <p> elements within the info sections */
  .info-section {
    display: flex;
    flex-direction: column;
  }

    .info-section p {
      display: flex;
      align-items: baseline;
      justify-content: flex-start; /* Align to left */
      padding-left: 0;
    }

      .info-section p strong { /* Or .info-section p label if you use <label> */
        margin-right: 40px;
        flex-shrink: 0;
        font-weight: bold;
        width: 140px; /* Fixed width for alignment */
      }

      .info-section p span { /* Target ALL spans within the <p> tags */
        color: blue; /* Blue color for values */
        flex-grow: 1; /* Allow values to expand */
      }

    .info-section h3 {
      color: #777;
      font-weight: normal;
    }

  /* Popup */
  .popup-overlay .info-section {
    display: flex;
    flex-direction: column;
  }

  .popup-overlay .info-section {
    display: flex;
    flex-direction: column;
  }

  .popup-overlay .info-section {
    display: flex;
    flex-direction: column;
  }

  .popup-overlay .info-section {
    display: flex;
    flex-direction: column;
  }

    .popup-overlay .info-section p {
      display: flex;
      align-items: baseline;
      justify-content: flex-start;
      padding-left: 130px; /* Adjust overall left padding as needed */
    }

      .popup-overlay .info-section p label,
      .popup-overlay .info-section p strong {
        color: #333;
        margin-right: 40px; /* Increased margin for more space */
        width: 160px; /* Fixed width for labels (adjust if needed) */
        flex-shrink: 0;
        font-weight: bold;
        padding-left: 20px; /* Add padding to labels as well */
        box-sizing: border-box; /* Include padding in width calculation */
      }

      .popup-overlay .info-section p span,
      .popup-overlay .info-section p .editable-input,
      .popup-overlay .info-section p select.editable-input {
        color: blue;
        flex-grow: 1;
        border: none;
        background-color: transparent;
        padding-left: 20px; /* Add padding to values */
        box-sizing: border-box; /* Include padding in width calculation */
      }

  @media (max-width: 1024px) {
    .user-profile {
      flex-direction: column;
      align-items: center;
      gap: 20px;
      padding: 10px;
    }

    .left-section, .right-section {
      width: 100%;
    }

    .profile-image {
      width: 150px;
      height: 150px;
      object-fit: cover;
    }

    .profile-image-container {
      margin-bottom: 10px;
    }

    /* Button Sizes */
    .view-courses-btn, .view-events-btn, .download-report-btn {
      width: 100%;
      padding: 12px;
      margin-top: 10px;
    }

    /* Tabs Layout */
    .tabs {
      flex-direction: column;
      align-items: center;
      gap: 10px;
    }

    .tab {
      padding: 12px 20px;
    }

    .course h4 {
      font-size: 16px;
    }

    .course-description {
      font-size: 12px;
    }
  }

  @media screen and (max-width: 768px) {
    .user-name {
      font-size: 24px;
    }
    .user-info-header {
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 16px;
    }

    .button-container {
      display: flex;
      flex-direction: column; /* Stack the buttons vertically */
      width: 100%; /* Ensure the container takes up the full width of its parent */
      gap: 10px; /* Space between the buttons */
      padding: 0; /* Remove any padding from the container to avoid shifts */
      margin: 0; /* Remove any margin from the container */
    }

    .view-events-btn, .download-report-btn {
      width: 100%; /* Both buttons take the full width of the container */
      padding: 12px; /* Consistent padding for both buttons */
      font-size: 16px; /* Consistent font size */
      box-sizing: border-box; /* Ensures padding doesn't affect the width */
      text-align: center; /* Centers the text inside each button */
      margin: 0; /* Ensures no extra margin affects alignment */
    }


    .user-info-header .user-name {
      font-size: 1.5rem; /* Increase the font size of the full name */
    }

      .user-info-header .user-role,
      .user-info-header .user-location {
        font-size: 1rem; /* Increase the font size of the department and address */
      }

    .theme-btn {
      font-size: 12px;
      padding: 8px;
    }

      .theme-btn.light, .theme-btn.dark {
        flex: 1;
        font-size: 12px;
      }

    .profile-image {
      width: 75%;
      height: 75%;
    }
    .course-description {
      font-size: 16px; /* Increase font size */
    }

    .tab {
      font-size: 14px;
      padding: 10px 15px;
    }


    .user-info-header {
      margin-bottom: 15px;
    }

    .courses-section h3 {
      font-size: 18px;
    }

    .course {
      font-size: 14px;
    }
    .task-count {
      top: 211%;
      right: 40%;
    }
    .popup-overlay .save-btn {
      padding: 8px 12px; /* Adjust button padding */
      font-size: 14px;
    }

    .popup-overlay .upload-btn {
      margin-left: -20px;
    }

    .popup-overlay .profile-pic {
      width: 30%; /* Adjust profile picture size */
    }

    .popup-overlay .info-section p {
      display: flex;
      align-items: baseline;
      justify-content: flex-start;
      padding-left: 50px; /* Adjust overall left padding as needed */
    }

    .popup-overlay .title-container .section-title {
      font-size: 18px; /* Adjust title font size */
    }

    .popup-overlay .profile-name-label {
      top: 45%;
      right: 35px; /* Aligns the label to the right */
    }
  }
</style>
