<template>
    <v-table>
      <thead>
        <tr>
          <th class="text-left">
            Title
          </th>
          <th class="text-left">
            Genre
          </th>
          <th class="text-left">
            Played?
          </th>
          <th class="text-left">
            Actions
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in desserts" :key="index">
          <td>{{ item.title }}</td>
          <td>{{ item.genre }}</td>
          <td>{{ item.played }}</td>
          <td>
            <div class="d-flex">
                <v-btn variant="outlined">
                    Update
                </v-btn>
                <v-btn variant="outlined" color="error">
                    Delete
                </v-btn>
            </div>
          </td>
        </tr>
      </tbody>
    </v-table>
  </template>


<script lang="ts">
  export default {
    data () {
      return {
        desserts: [
          {
            title: 'Frozen Yogurt',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'Ice cream sandwich',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'Eclair',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'Cupcake',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'Gingerbread',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'Jelly bean',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'Lollipop',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'Honeycomb',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'Donut',
            genre: 'Lorem',
            played: true,
          },
          {
            title: 'KitKat',
            genre: 'Lorem',
            played: true,
          },
        ],
      }
    },
    created() {
        this.getTableData();
    },
    methods: {
        async getTableData() {
            try {
                const resp = await this.axios.get('http://127.0.0.1:5000/api/shark')
                console.log('resp? ', resp)
            } catch (err) {
                console.log(err);
            }	
        }
    }
  }
</script>