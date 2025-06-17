<template>
  <dialog ref="dialog">
    <form method="dialog" @submit="submit">

      <label for="title"> Title </label>
      <input type="text" id="title" v-model="online_meeting.title" />
      <br />

      <label for="description"> Description </label>
      <textarea id="description" v-model="online_meeting.description">
      </textarea>
      <br />

      <label for="time"> Time </label>
      <input type="datetime-local" v-model="online_meeting.time" />
      <br />

      <input type="submit" value="Create">
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

