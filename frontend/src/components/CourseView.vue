<template>
  <MaterialCreate
    v-if="showMaterialCreateDialog" 
    :course_id="course.id"
    :instance="toBeEditedMaterial"
    @close="showMaterialCreateDialog = false; toBeEditedMaterial = null"
  />

  <div v-if="course">

    <div v-if="!showCourseEditingWidgets">
      <h1 id="course-title">{{ course.title }}</h1>
      <p id="course-description">{{ course.description }}</p>
    </div>
    <div v-else-if="showCourseEditingWidgets && $root.person_kind === 'P'">
      <input v-model="course.title" type="text" placeholder="Title" value="{{ course.title }}" size="50" />
      <br />
      <textarea v-model="course.description" cols="120" rows="10">
        {{ course.description }}
      </textarea>
      <br />
      <button @click="editCourse"> Save </button>
      <button @click="course = copy_of_course; showCourseEditingWidgets = false">
        Cancel
      </button>
    </div>

    <span id="course-edit-controls" v-if="$root.person_kind === 'P' && !showCourseEditingWidgets">
      <button @click="showMaterialCreateDialog = true"> Add New Material </button>
      <button @click="copy_of_course = {...course}; showCourseEditingWidgets = true"> 
        Edit Course Information 
      </button>
      <button @click="deleteCourse"> Delete Course </button>
    </span>

    <div class="weeks-container">
      <div class="week-box" v-for="week in weeks" :key="week.id" @click="toggleDropdown(week.id)">
        <span class="week-title">Week {{ week.id }} </span>
        <span class="arrow" :class="{ 'rotate': isDropdownOpen(week.id) }">&#9660;</span>

        <template v-for="materialTypeArray in week" v-if="isDropdownOpen(week.id)" class="dropdown-menu">
          <div v-if="materialTypeArray.length > 0"> 
            <h3> {{ stringifyMaterialType(materialTypeArray[0].kind) }} </h3>
            <ul>
              <li v-for="materialInstance in materialTypeArray">
                <a class="dropdown-item" @click="download(materialInstance.id)"> 
                  {{ materialInstance.name }} 
                </a>

                <span class="material-edit-controls" v-if="$root.person_kind === 'P'">
                  <button @click="toBeEditedMaterial = materialInstance; showMaterialCreateDialog = true">
                    Edit
                  </button>

                  <button @click="deleteMaterial(materialInstance)">
                    Delete
                  </button>
                </span>
              </li>
            </ul>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>

  import MaterialCreate from './MaterialCreate.vue';

  /* Materials Type */
  const LAB = 'l';
  const LECTURE = 'L';
  const TUTORIAL = 't';
  const ASSIGNMENT = 'a';
  const PROBLEM_SHEET = 's';
  const OTHER = 'o';

  export default {
    props: ['id'],
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
      };
    },
    beforeMount() {
      let course_promise = this.$root.request_api_endpoint(`api/course/${this.id}`, 'get', null);
      let materials_promise = this.$root.request_api_endpoint(`api/course/${this.id}/materials`, 'get', null);

      course_promise.then((data) => {
        this.course = data;
      });

      materials_promise.then((data) => {
        let max_weeks = data.map((d) => d.week || -1).reduce((a, v) => Math.max(a, v));
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
      });
    },
    methods: {
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
