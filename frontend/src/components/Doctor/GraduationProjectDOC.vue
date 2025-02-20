<template>
  <div class="projects-page">
    <div class="filter-section">
      <h2 class="filter-title">Filter</h2>

      <!-- Faculty Filter -->
      <div class="filter-item">
        <select v-model="filters.faculty" @change="updateFilter">
          <option value="">Faculty</option>
          <option value="Pharma D">Pharma D</option>
          <option value="Engineering">Engineering</option>
          <option value="Computer Science">Computer Science</option>
          <option value="Sustainable Architecture">Sustainable Architecture</option>
          <option value="Basic and Applied Science">Basic and Applied Science</option>
          <option value="Art and Design">Art and Design</option>
          <option value="International Business">International Business</option>
        </select>
      </div>

      <!-- Year Filter -->
      <div class="filter-item">
        <select v-model="filters.year" @change="updateFilter">
          <option value="">Year</option>
          <option value="2022">2022</option>
          <option value="2023">2023</option>
          <option value="2024">2024</option>
          <option value="2025">2025</option>
        </select>
      </div>
      <!-- Add Your Project Button -->
      <button @click="openPopup" class="add-project-btn">
        Upload new Project
      </button>
      <!-- Popup Modal -->
      <div v-if="showPopup" class="popup-overlay">
        <div class="popup-content">
          <button @click="closePopup" class="close-btn">×</button>
          <h2>Upload New Project</h2>
          <input type="text" placeholder="Enter the title of project" class="input-field" />

          <div class="upload-container" @click="triggerFileUpload">
            <!-- Hidden file input -->
            <input type="file"
                   ref="fileInput"
                   @change="handleFileUpload"
                   style="display: none" />

            <!-- Display Selected File Name or Placeholder -->
            <span class="file-name">
              {{ selectedFile ? selectedFile.name : "Upload File" }}
            </span>

            <!-- Upload Button -->
            <button class="upload-btn">
              Upload
            </button>
          </div>
          <button class="submit-btn" @click="uploadProject">Upload new Project</button>
        </div>
      </div>
    </div>
    <!-- "Our Best Projects" section when no filters are applied -->
    <div v-if="!filters.faculty && !filters.year" class="best-projects">
      <h2 class="projects-title">Our Best Projects</h2>

      <div class="project-list">
        <div v-for="project in popularProjects" :key="project.id" @click="goToProject(project.id)" class="project-item">
          <div class="project-image">
            <img :src="project.imageUrl" alt="Project Image" />
            <div class="overlay">
              <div class="overlay-text">
                <p class="project-title-overlay">{{ project.title }}</p>
              </div>
            </div>
          </div>
          <div class="project-details">
            <div class="project-instructor">
              <div class="instructor-avatar-container">
                <img class="instructor-icon" :src="project.instructorIconUrl" alt="Instructor Icon" />
              </div>
              <span class="instructor-name">{{ project.instructor }}</span>
            </div>
            <div class="project-title">{{ project.title }}</div>
            <p class="project-major">Majors: {{ project.major }}</p>
          </div>
          <!-- Stars Above, Remove Button Below -->
          <div class="project-card">
            <div class="project-rating">
              <span v-for="n in 5" :key="n" class="star">★</span>
            </div>
            <button class="remove-btn" @click.stop="removeProject(project.id)">Remove</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Only Show Filtered Projects After Faculty is Selected -->
    <div v-if="filters.faculty && filteredProjects.length > 0" class="filtered-projects">
      <h2 class="projects-title">Filtered Graduation Projects</h2>

      <div class="project-list">
        <div v-for="project in filteredProjects" :key="project.id" @click="goToProject(project.id)" class="project-item">
          <div class="project-image">
            <img :src="project.imageUrl" alt="Project Image" />
            <div class="overlay">
              <div class="overlay-text">
                <p class="project-title-overlay">{{ project.title }}</p>
              </div>
            </div>
          </div>
          <div class="project-details">
            <div class="project-instructor">
              <div class="instructor-avatar-container">
                <img class="instructor-icon" :src="project.instructorIconUrl" alt="Instructor Icon" />
              </div>
              <span class="instructor-name">{{ project.instructor }}</span>
            </div>
            <div class="project-title">{{ project.title }}</div>
            <p class="project-major">Majors: {{ project.major }}</p>
          </div>
          <div class="project-card">
            <div class="project-rating">
              <span v-for="n in 5" :key="n" class="star">★</span>
            </div>
            <button class="remove-btn" @click.stop="removeProject(project.id)">Remove</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Show the message only if faculty is selected and no projects match the filter -->
    <div v-else-if="filters.faculty && filteredProjects.length === 0" class="no-projects-message">
      <p>No projects found for the selected filters. Please adjust your filters.</p>
    </div>
  </div>
