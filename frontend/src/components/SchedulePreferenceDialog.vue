<template>
  <dialog ref="dialog">
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

