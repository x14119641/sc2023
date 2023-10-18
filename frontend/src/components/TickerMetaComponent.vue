<template>
  <div class="q-ma-md">
    <div class="q-py-md row">
      <div v-if="tick" class="col-3 text-h5">
        Ticker: <span class="text-blue-9"> {{ tick }}</span></div>
      <div v-else class="col-3 text-h5"></div>
      <div class="col-6"></div>
      <div class="col-3 ">
        <q-input
          class="q-ml-md "
          v-model="tickToGo"
          dense
          @keydown.enter.prevent="goTo"
          outlined
          placeholder="Search"
        >
          <template v-slot:after>
            <q-btn
              @click="goTo"
              round
              dense
              flat
              icon="search"
            ></q-btn>
          </template>
        </q-input>
      </div>
    </div>
    <div class="q-ta-md row">
        <!-- <router-view :key="$route.fullPath" @showLoading="showLoading"></router-view> -->
      <div v-if="my_data.length" class="col-12 text-h5">
        <TickerCardComponent :title="formatTitle()" total="n_tables" :my_data="my_data"/>
        
      </div>
      <div v-else class="col-3 text-h5">No data to show</div>
    </div>
    
  </div>

</template>

<script>
import TickerCardComponent from "@/components/TickerCardComponent.vue";

export default {
  name: "TickerMeta",
  components:{
    TickerCardComponent
  },
  data() {
    return {
      tick: "",
      tickToGo: "",
      loading_stg:"",
      my_data:[]
    };
  },
  mounted() {
    this.tick = this.$route.params.tick.toUpperCase();
    if (this.tick) {
        this.getData()
    }

  },
  methods: {
    async goTo() {
      let x = this.tickToGo;
      // this.$route.push({ name: 'tickerMeta', params: { tick: this.tickToGo }})
      this.$router.replace({ name: "tickerMeta", params: { tick: x } });
    },

    async getData() {
        const path = "http://127.0.0.1:5000/api/institutional/";

        this.axios
        .get(path+this.tick)
        .then((res) => {
            this.my_data = res.data;
            // this.columns = Object.keys(res.data[0]);
            this.rows= res.data;
            // object.rows.map((item) => item.data);
            this.loading_stg=false
        })
        .catch((error) => {
            console.log(error);
        });
    },
    formatTitle() {
        return 'Report for ' + this.tick
    }
  },

  // define a watcher
  
};
</script>
