
<template>
  <div>
    <!-- <p>{{my_data2}}</p>  -->
    <q-page class="flex flex-center">
      
      <q-table class="table"
              flat bordered
              title="Ticks"
              :rows="rows"
              :columns="columns"
              row-key="tick"
              id="myTable" 
              color="amber"
              :pagination=pagination
              :loading=loading_stg
              :columnDefs="columnDefs"
              :ref="table" 
      >
        <template  v-slot:top>
          <q-input  dense debounce="400"   class="input is-success" type="text" 
          
          v-model="search"
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
          
        </template>
        <template #header-cell-tick="props">
          <q-th :props="props">
            <q-icon
              size="sm"
              name="done"
              class="q-mr-sm"
              color="grey-7"
            />{{ props.col.label }}
          </q-th>
        </template>
        <template #body-cell="props">
          <q-td
            :props="props"
          >{{ props.value }}
          </q-td>
        </template>
      </q-table >
      <!-- <p>{{ my_data }}</p> -->
      <!-- <p>{{ columns }}</p> -->
      
    </q-page>
  </div>
</template>

<script>
/* eslint-disable */ 
export default {
  name: "PingComponent",
  data() {
    return {
      my_data: [],
      my_data2: [],
      columns: [],
      rows: [],
      number_rows:'',
      loading_stg:true,
      search: '',
      pagination: {
        sortBy: 'tick',
        descending: false,
        page: 1,
        rowsPerPage: 50
      },
      columnDefs: [
        { field: 'tick', width: 5, suppressSizeToFit: true },
        { field: 'name', width: 100, minWidth: 50, maxWidth: 100 },
      ],
      lowerSearch:'',
      i:0,
    };
  },
  methods: {
    
    getData() {
      const path = "http://127.0.0.1:5000/api/tickers";

      this.axios
        .get(path)
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
    build_columns_ticks() {
      this.columns= [
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
      ];
    },
    customFilter(rows, terms){
      // rows contain the entire data
      // terms contains whatever you have as filter
      
      console.log(terms,rows)
      
      lowerSearch = terms.search ? terms.search.toLowerCase() : ""

      const filteredRows = rows.filter(
        (row, i) =>{

        let ans = false
        
        //Gather toggle conditions
        let c1 = this.filterToggle.tick && row.category == "tick"
        let c2 = this.filterToggle.name && row.category == "name"
        
        
        //Gather search condition
               

        
        //Assume true in case there is no search 
        let s1 = true
        
        //If search term exists, convert to lower case and see which rows contain it
        if(lowerSearch != ""){
          s1 = false
          //Get the values
          let s1_values = Object.values(row)
          //Convert to lowercase
          let s1_lower = s1_values.map(x => x.toString().toLowerCase())
        
          for (let val = 0; val<s1_lower.length; val++){
            if (s1_lower[val].includes(lowerSearch)){
              s1 = true
              break
            }
          }
        }

        //assume row doesn't match
        ans = false
          
        //check if any of the conditions match  
        if ( (c1 && s1) || (c2 && s1) ) {
          ans = true
        }
        
        return ans

        })



      return filteredRows
    }
  },

  created() {
    this.getData();
    this.number_rows=50
    this.build_columns_ticks();
    this.my_data2 = this.$refs.table  
  },
};
</script>

<style lang="sass">
.custom-header-color


  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th /* bg color is important for th; just specify one */
    background-color: #00b4ff

  
</style>