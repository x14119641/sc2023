<template>
  <div class="">
      <TickDataComponent />
  </div>
      

</template>
  
  <script>
  // @ is an alias to /src
  import TickDataComponent from '@/components/TickersDataTableComponent.vue'
  
  export default {
    name: 'TicksDataTableView',
    components: {
      TickDataComponent
    }
  }
  </script>
  