</template>

<script>
  import projectImage from '@/assets/project-image.png';
  import instructorIcon1 from '@/assets/doctor-img4.png';
  import instructorIcon2 from '@/assets/doctor-img4.png';
  import instructorIcon3 from '@/assets/doctor-img4.png';

  export default {
    name: 'ProjectsPage',
    data() {
      return {
        popularProjects: [
          { id: 1, title: 'Smart Irrigation System', instructor: 'Dr. Mohamed', instructorIconUrl: instructorIcon1, imageUrl: projectImage, major: 'Computer Science', faculty: 'Computer Science', year: '2024' },
          { id: 2, title: 'Energy Efficient Homes', instructor: 'Dr. Ahmed', instructorIconUrl: instructorIcon2, imageUrl: projectImage, major: 'Sustainable Architecture', faculty: 'Engineering', year: '2023' },
          { id: 3, title: 'AI in Healthcare', instructor: 'Dr. Ayman', instructorIconUrl: instructorIcon3, imageUrl: projectImage, major: 'Artificial Intelligence', faculty: 'Engineering', year: '2024' },
        ],
        projects: [
          { id: 1, title: 'Smart Irrigation System', instructor: 'Dr. Mohamed', instructorIconUrl: instructorIcon1, imageUrl: projectImage, major: 'Computer Science', faculty: 'Computer Science', year: '2024' },
          { id: 2, title: 'Energy Efficient Homes', instructor: 'Dr. Ahmed', instructorIconUrl: instructorIcon2, imageUrl: projectImage, major: 'Sustainable Architecture', faculty: 'Engineering', year: '2023' },
          { id: 3, title: 'AI in Healthcare', instructor: 'Dr. Ayman', instructorIconUrl: instructorIcon3, imageUrl: projectImage, major: 'Artificial Intelligence', faculty: 'Engineering', year: '2024' },
        ],
        filters: {
          faculty: '',
          year: '',
        },
        showPopup: false,
        selectedFile: null, // Store uploaded file
        uploading: false, // Show loading state
      };
    },
    computed: {
      filteredProjects() {
        if (!this.filters.faculty && !this.filters.year) return this.projects;
        if (this.filters.faculty && !this.filters.year) {
          return this.projects.filter(project => project.faculty === this.filters.faculty);
        }
        if (!this.filters.faculty && this.filters.year) {
          return this.projects.filter(project => project.year === this.filters.year);
        }
        return this.projects.filter(project => project.faculty === this.filters.faculty && project.year === this.filters.year);
      },
    },
    methods: {
      updateFilter() { },
      goToProject(projectId) {
        this.$router.push({ name: 'ProjectDetails', params: { id: projectId } });
      },
      removeProject(projectId) {
        this.projects = this.projects.filter(project => project.id !== projectId);
      },
      openPopup() {
        this.selectedFile = null; // Reset file selection
        this.uploading = false; // Reset upload state
        this.showPopup = true;
      },
      closePopup() {
        this.showPopup = false;
      },
      triggerFileUpload() {
        this.$refs.fileInput.click(); // Opens file selection dialog
      },
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
          this.selectedFile = file;
        }
      },
      uploadFile() {
        if (!this.selectedFile) {
          alert('Please select a file first.');
          return;
        }

        this.uploading = true;
        console.log('Uploading file:', this.selectedFile.name);

        // Simulating API upload process
        setTimeout(() => {
          this.uploading = false;
          alert(`File "${this.selectedFile.name}" uploaded successfully!`);
        }, 1500);
      },
    },
  };
</script>

