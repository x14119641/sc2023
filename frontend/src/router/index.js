import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TestView from '../views/TestView.vue'
import TicksTableView from '../views/TicksTableView.vue'
import PingComponent from '../components/PingComponent.vue'
// import TestComponent from '../components/TestComponent.vue'
import TicksTableView2 from '../views/TicksTableView2.vue'
import TickersDataView from '../views/TickersDataView.vue'
import TickerMetaView from '../views/TickerMetaView.vue'
import TickersMetaDataView from '../views/TickersMetaDataView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/ping',
    name: 'ping',
    component: PingComponent
  },
  {
    path: '/test',
    name: 'test',
    component: TestView
  },
  {
    path: '/tickers',
    name: 'ticks',
    component: TicksTableView
  },
  {
    path: '/tickers2',
    name: 'ticks2',
    component: TicksTableView2
  },
  {
    path: '/tickersData',
    name: 'tickersData',
    component: TickersDataView,
    props: true
  },
  {
    path: '/ticker/:tick?',
    name: 'tickerMeta',
    component: TickerMetaView,
    props: true
  },
  {
    path: '/tickersMeta',
    name: 'tickersMetaData',
    component: TickersMetaDataView,
    props: true
  },
]




const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
