<template>
  <q-card class="my-card q-ma-md  ">
    <div class="text-h6 text-blue-12"> {{title}}</div>
    <div class="row justify-center text-center">
      <div class="col-10 q-my-md ">
        <q-input 
          color="yellow-8" 
          label-color="blue-12" 
          outlined
          placeholder="Format dd-mm-YYYY hh:mm:ss" 
          v-model="date_input" 
          label="Refreshed Date">
          <template v-slot:append>
            <q-icon name="event" color="deep-orange-6" />
          </template>
        </q-input>
      </div>
    </div>

    <div class="row justify-center text-center">
      <div class="col-10 ">
        <div class="q-mb-md q-gutter-sm">
          <q-btn outline style="color: #8ac926;" label="Tickers" @click="insertTickers()"/>
          <q-btn outline style="color: #1982c4;" label="Metadata" />
          <q-btn outline style="color: #6a4c93;" label="Institutional" @click="beforeInsertInstitutional()"/>
        </div>
      </div>
      
    </div>
  </q-card>
  <q-card class="my-card q-ma-md bg-grey-2">
    <div class="row justify-center text-center">
      <div class="col-12 q-ma-md ">
        <div class="text-h6 q-mx-md text-blue-12 bg-blue-1"> Modal Text</div>
        <div class="q-mx-md q-mt-md bg-blue-2">
          <p>{{msg}}</p>
        </div>
      </div>
    </div>
  </q-card>

  <q-dialog v-model="show_modal">
    <q-card>
      <q-card-section>
        <div class="text-h6">Alert</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        Refreshed date is not inserted, I recommend to use it
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="OK" color="primary" v-close-popup @click="insertInstitutional()"/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>


<script>
export default {
  name: 'AdminComponent',
  data () {
    return {
      title:'Admin',
      rows:'',
      date_input:'',
      show_modal:false,
      msg:''
    }
  },
  methods: {
    insertTickers() {
      const path = 'http://127.0.0.1:5000/api/insert_tickers'

      this.axios.get(path)
          .then((res) => {
              this.msg = res.data;
          })
          .catch((error)=>{console.log(error);
          });
    },

    beforeInsertInstitutional(){
      if (!this.date_input) {
        this.show_modal = true;
      } else {
        this.insertInstitutional()
      }
    },
    insertInstitutional() {
      const path = 'http://127.0.0.1:5000/api/insert_institutional'

      this.axios.post(path, {refreshed_date: this.date_input})
          .then((res) => {
              this.msg = res.data;
              this.rows=res.data;
          })
          .catch((error)=>{console.log(error);
          });
    }
  }
}

// export default {
//     name: 'PingComponent',
//     data() {
//         return {
//             msg:''
//         }        
//     },
//     methods: {
//         getMessage(){
//             const path = 'http://127.0.0.1:5000/ping'

//             this.axios.get(path)
//                 .then((res) => {
//                     this.msg = res.data;
//                 })
//                 .catch((error)=>{console.log(error);
//                 });
//         }
//     },
//     created(){
//         this.getMessage();
//     }
// }
</script>


