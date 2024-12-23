<template>
  <div class="lecture-container">
    <h1>Lecture for Course {{ courseId }} - Week {{ weekId }}</h1>
    <button class="download-button" @click="downloadContent">Download Lecture PDF</button>
    <p v-if="lectureContent">{{ lectureContent }}</p> <!-- Display the dynamic content -->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        courseId: this.$route.params.courseId, // Get the courseId from the route
        weekId: this.$route.params.weekId,     // Get the weekId from the route
        lectureContent: null,                  // Placeholder for lecture content
      };
    },
    created() {
      this.fetchLectureContent(); // Fetch content when component is created
    },
    methods: {
      fetchLectureContent() {
        // Here you would fetch the lecture content based on courseId and weekId.
        // For this example, I'm just setting a static message.
        // You can replace this with an API call to fetch actual content.

        this.lectureContent = `This is the content for the Lecture of Course ${this.courseId} - Week ${this.weekId}`;
      },
      downloadContent() {
        const link = document.createElement('a');
        link.href = `/path/to/your/lecture-${this.courseId}-week${this.weekId}.pdf`; // Dynamically generate the PDF path
        link.download = `Lecture-Course${this.courseId}-Week${this.weekId}.pdf`;
        link.click();
      },
    },
  };
</script>

<style scoped>
  .lecture-container {
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
