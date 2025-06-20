<template>
  <div class="app-container background-page">
    
    <header class="header">
      <!-- To Do Button that navigates to the To Do list -->
      <div v-if="$root.person_kind === 'S'" class="todo-button-container">
        <button class="todo-button" @click="goToToDoPage">
          To Do
          <span class="badge">{{ taskCount }}</span>
        </button>
      </div>
      <div v-else-if="$root.person_kind === 'P'">
      </div>

      <div v-if="$root.person_kind === 'S'" id="join-controls" class="join-controls-wrapper">
        <select id="course" v-model="enroll_in.course" @change="populateClassroomsForEnroll" class="join-select">
          <option value="0" disabled> Course </option>
          <option v-for="course in courses" :value="course.id">
            {{ course.title }}
          </option>
        </select>

        <select id="classroom" v-model="enroll_in.classroom" class="join-select">
          <option value="0" disabled> Instructor </option>
          <option v-for="classroom in classrooms_of_course" :value="classroom.id">
            {{ classroom.instructor.first_name }} {{ classroom.instructor.last_name }}
          </option>
        </select>

        <button class="join-button" @click="join">Join</button>
      </div>
    </header>

    <!-- The class cards or any other content here -->
  <div class="class-cards">
  <router-link
    v-for="classroom in registered_classes"
    :key="classroom.id"
    :to="{ name: 'ClassroomView', params: { courseId: classroom.course.id } }"
    class="class-card"
  >
    <div class="card-background">
      <div class="class-card-overlay">
        <h3>{{ classroom.course.title }}</h3>
        <p v-if="$root.person_kind === 'S'" class="author">
          👤 {{ classroom.instructor.first_name }} {{ classroom.instructor.last_name }}
        </p>
      </div>
    </div>
  </router-link>
</div>
  </div>
</template>

<script>
  import { useGlobalStore } from '@/global_store.js'

  export default {
    name: 'ClassroomList',
    data() {
      return {
        enroll_in: {
          course: 0,
          classroom: 0,
        },
        taskCount: 3,
        registered_classes: [],
        courses: [],
        classrooms_of_course: [],
      };
    },
    async beforeRouteEnter(to, from, next) {
      const store = useGlobalStore()

      let registered_classes = await store.request_api_endpoint('api/registered_classrooms');
      let registrable_classes = await store.request_api_endpoint('api/courses?list_registrable');

      next(vm => {
        vm.registered_classes = registered_classes
        vm.courses = registrable_classes.filter((d) =>
          registered_classes.find((e) => e.course.id === d.id) === undefined
        );
      });
    },
    methods: {
      populateClassroomsForEnroll() {
        let classrooms_promise = this.$root.request_api_endpoint(`api/course/${this.enroll_in.course}/classrooms`, 'get', null);
        classrooms_promise.then((data) => {
          this.classrooms_of_course = data;
        });
      },
      goToToDoPage() {
        this.$router.push({ name: 'ToDoPage' });
      },
      join() {
        let join_promise = this.$root.request_api_endpoint(
          `api/course/${this.enroll_in.course}/classroom/join`, 
          'post', 
          JSON.stringify({ 'classroom': this.enroll_in.classroom }),
          { 'Content-Type': 'application/json' },
        );

        join_promise.then((_) => 
          this.$root.request_api_endpoint(`api/course/${this.enroll_in.course}/classroom`, 'get', null)
        ).then((data) => {
          this.registered_classes = [...this.registered_classes, data];
          this.courses = this.courses.filter((c) => c.id === this.enroll_in.course);
          this.enroll_in = {
            course: 0,
            classroom: 0,
          };
        });
      }
    },
  };
</script>

<style scoped>
  .app-container {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    padding-top: 20px;
    height: 100vh;
  }
.background-page {
  position: relative;
  overflow: hidden;
}

.background-page::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/classroom.jpg');
  background-size: 65%;
  background-repeat: no-repeat;
  background-position: center top;
  filter: blur(4px) brightness(0.8); /* 🔹 blur + dim effect */
  z-index: 0;
}
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-width: 1000px;
    margin-bottom: 20px;
    border-bottom: 2px solid #f68b1e;
    padding-bottom: 10px;
    z-index: 10;
  }

  .todo-button-container {
    position: relative;
    display: inline-block;
  }

  .todo-button,
  .join-button {
    background-color: #3b3b98;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 14px;
    cursor: pointer;
    position: relative;
  }

  .todo-button:hover,
  .join-button:hover {
    background-color: darkorange;
  }

  .badge {
    background-color: #f68b1e;
    color: white;
    border-radius: 50%;
    padding: 3px 8px;
    font-size: 12px;
    position: absolute;
    top: -5px;
    right: -5px;
  }

  .join-controls-wrapper {
    display: flex;
    gap: 10px;
    align-items: center;
  }

  .join-select {
    background-color: #3b3b98;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 14px;
    cursor: pointer;
    appearance: none;
  }

  .join-select:hover {
    background-color: darkorange;
  }

  .join-select option {
    color: black;
  }

.class-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  width: 90%;
  max-width: 1200px;
  margin-top: 20px;
  padding-bottom: 20px;
  margin-left: 20%; 
}

.class-card {
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  padding: 0;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-color: transparent;
}

.card-background {
  width: 100%;
  height: 180px;
  background-image: url('@/assets/pexels-photo.png');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.class-card-overlay {
  color: white;
  padding: 15px;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.class-card h3 {
  margin: 0;
  font-size: 18px;
}

.author {
  font-size: 14px;
  margin-top: 8px;
  color: #f0f0f0;
}

  .class-card:hover {
    border: 1px solid #007bff;
  }

  .class-image {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 5px;
  }

  .class-image-container {
    position: relative;
  }

  .class-card-overlay {
    position: absolute;
    top: 50%;
    left: 40%;
    transform: translate(-50%, -50%);
    color: black;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    width: 80%;
    font-size: 14px;
  }

  @media (max-width: 768px) {
    .app-container {
      flex-direction: column;
      height: auto;
    }

    .background-container {
      padding-top: 10px;
    }

    .header {
      flex-direction: column;
      align-items: flex-start;
      margin-bottom: 15px;
    }

    .todo-button-container {
      margin-top: 10px;
      display: flex;
      flex-direction: column;
      width: 100%;
    }

    .todo-button, .join-button {
      font-size: 14px;
      padding: 12px 20px;
      width: 100%;
      text-align: center;
      border-radius: 5px;
      cursor: pointer;
      background-color: #3b3b98;
      color: white;
      border: none;
      margin-bottom: 15px;
    }

    .todo-button:hover, .join-button:hover {
      background-color: darkorange;
    }

    .badge {
      font-size: 10px;
      padding: 2px 6px;
    }

    .class-cards {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 15px;
      width: 90%;
      max-width: 100%;
      margin-top: 20px;
      padding-bottom: 20px;
      margin-bottom: 100px;
    }

    .class-card {
      padding: 12px;
      font-size: 14px;
    }

    .class-image {
      height: 100px;
    }

    .join-controls-wrapper {
      flex-direction: column;
      align-items: stretch;
      width: 100%;
      margin-top: 10px;
    }

    .join-select {
      width: 100%;
    }
  }
</style>
