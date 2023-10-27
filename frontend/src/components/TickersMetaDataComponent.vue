<template>
  <div class="q-ma-md">
    <p>MEta</p>
    <q-table 
      ref="table"
     :columns="qTableHeader" 
     row-key="name"
     :rows="tableData"
     separator="cell"
     no-data-label="I didn't find anything for you"
     :filter="filter"
     :filter-method="filterData"
     :loading="loading_stg"
  
     :columnDefs="columnDefs"
     wrap-cells
     >

      <template #top-right>
        <q-input label="Search records.." v-model="filter" dense>
          <q-icon name="search" size="md"></q-icon>
        </q-input>
      </template>
      <template #header-cell="props">
        <q-th :props="props" class="bg-primary text-white text-center text-bold thead-sticky">
          {{props.col.label}}
        </q-th> 
      </template>
      
      <template #body="props">
        
        <q-tr :props="props">
          <q-td key="tick" :props="props"  >
            <router-link :to="{ name: 'tickersMetaData', params: { tick: props.row.tick }}">{{props.row.tick}}</router-link>
          </q-td>
          <q-td key="ipo_year" :props="props">
            {{props.row.ipo_year}}
          </q-td>
          <q-td key="market_cap" :props="props">
            {{props.row.market_cap}}
          </q-td>
          <q-td key="last_sale" :props="props">
            {{props.row.last_sale}}
          </q-td>
          <q-td key="change_perc" :props="props">
            {{props.row.change_perc}}
          </q-td>
          <q-td key="net_change" :props="props">
            {{props.row.net_change}}
          </q-td>
          <q-td key="inserted" :props="props">
            {{props.row.inserted}}
          </q-td>
        </q-tr>
      </template>
    </q-table>
    <!-- <p>{{ tableData }}</p> -->
  </div>
</template>




<style lang="sass">

.sticky-header
  /* height or max-height is important */
  max-height: 100vh

  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th
    /* bg color is important for th; just specify one */
    background-color: #fff

  thead tr th
    position: sticky
    z-index: 1
  thead tr:first-child th
    top: 0

  /* this is when the loading indicator appears */
  &.q-table--loading thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
</style>

<script>

export default {
  name: 'TickersMetaData',
  data () {
    return {
      filter: "",
      loading_stg:true,
      pagination: {
        sortBy: 'tick',
        descending: false,
        page: 1,
        rowsPerPage: 60
      },
      columnDefs: [
        { field: 'tick', width: 5, maxWidth: 10, suppressSizeToFit: true },
        { field: 'ipo_year', width: 75, minWidth: 50, maxWidth: 75 ,suppressSizeToFit: true },
        { field: 'market_cap', width: 50, minWidth: 25, maxWidth: 50 },
        { field: 'last_sale', width: 50, minWidth: 25, maxWidth: 50 },
        { field: 'change_perc', width: 40, minWidth: 25, maxWidth: 40 },
        { field: 'net_change', width: 40, minWidth: 20, maxWidth: 40 },
        { field: 'inserted', width: 40, minWidth: 20, maxWidth: 40 },
      ],
      qTableHeader: [
        {
          name: "tick",
          required: true,
          label: "Tickers",
          align: "left",
          field: (row) => row.tick,
          format: (val) => `${val}`,
          sortable: true,
        },
        {
          name: "ipo_year",
          align: "center",
          label: "IPO Year",
          field: "ipo_year",
          sortable: true,
        },
        {
          name: "market_cap",
          align: "center",
          label: "Market Cap.",
          field: "market_cap",
          sortable: true,
        },
        {
          name: "last_sale",
          align: "center",
          label: "Last Sale",
          field: "last_sale",
        },
        {
          name: "change_perc",
          align: "center",
          label: "Change %",
          field: "change_perc",
        },
        {
          name: "net_change",
          align: "center",
          label: "Net Change",
          field: "net_change",
        },
        {
          name: "inserted",
          align: "center",
          label: "Inserted",
          field: "inserted",
        },
      ],
      tableData:[],
    }
  },
  created() {
    this.getData();
  },
  methods: {
    filterData(rows, term){
      const filteredItems = this.tableData.filter(
        item => `${item.name} || ${item.tick} `.toLowerCase().includes(term.toLowerCase()));
            return filteredItems;
        },
    getData() {
      const path = "http://127.0.0.1:5000/api/metadata/tickers";

      this.axios
        .get(path)
        .then((res) => {  
          this.tableData= res.data;
          this.loading_stg=false
        })
        .catch((error) => {
          console.log(error);
        });
    },
  }
}
</script>