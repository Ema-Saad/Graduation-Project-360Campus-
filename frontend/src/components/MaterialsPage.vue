<template>
  <div class="materials-page">
    <div class="filter-section">
      <h2 class="filter-title">Filter</h2>

      <!-- Faculty Filter -->
      <div class="filter-item">
        <select id="faculty-filter" v-model="filters.faculty" aria-label="Select Faculty">
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

      <!-- Level Filter -->
      <div class="filter-item">
        <select id="level-filter" v-model="filters.level" aria-label="Select Level">
          <option value="" disabled selected>Level</option>
          <option value="First Level">First Level</option>
          <option value="Second Level">Second Level</option>
          <option value="Third Level">Third Level</option>
          <option value="Fourth Level">Fourth Level</option>
          <option value="Fifth Level">Fifth Level</option>
          <option value="Sixth Level">Sixth Level</option>
        </select>
      </div>

      <!-- Semester Filter -->
      <div class="filter-item">
        <select id="semester-filter" v-model="filters.semester" aria-label="Select Semester">
          <option value="" disabled selected>Semester</option>
          <option value="Fall">Fall</option>
          <option value="Spring">Spring</option>
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
          <div class="course-image">
            <img :src="course.imageUrl" alt="Course Image" />
          </div>
          <div class="course-details">
            <div class="course-instructor">
              <img class="instructor-icon" :src="course.instructorIconUrl" alt="Instructor Icon" />
              <span>{{ course.instructor }}</span>
            </div>
            <p class="course-title">{{ course.title }}</p>
            <p class="course-code">{{ course.code }}</p>
          </div>
          <div class="course-rating">
            <span v-for="n in 5" :key="n" :class="{ filled: n <= course.rating }">★</span>
          </div>
        </router-link>
      </div>
    </div>

    <!-- Only Show Filtered Courses After Filters are Applied -->
    <div v-if="isFiltered && filteredCourses.length > 0" class="filtered-courses">
      <h2 class="best-courses-title">Filtered Courses</h2>

      <div class="course-list">
        <router-link v-for="course in filteredCourses" :key="course.id"
                     :to="{ name: 'CourseDetails', params: { id: course.id } }"
                     class="course-item">
          <div class="course-image">
            <img :src="course.imageUrl" alt="Course Image" />
          </div>
          <div class="course-details">
            <div class="course-instructor">
              <img class="instructor-icon" :src="course.instructorIconUrl" alt="Instructor Icon" />
              <span>{{ course.instructor }}</span>
            </div>
            <p class="course-title">{{ course.title }}</p>
            <p class="course-code">{{ course.code }}</p>
          </div>
          <div class="course-rating">
            <span v-for="n in 5" :key="n" :class="{ filled: n <= course.rating }">★</span>
          </div>
        </router-link>
      </div>
    </div>

    <!-- Message when no courses match the filter -->
    <div v-if="isFiltered && filteredCourses.length === 0" class="no-courses-message">
      <p>No courses found for the selected filters. Please adjust your filters.</p>
    </div>
  </div>
</template>

<script>
  import courseImage from '@/assets/pexels-pixabay.jpg'; // Common image for all courses
  import instructorIcon1 from '@/assets/doctor-img.png'; // Icon for Dr. Mohamed
  import instructorIcon2 from '@/assets/doctor-img2.png'; // Icon for Dr. Ayman
  import instructorIcon3 from '@/assets/doctor-img3.png'; // Icon for Dr. Mostafa

  export default {
    name: 'MaterialsPage',
    data() {
      return {
        // Predefined set of popular courses
        popularCourses: [
          { id: 1, code: 'CSC 410', title: 'Software Quality', instructor: 'Dr. Mohamed', instructorIconUrl: instructorIcon1, imageUrl: courseImage, rating: 5, faculty: 'Computer Science', level: 'First Level', semester: 'Spring' },
          { id: 2, code: 'CSC 420', title: 'Web Development', instructor: 'Dr. Mohamed', instructorIconUrl: instructorIcon1, imageUrl: courseImage, rating: 4, faculty: 'Computer Science', level: 'Second Level', semester: 'Spring' },
          { id: 3, code: 'CSC 430', title: 'Database Systems', instructor: 'Dr. Ayman', instructorIconUrl: instructorIcon2, imageUrl: courseImage, rating: 3, faculty: 'Computer Science', level: 'Third Level', semester: 'Fall' },
          { id: 4, code: 'CSC 440', title: 'Artificial Intelligence', instructor: 'Dr. Mostafa', instructorIconUrl: instructorIcon3, imageUrl: courseImage, rating: 5, faculty: 'Engineering', level: 'Third Level', semester: 'Fall' },
        ],

        // Array of all courses, including popular and filtered ones
        courses: [
          { id: 1, code: 'CSC 410', title: 'Software Quality', instructor: 'Dr. Mohamed', instructorIconUrl: instructorIcon1, imageUrl: courseImage, rating: 5, faculty: 'Computer Science', level: 'First Level', semester: 'Spring' },
          { id: 2, code: 'CSC 420', title: 'Web Development', instructor: 'Dr. Mohamed', instructorIconUrl: instructorIcon1, imageUrl: courseImage, rating: 4, faculty: 'Computer Science', level: 'Second Level', semester: 'Spring' },
          { id: 3, code: 'CSC 430', title: 'Database Systems', instructor: 'Dr. Ayman', instructorIconUrl: instructorIcon2, imageUrl: courseImage, rating: 3, faculty: 'Computer Science', level: 'Third Level', semester: 'Fall' },
          { id: 4, code: 'CSC 440', title: 'Artificial Intelligence', instructor: 'Dr. Mostafa', instructorIconUrl: instructorIcon3, imageUrl: courseImage, rating: 5, faculty: 'Engineering', level: 'Third Level', semester: 'Fall' },
          { id: 5, code: 'CSC 450', title: 'Machine Learning', instructor: 'Dr. Ayman', instructorIconUrl: instructorIcon2, imageUrl: courseImage, rating: 4, faculty: 'Engineering', level: 'First Level', semester: 'Spring' },
        ],

        filters: {
          faculty: '',  // Selected faculty
          level: '',    // Selected level
          semester: '', // Selected semester
        },
      };
    },
    computed: {
      // Check if any filter has been applied
      isFiltered() {
        return this.filters.faculty || this.filters.level || this.filters.semester;
      },

      // Filter courses based on selected filters (faculty, level, semester)
      filteredCourses() {
        return this.courses.filter((course) => {
          return (
            (this.filters.faculty === '' || course.faculty === this.filters.faculty) &&
            (this.filters.level === '' || course.level === this.filters.level) &&
            (this.filters.semester === '' || course.semester === this.filters.semester)
          );
        });
      },
    },
  };
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
      background-size: 16px;
    }

      .filter-item select:focus {
        outline: 2px solid #007bff;
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
    background-color: #f9f9f9;
    border-radius: 8px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: inherit;
  }

    .course-item:hover {
      background-color: #e0e0e0;
    }

  .course-image {
    flex: 0 0 100px;
    margin-right: 16px;
  }

    .course-image img {
      width: 100%;
      height: auto;
      border-radius: 4px;
      object-fit: cover;
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

  .instructor-icon {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    margin-right: 8px;
  }

  .course-title {
    font-size: 18px;
    font-weight: bold;
  }

  .course-code {
    font-weight: bold;
    color: #666;
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
</style>
