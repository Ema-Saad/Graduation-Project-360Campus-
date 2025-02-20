<template>
  <div class="verification-page">
    <div class="overlay">
      <img src="@/assets/logo-icon.png" alt="Logo" class="top-left-logo" />
      <div class="content">
        <!-- Illustration Section -->
        <div class="verification-illustration">
          <img src="@/assets/verification.jpg" alt="Verification Illustration" />
        </div>

        <!-- Verification Form Section -->
        <div class="verification-container">
          <h2 class="verification-title">Verification</h2>
          <p class="verification-text">
            Enter the verification code we just sent to your email address
          </p>

          <!-- Code Input Section -->
          <div class="code-inputs">
            <input type="text" maxlength="1" v-model="code[0]" @input="focusNext(0)" ref="code0" />
            <input type="text" maxlength="1" v-model="code[1]" @input="focusNext(1)" ref="code1" />
            <input type="text" maxlength="1" v-model="code[2]" @input="focusNext(2)" ref="code2" />
            <input type="text" maxlength="1" v-model="code[3]" @input="focusNext(3)" ref="code3" />
          </div>

          <!-- Next and Resend Buttons -->
          <button class="next-button" @click="handleVerification">Next</button>
          <p class="resend-code">
            <a href="#" @click.prevent="resendCode">Resend Code</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'VerificationPage',
    data() {
      return {
        code: ['', '', '', ''],
      };
    },
    methods: {
      handleVerification() {
        // Redirect to ResetPassword page upon successful verification
        this.$router.push({ name: 'DoctorResetPassword' });
      },
      focusNext(index) {
        // Automatically move to the next input when one character is entered
        if (this.code[index].length === 1 && index < this.code.length - 1) {
          this.$refs[`code${index + 1}`].focus();
        } else if (this.code[index] === '' && index > 0) {
          this.$refs[`code${index - 1}`].focus();
        }
      },
      resendCode() {
        // Logic to resend the verification code
        alert("Verification code resent!");
      },
    },
  };
</script>

<style scoped>
  .verification-page {
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
    max-width: 1100px;
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 20px;
    overflow: hidden;
  }

  .verification-illustration {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    padding: 40px;
  }

    .verification-illustration img {
      max-width: 100%;
    }

  .verification-container {
    flex: 1;
    padding: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.9);
  }

  .verification-title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 40px;
  }

  .verification-text {
    font-size: 16px;
    color: #555;
    text-align: center;
    margin-bottom: 20px;
  }

  .code-inputs {
    display: flex;
    gap: 10px;
    margin-bottom: -50px;
  }

    .code-inputs input {
      width: 50px;
      height: 50px;
      font-size: 24px;
      text-align: center;
      border: 2px solid #ccc;
      border-radius: 8px;
    }

  .next-button {
    background-color: #201887;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    width: 100%;
    margin-top: 140px;
  }

    .next-button:hover {
      background-color: darkorange;
    }

  .resend-code {
    margin-top: 25px;
    font-size: 14px;
  }

    .resend-code a {
      color: #777;
      text-decoration: underline;
    }

      .resend-code a:hover {
        color: #007bff;
      }

  @media (max-width: 1024px) {
    .content {
      width: 90%;
      max-width: 800px;
      flex-direction: column;
      align-items: center;
      padding: 30px;
    }

    .verification-illustration {
      width: 100%;
      padding: 20px;
    }

    .verification-container {
      width: 100%;
      padding: 30px;
    }

    .verification-title {
      font-size: 22px;
    }

    .verification-text {
      font-size: 15px;
      margin-bottom: 15px;
    }

    .code-inputs {
      gap: 8px;
      margin-bottom: 20px;
    }

      .code-inputs input {
        width: 45px;
        height: 45px;
        font-size: 22px;
      }

    .next-button {
      font-size: 16px;
      padding: 12px;
    }

    .resend-code {
      font-size: 14px;
    }
  }

  @media (max-width: 600px) {
    .verification-page {
      padding: 100px;
    }

    .top-left-logo {
      position: absolute;
      top: -10px;
      left: 20px;
      width: 30%; /* Adjust size as needed */
      height: auto;
    }

    .overlay {
      padding: 10px;
    }

    .content {
      padding: 15px;
      flex-direction: column;
      align-items: center;
    }

    .verification-illustration {
      padding: 10px;
    }

      .verification-illustration img {
        max-width: 60%;
      }

    .verification-container {
      padding: 15px;
    }

    .verification-title {
      font-size: 20px;
    }

    .verification-text {
      font-size: 14px;
    }

    .code-inputs input {
      width: 40px;
      height: 40px;
      font-size: 20px;
    }

    .next-button {
      padding: 10px 20px;
      font-size: 14px;
    }

    .resend-code a {
      font-size: 13px;
    }
  }
</style>
