<template>
  <div class="q-ma-md">
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
     :pagination=pagination
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
            <router-link :to="{ name: 'tickerMeta', params: { tick: props.row.tick }}">{{props.row.tick}}</router-link>
          </q-td>
          <q-td key="name" :props="props">
            {{props.row.name}}
          </q-td>
          <q-td key="sector" :props="props">
            {{props.row.sector}}
          </q-td>
          <q-td key="industry" :props="props">
            {{props.row.industry}}
          </q-td>
          <q-td key="country" :props="props">
            {{props.row.country}}
          </q-td>
          
          
         
        </q-tr>
      </template>
    </q-table>
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
  name: 'TickersData',
  data () {
    return {
      filter: "",
      loading_stg:true,
      pagination: {
        sortBy: 'tick',
        descending: false,
        page: 1,
        rowsPerPage: 50
      },
      columnDefs: [
        { field: 'tick', width: 5, maxWidth: 10, suppressSizeToFit: true },
        { field: 'name', width: 50, minWidth: 20, maxWidth: 50 , suppressSizeToFit: true},
        { field: 'sector', width: 75, minWidth: 50, maxWidth: 75 ,suppressSizeToFit: true },
        { field: 'industry', width: 50, minWidth: 25, maxWidth: 50 },
        { field: 'country', width: 50, minWidth: 25, maxWidth: 50 },
        { field: 'market_cap', width: 40, minWidth: 25, maxWidth: 40 },
        { field: 'ipo_year', width: 40, minWidth: 20, maxWidth: 40 },
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
          name: "name",
          align: "center",
          label: "Name",
          field: "name",
          sortable: true,
        },
        {
          name: "sector",
          align: "center",
          label: "Sector",
          field: "sector",
          sortable: true,
        },
        {
          name: "industry",
          align: "center",
          label: "Industry",
          field: "industry",
        },
        {
          name: "country",
          align: "center",
          label: "Country",
          field: "country",
          sortable: true,
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
      const path = "http://127.0.0.1:5000/api/tickers";

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