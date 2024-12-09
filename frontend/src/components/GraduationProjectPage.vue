<template>
  <div class="projects-page">
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

      <!-- Year Filter -->
      <div class="filter-item">
        <select id="year-filter" v-model="filters.year" aria-label="Select Year">
          <option value="" disabled selected>Year</option>
          <option value="2022">2022</option>
          <option value="2023">2023</option>
          <option value="2024">2024</option>
          <option value="2025">2025</option>
        </select>
      </div>
    </div>

    <!-- "Our Best Projects" section when no filters are applied -->
    <div v-if="!filters.faculty && !filters.year" class="best-projects">
      <h2 class="projects-title">Our Best Projects</h2>

      <div class="project-list">
        <router-link v-for="project in popularProjects" :key="project.id"
                     :to="{ name: 'ProjectDetails', params: { id: project.id } }"
                     class="project-item">
          <div class="project-image">
            <img :src="project.imageUrl" alt="Project Image" />
          </div>
          <div class="project-details">
            <div class="project-title">{{ project.title }}</div>
            <div class="project-instructor">
              <img class="instructor-icon" :src="project.instructorIconUrl" alt="Instructor Icon" />
              <div>
                <span class="instructor-name">{{ project.instructor }}</span>
                <p class="project-major">Majors: {{ project.major }}</p>
              </div>
            </div>
          </div>
          <div class="project-rating">
            <span v-for="n in 5" :key="n" class="star">★</span>
          </div>
        </router-link>
      </div>
    </div>

    <!-- Only Show Filtered Projects After Both Filters are Selected -->
    <div v-if="filters.faculty && filters.year && filteredProjects.length > 0" class="filtered-projects">
      <h2 class="projects-title">Filtered Graduation Projects</h2>

      <div class="project-list">
        <router-link v-for="project in filteredProjects" :key="project.id"
                     :to="{ name: 'ProjectDetails', params: { id: project.id } }"
                     class="project-item">
          <div class="project-image">
            <img :src="project.imageUrl" alt="Project Image" />
          </div>
          <div class="project-details">
            <div class="project-title">{{ project.title }}</div>
            <div class="project-instructor">
              <img class="instructor-icon" :src="project.instructorIconUrl" alt="Instructor Icon" />
              <div>
                <span class="instructor-name">{{ project.instructor }}</span>
                <p class="project-major">Majors: {{ project.major }}</p>
              </div>
            </div>
          </div>
          <div class="project-rating">
            <span v-for="n in 5" :key="n" class="star">★</span>
          </div>
        </router-link>
      </div>
    </div>

    <!-- Message when no projects match the filter -->
    <div v-else-if="filters.faculty && filters.year" class="no-projects-message">
      <p>No projects found for the selected filters. Please adjust your filters.</p>
    </div>
  </div>
</template>

<script>
  import projectImage from '@/assets/pexels-photo.png';
  import instructorIcon1 from '@/assets/doctor-img.png';
  import instructorIcon2 from '@/assets/doctor-img2.png';
  import instructorIcon3 from '@/assets/doctor-img3.png';

  export default {
    name: 'ProjectsPage',
    data() {
      return {
        popularProjects: [
          { id: 1, code: 'GP 410', title: 'Smart Irrigation System', instructor: 'Dr. Mohamed', instructorIconUrl: instructorIcon1, imageUrl: projectImage, major: 'Computer Science', faculty: 'Computer Science', year: '2024' },
          { id: 2, code: 'GP 420', title: 'Energy Efficient Homes', instructor: 'Dr. Ahmed', instructorIconUrl: instructorIcon2, imageUrl: projectImage, major: 'Sustainable Architecture', faculty: 'Engineering', year: '2023' },
          { id: 3, code: 'GP 430', title: 'AI in Healthcare', instructor: 'Dr. Ayman', instructorIconUrl: instructorIcon3, imageUrl: projectImage, major: 'Artificial Intelligence', faculty: 'Engineering', year: '2024' },
        ],
        projects: [
          { id: 1, code: 'GP 410', title: 'Smart Irrigation System', instructor: 'Dr. Mohamed', instructorIconUrl: instructorIcon1, imageUrl: projectImage, major: 'Computer Science', faculty: 'Computer Science', year: '2024' },
          { id: 2, code: 'GP 420', title: 'Energy Efficient Homes', instructor: 'Dr. Ahmed', instructorIconUrl: instructorIcon2, imageUrl: projectImage, major: 'Sustainable Architecture', faculty: 'Engineering', year: '2023' },
          { id: 3, code: 'GP 430', title: 'AI in Healthcare', instructor: 'Dr. Ayman', instructorIconUrl: instructorIcon3, imageUrl: projectImage, major: 'Artificial Intelligence', faculty: 'Engineering', year: '2024' },
        ],
        filters: {
          faculty: '',
          year: '',
        },
      };
    },
    computed: {
      filteredProjects() {
        return this.projects.filter((project) => {
          return (
            (this.filters.faculty === '' || project.faculty === this.filters.faculty) &&
            (this.filters.year === '' || project.year === this.filters.year)
          );
        });
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
    margin-right: 20px;
  }

    .filter-item select {
      width: 150px;
      padding: 8px;
      border: 1px solid #ccc;
      background-color: #FEC401;
      color: #000;
      font-size: 16px;
    }

  .projects-title {
    margin-top: 20px;
    font-size: 24px;
    font-weight: bold;
    color: #333;
  }

  .project-list {
    padding: 20px;
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

  .project-image img {
    width: 150px;
    height: auto;
    border-radius: 8px;
    margin-right: 15px;
  }

  .project-details {
    flex: 1;
  }

  .project-title {
    font-size: 18px;
    font-weight: bold;
    color: #333;
  }

  .project-instructor {
    display: flex;
    align-items: center;
    margin-top: 8px;
  }

  .instructor-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }

  .instructor-name {
    font-weight: bold;
    font-size: 16px;
    color: #333;
  }

  .project-major {
    font-size: 14px;
    color: #666;
  }

  .project-rating {
    margin-left: auto;
    color: #FEC401;
    font-size: 20px;
  }

  .star {
    margin-right: 3px;
  }
</style>
