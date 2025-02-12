<template>
  <div class="timetable-container">
    <!-- Filters Section -->
    <div class="filter-section">
      <h2 class="filter-title">Filter</h2>
      <div class="filter-item">
        <select v-model="selectedFaculty" aria-label="Select Faculty">
          <option value="">Faculty</option>
          <option value="Computer Science">Computer Science</option>
          <option value="Pharma D">Pharma D</option>
          <option value="Faculty of engineering">Faculty of engineering</option>
          <option value="Sustainable Architecture">Sustainable Architecture</option>
          <option value="Basic and Applied Science">Basic and Applied Science</option>
          <option value="Art and Design">Art and Design</option>
          <option value="International Business">International Business</option>
        </select>
      </div>

      <div class="filter-item">
        <select v-model="selectedLevel" aria-label="Select Level">
          <option value="">Level</option>
          <option value="First Level">First Level</option>
          <option value="Second Level">Second Level</option>
          <option value="Third Level">Third Level</option>
          <option value="Fourth Level">Fourth Level</option>
          <option value="Fifth Level">Fifth Level</option>
          <option value="Sixth Level">Sixth Level</option>
        </select>
      </div>

      <div class="filter-item">
        <select v-model="selectedSemester" aria-label="Select Semester">
          <option value="">Semester</option>
          <option value="Fall">Fall</option>
          <option value="Spring">Spring</option>
        </select>
      </div>
    </div>

    <!-- Display Dynamic Title based on Filters -->
    <h3 class="timetable-title">
      {{
        selectedFaculty && selectedLevel && selectedSemester
          ? `${selectedFaculty} - ${selectedLevel} - ${selectedSemester}`
          : 'Your Time Table'
      }}
    </h3>

    <!-- Display Image Instead of PDF -->
    <div class="image-container">
      <!-- If no filters selected, show the default timetable image -->
      <img v-if="!selectedFaculty && !selectedLevel && !selectedSemester" src="@/assets/default_timetable.png" alt="Your Time Table" />

      <!-- If filters are selected, show loading or image accordingly -->
      <div v-if="isLoading && timetableExists === null" class="loading-indicator">Loading...</div>
      <img v-if="imagePath && timetableExists" :src="imagePath" alt="Time Table" />
    </div>

    <!-- Always visible Download Button -->
    <button @click="downloadImage" class="download-btn" :aria-label="downloadButtonLabel">
      Download Time Table
    </button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        selectedFaculty: "",
        selectedLevel: "",
        selectedSemester: "",
        imagePath: "",
        isLoading: false, // To manage loading state
        timetableExists: null, // Tracks if the timetable exists or not
        downloadButtonLabel: "Download selected timetable image",
      };
    },
    watch: {
      // Watch for changes in the selected filters
      selectedFaculty() {
        this.updateImagePath();
      },
      selectedLevel() {
        this.updateImagePath();
      },
      selectedSemester() {
        this.updateImagePath();
      },
    },
    methods: {
      async updateImagePath() {
        // Only proceed if all selections are made (Faculty, Level, and Semester)
        if (this.selectedFaculty && this.selectedLevel && this.selectedSemester) {
          this.isLoading = true;
          this.timetableExists = null; // Reset the timetable existence state

          // Format the filter values by replacing spaces with underscores
          const formattedFaculty = this.selectedFaculty.replace(/\s+/g, '_');
          const formattedLevel = this.selectedLevel.replace(/\s+/g, '_');
          const formattedSemester = this.selectedSemester.replace(/\s+/g, '_');

          // Construct image filename
          const imageName = `${formattedFaculty}_${formattedLevel}_${formattedSemester}.jpg`;

          // Dynamically import images based on the pattern
          const images = import.meta.glob('@/assets/*.jpg');  // Adjust this to your actual assets folder location

          // Check if the image exists
          const imageImport = images[`/src/assets/${imageName}`];

          if (imageImport) {
            // Import the image dynamically and set the path
            imageImport().then((imageModule) => {
              this.imagePath = imageModule.default;
              this.timetableExists = true; // Set to true if the image exists
            });
          } else {
            this.timetableExists = false; // Set to false if the image doesn't exist
            this.imagePath = ""; // Clear image path
          }

          this.isLoading = false;
        } else {
          // No filters selected, show the default timetable
          this.imagePath = "";
          this.timetableExists = null; // Reset existence state
        }
      },

      downloadImage() {
        if (this.imagePath) {
          // Create an anchor element to simulate a download
          const link = document.createElement('a');
          link.href = this.imagePath; // Set the image path as the link's href
          link.download = `${this.selectedFaculty}_${this.selectedLevel}_${this.selectedSemester}_TimeTable.jpg`; // Set the download filename
          link.click(); // Trigger the download by simulating a click event
        } else {
          alert('No timetable image available for download');
        }
      },
    },
  };
