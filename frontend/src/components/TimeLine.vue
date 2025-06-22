<template>
  <div class="profile-container">
    <!-- Left Section -->
    <div class="profile-left">
      <!-- Profile Image Section -->
      <div class="profile-image-wrapper">
        <img src="@/assets/momen.jpg" alt="User Image" class="profile-photo" />
        <button class="profile-edit-btn" @click="showPopup = true">Edit profile</button>
      </div>

      <div class="timeline-separator">
        <span class="timeline-label">Courses</span>
      </div>

      <!-- Courses Section -->
      <div class="profile-courses">
        <div class="profile-course">
          <h4>CSC 410 Software Quality</h4>
          <p class="profile-course-description">Dr/ Mohamed</p>
          <p class="profile-course-description">Best courses in CSIT program</p>
        </div>
        <div class="profile-course">
          <h4>CSC 410 Software Quality</h4>
          <p class="profile-course-description">Dr/ Mohamed</p>
          <p class="profile-course-description">Best courses in CSIT program</p>
        </div>
        <router-link to="/my-courses">
          <button class="courses-view-btn">View my courses</button>
        </router-link>
      </div>

      <div class="timeline-separator">
        <span class="timeline-label">Events</span>
      </div>

      <!-- Events Section -->
      <div class="profile-events">
        <ul>
          <li>Event1</li>
          <li>Event2</li>
          <li>Event3</li>
        </ul>
      </div>
    </div>

    <!-- Right Section -->
    <div class="profile-right">
      <div class="user-info-header">
        <h1 class="user-fullname">Mo'men Ali</h1>
        <p class="user-department">CSIT</p>
        <p class="user-address">
          <i class="fas fa-map-marker-alt"></i> Alexandria
        </p>
        <div class="button-container">
          <router-link to="/events">
            <button class="events-view-btn">View Events</button>
          </router-link>
          <button class="download-report-btn" @click="downloadReport">Download Report</button>
        </div>
      </div>

      <div class="profile-tabs">
        <router-link to="/profile" class="profile-tab" :class="{ active: $route.path === '/profile' }">
          <i class="fas fa-user"></i> About
        </router-link>
        <router-link to="/timeline" class="profile-tab" active-class="active">
          <i class="fas fa-clock"></i> Timeline
          <span v-if="taskCalc > 0" class="task-calc">{{ taskCalc }}</span>
        </router-link>
        <router-link to="/settings" class="profile-tab" :class="{ active: $route.path === '/settings' }">
          <i class="fas fa-cog"></i> Settings
        </router-link>
      </div>

      <div class="timeline-section">
        <h3>Assignment</h3>
        <div class="view-btn-container">
          <div class="circle-number">{{ taskCount }}</div> <!-- Dynamic Orange Circle with Number -->
          <router-link to="/todo">
            <button class="timeline-view-btn">View</button>
          </router-link>
        </div>
      </div>

      <div class="section-separator"></div>

      <div class="timeline-section">
        <h3>Online Lecture</h3>
        <div class="view-btn-container">
          <div class="circle-number">{{ lectureCount }}</div> <!-- Dynamic Orange Circle with Number -->
          <router-link to="/todo">
            <button class="timeline-view-btn">View</button>
          </router-link>
        </div>
      </div>
    </div>

    <!-- Popup Modal (Edit Profile) -->
    <div v-if="showPopup" class="popup-overlay">
      <div class="popup-content">
        <button class="close-btn" @click="showPopup = false">✖</button>

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

        <!-- Events Section -->
        <div class="title-container">
          <h3 class="section-title">Events</h3>
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
        taskCount: 3, // Dynamic number for tasks
        lectureCount: 2, // Dynamic number for online lectures
        profilePicture: profilePicture, // Default or uploaded image
        newEvent: '',
        taskCalc: 3,
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
    object-fit: cover;
    border-radius: 3px;
    border: 1px solid #ccc;
  }
  .profile-edit-btn {
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

    .profile-edit-btn:hover {
      background-color: darkorange;
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

    .courses-view-btn:hover {
      background-color: darkorange;
    }

  /* Separator Line with Label */
  .timeline-separator {
    position: relative;
    margin: 20px 0;
    text-align: center;
  }

    .timeline-separator:before {
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

  .timeline-label {
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
  .profile-events ul {
    list-style: none;
    padding: 0;
  }

    .profile-events ul li {
      margin-bottom: 8px;
    }

  /* Right Section */
  .profile-right {
    width: 70%;
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

  .button-container {
    display: flex;
    gap: 10px;
    margin-top: 15px;
  }

  .events-view-btn,
  .download-report-btn {
    background-color: #3b3780;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    transition: background-color 0.3s ease; /* Smooth transition */
  }

    .events-view-btn:hover,
    .download-report-btn:hover {
      background-color: darkorange; /* Change to orange on hover */
    }
  .events-view-btn {
    padding: 10px 30px;
  }

  /* Tabs */
  .profile-tabs {
    display: flex;
    gap: 20px;
    margin: 20px 0;
    border-bottom: 1px solid #ddd;
  }
    .profile-tabs .profile-tab:hover {
      color: #3b3780;
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
  .task-calc {
    position: absolute;
    top: 42%;
    right: 50%;
    background-color: darkorange;
    color: white;
    padding: 4px 6px;
    border-radius: 50%;
    font-size: 14px;
    font-weight: bold;
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

  .section-separator {
    height: 1px;
    background-color: #ddd;
    margin: 20px 0;
  }

  .view-btn-container {
    position: relative; /* To position the circle relative to this container */
    display: flex;
    justify-content: flex-end;
    align-items: center; /* Ensure the button and circle are aligned */
  }
  .circle-number {
    position: absolute; /* Position it above the button */
    top: -7px; /* Adjust this value to fine-tune its position */
    left: 99%; /* Adjust this value to fine-tune its position */
    background-color: darkorange; /* Background color for the circle */
    color: white;
    font-size: 14px; /* Adjust size as needed */
    width: 20px; /* Set the size of the circle */
    height: 20px; /* Set the size of the circle */
    border-radius: 50%; /* Make it a circle */
    display: flex;
    justify-content: center;
    align-items: center; /* Center the number inside the circle */
    font-weight: bold; /* Make the number bold */
  }
  .timeline-view-btn {
    background-color: #3b3780;
    color: white;
    padding: 7px 20px;
    border: none;
    border-radius: 5px;
    font-size: 14px;
    cursor: pointer;
    margin-top: 10px;
    transition: background-color 0.3s;
  }

    .timeline-view-btn:hover {
      background-color: darkorange;
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
  /* For screens smaller than 1200px */
  @media screen and (max-width: 1200px) {
    /* Adjust .separator-label to the left and add space under it */
    .separator-label {
      left: 20px; /* Move the label to the left */
      margin-bottom: 25px; /* Add more space under the label to ensure text appears well */
    }

    /* Adjust layout for profile container */
    .profile-container {
      flex-direction: column; /* Stack sections vertically */
      gap: 20px;
      padding: 15px;
    }

    .profile-left, .profile-right {
      width: 100%; /* Make sections full-width */
    }

    .profile-image-wrapper {
      text-align: center;
    }

    .profile-photo {
      width: 80%; /* Adjust photo size */
      max-width: 200px;
    }

    .profile-edit-btn {
      bottom: 10px;
      left: 50%;
      transform: translateX(-50%);
      padding: 8px 12px;
      font-size: 12px;
    }

    .profile-courses h3 {
      font-size: 18px;
    }

    .profile-course h4 {
      font-size: 14px;
    }

    .profile-course-description {
      font-size: 12px;
    }

    .courses-view-btn {
      width: 100%;
      padding: 12px 20px;
    }

    .events-separator {
      margin: 15px 0;
    }

    .events-label {
      font-size: 14px;
    }

    .profile-events ul li {
      font-size: 14px;
    }

    .user-info-header {
      text-align: center;
    }

    .user-fullname {
      font-size: 22px;
    }

    .user-department {
      font-size: 14px;
    }

    .user-address {
      font-size: 12px;
    }

    .events-view-btn {
      width: 100%;
      padding: 12px 20px;
    }

    .button-container {
      flex-direction: column;
      gap: 10px;
    }

    .profile-tabs {
      flex-direction: column;
      align-items: center;
    }

    .profile-tab {
      width: 100%;
      text-align: center;
      padding: 10px;
      font-size: 14px;
    }

    .timeline-section h3 {
      font-size: 18px;
    }

    .timeline-section p {
      font-size: 14px;
    }

    .timeline-view-btn {
      width: 100%;
      padding: 12px 20px;
    }

    .timeline-section {
      margin-right: 10px;
    }

    .task-calc {
      margin-top: 190%;
      margin-left: auto; /* Push it to the right */
      margin-right: -14%;
    }

    .section-separator {
      margin: 15px 0;
    }
  }

  /* For screens smaller than 768px */
  @media screen and (max-width: 768px) {
    .profile-photo {
      max-width: 95%;
      height: 90%;
    }
    .profile-tab {
      text-decoration: none;
      color: #555;
      padding: 10px 15px;
      font-size: 16px;
      display: inline-block; /* Ensures the width of the tab matches the content */
    }

      .profile-tab.active {
        font-weight: bold;
        color: #3b3780;
        border-bottom: 3px solid #3b3780;
        padding-bottom: 5px; /* Optional: Adjust the spacing between the text and border */
        width: auto; /* Makes sure the border length is constrained to the tab width */
      }
    .profile-right {
      margin-left: 0; /* Removes any left margin */
      margin-left: 0;
      padding-left: 0; /* Removes any left padding */
    }

    .profile-container {
      display: flex;
      gap: 30px;
      max-width: 1700px;
      margin: auto;
      padding: 20px;
      font-family: Arial, sans-serif;
      color: #333;
    }
    .profile-edit-btn {
     margin-bottom: -15px;
    }
    .timeline-label {
        right: 45%;
    }

     .courses-view-btn {
      padding: 8px 15px;
    }
    .user-info-header .user-fullname {
      font-size: 1.5rem; /* Increase the font size of the full name */
    }

    .user-info-header .user-department,
    .user-info-header .user-address {
      font-size: 1rem; /* Increase the font size of the department and address */
    }

    .events-view-btn {
      padding: 8px 15px;
    }
    .profile-events ul li {
      font-size: 16px; /* Increase font size */
    }

    .timeline-view-btn {
      padding: 8px 15px;
    }

    .timeline-section{
      margin-right: 10px;
    }
    .task-calc {
      margin-top: 200%;
      margin-left: auto; /* Push it to the right */
      margin-right: -10%;
    }
    .profile-course-description{
        font-size: 16px;
    }

    .profile-course h4{
        font-size: 16px;
    }

    .popup-overlay .info-section p {
      display: flex;
      align-items: baseline;
      justify-content: flex-start;
      padding-left: 50px; /* Adjust overall left padding as needed */
    }

    .popup-overlay .profile-name-label {
      top: 35%;
      right: 40px; /* Aligns the label to the right */
    }

  }

  /* For screens smaller than 480px */
  @media screen and (max-width: 480px) {
    .separator-label {
      left: 5px; /* Move closer to the left edge */
      margin-bottom: 35px; /* Add more space under the label */
    }

    .popup-overlay .info-section p {
      display: flex;
      align-items: baseline;
      justify-content: flex-start;
      padding-left: 50px; /* Adjust overall left padding as needed */
    }

    .timeline-section {
      margin-right: 10px;
    }

    .task-calc {
      margin-top: 190%;
      margin-left: auto; /* Push it to the right */
      margin-right: -14%;
    }

    .user-profile {
      padding: 5px; /* Reduce padding */
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
      padding: 8px 10px; /* Reduce button padding */
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
