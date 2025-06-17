<template>
  <div class="attendance-system">
    <!-- Header -->
    <header class="header">
      <div class="logo">
        <div>
          <div class="logo-text">Lecture Attendance System</div>
          <div class="logo-subtext">Automated attendance using facial recognition</div>
        </div>
      </div>
      <div class="nav">
        <button class="nav-btn" @click="showRecords">
          View Records
        </button>
        <button class="nav-btn" @click="showSetup">
        take Attendance
        </button>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Setup Form -->
      <div v-if="currentScreen === 'setup'" class="setup-form">
        <h2 class="form-title">Start New Lecture Attendance</h2>

        <div class="form-group">
          <label class="form-label">
            Lecture Number
          </label>
          <input type="text" class="form-input" v-model="lectureNumber" placeholder="e.g., Lecture 5" />
        </div>

        <div class="form-group">
          <label class="form-label">
            Professor Name
          </label>
          <input type="text" class="form-input" v-model="doctorName" placeholder="Your name" />
        </div>

        <div class="form-group">
          <label class="form-label">
            Course Name
          </label>
          <input type="text" class="form-input" v-model="courseName" placeholder="Course title" />
        </div>

        <div class="form-actions">
          <button class="form-btn cancel-btn" @click="resetForm">
            Reset
          </button>
          <button class="form-btn submit-btn" @click="startCamera" :disabled="!canStart">
            Start Attendance
          </button>
        </div>
      </div>

      <!-- Camera View -->
      <div v-if="currentScreen === 'camera'" class="camera-view">
        <div class="camera-header">
          <h2 class="camera-title">{{ courseName }} - Lecture {{ lectureNumber }}</h2>
          <p class="camera-subtitle">Professor: {{ doctorName }}</p>
        </div>

        <div class="camera-container">
          <div class="camera-placeholder">
            <!-- Video feed from webcam -->
            <video ref="videoElement" autoplay playsinline width="640" height="480"></video>
          </div>

          <div v-if="attendanceMessage" class="attendance-confirmation">
            {{ attendanceMessage }}
          </div>

          <div v-if="isPlayingAudio" class="audio-indicator">
            Audio feedback playing...
          </div>
        </div>

        <div class="camera-controls">
          <div class="attendance-count">
            <span class="count">{{ attendanceCount }}</span> students marked present
          </div>
          <button class="stop-btn" @click="stopCamera">
            End Lecture
          </button>
        </div>
      </div>

      <!-- Attendance Records -->
      <div v-if="currentScreen === 'records'" class="records-container">
        <div class="records-header">
          <h2 class="records-title">Attendance Records</h2>
          <div class="records-actions">
            <button class="action-btn" @click="showAddModal = true">
              Add Student
            </button>
            <button class="action-btn export-btn" @click="exportCSV">
              Export CSV
            </button>
          </div>
        </div>

        <table class="attendance-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Timestamp</th>
              <th>Course Name</th>
              <th>Lecture Number</th>
              <th>Professor</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(record, index) in attendanceRecords" :key="index">
              <td>{{ record.id }}</td>
              <td>{{ record.name }}</td>
              <td>{{ record.timestamp }}</td>
              <td>{{ record.course }}</td>
              <td>{{ record.lecture }}</td>
              <td>{{ record.doctor }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>

    <!-- Add Student Modal -->
    <div v-if="showAddModal" class="modal-overlay">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">Add Student Manually</h3>
          <button class="close-btn" @click="showAddModal = false">
            &times; <!-- Added close icon -->
          </button>
        </div>
        <div class="modal-body">
          <div class="form-group" v-for="field in ['id','name','course','lecture','doctor']" :key="field">
            <label class="form-label">{{ field.charAt(0).toUpperCase() + field.slice(1) }}</label>
            <input
              type="text"
              class="form-input"
              v-model="newStudent[field]"
              :placeholder="'Enter ' + field.replace(/([A-Z])/g, ' $1')"
            />
          </div>
        </div>
        <div class="modal-footer">
          <button class="modal-btn modal-cancel-btn" @click="showAddModal = false">
            Cancel
          </button>
          <button class="modal-btn save-btn" @click="addStudentManually">
            Add Student
          </button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
    </footer>

    <!-- Hidden audio element -->
    <audio ref="audioFeedback"></audio>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentScreen: 'setup',
      lectureNumber: '1',
      doctorName: 'Dr. Marghany',
      courseName: 'Machine Learning',
      attendanceMessage: '',
      attendanceCount: 0,
      showAddModal: false,
      isPlayingAudio: false,
      cameraStream: null,
      newStudent: {
        id: '',
        name: '',
        course: '',
        lecture: '',
        doctor: ''
      },
      attendanceRecords: [
      ]
    };
  },
  computed: {
    canStart() {
      return this.lectureNumber && this.doctorName && this.courseName;
    }
  },
  methods: {
    getFormattedTimestamp() {
      const d = new Date();
      const pad = (n) => n.toString().padStart(2, '0');
      return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
    },

    startCamera() {
      if (!this.canStart) {
        alert('Please fill in all fields');
        return;
      }

      this.currentScreen = 'camera';
      this.attendanceCount = 0;
      this.attendanceMessage = '';

      // Access camera
      navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
          this.cameraStream = stream;
          this.$refs.videoElement.srcObject = stream;
        })
        .catch((err) => {
          console.error('Camera access denied:', err);
          alert('Camera access denied. Please allow camera access.');
        });

      this.simulateFaceDetection();
    },

    stopCamera() {
      this.currentScreen = 'setup';
      this.attendanceMessage = '';

      if (this.cameraStream) {
        this.cameraStream.getTracks().forEach(track => track.stop());
        this.cameraStream = null;
      }
    },

    simulateFaceDetection() {
      if (this.currentScreen !== 'camera') return;

      if (Math.random() > 0.7) {
        if (Math.random() > 0.3) {
          const names = ['Sarah Ali', 'Ahmed Hassan', 'Fatima Mahmoud', 'Omar Khalid', 'Layla Mohammed', 'Kareem Ibrahim', 'Nour Salah', 'Amir Zidan', 'Hana Abdelrahman'];
          const name = names[Math.floor(Math.random() * names.length)];

          this.attendanceMessage = `Attendance recorded for ${name}`;
          this.attendanceRecords.unshift({
            id: `32021${Math.floor(1000 + Math.random() * 9000)}`,
            name: name,
            timestamp: this.getFormattedTimestamp(),
            course: this.courseName,
            lecture: this.lectureNumber,
            doctor: this.doctorName
          });

          this.attendanceCount++;
          this.playAudioFeedback(name);

          setTimeout(() => {
            this.attendanceMessage = '';
          }, 3000);
        }
      }

      if (this.currentScreen === 'camera') {
        setTimeout(this.simulateFaceDetection, 2000);
      }
    },

    playAudioFeedback(name) {
      this.isPlayingAudio = true;
      try {
        const utterance = new SpeechSynthesisUtterance(`Attendance recorded for ${name}`);
        speechSynthesis.speak(utterance);
        utterance.onend = () => {
          this.isPlayingAudio = false;
        };
      } catch (e) {
        console.log('Audio feedback error:', e);
        this.isPlayingAudio = false;
      }
    },

    showRecords() {
      this.currentScreen = 'records';
    },

    showSetup() {
      this.currentScreen = 'setup';
    },

    resetForm() {
      this.lectureNumber = '';
      this.doctorName = '';
      this.courseName = '';
    },

    addStudentManually() {
      if (!this.newStudent.id || !this.newStudent.name) {
        alert('Please enter at least ID and Name');
        return;
      }

      this.attendanceRecords.unshift({
        id: this.newStudent.id,
        name: this.newStudent.name,
        timestamp: this.getFormattedTimestamp(),
        course: this.newStudent.course || this.courseName,
        lecture: this.newStudent.lecture || this.lectureNumber,
        doctor: this.newStudent.doctor || this.doctorName
      });
      this.newStudent = { id: '', name: '', course: '', lecture: '', doctor: '' };
      this.showAddModal = false;
    },

    exportCSV() {
      const headers = ['ID', 'Name', 'Timestamp', 'Course Name', 'Lecture Number', 'Professor'];
      const rows = this.attendanceRecords.map(record => [
        record.id, record.name, record.timestamp, record.course, record.lecture, record.doctor
      ]);

      let csvContent = headers.join(',') + '\n';
      rows.forEach(row => {
        csvContent += row.join(',') + '\n';
      });

      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');
      const url = URL.createObjectURL(blob);
      link.setAttribute('href', url);
      link.setAttribute('download', `attendance_${this.courseName || 'all'}_${this.lectureNumber || 'all'}.csv`);
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      alert(`Exported ${this.attendanceRecords.length} records to CSV file`);
    }
  },
  mounted() {
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.currentScreen === 'camera') {
        this.stopCamera();
      }
    });
  }
};
</script>
<style scoped>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
    }
    
    body {
      background: linear-gradient(135deg, #1a0a5e, #2a1680);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }
    
.attendance-system {
  width: 100%;
  max-width: 1200px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  margin: 0 auto; /* this centers the element horizontally */
}

    /* Header Styles */
    .header {
      background: linear-gradient(to right, #1e0a74, #2c1a8c);
      color: white;
      padding: 25px 40px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    
    .logo {
      display: flex;
      align-items: center;
      gap: 15px;
    }
    
    .logo-icon {
      font-size: 32px;
      color: #ffa500;
    }
    
    .logo-text {
      font-size: 26px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }
    
    .logo-subtext {
      font-size: 14px;
      opacity: 0.8;
      margin-top: 5px;
    }
    
    /* Navigation */
    .nav {
      display: flex;
      gap: 15px;
    }
    
    .nav-btn {
      background: darkorange;
      border: none;
      color: white;
      padding: 10px 20px;
      border-radius: 30px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    
    .nav-btn:hover {
  background: #e68816; /* a darker shade of darkorange */
}
    
    /* Main Content */
    .main-content {
      padding: 30px;
      min-height: 500px;
    }
    
    /* Setup Form */
    .setup-form {
      max-width: 600px;
      margin: 0 auto;
      padding: 30px;
      text-align: center;
      background: #f9fafc;
      border-radius: 15px;
      box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    }
    
    .form-title {
      font-size: 28px;
      color: #1e0a74;
      margin-bottom: 30px;
      position: relative;
      padding-bottom: 15px;
    }
    
    .form-title::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 80px;
      height: 4px;
      background: linear-gradient(to right, #201887, #ffa500);
      border-radius: 2px;
    }
    
    .form-group {
      margin-bottom: 25px;
      text-align: left;
    }
    
    .form-label {
      display: block;
      margin-bottom: 10px;
      font-weight: 500;
      color: #2d3748;
      font-size: 17px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .form-input {
      width: 100%;
      padding: 14px 18px;
      border: 2px solid #e2e8f0;
      border-radius: 10px;
      font-size: 16px;
      transition: all 0.3s;
      background: #fff;
    }
    
    .form-input:focus {
      border-color: #201887;
      outline: none;
      box-shadow: 0 0 0 3px rgba(32, 24, 135, 0.2);
    }
    
    .form-actions {
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-top: 30px;
    }
    
    .form-btn {
      padding: 14px 35px;
      border: none;
      border-radius: 50px;
      font-size: 17px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .submit-btn {
      background: #201887;
      color: white;
      box-shadow: 0 4px 15px rgba(32, 24, 135, 0.3);
    }
    
    .submit-btn:hover {
      background: darkorange;
      transform: translateY(-3px);
      box-shadow: 0 7px 20px rgba(255, 140, 0, 0.4);
    }
    
    /* Camera View */
    .camera-view {
      position: relative;
      background: #fff;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .camera-header {
      background: linear-gradient(to right, #1e0a74, #2c1a8c);
      color: white;
      padding: 20px;
      text-align: center;
    }
    
    .camera-title {
      font-size: 24px;
      margin-bottom: 5px;
    }
    
    .camera-subtitle {
      opacity: 0.9;
    }
    
    .camera-container {
      position: relative;
      width: 100%;
      max-width: 800px;
      height: 500px;
      margin: 0 auto;
      background: #000;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    
    .camera-feed {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .camera-placeholder {
      color: white;
      text-align: center;
      padding: 20px;
    }
    
    .camera-icon {
      font-size: 72px;
      margin-bottom: 20px;
      color: #ffa500;
    }
    
    .camera-text {
      font-size: 24px;
      margin-bottom: 15px;
      font-weight: 500;
    }
    
    .camera-hint {
      color: #ccc;
      max-width: 500px;
      margin: 0 auto;
      line-height: 1.6;
    }
    
    .attendance-confirmation {
      position: absolute;
      top: 20px;
      left: 0;
      right: 0;
      text-align: center;
      background: rgba(46, 204, 113, 0.9);
      color: white;
      padding: 15px;
      font-weight: bold;
      font-size: 18px;
      z-index: 10;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .camera-controls {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
      background: #f8fafc;
    }
    
    .attendance-count {
      font-size: 18px;
      font-weight: 500;
      color: #2d3748;
    }
    
    .count {
      font-weight: 700;
      color: #201887;
      font-size: 24px;
    }
    
    .stop-btn {
      background: #201887;
      color: white;
      border: none;
      padding: 14px 35px;
      border-radius: 50px;
      font-size: 17px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 15px rgba(32, 24, 135, 0.3);
    }
    
    .stop-btn:hover {
      background: darkorange;
      transform: translateY(-3px);
      box-shadow: 0 7px 20px rgba(255, 140, 0, 0.4);
    }
    
    /* Audio indicator */
    .audio-indicator {
      position: absolute;
      top: 60px;
      left: 0;
      right: 0;
      text-align: center;
      background: rgba(52, 152, 219, 0.9);
      color: white;
      padding: 10px;
      font-size: 16px;
      z-index: 10;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    
    /* Attendance Records */
    .records-container {
      padding: 30px;
      background: #fff;
      border-radius: 15px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    }
    
    .records-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 25px;
      flex-wrap: wrap;
      gap: 20px;
    }
    
    .records-title {
      font-size: 28px;
      color: #1e0a74;
      position: relative;
      padding-bottom: 10px;
    }
    
    .records-title::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 60px;
      height: 4px;
      background: linear-gradient(to right, #201887, #ffa500);
      border-radius: 2px;
    }
    
    .records-actions {
      display: flex;
      gap: 15px;
    }
    
    .action-btn {
      background: #201887;
      color: white;
      border: none;
      padding: 12px 25px;
      border-radius: 50px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(32, 24, 135, 0.25);
    }
    
    .action-btn:hover {
      background: darkorange;
      transform: translateY(-3px);
      box-shadow: 0 7px 18px rgba(255, 140, 0, 0.35);
    }
    
    .export-btn {
      background: #201887;
    }
    
    .export-btn:hover {
      background: darkorange;
    }
    
    .attendance-table {
      width: 100%;
      border-collapse: collapse;
      box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
      border-radius: 10px;
      overflow: hidden;
    }
    
    .attendance-table th {
      background: #1e0a74;
      color: white;
      text-align: left;
      padding: 16px;
      font-weight: 600;
    }
    
    .attendance-table td {
      padding: 14px;
      border-bottom: 1px solid #edf2f7;
    }
    
    .attendance-table tr:nth-child(even) {
      background-color: #f9fafb;
    }
    
    .attendance-table tr:hover {
      background-color: #f1f8ff;
    }
    
    /* Add Student Modal with scrollable form */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.7);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }
    
    .modal-content {
      background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
      border-radius: 15px;
      width: 90%;
      max-width: 500px;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
      display: flex;
      flex-direction: column;
      max-height: 90vh;
    }
    
    .modal-header {
      padding: 25px;
      background: rgba(0, 0, 0, 0.1);
      text-align: center;
      flex-shrink: 0;
    }
    
    .modal-title {
      font-size: 26px;
      color: white;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
.modal-header {
  padding: 25px;
  background: rgba(0, 0, 0, 0.1);
  text-align: center;
  flex-shrink: 0;
  position: relative; /* Add this to make close-btn position relative to header */
}
.close-btn {
  position: absolute; /* Change from fixed/absolute to relative to modal-header */
  top: 15px; /* Adjust position within header */
  right: 15px; /* Adjust position within header */

  border: none;
  width: 30px; /* Slightly smaller */
  height: 30px; /* Slightly smaller */
  border-radius: 50%;
  color: rgb(0, 0, 0);
  font-size: 20px;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}
    
    .modal-body {
      padding: 25px;
      background: rgba(255, 255, 255, 0.9);
      overflow-y: auto;
      max-height: 60vh;
    }
    
    .modal-footer {
      padding: 20px;
      display: flex;
      justify-content: center;
      gap: 15px;
      background: rgba(0, 0, 0, 0.1);
      flex-shrink: 0;
    }
    
    .modal-btn {
      padding: 12px 30px;
      border: none;
      border-radius: 50px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    
    .save-btn {
      background: #201887;
      color: white;
      box-shadow: 0 4px 15px rgba(32, 24, 135, 0.3);
    }
    
    .save-btn:hover {
      background: darkorange;
      transform: translateY(-3px);
      box-shadow: 0 7px 20px rgba(255, 140, 0, 0.4);
    }
       .action-btn {
      background: #201887;
      color: white;
      border: none;
      padding: 12px 22px;
      border-radius: 50px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(32, 24, 135, 0.25);
    }

    .modal-cancel-btn {
      background: rgba(255, 255, 255, 0.9);
      color: #4a5568;
      padding: 12px 45px;
    }

    .modal-cancel-btn:hover {
      background: darkorange;
      transform: translateY(-3px);
      box-shadow: 0 7px 18px rgba(255, 140, 0, 0.35);
    }
    
    /* Footer */
    .footer {
      background: linear-gradient(to right, #1e0a74, #2c1a8c);
      color: rgba(255, 255, 255, 0.8);
      text-align: center;
      padding: 20px;
      font-size: 14px;
    }
    
    /* Responsive */
    @media (max-width: 900px) {
      .header {
        flex-direction: column;
        gap: 20px;
        text-align: center;
      }
      
      .nav {
        width: 100%;
        justify-content: center;
      }
      
      .camera-container {
        height: 400px;
      }
      
      .records-header {
        flex-direction: column;
        align-items: flex-start;
      }
      
      .records-actions {
        width: 100%;
        justify-content: space-between;
      }
      
      .form-actions {
        flex-direction: column;
        gap: 15px;
      }
      
      .form-btn, .stop-btn, .action-btn {
        width: 100%;
        justify-content: center;
      }
    }
    
    @media (max-width: 600px) {
      .main-content {
        padding: 20px 15px;
      }
      
      .setup-form {
        padding: 20px;
      }
      
      .camera-container {
        height: 350px;
      }
      
      .camera-controls {
        flex-direction: column;
        gap: 20px;
      }
      
      .modal-content {
        width: 95%;
      }
    }
</style>
