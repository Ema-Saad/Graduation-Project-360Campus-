<template>
  <div class="app-container">
    <div :class="['background-container', { 'blur-background': showModal }]">

      <header class="header">
        <!-- To Do Button that navigates to the To Do list -->
        <button class="todo-button" @click="goToToDoPage">
          To Do <span class="badge">2</span>
        </button>
        <button class="join-button" @click="showModal = true">Join</button>
      </header>

      <!-- The class cards or any other content here -->
      <div class="class-cards">
        <button v-for="(classItem, index) in classes"
                :key="classItem.id"
                @click="goToCourseDetail(classItem.id)"
                class="class-card">
          <img :src="classItem.image" alt="Class Image" class="class-image" />
          <h3>{{ classItem.title }}</h3>
          <p>{{ classItem.subtitle }}</p>
          <p class="author">👤 {{ classItem.author }}</p>
        </button>
      </div>
    </div>

    <!-- Modal Popup for joining a class -->
    <div v-if="showModal" class="modal-container">
      <div class="modal">
        <button class="close-button" @click="showModal = false">×</button>
        <h2>Ask your doctor for the class code,</h2>
        <p>then enter it here</p>
        <input type="text" placeholder="Enter the class code..." class="input-box" />
        <button class="modal-button">Joining</button>
      </div>
    </div>
  </div>
</template>

<script>
  import class1Image from '@/assets/classroom.jpg';
  import class2Image from '@/assets/classroom.jpg';
  import class3Image from '@/assets/classroom.jpg';

  export default {
    name: 'MyCourses',
    data() {
      return {
        showModal: false,
        classes: [
          {
            id: 'csc410',
            image: class1Image,
            title: 'CSC 410',
            subtitle: 'Software Quality',
            author: 'Dr. Mohamed',
          },
          {
            id: 'csc411',
            image: class2Image,
            title: 'CSC 411',
            subtitle: 'Database Systems',
            author: 'Dr. Sarah',
          },
          {
            id: 'csc420',
            image: class3Image,
            title: 'CSC 420',
            subtitle: 'Web Development',
            author: 'Dr. John',
          },
        ],
      };
    },
    methods: {
      // Method to navigate to the To-Do page
      goToToDoPage() {
        this.$router.push({ name: 'ToDoPage' }); // 'ToDoPage' should be the name of the route for the to-do list
      },
      goToCourseDetail(courseId) {
        this.$router.push({ name: 'MyCourseDetail', params: { id: courseId } });
      },
    },
  };
</script>



<style scoped>
  /* Main container for the app */
  .app-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }

  /* Background container with optional blur effect */
  .background-container {
    flex-grow: 1;
    background-color: #f8f8f8;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    padding-top: 20px;
    transition: filter 0.3s ease;
  }

  .blur-background {
    filter: blur(5px); /* Applies blur when modal is visible */
  }

  /* Header section styling */
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

  .todo-button,
  .join-button {
    background-color: #3b3b98;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 14px;
    cursor: pointer;
  }

    .todo-button:hover,
    .join-button:hover {
      background-color: #2a2973;
    }

  .badge {
    background-color: #f68b1e;
    color: white;
    border-radius: 50%;
    padding: 3px 8px;
    font-size: 12px;
    margin-left: 5px;
  }

  /* Class Cards Section - Styling */
  .class-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 columns layout */
    gap: 20px;
    width: 90%;
    max-width: 1200px;
    margin-top: 20px;
    padding-bottom: 20px;
  }

  /* Class card styling */
  .class-card {
    display: block;
    width: 100%;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    background-color: #fff;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

    .class-card:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
    }

  .class-image {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 5px;
  }

  .author {
    margin-top: 10px;
    font-size: 12px;
    color: #555;
  }

  /* Modal container styling */
  .modal-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  /* Modal box styling */
  .modal {
    background: linear-gradient(to bottom, #3b3b98, #f9c74f);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    width: 300px;
    position: relative;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }

  .close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: transparent;
    border: none;
    font-size: 18px;
    cursor: pointer;
  }

  /* Input box styling */
  .input-box {
    width: 90%;
    padding: 10px;
    margin: 15px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 14px;
  }

  .modal-button {
    padding: 10px 20px;
    background-color: #3b3b98;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

    .modal-button:hover {
      background-color: #2a2973;
    }
</style>
