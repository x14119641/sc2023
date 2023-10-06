<template>
  <div class="">
      <TicksTableComponent />
  </div>
      

</template>
  
  <script>
  // @ is an alias to /src
  import TicksTableComponent from '@/components/TickersTableComponent.vue'
  
  export default {
    name: 'TicksTableView',
    components: {
      TicksTableComponent
    }
  }
  </script>
  