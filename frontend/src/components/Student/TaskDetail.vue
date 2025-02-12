<template>
  <div class="assignment-detail">
    <!-- Top Image -->
    <div class="top-image">
      <img src="@/assets/pexels-photo.png" alt="Assignment Detail Image" />
      <div class="top-image-overlay">
        <!-- Icon on the left -->
        <div class="icon">
          <i class="fas fa-file-alt"></i> <!-- Example icon -->
        </div>
        <!-- Assignment text on the right -->
        <div class="overlay-content">
          Assignment {{ assignmentNumber }} - {{ courseTitle }} - {{ courseCode }}
        </div>
      </div>
    </div>

    <!-- Two Sections Below -->
    <div class="sections-container">
      <!-- Left Section -->
      <div class="left-section">
        <div class="sheet-card">
          <div class="overlay">
            <span class="sheet-text">Assignment {{ assignmentNumber }}</span>
          </div>
          <img src="@/assets/pexels-photo.png" alt="Assignment Sheet Image" @click="viewSheet(assignmentNumber)" />

        </div>
      </div>

      <!-- Right Section -->
      <div class="right-section">
        <div class="deadline-section">
          <div class="left-info">
            <p class="due-date">Due Today, 11:59 pm</p>
            <div class="buttons">
              <input type="file" id="file-input" style="display:none;" @change="handleFileUpload" />
              <button @click="triggerFileInput" class="upload-button">Upload your Work</button>
              <button @click="submitWork" class="submit-button">Submit</button>
              <button @click="reSubmit" class="re-submit-button">Re-Submit</button>
            </div>

            <div v-if="uploadedFileName" class="uploaded-file">
              <p>Uploaded File: {{ uploadedFileName }}</p>
            </div>
          </div>

          <div class="right-info">
            <span class="status assigned">Assigned</span>
            <button @click="markAsDone" class="done-button">Mark As Done</button>
          </div>
        </div>
      </div>
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
        <div v-for="(message, index) in chatMessages" :key="index" class="chat-message" :class="message.sender === 'me' ? 'my-message' : 'their-message'">
          <div class="message-info">
            <span class="sender-name">{{ message.sender === 'me' ? 'You' : 'Ahmed' }}</span>
          </div>
          <div class="chat-bubble">
            <span class="message-text">{{ message.text }}</span>
          </div>
        </div>
      </div>
      <div class="chat-input">
        <input type="text" v-model="newMessage" placeholder="Enter your Message..." @keydown.enter="sendMessage" />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        assignmentNumber: 101,  // This would be dynamically passed or set based on context
        courseTitle: "Web Development",  // Example course title
        courseCode: "CS101",  // Example course code
        showChat: false,  // Control visibility of the chat
        newMessage: "",  // Model for new chat message
        chatMessages: [  // Array of chat messages
          { sender: "me", text: "Hello, how can I submit my work?" },
          { sender: "them", text: "You can upload it by clicking the 'Upload your Work' button." },
        ],
        selectedFile: null,  // Store the selected file
        uploaded: false,  // Track upload status
        uploadedFileName: "",  // Store the name of the uploaded file
      };
    },
    methods: {
      // Trigger the hidden file input element to open the file dialog
      triggerFileInput() {
        document.getElementById("file-input").click();  // Click the hidden input
      },

      // Handle the file upload and store the selected file's name
      handleFileUpload(event) {
        this.selectedFile = event.target.files[0];  // Get the first selected file
        if (this.selectedFile) {
          this.uploadedFileName = this.selectedFile.name;  // Set the uploaded file name
        }
      },

      // Navigate to the assignment detail page based on assignment number
      viewSheet(assignmentNumber) {
        this.$router.push({
          name: 'AssignmentByNumber',  // Navigate using the unique route name
          params: { assignmentNumber },  // Pass the assignment number as a parameter
        });
      },

      // Toggle chat visibility
      toggleChat() {
        this.showChat = !this.showChat;
      },

      // Send a new message in the chat
      sendMessage() {
        if (this.newMessage.trim()) {
          this.chatMessages.push({ sender: "me", text: this.newMessage });  // Add new message to chat
          this.newMessage = "";  // Clear input field
          this.$nextTick(() => {
            const chatMessages = this.$refs.chatMessages;
            chatMessages.scrollTop = chatMessages.scrollHeight;  // Auto scroll to bottom
          });

          // Simulate a response after 1 second
          setTimeout(() => {
            this.chatMessages.push({
              sender: "them",
              text: `I received your message: "${this.chatMessages[this.chatMessages.length - 2].text}"`,
            });
            this.$nextTick(() => {
              const chatMessages = this.$refs.chatMessages;
              chatMessages.scrollTop = chatMessages.scrollHeight;  // Auto scroll to bottom
            });
          }, 1000);  // Delay before simulating a response
        }
      },
    },
  };
</script>



