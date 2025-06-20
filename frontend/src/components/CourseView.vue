<template>
  <MaterialCreate
    v-if="showMaterialCreateDialog" 
    :course_id="course.id"
    :instance="toBeEditedMaterial"
    @close="showMaterialCreateDialog = false; toBeEditedMaterial = null"
  />

  <div v-if="course">
    <!-- Course Info -->
    <div v-if="!showCourseEditingWidgets">
      <h1 id="course-title">{{ course.title }}</h1>
      <p id="course-description">{{ course.description }}</p>
    </div>
       <!-- Edit Mode -->
    <div v-else-if="showCourseEditingWidgets && $root.person_kind === 'P'" class="course-edit-container">
      <div class="edit-form-card">
        <h2 class="edit-form-title">Edit Course Information</h2>
        
        <div class="form-group">
          <label for="course-title-input" class="form-label">Course Title</label>
          <input 
            id="course-title-input"
            v-model="course.title" 
            type="text" 
            class="form-input"
            placeholder="Enter course title"
          />
        </div>
        
        <div class="form-group">
          <label for="course-description-input" class="form-label">Course Description</label>
          <textarea 
            id="course-description-input"
            v-model="course.description" 
            class="form-textarea"
            placeholder="Enter detailed course description"
            rows="6"
          ></textarea>
        </div>
        
        <div class="form-actions">
          <button @click="editCourse" class="save-button">
            <span class="button-icon"></span> Save Changes
          </button>
          <button @click="course = copy_of_course; showCourseEditingWidgets = false" class="cancel-button">
            <span class="button-icon"></span> Cancel
          </button>
        </div>
      </div>
    </div>

    <!-- Instructor Controls -->
<div id="course-edit-controls" v-if="$root.person_kind === 'P' && !showCourseEditingWidgets">
  <button @click="showMaterialCreateDialog = true">➕ Add New Material</button>
  <button @click="copy_of_course = { ...course }; showCourseEditingWidgets = true">✏️ Edit Course Info</button>
  <button @click="deleteCourse">🗑️ Delete Course</button>
</div>

    <!-- Weeks Section -->
    <div class="weeks-container">
      <div class="week-box" v-for="week in weeks" :key="week.id" @click="toggleDropdown(week.id)">
        <div class="week-content">
          <!-- Image + Text -->
          <div class="week-image-container">
            <img class="week-image" :src="weekImage" alt="Week background" />
            <div class="week-overlay">
              <span class="week-overlay-text">Week {{ week.id }}</span>
            </div>
          </div>
          <!-- Arrow -->
          <div class="week-header">
            <span class="arrow" :class="{ rotate: isDropdownOpen(week.id) }">&#9660;</span>
          </div>
        </div>

        <!-- Dropdown Menu -->
        <div class="dropdown-menu" v-if="isDropdownOpen(week.id)">
          <template v-for="materialTypeArray in week">
            <div v-if="materialTypeArray.length > 0">
              <h3>{{ stringifyMaterialType(materialTypeArray[0].kind) }}</h3>
              <ul>
                <li v-for="materialInstance in materialTypeArray" :key="materialInstance.id">
                  <a class="dropdown-item" href="" @click.prevent="download(materialInstance.id)">
                    {{ materialInstance.name }}
                  </a>

                  <span class="material-edit-controls" v-if="$root.person_kind === 'P'">
                    <button @click="toBeEditedMaterial = materialInstance; showMaterialCreateDialog = true">Edit</button>
                    <button @click="deleteMaterial(materialInstance)">Delete</button>
                  </span>
                </li>
              </ul>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import weekImage from '@/assets/pexels-photo.png';
  import MaterialCreate from './MaterialCreate.vue';
  import { useGlobalStore } from '@/global_store.js'

  /* Materials Type */
  const LAB = 'l';
  const LECTURE = 'L';
  const TUTORIAL = 't';
  const ASSIGNMENT = 'a';
  const PROBLEM_SHEET = 's';
  const OTHER = 'o';

  export default {
    props: ['courseId'],
    components: {
      MaterialCreate,
    },
    data() {
      return {
        course: null,
        copy_of_course: null,
        weeks: [],
        openDropdowns: [], // Store open dropdown states
        showCourseEditingWidgets: false,
        showMaterialCreateDialog: false,
        toBeEditedMaterial: null,
        weekImage: weekImage
      };
    },
    async beforeRouteEnter(to, from, next) {
      let store = useGlobalStore()

      let course = await store.request_api_endpoint(`api/course/${to.params.courseId}`);
      let materials = await store.request_api_endpoint(`api/course/${to.params.courseId}/materials`);

      next(vm => {
        vm.course = course
        vm.setMaterials(materials)
      });
    },
    methods: {
      setMaterials(data) {
        let max_weeks = data.map((d) => d.week || -1).reduce((a, v) => Math.max(a, v), 0);
        this.weeks = new Array(max_weeks);

        for (let i = 1; i <= max_weeks; i ++) {
          this.weeks[i] = {
            id: i,
            labs: data.filter((d) => d.week === i && d.kind === LAB),
            lectures: data.filter((d) => d.week === i && d.kind === LECTURE),
            tutorials: data.filter((d) => d.week === i && d.kind === TUTORIAL),
            assignments: data.filter((d) => d.week === i && d.kind === ASSIGNMENT),
            problem_sheets: data.filter((d) => d.week === i && d.kind === PROBLEM_SHEET),
            others: data.filter((d) => d.week === i && d.kind === OTHER),
          };
        }

        this.weeks = this.weeks.filter((d) => d.labs.length + 
                                              d.lectures.length + 
                                              d.tutorials.length + 
                                              d.assignments.length + 
                                              d.problem_sheets.length +
                                              d.others.length > 0);

      },
      async editCourse() {
        try {
          let editing_result = await this.$root.request_api_endpoint(
            `api/course/${this.course.id}/edit`, 
            'post', 
            JSON.stringify(this.course),
            { 'Content-Type': 'application/json' }
          );

          this.showCourseEditingWidgets = false;
        } catch (err) {
          console.log(err);

        }
      },
      deleteCourse() {
        this.$router.push({ name: 'CourseList' });
      },
      async deleteMaterial(material) {
        try {
          await this.$root.request_api_endpoint(`api/material/${material.id}/delete`, 'delete');

        } catch (err) {

        }
      },
      stringifyMaterialType(type) {
        switch (type) {
          case LECTURE: return "Lectures"; break;
          case LAB: return "Labs"; break;
          case TUTORIAL: return "Tutorals"; break;
          case ASSIGNMENT: return "Assignments"; break;
          case PROBLEM_SHEET: return "Problem Sheets"; break;
          case OTHER: return "Other"; break;
        }
      },
      download(materialId) {
        this.$root.download_file(`api/material/${materialId}`);
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

<style>
  .image-container {
    width: 100%;
    position: relative;
  }
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
.week-box {
  border-radius: 12px;
  background-color: white;
  padding: 20px;
  margin-bottom: 24px;
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  border: 1px solid #f0f0f0;
}
.week-box:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
}

.week-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.week-image-container {
  position: relative;
  width: 200px; 
  height: 150px;
  border-radius: 8px;
  overflow: hidden;
  flex-shrink: 0;
}

.week-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.week-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.week-overlay-text {
  font-weight: bold;
  font-size: 1rem;
  color: #000;
}

.week-header {
  font-size: 1.5rem;
  color: #333;
}

.arrow {
  font-size: 1.5rem;
  transition: transform 0.3s ease;
}

.arrow.rotate {
  transform: rotate(180deg);
}

.dropdown-menu {
  margin-top: 10px;
  padding-left: 20px;
}

.dropdown-menu h3 {
  font-weight: 700;
  font-size: 1.3rem;
  margin-top: 20px;
  margin-bottom: 10px;
}

.dropdown-item {
  font-size: 1.1rem;
  font-weight: 700;
  padding: 6px 0;
  display: block;
  color: #000;
  text-decoration: none;
}

.dropdown-item:hover {
  color: #3b3b98;
}

#course-edit-controls {
  display: flex;
  gap: 16px;
  margin: 20px 0;
  flex-wrap: wrap;
  justify-content: flex-start;
}

#course-edit-controls button {
  background-color: #3b3b98;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  gap: 8px;
}

