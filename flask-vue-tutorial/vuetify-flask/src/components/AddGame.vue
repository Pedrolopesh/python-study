<template>
    <div class="text-center">
      <v-dialog
        v-model="dialog"
        width="auto"
      >
        <template v-slot:activator="{ props }">
          <v-btn
            color="primary"
            v-bind="props"
          >
            Add Game
          </v-btn>
        </template>
  
        <v-card>
        
            <v-toolbar
                color="primary"
                title="Add a new game"
            ></v-toolbar>

            <div>
                <v-text-field label="Title" v-model="gameForm.title"></v-text-field>
                <v-text-field label="Genre" v-model="gameForm.genre"></v-text-field>
                
                <v-checkbox label="Checkbox" v-model="gameForm.played"></v-checkbox>
            </div>
          
          <v-card-actions>
            <v-btn color="primary" block @click="sendForm()">Submit</v-btn> 
            <v-btn color="error" block @click="dialog = false">Reset</v-btn>
          </v-card-actions>
        
        </v-card>
      </v-dialog>
    </div>
  </template>


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