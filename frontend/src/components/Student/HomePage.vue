<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section" :style="{ backgroundImage: `url(${currentBackground})`, backgroundSize: 'cover', backgroundPosition: 'center center' }">

      <div class="hero-text">
        <h1>Welcome to the Learning Platform</h1>
        <p>Explore our courses and resources to learn and grow.</p>
        <router-link to="/my-courses">
          <button class="explore-btn">Explore Our Courses</button>
        </router-link>
      </div>
    </section>

    <!-- Popup Icon and Window -->
    <!-- Popup Icon (Navigates Directly to Map Page) -->
    <div>
      <div class="popup-icon" @click="goToMapPage">
        <i class="fas fa-map-marker-alt"></i>
      </div>
    </div>

    <!-- Popular Materials Section -->
    <section class="popular-materials-section">
      <div class="popular-materials-header">
        <h1>Our Popular Materials</h1>
        <router-link to="/materials" class="see-more-link">See More...</router-link>
      </div>

      <!-- Course Cards -->
      <div class="card-container">
        <div class="card" v-for="course in courses" :key="course.id">
          <a href="javascript:void(0)" @click.prevent="goToCourseDetails(course.id)" class="card-link">
            <div class="card-image-container">
              <img class="card-img" src="@/assets/pexels-photo.png" alt="Course Image" />
              <div class="overlay-text">
                <h3 class="course-title">{{ course.title }}</h3>
                <p class="course-code">{{ course.code }}</p>
              </div>
            </div>
          </a>
          <!-- Move the instructor info inside the card -->
          <div class="instructor-info">
            <div class="instructor-avatar-container">
              <img class="instructor-avatar" src="@/assets/doctor-img4.png" alt="Instructor Avatar" />
            </div>
            <div>
              <p class="instructor-name">{{ course.instructor }}</p>
              <p class="course-subtitle">{{ course.subtitle }}</p>
            </div>
          </div>
          <!-- Add the "View Class" button under instructor info -->
          <div class="card-content">
            <button class="view-course-btn" @click="goToCourseDetails(course.title)">View Course</button>
          </div>
        </div>
      </div>
    </section>
    <!-- Events Section -->
    <div class="hero-section1">
      <div class="hero-images">
        <div class="hero-image1">
          <img src="@/assets/event2.png" alt="Hero Image 1" class="hero-image" />
        </div>
        <div class="hero-image2">
          <img src="@/assets/event1.png" alt="Hero Image 2" class="hero-image" />
        </div>
      </div>
      <div class="hero-text1">
        <h1 class="events-header">
          <span class="our-text">Our</span>
          <span class="events-text">Events</span>
          <span class="exclamation">!!</span>
        </h1>

        <p class="event-description">
          Stay engaged and be part of our vibrant community through a variety of exciting events!<br>
          From educational workshops to fun social gatherings, there’s something for everyone.<br>
          Whether you're looking to learn something new, connect with peers, or just enjoy a good time.
        </p>
        <button class="hero-button" @click="goToEventsPage">Explore Our Events</button>
      </div>
    </div>

    <!-- My Class Section -->
    <section class="my-class-section">
      <div class="my-class-container">
        <h1 class="my-class-header">My Class</h1>
        <p class="my-class-description">
          Here you can find all the courses you are currently enrolled in. Click on any course card to learn more and access the course materials.
        </p>
        <div class="see-more-container">
          <router-link to="/my-courses" class="see-more-link">See More...</router-link>
        </div>
      </div>

      <!-- My Courses Cards -->
      <div class="card-container">
        <div class="card" v-for="course in courses" :key="course.id">
          <a href="javascript:void(0)" @click.prevent="goToMyCourseDetail(course.id)" class="card-link">
            <div class="card-image-container">
              <img class="card-img" src="@/assets/pexels-photo.png" alt="Course Image" />
              <div class="overlay-text">
                <h3 class="course-title">{{ course.title }}</h3>
                <p class="course-code">{{ course.code }}</p>
              </div>
            </div>
          </a>
          <!-- Instructor info inside the card -->
          <div class="instructor-info">
            <div class="instructor-avatar-container">
              <img class="instructor-avatar" src="@/assets/doctor-img4.png" alt="Instructor Avatar" />
            </div>
            <div>
              <p class="instructor-name">{{ course.instructor }}</p>
              <p class="course-subtitle">{{ course.subtitle }}</p>
            </div>
          </div>

        </div>
      </div>

    </section>
  </div>
