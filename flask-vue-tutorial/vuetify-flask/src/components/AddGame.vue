<template>
    <div class="text-center container-add-game">
      <v-dialog
        v-model="dialog"
        width="500px"
      >
        <template v-slot:activator="{ props }">
          <v-btn
            class="d-block"
            color="primary"
            v-bind="props"
          >
            Add Game
          </v-btn>
        </template>
  
        <v-card class="container-card-add-game">

            <v-toolbar
                color="primary"
                title="Add a new game"
            ></v-toolbar>

            <div>
                <v-text-field label="Title" v-model="gameForm.title"></v-text-field>
                <v-text-field label="Genre" v-model="gameForm.genre"></v-text-field>
                
                <v-checkbox label="Checkbox" v-model="gameForm.played"></v-checkbox>
            </div>
          
          <v-card-actions class="container-add-game-actions">
            <v-btn class="d-block" variant="outlined" color="primary" block @click="sendForm()">Submit</v-btn> 
            <v-btn class="d-block" variant="outlined" color="error" block @click="dialog = false">Reset</v-btn>
          </v-card-actions>
        
        </v-card>
      </v-dialog>
    </div>
  </template>

<style>
.container-add-game {
  display: block;
  max-width: 100%;
  width: 55%;
  margin: 20px auto;
}

.container-card-add-game {
  display: block;
  max-width: 100%;
  width: 100%;
  /* margin: 20px auto; */
}

.container-add-game-actions {
  max-width: 25%;
}
</style>

<script lang="ts">
  export default {
    data: () => ({
      dialog: false,
      gameForm: {
        title: '',
        genre: '',
        played: false
      }
    }),
    methods: {
        async sendForm() {
            const path = 'http://127.0.0.1:5000/api/games'
            const respAddGame = await this.axios.post(path, {body: this.gameForm})
            console.log('respAddGame: ', respAddGame)
        }
    }
  }
</script>