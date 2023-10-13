<template>
  <div class="">
      <TickComponent2 />
  </div>
      

</template>
  
  <script>
  // @ is an alias to /src
  import TickComponent2 from '@/components/TickersTableComponent2.vue'
  
  export default {
    name: 'TicksTableView2',
    components: {
      TickComponent2
    }
  }
  </script>
  