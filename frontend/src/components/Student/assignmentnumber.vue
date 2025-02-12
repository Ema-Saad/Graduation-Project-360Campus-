<template>
  <div class="assignment-container">
    <h1>Assignment Number {{ assignmentNumber }}</h1>
    <button class="download-button" @click="downloadContent">Download Assignment PDF</button>
    <p v-if="assignmentContent">{{ assignmentContent }}</p>
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
  </div>
</template>

<script>
  export default {
    data() {
      return {
        assignmentNumber: this.$route.params.assignmentNumber, // Access passed assignmentNumber
        assignmentContent: null,
        showChat: false,
        chatMessages: [],
        newMessage: "",
      };
    },
    created() {
      this.fetchAssignmentContent();
    },
    methods: {
      fetchAssignmentContent() {
        this.assignmentContent = `This is the content for the Assignment Number ${this.assignmentNumber}`;
      },
      downloadContent() {
        const link = document.createElement('a');
        link.href = `/path/to/your/assignment-${this.assignmentNumber}.pdf`;
        link.download = `Assignment-${this.assignmentNumber}.pdf`;
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
            if (chatMessagesElement) {
              chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
            }
          });
        }
      },
      autoReply() {
        setTimeout(() => {
          this.chatMessages.push({ sender: "them", text: "Thanks for your message!" });
          this.$nextTick(() => {
            const chatMessagesElement = this.$refs.chatMessages;
            if (chatMessagesElement) {
              chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
            }
          });
        }, 1000);
      },
    },
  };
</script>


<style scoped>
  .assignment-container {
    position: relative;
    padding: 20px;
  }

  .download-button {
    position: absolute;
    top: 40px;
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
    bottom: 74%;
    right: 220px;
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
  }

    .chat-icon:hover {
      background: radial-gradient(circle, #3234A9 40%, rgba(50, 52, 169, 0.5) 70%, rgba(50, 52, 169, 0.1) 100%);
      color: black; /* Change icon color */
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
  /* Responsive Styles */
  @media screen and (max-width: 1200px) {
    .download-button {
      width: 100%;
      max-width: 350px;
      position: static;
      margin-top: 10px;
      font-size: 1rem;
    }

    .chat-popup {
      width: 80%;
    }

    .chat-icon {
      position: absolute;
      top: 0; /* Aligns chat icon at the top */
      right: 10px; /* Right aligned */
      z-index: 0; /* Place chat icon behind other elements */
      bottom: initial; /* Reset bottom positioning */
    }
  }

  @media screen and (max-width: 1024px) {
    .assignment-container {
      padding: 20px;
      text-align: center;
    }

    .download-button {
      position: static;
      margin-top: 10px;
      width: 80%;
      max-width: 300px;
    }

    .chat-icon {
      position: absolute;
      top: 0; /* Top aligned to be behind the button */
      right: 10px; /* Adjust this for desired positioning */
      z-index: 0; /* Behind the button */
    }
  }

  @media screen and (max-width: 768px) {
    .assignment-container {
      padding: 15px;
    }

    h1 {
      font-size: 1.5rem;
    }

    .download-button {
      width: 90%;
      font-size: 0.9rem;
      padding: 8px;
    }

    p {
      font-size: 0.9rem;
    }

    .chat-icon {
      position: absolute;
      top: 0; /* Top aligned */
      right: 10px;
      z-index: 0; /* Behind the download button */
    }
  }

  @media screen and (max-width: 480px) {
    .assignment-container {
      padding: 10px;
    }

    h1 {
      font-size: 1.3rem;
    }

    .download-button {
      width: 100%;
      font-size: 0.85rem;
      padding: 8px;
    }

    p {
      font-size: 0.85rem;
    }

    .chat-popup {
      width: 100%;
      height: 400px;
    }

    .chat-icon {
      position: absolute;
      top: 0; /* Positioned at the top */
      right: 10px;
      z-index: 0; /* Behind other elements */
    }
  }

</style>

