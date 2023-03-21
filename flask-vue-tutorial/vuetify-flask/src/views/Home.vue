<template>
    <div>
      <AddGame />
      <GameTable />
    </div>
</template>

<script lang="ts">
  import GameTable from '@/components/GameTable.vue';
  import AddGame from '@/components/AddGame.vue';
  export default {
    components: {
      GameTable,
      AddGame,
    },
  };
</script>
