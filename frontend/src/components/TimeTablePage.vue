<template>
  <div class="timetable-container">
    <!-- Filters Section -->
    <div class="filter-section">
      <h2 class="filter-title">Filter</h2>
      <div class="filter-item">
        <select v-model="selectedFaculty" aria-label="Select Faculty">
          <option value="" disabled selected>Faculty</option>
          <option value="Pharma D">Pharma D</option>
          <option value="Engineering">Engineering</option>
          <option value="Computer Science">Computer Science</option>
          <option value="Sustainable Architecture">Sustainable Architecture</option>
          <option value="Basic and Applied Science">Basic and Applied Science</option>
          <option value="Art and Design">Art and Design</option>
          <option value="International Business">International Business</option>
        </select>
      </div>

      <div class="filter-item">
        <select v-model="selectedLevel" aria-label="Select Level">
          <option value="" disabled selected>Level</option>
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
          <option value="" disabled selected>Semester</option>
          <option value="Fall">Fall</option>
          <option value="Spring">Spring</option>
        </select>
      </div>
    </div>

    <!-- Display Selected Faculty, Level, and Semester -->
    <h3>{{ selectedFaculty }} {{ selectedLevel }} {{ selectedSemester }} Time Table</h3>

    <!-- Display Image Instead of PDF -->
    <div class="image-container">
      <!-- Loading Indicator -->
      <div v-if="isLoading" class="loading-indicator">Loading...</div>
      <!-- Image Preview -->
      <img :src="imagePath" alt="Time Table" v-if="imagePath" />
      <!-- Fallback Image -->
      <img v-else src="@/assets/placeholder.jpg" alt="No Time Table Available" />
    </div>

    <!-- Download Button -->
    <button @click="downloadImage" class="download-btn" v-if="imagePath" :aria-label="downloadButtonLabel">
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
        if (this.selectedFaculty && this.selectedLevel && this.selectedSemester) {
          this.isLoading = true;

          // Format the filter values by replacing spaces with underscores
          const formattedFaculty = this.selectedFaculty.replace(/\s+/g, '_');
          const formattedLevel = this.selectedLevel.replace(/\s+/g, '_');
          const formattedSemester = this.selectedSemester.replace(/\s+/g, '_');

          // Construct image filename
          const imageName = `${formattedFaculty}_${formattedLevel}_${formattedSemester}.jpg`;

          // Use Vite's import.meta.glob to dynamically load the image
          const images = import.meta.glob('@/assets/*.jpg');  // Load all .jpg images from assets

          // Get the matching image path
          const imagePath = images[`/src/assets/${imageName}`];

          console.log("imagePath:", imagePath); // Debugging line to check image path

          if (imagePath) {
            // If the image exists, set imagePath to the imported module path
            this.imagePath = imagePath;
          } else {
            // Fallback to an empty path or a default image if not found
            this.imagePath = "";
          }

          this.isLoading = false;
        } else {
          this.imagePath = ""; // Clear image path if any selection is missing
        }
      },

      downloadImage() {
        if (this.imagePath) {
          const link = document.createElement('a');
          link.href = this.imagePath;
          link.download = `${this.selectedFaculty}_${this.selectedLevel}_${this.selectedSemester}_TimeTable.jpg`;
          link.click();
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
    padding: 10px;
    border-bottom: 1px solid #ccc;
    justify-content: center;
  }

  .filter-title {
    margin-right: 20px;
    font-weight: bold;
    font-size: 1.2em;
    color: #333;
  }

  .filter-item {
    margin-right: 30px;
  }

    .filter-item select {
      width: 200px;
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
      background-size: 16px;
    }

      .filter-item select:focus {
        outline: 2px solid #007bff;
      }

    .filter-item option[value=""][disabled] {
      color: #000;
    }

  h3 {
    margin-top: 20px;
    font-size: 1.2em;
  }

  .image-container img {
    width: 100%;
    height: auto;
    border-radius: 8px;
    border: 1px solid #ddd;
    margin-top: 20px;
  }

  .loading-indicator {
    font-size: 1.2em;
    color: #007bff;
    font-weight: bold;
  }

  .download-btn {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #1e0a74;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-bottom: 20px;
    transition: background-color 0.3s;
  }

    .download-btn:hover {
      background-color: #0056b3;
    }
</style>
