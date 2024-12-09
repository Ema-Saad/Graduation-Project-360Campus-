<template>
  <div>
    <!-- Background container -->
    <div :class="['background-container', { 'blur-background': showModal }]">
      <!-- Button to trigger the modal -->
      <button class="center-button" @click="showModal = true">Join a class</button>
    </div>

    <!-- Popup Modal -->
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
  export default {
    name: "App",
    data() {
      return {
        showModal: false, // State to control modal visibility
      };
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
    background-color: blue;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

    .center-button:hover {
      background-color: #0056b3;
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
  .modal {
    background: linear-gradient(to bottom, #3b3b98, #f9c74f);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    width: 300px;
    position: relative;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }

  /* Close button styling */
  .close-button {
    position: absolute;
    top: 10px;
    right: 15px;
    background: transparent;
    border: none;
    font-size: 18px;
    cursor: pointer;
  }

  /* Input box styling */
  .input-box {
    width: 90%; /* Adjusted to make it responsive within the modal */
    max-width: 250px; /* Ensures it doesn’t get too wide */
    padding: 10px;
    margin: 15px 0; /* Adds space above and below */
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 14px;
    text-align: center; /* Centers placeholder text */
  }

  /* Modal button styling */
  .modal-button {
    padding: 10px 20px;
    background-color: #003399;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

    .modal-button:hover {
      background-color: #002266;
    }
</style>
