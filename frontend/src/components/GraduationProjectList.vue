<template>
  <GraduationProjectCreate 
    v-if="$root.person_kind === 'P' && showPopup" 
    @closed="showPopup = false"
  />

  <div class="projects-page">
    <div class="filter-section">
      <h2 class="filter-title">Filter</h2>

      <!-- Faculty Filter -->
      <div class="filter-item">
        <select v-model="filters.faculty" @change="updateFilter">
          <option value="">Faculty</option>
          <option v-for="college in colleges" :value="college.id" :key="college.id">
            {{ college.name }}
          </option>
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

      <button v-if="$root.person_kind === 'P'" @click="showPopup = true">
        Upload New Project
      </button>
    </div>

    <div v-if="filteredProjects.length > 0" class="filtered-projects">
    <h2 class="projects-title">
  {{ filters.faculty || filters.year ? "Filtered Graduation Projects" : "Popular Graduation Projects" }}
</h2>
      <div class="project-list">
        <router-link 
          v-for="project in filteredProjects" 
          :key="project.id" 
          :to="{ name: 'GraduationProjectView', params: { graduationProjectId: project.id } }" 
          class="project-item"
        >
          <div class="project-image">
            <img :src="project.imageUrl || defaultProjectImg" alt="Project Image" />
            <div class="overlay">
             <div class="overlay-text">
  <p class="project-title-overlay">{{ project.name }}</p>
</div>
            </div>
          </div>
          <div class="project-details">
        <div class="project-instructor">
  <div class="instructor-avatar-container">
    <img class="instructor-icon" :src="project.instructorIconUrl || defaultInstructorIcon" alt="Instructor Icon" />
    <div class="instructor-info">
<span class="instructor-name">csit_csc_prof1</span>
    </div>
  </div>
</div>
            <p class="project-major">Majors: {{ project.faculty }}</p>
          </div>
          <div class="project-rating">
            <span v-for="n in Math.floor(project.rate * 0.5)" :key="n" class="star">★</span>
            <button v-if="$root.person_kind === 'P'" class="remove-btn" @click.stop="removeProject(project.id)">Remove</button>
          </div>
        </router-link>
      </div>
    </div>

    <div v-else class="no-projects-message">
      <p>No projects found for the selected filters. Please adjust your filters.</p>
    </div>
  </div>
</template>

<script>
import defaultProjectImg from '@/assets/project-image.png';
import defaultInstructorIcon from '@/assets/customer.png';
import GraduationProjectCreate from './GraduationProjectCreate.vue'
import { useGlobalStore } from '@/global_store.js'

export default {
  name: "ProjectsPage",
  components: {
    GraduationProjectCreate,
  },
  data() {
    return {
      showPopup: false,
      colleges: [],
       defaultProjectImg,
    defaultInstructorIcon,
      projects: [], // Stores all graduation projects fetched from the API
      filters: {
        faculty: "",
        year: ""
      }
    };
  },
  
  computed: {
    filteredProjects() {
      return this.projects.filter(project => {
        return (
          (!this.filters.faculty || project.faculty === this.filters.faculty) &&
          (!this.filters.year || project.year == this.filters.year)
        );
      });
    },
  },
  async beforeRouteEnter(to, from, next) {
    const store = useGlobalStore()

    let colleges = await store.request_api_endpoint("api/colleges");
    let projects = await store.request_api_endpoint("api/graduation-projects/");

    next(vm => {
      vm.colleges = colleges
      vm.projects = projects

      vm.projects = vm.projects
          .map(d => ({ ...d, rate: parseFloat(d.rate) }))
          .sort((a, b) => a.rate - b.rate);
    })
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
    padding: 15px;
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
  background-color: #f4f8ff;
  border: 1px solid #3b3b98;
  box-shadow: 0 12px 24px rgba(59, 59, 152, 0.3);
  cursor: pointer;
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
    left: 100px;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 1; 
  }
  .overlay-text {
    color: black;
    padding: 10px;
    width: 80%;
    left: 25px;
    box-sizing: border-box;
  }
.project-title-overlay {
  font-size: 1.2rem;
  font-weight: bold;
  margin: 0;
  word-break: break-word;
  text-align: center;
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

.instructor-info {
  position: absolute;
  left: 20px;
  top: 0;
  display: flex;
  flex-direction: column;
  padding: 5px 10px 5px 30px;
  border-radius: 20px;
  min-width: 150px;
  z-index: 1; 
}

.instructor-avatar-container {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(to bottom, #f08a24, #3b3b98);
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 10px;
  position: relative; /* Added for positioning context */
}
.project-faculty {
  font-size: 0.8em;
  color: #666;
}
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
.filter-section button {
  background-color: #201887;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  margin-left: auto; /* optional: push it to the right */
}

.filter-section button:hover {
  background-color: darkorange;
  transform: translateY(-2px);
}
.remove-btn {
  background-color: #201887;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 6px 12px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  margin-left: 12px;
}

.remove-btn:hover {
  background-color: darkorange;
  transform: translateY(-1px);
}

  /* Media Queries for Responsiveness */
  @media (max-width: 1200px) {
    .filter-section {
      flex-direction: column;
      align-items: flex-start;
    }

    .filter-item {
      margin-bottom: 10px;
      width: 100%; /* Ensure filter items take full width */
    }

      .filter-item select {
        width: 100%; /* Make select dropdown take full width */
      }
  }

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

    .filter-section {
      padding: 15px;
    }

    .filter-item select {
      padding: 8px;
      width: 100%; /* Make select dropdown take full width */
    }

    .filter-item {
      width: 100%; /* Ensure filter items take full width */
      margin-bottom: 10px;
    }
  }

  @media (max-width: 480px) {
    .filter-section {
      padding: 5px;
    }

    .filter-item select {
      font-size: 12px;
      padding: 6px;
      width: 100%; /* Ensure select dropdown is full width */
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

    .projects-title {
      font-size: 18px;
      text-align: center;
    }

    .filter-title {
      font-size: 16px;
      text-align: center;
      margin-bottom: 10px;
    }

    .filter-item {
      width: 100%; /* Ensure filter items take full width */
      margin-bottom: 10px;
    }

      .filter-item select {
        padding: 6px;
        width: 100%; /* Make select dropdown take full width */
      }
  }


</style>
