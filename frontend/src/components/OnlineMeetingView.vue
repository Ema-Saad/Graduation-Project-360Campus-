<template>
  <div class="meeting-card">
    <div class="left-section">
      <h1 class="meeting-title">Meeting Zoom ID : 607438079 </h1>
    </div>
    <div class="right-section">
      <a href="http://127.0.0.1:3000/" class="join-button">Join</a>
      <p class="start-time">Start in Dec 8, 2024, 11:59 PM</p>
    </div>
  </div>
</template>

<script>

  

  export default {
  };
</script>

<style scoped>
  /* Main container */
  .meeting-card {
    display: flex;
    justify-content: space-between; /* Title and button on opposite ends */
    align-items: flex-start; /* Align both sections to the top */
    padding: 16px;
    width: 100%;
    border-bottom: 1px solid #e2e8f0; /* Light gray border */
  }

  /* Left section for the meeting title */
  .left-section {
    display: flex;
    align-items: center; /* Vertically center the title */
    margin-top: 15px;
  }

  /* Right section containing button and date */
  .right-section {
    display: flex;
    flex-direction: column; /* Stack button and date vertically */
    align-items: flex-end; /* Align items to the right */
    gap: 6px; /* Space between button and date */
    margin-top: 20px; /* Push right-section to the bottom */
  }

  /* Join button styling */
  .join-button {
    background-color: #201887; /* Blue */
    color: white;
    padding: 9px 32px;
    border-radius: 6px;
    border: none;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.3s ease;
    margin-right: 30px;
  }

    .join-button:hover {
      background-color: darkorange; /* Darker blue on hover */
    }

  /* Start time text */
  .start-time {
    font-size: 14px;
    color: #475569; /* Dark gray */
    margin-right: 30px;
  }

  /* Meeting title */
  .meeting-title {
    font-size: 18px;
    font-weight: bold;
    color: #1e293b; /* Dark text */
  }

  /* Media query for smaller screen sizes */
  @media (max-width: 768px) {
    .meeting-card {
      flex-direction: column; /* Stack the left and right sections vertically */
      align-items: flex-start; /* Align all elements to the left */
      padding: 12px; /* Reduce padding on smaller screens */
    }

    .left-section {
      margin-top: 10px; /* Adjust margin to match new layout */
    }

    .right-section {
      align-items: flex-start; /* Align button and time to the left */
      margin-top: 10px; /* Reduce space between button and time */
    }

    .join-button {
      padding: 6px 16px; /* Adjust button padding to be more compact */
      margin-right: 0; /* Remove margin to better fit on small screens */
      font-size: 14px; /* Adjust button font size for readability */
    }

    .start-time {
      font-size: 12px; /* Reduce font size for start time */
      color: #475569; /* Maintain color contrast */
    }

    .meeting-title {
      font-size: 16px; /* Reduce font size for the title */
    }
  }

</style>
