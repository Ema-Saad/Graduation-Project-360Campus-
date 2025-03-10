<template>
  <div class="events-page" v-for="event in events">
    <div class="images-container">
      <img src="@/assets/event3.png" alt="Event Image 1" class="image image1" />
      <img src="@/assets/event4.png" alt="Event Image 2" class="image image2" />
      <img src="@/assets/event1.png" alt="Event Image 3" class="image image3" />
      <img src="@/assets/event2.png" alt="Event Image 4" class="image image4" />
    </div>

    <div class="event-details">
      <h2>{{ event.title }}</h2>
      <p>
        {{ event.description }}
      </p>
      <div class="event-info">
        <p><span class="icon">🕒</span>{{ event.date }} </p>
        <p><span class="icon">📍</span> HQ Professor Abo Ismail Theater</p>
      </div>
      <button :class="enrollButtonClass" @click="openModal">{{ enrollButtonText }}</button>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal">
        <button class="close-button" @click="closeModal">×</button>
        <h2>AI for Good Summit 2024 Event</h2>
        <form class="modal-form" @submit.prevent="confirmEnrollment">
          <input type="text" placeholder="Enter your Name..." required />
          <input type="email" placeholder="Enter your Email..." required />
          <button type="submit" class="confirmation-button">Confirmation</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    beforeMount() {
      let events = this.$root.request_api_endpoint('api/events', 'get', null);
      
      events.then((data) => {
        this.events = data;
      });

    },
    data() {
      return {
        showModal: false,
        enrollmentConfirmed: false, // Tracks if the user has confirmed their enrollment
        events: [],
      };
    },
    computed: {
      enrollButtonClass() {
        // Change the button's style dynamically
        return this.enrollmentConfirmed ? "enroll-button confirmed" : "enroll-button";
      },
      enrollButtonText() {
        // Change the button's text dynamically
        return this.enrollmentConfirmed ? "Enrolled!" : "Enroll";
      },
    },
    methods: {
      openModal() {
        this.showModal = true;
      },
      closeModal() {
        this.showModal = false;
      },
      confirmEnrollment() {
        this.enrollmentConfirmed = true; // Mark the enrollment as confirmed
        this.closeModal(); // Close the modal
      },
    },
  };
</script>

<style scoped>
  /* Main Container */
  .events-page {
    display: flex;
    align-items: flex-start;
    padding: 20px;
    font-family: Arial, sans-serif;
  }

  /* Overlapping Images */
  .images-container {
    position: relative;
    flex: 1;
    max-width: 50%;
    height: 400px;
  }

  .image {
    position: absolute;
    border-radius: 5px;
    object-fit: cover;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  }

  /* Image Overlapping Positions */
  .image1 {
    width: 300px;
    height: 190px;
    top: 20px;
    left: 302px;
    z-index: 4;
  }

  .image2 {
    width: 300px;
    height: 190px;
    top: 20px;
    left: 10px;
    z-index: 3;
  }

  .image3 {
    width: 293px;
    height: 200px;
    top: 210px;
    left: 10px;
    z-index: 2;
  }

  .image4 {
    width: 310px;
    height: 210px;
    top: 200px;
    left: 290px;
    z-index: 1;
  }

  /* Event Details Section */
  .event-details {
    flex: 1;
    padding: 20px;
  }

    .event-details h2 {
      font-size: 1.8rem;
      font-weight: bold;
      margin-bottom: 1rem;
    }

    .event-details p {
      line-height: 1.6;
      font-size: 1rem;
      margin-bottom: 1rem;
    }

  .event-info {
    margin-bottom: 20px;
  }

    .event-info p {
      display: flex;
      align-items: center;
      font-size: 0.9rem;
      margin: 5px 0;
    }

  .icon {
    margin-right: 10px;
    font-size: 1.2rem;
  }

  /* Enroll Button Styles */
  .enroll-button {
    padding: 10px 20px;
    background-color: #201887;
    color: white;
    width: 95px;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: transform 0.3s, background-color 0.3s;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  }

    .enroll-button:hover {
      background-color: #f6790f;
    }

    /* Confirmed Enroll Button Styles */
    .enroll-button.confirmed {
      background-color: #32cd32; /* Green to indicate success */
      cursor: not-allowed; /* Prevent further clicks */
    }

  /* Modal Styles */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  .modal {
    background: linear-gradient(to bottom, #4b0082, #f8c471);
    border-radius: 10px;
    padding: 30px;
    text-align: center;
    width: 400px;
    position: relative;
    color: white;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }

  .close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: transparent;
    border: none;
    font-size: 1.5rem;
    color: white;
    cursor: pointer;
  }

  .modal h2 {
    font-size: 1.5rem;
    margin-bottom: 20px;
  }

  .modal-form input {
    width: 100%;
    padding: 12px;
    margin: 10px 0;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    color: #333;
  }

    .modal-form input::placeholder {
      color: #aaa;
    }

  .confirmation-button {
    padding: 10px 20px;
    background-color: #4b0082;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s;
  }

    .confirmation-button:hover {
      background-color: #3a0069;
    }

  /* Responsive Styles */
  /* Responsive Styles */
  @media screen and (max-width: 1024px) {
    .events-page {
      flex-direction: column;
      align-items: center;
      padding: 20px;
    }

    .images-container {
      max-width: 80%;
      height: auto;
      margin-bottom: 20px;
    }

    .image {
      position: static;
      width: 100%;
      max-width: 300px;
      height: auto;
      margin: 10px;
    }

    .event-details {
      text-align: center;
    }

    .enroll-button {
      width: 100%;
    }
  }

  @media screen and (max-width: 768px) {
    .images-container {
      max-width: 100%;
      text-align: center;
    }

    .image {
      max-width: 250px;
      margin: 5px;
    }

    .event-details {
      padding: 15px;
    }

      .event-details h2 {
        font-size: 1.5rem;
      }

      .event-details p {
        font-size: 0.9rem;
      }

    .modal {
      width: 90%;
      padding: 20px;
    }

    .modal-form input {
      font-size: 0.9rem;
      padding: 10px;
    }
  }

  @media screen and (max-width: 480px) {
    .events-page {
      padding: 10px;
    }

    .images-container {
      max-width: 100%;
    }

    .image {
      max-width: 200px;
    }

    .event-details h2 {
      font-size: 1.3rem;
    }

    .event-details p {
      font-size: 0.85rem;
    }

    .modal {
      width: 95%;
      padding: 15px;
    }

    .confirmation-button {
      width: 100%;
      padding: 10px;
      font-size: 0.9rem;
    }
  }


</style>
