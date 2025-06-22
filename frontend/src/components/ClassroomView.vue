<template>
  <AssignmentCreate
    :course_id="courseId"
    v-if="showAssignmentCreateDialog"
    @close="showAssignmentCreate = false"
  />

  <OnlineMeetingCreate
    :course_id="courseId"
    v-if="showOnlineMeetingCreateDialog"
    @close="showOnlineMeetingCreateDialog = false"
  />
  <div v-if="classroom" class="page">
    <!-- Top Banner -->
    <div class="top-banner">
      <div class="banner-text">
        <h1 class="course-name">{{ classroom.course.title }}</h1>
        <span class="course-code">Taught by {{ classroom.instructor.first_name }} {{ classroom.instructor.last_name }}</span>
      </div>
      <img :src="bannerImage" alt="Course Banner" class="banner-image" />
    </div>

    <!-- Homework Section -->
    <div class="homework-section">
      <div class="section-header">
        <div class="badge">{{ tasks.length }}</div> <!-- Bind the badge count here -->
        <h2 class="section-title">Required Homework</h2>
        <button class="todo-button">
          <router-link :to="{ name: 'CourseView', params: { courseId } }">
            Materials
          </router-link>
        </button>
      </div>

<div v-if="$root.person_kind === 'P'" style="margin-bottom: 15px;">
  <button class="assignment-button" @click="showAssignmentCreateDialog = true"> 
    Add new assignment 
  </button>
  <button class="meeting-button" @click="showOnlineMeetingCreateDialog = true"> 
    Add new meeting 
  </button>
<a href="http://127.0.0.1:3000/" target="_blank" class="quiz-button">
  create meeting
</a>

</div>
      <div id="task-list">
  <div class="task-item" v-for="task in tasks" :key="task.id">
    <div class="task-icon">
      <span class="fas" :class="[getIcon(task)]"></span>
    </div>
        
    <router-link class="task" :to="task.url">
      <span class="task-name"> {{ task.title }} </span>
    </router-link>

    <div class="due"> {{ computeTimeString(task) }} </div>

    <!-- Add this delete button only for instructors -->
<!-- Add this delete button only for instructors -->
<button
  class="delete-button"
  @click="deleteTask(task.id)"
>
  Delete
</button>


  </div>
</div>

    </div>
    <!-- Added to the bottom of the template -->
<div class="chat-icon" @click="toggleChat">
  <i class="fas fa-comment-dots"></i>
</div>

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
        <span class="sender-name">{{ message.sender === 'me' ? 'You' : classroom.instructor.first_name }}</span>
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
  </div>
