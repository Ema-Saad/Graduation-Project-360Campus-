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
    position: relative;
  }

  .download-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #1e0a74;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 7px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

    .download-button:hover {
      background-color: darkorange;
    }

  /* Media Queries for Responsiveness */
  @media (max-width: 768px) {
    .lecture-container {
      padding: 15px;
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

  @media (max-width: 480px) {
    .lecture-container {
      padding: 10px;
    }

    .download-button {
      position: relative;
      top: auto;
      right: auto;
      margin-top: 15px;
      width: 100%;
      font-size: 1.2em;
      padding: 12px;
      z-index: 10; /* Keeps it above the content */
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

  /* Extra adjustments for very small screens */
  @media (max-width: 360px) {
    .lecture-container {
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
      z-index: 10; /* Keeps it above the content */
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
