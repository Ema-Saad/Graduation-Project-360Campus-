<template>
  <div class="error-page">
    <div class="overlay">
      <div class="content">
        <!-- Illustration Section -->
        <div class="error-illustration">
          <img src="@/assets/error-illustration.jpg" alt="Error Illustration" />
        </div>

        <!-- Error Form Section -->
        <div class="error-container">
          <!-- Error Banner -->
          <div class="error-banner">Something is wrong</div>

          <!-- Error Message and Buttons -->
          <h2 class="error-title">Invalid password</h2>
          <p class="error-text">
            New password not accepted. Please try again.
          </p>

          <!-- Action Buttons -->
          <button @click="goResetPassword" class="action-button">Reset Password</button>
          <button @click="goLogin" class="action-button">Login</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ErrorPage',
  methods: {
    goResetPassword() {
      this.$router.push({ name: 'ResetPassword' }); // Navigate to Reset Password page
    },
    goLogin() {
      this.$router.push({ name: 'Login' }); // Navigate to Login page
    }
  }
};
</script>

<style scoped>
  /* Full-page background image */
  .error-page {
    position: relative;
    height: 100vh;
    background: url('@/assets/error-background.jpg') no-repeat center center / cover;
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
    background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent background */
    border-radius: 20px;
    overflow: hidden;
  }

  .error-illustration {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    padding: 40px;
  }

    .error-illustration img {
      max-width: 100%;
    }

  .error-container {
    position: relative;
    flex: 1;
    padding: 60px 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: rgba(255, 255, 255, 0.9);
  }

  .error-banner {
    position: absolute;
    top: 20px;
    left: 20px;
    background-color: #c0392b; /* Red color for error */
    color: white;
    padding: 15px 25px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 18px;
  }

  .error-title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
  }

  .error-text {
    font-size: 16px;
    color: #666;
    margin-bottom: 30px;
    text-align: center;
  }

  .action-button {
    background-color: #e74c3c; /* Red color for the buttons */
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    width: 100%;
    margin-bottom: 15px; /* Space between buttons */
  }

    .action-button:hover {
      background-color: #c0392b;
    }
</style>