</template>

<script>
  import bg1 from '@/assets/pexels-pixabay.jpg'; // Importing the first background image
  import bg2 from '@/assets/background2.jpg';  // Importing the second background image
  import bg3 from '@/assets/background3.jpg';  // Importing the third background image

  export default {
    data() {
      return {
        showPopup: false,
        mobileMenuOpen: false,
        dropdownOpen: false,
        currentBackgroundIndex: 0,
        // Use dynamic URLs from imported images
        backgrounds: [
          bg1,  // First background image
          bg2,  // Second background image
          bg3   // Third background image
        ],
        courses: [
          {
            id: 'csc412',
            title: "Software Security",
            code: "CSC 412",
            instructor: "Dr. Asmaa",
            subtitle: "CSC412: Software Security"
          },
          {
            id: 'csc450',
            title: "Machine Learning",
            code: "CSC 450",
            instructor: "Dr. John",
            subtitle: "CSC450: Machine Learning"
          },
          {
            id: 'csc320',
            title: "Web Development",
            code: "CSC 320",
            instructor: "Dr. Jane",
            subtitle: "CSC320: Web Development"
          }
        ]
      };
    },
    computed: {
      currentBackground() {
        return this.backgrounds[this.currentBackgroundIndex];
      }
    },
    mounted() {
      this.preloadBackgrounds();
      setInterval(this.changeBackground, 4000); // Change background every 4 seconds
    },

    methods: {
      togglePopup() {
        this.showPopup = !this.showPopup;
      },
      goToMapPage() {
        console.log("Navigating to Map Page");
        this.$router.push({ name: 'Map' }); // Navigate directly
      },
      goToEventsPage() {
        console.log("Navigating to Events Page");
        this.$router.push({ name: 'Events' });
      },
      goToCourseDetails(courseId) {
        console.log("Navigating to course details:", courseId);
        this.$router.push({ name: 'CourseDetails', params: { id: courseId } });
      },
      goToMyCourseDetail(courseId) {
        console.log("Navigating to my course details:", courseId);
        this.$router.push({ name: 'MyCourseDetail', params: { id: courseId } });
      },
      toggleMobileMenu() {
        this.mobileMenuOpen = !this.mobileMenuOpen;
      },
      toggleDropdown() {
        this.dropdownOpen = !this.dropdownOpen;
      },
      changeBackground() {
        this.currentBackgroundIndex = (this.currentBackgroundIndex + 1) % this.backgrounds.length;
      },
      preloadBackgrounds() {
        this.backgrounds.forEach((bg) => {
          const img = new Image();
          img.src = bg;
        });
      }
    }
  };
</script>


