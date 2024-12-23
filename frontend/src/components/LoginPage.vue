<template>
  <div class="login-page">
    <div class="overlay">
      <div class="content">
        <!-- Illustration Section -->
        <div class="login-illustration">
          <img src="@/assets/login.jpg" alt="Login Illustration" />
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
              this.$router.push({ name: 'Home' });
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
    background-color: #1e0a74;
    color: #ffb100;
    padding: 15px 25px;
    border-radius: 20px;
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
    background-color: #4b0082;
    color: #fff;
    border: none;
    padding: 15px 30px;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    width: 100%;
    margin-top: 20px;
  }

    .join-button:hover {
      background-color: #5a0092;
    }

  .forgot-password {
    margin-top: 15px;
    font-size: 14px;
  }

    .forgot-password a {
      color: #007bff;
      text-decoration: none;
    }

      .forgot-password a:hover {
        text-decoration: underline;
      }
</style>
