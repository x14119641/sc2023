<template>
  <div class="">
      <AdminComponent/>
  </div>
      

</template>
  
  <script>
  // @ is an alias to /src
  import AdminComponent from '@/components/AdminComponent.vue'
  
  export default {
    name: 'AdminView',
    components: {
      AdminComponent
    }
  }
  </script>
  