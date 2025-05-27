<template>

  <AssignmentCreate
    :course_id="course_id"
    v-if="showAssignmentCreateDialog"
    @close="showAssignmentCreate = false"
  />

  <div v-if="classroom" class="page">
    <!-- Top Banner -->
    <div class="top-banner">
      <div class="banner-text">
        <h1 class="course-name">{{ classroom.course.title }}</h1>
        <span class="course-code">Taught by {{ classroom.instructor.first_name }} {{ classroom.instructor.last_name }}</span>
      </div>
      <img :src="bannerImage" alt="Course Banner" class="banner-image" />
      <div v-if="$root.person_kind === 'P'">
        <button @click="showAssignmentCreateDialog = true"> 
          Add new assignment 
        </button>
        <button> Add new meeting </button>
        <button> Add new quiz </button>
      </div>
    </div>

    <!-- Homework Section -->
    <div class="homework-section">
      <div class="section-header">
        <div class="badge">{{ tasks.length }}</div> <!-- Bind the badge count here -->
        <h2 class="section-title">Required Homework</h2>
        <button class="todo-button">
          <router-link :to="{ name: 'CourseDetails', params: { id: this.course_id } }">
            Materials
          </router-link>
        </button>
      </div>

      <div id="task-list">
          <div class="task-item" v-for="task in tasks">
            <div class="task-icon">
              <span class="fas fa-file-alt"></span>
            </div>
              
            <router-link class="task" :to="{ name: 'taskDetail', params: { taskId: task.id } }">
              <span class="task-name"> {{ task.title }} </span>
            </router-link>

            <div class="due"> {{ computeTimeString(task) }} </div>
          </div>
      </div>
    </div>
  </div>
</template>


<script>
  import bannerImage from "@/assets/pexels-photo.png";
  import week1Image from "@/assets/pexels-photo.png";
  import week2Image from "@/assets/pexels-photo.png";
  import week3Image from "@/assets/pexels-photo.png";
  import week4Image from "@/assets/pexels-photo.png";

  import AssignmentCreate from "./AssignmentCreate.vue";
  export default {
    data() {
      return {
        bannerImage,
        tasks: [],
        classroom: null,
        homeworkCount: 2, // Dynamic count for homework (this can be changed based on real data)
        showAssignmentCreateDialog: false,
      };
    },
    components: {
      AssignmentCreate,
    },
    props: ['course_id'],
    beforeMount() {
      let classroom_promise = this.$root.request_api_endpoint(`api/course/${this.course_id}/classroom`, 'get', null);
      let tasks_promise = this.$root.request_api_endpoint(`api/course/${this.course_id}/classroom/tasks`, 'get', null);

      classroom_promise.then((data) => {
        this.classroom = data;
      });

      tasks_promise.then((data) => {
        this.tasks = data.map((d) => ({ ...d, time: d.time ? new Date(d.time) : null }));
      });
    },
    methods: {
      computeTimeString(task) {
        
        let date = task.time;

        const MILLISECONDS_IN_DAY = 24 * 60 * 60 * 1000;
        const DAYS = [
          "Sunday", "Monday", "Tuesday", 
          "Wednesday", "Thursday", "Friday", "Saturday"
        ];
        const MONTHS = [
          "Jan", "Feb", "Mar", "Apr",
          "May", "Jun", "Jul", "Aug",
          "Sep", "Oct", "Nov", "Dec",
        ];

        let hour = `${date.getHours().toString().padStart(2, "0")}:${date.getMinutes().toString().padStart(2, "0")}`;
        if (Date.now() > date) {
          return "Missed";

        } else if (date - Date.now() <= MILLISECONDS_IN_DAY) {
          return `Due Today at ${hour}`;

        } else if (date - Date.now() <= 2 * MILLISECONDS_IN_DAY) {
          return `Due Tomorrow at ${hour}`;

        } else if (date - Date.now() <= 7 * MILLISECONDS_IN_DAY) {
          return `Due ${DAYS[date.getDay()]} at ${hour}`;
        } else {
          return `Due ${MONTHS[date.getMonth()]}. ${date.getDate().toString().padStart(2, "0")} at ${hour}`;
        }

      }

    }
  };

</script>


<style scoped>
  /* General Page Styles */
  .page {
    padding: 0;
    margin: 0 auto;
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    max-width: 1300px; /* Adjusted the width */
    border: 1px solid #ddd; /* Optional: Adds a border around the page for emphasis */
  }

  /* Top Banner */
  .top-banner {
    position: relative;
    width: 100%;
    text-align: center;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .banner-image {
    width: 100%;
    height: 270px;
    max-width: 100%;
    display: block;
    margin: 0 auto;
    border-bottom: 2px solid #ddd;
    max-height: 500px;
  }

  /* Banner Text */
  .banner-text {
    position: absolute;
    top: 30%; /* Vertically center */
    left: 10%; /* Horizontally center */
    color: black;
    font-family: Arial, sans-serif;
  }

  .course-code {
    font-size: 1.2em;
    font-weight: bold;
  }

  .course-name {
    font-size: 2.5em;
    font-weight: bold;
    margin-top: 5px;
  }


  /* Homework Section */
  .homework-section {
    padding: 20px;
    margin: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .section-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }

  .badge {
    background-color: orange;
    color: white;
    font-size: 1.5em;
    font-weight: bold;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .section-title {
    font-size: 1.8em;
    flex-grow: 1;
    margin-left: 10px;
  }

  .todo-button {
    padding: 10px 20px;
    background-color: navy;
    color: white;
    font-size: 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .todo-button > a {
    text-decoration: none;
    color: white;
  }

    .todo-button:hover {
      background-color: darkorange;
    }

  .task-list {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .task-item {
    align-items: center;
    justify-content: left;
    display: flex;
    flex-direction: row;
  }


  .task-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #1a237e;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 10px;
  }

  .task-icon span {
    font-size: 1.5em;
  }

  .task-name {
    text-weight: bold;
  }

  .due {
    flex: 1;
    text-align: right;
    color: gray;
  }

  @media (max-width: 1200px) {
    .banner-text {
      left: 5%;
      top: 20%;
    }

    .course-name {
      font-size: 2em;
    }

    .todo-button {
      font-size: 0.9em;
    }

  }

  /* For medium screens (up to 768px wide) */
  @media (max-width: 768px) {
    .top-banner {
      text-align: left;
    }

    .banner-text {
      left: 0;
      top: 10%;
      width: 100%;
    }

    .course-code {
      font-size: 1em;
    }

    .course-name {
      font-size: 1.8em;
    }
  }

  /* For small screens (up to 480px wide) */
  @media (max-width: 480px) {
    .top-banner {
      text-align: left;
    }

    .banner-text {
      left: 0;
      top: 15%;
    }

    .course-name {
      font-size: 1.5em;
    }

  }

</style>
