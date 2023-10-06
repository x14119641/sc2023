<template>
  <div>
    <q-page class="flex flex-center">
      <q-table
              flat bordered
              title="Ticks"
              :rows="rows"
              :columns="columns"
              row-key="tick"
              dark
              color="amber"
            />
      <!-- <p>{{ my_data }}</p> -->
      <p>{{ columns }}</p>
      <p>{{ rows }}</p>
    </q-page>
  </div>
</template>

<script>
export default {
  name: "PingComponent",
  data() {
    return {
      my_data: "",
      columns: "",
      rows: "",
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
          this.rows = res.data;
          // object.rows.map((item) => item.data);
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
  },
  created() {
    this.getData();
    this.build_columns_ticks();
  },
};
</script>
