<template>
  <div class="available-time">
    <h2>Choose Your Available Time</h2>
    <div v-for="(slots, day) in schedule" :key="day" class="day-section">
      <h3>{{ day }}</h3>
      <div v-for="slot in slots" :key="slot" class="slot">
        <input type="checkbox"
               :id="`${day}-${slot}`"
               :value="slot"
               v-model="selectedSlots[day]" />
        <label :for="`${day}-${slot}`">{{ slot }}</label>
      </div>
      <hr />
    </div>
    <button class="submit-btn" @click="submitSelection">Submit</button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        schedule: {
          Sunday: ["First Slot", "Second Slot", "Third Slot", "Fourth Slot"],
          Monday: ["First Slot", "Second Slot", "Third Slot", "Fourth Slot"],
          Tuesday: ["First Slot", "Second Slot", "Third Slot", "Fourth Slot"],
          Wednesday: ["First Slot", "Second Slot", "Third Slot", "Fourth Slot"],
          Thursday: ["First Slot", "Second Slot", "Third Slot", "Fourth Slot"],
        },
        selectedSlots: {
          Sunday: [],
          Monday: [],
          Tuesday: [],
          Wednesday: [],
          Thursday: []
        }
      };
    },
    methods: {
      submitSelection() {
        console.log("Selected Slots:", this.selectedSlots);
        alert("Your availability has been submitted successfully!");
      }
    }
  };
</script>

<style scoped>
  .available-time {
    font-family: Arial, sans-serif;
    max-width: 100%;
    margin: 0;
    padding: 20px;
    text-align: center;
  }

  .day-section {
    margin-bottom: 20px;
    text-align: left;
  }

  h3 {
    font-weight: bold;
  }

  .slot {
    display: flex;
    align-items: center;
    margin: 5px 0;
  }

  input[type="checkbox"] {
    margin-right: 10px;
    appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background-color: lightgray;
    display: inline-block;
    position: relative;
    cursor: pointer;
  }

    input[type="checkbox"]:checked {
      background-color: #2d1cc4;
    }

  .submit-btn {
    margin-top: 20px;
    padding: 13px 28px;
    font-size: 16px;
    background-color: #201887;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

    .submit-btn:hover {
      background-color: darkorange;
    }

  hr {
    border: none;
    height: 1px;
    background: #ccc;
  }
  @media (max-width: 768px) {
    .available-time {
      padding: 15px;
    }

    .day-section {
      text-align: center;
    }

    .slot {
      flex-direction: column;
      align-items: center;
    }

    .submit-btn {
      width: 100%;
      padding: 15px;
    }
  }

</style>
