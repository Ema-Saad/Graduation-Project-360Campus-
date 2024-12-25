<template>
  <div>
 
    <!-- Hero Section with Background Image and Text Overlay -->
    <section class="hero-section">
      <div class="hero-text">
        <h1>Welcome to the Learning Platform</h1>
        <p>Explore our courses and resources to learn and grow.</p>
        <button class="explore-btn" @click="goTo('explore')">Explore Our Courses</button>
      </div>
    </section>


    <!-- Cards Section with 3 cards beside each other -->
    <!-- Our Popular Materials Section -->
    <section class="popular-materials-section">
      <div class="popular-materials-header">
        <h1>Our Popular Materials</h1>
        <a href="#see-more" class="see-more-link">See More</a>
      </div>

      <!-- Card Container -->
      <div class="card-container">
        <div class="card" v-for="i in 3" :key="i">

          <img class="card-img" src="@/assets/pexels-pixabay.jpg" alt="Course Image" />

          <div class="card-content">
            <h2 class="card-title">Course Title {{ i }}</h2>
            <p class="card-description">
              This is a brief description of the course. Learn more about the course content, objectives, and what you will achieve by the end of the course.
            </p>
            <button class="download-btn">View Course</button>
          </div>
        </div>
      </div>
    </section>
    <div class="hero-section1">
      <div class="hero-image1">
        <img src="@/assets/pexels-pixabay.jpg" alt="Hero Image" class="hero-image">

      </div>
      <div class="hero-text1">
        <h1>Our Events</h1>
        <p>Your subtitle or description here.</p>
        <button class="hero-button">Explore Our Events</button>
      </div>
    </div>



    <!-- Cards Section with 3 cards beside each other -->
    <!-- Our Popular Materials Section -->
    <section class="my-class-section">
      <div class="my-class-header">
        <h1>My Class</h1>
        <a href="#see-more" class="see-more-link">See More</a>
      </div>

      <!-- Added description below the header -->
      <p class="my-class-description">
        Here you can find all the courses you are currently enrolled in. Click on any course card to learn more and access the course materials.
      </p>

      <!-- Card Container -->
      <div class="card-container">
        <div class="card" v-for="i in 3" :key="i">
          <a href="#course-{{ i }}" class="card-link">
            <!-- Make the card clickable -->
            <img class="card-img" src="@/assets/pexels-pixabay.jpg" alt="Course Image" />
            <div class="card-content">
              <h2 class="card-title">Course Title {{ i }}</h2>
              <p class="card-description">
                This is a brief description of the course. Learn more about the course content, objectives, and what you will achieve by the end of the course.
              </p>
            </div>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        searchQuery: '', // Keep this if you have a search input on the homepage
        mobileMenuOpen: false, // Remove if not needed
        dropdownOpen: false // Remove if not needed
      };
    },
    beforeCreate() {
      if (!this.$root.authtoken) {
        this.$router.replace({ name: 'Login' })
      }

    },
    methods: {
      goTo(target) {
        // Simulate navigation, replace with actual routing later if needed
        alert(`Navigating to ${target}`);
      },
      // You can keep these methods if they are relevant to other parts of the homepage
      toggleMobileMenu() {
        this.mobileMenuOpen = !this.mobileMenuOpen;
      },
      toggleDropdown() {
        this.dropdownOpen = !this.dropdownOpen;
      }
    }
  };

</script>