<style scoped>
  /* Top Image Overlay */
  .top-image-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding-left: 20px;
  }

  .icon {
    margin-right: 10px;
    z-index: 1;
    font-size: 2rem;
  }

  .overlay-content {
    color: black;
    font-size: 1.5rem;
    font-weight: bold;
    z-index: 2;
  }

  /* General Styling */
  .task-detail {
    font-family: Arial, sans-serif;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
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
    height: 450px;
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

  /* Message Info */
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


  /* Top Image */
  .top-image {
    position: relative;
    width: 98vw;
    margin: 0;
    padding: 0;
  }

    .top-image img {
      width: 100%;
      height: 270px;
      object-fit: cover;
      max-width: 100%;
      display: block;
      margin: 0 auto;
    }

  /* Sections Container */
  .sections-container {
    display: flex;
    justify-content: space-between;
    width: 80%;
    margin-top: 20px;
    gap: 20px;
  }

  .left-section {
    flex: 1;
    margin-left: 80px;
  }

  .sheet-card {
    position: relative;
    border: 1px solid #e0e0e0;
    padding: 15px;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
  }

    .sheet-card img {
      width: 100%;
      height: 150px;
      object-fit: cover;
      cursor: pointer;
      border-radius: 5px;
    }

    .sheet-card .overlay {
      position: absolute;
      top: 50%;
      left: 40%;
      transform: translate(-50%, -50%);
      padding: 5px 10px;
      border-radius: 5px;
      opacity: 1;
      color: black;
      font-size: 18px;
      font-weight: bold;
      text-align: center;
    }

    .sheet-card:hover {
      border: 1px solid blue;
    }


  .right-section {
    flex: 1;
    width: 140%; /* Optional: makes it wider but within 80% of its parent container */
    background-color: #fef4d1;
    padding: 12px;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    margin-left: 130px;
  }



  .deadline-section {
    display: flex;
    justify-content: space-between;
    width: 100%;
  }

  .left-info {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  .due-date {
    font-size: 18px;
    font-weight: bold;
    color: black;
    margin-bottom: 40px;
  }

  .buttons {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }

  .upload-button {
    background-color: #f68b1e;
    color: black;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 14px;
    transition: background-color 0.3s;
  }

    .upload-button:hover {
      background-color: #fb6604;
    }

  .re-submit-button {
    background-color: #f68b1e;
    color: black;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 14px;
    transition: background-color 0.3s;
  }

    .re-submit-button:hover {
      background-color: #fb6604;
    }

  .submit-button {
    background-color: #f68b1e;
    color: black;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 14px;
    transition: background-color 0.3s;
  }

    .submit-button:hover {
      background-color: #fb6604;
    }


  .right-info {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-end;
    margin-top: 20px;
  }

  .status {
    font-size: 14px;
    font-weight: bold;
    color: green;
    margin-bottom: 45px;
  }

  .done-button {
    background-color: #3b3b98;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 14px;
    transition: background-color 0.3s;
  }

    .done-button:hover {
      background-color: #f68b1e;
    }
  /* Media Queries */
  /* Media Queries */

  /* Tablet and smaller screens */
  @media (max-width: 768px) {
    /* Adjusting Top Image */
    .top-image img {
      height: 200px;
    }

    /* Adjust Sections Layout */
    .sections-container {
      flex-direction: column;
      align-items: center;
      width: 100%;
      gap: 10px;
    }

    /* Make both sections 100% width */
    .left-section,
    .right-section {
      width: 100%;
      padding: 10px;
      margin-left: 0; /* Remove left margin */
      margin-right: 0; /* Remove right margin */
    }

    /* Adjust Chat Popup */
    .chat-popup {
      width: 280px;
      bottom: 30px;
    }

    /* Chat Input */
    .chat-input input {
      font-size: 0.9em;
    }

    /* Adjust Button Sizes */
    .upload-button,
    .re-submit-button,
    .done-button {
      font-size: 12px;
      padding: 8px 16px;
    }

    .due-date {
      font-size: 16px;
    }
  }

  /* Small screens (mobile) */
  @media (max-width: 480px) {
    /* Further adjustments for smaller screens */
    .top-image img {
      height: 150px;
    }

    .sections-container {
      gap: 5px;
    }

    .sheet-card img {
      height: 120px;
    }

    /* Adjust Font Sizes */
    .overlay-content {
      font-size: 1.2rem;
    }

    .chat-header span {
      font-size: 1.1em;
    }

    .chat-bubble {
      font-size: 0.9em;
    }

    /* Adjust Button Padding */
    .upload-button,
    .re-submit-button,
    .done-button {
      font-size: 11px;
      padding: 6px 12px;
    }
  }

  /* Extra small screens */
  @media (max-width: 320px) {
    /* Additional tweaks for very small screens */
    .top-image img {
      height: 120px;
    }

    .sheet-card img {
      height: 100px;
    }

    .overlay-content {
      font-size: 1rem;
    }

    .chat-header span {
      font-size: 1em;
    }

    .upload-button,
    .re-submit-button,
    .done-button {
      font-size: 10px;
      padding: 5px 10px;
    }
  }

</style>
