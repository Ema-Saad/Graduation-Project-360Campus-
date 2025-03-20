<template>
  <div class="app-container">
    <div :class="['background-container', { 'blur-background': showModal }]">

      <header class="header">
        <!-- To Do Button that navigates to the To Do list -->
        <div class="todo-button-container">
          <button class="todo-button" @click="goToToDoPage">
            To Do
            <span class="badge">{{ taskCount }}</span>
          </button>
        </div>

        <button class="join-button" @click="showModal = true">Join</button>
      </header>

      <!-- The class cards or any other content here -->
      <div class="class-cards">
        <button v-for="klass in registered_classes"
                :key="klass.id"
                @click="goToCourseDetail(klass.id)"
                class="class-card">

          <h3>{{ klass.course.title }}</h3>
          <p class="author">👤 {{ klass.instructor.first_name }} {{ klass.instructor.last_name }}</p>
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
  import class1Image from '@/assets/pexels-photo.png';
  import class2Image from '@/assets/pexels-photo.png';
  import class3Image from '@/assets/pexels-photo.png';

  export default {
    name: 'MyCourses',
    data() {
      return {
        showModal: false,
        taskCount: 3,
        registered_classes: [],
      };
    },
    beforeMount() {
      let classes = this.$root.request_api_endpoint('api/registered_classrooms', 'get', null);

      classes.then((data) => {
        this.registered_classes = data;
      });

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

  .todo-button-container {
    position: relative; /* To position the badge relative to the button */
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
    position: relative; /* To allow absolute positioning of the badge */
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
    top: -5px; /* Move the badge a little above */
    right: -5px; /* Position it on the top-right corner */
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
    border: 1px solid #ccc;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    background-color: #fff;
    cursor: pointer;
    position: relative; /* Allow positioning of the overlay */
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

    .class-card:hover {
      border: 1px solid #007bff;
    }

  /* Class image styling */
  .class-image {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 5px;
  }

  /* Author text styling */
  .author {
    margin-top: 10px;
    font-size: 12px;
    color: #555;
  }

  /* Class card image container */
  .class-image-container {
    position: relative;
  }

  /* Class card overlay styling */
  .class-card-overlay {
    position: absolute;
    top: 50%;
    left: 40%;
    transform: translate(-50%, -50%); /* Center the overlay */
    color: black; /* Ensure the text is visible on darker images */
    padding: 10px;
    border-radius: 5px;
    text-align: center; /* Center the text inside the overlay */
    width: 80%; /* Adjust width */
    font-size: 14px;
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

  /* Media query for screens below 768px */
  @media (max-width: 768px) {
    /* Adjust the layout of the app container for mobile */
    .app-container {
      flex-direction: column;
      height: auto;
    }

    /* Adjust the background container to fit mobile view */
    .background-container {
      padding-top: 10px;
    }

    /* Header adjustments */
    .header {
      flex-direction: column;
      align-items: flex-start;
      margin-bottom: 15px;
    }

    .todo-button-container {
      margin-top: 10px;
      display: flex;
      flex-direction: column; /* Stack the buttons vertically */
      width: 100%; /* Ensure container takes full width */
    }

    /* Button adjustments */
    .todo-button, .join-button {
      font-size: 14px;
      padding: 12px 20px;
      width: 100%; /* Ensure buttons are full width */
      text-align: center; /* Center text inside buttons */
      border-radius: 5px;
      cursor: pointer;
      background-color: #3b3b98; /* Default color */
      color: white; /* Text color */
      border: none;
      margin-bottom: 15px; /* Add margin-bottom to create space between buttons */
    }

      .todo-button:hover, .join-button:hover {
        background-color: darkorange;
      }

    /* Badge adjustments */
    .badge {
      font-size: 10px;
      padding: 2px 6px;
    }

    /* Class Cards adjustments */
    .class-cards {
      display: grid;
      grid-template-columns: repeat(2, 1fr); /* 2 columns for smaller screens */
      gap: 15px;
      width: 90%;
      max-width: 100%;
      margin-top: 20px;
      padding-bottom: 20px;
      margin-bottom: 100px; /* Push the cards above the footer */
    }

    /* Class card adjustments */
    .class-card {
      padding: 12px;
      font-size: 14px;
    }

    .class-image {
      height: 100px;
    }

    /* Adjust the modal for mobile */
    .modal-container {
      padding: 10px;
    }

    .modal {
      width: 90%;
      padding: 15px;
    }

    .input-box {
      width: 100%;
      font-size: 12px;
    }

    .modal-button {
      padding: 8px 16px;
    }
  }

</style>