</template>
<script>
  import bannerImage from "@/assets/pexels-photo.png";
  import { useGlobalStore } from '@/global_store.js';
  import AssignmentCreate from "./AssignmentCreate.vue";
  import OnlineMeetingCreate from "./OnlineMeetingCreate.vue";

  export default {
    data() {
      return {
        bannerImage,
        tasks: [],
        classroom: null,
        showChat: false,
        chatMessages: [
          { sender: "them", text: "Hi there! How can I help you with the course?" }
        ],
        newMessage: "",
        homeworkCount: 2,
        showAssignmentCreateDialog: false,
        showOnlineMeetingCreateDialog: false,
      };
    },
    components: {
      AssignmentCreate,
      OnlineMeetingCreate,
    },
    props: ['courseId'],
    beforeRouteEnter(to, from, next) {
      const store = useGlobalStore();

      Promise.all([
        store.request_api_endpoint(`api/course/${to.params.courseId}/classroom`),
        store.request_api_endpoint(`api/course/${to.params.courseId}/classroom/tasks`),
        store.request_api_endpoint(`api/course/${to.params.courseId}/classroom/assignments`)
      ])
        .then(([classroom, tasks, assignments]) => {
          const normalise = (d) => ({
            ...d,
            time: d.time ? new Date(d.time) : null,
            url: (() => {
              if (d.kind === 'a') return { name: 'AssignmentView', params: { assignmentId: d.id } };
              else if (d.kind === 'o') return { name: 'OnlineMeetingView', params: { onlineMeetingId: d.id } };
              else return {};
            })(),
          });

          const userKey = store.person?.id || 'student';
          let deleted = JSON.parse(localStorage.getItem(`deletedTasks_${userKey}`) || '[]');
          tasks = tasks.filter(t => !deleted.includes(t.id));
          assignments = assignments.filter(a => !deleted.includes(a.id));

          next(vm => {
            vm.classroom = classroom;
            vm.tasks = [
              ...tasks.map(normalise),
              ...assignments.map(normalise)
            ];
          });
        })
        .catch(err => {
          console.error("Error in beforeRouteEnter:", err);
          next(); // Always call next to continue routing
        });
    },
    methods: {
      getIcon(task) {
        return task.kind === 'o' ? 'fa-video' : 'fa-file-alt';
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
          this.chatMessages.push({
            sender: "them",
            text: this.getRandomResponse()
          });
          this.$nextTick(() => {
            const chatMessagesElement = this.$refs.chatMessages;
            chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
          });
        }, 1000);
      },
      getRandomResponse() {
        const responses = [
          "I'll get back to you on that.",
          "Thanks for your question!",
          "That's a good point.",
          "Let me check the syllabus for you.",
          "I can help with that during office hours.",
          "Have you checked the course materials?",
          "That's covered in week 3's lecture."
        ];
        return responses[Math.floor(Math.random() * responses.length)];
      },
      computeTimeString(task) {
        let date = task.time;
        const MILLISECONDS_IN_DAY = 24 * 60 * 60 * 1000;
        const DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

        if (!date) return "No Due Date";
        let hour = `${date.getHours().toString().padStart(2, "0")}:${date.getMinutes().toString().padStart(2, "0")}`;

        if (Date.now() > date) return "Missed";
        else if (date - Date.now() <= MILLISECONDS_IN_DAY) return `Due Today at ${hour}`;
        else if (date - Date.now() <= 2 * MILLISECONDS_IN_DAY) return `Due Tomorrow at ${hour}`;
        else if (date - Date.now() <= 7 * MILLISECONDS_IN_DAY) return `Due ${DAYS[date.getDay()]} at ${hour}`;
        else return `Due ${MONTHS[date.getMonth()]}. ${date.getDate().toString().padStart(2, "0")} at ${hour}`;
      },
      deleteTask(taskId) {
        this.tasks = this.tasks.filter(task => task.id !== taskId);
        const store = useGlobalStore();
        const userKey = store.person?.id || 'student';

        let deleted = JSON.parse(localStorage.getItem(`deletedTasks_${userKey}`) || '[]');
        if (!deleted.includes(taskId)) {
          deleted.push(taskId);
          localStorage.setItem(`deletedTasks_${userKey}`, JSON.stringify(deleted));
        }
      },
      resetDeletedTasks() {
        const store = useGlobalStore();
        const userKey = store.person?.id || 'student';
        localStorage.removeItem(`deletedTasks_${userKey}`);
        location.reload();
      }
    }
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

  .todo-button > a {
    text-decoration: none;
    color: white;
  }

    .todo-button:hover {
      background-color: darkorange;
    }
  .assignment-button,
.meeting-button,
.quiz-button {
  padding: 10px 20px;
  background-color: navy;
  color: white;
  font-size: 1em;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 10px;
}

/* Individual hover styles (same for now, but can be customized) */
.assignment-button:hover,
.meeting-button:hover,
.quiz-button:hover {
  background-color: darkorange;
}

  .task-list {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .task-item {
    align-items: center;
    justify-content: left;
    display: flex;
    flex-direction: row;
  }

  .task-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #1a237e;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 10px;
  }

  .task-icon span {
    font-size: 1.5em;
  }

  .task-name {
    text-weight: bold;
  }

  .due {
    flex: 1;
    text-align: right;
    color: gray;
  }
.quiz-button {
  text-decoration: none;
}
.chat-icon {
  position: fixed;
  bottom: 46%;
  right: 8%;
  background-color: darkorange;
  color: black;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  font-size: 1.5em;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s, transform 0.3s ease-in-out;
  z-index: 1000;
}

.chat-icon:hover {
  background: radial-gradient(circle, #3234A9 40%, rgba(50, 52, 169, 0.5) 70%, rgba(50, 52, 169, 0.1) 100%);
  color: black;
  transform: scale(1.1) translateY(-3px);
  box-shadow: 0 0 20px rgba(50, 52, 169, 0.6);
}

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
  height: 450px;
}

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

.chat-messages {
  flex-grow: 1;
  overflow-y: auto;
  max-height: 300px;
  padding-right: 10px;
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

@media (max-width: 1024px) {
  .chat-icon {
    top: 50px;
    right: 20px;
    width: 45px;
    height: 45px;
    font-size: 1.4em;
    z-index: 5;
  }
}

@media (max-width: 600px) {
  .chat-icon {
    top: 65px;
    right: 12px;
    width: 38px;
    height: 38px;
    font-size: 1.1em;
  }
}

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

  }

</style>
