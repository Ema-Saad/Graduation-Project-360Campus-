<template>
  <div class="popup-overlay">
    <div class="popup-content">
      <button @click="$emit('closed')" class="close-btn">×</button>
      <h2>Upload New Project</h2>
      <input type="text" placeholder="Enter the title of project" class="input-field" />

      <div class="upload-container" @click="triggerFileUpload">
        <!-- Hidden file input -->
        <input type="file"
               ref="fileInput"
               @change="handleFileUpload"
               style="display: none" />

        <!-- Display Selected File Name or Placeholder -->
        <span class="file-name">
          {{ selectedFile ? selectedFile.name : "Upload File" }}
        </span>

        <!-- Upload Button -->
        <button class="upload-btn">
          Upload
        </button>
      </div>
      <button class="submit-btn" @click="uploadProject">Upload new Project</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'GraduationProjectCreate',
    emits: ['closed'],
    data() {

    },
    methods: {
    }
  }

</script>

<style scoped>
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: none; /* Removes the gray background */
  }

  .popup-content {
    background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
    padding: 7px; /* ;Increased padding for more space */
    border-radius: 10px;
    width: 480px; /* Increase width */
    max-width: 60%; /* Ensure it doesn't exceed screen width */
    height: 400px; /* Increase height */
    max-height: 90%; /* Ensure it doesn't exceed screen height */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative; /* Ensure positioning works */
    top: 90px; /* Move the popup down */
  }

  .close-btn {
    position: absolute;
    top: 10px;
    right: 15px;
    font-size: 40px;
    background: none;
    border: none;
    cursor: pointer;
  }

  .input-field,
  .upload-container {
    width: 90%;
    height: 45px;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
    border: 1px solid #ccc;
    display: flex;
    align-items: center;
  }

  .input-field {
    width: 90%;
    height: 25px;
  }

  .upload-container {
    background: white;
    justify-content: space-between;
    padding: 0 10px;
    position: relative;
  }

  .upload-label {
    flex-grow: 1;
    display: flex;
    align-items: center;
    overflow: hidden;
  }

  .file-name {
    flex-grow: 1;
    margin-left: 0px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: calc(100% - 90px); /* Adjusts width dynamically */
    color: #666; /* Match the input text color (dark gray) */
    opacity: 1; /* Ensure it's fully visible */
  }

  .upload-btn {
    background: #201887;
    color: white;
    border: none;
    padding: 5px 8px;
    border-radius: 5px;
    height: 80%;
    width: 75px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    flex-shrink: 0; /* Prevents button from shrinking */
  }

    .upload-btn:hover {
      background: darkorange;
    }

  .submit-btn {
    background: #201887;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    margin-top: 50px; /* Increase margin to shift it down */
    width: 35%;
    cursor: pointer;
  }

    .submit-btn:hover {
      background: darkorange;
    }

  .popup-content h2 {
    color: white; /* Ensure h2 is white */
    margin-top: -10px; /* Moves it up */
    padding-bottom: 25px; /* Adds spacing below */
    text-align: center; /* Keep it centered */
  }


</style>

