<template>
  <div class="q-ma-md">
    <q-table 
     :columns="qTableHeader" 
     row-key="name"
     :rows="tableData"
     separator="cell"
     no-data-label="I didn't find anything for you"
     :filter="filter"
     :filter-method="filterData"
     :loading="loading_stg"
     :pagination=pagination
     >

      <template #top-right>
        <q-input label="Search records.." v-model="filter" dense>
          <q-icon name="search" size="md"></q-icon>
        </q-input>
      </template>
      <template #header-cell="props">
        <q-th :props="props" class="bg-primary text-white text-center text-bold">
          {{props.col.label}}
        </q-th> 
      </template>
      
      <template #body="props">
        <q-tr :props="props">
          <q-td key="tick" :props="props">
            {{props.row.tick}}
          </q-td>
          <q-td key="name" :props="props">
            {{props.row.name}}
          </q-td>
          
         <q-td key="id" :props="props">
           <q-btn class="bg-primary text-white q-mr-sm">{{props.row.actions[0]}}</q-btn>
           <q-btn class="bg-blue-7 text-white">{{props.row.actions[1]}}</q-btn>
         </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
</template>

<script>

export default {
  name: 'PageIndex',
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
          // object.rows.map((item) => item.data);
          this.loading_stg=false
        })
        .catch((error) => {
          console.log(error);
        });
    },
  }
}
</script>