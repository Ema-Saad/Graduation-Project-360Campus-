<template>
  <div class="courselecture-container">
    <h1>Course Lecture {{ courseId }} - Week {{ weekId }}</h1>
    <button class="download-button" @click="downloadContent">Download Lecture PDF</button>
    <p v-if="lectureContent">{{ lectureContent }}</p>

    <!-- Chat Icon using a different emoji -->
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
  </div>
</template>

<script>
  export default {
    data() {
      return {
        courseId: this.$route.params.courseId,
        weekId: this.$route.params.weekId,
        lectureContent: null,
        showChat: false,
        chatMessages: [
          { sender: "them", text: "Hi there!" },
          { sender: "me", text: "Hello!" }
        ],
        newMessage: ""
      };
    },
    created() {
      this.fetchLectureContent();
    },
    methods: {
      fetchLectureContent() {
        this.lectureContent = `This is the content for Course Lecture ${this.courseId} - Week ${this.weekId}`;
      },
      downloadContent() {
        const link = document.createElement('a');
        link.href = `/path/to/your/courselecture-${this.courseId}-week${this.weekId}.pdf`;
        link.download = `CourseLecture-${this.courseId}-Week${this.weekId}.pdf`;
        link.click();
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
      }
    }
  };
</script>

<style scoped>
  .courselecture-container {
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
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

    .download-button:hover {
      background-color: darkorange;
    }

  .chat-icon {
    position: fixed;
    bottom: 76%;
    right: 200px;
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
  @media (max-width: 1024px) {
    .tutorialchat-container {
      padding: 15px;
    }

    .chat-icon {
      top: 50px; /* Adjust position */
      right: 20px;
      width: 45px;
      height: 45px;
      font-size: 1.4em;
      z-index: 5; /* Ensures it's behind the download button */
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

  @media (max-width: 600px) {
    .tutorialchat-container {
      padding: 10px;
    }

    .chat-icon {
      top: 65px;
      right: 12px;
      width: 38px;
      height: 38px;
      font-size: 1.1em;
    }

    .download-button {
      font-size: 1em;
      padding: 10px;
      width: 100%;
      text-align: center;
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
</style>