</script>

<style scoped>
  .timetable-container {
    max-width: 1200px;
    margin: auto;
    text-align: center;
    padding-bottom: 50px;
  }

  .filter-section {
    display: flex;
    align-items: center;
    padding: 15px 10px;
    border-bottom: 1px solid #ccc;
    justify-content: center;
    flex-wrap: wrap;
  }

  .filter-title {
    margin-right: 20px;
    font-weight: bold;
    font-size: 1.2em;
    color: #333;
  }

  .filter-item {
    margin-right: 30px;
    margin-bottom: 10px;
    display: inline-block;
    transition: all 0.3s ease;
  }

    .filter-item:hover {
      cursor: pointer; /* Applied to the parent container */
      color: #007bff;
      text-decoration: underline;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .filter-item select {
      width: 280px;
      padding: 10px;
      padding-right: 40px; /* Increased space for the larger arrow */
      border: 1px solid #ccc;
      background-color: #FEC401;
      color: #000;
      font-size: 16px;
      appearance: none;
      background-image: url('data:image/svg+xml;charset=UTF-8,%3Csvg xmlns%3D"http://www.w3.org/2000/svg" viewBox%3D"0 0 24 24" width%3D"24" height%3D"24"%3E%3Cpath fill%3D"%23000000" d%3D"M12 16l4-4H8z"%3E%3C/path%3E%3C/svg%3E');
      background-repeat: no-repeat;
      background-position: right 10px center;
      background-size: 24px 24px; /* Increased the arrow size */
      transition: all 0.3s ease;
      cursor: pointer;
    }

      .filter-item select:hover {
        border: 1px solid #007bff;
      }

      .filter-item select:focus {
        outline: 1px solid #007bff;
      }

    .filter-item option[value=""][disabled] {
      color: #000;
    }


  .timetable-title {
    text-align: left;
    margin-top: 20px;
    font-size: 1.4em;
    font-weight: 500;
    padding-left: 20px;
    color: #333;
  }

  .image-container {
    margin-top: 20px;
  }

    .image-container img {
      width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid #ddd;
      object-fit: contain;
    }

  .loading-indicator {
    font-size: 1.2em;
    color: #007bff;
    font-weight: bold;
  }

  .download-btn {
    display: inline-block;
    margin-top: 20px;
    padding: 12px 25px;
    background-color: #1e0a74;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-bottom: 20px;
    transition: background-color 0.3s;
    font-size: 16px;
  }

    .download-btn:hover {
      background-color: #ff7a00;
    }
  @media (max-width: 1024px) {
    .timetable-container {
      padding: 20px;
    }

    .filter-section {
      flex-direction: column;
      align-items: stretch;
      padding: 10px;
    }

    .filter-title {
      margin-bottom: 15px;
      text-align: center;
      font-size: 1.1em;
    }

    .filter-item {
      margin-right: 0;
      margin-bottom: 15px;
      width: 100%; /* Ensures dropdowns take full width */
    }

      .filter-item select {
        width: 100%;
        padding: 12px;
        font-size: 16px;
      }

    .timetable-title {
      font-size: 1.3em;
      padding-left: 0;
      margin-top: 20px;
      text-align: center; /* Centered title for better alignment */
    }

    .image-container img {
      max-width: 90%;
      margin: 20px auto;
    }

    .download-btn {
      width: 100%;
      padding: 14px;
      font-size: 16px;
    }
  }

  @media (max-width: 600px) {
    .filter-title {
      font-size: 1.1em;
      text-align: center;
    }

    .filter-item select {
      padding: 12px;
      font-size: 14px;
    }

    .timetable-title {
      font-size: 1.2em;
      text-align: center; /* Centered title for smaller screens */
    }

    .image-container img {
      max-width: 100%; /* Ensures image doesn't overflow */
      margin-top: 20px;
    }

    .download-btn {
      padding: 15px 30px;
      font-size: 14px;
    }
  }

</style>
