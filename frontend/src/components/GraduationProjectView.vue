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
    max-width: 100%; /* Ensure full-width container */
    margin: 0; /* No margin, ensuring no shift */
    padding: 20px; /* Add padding to prevent content from touching the edges */
    font-family: 'Georgia', serif;
    line-height: 1.6;
    color: #333;
    box-sizing: border-box; /* Include padding in element's total width */
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
    font-size: 25px;
    cursor: pointer;
    color: #2e2d2d;
    margin-right: 10px;
      transition: color 0.3s ease, transform 0.2s ease;
  }

.back-button:hover {
  color: rgb(0, 0, 0);
  transform: scale(1.2);
}

  .project-title {
    font-size: 28px;
    font-weight: bold;
  }

  .download-button {
    padding: 10px 15px;
    background-color: #201887;
    color: #fff;
    border: none;
    border-radius: 7px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
  }

    .download-button:hover {
      background-color: darkorange;
    }

  .project-content {
    width: 100%; /* Ensure content spans full width */
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

  /* Media Queries for Responsiveness */

  /* For screens smaller than 1200px */
  @media (max-width: 1200px) {
    .project-details-container {
      padding: 15px;
    }

    .header {
      flex-direction: column;
      align-items: flex-start;
      margin-bottom: 20px;
    }

    .back-button {
      font-size: 22px;
    }

    .project-title {
      font-size: 24px;
    }

    .download-button {
      padding: 8px 12px;
      font-size: 14px;
    }

    .project-content h2 {
      font-size: 18px;
      margin-top: 20px;
    }

    .project-content p {
      font-size: 14px;
      margin-bottom: 12px;
    }

      .project-content p strong {
        font-size: 15px;
      }
  }

  /* For screens smaller than 768px */
  @media (max-width: 768px) {
    .project-details-container {
      padding: 10px;
    }

    .header {
      flex-direction: column;
      align-items: flex-start;
    }

    .back-button {
      font-size: 20px;
      margin-bottom: 10px;
    }

    .project-title {
      font-size: 22px;
    }

    .download-button {
      padding: 8px 12px;
      font-size: 14px;
    }

    .project-content h2 {
      font-size: 16px;
      margin-top: 18px;
    }

    .project-content p {
      font-size: 13px;
      margin-bottom: 10px;
    }

      .project-content p strong {
        font-size: 14px;
      }
  }

  /* For screens smaller than 480px */
  @media (max-width: 480px) {
    .project-details-container {
      padding: 8px;
    }

    .header {
      flex-direction: column;
      align-items: flex-start;
    }

    .back-button {
      font-size: 18px;
      margin-bottom: 10px;
    }

    .project-title {
      font-size: 20px;
    }

    .download-button {
      padding: 6px 10px;
      font-size: 12px;
    }

    .project-content h2 {
      font-size: 14px;
      margin-top: 16px;
    }

    .project-content p {
      font-size: 12px;
      margin-bottom: 8px;
    }

      .project-content p strong {
        font-size: 13px;
      }
  }
</style>
