<template>
  <div>
    <!-- Main Header Image inside a container -->
    <div class="image-container">
      <img src="../assets/pexels-photo.png" alt="Course Image" class="main-image" />
    </div>

    <h1>{{ course.title }}</h1>
    <p>{{ course.description }}</p>

    <div class="weeks-container">
      <div class="week-box" v-for="week in weeks" :key="week.id">
        <div class="week-header" @click="toggleDropdown(week.id)">
          <img src="../assets/pexels-photo.png" alt="Week Image" class="week-image" />
          <span class="arrow" :class="{ 'rotate': isDropdownOpen(week.id) }">&#9660;</span>
        </div>

        <div v-if="isDropdownOpen(week.id)" class="dropdown-menu">
          <router-link :to="{ name: 'Lecture', params: { weekId: week.id } }" class="dropdown-item">Lecture</router-link>
          <router-link :to="{ name: 'Tutorial', params: { weekId: week.id } }" class="dropdown-item">Tutorial</router-link>
          <router-link :to="{ name: 'Lab', params: { weekId: week.id } }" class="dropdown-item">Lab</router-link>
          <router-link :to="{ name: 'Assignment', params: { weekId: week.id } }" class="dropdown-item">Assignment</router-link>
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
    width: 100%; /* Allow the container to take full width */
    max-width: 1200px; /* Optional: Limit the max width of the image container */
    margin: 0 auto; /* Center the image */
    overflow: hidden; /* Hide excess image if it exceeds the container */
  }

  /* Styling for the main image */
  .main-image {
    width: 100%; /* Make the image fill the container width */
    height: auto; /* Maintain the aspect ratio */
    object-fit: cover; /* Ensures the image covers the space without distortion */
  }

  .week-box {
    border: 1px solid #007bff;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 15px;
    position: relative;
  }

  .week-header {
    display: flex;
    align-items: center;
    cursor: pointer;
  }

  .week-image {
    width: 60px;
    height: auto;
    border-radius: 4px;
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
    color: #007bff;
    padding: 8px 0;
  }

    .dropdown-item:hover {
      text-decoration: underline;
    }
</style>
