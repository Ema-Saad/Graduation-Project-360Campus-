<template>
  <dialog ref="dialog">
    <button class="close-icon" @click.prevent="$refs.dialog.close()">✕</button>
    <form method="method" @submit="submit">
      <table>
        <thead>
          <tr>
            <th> Day </th>
            <th> First Period </th>
            <th> Second Period </th>
            <th> Thrid Period </th>
            <th> Fouth Period </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu']">
            <th> {{ day }} </th>
            <td v-for="slot in [0, 1, 2, 3]">
              <input type="checkbox" 
                     v-model="preferences" 
                     :value="`${day}, ${2 * slot}`"
              />

              <input type="checkbox" 
                     v-model="preferences" 
                     :value="`${day}, ${2 * slot + 1}`"
              />

              <label> Full </label>
              <input type="checkbox" 
                     v-model="preferences" 
                     :value="[`${day}, ${2 * slot}`, `${day}, ${2 * slot + 1}`]"
              />
            </td>
            <td> 
              <button @click.prevent="preferences = preferences.filter((d) => !d.startsWith(day))">
                Clear 
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <input type="submit" value="Update Preferences" />
      <button @click.prevent="preferences = []">
        Clear
      </button>
      <button @click.prevent="$refs.dialog.close()">
        Close
      </button>
    </form>
  </dialog>
</template>

<script>
  export default {
    data() {
      return {
        preferences: [],
      }
    },

    async beforeMount() {
      const preferences = await this.$root.request_api_endpoint(
        'api/schedule/preference/list',
        'get',
        null
      );

      const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu']

      this.preferences = preferences.map((d) => `${DAYS[d.day]}, ${d.slot}`)
    },

    mounted() {
      this.$refs.dialog.showModal();
    },

    methods: {
      async submit(evt) {
        const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu']

        const preferences = this.preferences
          .map((s) => s.split(', '))
          .map(([d, s]) => ({day: DAYS.indexOf(d), slot: parseInt(s)}))

        await this.$root.request_api_endpoint(
          'api/schedule/preference/create',
          'post',
          JSON.stringify(preferences),
          { 'Content-Type': 'application/json' }
        )
      }
    }
  }
</script>

<style>
dialog {
  padding: 2rem;
  border: none;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  max-width: 90%;
  width: 900px;
  max-height: 91vh;
  overflow: hidden;
  background: linear-gradient(to bottom, rgba(32, 24, 135, 1), rgba(244, 196, 98, 1));
  font-family: 'Segoe UI', sans-serif;
  position: relative;
    overflow: hidden;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  padding-right: 4px;  
  box-sizing: border-box;
}

.close-icon {
  position: absolute;
  top: 12px;
  right: 16px;
  background-color: transparent;
  border: none;
  font-size: 22px;
  color: #ffffffcc; /* semi-transparent white for elegance */
  cursor: pointer;
  z-index: 10;
  transition: color 0.3s ease, transform 0.2s ease;
}

.close-icon:hover {
  color: #ff5722;
  transform: scale(1.2); 
}

table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  overflow: hidden;
}

thead {
  background-color: #201887; 
  color: white;
}

th, td {
  padding: 12px;
  text-align: center;
  border-bottom: 1px solid #e5e7eb;
}

input[type="checkbox"] {
  transform: scale(1.2);
  margin: 2px 4px;
  accent-color: #201887;
}

label {
  display: block;
  margin-top: 4px;
  font-size: 13px;
  color: #ffffff;
}

button, input[type="submit"] {
  background-color: #201887;
  color: white;
  border: none;
  padding: 10px 16px;
  margin: 4px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease;
}
button:not(.close-icon):hover,
input[type="submit"]:hover {
  background-color: darkorange;
}

td > button {
  background-color: #201887; 
  color: white;
  padding: 6px 15px;
  font-size: 12px;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

td > button:hover {
  background-color: darkorange;
}

form > button {
  background-color: #9ca3af; 
  margin: 1px 1px; 
}

form > button:hover {
  background-color: darkorange;
}

</style>