<template>
  <div v-if="assignment && assignment.classroom" class="assignment-detail">
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
          <router-link :to="{ name: 'ClassroomView', params: { courseId: assignment.classroom.course.id } }">
            {{ assignment.classroom.course.title }}
          </router-link>
          <br />
          <span v-if="!showTitleControls">
            {{ assignment.title }} 
          </span>

          <span v-if="$root.person_kind === 'P'">
            <button
              v-if="!showTitleControls"
              @click="showTitleControls = true; copy = {...assignment}"
            >
              Edit
            </button>
           <span v-else>
  <input v-model="assignment.title" type="text" />
  <button class="save-button" @click="showTitleControls = false">Save</button>
  <button class="cancel-button" @click="assignment = {...copy}; copy = null; showTitleControls = false">Cancel</button>
</span>
          </span>
          <br />
          Taught by {{ assignment.classroom.instructor.first_name }} {{ assignment.classroom.instructor.last_name }}
        </div>
      </div>
    </div>

    <div class="sections-container">
      <div class="left-section">
  <p v-if="!showDescriptionTextbox">
    {{ this.assignment.description }}
  </p>

  <span v-if="$root.person_kind === 'P'">
    <button
      v-if="!showDescriptionTextbox"
      @click="showDescriptionTextbox = true; copy = {...assignment}"
    > 
      Edit
    </button>
    <span v-else>
      <textarea v-if="showDescriptionTextbox" v-model="assignment.description"></textarea>

      <button class="save-button" @click="showDescriptionTextbox = false">
        Save
      </button>

      <button class="cancel-button" @click="assignment = {...copy}; copy = null; showDescriptionTextbox = false">
        Cancel
      </button>
    </span>
  </span>
</div>
      <!-- Right Section -->
      <div class="right-section">
        <div class="deadline-section">
          <div class="left-info">
            <p
              v-if="!showDeadlineControls"
              class="due-date"
            >
              {{ computeDueString(assignment.deadline) }}
            </p>
            <span v-if="$root.person_kind === 'P'">
              <button
                v-if="!showDeadlineControls"
                @click="copy = {...assignment}; showDeadlineControls = true"
              >
                Edit
              </button>
            <span v-else>
  <input ref="deadlineControl" type="datetime-local" />
  <button class="save-button" 
    @click="assignment.deadline = new Date($refs.deadlineControl.value); showDeadlineControls = false">
    Save
  </button>
  <button class="cancel-button" @click="assignment = {...copy}; copy = null; showDeadlineControls = false">
    Cancel
  </button>
</span>
            </span>

            <div v-if="$root.person_kind === 'S' && (!assignment.deadline || assignment.deadline > Date.now())" class="buttons">
              <input type="file" id="file-input" style="display:none;" @change="handleFileUpload" />
              <button @click="triggerFileInput" class="upload-button">Upload your Work</button>
              <button v-if="!assignment.submitted" @click="submit" class="submit-button">Submit</button>
              <button v-else @click="unsubmit" class="re-submit-button">Unsubmit</button>
            </div>

          </div>

          <div v-if="$root.person_kind === 'S'" class="right-info">
            <span> {{ assignment.grade ?? "???" }} / {{ assignment.max_grade }} </span>
            <span v-if="assignment.deadline">
              <span v-if="assignment.submitted" class="status-assigned">Submitted</span>
              <span v-else-if="assignment.deadline > Date.now()" class="status-assigned">Assigned</span>
              <span v-else class="status-missed">Missed</span>
            </span>
            <div v-if="uploadedFileName" class="uploaded-file">
              <p>Uploaded File: {{ uploadedFileName }}</p>
            </div>
          </div>
          <div v-else>
            <span v-if="!showMaxGradeControls"> 
              Grade: {{ assignment.max_grade }} 
       <button @click="copy = {...assignment}; showMaxGradeControls = true">
                Edit
              </button>
            </span>
       <span v-else>
  <input type="number" v-model="assignment.max_grade" />
  <button class="save-button" @click="showMaxGradeControls = false">
    Save
  </button>
  <button class="cancel-button" @click="assignment = {...copy}; copy = null; showMaxGradeControls = false">
    Cancel
  </button>
