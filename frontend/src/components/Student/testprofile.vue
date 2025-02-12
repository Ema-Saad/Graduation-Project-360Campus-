<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100 p-4">
    <div class="profile-container relative w-full max-w-2xl bg-white shadow-lg rounded-2xl border border-gray-300 p-8">

      <!-- Close Button -->
      <button class="close-btn" @click="close">&times;</button>

      <!-- Profile Picture Upload -->
      <div class="flex justify-between items-start">
        <label class="upload-btn cursor-pointer">
          Upload
          <input type="file" @change="uploadImage" class="hidden" />
        </label>
        <div class="flex flex-col items-center">
          <img :src="profilePicture" alt="Profile Picture" class="profile-pic" />
          <p class="text-black font-medium mt-2 text-sm">Profile Picture</p>
        </div>
      </div>

      <!-- Profile Name -->
      <h1 class="text-3xl font-extrabold text-center mt-4">{{ profile.name }}</h1>
      <p class="text-center text-black text-lg font-medium">Profile Name</p>

      <hr class="my-6 border-black" />

      <!-- Details Section -->
      <h2 class="section-title">Details</h2>

      <!-- University Information -->
      <div class="mt-4 text-gray-700">
        <h3 class="section-subtitle">University Information</h3>
        <div class="grid grid-cols-2 gap-y-2">
          <p class="info-label">Student ID:</p>
          <p class="info-value text-blue-600">{{ profile.studentId }}</p>

          <p class="info-label">Full Name (AR):</p>
          <p class="info-value">{{ profile.fullNameAr }}</p>

          <p class="info-label">Full Name (EN):</p>
          <p class="info-value text-blue-600">{{ profile.fullNameEn }}</p>

          <p class="info-label">Nationality:</p>
          <p class="info-value text-blue-600">{{ profile.nationality }}</p>

          <p class="info-label">National ID:</p>
          <p class="info-value">{{ profile.nationalId }}</p>

          <p class="info-label">E-mail:</p>
          <p class="info-value text-blue-600">{{ profile.email }}</p>
        </div>
      </div>

      <!-- Contact Information -->
      <div class="mt-6 text-gray-700">
        <h3 class="section-subtitle">Contact Information</h3>
        <div class="grid grid-cols-2 gap-y-2">
          <p class="info-label">Phone:</p>
          <p class="info-value text-blue-600">{{ profile.phone }}</p>

          <p class="info-label">Address:</p>
          <p class="info-value text-blue-600">{{ profile.address }}</p>

          <p class="info-label">E-mail:</p>
          <p class="info-value text-blue-600">{{ profile.email }}</p>
        </div>
      </div>

      <!-- Basic Information -->
      <div class="mt-6 text-gray-700">
        <h3 class="section-subtitle">Basic Information</h3>
        <div class="grid grid-cols-2 gap-y-2">
          <p class="info-label">Birth Date:</p>
          <p class="info-value text-blue-600">{{ profile.birthDate }}</p>

          <p class="info-label">Gender:</p>
          <p class="info-value text-blue-600">{{ profile.gender }}</p>
        </div>
      </div>

      <hr class="my-6 border-black" />

      <!-- Skills Section -->
      <div class="flex justify-between items-center">
        <button class="add-btn" @click="addSkill">Add</button>
        <h2 class="section-title">Skills</h2>
      </div>

      <ul class="mt-4 list-none text-black font-bold">
        <li v-for="(skill, index) in profile.skills" :key="index" class="mt-1">{{ skill }}</li>
      </ul>

      <!-- Save Button -->
      <button class="save-btn">Save</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfilePage",
  data() {
    return {
      profilePicture: require('@/assets/Edit profile.png'), // Use uploaded image
      profile: {
        name: "Ali Ali",
        studentId: "+121548778511",
        fullNameAr: "علي محمد علي",
        fullNameEn: "Ali Mohamed Ali",
        nationality: "Egyptian",
        nationalId: "30305048754585",
        email: "ali.ali@ejust.edu.eg",
        phone: "+121548778511",
        address: "Alexandria",
        birthDate: "01/05/2003",
        gender: "Male",
        skills: ["UI/UX", "Web - Design", "Coding", "Project Management"],
      },
    };
  },
  methods: {
    uploadImage(event) {
      const file = event.target.files[0];
      if (file) {
        this.profilePicture = URL.createObjectURL(file);
      }
    },
    addSkill() {
      const newSkill = prompt("Enter a new skill:");
      if (newSkill) {
        this.profile.skills.push(newSkill);
      }
    },
    close() {
      alert("Closing profile page...");
    },
  },
};
</script>

<style scoped>
  /* Profile Container */
  .profile-container {
    background: white;
    max-width: 750px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    padding: 25px;
    border: 1px solid #000;
  }

  /* Close Button */
  .close-btn {
    font-size: 24px;
    font-weight: bold;
    position: absolute;
    top: 20px;
    right: 25px;
    cursor: pointer;
  }

    .close-btn:hover {
      color: red;
    }

  /* Profile Picture */
  .profile-pic {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
  }

  /* Upload Button */
  .upload-btn {
    background-color: #1d1b4f;
    color: white;
    padding: 8px 15px;
    border-radius: 8px;
    font-weight: bold;
  }

    .upload-btn:hover {
      background-color: #131236;
    }

  /* Info Labels */
  .info-label {
    font-weight: bold;
    color: black;
  }

  /* Section Titles */
  .section-title {
    font-size: 20px;
    font-weight: bold;
    color: black;
  }

  /* Add Button */
  .add-btn {
    background-color: #1d1b4f;
    color: white;
    padding: 8px 15px;
    border-radius: 8px;
    font-weight: bold;
  }

    .add-btn:hover {
      background-color: #131236;
    }

  /* Save Button */
  .save-btn {
    background-color: #1d1b4f;
    color: white;
    width: 100%;
    padding: 12px;
    border-radius: 8px;
    font-weight: bold;
  }

    .save-btn:hover {
      background-color: #131236;
    }
</style>
