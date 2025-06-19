<template>
  <dialog ref="dialog" class="styled-dialog">
    <form method="dialog" @submit="submit">
      <label for="title">Title</label>
<input v-model="assignment.title" id="title" type="text" placeholder="Title" />

      <br />

      <label for="description"> Description </label>
      <textarea v-model="assignment.description" id="description">
        Brief Description of the Assignment
      </textarea>
      <br />

      <label for="max_grade"> Maximum Grade </label>
      <input v-model="assignment.max_grade" id="max_grade" type="number" />
      <br />

      <label for="deadline"> Deadline </label>
      <input v-model="assignment.deadline" id="deadline" type="date" />
      <br />

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
        assignment: {
          title: "",
          description: "",
          max_grade: 0,
          deadline: null,
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
            `api/course/${this.course_id}/classroom/assignments/add`,
            'post',
            JSON.stringify(this.assignment),
            { 'Content-Type': 'application/json' },
          );

        } catch (err) {
          console.log(err);

        }
      }
    },
  }

</script>
<style scoped>
.styled-dialog {
  padding: 24px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
  color: white;
  width: 550px; /* Dialog slightly larger */
  max-width: 95%;
  font-family: sans-serif;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.styled-dialog form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.styled-dialog form input[type="text"],
.styled-dialog form input[type="number"],
.styled-dialog form input[type="date"],
.styled-dialog form textarea {
  width: 100%;
  padding: 6px 10px;
  font-size: 14px;
  border-radius: 5px;
  border: none;
}

/* Submit button (Create) */
dialog input[type="submit"] {
  width: 100%;
  padding: 12px;
  margin-top: 15px;
  font-size: 1em;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  background-color: navy;
  color: white;
  transition: background-color 0.3s ease;
}

dialog input[type="submit"]:hover {
  background-color: darkorange;
}

/* Cancel button */
dialog button:not(.close-button) {
  width: 100%;
  padding: 12px;
  margin-top: 10px;
  font-size: 1em;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  background-color: rgb(169, 165, 165);
  color: white;
  transition: background-color 0.3s ease;
}

dialog button:not(.close-button):hover {
  background-color: darkorange;
}

</style>

