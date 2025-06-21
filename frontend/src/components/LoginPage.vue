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
        async handleLogin() {
          try {
            let result = await this.$root.login(this.username, this.password);
            if (result)
              this.$router.push({ name: 'Home' });
          } catch (err) {
              this.errors = `an Error occured\n${err}`;
          }
        },
    },
};
</script>

<style scoped>
  /* Full-page background image */
/* Full-page layout */
.login-page {
  height: 100vh;
  background: url('@/assets/background.jpg') no-repeat center center / cover;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.top-left-logo {
  position: absolute;
  top: 20px;
  left: 30px;
  width: 140px;
}

.overlay {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-left: 40px; /* shift content slightly to the left */
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.content {
  display: flex;
  width: 70%;
  max-width: 1200px;
  background-color: rgba(255, 255, 255, 0.80);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
  transform: translateX(70%); /* previously -5%, now shifted more */
}

/* Left-side illustration */
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
  height: auto;
}

/* Right-side login form */
.login-container {
  flex: 1;
  padding: 60px 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
}

/* Welcome badge */
.welcome-banner {
  position: absolute;
  top: 25px;
  left: 25px;
  background-color: #201887;
  color: #f76f2a;
  padding: 8px 20px;
  font-weight: 600;
  border-radius: 15px;
  font-size: 16px;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
}

/* Title */
.login-title {
  font-size: 26px;
  font-weight: 700;
  color: #333;
  margin-bottom: 30px;
  text-align: center;
}

/* Form Fields */
.input-group {
  margin-bottom: 20px;
  width: 100%;
}

.input-group label {
  font-size: 14px;
  color: #555;
  margin-bottom: 5px;
  display: block;
}

.input-group input {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: none;
  border-bottom: 2px solid #ccc;
  background-color: transparent;
  transition: border-color 0.3s ease;
}

.input-group input:focus {
  border-color: #201887;
  outline: none;
}

/* Button */
.join-button {
  background-color: #201887;
  color: white;
  padding: 12px 25px;
  border-radius: 10px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  width: 100%;
  transition: background-color 0.3s ease;
  margin-top: 20px;
}

.join-button:hover {
  background-color: #f76f2a;
}

/* Forgot Password */
.forgot-password {
  text-align: center;
  margin-top: 25px;
}

.forgot-password a {
  color: #555;
  text-decoration: underline;
}

.forgot-password a:hover {
  color: #201887;
}

.errorlist {
  margin-top: 15px;
  color: red;
  text-align: center;
  white-space: pre-line;
}

/* Responsive tweaks */
@media (max-width: 1024px) {
  .content {
    flex-direction: column;
    align-items: center;
    width: 90%;
  }
  .login-illustration {
    padding: 20px;
    width: 100%;
  }
  .login-container {
    padding: 40px 30px;
    width: 100%;
  }
}

@media (max-width: 768px) {
  .login-title {
    font-size: 22px;
  }
  .top-left-logo {
    width: 120px;
  }
}

@media (max-width: 480px) {
  .login-title {
    font-size: 20px;
  }
  .login-container {
    padding: 30px 20px;
  }
}


</style>
