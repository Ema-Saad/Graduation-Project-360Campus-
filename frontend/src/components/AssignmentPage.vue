<template>
  <div class="assignment-container">
    <h1>Assignment for Course {{ courseId }} - Week {{ weekId }}</h1>
    <button class="download-button" @click="downloadContent">Download Assignment PDF</button>
    <p v-if="assignmentContent">{{ assignmentContent }}</p> <!-- Display the dynamic content -->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        courseId: this.$route.params.courseId, // Get the courseId from the route
        weekId: this.$route.params.weekId,     // Get the weekId from the route
        assignmentContent: null,               // Placeholder for assignment content
      };
    },
    created() {
      this.fetchAssignmentContent(); // Fetch content when component is created
    },
    methods: {
      fetchAssignmentContent() {
        // Here you would fetch the assignment content based on courseId and weekId.
        // For this example, I'm just setting a static message.
        // You can replace this with an API call to fetch actual content.

        this.assignmentContent = `This is the content for the Assignment of Course ${this.courseId} - Week ${this.weekId}`;
      },
      downloadContent() {
        const link = document.createElement('a');
        link.href = `/path/to/your/assignment-${this.courseId}-week${this.weekId}.pdf`; // Dynamically generate the PDF path
        link.download = `Assignment-Course${this.courseId}-Week${this.weekId}.pdf`;
        link.click();
      },
    },
  };
</script>

<style scoped>
  .assignment-container {
    position: relative; /* Make the container relative for absolute positioning of the button */
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
