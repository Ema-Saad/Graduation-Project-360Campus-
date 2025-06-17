<template>
  <dialog ref="dialog">
    <form method="dialog" @submit="submit">

      <input v-model="assignment.title" type="text" placeholder="Title" />
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

      <input type="Submit" value="Create" />
      <button @click.prevent="$refs.dialog.close()">
        Cancel
      </button>
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
