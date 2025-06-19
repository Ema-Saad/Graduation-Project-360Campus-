<template>
  <dialog ref="dialog" class="custom-dialog">
    <form method="dialog" @submit="submit">
      <label for="name">Name</label>
      <input id="name" v-model="material.name" type="text" class="wide-input" placeholder="Material Name" />

      <label for="file">Upload File</label>
      <div class="file-upload-wrapper">
        <input id="file" ref="file" type="file" @change="onFileChange" />
        <span class="fake-button">Choose File</span>
       <span class="file-name">{{ fileName }}</span>
      </div>

      <label for="kind">Kind</label>
      <select id="kind" v-model="material.kind">
        <option value="l">Lab</option>
        <option value="L">Lecture</option>
        <option value="t">Tutorial</option>
        <option value="a">Assignment</option>
        <option value="s">Problem sheet</option>
        <option value="o">Other</option>
      </select>

      <label for="week">Week Number</label>
      <input id="week" v-model="material.week" type="number" placeholder="e.g. 3" />

      <div class="form-buttons">
        <input type="submit" value="Upload" />
        <button @click.prevent="$refs.dialog.close()">Cancel</button>
      </div>
    </form>
  </dialog>
</template>

<script>

  export default {
    props: ['course_id', 'instance'],

    data() {
      return {
        method: 'post',
        fileName: 'No file chosen',
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

      },
      onFileChange(e) {
  const file = e.target.files[0];
  this.fileName = file ? file.name : 'No file chosen';
}
    }
    
  }

</script>

<style>
.custom-dialog {
  background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
  border: none;
  padding: 30px;
  border-radius: 20px;
  color: white;
  width: 480px;
  max-width: 95%;
  font-family: 'Segoe UI', sans-serif;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.custom-dialog form {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.wide-input {
  width: 94.5%;
  font-size: 16px;
  padding: 14px;
    border-radius: 10px;
  border: none;
  font-size: 15px;
  background-color: #fff;
  color: #333;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  transition: border 0.2s;
}

.custom-dialog label {
  font-weight: 600;
  font-size: 15px;
  margin-bottom: 4px;
}

.custom-dialog input[type="textbox"],
.custom-dialog input[type="number"],
.custom-dialog select {
  padding: 12px;
  border-radius: 10px;
  border: none;
  font-size: 15px;
  background-color: #fff;
  color: #333;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  transition: border 0.2s;
}
.custom-dialog input[type="file"] {
  background-color: #fff;
  padding: 10px;
  border-radius: 10px;
  border: 2px dashed #ccc;
  font-size: 14px;
  color: #444;
  cursor: pointer;
  transition: border 0.2s;
}

.custom-dialog input[type="file"]:hover {
  border-color: #3b3b98;
}

.custom-dialog input[type="submit"],
.custom-dialog button {
  padding: 12px;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.1s;
}

.custom-dialog input[type="submit"] {
  background-color: #201887;
  color: white;
}

.custom-dialog input[type="submit"]:hover {
  background-color: darkorange;
  transform: scale(1.02);
}

.custom-dialog button {
  background-color: rgb(169, 165, 165);
  color: white;
}

.custom-dialog button:hover {
  background-color: darkorange;
  transform: scale(1.02);
}
.file-upload-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
  background-color: #fff;
  border-radius: 10px;
  border: 2px dashed #ccc;
  padding: 12px;
  color: #444;
  font-size: 14px;
  cursor: pointer;
  transition: border-color 0.3s ease;
}

.file-upload-wrapper:hover {
  border-color: #3b3b98;
}

.file-upload-wrapper input[type="file"] {
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
  height: 100%;
  width: 100%;
  cursor: pointer;
}

.fake-button {
  font-weight: bold;
  color: #3b3b98;
}

.file-name {
  margin-left: 10px;
  color: #666;
  font-style: italic;
}

.form-buttons {
  display: flex;
  flex-direction: column;
  gap: 15px;
  align-items: stretch;
  margin-top: 20px; 
}
</style>
