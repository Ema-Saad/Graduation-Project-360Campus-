<template>
  <div class="project-details-container">
    <!-- Project Title and Close Button -->
    <div class="header">
      <button class="back-button" @click="goBack">✖</button>
      <h1 class="project-title">{{ project.title }}</h1>
      <button @click="downloadPDF" class="download-button">Download Project</button>
    </div>

    <!-- Project Content -->
    <div class="project-content">
      <h2>Introduction</h2>
      <p><strong>Purpose</strong></p>
      <p>{{ project.description }}</p>

      <p><strong>Document conventions</strong></p>
      <p>{{ project.documentConventions }}</p>

      <p><strong>Project scope</strong></p>
      <p>{{ project.scope }}</p>

      <h2>Overall Description</h2>
      <p><strong>Product perspective</strong></p>
      <p>{{ project.productPerspective }}</p>

      <!-- Additional fields as needed -->
    </div>
  </div>
</template>

<script>
  export default {
    props: ['id'],
    data() {
      return {
        project: {
          title: '360Campus Project',
          description: 'The purpose of this document is to provide a comprehensive overview of the 360Campus system. This integrated platform aims to enhance the university experience...',
          documentConventions: 'Document conventions text here...',
          scope: '360Campus is an integrated online platform designed to facilitate various functions within the university...',
          productPerspective: 'The 360Campus system is a new, self-contained product designed to enhance the university experience...',
        }
      };
    },
    methods: {

      goBack() {
        this.$router.go(-1); // Navigate back to the previous page
      },

      downloadPDF() {
        // Replace with the actual PDF URL
        const pdfUrl = 'path/to/360Campus_Project.pdf';
        const link = document.createElement('a');
        link.href = pdfUrl;
        link.setAttribute('download', '360Campus_Project.pdf');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
    }
  };
</script>

<style scoped>
  .project-details-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Georgia', serif;
    line-height: 1.6;
    color: #333;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .back-button {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #333;
    margin-right: 10px;
  }

  .project-title {
    font-size: 28px;
    font-weight: bold;
  }

  .download-button {
    padding: 10px 15px;
    background-color: #3a0ca3;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
  }

    .download-button:hover {
      background-color: #240c6a;
    }

  .project-content h2 {
    font-size: 20px;
    color: #2a3d6b;
    margin-top: 20px;
    margin-bottom: 10px;
  }

  .project-content p {
    margin-bottom: 15px;
  }

    .project-content p strong {
      color: #2a3d6b;
      font-weight: bold;
    }


</style>
