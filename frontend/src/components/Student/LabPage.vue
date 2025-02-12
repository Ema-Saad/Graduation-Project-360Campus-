<template>
  <div class="lab-container">
    <h1>Lab for Course {{ courseId }} - Week {{ weekId }}</h1>
    <button class="download-button" @click="downloadContent">Download Lab PDF</button>
    <p v-if="labContent">{{ labContent }}</p>
  </div>
</template>

<script>
  export default {
    props: ['id'],
    data() {
      return {
        courseId: this.$route.params.courseId,  // Access the course ID from the route
        weekId: this.$route.params.weekId,      // Access the week ID from the route
        labContent: null,                       // Placeholder for lab content
      };
    },
    created() {
      this.fetchLabContent(); // Fetch the lab content when the component is created
    },
    methods: {
      fetchLabContent() {
        // Example: Fetch or load content based on courseId and weekId
        this.labContent = `This is the content for the Lab for Course ${this.courseId}, Week ${this.weekId}`;
      },
      downloadContent() {
        const link = document.createElement('a');
        link.href = '/path/to/your/lab.pdf'; // Replace with the actual path to your PDF
        link.download = 'Lab.pdf';
        link.click();
      },
    },
  };
</script>

<style scoped>
  .lab-container {
    position: relative;
  }

  .download-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #201887;
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

    .lab-container {
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
      z-index: 10; /* Keeps it above the chat icon */
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

    .lab-container {
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
      z-index: 10; /* Keeps it above the chat icon */
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

    .lab-container {
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
      z-index: 10; /* Keeps it above the chat icon */
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
