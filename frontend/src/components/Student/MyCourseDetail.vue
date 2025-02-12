<template>
  <div class="page">
    <!-- Top Banner -->
    <div class="top-banner">
      <div class="banner-text">
        <span class="course-code">{{ course.title }}</span>
        <h1 class="course-name">{{ course.subtitle }}</h1>
      </div>
      <img :src="bannerImage" alt="Course Banner" class="banner-image" />
    </div>

    <!-- Chat Icon -->
    <div class="chat-icon" @click="toggleChat">
      <i class="fas fa-comment-dots"></i>
    </div>

    <!-- Chat Popup -->
    <div v-if="showChat" class="chat-popup">
      <div class="chat-header">
        <span>Chat</span>
        <button class="close-button" @click="toggleChat" aria-label="Close Chat">✖</button>
      </div>
      <div class="chat-messages" ref="chatMessages">
        <div v-for="(message, index) in chatMessages"
             :key="index"
             class="chat-message"
             :class="message.sender === 'me' ? 'my-message' : 'their-message'">
          <div class="message-info">
            <img v-if="message.sender === 'them'" src="@/assets/chaticon.png" alt="Person Icon" class="person-icon" />
            <img v-if="message.sender === 'me'" src="@/assets/chaticon2.png" alt="Your Icon" class="person-icon" />
            <span class="sender-name">{{ message.sender === 'me' ? 'You' : 'Ahmed' }}</span>
          </div>
          <div class="chat-bubble">
            <span class="message-text">{{ message.text }}</span>
          </div>
        </div>
      </div>
      <div class="chat-input">
        <input type="text" v-model="newMessage" placeholder="Enter your Message...." @keydown.enter="sendMessage" />
        <button @click="sendMessage">Send</button>
      </div>
    </div>

    <!-- Homework Section -->
    <div class="homework-section">
      <div class="section-header">
        <div class="badge">{{ homeworkCount }}</div> <!-- Bind the badge count here -->
        <h2 class="section-title">Required Homework</h2>
        <button class="todo-button" @click="goToTodoPage">To Do</button>
      </div>



      <!-- Homework List Item -->
      <ul class="homework-list">
        <li v-for="(week, index) in course.weeks" :key="index" class="homework-item" @click="toggleDetails(index)">
          <div class="week-content">
            <div class="week-image-container">
              <img :src="week.image" :alt="'Week ' + week.weekNumber" class="week-image" />
              <div class="week-overlay">
                <span class="week-text">Week {{ week.weekNumber }}</span>
              </div>
            </div>
          </div>

          <!-- Week Info -->
          <div class="week-info">
            <button class="expand-button">{{ week.showDetails ? '▲' : '▼' }}</button>
          </div>

          <!-- Week Details Dropdown -->
          <div v-if="week.showDetails" class="week-details">
            <ul class="dropdown-menu">
              <li>
                <router-link :to="{ name: 'CourseLecture', params: { weekId: week.weekNumber } }" class="dropdown-item">
                  Lecture
                </router-link>
              </li>
              <li>
                <router-link :to="{ name: 'TutorialChat', params: { courseId: course.title, weekId: week.weekNumber } }" class="dropdown-item">
                  Tutorial
                </router-link>
              </li>
              <li>
                <!-- Updated route for Lab -->
                <router-link :to="{ name: 'CourseLab', params: { courseId: course.title, weekId: week.weekNumber } }" class="dropdown-item">
                  Lab
                </router-link>
              </li>
              <li>
                <router-link :to="{ name: 'taskDetail', params: { taskId: week.weekNumber } }" class="dropdown-item">
                  Assignment
                </router-link>
              </li>
              <li>
                <router-link :to="{ name: 'Quiz', params: { weekId: week.weekNumber } }" class="dropdown-item">
                  Quiz
                </router-link>
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>


