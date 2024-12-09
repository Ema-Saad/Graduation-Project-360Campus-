<template>
  <div class="page">
    <!-- Top Banner -->
    <div class="top-banner">
      <img :src="bannerImage" alt="Course Banner" class="banner-image" />
    </div>

    <!-- Homework Section -->
    <div class="homework-section">
      <div class="section-header">
        <div class="badge">2</div>
        <h2 class="section-title">Required Homework</h2>
        <button class="todo-button" @click="goToTodoPage">To Do</button>
      </div>

      <!-- Weekly Homework List -->
      <ul class="homework-list">
        <li v-for="(week, index) in course.weeks" :key="index" class="homework-item">
          <div class="week-content">
            <img :src="week.image" :alt="'Week ' + week.weekNumber" class="week-image" />
            <div class="week-info">
              <span class="week-title">Week {{ week.weekNumber }}</span>
              <button class="expand-button" @click="toggleDetails(index)">
                {{ week.showDetails ? '▲' : '▼' }}
              </button>
            </div>
          </div>

          <!-- Week Details Dropdown -->
          <div v-if="week.showDetails" class="week-details">
            <ul class="dropdown-menu">
              <li>
                <router-link :to="{ name: 'Lecture', params: { weekId: week.weekNumber } }" class="dropdown-item">Lecture</router-link>
              </li>
              <li>
                <router-link :to="{ name: 'Tutorial', params: { weekId: week.weekNumber } }" class="dropdown-item">Tutorial</router-link>
              </li>
              <li>
                <router-link :to="{ name: 'Lab', params: { weekId: week.weekNumber } }" class="dropdown-item">Lab</router-link>
              </li>
              <li>
                <router-link :to="{ name: 'Assignment', params: { weekId: week.weekNumber } }" class="dropdown-item">Assignment</router-link>
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import bannerImage from "@/assets/pexels-photo.png"; // Import the top banner image
  import week1Image from "@/assets/pexels-photo.png"; // Import week 1 image
  import week2Image from "@/assets/pexels-photo.png"; // Import week 2 image
  import week3Image from "@/assets/pexels-photo.png"; // Import week 3 image
  import week4Image from "@/assets/pexels-photo.png"; // Import week 4 image

  export default {
    data() {
      return {
        bannerImage, // Top banner image
        course: {
          title: "CSC 410",
          subtitle: "Software Quality",
          author: "Mohamed",
          weeks: [
            { weekNumber: 1, image: week1Image, showDetails: false },
            { weekNumber: 2, image: week2Image, showDetails: false },
            { weekNumber: 3, image: week3Image, showDetails: false },
            { weekNumber: 4, image: week4Image, showDetails: false },
          ],
        },
      };
    },
    methods: {
      toggleDetails(index) {
        this.course.weeks[index].showDetails = !this.course.weeks[index].showDetails;
      },
      goToTodoPage() {
        // Navigate to the TodoPage when the "To Do" button is clicked
        this.$router.push({ name: 'ToDoPage' });
      }
    },
  };
</script>

<style scoped>
  /* General Page Styles */
  .page {
    padding: 0;
    margin: 0 auto;
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    max-width: 1300px; /* Adjusted the width */
    border: 1px solid #ddd; /* Optional: Adds a border around the page for emphasis */
  }

  /* Top Banner */
  .top-banner {
    width: 100%;
    text-align: center;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .banner-image {
    width: 100%;
    height: auto;
    max-width: 100%;
    display: block;
    margin: 0 auto;
    border-bottom: 2px solid #ddd;
    max-height: 500px;
  }

  /* Homework Section */
  .homework-section {
    padding: 20px;
    margin: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .section-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }

  .badge {
    background-color: orange;
    color: white;
    font-size: 1.5em;
    font-weight: bold;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .section-title {
    font-size: 1.8em;
    flex-grow: 1;
    margin-left: 10px;
  }

  .todo-button {
    padding: 10px 20px;
    background-color: navy;
    color: white;
    font-size: 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  /* Weekly Homework List */
  .homework-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .homework-item {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
  }

  .week-content {
    display: flex;
    align-items: center;
    gap: 15px;
  }

  .week-image {
    width: 100px;
    height: 100px;
    border-radius: 8px;
    object-fit: cover;
  }

  .week-info {
    display: flex;
    flex-grow: 1;
    justify-content: space-between;
    align-items: center;
  }

  .week-title {
    font-size: 1.2em;
    font-weight: bold;
  }

  .expand-button {
    background: none;
    border: none;
    color: gray;
    font-size: 1.5em;
    cursor: pointer;
  }

  .week-details {
    margin-top: 10px;
  }

    .week-details .dropdown-menu {
      display: flex;
      flex-direction: column;
      padding-left: 0;
    }

  .dropdown-item {
    text-decoration: none;
    color: #007bff;
    padding: 8px 0;
  }

    .dropdown-item:hover {
      text-decoration: underline;
    }
</style>
