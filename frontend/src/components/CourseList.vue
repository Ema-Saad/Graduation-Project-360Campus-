<template>
  <div class="materials-page">
    <div class="filter-section">
      <h2 class="filter-title">Filter</h2>

      <!-- Faculty Filter -->
      <div class="filter-item">
        <select id="faculty-filter" v-model="filters.faculty">
          <option value="">Faculty</option>
          <option v-for="college in colleges" :value="college.code">{{ college.name }}</option>
        </select>
      </div>

      <!-- Level Filter -->
      <div class="filter-item">
        <select id="level-filter" v-model="filters.level">
          <option value="">Level</option>
          <option value="1">First Level</option>
          <option value="2">Second Level</option>
          <option value="3">Third Level</option>
          <option value="4">Fourth Level</option>
          <option value="5">Fifth Level</option>
          <option value="6">Sixth Level</option>
        </select>
      </div>

      <!-- Semester Filter -->
      <div class="filter-item">
        <select id="semester-filter" v-model="filters.semester">
          <option value="">Semester</option>
          <option value="F">Fall</option>
          <option value="S">Spring</option>
        </select>
      </div>
    </div>

    <!-- Display Popular Courses if No Filters are Applied -->
    <div v-if="!isFiltered" class="popular-courses">
      <h2 class="best-courses-title">Our Popular Courses</h2>
      <div class="course-list">
        <router-link v-for="course in popularCourses" :key="course.id"
                     :to="{ name: 'CourseDetails', params: { id: course.id } }"
                     class="course-item">
          <!--<div class="course-image">
            <img :src="course.imageUrl" alt="Course Image" />
          </div>-->
          <div class="course-details">
            <p class="course-title">{{ course.title }}</p>
            <p class="course-code">{{ course.id }}</p>
          </div>
        </router-link>
      </div>
    </div>

    <!-- Show Filtered Courses if Filters are Applied -->
    <div v-if="isFiltered && filteredCourses.length > 0" class="filtered-courses">
      <h2 class="best-courses-title">Filtered Courses</h2>
      <div class="course-list">
        <!-- Course Item -->
        <router-link v-for="course in filteredCourses" :key="course.id"
                     :to="{ name: 'CourseDetails', params: { id: course.id } }"
                     class="course-item">
          <!--<div class="course-image">
            <img :src="course.imageUrl" alt="Course Image" />
          </div>-->
          <div class="course-details">
            <p class="course-title">{{ course.title }}</p>
            <p class="course-code">{{ course.id }}</p>
          </div>
        </router-link>
      </div>
    </div>

    <!-- Message if No Courses Match the Filter -->
    <div v-if="isFiltered && filteredCourses.length === 0" class="no-courses-message">
      <p>No courses found for the selected filters. Please adjust your filters.</p>
    </div>
  </div>
</template>

<script>
  import courseImage from '@/assets/pexels-photo.png'; // Common image for all courses
  import instructorIcon1 from '@/assets/doctor-img4.png'; // Icon for Dr. Mohamed
  import instructorIcon2 from '@/assets/doctor-img4.png'; // Icon for Dr. Ayman
  import instructorIcon3 from '@/assets/doctor-img4.png'; // Icon for Dr. Mostafa

  export default {
    name: 'CourseList',
    data() {
      return {
        colleges: [],
        popularCourses: [],
        courses: [],

        filters: {
          faculty: '',  // Selected faculty
          level: '',    // Selected level
          semester: '', // Selected semester
        },
      };
    },
    beforeMount() {
      let colleges = this.$root.request_api_endpoint('api/colleges', 'get', null);
      let courses = this.$root.request_api_endpoint('api/courses', 'get', null);

      colleges.then((data) => { 
        this.colleges = data;
      });

      courses.then((data) => {
        this.popularCourses = this.courses = data;
      });

    },
    computed: {
      isFiltered() {
        return this.filters.faculty || this.filters.level || this.filters.semester;
      },

      filteredCourses() {
        return this.courses.filter(course => {
          return (
            (!this.filters.faculty || course.college.code === this.filters.faculty) &&
            (!this.filters.level || course.level === this.filters.level) &&
            (!this.filters.semester || course.semester === this.filters.semester)
          );
        });
      },
    },
  }
</script>