#course-edit-controls button:hover {
  background-color: darkorange;
  transform: translateY(-2px);
}
.material-edit-controls {
  display: flex;
  gap: 8px;
  margin-top: 6px;
  border-radius: 8px;
}

.material-edit-controls button {
  background-color: #3b3b98;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 10px 10px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
  width: 120px; /* Increased width */
  display: flex;
  justify-content: center;
  align-items: center;
}

.material-edit-controls button:hover {
  background-color: darkorange;
  transform: translateY(-2px);
}

  .course-edit-container {
    background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  }
.edit-form-title {
  color: #ffffff;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 700; /* Make it bold */
  text-align: center; /* Center the text */
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 0.75rem;
  width: 100%; /* Ensure full width */
}
.form-group {
  margin-bottom: 1.5rem;
  width: 100%;
  max-width: 400px; /* Match buttons width */
  margin-left: auto;
  margin-right: auto;
}
.form-label {
  display: block;
  margin-bottom: 0.4rem;  
  font-weight: 200;       
  color: #fdfdfd;
  font-size: 0.85rem;  
  letter-spacing: 0.3px;
}
.form-input, 
.form-textarea {
  width: 100%;
  max-width: 400px; /* Added max-width to match buttons */
  padding: 0.75rem 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s, box-shadow 0.3s;
  display: block; /* Ensure they take full width */
  margin: 0 auto; /* Center the inputs */
}
.form-textarea {
  min-height: 120px;
  resize: vertical;
}
  .form-input:focus, .form-textarea:focus {
    outline: none;
    border-color: #3b3b98;
    box-shadow: 0 0 0 3px rgba(59, 59, 152, 0.1);
  }

  .form-textarea {
    min-height: 120px;
    resize: vertical;
  }
.form-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 1.5rem;
  width: 130%;
  max-width: 400px; /* Match input field width */
  margin-left: auto;
  margin-right: auto;
}
.save-button, .cancel-button {
  width: 110%; /* Ensure full width of container */
  padding: 12px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.save-button {
  background-color: #3b3b98;
  color: white;
}

.save-button:hover {
  background-color: darkorange;
  transform: translateY(-2px);
}

.cancel-button {
  background-color: rgb(169, 165, 165);
  color: #ffffff;
}
.cancel-button:hover {
  background-color: darkorange;
  transform: translateY(-2px);
}
.form-group .course-title,
.form-group .course-description,
.form-group .edit-form-title {
  font-weight: 700px bold !important;
}
.arrow {
  font-size: 1.5rem;
  transition: transform 0.3s ease;
  display: inline-block;
  transform-origin: center;
}

.arrow.rotate {
  transform: rotate(180deg);
}
  
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