<style scoped>
  /* Hero Section Styles */
  .hero-section {
    position: relative;
    background-image: url('../src/assets/pexels-pixabay.jpg');
    background-size: cover;
    background-position: center;
    height: 50vh; /* Adjust height as needed */
    display: flex;
    align-items: center;
    justify-content: flex-start; /* Align content to the left */
    padding-left: 50px; /* Add left padding */
    color: white;
  }

  .hero-text {
    max-width: 400px; /* Set max width for readability */

    padding: 20px;
    border-radius: 5px;
  }

    .hero-text h1 {
      font-size: 2.5em;
      margin: 0;
    }

    .hero-text p {
      font-size: 1.2em;
      margin-top: 10px;
    }

  /* Our Popular Materials Section Styles */
  .popular-materials-section {
    background-color: #f5f5f5; /* Light gray background */
    padding: 30px 20px;
  }

  .popular-materials-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

    .popular-materials-header h1 {
      font-size: 2em;
      color: #1e0a74; /* Dark blue color for header */
      margin: 0;
    }

  .see-more-link {
    font-size: 1em;
    color: #ff6a00; /* Orange color for link */
    text-decoration: none;
    font-weight: bold;
  }

    .see-more-link:hover {
      text-decoration: underline;
    }

  /* Hero Section Styles */
  .hero-section1 {
    position: relative;
    background: linear-gradient(to right, #F17E0B -50%, #FFF8DF 100%, #F17E0B 100%);
    background-attachment: fixed; /* Fix background so it doesn't scroll */
    height: 50vh; /* Adjust height as needed */
    display: flex;
    align-items: center; /* Center items vertically */
    justify-content: center; /* Center items horizontally */
    color: white;
    padding: 20px; /* Add padding around the content */
    text-align: center; /* Center-align text */
  }

  .hero-image1 {
    width: 50%; /* Adjust width as needed */
    max-width: 300px; /* Optional: set a max width for the image */
    margin-right: 20px; /* Space between image and text */
  }

    .hero-image1 img {
      width: 100%; /* Make image responsive */
      height: auto; /* Maintain aspect ratio */
      border-radius: 10px; /* Optional: round the corners of the image */
    }

  .hero-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 400px; /* Set max width for readability */
    padding: 20px;
    border-radius: 5px;
  }

  .hero-text1 {
    text-align: center; /* Center-align text */
    color: black;
  }

    .hero-text1 h1 {
      font-size: 2.5em;
      margin: 0;
    }

    .hero-text1 p {
      font-size: 1.2em;
      margin-top: 10px;
    }

  /* Button Styles */
  .hero-button {
    background-color: blue; /* Button background color */
    color: white; /* Button text color */
    border: none; /* Remove border */
    padding: 10px 20px; /* Padding for button */
    font-size: 1em; /* Button font size */
    border-radius: 5px; /* Rounded corners */
    cursor: pointer; /* Pointer cursor on hover */
    margin-top: 15px; /* Space above the button */
    transition: background-color 0.3s ease; /* Transition for hover effect */
  }

    .hero-button:hover {
      background-color: orange; /* Darker color on hover */
    }

  .explore-btn {
    background-color: #F17E0B; /* Button color */
    color: white; /* Button text color */
    border: none; /* Remove default border */
    padding: 10px 20px; /* Padding for the button */
    font-size: 1em; /* Font size */
    cursor: pointer; /* Pointer cursor on hover */
    border-radius: 5px; /* Rounded corners */
    margin-top: 10px; /* Space between button and text */
  }

    .explore-btn:hover {
      background-color: #ff6a00; /* Darken button on hover */
    }

  /* My Class Section Styles */
  .my-class-section {
    background-color: #f5f5f5; /* Light gray background */
    padding: 30px 20px;
  }

  .my-class-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

    .my-class-header h1 {
      font-size: 2em;
      color: #1e0a74; /* Dark blue color for header */
      margin: 0;
    }

  .my-class-description {
    font-size: 1.1em; /* Adjust font size as needed */
    color: #333; /* Dark gray color for text */
    margin: 10px 0 20px; /* Margin for spacing */
  }

  .see-more-link {
    font-size: 1em;
    color: #ff6a00; /* Orange color for link */
    text-decoration: none;
    font-weight: bold;
  }

    .see-more-link:hover {
      text-decoration: underline;
    }

  .card {
    position: relative;
    margin: 10px;
    border: 1px solid #ccc; /* Optional: Add a border */
    border-radius: 8px; /* Optional: Add rounded corners */
    overflow: hidden; /* Ensure content stays within bounds */
  }

  .card-link {
    display: block; /* Make the link fill the card */
    text-decoration: none; /* Remove underline from link */
    color: inherit; /* Inherit color from card content */
  }

  .card-img {
    width: 100%; /* Make image responsive */
    height: auto; /* Maintain aspect ratio */
  }

  .card-content {
    padding: 15px; /* Add padding inside card */
  }



  .explore-btn {
    background-color: darkblue;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    margin-top: 15px; /* Space between description and button */
  }

    .explore-btn:hover {
      background-color: orange;
    }

  /* Card Styles */
  .card-container {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin: 20px;
  }

  .card {
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 10px;
    overflow: hidden;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .card-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  .card-content {
    text-align: center;
    padding: 10px;
  }

  .card-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .card-description {
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
  }

  .download-btn {
    background-color: darkblue;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
  }

    .download-btn:hover {
      background-color: orange;
    }

  /* Responsive Layout for Cards */
  @media screen and (max-width: 768px) {
    .card-container {
      flex-direction: column;
      align-items: center;
    }

    .card {
      width: 100%;
      margin-bottom: 20px;
    }
  }

</style>


