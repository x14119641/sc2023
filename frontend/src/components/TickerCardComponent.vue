<template>
  <div
    class="row bg-blue-grey-2 "
    style="min-height: 400px; width: 100%; padding: 5px"
  >

    <div
      id="parent"
      class="fit  wrap row items-stretch "
      style="overflow: hidden"
    >
      <div class="col-12 bg-grey-6 " style="overflow: auto">
        <q-card class="no-border-radius">
          <q-card-section> 
            <div class="text-h6">{{title}} </div>
            <div class="text-subtitle2">
              Institutional Ownership of 
              <span v-if="total_last_ownership" :class="ownership_style(total_last_ownership)">
                {{ total_last_ownership }}%</span></div> 
          </q-card-section>
          
        </q-card>
      </div>
      <div class="row wrap fit items-start content-start" v-for="dict in my_data"  v-bind:key="dict" >
        <div class="q-mt-xs col-auto bg-grey-10 " style="overflow: auto">
          <q-card class="no-border-radius">
            <q-card-section horizontal> 
              <div class="q-ma-md" style="min-width:200px">Positions Holders</div>
            </q-card-section>
          </q-card>
  
          <q-card class="no-border-radius">
            <q-card-section horizontal> 
              <div class="q-ma-md" style="min-width:250px">New</div>
              <q-separator vertical />
              <div class=" q-ma-md ">{{ dict['new_positions_holders'] }}</div>
            </q-card-section>
          </q-card>
          
          <q-card class="no-border-radius">
            <q-card-section horizontal> 
              <div class="q-ma-md" style="min-width:250px">Held</div>
              <q-separator vertical />
              <div class=" q-ma-md ">{{ dict['held_positions_holders'] }}</div>
            </q-card-section>
          </q-card>
  
          <q-card class="no-border-radius">
            <q-card-section horizontal> 
              <div class="q-ma-md" style="min-width:250px">Sold</div>
              <q-separator vertical />
              <div class=" q-ma-md ">{{ dict['sold_out_positions_holders'] }}</div>
            </q-card-section>
          </q-card>
          <q-separator horizontal />
          <q-card class="no-border-radius">
            <q-card-section horizontal> 
              <div class="q-ma-md" style="min-width:250px">Increased</div>
              <q-separator vertical />
              <div class=" q-ma-md ">{{ dict['increased_positions_holders'] }}</div>
            </q-card-section>
          </q-card>
          <q-card class="no-border-radius">
            <q-card-section horizontal> 
              <div class="q-ma-md" style="min-width:250px">Decreased</div>
              <q-separator vertical />
              <div class=" q-ma-md ">{{ dict['decreased_positions_holders'] }}</div>
            </q-card-section>
          </q-card>
          <q-card class="no-border-radius">
            <q-card-section horizontal> 
              <div class="q-ma-md" style="min-width:250px">Total</div>
              <q-separator vertical />
              <div class=" q-ma-md ">{{ dict['total_institutional_holders'] }}</div>
            </q-card-section>
          </q-card>
        
        
        
      </div>
      <div class="q-mt-xs q-pl-xs col-auto  " style="overflow: auto">
        <!-- Añado columna vacia para cuando haga resize los margines sean iguales entre las columnas -->
      </div>
      <div class="q-my-xs  col-auto  " style="overflow: auto">
        <q-card class="no-border-radius">
          <q-card-section horizontal> 
            <div class="q-ma-md" style="min-width:250px">Positions Holders</div>
          </q-card-section>
        </q-card>
        <q-card class="no-border-radius">
          <q-card-section horizontal> 
            <div class="q-ma-md" style="min-width:250px">New</div>
            <q-separator vertical />
            <div class=" q-ma-md ">333</div>
            <!-- <div class=" q-ma-md ">{{ dict['new_positions_holders'] }}</div> -->
          </q-card-section>
        </q-card>
        
      </div>
      </div>

      
    </div>
    
  </div>
  <p>{{ total_last_ownership }}</p>
</template>

<script>
export default {
  props: ["title", "total", "my_data"],
  data() {
    return {
      colorDefault1: this.color1 ? this.color1 : "#949398FF",
      colorDefault2: this.color2 ? this.color2 : "#F4DF4EFF",
      myTitle: this.title,
      total_last_ownership: this.my_data[0]['institutional_ownership_perc'],
      // my_data:[],
      my_data2:[]
    }
  },
  methods:{
    ownership_style(val) {
      if (val < 0)
          return 'text-h5 text-weight-bold text-negative'
      if (val > 50 || val <80)
          return 'text-h5 text-weight-bold text-blue'
      return 'text-h5 text-weight-bold text-positive'
    }
  },
  // mounted() {
  //    {
  //     this.total_last_ownership= this.my_data[0]
  //   }
  // }

  // watch: {
  //       my_data: function(newVal) { 

  //          this.total_last_ownership = newVal[0]['institutional_ownership_perc']
  //       }
  //     }
};
</script>

<style scoped></style>
