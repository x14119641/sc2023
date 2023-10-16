<template>
  <div class="">
      <TickersDataComponent />
  </div>
      

</template>
  
  <script>
  // @ is an alias to /src
  import TickersDataComponent from '@/components/TickersDataComponent.vue'
  
  export default {
    name: 'TicksDataTableView',
    components: {
      TickersDataComponent
    }
  }
  </script>
  