<script>
  import bannerImage from "@/assets/pexels-photo.png";
  import week1Image from "@/assets/pexels-photo.png";
  import week2Image from "@/assets/pexels-photo.png";
  import week3Image from "@/assets/pexels-photo.png";
  import week4Image from "@/assets/pexels-photo.png";
  export default {
    data() {
      return {
        bannerImage,
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
        showChat: false,
        chatMessages: [
          { sender: "them", text: "Hi there!" },
          { sender: "me", text: "Hello!" },
        ],
        newMessage: "",
        homeworkCount: 2, // Dynamic count for homework (this can be changed based on real data)
      };
    },
    methods: {
      toggleDetails(index) {
        this.course.weeks[index].showDetails = !this.course.weeks[index].showDetails;
      },
      goToTodoPage() {
        this.$router.push({ name: "ToDoPage" });
      },
      toggleChat() {
        this.showChat = !this.showChat;
      },
      sendMessage() {
        if (this.newMessage.trim() !== "") {
          this.chatMessages.push({ sender: "me", text: this.newMessage });
          this.newMessage = "";
          this.autoReply();
          this.$nextTick(() => {
            const chatMessagesElement = this.$refs.chatMessages;
            chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
          });
        }
      },
      autoReply() {
        setTimeout(() => {
          this.chatMessages.push({ sender: "them", text: "Thanks for your message!" });
          this.$nextTick(() => {
            const chatMessagesElement = this.$refs.chatMessages;
            chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
          });
        }, 1000);
      },
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
    position: relative;
    width: 100%;
    text-align: center;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .banner-image {
    width: 100%;
    height: 270px;
    max-width: 100%;
    display: block;
    margin: 0 auto;
    border-bottom: 2px solid #ddd;
    max-height: 500px;
  }

  /* Banner Text */
  .banner-text {
    position: absolute;
    top: 30%; /* Vertically center */
    left: 10%; /* Horizontally center */
    color: black;
    font-family: Arial, sans-serif;
  }

  .course-code {
    font-size: 1.2em;
    font-weight: bold;
  }

  .course-name {
    font-size: 2.5em;
    font-weight: bold;
    margin-top: 5px;
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

    .todo-button:hover {
      background-color: darkorange;
    }

  /* Weekly Homework List */
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
    border-radius: 8px;
    padding: 15px;
    border: 1px solid #ccc;
    cursor: pointer; /* Ensure it's clickable */
    transition: border-color 0.3s ease, background-color 0.3s ease;
  }

    .homework-item:hover {
      border-color: #007bff;
    }
  .week-content {
    display: flex;
    align-items: center;
    gap: 15px;
  }

  .week-image-container {
    position: relative; /* Positioning context for overlay */
    width: 100%; /* Ensure the container takes up full width */
  }

  .week-image {
    width: 25%;
    height: 120px;
    object-fit: cover;
    border-radius: 4px;
  }
  .week-overlay {
    position: absolute;
    top: 50%;
    left: 10%;
    transform: translate(-50%, -50%);
    padding: 10px 20px;
    border-radius: 4px;
  }

  .week-text {
    color: black;
    font-size: 1.3em;
    font-weight: bold;
  }

  .week-info {
    display: flex;
    flex-grow: 1;
    justify-content: flex-end;
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

  /* Remove bullets from the dropdown menu */
  .dropdown-menu {
    list-style: none; /* Remove bullet points */
    padding-left: 0; /* Remove left padding */
  }

  /* Remove any default styling that might add circles */
  .dropdown-item {
    text-decoration: none;
    color: black; /* Set the link color to black */
    padding: 8px 0;
    margin: 0; /* Ensure there is no margin */
    border-radius: 0; /* Remove border radius if applied */
  }

    .dropdown-item:hover {
      text-decoration: underline; /* Underline effect on hover */
      color: #007bff; /* Optional: Change color to blue when hovered */
    }
  /* Chat Icon */
  .chat-icon {
    position: fixed;
    bottom: 42%;
    right: 16px;
    background-color: darkorange; /* Make the chat icon background black */
    color: black; /* Change icon color to white for contrast */
    width: 50px; /* Decreased width */
    height: 50px; /* Slightly larger height to balance the icon */
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    font-size: 1.5em;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s, transform 0.3s ease-in-out; /* Smooth transition for hover effect */
  }

    .chat-icon:hover {
      background: radial-gradient(circle, #3234A9 40%, rgba(50, 52, 169, 0.5) 70%, rgba(50, 52, 169, 0.1) 100%);
      color: black; /* Change icon color */
      transform: scale(1.1) translateY(-3px);
      box-shadow: 0 0 20px rgba(50, 52, 169, 0.6);
    }

  /* Chat Popup */
  .chat-popup {
    position: fixed;
    bottom: 40px;
    right: 20px;
    width: 350px;
    background: linear-gradient( rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7) ), url('@/assets/chatbackground.jpeg') no-repeat center center;
    background-size: cover;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    color: white;
    z-index: 1000;
    padding: 15px;
    display: flex;
    flex-direction: column;
    height: 450px; /* Ensure the chat popup has a fixed height */
  }

  /* Chat Header */
  .chat-header {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .close-button {
    background: none;
    border: none;
    color: white;
    font-size: 1.5em;
    cursor: pointer;
  }

  /* Chat Message Styling */
  /* Chat Messages */
  .chat-messages {
    flex-grow: 1;
    overflow-y: auto;
    max-height: 300px; /* Adjust as needed */
    padding-right: 10px; /* Prevent text from overlapping the scrollbar */
    margin-bottom: 10px;
  }

    .chat-messages::-webkit-scrollbar {
      width: 8px;
    }

    .chat-messages::-webkit-scrollbar-thumb {
      background-color: #1d72b8;
      border-radius: 4px;
    }

      .chat-messages::-webkit-scrollbar-thumb:hover {
        background-color: #135a96;
      }

  .my-message {
    text-align: right;
  }

  .their-message {
    text-align: left;
  }

  /* Message Info (Name and Icon) */
  .message-info {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-bottom: 5px;
  }

  .my-message .message-info {
    justify-content: flex-end;
  }

  .message-info img {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin-right: 5px;
  }

  .my-message .message-info img {
    margin-right: 0;
    margin-left: 5px;
  }

  .sender-name {
    font-size: 0.85em;
    font-weight: bold;
    color: #d0d0d0;
  }

  /* Chat Bubble */
  .chat-bubble {
    display: inline-block;
    padding: 10px;
    border-radius: 15px;
    background-color: rgba(255, 255, 255, 0.9);
    max-width: 70%;
    word-wrap: break-word;
  }

  .my-message .chat-bubble {
    background-color: #1d72b8;
    color: white;
  }

  .their-message .chat-bubble {
    background-color: white;
    color: black;
    text-align: left;
  }


  /* Chat Input */
  .chat-input {
    display: flex;
    padding-top: 10px;
  }

    .chat-input input {
      flex-grow: 1;
      padding: 10px;
      border-radius: 15px;
      border: none;
      margin-right: 10px;
      font-size: 1em;
      background-color: #f1f1f1;
    }

    .chat-input button {
      padding: 10px 20px;
      background-color: #1d72b8;
      color: white;
      border: none;
      border-radius: 20px;
      cursor: pointer;
    }
  /* Media Queries for Responsiveness */
  /* Media Queries for Responsiveness */

  /* For large screens (up to 1200px wide) */
  @media (max-width: 1200px) {
    .banner-text {
      left: 5%;
      top: 20%;
    }

    .course-name {
      font-size: 2em;
    }

    .todo-button {
      font-size: 0.9em;
    }

    .week-image-container {
      width: 150px; /* Wider container */
      height: 100px; /* Adjust height */
    }

    .week-image {
      width: 60%; /* Make the image wider */
      height: auto;
    }

    .week-text {
      font-size: 1.1em;
    }

    /* Positioning the arrow */
    .week-arrow {
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.5em; /* Adjust arrow size */
    }
  }

  /* For medium screens (up to 768px wide) */
  @media (max-width: 768px) {
    .top-banner {
      text-align: left;
    }

    .banner-text {
      left: 0;
      top: 10%;
      width: 100%;
    }

    .course-code {
      font-size: 1em;
    }

    .course-name {
      font-size: 1.8em;
    }

    .homework-item {
      flex-direction: column;
      align-items: center;
    }

    .week-info {
      justify-content: center;
    }

    .chat-popup {
      width: 300px;
    }

    .week-image-container {
      width: 120px; /* Adjust width */
      height: 80px;
    }

    .week-image {
      width: 70%; /* Image is wider */
      height: auto;
    }

    .week-arrow {
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.3em; /* Adjust size */
    }

    .chat-icon {
      bottom: 10px;
      right: 10px;
      width: 50px;
      height: 50px;
    }

    .chat-popup {
      width: 270px;
      height: 400px;
    }
  }

  /* For small screens (up to 480px wide) */
  @media (max-width: 480px) {
    .top-banner {
      text-align: left;
    }

    .banner-text {
      left: 0;
      top: 15%;
    }

    .course-name {
      font-size: 1.5em;
    }

    .week-image-container {
      width: 100px; /* Smaller container */
      height: 70px;
    }

    .week-image {
      width: 80%; /* Make the image wider */
      height: auto;
    }

    .week-arrow {
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.2em; /* Adjust arrow size */
    }

    .week-text {
      font-size: 1em;
    }

    .chat-icon {
      bottom: 10px;
      right: 10px;
      width: 50px;
      height: 50px;
    }

    .chat-popup {
      width: 270px;
      height: 400px;
    }
  }

</style>
