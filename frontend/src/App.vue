<style>
  html { overflow-y: auto }
</style>

<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="glossy">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          icon="menu"
        />

        <q-toolbar-title>
          Quasar App
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="bg-grey-2"
    >
      <q-list>
        <q-item-label header>Essential Links</q-item-label>
        <q-item to="/test">
          <q-item-section avatar>
            <q-icon name="task" />
          </q-item-section>
        
          <q-item-section>
            Test Page
          </q-item-section>
        </q-item>

        <q-item to="/tickersData">
          <q-item-section avatar>
            <q-icon name="segment" />
          </q-item-section>
        
          <q-item-section>
            Tickers
          </q-item-section>
        </q-item>

        <q-item to="/ticker/">
          <q-item-section avatar>
            <q-icon name="query_stats" />
          </q-item-section>
        
          <q-item-section>
            Ticks Search
          </q-item-section>
        </q-item>
        <q-item to="/tickersMeta">
          <q-item-section avatar>
            <q-icon name="analytics" />
          </q-item-section>
        
          <q-item-section>
            Ticks Metadata
          </q-item-section>
        </q-item>
        <q-item to="/admin">
          <q-item-section avatar>
            <q-icon name="admin_panel_settings" />
          </q-item-section>
        
          <q-item-section>
            Admin
          </q-item-section>
        </q-item>
          

        
      </q-list>
    </q-drawer>

    <q-page-container>
      <!-- <PingComponent /> -->
      <!-- <router-link to="/test">test</router-link>  -->
      <HelloWorld v-if="$route.name == 'home'"  />
      <!-- <TestView /> -->
      <!-- <router-view/> -->
      <router-view :key="$route.fullPath" @showLoading="showLoading"></router-view>
    </q-page-container>
  </q-layout>
  
</template>



<script>
import { ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
// import PingComponent from './components/PingComponent.vue'

export default {
  name: 'LayoutDefault',

  components: {
    // PingComponent,
    HelloWorld,  
    
    // TestView
  },

  setup () {
    return {
      leftDrawerOpen: ref(false)
    }
  }
}
</script>
