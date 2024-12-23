<template>
  <div class="error-page">
    <div class="overlay">
      <div class="content">
        <!-- Error Illustration Section -->
        <div class="error-illustration">
          <img src="@/assets/Error.jpg" alt="Error Illustration" />
        </div>

        <!-- Error Form Section -->
        <div class="error-container">
          <!-- Error Banner -->
          <div class="error-banner">Something is wrong</div>

          <p class="error-text">
            Invalid password. New password not accepted. Please try again.
          </p>

          <!-- Action Buttons -->
          <button @click="goResetPassword" class="action-button reset">Reset Password</button>
          <button @click="goLogin" class="action-button login">Login</button>
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
  /* Error Banner */
  .error-banner {
    position: absolute; /* Position it absolutely within the container */
    top: 20px;
    left: 20px; /* Position it in the top left corner */
    background-color: #1e0a74; 
    color: #ffb100;
    padding: 15px 25px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 18px;
    text-align: center; /* Center text */
    width: auto;
  }

  .error-page {
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
    background-color: rgba(0, 0, 0, 0.4); /* Decreased opacity of the overlay */
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .content {
    display: flex;
    width: 80%;
    max-width: 1200px;
    background-color: rgba(255, 255, 255, 0.85); /* Slightly decreased opacity */
    border-radius: 20px;
    overflow: hidden;
  }

  /* Left Section: Error Form */
  .error-container {
    flex: 1;
    padding: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: rgba(255, 255, 255, 0.1); /* Slight opacity decrease */
    position: relative; /* Required for absolute positioning of the banner */
  }

  .error-text {
    font-size: 16px;
    color: #666;
    text-align: center;
    margin-bottom: 30px;
  }

  /* Action Buttons */
  .action-button {
    background-color: #1e0a74; /* Red color for buttons */
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    cursor: pointer;
    width: 100%;
    margin-bottom: 15px; /* Space between buttons */
  }

  .reset {
    font-size: 16px; /* Larger font size for Reset Password */
  }

  .login {
    font-size: 14px; /* Smaller font size for Login */
  }

  .action-button:hover {
    background-color: #c0392b;
  }

  /* Right Section: Error Illustration */
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
      max-height: 100%;
    }
</style>
