<template>
  <dialog ref="dialog">
    <form method="dialog" @submit="submit" >
      <input ref="name" type="textbox" placeholder="Name" />

      <br />

      <label> File </label>
      <input ref="file" type="file" placeholder="file" />
      
      <br />

      <label> Kind </label>

      <select ref="kind">
        <option value="l">Lab</option>
        <option value="L">Lecture</option>
        <option value="t">Tutorial</option>
        <option value="a">Assignment</option>
        <option value="s">Problem sheet</option>
        <option value="o">Other</option>
      </select>

      <br />

      <input ref="week" type="number" placeholder="Week" />

      <br />

      <input type="submit" value="Upload" />
      <button @click.prevent="$refs.dialog.close()"> Cancel </button>
    </form>
  </dialog>
</template>

<script>

  export default {
    props: ['course_id'],

    mounted() {
      this.$refs.dialog.showModal();

    },

    methods: {
      async submit() {
        try {
          let data = new FormData();
          data.append('name', this.$refs.name.value);
          data.append('week', this.$refs.week.value);
          data.append('kind', this.$refs.kind.value);
          data.append('file', this.$refs.file.files[0]); 

          let material_create = await this.$root.request_api_endpoint(
            `api/course/${this.course_id}/material/add`,
            'post',
            data,
          );

        } catch (err) {

        }

      }
    }
  }

</script>

