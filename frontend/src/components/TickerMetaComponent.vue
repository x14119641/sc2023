<template>
  <div class="q-ma-md">
    <div class="q-pa-md row">
      <div v-if="tick" class="col-3 text-h5">{{ tick }}</div>
      <div v-else class="col-3 text-h5"></div>
      <div class="col-6"></div>
      <div class="col-3">
        <q-input
          class="q-ml-md"
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
              icon="add"
            ></q-btn>
          </template>
        </q-input>
      </div>
    </div>
    <div class="q-pa-md row">
        <router-view :key="$route.fullPath" @showLoading="showLoading"></router-view>
      <div v-if="tick" class="col-3 text-h5">the page is here{{ tick }}
        
      </div>
      <div v-else class="col-3 text-h5">No data to show</div>
    </div>
    <p>{{ tick }}</p>
  </div>
</template>

<script>
export default {
  name: "TickerMeta",
  data() {
    return {
      tick: "",
      tickToGo: "",
    };
  },
  mounted() {
    this.tick = this.$route.params.tick;
  },
  methods: {
    async goTo() {
      let x = this.tickToGo;
      // this.$route.push({ name: 'tickerMeta', params: { tick: this.tickToGo }})
      this.$router.replace({ name: "tickerMeta", params: { tick: x } });
    },
  },

  // define a watcher
  
};
</script>
