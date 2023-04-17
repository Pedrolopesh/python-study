<template>
    <v-table class="container-table">
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
        <tr v-for="(item, index) in gameData" :key="index">
          <td v-if="item.title">{{ item.title }}</td>
          <td v-if="item.genre">{{ item.genre }}</td>
          <td v-if="item.played !== null">{{ handlePlayedGame(item.played) }}</td>
          <td v-if="item.title && item.genre && item.played !== null">
            <div class="d-flex">
                <v-btn class="mr-2" variant="outlined">
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

<style>
.container-table {
  display: block;
  max-width: 100%;
  width: 55%;
  margin: 20px auto;
}
</style>

<script lang="ts">

  interface GameData {
    title: string;
    genre: string;
    played: boolean;
  }

  export default {
    data () {
      return {
        gameData: [] as GameData[]
      }
    },
    created() {
        this.getTableData();
    },
    methods: {
        async getTableData() {
            try {
                const resp = await this.axios.get('http://127.0.0.1:5000/api/games')
                console.log('resp table? ', resp)
                if (resp?.data?.games) {
                    this.gameData = resp.data.games
                }
            } catch (err) {
                console.log(err);
            }	
        },
        handlePlayedGame(playedParam: boolean) {
          if (playedParam) return 'Yes'
          else return 'No'
        }
    }
  }
</script>