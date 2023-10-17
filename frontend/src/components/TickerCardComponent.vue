<template>
  <div
    class="row bg-blue-grey-2"
    style="min-height: 400px; width: 100%; padding: 5px"
  >
    <div
      id="parent"
      class="fit row wrap justify-start items-start content-start"
      style="overflow: hidden"
    >
      <div class="col-12 bg-grey-6" style="overflow: auto">
        <q-card class="no-border-radius">
          <q-card-section> 
            <div class="text-h6">{{title}} </div>
            <div class="text-subtitle2">by John Doe</div>
          </q-card-section>
          
        </q-card>
      </div>
      <div class="q-mt-xs col-2 bg-grey-10" style="overflow: auto">
        <q-card class="no-border-radius">
          <q-card-section> Child #2 </q-card-section>
          
        </q-card>
        
      </div>
      <div class="q-ma-xs col-2 bg-grey-10" style="overflow: auto">
        <q-card class="no-border-radius">
          <q-card-section> Child #3 </q-card-section>
          
        </q-card>
        
      </div>
    </div>
    
  </div>
  <p>{{ my_data }}</p>
</template>

<script>
export default {
  props: ["title", "total", "my_data"],
  data() {
    return {
      colorDefault1: this.color1 ? this.color1 : "#949398FF",
      colorDefault2: this.color2 ? this.color2 : "#F4DF4EFF",
      // myTitle: this.title,
      // myText:
    };
  },
};
</script>

<style scoped></style>
