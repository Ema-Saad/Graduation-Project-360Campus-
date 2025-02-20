<template>
  <div class="reset-password-page">
    <div class="overlay">
      <img src="@/assets/logo-icon.png" alt="Logo" class="top-left-logo" />
      <div class="content">
        <!-- Illustration Section -->
        <div class="reset-password-illustration">
          <img src="@/assets/ResetPassword.jpg" alt="Reset Password Illustration" />
        </div>

        <!-- Reset Password Form Section -->
        <div class="reset-password-container">
          <div class="welcome-banner">Reset Password</div>

          <h2 class="reset-password-title">Enter New Password</h2>
          <p class="reset-password-text">
            The new password must be different from previously used passwords.
          </p>

          <form @submit.prevent="handleResetPassword" class="reset-password-form">
            <div class="input-group">
              <label for="new-password">New Password</label>
              <div class="input-with-icon">
                <img src="@/assets/lock.png" alt="Lock Icon" class="lock-icon" />
                <input type="password" id="new-password" v-model="newPassword" placeholder="Enter new password" />
              </div>
            </div>
            <div class="input-group">
              <label for="confirm-password">Confirm Password</label>
              <div class="input-with-icon">
                <img src="@/assets/lock.png" alt="Lock Icon" class="lock-icon" />
                <input type="password" id="confirm-password" v-model="confirmPassword" placeholder="Confirm new password" />
              </div>
            </div>
            <button type="submit" class="next-button">Next</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'ResetPasswordPage',
    data() {
      return {
        newPassword: '',
        confirmPassword: '',
      };
    },
    methods: {
      handleResetPassword() {
        if (this.newPassword === this.confirmPassword) {
          // Logic to handle password reset
          this.$router.push({ name: 'DoctorCongratulations' }); // Redirect to Congratulations page
        } else {
          alert('Passwords do not match');
        }
      }

    },
  };
</script>

<style scoped>
  /* Full-page background image */
  .reset-password-page {
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
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .content {
    display: flex;
    width: 80%;
    max-width: 1200px;
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 20px;
    overflow: hidden;
  }

  .reset-password-illustration {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    padding: 40px;
  }

    .reset-password-illustration img {
      max-width: 100%;
    }

  .reset-password-container {
    position: relative;
    flex: 1;
    padding: 60px 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.7);
  }

  .welcome-banner {
    position: absolute;
    top: 20px;
    left: 2px;
    background-color: #201887;
    color: #f76f2a;
    padding: 7px 25px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 18px;
  }

  .reset-password-title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
  }

  .reset-password-text {
    font-size: 14px;
    color: #666;
    text-align: center;
    margin-bottom: 30px;
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

  .input-with-icon {
    display: flex;
    align-items: center;
  }

  .lock-icon {
    width: 20px;
    height: 20px;
    margin-right: 1px;
  }

  .input-with-icon input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: none;
    border-bottom: 2px solid #ccc;
    background-color: transparent;
  }

    .input-with-icon input:focus {
      outline: none;
      border-color: #007bff;
    }

  .next-button {
    background-color: #201887;
    color: #fff;
    border: none;
    padding: 15px 30px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    width: 100%;
    margin-top: 20px;
  }

    .next-button:hover {
      background-color: darkorange;
    }
  /* Media Queries for Responsiveness */
  @media (max-width: 1200px) {
    .content {
      flex-direction: column;
      width: 90%;
      padding: 30px;
    }

    .reset-password-illustration {
      padding: 20px;
    }

    .reset-password-container {
      padding: 40px 30px;
    }

    .reset-password-title {
      font-size: 22px;
    }

    .reset-password-text {
      font-size: 14px;
    }

    .top-left-logo {
      position: absolute;
      top: -10px;
      left: 20px;
      width: 40%; /* Adjust size as needed */
      height: auto;
    }

    .welcome-banner {
      position: absolute;
      top: 5px;
      left: 2px;
      background-color: #201887;
      color: #f76f2a;
      padding: 7px 25px;
      border-radius: 20px;
      font-weight: bold;
      font-size: 18px;
    }

    .next-button {
      padding: 12px 25px;
      font-size: 14px;
    }
  }

  @media (max-width: 768px) {
    .content {
      padding: 20px;
    }

    .reset-password-illustration {
      display: none; /* Hide the illustration on smaller screens */
    }

    .welcome-banner {
      position: absolute;
      top: 5px;
      left: 2px;
      background-color: #201887;
      color: #f76f2a;
      padding: 7px 25px;
      border-radius: 20px;
      font-weight: bold;
      font-size: 18px;
    }

    .reset-password-container {
      padding: 25px 20px;
    }

    .reset-password-title {
      font-size: 20px;
    }

    .reset-password-text {
      font-size: 13px;
    }

    .top-left-logo {
      position: absolute;
      top: -10px;
      left: 20px;
      width: 40%; /* Adjust size as needed */
      height: auto;
    }

    .next-button {
      padding: 10px 20px;
      font-size: 14px;
    }
  }

  @media (max-width: 480px) {
    .content {
      padding: 15px;
    }

    .reset-password-container {
      padding: 20px 15px;
    }

    .reset-password-title {
      font-size: 18px;
    }

    .welcome-banner {
      position: absolute;
      top: 5px;
      left: 2px;
      background-color: #201887;
      color: #f76f2a;
      padding: 7px 25px;
      border-radius: 20px;
      font-weight: bold;
      font-size: 18px;
    }

    .reset-password-text {
      font-size: 12px;
    }

    .top-left-logo {
      position: absolute;
      top: -10px;
      left: 20px;
      width: 30%; /* Adjust size as needed */
      height: auto;
    }

    .next-button {
      padding: 8px 15px;
      font-size: 12px;
    }
  }
</style>
