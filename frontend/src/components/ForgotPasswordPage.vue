<template>
  <div class="forgot-password-page">
    <div class="overlay">
      <div class="content">
        <!-- Illustration Section -->
        <div class="forgot-password-illustration">
          <img src="@/assets/forgetpassword.jpg" alt="Forgot Password Illustration" />
        </div>
        <!-- Forgot Password Form Section -->
        <div class="forgot-password-container">
          <div class="welcome-banner">Forgot Your Password?</div>
          <h2 class="forgot-password-title">Reset Your Password</h2>

          <!-- Instructions text in the center -->
          <p class="forgot-password-text">
            Enter the email address associated with your account.
          </p>

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
      this.$router.push({ name: 'Verification' });
    },
    cancel() {
      this.$router.push({ name: 'Login' }); // Go back to login page
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
    background-color: #1e0a74;
    color: #ffb100;
    padding: 15px 25px;
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
    background-color: #4b0082;
    color: #fff;
    border: none;
    padding: 15px 30px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    width: 48%;
  }

  .cancel-button {
    background-color: #fff;
    color: #4b0082;
    border: 2px solid #4b0082;
  }

    .cancel-button:hover {
      background-color: #f1f1f1;
    }

  .next-button:hover {
    background-color: #5a0092;
  }
</style>
