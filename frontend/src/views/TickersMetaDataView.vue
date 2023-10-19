<template>
  <div class="">
      <TickersMetaDataComponent />
  </div>
      

</template>
  
  <script>
  // @ is an TickersMetaDataComponent to /src
  import TickersMetaDataComponent from '@/components/TickersMetaDataComponent.vue'
  
  export default {
    name: 'TicksMetaDataTableView',
    components: {
      TickersMetaDataComponent
    }
  }
  </script>
  