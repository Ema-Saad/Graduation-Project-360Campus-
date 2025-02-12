<template>
  <div>
    <!-- Main Header Image inside a container -->
    <div class="image-container">
      <div class="overlay">
        <div class="overlay-text">
          <span class="course-code">{{ course.title }}</span>
          <h1 class="course-name">{{ course.description }}</h1>
        </div>
      </div>
      <img src="../assets/pexels-photo.png" alt="Course Image" class="main-image" />
    </div>

    <h1>{{ course.title }}</h1>
    <p>{{ course.description }}</p>

    <div class="weeks-container">
      <div class="week-box" v-for="week in weeks" :key="week.id">
        <!-- Week Box with Overlay -->
        <div class="week-header" @click="toggleDropdown(week.id)">
          <div class="week-image-container">
            <!-- Week Overlay on top of Image -->
            <div class="week-overlay">
              Week {{ week.id }} <!-- Display "Week" before the Week ID -->
            </div>
            <img src="../assets/pexels-photo.png" alt="Week Image" class="week-image" />
          </div>
          <span class="arrow" :class="{ 'rotate': isDropdownOpen(week.id) }">&#9660;</span>
        </div>

        <div v-if="isDropdownOpen(week.id)" class="dropdown-menu">
          <router-link :to="{ name: 'Lecture', params: { weekId: week.id } }" class="dropdown-item">Lecture</router-link>
          <router-link :to="{ name: 'Tutorial', params: { weekId: week.id } }" class="dropdown-item">Tutorial</router-link>
          <router-link :to="{ name: 'Lab', params: { weekId: week.id } }" class="dropdown-item">Lab</router-link>
          <!-- Navigate to 'AssignmentById' route -->
          <router-link :to="{ name: 'AssignmentById', params: { id: course.id, week: week.id } }" class="dropdown-item">Assignment</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['id'],
    data() {
      return {
        course: {
          title: 'Course Title',
          description: 'Course Description',
        },
        weeks: [
          { id: 1 },
          { id: 2 },
          { id: 3 },
        ],
        openDropdowns: [], // Store open dropdown states
      };
    },
    created() {
      this.loadCourse();
    },
    methods: {
      loadCourse() {
        const courseId = this.id;
        // You can load course details here based on the courseId
        // Example: make an API call to fetch course details
      },
      toggleDropdown(weekId) {
        const index = this.openDropdowns.indexOf(weekId);
        if (index === -1) {
          this.openDropdowns.push(weekId);
        } else {
          this.openDropdowns.splice(index, 1);
        }
      },
      isDropdownOpen(weekId) {
        return this.openDropdowns.includes(weekId);
      },
    },
  };
</script>


<style scoped>
  /* Container to constrain image */
  .image-container {
    width: 100%;
    position: relative; /* Positioning context for overlay */
  }
  /* Styling for the main image */
  .main-image {
    width: 100%;
    height: 250px;
    object-fit: cover;
    max-width: 100%;
    display: block;
    margin: 0 auto;
    border-bottom: 2px solid #ddd;
    max-height: 500px;
  }

  /* Overlay with dark background and centered text */
  .overlay {
    position: absolute;
    top: 30%; /* Adjust this value to move the text upwards or downwards */
    left: 30%; /* Horizontally center */
    transform: translateX(-50%); /* Center the text horizontally */
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: black; /* Text color */
    font-size: 1em; /* Adjust font size as needed */
    font-weight: bold; /* Make the text bold */
    z-index: 1; /* Ensures the overlay text is above the image */
  }



  /* Text in the overlay */
  .overlay-text {
    z-index: 2; /* Ensure text appears above the overlay */
  }

  .course-code {
    font-size: 1.5em;
    font-weight: bold;
  }

  .course-name {
    font-size: 2.5em;
    font-weight: bold;
    margin-top: 10px;
  }

  .week-box {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 15px;
    position: relative;
  }

    .week-box:hover {
      border: 1px solid #007bff;
    }

  .week-header {
    display: flex;
    align-items: center;
    cursor: pointer;
  }

  /* Week Image with Overlay */
  .week-image-container {
    position: relative; /* Positioning context for overlay */
    width: 100%; /* Ensure the container takes up full width */
  }

  .week-image {
    width: 25%;
    height: 120px;
    object-fit: cover;
    border-radius: 4px;
  }
  /* Week Overlay */
  /* Week Overlay */
  .week-overlay {
    position: absolute;
    top: 30%; /* Adjust the percentage to move the text upwards or downwards */
    left: 3%; /* Horizontally center */
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: black; /* Text color */
    font-size: 2em; /* Adjust as needed */
    font-weight: bold; /* Make the text bold */
    z-index: 1;
  }

  .week-overlay-text {
    z-index: 2; /* Ensure text appears above the overlay */
  }

  .arrow {
    margin-left: auto;
    transition: transform 0.3s ease;
  }

    .arrow.rotate {
      transform: rotate(180deg);
    }

  .dropdown-menu {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
  }

  .dropdown-item {
    text-decoration: none;
    color: black;
    padding: 8px 0;
  }

    .dropdown-item:hover {
      text-decoration: underline;
      color: #007bff; /* Optional: Change color to blue when hovered */
    }
  /* Responsive Styles */
  @media screen and (max-width: 1024px) {
    .overlay {
      top: 20%; /* Adjust text positioning */
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.9em; /* Adjust font size for better fit */
    }

    .course-code {
      font-size: 1.2em;
    }

    .course-name {
      font-size: 2em;
    }

    .main-image {
      height: 200px; /* Smaller image size for smaller screens */
    }

    .week-image {
      width: 35%; /* Adjust image width for better fit */
      height: 100px;
    }

    .week-overlay {
      font-size: 1.5em; /* Reduce overlay text size */
      left: 5%;
    }
  }

  @media screen and (max-width: 768px) {
    .overlay {
      top: 15%;
      font-size: 0.8em;
    }

    .course-code {
      font-size: 1em;
    }

    .course-name {
      font-size: 1.8em;
    }

    .week-box {
      padding: 8px;
    }

    .week-header {
      flex-direction: column; /* Stack elements vertically */
      align-items: flex-start;
    }

    .week-image {
      width: 100%; /* Full width */
      height: auto;
    }

    .week-overlay {
      font-size: 1.2em;
      left: 10%;
    }
  }

  @media screen and (max-width: 480px) {
    .overlay {
      top: 10%;
      font-size: 0.7em;
    }

    .course-code {
      font-size: 0.9em;
    }

    .course-name {
      font-size: 1.5em;
    }

    .main-image {
      height: 150px; /* Even smaller image for very small screens */
    }

    .week-box {
      padding: 5px;
    }

    .week-image {
      width: 100%;
      height: auto;
    }

    .week-overlay {
      font-size: 1em;
      left: 15%;
    }

    .dropdown-item {
      font-size: 14px; /* Reduce text size for smaller screens */
      padding: 6px 0;
    }
  }

</style>
