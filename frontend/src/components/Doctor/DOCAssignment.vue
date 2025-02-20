<template>
  <div class="assignment-container">
    <h1>Assignment for Course {{ courseId }} - Week {{ weekId }}</h1>
    <button class="download-button" @click="downloadContent">Download Assignment PDF</button>
    <p v-if="assignmentContent">{{ assignmentContent }}</p> <!-- Display dynamic assignment content -->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        courseId: this.$route.params.courseId,  // Get courseId from the route parameters
        weekId: this.$route.params.weekId,      // Get weekId from the route parameters
        assignmentContent: null,                // Placeholder for dynamic assignment content
      };
    },
    created() {
      this.fetchAssignmentContent();  // Fetch content when component is created
    },
    methods: {
      fetchAssignmentContent() {
        // Replace this with an API call to fetch assignment content based on courseId and weekId.
        this.assignmentContent = `This is the content for the Assignment of Course ${this.courseId} - Week ${this.weekId}`;
      },
      downloadContent() {
        const link = document.createElement('a');
        link.href = `/path/to/your/assignment-${this.courseId}-week${this.weekId}.pdf`;  // Dynamically generate the PDF path
        link.download = `Assignment-Course${this.courseId}-Week${this.weekId}.pdf`;
        link.click();
      },
    },
  };
</script>

<style scoped>
  .assignment-container {
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
      background-color: darkorange; /* Darker blue on hover */
    }

  /* Media Queries for Responsiveness */
  @media (max-width: 1024px) {
    .assignment-container {
      padding: 15px;
    }

    .download-button {
      position: relative; /* Change position to relative for better layout */
      top: auto;
      right: auto;
      margin-top: 15px;
      margin-right: 0;
      width: 100%;
      font-size: 1.2em;
      padding: 12px;
    }

      .download-button:hover {
        background-color: #004085; /* Adjust hover color for contrast */
      }

    h1 {
      font-size: 1.6em;
      text-align: center;
    }

    p {
      font-size: 1.1em;
      text-align: center;
      margin-top: 15px;
    }
  }

  @media (max-width: 600px) {
    .assignment-container {
      padding: 10px;
    }

    .download-button {
      font-size: 1em;
      padding: 10px;
    }

    h1 {
      font-size: 1.4em;
      margin-bottom: 10px;
    }

    p {
      font-size: 1em;
      margin-top: 10px;
    }
  }

  @media (max-width: 360px) {
    .assignment-container {
      padding: 5px;
    }

    .download-button {
      position: relative;
      top: auto;
      right: auto;
      margin-top: 15px;
      width: 100%;
      font-size: 1.2em;
      padding: 12px;
      z-index: 10; /* Keeps it above other content */
    }

    h1 {
      font-size: 1.6em;
      text-align: center;
    }

    p {
      font-size: 1.1em;
      text-align: center;
      margin-top: 15px;
    }
  }
</style>
