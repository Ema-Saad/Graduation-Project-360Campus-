<template>
  <dialog ref="dialog">
    <form method="dialog" @submit="submit">
      <label for="title"> Title </label>
      <input type="text" id="title" v-model="online_meeting.title" />

      <label for="description"> Description </label>
      <textarea id="description" v-model="online_meeting.description"></textarea>

      <label for="time"> Time </label>
      <input type="datetime-local" v-model="online_meeting.time" />

      <input type="submit" value="Create" />
      <button @click.prevent="$refs.dialog.close()">Cancel</button>
    </form>
  </dialog>
</template>


<script>
  export default {
    props: ['course_id'],
    data() {
      return {
        online_meeting: {
          title: "",
          description: "",
          time: null,
        }
      };
    },

    mounted() {
      this.$refs.dialog.showModal();
    },

    methods: {
      async submit(evt) {
        try {
          await this.$root.request_api_endpoint(
            `api/course/${this.course_id}/classroom/online-meeting/add`,
            'post',
            JSON.stringify(this.online_meeting),
            { 'Content-Type': 'application/json' }
          );
        } catch (err) {

        }
      }
    }
  }
</script>

<style scoped>
dialog {
  position: relative;
  padding: 25px 30px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
  color: white;
  width: 450px;
  max-width: 95%;
  font-family: Arial, sans-serif;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

form {
  display: flex;
  flex-direction: column;
}

dialog label {
  margin-top: 10px;
  font-weight: bold;
}

dialog input,
dialog textarea {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border-radius: 6px;
  border: none;
  font-size: 1em;
}

dialog textarea {
  resize: vertical;
  min-height: 80px;
}

dialog input[type="submit"],
dialog button {
  width: 100%;
  padding: 12px;
  margin-top: 15px;
  font-size: 1em;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

/* Submit button */
dialog input[type="submit"] {
  background-color: #1a237e;
  color: white;
}

dialog input[type="submit"]:hover {
  background-color: darkorange;
}

/* Cancel button */
dialog button:not(.close-button) {
  background-color: rgb(169, 165, 165);
  color: white;
}

dialog button:not(.close-button):hover {
  background-color: darkorange;
}

</style>