<style scoped>
  /* Hero Section Styles */
  .hero-section {
    position: relative;
    background-size: cover;
    background-position: center;
    height: 50vh;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding-left: 50px;
    color: white;
    transition: background-image 0.9s ease-in-out;
  }

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

  .hero-text1 {
    max-width: 400px; /* Set max width for readability */
    padding: 20px;
    border-radius: 5px;
  }

    .hero-text1 h1 {
      font-size: 2.5rem; /* Adjust font size */
      text-align: center;
      font-weight: bold;
    }

    .hero-text1 .our-text {
      font-size: 1.5rem; /* Slightly smaller font size for 'Our' */
      color: black; /* 'Our' text in black */
      text-decoration: underline; /* Add underline to 'Our' */
      text-decoration-color: orange; /* Make the underline orange */
    }


    .hero-text1 .events-text {
      font-size: 2.5rem; /* Larger font size for 'Events' */
      color: orange; /* 'Events' text in orange */
    }

    .hero-text1 .exclamation {
      font-size: 2rem;
      color: orange; /* Match the style for exclamation marks */
    }

  .event-description {
    font-size: 1rem;
    margin-top: 15px;
    color: #333; /* Dark text for readability */
  }


  .hero-text p {
    font-size: 1.2em;
    margin-top: 10px;
  }

  .event-description {
    color: black; /* Make the text black */
    font-size: 1.1rem; /* Adjust font size */
    line-height: 1.8; /* Improve line spacing for readability */
    margin-top: 10px; /* Space above the paragraph */
    margin-bottom: 20px; /* Space below the paragraph */
    text-align: left; /* Align the text to the left */
    padding-left: 15px; /* Add some left padding for indentation */
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

  .see-more-container {
    width: 100%;
    display: flex;
    justify-content: flex-end;
  }

  .see-more-link {
    font-size: 1em;
    color: blue;
    text-decoration: none;
    font-weight: bold;
    padding: 5px 10px;
    border-radius: 4px;
    transition: background 0.3s, color 0.3s;
  }

    .see-more-link:hover {
      color: white;
      background-color: #ff6a00;
      text-decoration: none;
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

  .hero-images {
    display: flex;
    justify-content: flex-start; /* Align images to the left */
    gap: 0; /* Remove any space between the images */
  }

  .hero-image1, .hero-image2 {
    width: 300px; /* Set the same width for both images */
    height: 300px; /* Set the same height for both images */
    border-radius: 10px; /* Optional: border-radius for rounded corners */
  }

    .hero-image1 img, .hero-image2 img {
      width: 100%;
      height: 100%;
      object-fit: cover; /* Ensure images maintain their aspect ratio */
    }

  /* First Image */
  .hero-image1 {
    margin-right: 20px; /* Space between the first image and the text */
    position: relative;
    margin-left: -100px; /* Shift the first image more to the left */
  }

  /* Second Image */
  .hero-image2 {
    margin-left: -20px; /* Shift the second image more to the left */
    position: relative;
  }

  .hero-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 400px; /* Set max width for readability */
    padding: 20px;
    border-radius: 5px;
  }

  /* Text Container */
  .hero-text1 {
    margin-left: 60px; /* Create space between the text and the images */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
  }

    .hero-text1 h1 {
      font-size: 2.5em;
      margin: 0;
      margin-left: 10px; /* Shift the header to the right */
    }


    .hero-text1 p {
      max-width: 400px; /* Optional: control the width */
      word-wrap: break-word; /* Ensure long words break into the next line */
      line-height: 1.6; /* Increase line height for better readability */
      font-size: 1.2em;
      margin-top: 10px;
    }

  /* Button Styles */
  .hero-button {
    background-color: #201887; /* Button background color */
    color: white; /* Button text color */
    border: none; /* Remove border */
    padding: 10px 20px; /* Padding for button */
    font-size: 1em; /* Button font size */
    border-radius: 5px; /* Rounded corners */
    cursor: pointer; /* Pointer cursor on hover */
    margin-top: 15px; /* Space above the button */
    margin-left: 15px; /* Shift the button to the right */
    transition: background-color 0.3s ease; /* Transition for hover effect */
  }

    .hero-button:hover {
      background-color: darkorange; /* Darker color on hover */
    }

  .events-header {
    color: #1e0a74; /* Dark blue color */
  }

  .explore-btn {
    background-color: #201887;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    margin-top: 15px; /* Space between description and button */
    display: inline-block; /* Makes the button inline so margin-left works */
    position: relative; /* Allow for positioning adjustments */
  }

    .explore-btn:hover {
      background-color: darkorange;
    }

  /* Instructor Info Styles */
  .instructor-info {
    display: flex; /* Align the image and text side by side */
    align-items: center; /* Vertically center the content */
    justify-content: flex-start; /* Align items to the left */
    gap: 15px; /* Space between the image and the text */
    padding: 10px 0; /* Add padding to separate from other elements */
    margin-right: 90px; /* Ensure the container starts from the left edge */
  }

  /* Avatar container to handle background gradient */
  .instructor-avatar-container {
    width: 50px; /* Fixed width */
    height: 50px; /* Fixed height */
    border-radius: 50%; /* Circular shape */
    background: linear-gradient(to bottom, #f08a24, #3b3b98);
    display: flex; /* Center the image inside the container */
    justify-content: center; /* Center the image horizontally */
    align-items: center; /* Center the image vertically */
  }

  /* Avatar image inside the container */
  .instructor-avatar {
    width: 45px; /* Slightly smaller width to fit inside the container */
    height: 45px; /* Slightly smaller height to fit inside the container */
    border-radius: 50%; /* Keep image circular */
    object-fit: cover; /* Ensure image covers the circle area */
  }

  .instructor-info div {
    display: flex;
    flex-direction: column; /* Stack the instructor name and course subtitle vertically */
  }

  .instructor-name {
    font-size: 1.1em; /* Slightly larger font size for the instructor's name */
    font-weight: bold; /* Make the instructor's name bold */
    color: #333; /* Dark gray color for the name */
  }


  .course-subtitle {
    font-size: 1em; /* Regular font size for the subtitle */
    color: #777; /* Lighter gray color for the subtitle */
    margin-top: 5px; /* Space between the instructor name and subtitle */
  }

  /* My Class Section Styles */
  .my-class-section {
    background-color: #f5f5f5; /* Light gray background */
    padding: 30px 20px;
  }

  .my-class-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .my-class-header {
    font-size: 2em;
    color: #1e0a74;
    margin: 0;
  }

    .my-class-header h1 {
      font-size: 2em;
      color: #1e0a74; /* Dark blue color for header */
      margin: 0;
    }

  .my-class-description::after {
    content: "";
    display: block;
    width: 130px; /* Small width */
    height: 2px; /* Very thin line */
    background-color: #ff6a00; /* Line color */
    margin: 7px auto 0; /* Space between text and line, centered */
  }

  .see-more-container {
    width: 100%;
    display: flex;
    justify-content: flex-end;
  }

  .see-more-link {
    font-size: 1em;
    color: blue;
    text-decoration: none;
    font-weight: bold;
    padding: 5px 10px;
    border-radius: 4px;
    transition: background 0.3s, color 0.3s;
  }

    .see-more-link:hover {
      color: white;
      background-color: darkorange;
      text-decoration: none;
    }

  .card {
    position: relative;
    margin: 10px;
    border: 1px solid #ccc; /* Default gray border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Ensure content stays within bounds */
    cursor: pointer; /* Make the card clickable */
  }

    .card:hover {
      border: 1px solid blue; /* Blue border on hover */
    }

  .card-link {
    display: block; /* Make the link fill the entire card */
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

  /* Card Container */
  .card-container {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin: 20px;
  }

  /* Card Styles */
  .card {
    position: relative;
    margin: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    overflow: hidden;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  /* Card Image Container with Overlay */
  .card-image-container {
    position: relative;
    overflow: hidden;
  }

  /* Overlay Text Style */
  .overlay-text {
    position: absolute;
    top: 50%;
    left: 30%;
    transform: translate(-50%, -50%); /* Center the overlay text */
    color: black;
    text-align: center;
    z-index: 1;
    padding: 10px;
    border-radius: 5px; /* Optional: Add rounded corners to the overlay */
  }

  .course-title {
    font-size: 1.5em;
    font-weight: bold;
    margin-bottom: 5px; /* Space between title and code */
  }

  .course-code {
    font-size: 1.2em;
    font-weight: normal;
  }

  /* Card Content */
  .card-content {
    padding: 15px;
  }

  /* Card Title */
  .card-title {
    font-size: 1.5em;
    margin-bottom: 10px;
  }

  /* Card Description */
  .card-description {
    font-size: 1.2em;
    margin-bottom: 20px;
  }

  .view-course-btn {
    background-color: #201887;
    color: white;
    padding: 9px 35px;
    border-radius: 5px;
    border: none; /* Remove border */
    font-size: 1em; /* Button font size */
    cursor: pointer;
    margin-top: -100px; /* Shift the button upwards */
  }

    .view-course-btn:hover {
      background-color: darkorange;
    }
  .popup-icon {
    position: fixed;
    top: 58%; /* You can adjust this to place the icon where you want it */
    right: 20px; /* Distance from the right edge of the screen */
    cursor: pointer;
    font-size: 29px;
    color: black;
    background: #fe6805; /* Initial Orange */
    padding: 10px;
    border-radius: 50%; /* Circular shape */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Shadow for the icon */
    transition: all 0.3s ease; /* Smooth transition for hover effects */
    display: flex;
    align-items: center;
    justify-content: center;
    width: 35px;
    height: 35px;
    z-index: 1000; /* Ensures it stays on top of other elements */
  }

/* Hover Effect */
.popup-icon:hover {
    background: radial-gradient(circle, #3234A9 40%, rgba(50, 52, 169, 0.5) 70%, rgba(50, 52, 169, 0.1) 100%);
    color: black; /* Change icon color */
    transform: scale(1.1) translateY(-3px);
    box-shadow: 0 0 20px rgba(50, 52, 169, 0.6);
}


    /* Click Effect */
    .popup-icon:active {
      transform: scale(0.95); /* Slight shrink effect when clicked */
    }

  .popup-window {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .popup-content {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }

  /* Responsive Layout for Cards */
  /* Responsive Layout for Cards */
  @media screen and (max-width: 768px) {
    /* Hero Section Layout */
    .hero-section1 {
      height: auto; /* Allow height to adjust for smaller screens */
      padding: 20px; /* Add padding */
      flex-direction: column; /* Stack images and text vertically */
      justify-content: center; /* Center content vertically */
      text-align: center; /* Center text */
    }

    .hero-images {
      display: flex;
      flex-direction: column; /* Stack images vertically */
      align-items: center; /* Center images */
      gap: 10px; /* Add space between images */
    }

    .hero-image1 {
      width: 100%; /* Make image take full width */
      height: auto; /* Maintain aspect ratio */
      transform: translateX(13%); /* Shift Image 1 to the right by 10% */
    }

    .hero-image2 {
      width: 100%; /* Make image take full width */
      height: auto; /* Maintain aspect ratio */
    }

    .hero-text1 {
      margin-left: 0; /* Remove left margin for text */
      margin-top: 20px; /* Add space above the text */
      align-items: center; /* Center the text */
      padding: 0 20px; /* Add padding */
    }

    .events-header h1 {
      font-size: 2rem; /* Adjust font size for smaller screens */
    }

    .event-description {
      font-size: 1.1rem; /* Adjust font size for readability */
      line-height: 1.6; /* Increase line height */
      margin-top: 15px; /* Space between the text and the button */
    }

    .hero-button {
      width: 100%; /* Make the button full width on small screens */
      margin-top: 20px; /* Add space above the button */
    }

    /* Card Container */
    .card-container {
      flex-direction: column; /* Stack cards vertically */
      align-items: center; /* Center cards */
    }

    .card {
      width: 100%; /* Make each card take full width */
      margin-bottom: 20px; /* Add margin between cards */
    }

    /* Popup Icon Styles */
    .popup-icon {
      position: fixed; /* Keep the icon fixed in the viewport */
      bottom: 20px; /* Position from the bottom */
      right: 20px; /* Position from the right */
      z-index: 1000; /* Ensure it stays on top */
      cursor: pointer; /* Indicate it is clickable */
      border-radius: 50%; /* Circular icon */
      padding: 10px; /* Increase padding for easier tapping */
      width: 35px; /* Icon size */
      height: 35px; /* Icon size */
      transition: background-color 0.3s ease, transform 0.3s ease; /* Smooth transition */
    }

      /* Popup Icon Hover Styles */
      .popup-icon:hover {
        background-color: blue; /* Change background color on hover */
        transform: scale(1.1); /* Slight scale effect on hover */
      }

      /* Icon Image Styles */
      .popup-icon img {
        width: 100%; /* Ensure image fills the icon size */
        height: 100%; /* Ensure image fills the icon size */
        transition: filter 0.3s ease; /* Smooth transition for image effect */
      }

      .popup-icon:hover img {
        filter: brightness(8) invert(1); /* Change icon image color on hover */
      }

    /* Popup Window Styles */
    .popup-window {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px; /* Add padding around popup */
    }

    .popup-content {
      background-color: white;
      padding: 20px;
      border-radius: 10px;
      text-align: center;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
      max-width: 90%; /* Limit the width of the popup */
      width: auto; /* Allow auto-width */
      box-sizing: border-box; /* Include padding in width calculation */
    }

      /* Popup Button Styles */
      .popup-content button {
        background-color: #F17E0B;
        color: white;
        border: none;
        padding: 10px 20px;
        margin-top: 10px;
        cursor: pointer;
        border-radius: 5px;
        width: 100%; /* Make button fill the popup */
      }

        .popup-content button:hover {
          background-color: orange;
        }
  }


</style>