<style scoped>
  /* Styles for the page layout and appearance */
  .materials-page {
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
      background-size: 24px; /* Increase the size of the arrow */
      transition: all 0.3s ease;
      cursor: pointer;
    }

      /* Hover effect for select elements */
      .filter-item select:hover {
        border: 1px solid #007bff;
      }

      .filter-item select:focus {
        outline: 1px solid #007bff;
      }

  .best-courses-title {
    margin-top: 20px;
    font-size: 24px;
    font-weight: bold;
    color: #333;
  }

  .course-list {
    padding: 20px;
  }

  .course-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px;
    border-radius: 8px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: inherit;
    border: 1px solid #ccc; /* Add a border with color */
  }

    .course-item:hover {
      border: 1px solid #007bff; /* Change border color to blue on hover */
    }
  .course-image {
    position: relative;
    flex: 0 0 250px; /* Adjust width as needed */
    margin-right: 16px;
  }

    .course-image img {
      width: 100%; /* Ensures the image fills the container */
      height: auto;
      border-radius: 4px;
      object-fit: cover;
    }

  .overlay-text {
    position: absolute;
    top: 50%;
    left: 10px; /* Adjust to fit text within the image */
    transform: translateY(-50%);
    color: black;
    padding: 10px;
    border-radius: 4px;
    width: 90%;
  }

    .overlay-text .course-title,
    .overlay-text .course-code {
      font-size: 16px;
      font-weight: bold;
      margin: 0;
      color: black;
    }

  .course-details {
    flex: 1;
    font-size: 16px;
  }

  .course-instructor {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
  }
  /* Instructor Info Styles */
  .instructor-info {
    display: flex; /* Align the image and text side by side */
    align-items: center; /* Vertically center the content */
    justify-content: flex-start; /* Align items to the left */
    gap: 15px; /* Space between the image and the text */
    padding: 10px 0; /* Add padding to separate from other elements */
    margin-right: 90px; /* Ensure the container starts from the left edge */
  }

  /* Avatar container to handle background gradient */
  .instructor-avatar-container {
    width: 40px; /* Reduced width */
    height: 40px; /* Reduced height */
    border-radius: 50%; /* Circular shape */
    background: linear-gradient(to bottom, #f08a24, #3b3b98);
    display: flex; /* Center the image inside the container */
    justify-content: center; /* Center the image horizontally */
    align-items: center; /* Center the image vertically */
    margin-right: 10px; /* Add space between the avatar and the info */
  }

  /* Avatar image inside the container */
  .instructor-avatar {
    width: 30px; /* Adjusted width to fit the new container size */
    height: 30px; /* Adjusted height to fit the new container size */
    border-radius: 50%; /* Keep image circular */
    object-fit: cover; /* Ensure image covers the circle area */
  }

  .instructor-info div {
    display: flex;
    flex-direction: column; /* Stack the instructor name and course subtitle vertically */
  }

  .instructor-name {
    font-size: 1.1em; /* Slightly larger font size for the instructor's name */
    font-weight: bold; /* Make the instructor's name bold */
    color: #333; /* Dark gray color for the name */
  }


  .course-title {
    font-size: 18px;
    font-weight: bold;
  }

  .course-code {
    font-weight: bold;
    font-size: 16px;
  }

  .course-rating {
    display: flex;
    gap: 5px;
    font-size: 18px;
  }

    .course-rating .filled {
      color: #f0c14b;
    }

  .no-courses-message {
    text-align: center;
    color: #888;
    font-size: 16px;
    margin-top: 30px;
  }



  /* Responsive styles */
  @media screen and (max-width: 1024px) {
    .filter-section {
      flex-direction: column;
      align-items: stretch;
    }

    .filter-item {
      margin-right: 0;
      margin-bottom: 10px;
      width: 100%;
    }

      .filter-item select {
        width: 100%;
      }

    .course-list {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 15px;
    }

    .course-item {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .course-image {
      flex: 0 0 auto;
      width: 100%;
      max-width: 300px;
      margin-bottom: 10px;
    }

    .course-details {
      text-align: center;
    }
  }

  @media screen and (max-width: 768px) {
    /* Adjust filter section layout */
    .filter-section {
      flex-direction: column;
      align-items: stretch;
      padding: 15px;
    }

    /* Adjust filter item layout */
    .filter-item {
      margin-right: 0;
      margin-bottom: 15px;
      width: 100%;
    }

      .filter-item select {
        width: 100%;
        padding: 10px;
        font-size: 14px;
      }

    /* Adjust course list layout */
    .course-list {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 15px;
    }

    /* Adjust course item padding and layout */
    .course-item {
      padding: 12px;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    /* Adjust course image layout */
    .course-image {
      width: 100%;
      max-width: 250px;
      margin-bottom: 10px;
    }

    /* Adjust course details text alignment */
    .course-details {
      text-align: center;
    }

    /* Adjust course title font size */
    .course-title {
      font-size: 16px;
    }

    /* Adjust course code font size */
    .course-code {
      font-size: 14px;
    }

    /* Adjust rating font size */
    .course-rating {
      font-size: 16px;
    }

    /* Adjust instructor name font size */
    .instructor-name {
      font-size: 14px;
    }
  }

</style>
