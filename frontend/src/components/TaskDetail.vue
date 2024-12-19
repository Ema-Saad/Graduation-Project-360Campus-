<template>
  <div class="task-detail">
    <!-- Top Image -->
    <div class="top-image">
      <img src="@/assets/pexels-pixabay.jpg" alt="Task Detail Image" />
    </div>

    <!-- Two Sections Below -->
    <div class="sections-container">
      <!-- Left Section -->
      <div class="left-section">
        <div class="sheet-card">
          <h3>Sheet 1</h3>
          <img src="@/assets/pexels-pixabay.jpg" alt="Sheet Image" @click="viewSheet" />
        </div>
      </div>

      <!-- Right Section -->
      <div class="right-section">
        <div class="deadline-section">
          <p class="due-date">Due Today, 11:59 pm</p>
          <span class="status assigned">Assigned</span>
          <div class="buttons">
            <button @click="uploadWork" class="upload-button">Upload your Work</button>
            <button @click="markAsDone" class="done-button">Mark As Done</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        task: {
          status: "Assigned",
        },
      };
    },
    methods: {
      uploadWork() {
        alert("Upload your work functionality not implemented yet.");
      },
      markAsDone() {
        this.task.status = "Done";
        alert("Task marked as done!");
      },
      viewSheet() {
        alert("Sheet clicked!");
      },
    },
  };
</script>

<style scoped>
  /* General Styling */
  .task-detail {
    font-family: Arial, sans-serif;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  /* Top Image */
  .top-image img {
    width: 100%;
    max-height: 300px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 20px;
  }

  /* Sections Container */
  .sections-container {
    display: flex;
    justify-content: space-between;
    width: 80%;
    margin-top: 20px;
    gap: 20px;
  }

  /* Left Section */
  .left-section {
    flex: 1;
  }

  .sheet-card {
    border: 1px solid #e0e0e0;
    padding: 15px;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
  }

    .sheet-card h3 {
      font-size: 16px;
      font-weight: bold;
      margin-bottom: 10px;
      color: #333;
    }

    .sheet-card img {
      width: 100%;
      height: 150px;
      object-fit: cover;
      cursor: pointer;
      border-radius: 5px;
      transition: transform 0.3s;
    }

      .sheet-card img:hover {
        transform: scale(1.05);
      }

  /* Right Section */
  .right-section {
    flex: 1;
    background-color: #fef4d1; /* Light yellow background */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
  }

  .deadline-section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .due-date {
    font-size: 18px;
    font-weight: bold;
    color: #444;
    margin-bottom: 10px;
  }

  .status {
    font-size: 14px;
    font-weight: bold;
    color: green;
    margin-bottom: 15px;
  }

  /* Buttons */
  .buttons {
    display: flex;
    gap: 15px;
  }

  .upload-button {
    background-color: #f68b1e; /* Orange color */
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 14px;
    transition: background-color 0.3s;
  }

    .upload-button:hover {
      background-color: #f57c00;
    }

  .done-button {
    background-color: #3b3b98; /* Blue color */
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 14px;
    transition: background-color 0.3s;
  }

    .done-button:hover {
      background-color: #2d2d70;
    }
</style>
