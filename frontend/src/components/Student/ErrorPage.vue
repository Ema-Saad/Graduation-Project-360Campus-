<template>
  <div class="error-page">
    <div class="overlay">
      <img src="@/assets/logo-icon.png" alt="Logo" class="top-left-logo" />
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
    left: 0px; /* Position it in the top left corner */
    background-color: #201887;
    color: #f76f2a;
    padding: 7px 25px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 18px;
    text-align: center; /* Center text */
    width: auto;
  }

  .error-page {
    position: relative;
    min-height: 100vh; /* Ensure it takes the full viewport height */
    background: url('@/assets/background.jpg') no-repeat center center / cover;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .top-left-logo {
    position: absolute;
    top: -10px;
    left: 20px;
    width: 20%; /* Adjust size as needed */
    height: auto;
  }
  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* Decreased opacity of the overlay */
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .content {
    display: flex;
    width: 80%;
    max-width: 1200px;
    background-color: rgba(255, 255, 255, 0.7); /* Slightly decreased opacity */
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
    background-color: #201887; /* Red color for buttons */
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
    background-color: darkorange;
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

  /* Responsive Styles */
  /* Responsive Styles */
  @media screen and (max-width: 1024px) {
    .content {
      width: 90%;
      flex-direction: column;
      text-align: center;
    }

    .error-illustration {
      padding: 20px;
    }

    .error-container {
      padding: 30px;
    }

    .error-banner {
      top: 5px;
      left: 20px;
      font-size: 16px;
      padding: 10px 20px;
    }

    .action-button {
      font-size: 14px;
      padding: 10px 20px;
    }

    /* Increase Logo Size */
    .top-left-logo {
      width: 40%; /* Increase size for medium screens */
    }
  }

  @media screen and (max-width: 768px) {
    .error-page {
      height: auto;
      padding: 20px;
    }

    .content {
      width: 95%;
    }

    .error-illustration img {
      max-width: 80%;
    }

    .error-text {
      font-size: 14px;
    }

    .error-banner {
      font-size: 14px;
    }

    .action-button {
      font-size: 12px;
      padding: 8px 16px;
    }

    /* Increase Logo Size */
    .top-left-logo {
      width: 30%; /* Increase size for smaller screens */
    }
  }

  @media screen and (max-width: 480px) {
    .content {
      width: 100%;
      padding: 20px;
    }

    .error-container {
      padding: 20px;
    }

    .error-illustration img {
      max-width: 100%;
    }

    .error-text {
      font-size: 12px;
    }

    .error-banner {
      font-size: 12px;
      top: 5px;
      padding: 8px 16px;
    }

    .action-button {
      font-size: 12px;
      padding: 6px 12px;
    }

    /* Increase Logo Size */
    .top-left-logo {
      width: 40%; /* Even larger logo for very small screens */
    }
  }

  
  
</style>
