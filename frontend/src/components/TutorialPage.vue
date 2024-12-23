<template>
  <div class="tutorial-container">
    <h1>Tutorial for Course {{ courseId }} - Week {{ weekId }}</h1>
    <button class="download-button" @click="downloadContent">Download Tutorial PDF</button>
    <p v-if="tutorialContent">{{ tutorialContent }}</p> <!-- Display dynamic tutorial content -->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        courseId: this.$route.params.courseId,  // Get courseId from the route parameters
        weekId: this.$route.params.weekId,      // Get weekId from the route parameters
        tutorialContent: null,                  // Placeholder for dynamic tutorial content
      };
    },
    created() {
      this.fetchTutorialContent();  // Fetch content when component is created
    },
    methods: {
      fetchTutorialContent() {
        // Replace this with an API call to fetch tutorial content based on courseId and weekId.
        this.tutorialContent = `This is the content for the Tutorial of Course ${this.courseId} - Week ${this.weekId}`;
      },
      downloadContent() {
        const link = document.createElement('a');
        link.href = `/path/to/your/tutorial-${this.courseId}-week${this.weekId}.pdf`;  // Dynamically generate the PDF path
        link.download = `Tutorial-Course${this.courseId}-Week${this.weekId}.pdf`;
        link.click();
      },
    },
  };
</script>

<style scoped>
  .tutorial-container {
    position: relative; /* Relative positioning to position the button absolutely */
  }

  .download-button {
    position: absolute; /* Position the button absolutely */
    top: 10px; /* Distance from the top */
    right: 10px; /* Distance from the right */
    background-color: #1e0a74; /* Blue background */
    color: white; /* White text */
    padding: 10px 15px; /* Padding for the button */
    border: none; /* Remove border */
    border-radius: 4px; /* Rounded corners */
    cursor: pointer; /* Pointer cursor for button */
    transition: background-color 0.3s; /* Smooth background color change */
  }

    .download-button:hover {
      background-color: #0056b3; /* Darker blue on hover */
    }
</style>
