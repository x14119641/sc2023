<template>
  <div class="q-ma-md bg-grey-2">
    <p >This is {{ title }} Page</p>
    <div class="row justify-center text-center">
      <div class="col-3 q-my-md bg-grey">Column 1</div>
      <div class="col-3 q-my-md  q-ml-md bg-black text-white">Column 2</div>
      <div class="col-3 q-my-md q-ml-md bg-blue">Column 3</div>
    </div>

    <div class="row justify-center text-center">
      <div class="col-3 q-my-md bg-grey">Column 4</div>
      <div class="col-3 q-my-md  q-ml-md bg-black text-white">Column 5</div>
      <div class="col-3 q-my-md q-ml-md bg-blue">Column 6</div>
    </div>
  </div>
  <div class="q-ma-md bg-grey-2">
    <div class="row justify-center text-center">
      <div class="col-12 q-ma-sm bg-blue-3">HEre goes the modal message
        <div class=" bg-blue-9">
          Inner Box
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminComponent',
  data () {
    return {
      title:'Admin',
      rows:''
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


