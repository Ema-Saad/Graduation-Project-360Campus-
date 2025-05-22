<template>
  <dialog ref="dialog">
    <form method="dialog" @submit="submit" >
      <input v-model="material.name" type="textbox" placeholder="Name" />

      <br />

      <label> File </label>
      <input ref="file" type="file" placeholder="file" />
      
      <br />

      <label> Kind </label>

      <select v-model="material.kind">
        <option value="l">Lab</option>
        <option value="L">Lecture</option>
        <option value="t">Tutorial</option>
        <option value="a">Assignment</option>
        <option value="s">Problem sheet</option>
        <option value="o">Other</option>
      </select>

      <br />

      <input v-model="material.week" type="number" placeholder="Week" />

      <br />

      <input type="submit" value="Upload" />
      <button @click.prevent="$refs.dialog.close()"> Cancel </button>
    </form>
  </dialog>
</template>

<script>

  export default {
    props: ['course_id', 'instance'],

    data() {
      return {
        method: 'post',
        url: `api/course/${this.course_id}/material/add`,
        material: {
          name: '',
          kind: 'o',
          week: 0,
        },
      };
    },

    beforeMount() {
      if (this.instance) {
        this.url = `api/material/${this.instance.id}/edit`;
        this.method = 'put';
        this.material = this.instance;
      }
    },

    mounted() {
      this.$refs.dialog.showModal();
    },

    methods: {
      async submit() {
        try {
          let data = new FormData();
          data.append('name', this.material.name);
          data.append('week', this.material.week);
          data.append('kind', this.material.kind);

          let file = this.$refs.file.files[0];

          if (file)
            data.append('file', file); 

          let { url, method } = this;
          let material_create = await this.$root.request_api_endpoint(url, method, data);

        } catch (err) {

        }

      }
    }
  }

</script>

