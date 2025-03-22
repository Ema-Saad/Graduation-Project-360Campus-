<template>
  <div v-if="course">

    <h1 id="course-title">{{ course.title }}</h1>
    <p id="course-description">{{ course.description }}</p>

    <div class="weeks-container">
      <div class="week-box" v-for="week in weeks" :key="week.id" @click="toggleDropdown(week.id)">
        <span class="week-title">Week {{ week.id }} </span>
        <span class="arrow" :class="{ 'rotate': isDropdownOpen(week.id) }">&#9660;</span>

        <div v-if="isDropdownOpen(week.id)" class="dropdown-menu">
          <button v-for="lab in week.labs" class="dropdown-item" @click="download(lab.id)">
            Lab: {{ lab.name }} 
          </button>

          <button v-for="lecture in week.lectures" class="dropdown-item" @click="download(lecture.id)"> 
            Lecture: {{ lecture.name }}
          </button>

          <button v-for="tutorial in week.tutorials" class="dropdown-item" @click="download(tutorial.id)"> 
            Tutorial: {{ tutorial.name }} 
          </button>

          <button v-for="assignment in week.assignments" class="dropdown-item" @click="download(assignment.id)"> 
            Assignment: {{ assignment.name }} 
          </button>

          <button v-for="problem_sheet in week.problem_sheets" class="dropdown-item" @click="download(problem_sheet.id)"> 
            Problem Sheet: {{ problem_sheet.name }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  /* Materials Type */
  const LAB = 'l';
  const LECTURE = 'L';
  const TUTORIAL = 't';
  const ASSIGNMENT = 'a';
  const PROBLEM_SHEET = 's';
  const OTHER = 'o';

  export default {
    props: ['id'],
    data() {
      return {
        course: null,
        weeks: [],
        openDropdowns: [], // Store open dropdown states
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
            labs: data.filter((d) => d.week === i && d.material_type === LAB),
            lectures: data.filter((d) => d.week === i && d.material_type === LECTURE),
            tutorials: data.filter((d) => d.week === i && d.material_type === TUTORIAL),
            assignments: data.filter((d) => d.week === i && d.material_type === ASSIGNMENT),
            problem_sheets: data.filter((d) => d.week === i && d.material_type === PROBLEM_SHEET),
          };
        }

        this.weeks = this.weeks.filter((d) => d.labs.length + 
                                              d.lectures.length + 
                                              d.tutorials.length + 
                                              d.assignments.length + 
                                              d.problem_sheets.length > 0);
      });
    },
    methods: {
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
  .week-box {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 3em;
    padding-top: 0.5em;
    position: relative;
  }

    .week-box:hover {
      border: 1px solid #007bff;
    }

  .weeks-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    padding: 20px;

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
    flex-direction: row;
    flex-wrap: wrap;
  }

  .dropdown-item {
    color: black;
    padding: 1vh;
    margin: 3vh;
  }

  .dropdown-item:hover {
    color: #007bff; /* Optional: Change color to blue when hovered */
  }

  #course-title {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

</style>
