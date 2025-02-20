<template>
  <div class="forgot-password-page">
    <div class="overlay">
      <img src="@/assets/logo-icon.png" alt="Logo" class="top-left-logo" />
      <div class="content">
        <!-- Illustration Section -->
        <div class="forgot-password-illustration">
          <img src="@/assets/forgetpassword.jpg" alt="Forgot Password Illustration" />
        </div>
        <!-- Forgot Password Form Section -->
        <div class="forgot-password-container">
          <div class="welcome-banner">Forgot Your Password?</div>
          <h2 class="forgot-password-title">Enter the email address associated with your account.</h2>

          <form @submit.prevent="handleResetPassword" class="forgot-password-form">
            <div class="input-group">
              <label for="email">Email</label>
              <input type="email" id="email" v-model="email" placeholder="Enter your email" />
            </div>
            <div class="button-group">
              <button type="button" class="cancel-button" @click="cancel">Cancel</button>
              <button type="submit" class="next-button">Next</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ForgotPasswordPage',
  data() {
    return {
      email: '',
    };
  },
  methods: {
    handleResetPassword() {
      // Logic for resetting password
      console.log("Email submitted:", this.email);
      this.$router.push({ name: 'NextStep' }); // Route to the next step or page
    },
    cancel() {
      this.$router.push({ name: 'Login' }); // Go back to login page
    },
    handleResetPassword() {
      // Logic for resetting password (e.g., API call if needed)
      console.log("Email submitted:", this.email);

      // Redirect to the Verification page
      this.$router.push({ name: 'DoctorVerification' });
    },
    cancel() {
      this.$router.push({ name: 'DoctorLogin' }); // Go back to login page
    },
  },
};
</script>

<style scoped>
  .forgot-password-page {
    position: relative;
    height: 100vh;
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
    background-color: rgba(0, 0, 0, 0.7); /* Reduced opacity */
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

  .forgot-password-illustration {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    padding: 40px;
  }

    .forgot-password-illustration img {
      max-width: 100%;
    }

  .forgot-password-container {
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
    left: 1px;
    background-color: #201887;
    color: #f76f2a;
    padding: 7px 25px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 18px;
  }

  .forgot-password-title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
  }

  .forgot-password-text {
    text-align: center;
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
  }

  .input-group {
    margin-bottom: 20px;
    width: 100%;
  }

    .input-group label {
      display: block;
      font-size: 14px;
      color: #666;
      margin-bottom: 5px;
    }

    .input-group input {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: none;
      border-bottom: 2px solid #ccc;
      background-color: transparent;
    }

      .input-group input:focus {
        outline: none;
        border-color: #007bff;
      }

  .button-group {
    display: flex;
    gap: 20px;
    width: 100%;
    margin-top: 20px;
  }

  .cancel-button, .next-button {
    background-color: #201887;
    color: #fff;
    border: none;
    padding: 8px 15px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    width: 48%;
  }

  .cancel-button {
    background-color: white;
    color: #201887;
  }

    .cancel-button:hover, .next-button:hover {
      background-color: darkorange;
    }

  /* Responsive Styles */
  /* Responsive Styles */
  @media screen and (max-width: 1024px) {
    .forgot-password-page {
      padding-top: 40px; /* Adjust top padding */
    }

    .content {
      width: 90%;
      flex-direction: column;
      text-align: center;
      padding: 20px;
    }

    .forgot-password-illustration {
      padding: 20px;
      width: 100%;
      display: flex;
      justify-content: center;
    }

    .forgot-password-container {
      padding: 40px;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    .welcome-banner {
      top: 20px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 16px;
      padding: 10px 20px;
    }

    .forgot-password-title {
      font-size: 20px;
      margin-bottom: 20px;
    }

    .input-group input {
      font-size: 14px;
      padding: 8px;
      width: 100%;
    }

    .button-group {
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 100%;
      align-items: center;
    }

    .cancel-button, .next-button {
      font-size: 14px;
      padding: 12px 24px;
      width: 100%;
    }

    /* Decreased Image Size */
    .forgot-password-illustration img {
      max-width: 80%; /* Decreased image size to 80% */
      height: auto;
      display: block;
      margin: 0 auto;
    }
  }

  @media screen and (max-width: 768px) {
    .forgot-password-page {
      padding-top: 45px;
    }

    .overlay {
      padding: 2px;
    }

    .top-left-logo {
      width: 30%;
    }

    .content {
      width: 95%;
      flex-direction: column;
      align-items: center;
    }

    .forgot-password-illustration {
      width: 90%;
      padding: 15px;
    }

      .forgot-password-illustration img {
        max-width: 50%; /* Decreased image size to 80% */
        height: auto;
        display: block;
        margin: 0 auto;
      }

    .forgot-password-container {
      padding: 30px;
      width: 100%;
    }

    .welcome-banner {
      font-size: 14px;
      top: 15px;
      left: 50%;
      transform: translateX(-50%);
      padding: 8px 16px;
    }

    .forgot-password-title {
      font-size: 20px;
      margin-bottom: 20px;
    }

    .input-group input {
      font-size: 13px;
      padding: 8px;
      width: 100%;
    }

    .button-group {
      display: flex;
      flex-direction: column;
      gap: 15px;
      width: 100%;
      align-items: center;
    }

    .cancel-button, .next-button {
      font-size: 12px;
      padding: 10px 20px;
      width: 100%;
    }
  }

  @media screen and (max-width: 480px) {
    .forgot-password-page {
      padding-top: 30px;
    }

    .overlay {
      padding: 5px;
    }

    .content {
      padding: 20px;
      flex-direction: column;
      align-items: center;
    }


    .forgot-password-container {
      padding: 15px;
      width: 100%;
    }

    .forgot-password-illustration img {
      max-width: 80%; /* Decreased image size to 80% */
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .welcome-banner {
      font-size: 12px;
      top: 10px;
      padding: 8px 16px;
    }

    .forgot-password-title {
      font-size: 18px;
      margin-bottom: 15px;
    }

    .input-group input {
      font-size: 12px;
      padding: 6px;
      width: 100%;
    }

    .button-group {
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 100%;
      align-items: center;
    }

    .cancel-button, .next-button {
      font-size: 12px;
      padding: 8px 16px;
      width: 100%;
    }
  }
</style>
