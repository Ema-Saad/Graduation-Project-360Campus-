<template>
  <div>
    <!-- Background container -->
    <div :class="['background-container', { 'blur-background': showModal }]">
      <!-- Button to trigger the modal -->
      <button class="center-button" @click="showModal = true">Create a class</button>
    </div>

    <!-- Popup Modal -->
    <div v-if="showModal" class="modal-container">
      <div class="modal">
        <button class="close-button" @click="closeModal">×</button>
        <h2>Create New Class</h2>
        <input v-model="subject" type="text" placeholder="Enter the subject..." class="input-box" />
        <input v-model="classCode" type="text" placeholder="Enter the class code..." class="input-box" />
        <button class="modal-button" @click="createClass">Create</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "App",
    data() {
      return {
        showModal: false, // State to control modal visibility
        subject: "", // Store input value for subject
        classCode: "", // Store input value for class code
      };
    },
    methods: {
      createClass() {
        if (this.subject.trim() === "" || this.classCode.trim() === "") {
          alert("Please enter both subject and class code!");
          return;
        }
        console.log("Class Created:", {
          subject: this.subject,
          classCode: this.classCode,
        });
        this.closeModal();
      },
      closeModal() {
        this.showModal = false;
        this.subject = ""; // Reset input field
        this.classCode = ""; // Reset input field
      },
    },
  };
</script>


<style scoped>
  /* Background container styling */
  .background-container {
    background-image: url('../src/assets/classroom.jpg');
    background-size: 900px;
    background-position: center;
    background-repeat: no-repeat;
    height: 90vh;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    transition: filter 0.3s ease; /* Smooth transition for blur */
  }

  /* Apply blur effect when modal is visible */
  .blur-background {
    filter: blur(5px); /* Blurs the background */
  }

  /* Center button styling */
  .center-button {
    margin-bottom: 20px;
    padding: 10px 20px;
    font-size: 16px;
    background-color: #201887;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

    .center-button:hover {
      background-color: darkorange;
    }

  /* Modal container styling */
  .modal-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  /* Modal box styling */
  /* Modal box styling */
  .modal {
    background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
    border-radius: 10px;
    width: 450px; /* Increase width */
    max-width: 60%; /* Ensure it doesn't exceed screen width */
    height: 400px; /* Increase height */
    max-height: 90%; /* Ensure it doesn't exceed screen height */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative; /* Ensure positioning works */
  }

  /* Close button styling */
  .close-button {
    position: absolute;
    top: 10px;
    right: 15px;
    background: transparent;
    border: none;
    font-size: 35px;
    cursor: pointer;
  }

  /* Input box styling */
  .input-box {
    width: 100%; /* Make it take full width inside the modal */
    max-width: 350px; /* Increased width */
    padding: 12px; /* Slightly larger padding for better appearance */
    margin: 15px 0; /* Adds space above and below */
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px; /* Slightly larger text */
    text-align: center; /* Centers placeholder text */
  }

  .modal h2 {
    color: white;
  }

  /* Modal button styling */
  .modal-button {
    padding: 10px 25px;
    background-color: #201887;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

    .modal-button:hover {
      background-color: darkorange;
    }

  /* Mobile responsiveness */
  @media (max-width: 768px) {
    .background-container {
      background-size: cover; /* Ensure background image scales well */
      height: 56vh; /* Adjust height for smaller screens */
    }

    .center-button {
      font-size: 14px;
      padding: 8px 16px;
      margin-bottom: -1%;
    }

    .modal-container {
      align-items: flex-start; /* Position modal better on small screens */
      padding-top: 10vh;
    }

    .modal {
      width: 80%;
      height: auto; /* Allow modal to adjust based on content */
      padding: 20px;
    }

    .close-button {
      font-size: 30px; /* Reduce close button size */
      top: 5px;
      right: 10px;
    }

    .input-box {
      width: 85%;
      max-width: 300px; /* Slightly reduce max width */
      font-size: 15px; /* Adjust font size */
    }

    .modal-button {
      padding: 12px 22px;
      font-size: 15px; /* Slightly reduce button size */
    }
  }

  @media (max-width: 480px) {
    .background-container {
      background-size: cover; /* Ensure background image scales even better on very small screens */
      height: 45vh; /* Further adjust the height for smaller screens */
      padding-bottom: 50px; /* Add more space for very small screens */
    }

    .center-button {
      font-size: 14px;
      padding: 6px 12px;
      margin-bottom: -1%;
    }

    .modal-container {
      align-items: flex-start; /* Ensure modal aligns properly */
      padding-top: 5vh;
    }

    .modal {
      width: 90%;
      height: auto; /* Allow modal to expand as needed */
      padding: 15px;
    }

    .close-button {
      font-size: 28px; /* Reduce size for better fit */
      top: 5px;
      right: 8px;
    }

    .input-box {
      width: 90%; /* Make input fields more usable */
      max-width: 320px;
      font-size: 14px;
    }

    .modal-button {
      padding: 10px 20px;
      font-size: 14px; /* Slightly reduce button size */
    }
  }

</style>
