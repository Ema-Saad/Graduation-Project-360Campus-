<template>
  <footer class="footer">
    <div class="footer-container">
      <!-- Logo and Title -->
      <div class="footer-logo-section">
        <img src="@/assets/logo-icon.png" alt="Logo" class="footer-logo" />

        <span class="footer-title">360Campus</span>
      </div>
      <!-- Navigation Links -->
      <div class="footer-column">
        <h3 class="footer-heading">Navigation</h3>
        <ul>
          <li><router-link to="/home">Home</router-link></li>
          <li><router-link to="/course/list">Materials</router-link></li>
          <li><router-link to="/classroom/list">My Courses</router-link></li>
          <li><router-link to="/event/list">Events</router-link></li>
        </ul>
      </div>

      <!-- Social Links -->
      <div class="footer-column">
        <h3 class="footer-heading">Social</h3>
        <ul>
          <li><a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a></li>
          <li><a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a></li>
          <li><a href="https://instagram.com" target="_blank" rel="noopener noreferrer">Instagram</a></li>
          <li><a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>

        </ul>
      </div>

      <!-- Work Process Links -->
      <div class="footer-column">
        <h3 class="footer-heading">Work Process</h3>
        <ul>
          <li><a href="#service">Choose The Service You Need</a></li>
          <li><a href="#materials">See List of Materials</a></li>
          <li><a href="#courses">Choose Your Courses</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <span>Copyright © 2025 E-Learning</span>
      <span>Designed by Digital Innovators Team</span>
    </div>
  </footer>
</template>

<script>
  export default {};
</script>
<style>
  body {
    font-family: 'Inknut Antiqua', serif;
  }
  /* Footer Styles */
  .footer {
    background-color: #201887; /* Dark blue background */
    color: white;
    padding: 30px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .footer-container {
    display: flex;
    justify-content: space-around;
    width: 100%;
    max-width: 1200px;
    padding-bottom: 20px;
    border-bottom: 1px solid white;
  }

  .footer-logo-section {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .footer-logo {
    width: 50px;
    height: 50px;
  }

  .footer-title {
    font-size: 24px;
    font-weight: bold;
    color: #ff6a00; /* Orange color for title text */
  }

  .footer-column {
    display: flex;
    flex-direction: column;
  }

  .footer-heading {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .footer-column ul {
    list-style-type: none;
    padding: 0;
  }

  .footer-column li {
    margin: 5px 0;
  }

  .footer-column a {
    color: white;
    text-decoration: none;
    font-size: 16px;
  }

    .footer-column a:hover {
      text-decoration: underline;
    }

  .footer-bottom {
    display: flex;
    justify-content: space-between;
    width: 100%;
    max-width: 1200px;
    padding-top: 15px;
    font-size: 14px;
    color: #ccc; /* Lighter text color */
  }

  /* Footer Styles */
  .footer {
    background-color: #201887; /* Dark blue background */
    color: white;
    padding: 30px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .footer-container {
    display: flex;
    justify-content: space-between;
    width: 100%;
    max-width: 1200px;
    padding-bottom: 20px;
    border-bottom: 1px solid white;
    flex-wrap: wrap; /* Allow items to wrap in smaller screens */
  }

  .footer-logo-section {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-right: 20px; /* Add margin to prevent it from touching other sections */
  }

  .footer-logo {
    width: 120px;
    height: 70px;
  }

  .footer-title {
    font-size: 24px;
    font-weight: bold;
    color: #ff6a00; /* Orange color for title text */
  }

  .footer-column {
    display: flex;
    flex-direction: column;
    margin: 0 15px; /* Add margin for spacing */
  }

  .footer-heading {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .footer-column ul {
    list-style-type: none;
    padding: 0;
  }

  .footer-column li {
    margin: 5px 0;
  }

  .footer-column a {
    color: white;
    text-decoration: none;
    font-size: 16px;
  }

    .footer-column a:hover {
      text-decoration: underline;
    }

  .footer-bottom {
    display: flex;
    justify-content: space-between;
    width: 100%;
    max-width: 1200px;
    padding-top: 15px;
    font-size: 14px;
    color: #ccc; /* Lighter text color */
    margin-top: 20px;
    text-align: center;
  }

    .footer-bottom span {
      margin: 5px 0;
    }

  /* Responsive Styles */
  @media screen and (max-width: 1024px) {
    .footer-container {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .footer-logo-section {
      margin-bottom: 20px;
    }

    .footer-logo {
      width: 40px; /* Adjust logo size for smaller screens */
      height: 40px;
    }

    .footer-title {
      font-size: 20px; /* Adjust title font size for better readability */
    }

    .footer-column {
      margin-bottom: 20px;
    }

    .footer-bottom {
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin-top: 20px;
    }

      .footer-bottom span {
        margin: 5px 0;
      }
  }

  @media screen and (max-width: 768px) {
    .footer-logo-section {
      margin-bottom: 10px;
    }

    .footer-logo {
      width: 35px; /* Adjust logo size for very small screens */
      height: 35px;
    }

    .footer-title {
      font-size: 18px; /* Adjust title font size for mobile screens */
    }

    .footer-column a {
      font-size: 14px; /* Smaller font size for links */
    }

    .footer-bottom {
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin-top: 10px;
    }
  }

  @media screen and (max-width: 480px) {
    .footer-logo {
      width: 30px; /* Further adjust logo size for extra small screens */
      height: 30px;
    }

    .footer-title {
      font-size: 16px; /* Adjust title font size for smaller screens */
    }

    .footer-column a {
      font-size: 12px; /* Further reduce font size for links */
    }

    .footer-bottom {
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin-top: 10px;
    }
  }
</style>