</span>
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
        <div v-for="(message, index) in chatMessages"
            :key="index"
            class="chat-message"
            :class="message.sender === 'me' ? 'my-message' : 'their-message'">
          <div class="message-info">
            <img v-if="message.sender === 'them'" src="@/assets/chaticon.png" alt="Person Icon" class="person-icon" />
            <img v-if="message.sender === 'me'" src="@/assets/chaticon2.png" alt="Your Icon" class="person-icon" />
            <span class="sender-name">{{ message.sender === 'me' ? 'You' : 'csit_csc_prof1' }}</span>
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

  import { useGlobalStore } from '@/global_store.js'

  export default {
    data() {
      return {
        assignment: null,
        copy: null,
        selectedFile: null,  // Store the selected file
        uploaded: false,  // Track upload status
        uploadedFileName: "",  // Store the name of the uploaded file
        grade: null,
        showDescriptionTextbox: false,
              showChat: false,
      chatMessages: [
        { sender: "them", text: "Hi there! How can I help you with this assignment?" }
      ],
      newMessage: "",
        showTitleControls: false,
        showDeadlineControls: false,
        showMaxGradeControls: false,
      };
    },
    props: ['assignmentId'],
    async beforeRouteEnter(to, from, next) {
      const store = useGlobalStore()

      let assignment = await store.request_api_endpoint(`api/assignment/${to.params.assignmentId}`)
      assignment = {...assignment, deadline: assignment.time ? new Date(assignment.time) : null }
      let submission = !assignment.submitted ? 
        null : await store.request_api_endpoint(`api/assignment/${to.params.assignmentId}/submission`)

      next(vm => {
        vm.setAssignment(assignment, submission)
      });
    },
    async beforeRouteLeave(to, from) {
      if (this.$root.person_kind !== 'P') {
        return true 
      }
      try {
        const store = useGlobalStore()
        let assignment = {
          title: this.assignment.title,
          description: this.assignment.description,
          time: this.assignment.deadline,
          max_grade: this.assignment.max_grade,
        }
        await store.request_api_endpoint(
          `api/assignment/${this.assignment.id}/modify`,
          'post',
          JSON.stringify(assignment),
          { 'Content-Type': 'application/json' },
        )
      } catch (err) {
        return false;
      }

    },
    methods: {
      setAssignment(assignment, submission = null) {
        this.assignment = assignment
        if (submission) {
          this.uploadedFileName = submission.submitted_file
          this.grade = submission.grade
        }
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
      computeDueString(date) {
        const MILLISECONDS_IN_DAY = 24 * 60 * 60 * 1000;
        const DAYS = [
          "Sunday", "Monday", "Tuesday", 
          "Wednesday", "Thursday", "Friday", "Saturday"
        ];
        const MONTHS = [
          "Jan", "Feb", "Mar", "Apr",
          "May", "Jun", "Jul", "Aug",
          "Sep", "Oct", "Nov", "Dec",
        ];

        if (!date) {
          return "No Due Date";
        }

        let hour = `${date.getHours().toString().padStart(2, "0")}:${date.getMinutes().toString().padStart(2, "0")}`;
        if (Date.now() > date) {
          return `Was Due ${MONTHS[date.getMonth()]}. ${date.getDate().toString().padStart(2, "0")} ${date.getYear()} at ${hour}`;

        } else if (date - Date.now() <= MILLISECONDS_IN_DAY) {
          return `Due Today at ${hour}`;

        } else if (date - Date.now() <= 2 * MILLISECONDS_IN_DAY) {
          return `Due Tomorrow at ${hour}`;

        } else if (date - Date.now() <= 7 * MILLISECONDS_IN_DAY) {
          return `Due ${DAYS[date.getDay()]} at ${hour}`;
        } else {
          return `Due ${MONTHS[date.getMonth()]}. ${date.getDate().toString().padStart(2, "0")} at ${hour}`;
        }

      },
      // Trigger the hidden file input element to open the file dialog
      triggerFileInput() {
        document.getElementById("file-input").click();  // Click the hidden input
      },

      async submit() {
        const store = useGlobalStore()
        if (!this.selectedFile) return;

        let data = new FormData();
        data.append('file', this.selectedFile);

        let submit = await store.request_api_endpoint(`api/assignment/${this.assignmentId}/submit/${this.selectedFile.name}`, 'post', data);
        this.assignment = await store.request_api_endpoint(`api/assignment/${this.assignmentId}`)
        this.assignment.deadline = this.assignment.deadline ? new Date(this.assignment.deadline) : null
      },

      unsubmit() {
        let unsubmit_promise = this.$root.request_api_endpoint(`api/assignment/${this.assignmentId}/unsubmit`, 'post', null);

        unsubmit_promise
          .then((_) => this.$root.request_api_endpoint(`api/assignment/${this.assignmentId}`, 'get', null))
          .then((data) => {
            this.assignment = {...data, deadline: data.deadline ? new Date(data.deadline) : null };
          });

        this.selectedFile = this.uploadedFileName = null;
      },

      // Handle the file upload and store the selected file's name
      handleFileUpload(event) {
        this.selectedFile = event.target.files[0];  // Get the first selected file
        if (this.selectedFile) {
          this.uploadedFileName = this.selectedFile.name;  // Set the uploaded file name
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
    background-color: #f7c974;
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

.right-section {
  flex: 1;
  background-color: #f7c974;
  padding: 12px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin-left: auto; /* This pushes the section to the right */
  width: 40%; /* Adjust width as needed */
  max-width: 500px; /* Optional: set a max-width */
  position: sticky;
  top: 20px; /* Keeps it visible when scrolling */
  align-self: flex-start; /* Aligns to top of container */
}

.sections-container {
  display: flex;
  justify-content: space-between;
  width: 90%;
  margin: 20px auto;
  gap: 20px;
}
  .right-info {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-end;
    margin-top: 20px;
  }

  .status-assigned {
    font-size: 14px;
    font-weight: bold;
    color: green;
    margin-bottom: 45px;
  }

  .status-missed {
    font-size: 14px;
    font-weight: bold;
    color: red;
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
  .chat-input button {
  background-color: #201887; /* Default color */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.chat-input button:hover {
  background-color: darkorange; /* Hover color */
  transform: scale(1.1); /* Optional scaling effect on hover */
}


.overlay-content > span > button,
.overlay-content > span > span > button {
  padding: 6px 12px;
  margin-right: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  margin-bottom: 12px;
}

.overlay-content > span > button,
.overlay-content > span > span > button:nth-child(1) {
  background-color: navy;
  color: white;
}

.overlay-content > span > span > button:nth-child(2) {
  background-color: gray;
  color: white;
}

.overlay-content > span > button:hover,
.overlay-content > span > span > button:nth-child(1):hover {
  background-color: darkorange;
}

.overlay-content > span > span > button:nth-child(2):hover {
  background-color: darkorange;
}
.overlay-content > span > button,
.overlay-content > span > span > button {
  padding: 6px 12px;
  margin-right: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  color: white;
}

.overlay-content > span > span > button.save-button {
  background-color: navy;
   width: 250px;
}
.overlay-content > span > button{
    background-color: navy;
    margin-left: 10px;
    border-radius: 8px;
    padding: 6px 25px;
}

.overlay-content > span > span > button.save-button:hover {
  background-color: darkorange;
}

.overlay-content > span > span > button.cancel-button {
  background-color: rgb(159, 154, 154);
   width: 250px;
}

.overlay-content > span > span > button.cancel-button:hover {
  background-color: darkorange;
}

.overlay-content > span > span > input[type="text"] {
  padding: 6px 30px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
  margin-bottom: 8px;
  font-size: 14px;      
  font-weight: 600;     
  min-width: 200px;  
  box-sizing: border-box;
}

.left-section button {
  padding: 6px 12px;
  margin-right: 8px;
  margin-bottom: 12px;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  color: white;
}

.left-section .save-button {
  background-color: navy;
  width: 80px;
    padding: 7px 125px;
}

.left-section .save-button:hover {
  background-color: darkorange;
}

.left-section .cancel-button {
  background-color: rgb(159, 154, 154);
  width: 80px;
  padding: 7px 125px;
}

.left-section .cancel-button:hover {
  background-color: darkorange;
}
.left-section textarea {
  padding: 6px 12px;
  font-size: 14px;
  font-weight: 600;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
  margin-bottom: 8px;
  width: 250px;
  resize: vertical;
  box-sizing: border-box;
}
.left-section > span > button {
  background-color: navy;
  color: white;
  padding: 6px 25px;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 12px;
}

.left-section > span > button:hover {
  background-color: darkorange;
}

.right-section button,
span > button {
  padding: 6px 12px;
  margin-right: 8px;
  margin-bottom: 12px;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  color: white;
}
span > button:not(.save-button):not(.cancel-button),
.right-section > div > div > span > button {
  background-color: navy;
}

span > button:not(.save-button):not(.cancel-button):hover,
.right-section > div > div > span > button:hover {
  background-color: darkorange;
}

.save-button {
  background-color: navy;
  width: 80px;
}

.save-button:hover {
  background-color: darkorange;
}

.cancel-button {
  background-color: rgb(159, 154, 154);
  width: 90px;
}

.cancel-button:hover {
  background-color: darkorange;
}
.right-section input[type="datetime-local"] {
  padding: 6px 10px;
  font-size: 14px;
  font-weight: 600;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
  margin-bottom: 8px;
  width: 250px;
  box-sizing: border-box;
}

span > button:not(.save-button):not(.cancel-button) {
  background-color: navy;
  color: white;
  padding: 6px 12px;
  margin-left: 8px;
  margin-bottom: 12px;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}

span > button:not(.save-button):not(.cancel-button):hover {
  background-color: darkorange;
}

.right-section .save-button {
  background-color: navy;
  color: white;
  width: 80px;
  padding: 6px 60px;
  margin-right: 8px;
  margin-bottom: 12px;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}

.right-section .save-button:hover {
  background-color: darkorange;
}

.right-section .cancel-button {
  background-color: rgb(159, 154, 154);
  color: white;
  width: 90px;
  padding: 6px 60px;
  margin-bottom: 12px;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}

.right-section .cancel-button:hover {
  background-color: darkorange;
}

input[type="number"] {
  padding: 6px 12px;
  font-size: 14px;
  font-weight: 600;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
  margin-bottom: 8px;
  width: 120px;
  box-sizing: border-box;
}

.buttons > .upload-button,
.buttons > .submit-button {
  background-color: orange;
  color: rgb(0, 0, 0);
  padding: 8px 12px;
  margin-right: 10px;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}

.buttons > .upload-button:hover,
.buttons > .submit-button:hover {
  background-color: darkorange;
}
.left-section > span > button,
.right-section > div > div > span > button,
span > button:not(.save-button):not(.cancel-button) {
  padding: 6px 30px;
}
.chat-icon {
  position: fixed;
  bottom: 340px;
  right: 20px;
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
  bottom: 80px;
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
.close-button:hover,
.close-button:focus,
.close-button:active {
  background: none;
  outline: none;
  box-shadow: none;
  transform: scale(1.2);
}

@media (max-width: 768px) {
  .chat-popup {
    width: 300px;
    height: 400px;
    bottom: 70px;
  }
  
  .chat-icon {
    width: 45px;
    height: 45px;
    font-size: 1.4em;
  }
}

@media (max-width: 480px) {
  .chat-popup {
    width: 280px;
    height: 380px;
    right: 10px;
  }
  
  .chat-icon {
    width: 40px;
    height: 40px;
    font-size: 1.2em;
    right: 15px;
  }
}

  /* Tablet and smaller screens */
  @media (max-width: 768px) {
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
