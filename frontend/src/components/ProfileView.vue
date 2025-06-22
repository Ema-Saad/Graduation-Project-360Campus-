<template>
  <div :class="{'blur': showPopup}" class="user-profile">
    <!-- Left Section -->
    <div class="left-section">
      <!-- Profile Image Section -->
      <div class="profile-image-container">
        <img src="@/assets/Momen.jpg" alt="User Image" class="profile-image" />
        <button class="edit-profile-btn" @click="openPopup">Edit profile</button>
      </div>

      <div class="separator">
        <span class="separator-label">Courses</span>
      </div>

      <!-- Courses Section -->
      <div class="courses-section">
        <div class="course">
          <h4>CSC 410 Software Quality</h4>
          <p class="course-description">Dr/ Mohamed</p>
          <p class="course-description">Best courses in CSIT program</p>
        </div>
        <div class="course">
          <h4>CSC 410 Software Quality</h4>
          <p class="course-description">Dr/ Mohamed</p>
          <p class="course-description">Best courses in CSIT program</p>
        </div>
        <!-- Updated to use router-link -->
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

        <!-- Wrap the buttons in a new container -->
        <div class="buttons-container">
          <router-link to="/events">
            <button class="view-events-btn">View Events</button>
          </router-link>
          <!-- Add Download Report Button -->
          <button class="download-report-btn" @click="downloadReport">Download Report</button>
        </div>
      </div>

      <!-- Tabs -->
      <div class="tabs">
        <router-link to="/profile" class="tab" active-class="active">
          <i class="fas fa-user"></i> About
        </router-link>
        <router-link to="/timeline" class="tab" active-class="active">
          <i class="fas fa-clock"></i> Timeline
          <span v-if="taskCount > 0" class="task-count">{{ taskCount }}</span>
        </router-link>
        <router-link to="/settings" class="tab" active-class="active">
          <i class="fas fa-cog"></i> Settings
        </router-link>
      </div>

      <!-- Information Sections -->
      <div class="info-section">
        <h3>University Information</h3>
        <p><strong>Student ID:</strong> <span>320210001</span></p>
        <p><strong>Full Name (AR):</strong> <span>مؤمن علي</span></p>
        <p><strong>Full Name (EN):</strong> <span>mo'men Ali</span></p>
        <p><strong>Nationality:</strong> <span>Egyptian</span></p>
        <p><strong>National ID:</strong> <span>30305048754585</span></p>
        <p><strong>E-mail:</strong> <span>mo'men Ali@ejust.edu.eg</span></p>
      </div>

      <div class="info-section">
        <h3>Contact Information</h3>
        <p><strong>Phone:</strong> <span>+12154878511</span></p>
        <p><strong>Address:</strong> <span>Alexandria</span></p>
        <p><strong>E-mail:</strong> <span>mo'men Ali@ejust.edu.eg</span></p>
      </div>

      <div class="info-section">
        <h3>Basic Information</h3>
        <p><strong>Birth Date:</strong> <span>06/06/2003</span></p>
        <p><strong>Gender:</strong> <span>Male</span></p>
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
<img src="@/assets/Momen1.jpg" alt="Profile Picture" class="profile-pic" />
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
        newSkill: "",
        newEvent: '',
        taskCount: 3, 
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
  .blur {
    filter: blur(0.3px);
    opacity: 0.3;
    pointer-events: none; /* Optional: Disables interaction with blurred elements */
    transition: filter 0.3s ease; /* Smooth transition for the blur */
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
      background-color: darkorange;
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
      transform: translateY(-50%);
      background: #ccc;
      z-index: 1;
    }

  .separator-label {
    position: relative;
    z-index: 2;
    background: white;
    padding: 0 10px;
    right: 150px; /* Align the label to the left */
    color: #555;
    font-size: 16px;
    font-weight: bold;
    transform: translateY(0);
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

  /* Buttons Container */
  .buttons-container {
    display: flex;
    gap: 10px;
    width: 100%;
  }

  /* View Events and Download Report Buttons */
  .view-events-btn, .download-report-btn {
    background-color: #3b3780;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
  }
    .view-events-btn:hover,
    .download-report-btn:hover {
      background-color: darkorange; /* Change to orange on hover */
    }

  .view-events-btn {
    padding: 10px 30px;
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
    color: #555; /* Default color */
    padding: 10px 15px;
    font-size: 16px;
    position: relative; /* Make the tab positioned */
    transition: color 0.3s ease; /* Smooth transition for color change */
  }

    .tab:hover {
      color: #3b3780; /* Change color to blue on hover */
    }
    .tab.active {
      font-weight: bold;
      color: #3b3780;
      border-bottom: 3px solid #3b3780;
    }

  .task-count {
    position: absolute;
    top: -10px;
    right: 1px;
    background-color: darkorange;
    color: white;
    padding: 4px 6px;
    border-radius: 50%;
    font-size: 14px;
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
    top: 33%;
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
  /* Media Queries for responsiveness */
  /* For screens smaller than 1200px */
  @media screen and (max-width: 1200px) {
    /* Adjust .separator-label to the left and add space under it */
    .separator-label {
      left: 20px; /* Move the label to the left */
      margin-bottom: 25px; /* Add more space under the label to ensure text appears well */
    }
    /* Adjust other layout components if needed */
    .user-profile {
      flex-direction: column; /* Stack the sections vertically */
      gap: 20px;
    }
    .popup-overlay .info-section p {
      display: flex;
      align-items: baseline;
      justify-content: flex-start;
      padding-left: 50px; /* Adjust overall left padding as needed */
    }

    .popup-overlay .profile-name-label {
      top: 45%;
      right: 35px; /* Aligns the label to the right */
    }

    .left-section, .right-section {
      width: 100%; /* Make sections full-width on smaller screens */
    }
  }

  /* For screens smaller than 768px */
  @media screen and (max-width: 768px) {
    .separator-label {
      left: 10px; /* Move the label further to the left for smaller screens */
      margin-bottom: 30px; /* Add more space under the label to ensure text appears well */
    }

    .profile-image {
      width: 75%;
      height: 75%;
    }

    .popup-overlay .info-section p {
      display: flex;
      align-items: baseline;
      justify-content: flex-start;
      padding-left: 50px; /* Adjust overall left padding as needed */
    }
    .user-profile {
      padding: 10px; /* Reduce padding for smaller screens */
    }

    .left-section, .right-section {
      width: 100%; /* Sections will be full-width */
    }
    .user-info-header {
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 16px;
    }
      .user-info-header .user-name {
        font-size: 1.5rem; /* Set the font size for the name */
        margin-bottom: 5px; /* Reduce the space below the name */
      }

      .user-info-header .user-role,
      .user-info-header .user-location {
        font-size: 1rem; /* Set the font size for the role and location */
        margin-bottom: 3px; /* Reduce the space below the role and location */
      }


    .view-events-btn{
        width: 100%;
    }
    .separator-label{
        left: -45%;
    }
    .buttons-container {
      flex-direction: column; /* Stack buttons vertically */
      gap: 10px;
    }

    .tabs {
      display: flex;
      flex-direction: column; /* Stack tabs vertically */
      gap: 10px;
      align-items: center; /* Center items horizontally */
      justify-content: center; /* Center items vertically */
      text-align: center; /* Ensures text inside is centered */
      margin: auto; /* Center the container itself if needed */
    }

    .popup-overlay .save-btn {
      padding: 8px 12px; /* Adjust button padding */
      font-size: 14px;
    }
    .popup-overlay .upload-btn{
        margin-left: -20px;
    } 

    .popup-overlay .profile-pic {
      width: 30%; /* Adjust profile picture size */
    }
    .task-count {
      top: -7px;
      right: 0%;
    }
    .popup-overlay .title-container .section-title {
      font-size: 18px; /* Adjust title font size */
    }
    .popup-overlay .profile-name-label {
      top: 45%;
      right: 35px; /* Aligns the label to the right */
    }
  }

  /* For screens smaller than 480px */
  @media screen and (max-width: 480px) {
    .separator-label {
      left: 5px; /* Move closer to the left edge on very small screens */
      margin-bottom: 35px; /* Add more space under the label to ensure text appears well */
    }
    .popup-overlay .info-section p {
      display: flex;
      align-items: baseline;
      justify-content: flex-start;
      padding-left: 50px; /* Adjust overall left padding as needed */
    }
    .popup-overlay .profile-name-label {
      top: 45%;
      right: 35px; /* Aligns the label to the right */
    }

    .user-profile {
      padding: 5px; /* Further reduce padding */
    }

    .left-section, .right-section {
      width: 100%; /* Full-width sections */
    }

    .buttons-container {
      flex-direction: column; /* Stack buttons vertically */
      gap: 8px;
    }

    .tabs {
      flex-direction: column; /* Stack tabs vertically */
      gap: 8px;
    }

    .popup-overlay .save-btn {
      padding: 8px 10px; /* Further reduce button padding */
      font-size: 13px;
    }

    .popup-overlay .profile-pic {
      width: 40%; /* Adjust profile picture size */
    }
    .task-count {
      top: -10px;
      right: 78%;
    }

    .popup-overlay .title-container .section-title {
      font-size: 16px; /* Adjust title font size */
    }
  }

</style>
