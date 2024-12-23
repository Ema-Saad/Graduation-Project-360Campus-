<template>
  <div class="congratulations-page">
    <div class="overlay">
      <div class="content">
        <!-- Illustration Section -->
        <div class="congratulations-illustration">
          <img src="@/assets/Congratulations.jpg" alt="Congratulations Illustration" />
        </div>

        <!-- Congratulations Form Section -->
        <div class="congratulations-container">
          <div class="welcome-banner">Congratulations</div>
          <h2 class="congratulations-title">The operation was successful</h2>
          <p class="congratulations-text">
            The new password has been accepted and enjoy our website <strong>Campus-360 Student</strong>.
          </p>
          <button @click="goHome" class="home-button">Go to Home Page</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'CongratulationsPage',
    methods: {
      goHome() {
        this.$router.push({ name: 'Home' }); // Redirect to the home page
      },
    },
  };
</script>

<style scoped>
  /* Full-page background image */
  .congratulations-page {
    position: relative;
    height: 100vh;
    background: url('@/assets/background.jpg') no-repeat center center / cover;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* Semi-transparent dark overlay */
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .content {
    display: flex;
    width: 80%;
    max-width: 1200px;
    background-color: rgba(255, 255, 255, 0.7); /* Slightly transparent background */
    border-radius: 20px;
    overflow: hidden;
  }

  .congratulations-illustration {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    padding: 40px;
  }

    .congratulations-illustration img {
      max-width: 100%;
    }

  .congratulations-container {
    position: relative;
    flex: 1;
    padding: 60px 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: rgba(255, 255, 255, 0.7);
  }

  .welcome-banner {
    position: absolute;
    top: 20px;
    left: 2px;
    background-color: #1e0a74;
    color: #ffb100;
    padding: 15px 25px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 18px;
  }

  .congratulations-title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
  }

  .congratulations-text {
    font-size: 16px;
    color: #666;
    margin-bottom: 30px;
    text-align: center;
  }

  .home-button {
    background-color: #4b0082;
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    width: 100%;
  }

    .home-button:hover {
      background-color: #5a0092;
    }
</style>