<style scoped>
  .projects-page {
    font-family: 'Inknut Antiqua', serif;
  }

  .filter-section {
    display: flex;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ccc;
  }

  .filter-title {
    margin-right: 20px;
    font-weight: bold;
  }

  .filter-item {
    margin-right: 30px;
    display: inline-block;
    transition: all 0.3s ease;
  }

    .filter-item:hover {
      cursor: pointer; /* This is applied to the parent container */
      color: #007bff;
      text-decoration: underline;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .filter-item select {
      width: 300px;
      padding: 8px;
      padding-right: 30px;
      border: 1px solid #ccc;
      background-color: #FEC401;
      color: #000;
      font-size: 16px;
      appearance: none;
      background-image: url('data:image/svg+xml;charset=UTF-8,%3Csvg xmlns%3D"http://www.w3.org/2000/svg" viewBox%3D"0 0 24 24" width%3D"24" height%3D"24"%3E%3Cpath fill%3D"%23000000" d%3D"M12 16l4-4H8z"%3E%3C/path%3E%3C/svg%3E');
      background-repeat: no-repeat;
      background-position: right 10px center;
      background-size: 24px 24px;
      transition: all 0.3s ease;
      cursor: pointer; /* Apply cursor pointer directly on the select */
    }

      .filter-item select:hover {
        border: 1px solid #007bff;
      }

      .filter-item select:focus {
        outline: 1px solid #007bff;
      }

  .projects-title {
    margin-top: 2px;
    font-size: 24px;
    font-weight: bold;
    color: #333;
    padding: 20px 5px 5px 5px; /* Reduced bottom padding */
  }

  .project-list {
    padding: 10px; /* Reduced padding around the project list */
  }

  .project-item {
    display: flex;
    align-items: center;
    padding: 15px;
    background-color: #fff;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: inherit;
  }

    .project-item:hover {
      border: 1px solid #007bff;
      cursor: pointer; /* Add pointer cursor */
    }

  .project-image {
    position: relative; /* Needed for absolute positioning of overlay */
    overflow: hidden; /* Hide overflowing overlay content */
  }

    .project-image img {
      width: 230px; /* Increased width */
      height: auto; /* Maintain aspect ratio */
      border-radius: 8px;
      margin-right: 15px;
    }

  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 1; /* Always visible */
    /* Remove the transition if you don't want a fade-in effect */
    /* transition: opacity 0.3s ease;  */
  }

  .overlay-text {
    color: black;
    padding: 10px;
    width: 80%;
    left: 25px;
    box-sizing: border-box;
  }

  .project-title-overlay {
    font-size: 0.9rem;
    font-weight: bold;
    margin: 0;
  }

  .project-details {
    flex: 1;
    font-size: 16px;
  }

  .project-instructor {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
  }

  /* Instructor Info Styles */
  .instructor-info {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 15px;
    padding: 10px 0;
    margin-right: 90px;
  }

  /* Avatar container to handle background gradient */
  .instructor-avatar-container {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: linear-gradient(to bottom, #f08a24, #3b3b98);
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 10px;
  }

  /* Avatar image inside the container */
  .instructor-icon {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    object-fit: cover;
  }

  .project-title {
    font-size: 18px;
    font-weight: bold;
  }

  .project-major {
    font-weight: bold;
    font-size: 16px;
  }

  .instructor-name {
    font-size: 1.1em;
    font-weight: bold;
    color: #333;
  }


  .project-rating {
    margin-left: auto;
    color: #FEC401;
    font-size: 20px;
  }

  .star {
    margin-right: 3px;
  }

  .remove-btn {
    background-color: #201887;
    color: white;
    padding: 8px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 5px; /* Spacing between stars and button */
    margin-left: 5px; /* Moves the button slightly to the right */
    display: block;
    width: fit-content;
  }

    .remove-btn:hover {
      background-color: darkorange;
    }

  .add-project-btn {
    background-color: #201887;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-left: auto;
  }

    .add-project-btn:hover {
      background-color: darkorange;
    }

  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: none; /* Removes the gray background */
  }

  .popup-content {
    background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
    padding: 7px; /* ;Increased padding for more space */
    border-radius: 10px;
    width: 480px; /* Increase width */
    max-width: 60%; /* Ensure it doesn't exceed screen width */
    height: 400px; /* Increase height */
    max-height: 90%; /* Ensure it doesn't exceed screen height */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative; /* Ensure positioning works */
    top: 90px; /* Move the popup down */
  }

  .close-btn {
    position: absolute;
    top: 10px;
    right: 15px;
    font-size: 40px;
    background: none;
    border: none;
    cursor: pointer;
  }

  .input-field,
  .upload-container {
    width: 90%;
    height: 45px;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
    border: 1px solid #ccc;
    display: flex;
    align-items: center;
  }

  .input-field {
    width: 90%;
    height: 25px;
  }

  .upload-container {
    background: white;
    justify-content: space-between;
    padding: 0 10px;
    position: relative;
  }

  .upload-label {
    flex-grow: 1;
    display: flex;
    align-items: center;
    overflow: hidden;
  }

  .file-name {
    flex-grow: 1;
    margin-left: 0px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: calc(100% - 90px); /* Adjusts width dynamically */
    color: #666; /* Match the input text color (dark gray) */
    opacity: 1; /* Ensure it's fully visible */
  }

  .upload-btn {
    background: #201887;
    color: white;
    border: none;
    padding: 5px 8px;
    border-radius: 5px;
    height: 80%;
    width: 75px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    flex-shrink: 0; /* Prevents button from shrinking */
  }

    .upload-btn:hover {
      background: darkorange;
    }

  .submit-btn {
    background: #201887;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    margin-top: 50px; /* Increase margin to shift it down */
    width: 35%;
    cursor: pointer;
  }

    .submit-btn:hover {
      background: darkorange;
    }

  .popup-content h2 {
    color: white; /* Ensure h2 is white */
    margin-top: -10px; /* Moves it up */
    padding-bottom: 25px; /* Adds spacing below */
    text-align: center; /* Keep it centered */
  }


  /* Media Queries for Responsiveness */
  /* ✅ Large screens (max-width: 1200px) */
  @media (max-width: 1200px) {
    .filter-section {
      flex-direction: column;
      align-items: flex-start;
    }

    .filter-item {
      width: 100%; /* Make filter items take full width */
      margin-bottom: 10px;
    }

      .filter-item select {
        width: 100%; /* Expand dropdowns */
      }

    .popup-content {
      width: 50%; /* Adjust popup size */
    }
  }

  /* ✅ Tablets (max-width: 768px) */
  @media (max-width: 768px) {
    .projects-title {
      font-size: 20px;
    }

    .filter-title {
      font-size: 18px;
    }

    .filter-item select {
      font-size: 14px;
    }

    .project-item {
      padding: 10px;
    }

    .project-image img {
      width: 120px;
    }

    .project-title {
      font-size: 16px;
    }

    .project-instructor .instructor-name {
      font-size: 14px;
    }

    .project-rating {
      font-size: 18px;
    }

    .popup-content {
      width: 70%; /* Adjust popup width */
      height: auto; /* Let it adjust dynamically */
    }

    .remove-btn,
    .submit-btn {
      width: 50%; /* Make buttons wider for easier tapping */
    }
  }

  /* ✅ Mobile Devices (max-width: 480px) */
  @media (max-width: 480px) {
    .filter-section {
      padding: 5px;
    }

    .filter-title,
    .projects-title {
      font-size: 16px;
      text-align: center;
      margin-bottom: 10px;
    }

    .filter-item {
      width: 100%;
      margin-bottom: 10px;
    }

      .filter-item select {
        font-size: 12px;
        padding: 6px;
        width: 100%;
      }

    .project-item {
      padding: 8px;
    }

    .project-image img {
      width: 100px;
    }

    .project-title {
      font-size: 14px;
    }

    .project-rating {
      font-size: 16px;
    }

    .popup-content {
      width: 90%; /* Full width for small screens */
      height: auto; /* Adaptive height */
      padding: 15px; /* Ensure proper spacing */
    }

    .submit-btn {
      width: 60%; /* Wider button for easier tapping */
      margin-top: 20px;
    }

    .remove-btn {
      width: 60%;
    }

    .close-btn {
      top: 5px;
      right: 10px;
      font-size: 30px; /* Smaller close button */
    }
  }
</style>
