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
      <img :src="mainImage" alt="Course Image" class="main-image" />
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
              Week {{ week.id }}
            </div>
            <img :src="weekImage" alt="Week Image" class="week-image" />
          </div>
          <span class="arrow" :class="{ 'rotate': isDropdownOpen(week.id) }">&#9660;</span>
        </div>

        <!-- Dropdown Menu with a stable parent container -->
        <div v-if="isDropdownOpen(week.id)" :key="'dropdown-' + week.id" class="dropdown-menu">
          <ul class="dropdown-list">
            <li class="dropdown-item">
              <router-link :to="{ name: 'DOCLecture', params: { id: course.id } }">
                Lecture
              </router-link>
            </li>
            <li class="dropdown-item">
              <router-link :to="{ name: 'DOCTutorial', params: { id: course.id } }">
                Tutorial
              </router-link>
            </li>
            <li class="dropdown-item">
              <router-link :to="{ name: 'DOCLab', params: { id: course.id } }">
                Lab
              </router-link>
            </li>
            <li class="dropdown-item">
              <router-link :to="{ name: 'DOCAssignmentById', params: { id: course.id } }">
                Assignment
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  // Import images directly in Vue.js
  import mainImage from '@/assets/pexels-photo.png'; // Main image
  import weekImage from '@/assets/static-week-image.png'; // Static week image

  export default {
    props: ['id'],
    data() {
      return {
        course: {
          id: this.id, // Use the passed prop for the course id
          title: 'Course Title',
          description: 'Course Description',
        },
        weeks: [
          { id: 1 },
          { id: 2 },
          { id: 3 },
        ],
        mainImage, // imported main image
        weekImage, // imported week image
        openDropdowns: [], // Track open dropdowns
      };
    },
    created() {
      this.loadCourse();
    },
    methods: {
      loadCourse() {
        const courseId = this.id;
        // Example: API call to fetch course details using courseId
        console.log(`Loading course with ID: ${courseId}`);
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
    position: relative;
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
    top: 30%;
    left: 30%;
    transform: translateX(-50%);
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: black;
    font-size: 1em;
    font-weight: bold;
    z-index: 1;
  }

  /* Text in the overlay */
  .overlay-text {
    z-index: 2;
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
    position: relative;
    width: 100%;
  }

  .week-image {
    width: 25%;
    height: 120px;
    object-fit: cover;
    border-radius: 4px;
  }

  /* Week Overlay */
  .week-overlay {
    position: absolute;
    top: 30%;
    left: 3%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: black;
    font-size: 2em;
    font-weight: bold;
    z-index: 1;
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
  }

  .dropdown-list {
    list-style: none;
    padding: 0;
    margin: 0;
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
      color: #007bff;
    }

  /* Responsive Styles */
  @media screen and (max-width: 1024px) {
    .overlay {
      top: 20%;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.9em;
    }

    .course-code {
      font-size: 1.2em;
    }

    .course-name {
      font-size: 2em;
    }

    .main-image {
      height: 200px;
    }

    .week-image {
      width: 35%;
      height: 100px;
    }

    .week-overlay {
      font-size: 1.5em;
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
      flex-direction: column;
      align-items: flex-start;
    }

    .week-image {
      width: 100%;
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
      height: 150px;
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
      font-size: 14px;
      padding: 6px 0;
    }
  }
</style>
