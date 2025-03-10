<template>
  <div class="login-page">
    <div class="overlay">
      <img src="@/assets/logo-icon.png" alt="Logo" class="top-left-logo" />

      <div class="content">
        <!-- Illustration Section -->
        <div class="login-illustration">
          <img src="@/assets/login.png" alt="Login Illustration" />
        </div>
        <!-- Login Form Section -->
        <div class="login-container">
          <div class="welcome-banner">Welcome Back</div>
          <h2 class="login-title">Login Your Account</h2>
          <form @submit.prevent="handleLogin" class="login-form">
            <div class="input-group">
              <label for="username">Username/Email</label>
              <input type="text" id="username" v-model="username" placeholder="Username/Email" />
            </div>
            <div class="input-group">
              <label for="password">Password</label>
              <input type="password" id="password" v-model="password" placeholder="Password" />
            </div>
            <button type="submit" class="join-button">Join</button>
          </form>
          <!-- Forgot Password Link -->
          <p class="forgot-password">
            <router-link to="/forgot-password">Forgot Password?</router-link>
          </p>
          <p class="errorlist">
            {{ errors }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { getCurrentInstance } from 'vue';

export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            password: '',
            errors: '',
        };
    },
    methods: {
        handleLogin() {
          this.$root.login(this.username, this.password)
            .then(() => {
              this.$router.push({ name: 'StudentHome' });
            })
            .catch((err) => {
              this.errors = `an Error occured\n${err}`;
            });

        },
    },
};
</script>

<style scoped>
  /* Full-page background image */
  .login-page {
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
    background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent dark overlay */
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .content {
    display: flex;
    width: 70%;
    max-width: 1200px;
    background-color: rgba(255, 255, 255, 0.7); /* Slightly transparent background */
    border-radius: 20px;
    overflow: hidden;
  }

  .login-illustration {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    padding: 40px;
  }

    .login-illustration img {
      max-width: 100%;
    }

  .login-container {
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
    background-color: #201887;
    color: #f76f2a;
    padding: 7px 25px;
    border-radius: 15px;
    font-weight: bold;
    font-size: 18px;
  }

  .login-title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
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

  .join-button {
    background-color: #201887;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    width: 60%;
    margin-top: 15px;
    margin-left: 60px;
  }

    .join-button:hover {
      background-color: darkorange;
    }

  .forgot-password {
    margin-top: 25px;
    font-size: 14px;
    margin-left: 45px;
  }

    .forgot-password a {
      color: #777;
      text-decoration: underline;
    }

      .forgot-password a:hover {
        color: #007bff;
      }
  @media (max-width: 1024px) {
    .overlay {
      padding: 20px;
    }

    .content {
      flex-direction: column;
      width: 100%;
      text-align: center;
      padding: 20px;
    }

    .login-illustration {
      padding: 20px;
      width: 100%;
    }

    .login-container {
      padding: 40px 30px;
      width: 100%;
    }

    .welcome-banner {
      font-size: 16px;
      padding: 8px 15px;
    }

    .login-title {
      font-size: 20px;
      margin-bottom: 15px;
    }

    .input-group {
      margin-bottom: 15px;
    }

    .join-button {
      font-size: 14px;
      padding: 12px 25px;
      width: 100%;
    }

    .top-left-logo {
      width: 15%;
    }
  }

  @media (max-width: 768px) {
    .overlay {
      padding: 3px;
    }
    .login-page {
      padding: 30px;
    }

      .content {
      padding: 20px;
      flex-direction: column;
      align-items: center;
    }

    .login-illustration {
      padding: 5px;
      width: 85%;
    }

      .login-illustration img {
        max-width: 60%;
      }

    .login-container {
      padding: 25px;
      width: 100%;
    }

    .welcome-banner {
      font-size: 14px;
      padding: 6px 10px;
      top: 15px;
    }

    .login-title {
      font-size: 18px;
      margin-bottom: 15px;
    }

    .join-button {
      font-size: 14px;
      padding: 12px 20px;
      width: 100%;
      margin-left: 10px
    }

    .forgot-password {
      margin-left: 10px
    }

    .top-left-logo {
      width: 25%;
    }
  }

  @media (max-width: 480px) {
    .overlay {
      padding: 5px;
    }

    .content {
      padding: 20px;
      flex-direction: column;
      align-items: center;
    }

    .login-illustration {
      padding: 10px;
      width: 100%;
    }

    .login-container {
      padding: 20px;
      width: 100%;
    }

    .welcome-banner {
      font-size: 12px;
      padding: 6px 10px;
      top: 15px;
    }

    .login-title {
      font-size: 16px;
      margin-bottom: 10px;
    }

    .join-button {
      font-size: 12px;
      padding: 10px 15px;
      width: 100%;
    }

    .top-left-logo {
      width: 30%;
    }
  }

</style>
